#!/usr/bin/env python3
"""
Decision-tree expected value calculator for scenario/war-gaming analysis.
Handles a decision node followed by chance nodes (competitor/market response
scenarios) with probabilities and payoffs, computing EV per initial choice
and flagging the choice with the best worst-case (maximin) if it differs
from the best-EV choice.

Usage:
    python3 decision_tree_ev.py --config scenarios.json

scenarios.json shape:
{
  "options": [
    {
      "name": "Aggressive price cut",
      "scenarios": [
        {"name": "Competitor matches", "probability": 0.5, "payoff": -200000},
        {"name": "Competitor holds", "probability": 0.3, "payoff": 900000},
        {"name": "Competitor exits segment", "probability": 0.2, "payoff": 1500000}
      ]
    }
  ]
}
Probabilities within an option's scenarios must sum to 1.0 (+/- 0.01).
"""
import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    print("=== Decision Tree: Expected Value by Option ===\n")
    results = []
    for opt in cfg["options"]:
        probs = [s["probability"] for s in opt["scenarios"]]
        p_sum = sum(probs)
        if abs(p_sum - 1.0) > 0.01:
            print(f"  >>> WARNING: '{opt['name']}' scenario probabilities sum to "
                  f"{p_sum:.2f}, not 1.0 — fix before trusting this EV.")
        ev = sum(s["probability"] * s["payoff"] for s in opt["scenarios"])
        worst_case = min(s["payoff"] for s in opt["scenarios"])
        best_case = max(s["payoff"] for s in opt["scenarios"])
        results.append((opt["name"], ev, worst_case, best_case, opt["scenarios"]))

    print(f"{'Option':<28}{'EV':>14}{'Worst case':>14}{'Best case':>14}")
    print("-" * 70)
    for name, ev, worst, best, _ in results:
        print(f"{name:<28}{ev:>14,.0f}{worst:>14,.0f}{best:>14,.0f}")

    best_ev = max(results, key=lambda r: r[1])
    best_worst_case = max(results, key=lambda r: r[2])

    print(f"\nHighest expected value: {best_ev[0]} (EV = {best_ev[1]:,.0f})")
    print(f"Best worst-case (maximin, most defensible if you're risk-averse "
          f"or can't survive the downside): {best_worst_case[0]} "
          f"(worst case = {best_worst_case[2]:,.0f})")

    if best_ev[0] != best_worst_case[0]:
        print(f"\n>>> FLAG: the EV-maximizing option and the maximin (safest-downside)")
        print(f"    option are different choices. If the worst case of '{best_ev[0]}'")
        print(f"    ({best_ev[2]:,.0f}) is something the business could not actually")
        print(f"    survive, expected value alone is the wrong decision criterion here —")
        print(f"    this needs an explicit risk-tolerance conversation, not a silent")
        print(f"    default to the highest-EV row.")

    print("\n=== Scenario Detail ===")
    for name, ev, worst, best, scenarios in results:
        print(f"\n{name}:")
        for s in scenarios:
            print(f"  {s['name']:<28} p={s['probability']:.2f}  payoff={s['payoff']:>12,.0f}")


if __name__ == "__main__":
    main()
