#!/usr/bin/env python3
"""
Triangulated market sizing (TAM/SAM/SOM) with top-down vs. bottom-up cross-check.

Usage:
    python3 tam_sam_som.py --config market.json

market.json shape:
{
  "top_down": {"total_population": 5000000, "target_share_pct": 12, "avg_annual_spend": 4800},
  "bottom_up": {"units_or_customers": 45000, "avg_annual_revenue_per_customer": 6200},
  "serviceable_filters": {"pct_geography": 70, "pct_segment_fit": 55, "pct_regulatory_eligible": 90},
  "obtainable": {"realistic_share_of_sam_pct": 8, "years_to_reach": 3}
}

Prints TAM (two independent estimates + variance), SAM, SOM, and flags if the
top-down and bottom-up TAM estimates disagree by more than 30% (a signal the
inputs need to be revisited before anyone puts the number in a deck).
"""
import argparse
import json


def money(x):
    return f"${x:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    td = cfg["top_down"]
    tam_top_down = td["total_population"] * (td["target_share_pct"] / 100) * td["avg_annual_spend"]

    bu = cfg["bottom_up"]
    tam_bottom_up = bu["units_or_customers"] * bu["avg_annual_revenue_per_customer"]

    variance_pct = abs(tam_top_down - tam_bottom_up) / max(tam_top_down, tam_bottom_up) * 100

    tam_reconciled = (tam_top_down + tam_bottom_up) / 2

    filt = cfg["serviceable_filters"]
    sam = tam_reconciled
    for _, pct in filt.items():
        sam *= pct / 100

    ob = cfg["obtainable"]
    som = sam * (ob["realistic_share_of_sam_pct"] / 100)

    print("=== Market Sizing: TAM / SAM / SOM ===\n")
    print(f"TAM (top-down):    {money(tam_top_down)}")
    print(f"TAM (bottom-up):   {money(tam_bottom_up)}")
    print(f"Variance:          {variance_pct:.1f}%")
    if variance_pct > 30:
        print("  >>> FLAG: top-down and bottom-up disagree by more than 30%.")
        print("      Do not present a single TAM number yet — the two methods are")
        print("      built on inconsistent assumptions about population, spend, or")
        print("      fit. Reconcile the inputs before this goes in a deck.")
    print(f"TAM (reconciled, avg): {money(tam_reconciled)}\n")

    print(f"SAM (after serviceability filters {', '.join(f'{k}={v}%' for k, v in filt.items())}):")
    print(f"  {money(sam)}\n")

    print(f"SOM (realistic {ob['realistic_share_of_sam_pct']}% share of SAM over {ob['years_to_reach']} years):")
    print(f"  {money(som)}")
    print(f"  Implied annual run-rate to reach SOM: {money(som / ob['years_to_reach'])}/year")


if __name__ == "__main__":
    main()
