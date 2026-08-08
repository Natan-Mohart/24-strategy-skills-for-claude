#!/usr/bin/env python3
"""
Driver-based business case: NPV, IRR, payback, and a sensitivity table.

Usage:
    python3 npv_case.py --config case.json

case.json shape:
{
  "discount_rate_pct": 10,
  "initial_investment": 2000000,
  "years": [
    {"revenue": 800000, "cogs_pct": 40, "opex": 300000},
    {"revenue": 1800000, "cogs_pct": 38, "opex": 400000},
    {"revenue": 3200000, "cogs_pct": 35, "opex": 550000},
    {"revenue": 4500000, "cogs_pct": 33, "opex": 700000},
    {"revenue": 5600000, "cogs_pct": 32, "opex": 800000}
  ],
  "sensitivity": {
    "revenue_swing_pct": [-20, -10, 0, 10, 20],
    "discount_rate_swing_pts": [-2, -1, 0, 1, 2]
  }
}

Prints annual cash flows, NPV, IRR (bisection method, no numpy dependency),
payback period, and a revenue x discount-rate NPV sensitivity grid — the
part most hand-built "business cases" skip because it's tedious by hand.
"""
import argparse
import json


def cashflows(cfg, revenue_multiplier=1.0):
    flows = [-cfg["initial_investment"]]
    for y in cfg["years"]:
        rev = y["revenue"] * revenue_multiplier
        gross_profit = rev * (1 - y["cogs_pct"] / 100)
        cf = gross_profit - y["opex"]
        flows.append(cf)
    return flows


def npv(flows, rate_pct):
    r = rate_pct / 100
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(flows))


def irr(flows, lo=-0.99, hi=5.0, tol=1e-6, max_iter=200):
    def f(rate):
        return sum(cf / ((1 + rate) ** t) for t, cf in enumerate(flows))
    f_lo, f_hi = f(lo), f(hi)
    if f_lo * f_hi > 0:
        return None  # no sign change in range -> no IRR found
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        f_mid = f(mid)
        if abs(f_mid) < tol:
            return mid * 100
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return mid * 100


def payback_period(flows):
    cumulative = 0
    for t, cf in enumerate(flows):
        cumulative += cf
        if cumulative >= 0:
            if t == 0:
                return 0
            prior_cumulative = cumulative - cf
            fraction = -prior_cumulative / cf if cf != 0 else 0
            return (t - 1) + fraction
    return None  # never pays back within modeled years


def money(x):
    return f"${x:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    base_flows = cashflows(cfg)
    base_npv = npv(base_flows, cfg["discount_rate_pct"])
    base_irr = irr(base_flows)
    pb = payback_period(base_flows)

    print("=== Business Case: Base Case ===\n")
    print("Year 0:", money(base_flows[0]))
    for i, cf in enumerate(base_flows[1:], start=1):
        print(f"Year {i}: {money(cf)}")
    print(f"\nDiscount rate: {cfg['discount_rate_pct']}%")
    print(f"NPV: {money(base_npv)}")
    print(f"IRR: {base_irr:.1f}%" if base_irr is not None else "IRR: not found in range (check sign of cash flows)")
    print(f"Payback: {pb:.1f} years" if pb is not None else "Payback: does not pay back within modeled years")

    sens = cfg.get("sensitivity")
    if sens:
        print("\n=== NPV Sensitivity Grid ===")
        rev_swings = sens["revenue_swing_pct"]
        rate_swings = sens["discount_rate_swing_pts"]
        header = "Revenue \\ Rate".ljust(16) + "".join(
            f"{cfg['discount_rate_pct']+r:>12}%" for r in rate_swings
        )
        print(header)
        for rs in rev_swings:
            row_label = f"{rs:+d}%".ljust(16)
            row = row_label
            flows = cashflows(cfg, revenue_multiplier=1 + rs / 100)
            for rr in rate_swings:
                val = npv(flows, cfg["discount_rate_pct"] + rr)
                row += f"{val:>13,.0f}"
            print(row)
        print("\nRead: rows = revenue vs. plan, columns = discount rate vs. base.")
        print("Use this to name the conditions under which the case still holds.")


if __name__ == "__main__":
    main()
