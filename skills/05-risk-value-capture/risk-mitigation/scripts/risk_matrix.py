#!/usr/bin/env python3
"""
Risk register scorer: likelihood x impact matrix with a velocity factor
(how fast the risk could materialize), which a plain 2-factor heat map
misses — a slow-brewing catastrophic risk and a fast-moving one with the
same likelihood x impact score need very different monitoring cadences.

Usage:
    python3 risk_matrix.py --config risks.json

risks.json shape:
{
  "risks": [
    {
      "name": "Key supplier concentration",
      "likelihood_1to5": 3,
      "impact_1to5": 5,
      "velocity_1to5": 2,
      "current_mitigation": "Single backup supplier identified, not yet contracted"
    }
  ]
}
velocity_1to5: 1 = years to materialize, 5 = could hit within weeks.
"""
import argparse
import json


def priority_tier(score, velocity):
    if score >= 20 or (score >= 15 and velocity >= 4):
        return "CRITICAL - active mitigation now"
    if score >= 12:
        return "HIGH - mitigation plan required"
    if score >= 6:
        return "MODERATE - monitor, contingency plan"
    return "LOW - accept, periodic review"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    results = []
    for r in cfg["risks"]:
        score = r["likelihood_1to5"] * r["impact_1to5"]
        tier = priority_tier(score, r["velocity_1to5"])
        results.append((r["name"], r["likelihood_1to5"], r["impact_1to5"],
                         r["velocity_1to5"], score, tier, r.get("current_mitigation", "")))

    results.sort(key=lambda r: r[4], reverse=True)

    print("=== Risk Register: Likelihood x Impact x Velocity ===\n")
    print(f"{'Risk':<32}{'L':>3}{'I':>3}{'V':>3}{'Score':>7}  Tier")
    print("-" * 95)
    for name, l, i, v, score, tier, mit in results:
        print(f"{name:<32}{l:>3}{i:>3}{v:>3}{score:>7}  {tier}")

    critical = [r for r in results if "CRITICAL" in r[5]]
    unmitigated_critical = [r for r in critical if not r[6].strip()]
    if unmitigated_critical:
        print(f"\n>>> FLAG: {len(unmitigated_critical)} CRITICAL risk(s) have no")
        print("    documented current mitigation. These need an owner and a plan")
        print("    before anything else on this register.")
        for r in unmitigated_critical:
            print(f"      - {r[0]}")

    high_velocity_moderate_score = [r for r in results if r[3] >= 4 and 6 <= r[4] < 12]
    if high_velocity_moderate_score:
        print(f"\n>>> NOTE: risk(s) with moderate score but high velocity — a static")
        print("    heat map would rank these lower than they deserve, since they can")
        print("    materialize fast even if their expected impact score looks middling:")
        for r in high_velocity_moderate_score:
            print(f"      - {r[0]} (score {r[4]}, velocity {r[3]}/5)")


if __name__ == "__main__":
    main()
