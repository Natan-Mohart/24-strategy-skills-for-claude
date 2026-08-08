#!/usr/bin/env python3
"""
Full-Potential Diagnostic calculator: sizes the $ value at stake between
current performance and a top-quartile/best-practice benchmark, metric by
metric, then rolls it into a single "value at stake" number — the core
tool behind McKinsey's "full potential" transformation framing.

Usage:
    python3 full_potential_calc.py --config metrics.json

metrics.json shape:
{
  "revenue_base": 120000000,
  "metrics": [
    {
      "name": "Gross margin %",
      "current_value": 38,
      "benchmark_value": 46,
      "unit": "pct_of_revenue",
      "direction": "higher_is_better"
    },
    {
      "name": "SG&A as % of revenue",
      "current_value": 22,
      "benchmark_value": 16,
      "unit": "pct_of_revenue",
      "direction": "lower_is_better"
    },
    {
      "name": "Inventory turns",
      "current_value": 4.2,
      "benchmark_value": 6.5,
      "unit": "turns",
      "working_capital_base": 18000000,
      "direction": "higher_is_better"
    }
  ]
}
For pct_of_revenue metrics, value at stake = |benchmark - current| % x revenue_base.
For "turns" metrics with a working_capital_base, value at stake is approximated as
the working capital freed by moving current turns to benchmark turns.
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

    revenue = cfg["revenue_base"]
    total_value_at_stake = 0

    print("=== Full-Potential Diagnostic: Value at Stake ===\n")
    print(f"Revenue base: {money(revenue)}\n")
    print(f"{'Metric':<28}{'Current':>10}{'Benchmark':>11}{'Gap':>9}{'Value at Stake':>18}")
    print("-" * 80)

    for m in cfg["metrics"]:
        current = m["current_value"]
        bench = m["benchmark_value"]
        gap = bench - current if m["direction"] == "higher_is_better" else current - bench

        if m["unit"] == "pct_of_revenue":
            value_at_stake = abs(gap) / 100 * revenue
        elif m["unit"] == "turns" and "working_capital_base" in m:
            wc = m["working_capital_base"]
            # working capital roughly scales inversely with turns
            wc_at_benchmark = wc * (current / bench)
            value_at_stake = abs(wc - wc_at_benchmark)
        else:
            value_at_stake = 0

        total_value_at_stake += value_at_stake
        gap_str = f"{gap:+.1f}"
        print(f"{m['name']:<28}{current:>10.1f}{bench:>11.1f}{gap_str:>9}{money(value_at_stake):>18}")

    print("-" * 80)
    print(f"{'TOTAL VALUE AT STAKE':<28}{'':<30}{money(total_value_at_stake):>18}")
    print(f"\nAs % of revenue base: {total_value_at_stake / revenue * 100:.1f}%")
    print("\nNote: this is the theoretical gap to benchmark, not a capture plan.")
    print("Typical full-potential programs capture 40-70% of the identified gap")
    print("within the first 18-24 months — use this number to size ambition, not")
    print("as a guaranteed outcome. Pair with initiative-prioritizer to sequence")
    print("which gaps to close first.")


if __name__ == "__main__":
    main()
