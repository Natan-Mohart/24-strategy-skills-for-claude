#!/usr/bin/env python3
"""
Unit economics health check: LTV, LTV:CAC ratio, CAC payback period, and a
cohort-decay-aware LTV calculation (not the naive "ARPU / churn" shortcut,
which overstates LTV whenever churn is front-loaded, as it usually is).

Usage:
    python3 unit_economics.py --config unit_econ.json

unit_econ.json shape:
{
  "cac": 450,
  "monthly_revenue_per_customer": 80,
  "gross_margin_pct": 75,
  "monthly_churn_pct_by_month": [8, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3],
  "discount_rate_annual_pct": 12
}
monthly_churn_pct_by_month lets churn decay realistically over the first
year (most businesses lose new customers faster than mature ones) instead
of assuming one flat churn rate forever, which is the most common way LTV
gets overstated.
"""
import argparse
import json


def money(x):
    return f"${x:,.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    cac = cfg["cac"]
    rev = cfg["monthly_revenue_per_customer"]
    margin = cfg["gross_margin_pct"] / 100
    churn_by_month = cfg["monthly_churn_pct_by_month"]
    monthly_discount = (cfg.get("discount_rate_annual_pct", 10) / 100) / 12

    survival = 1.0
    cum_margin = 0
    cum_margin_undiscounted = 0
    payback_month = None
    cac_recovered = 0

    print("=== Unit Economics Health Check ===\n")
    print(f"{'Month':<7}{'Survival %':>12}{'Margin $':>12}{'Cum Margin $':>15}")
    print("-" * 50)
    for m, churn_pct in enumerate(churn_by_month, start=1):
        if m > 1:
            survival *= (1 - churn_by_month[m - 2] / 100)
        month_margin = rev * margin * survival
        cum_margin_undiscounted += month_margin
        cum_margin += month_margin / ((1 + monthly_discount) ** m)
        cac_recovered += month_margin
        if payback_month is None and cac_recovered >= cac:
            payback_month = m
        print(f"{m:<7}{survival*100:>11.1f}%{money(month_margin):>12}{money(cum_margin_undiscounted):>15}")

    # extend LTV tail at final churn rate to a reasonable horizon (36 months total)
    final_churn = churn_by_month[-1] / 100
    for m in range(len(churn_by_month) + 1, 37):
        survival *= (1 - final_churn)
        month_margin = rev * margin * survival
        cum_margin += month_margin / ((1 + monthly_discount) ** m)
        cum_margin_undiscounted += month_margin
        cac_recovered += month_margin
        if payback_month is None and cac_recovered >= cac:
            payback_month = m

    ltv_cac = cum_margin / cac

    print("\n=== Summary (36-month horizon, discounted) ===")
    print(f"CAC:                          {money(cac)}")
    print(f"LTV (discounted contribution margin): {money(cum_margin)}")
    print(f"LTV:CAC ratio:                {ltv_cac:.2f}")
    print(f"CAC payback period:           {payback_month if payback_month else '36+'} months")

    print("\n=== Health Read ===")
    if ltv_cac >= 3:
        print(f"LTV:CAC of {ltv_cac:.1f} is in the healthy range (>=3 is the common benchmark).")
    elif ltv_cac >= 1.5:
        print(f"LTV:CAC of {ltv_cac:.1f} is marginal. Growth is likely destroying value per")
        print("customer acquired even though revenue is growing. Investigate CAC or retention.")
    else:
        print(f"LTV:CAC of {ltv_cac:.1f} is below 1.5. Acquiring customers at this rate is")
        print("likely destroying value. This is a stop-and-fix signal, not a scale signal.")

    if payback_month and payback_month > 18:
        print(f"\n>>> FLAG: {payback_month}-month payback is long. Growth at this payback")
        print("    period requires either a lot of cash runway or outside financing to fund")
        print("    the gap between spending on CAC and recovering it.")


if __name__ == "__main__":
    main()
