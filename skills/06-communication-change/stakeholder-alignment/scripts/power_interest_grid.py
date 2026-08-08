#!/usr/bin/env python3
"""
Power-Interest stakeholder grid with a recommended engagement strategy per
quadrant, plus a coalition-math check: does the sum of "power" among
currently-supportive stakeholders actually exceed the power held by
opposed/skeptical stakeholders? A grid with lots of green dots but a
minority of the real power is a false-confidence trap.

Usage:
    python3 power_interest_grid.py --config stakeholders.json

stakeholders.json shape:
{
  "stakeholders": [
    {"name": "CFO", "power_1to5": 5, "interest_1to5": 4, "stance": "skeptical"}
  ]
}
stance: one of "champion", "supportive", "neutral", "skeptical", "opposed"
"""
import argparse
import json


def quadrant(power, interest):
    high = 3.5
    if power >= high and interest >= high:
        return "MANAGE CLOSELY (high power, high interest)"
    if power >= high and interest < high:
        return "KEEP SATISFIED (high power, low interest)"
    if power < high and interest >= high:
        return "KEEP INFORMED (low power, high interest)"
    return "MONITOR (low power, low interest)"


STANCE_SIGN = {"champion": 1, "supportive": 1, "neutral": 0, "skeptical": -1, "opposed": -1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    print("=== Power-Interest Stakeholder Grid ===\n")
    print(f"{'Stakeholder':<20}{'Power':>7}{'Interest':>10}{'Stance':>12}  Quadrant")
    print("-" * 90)
    supportive_power = 0
    opposed_power = 0
    for s in cfg["stakeholders"]:
        q = quadrant(s["power_1to5"], s["interest_1to5"])
        print(f"{s['name']:<20}{s['power_1to5']:>7}{s['interest_1to5']:>10}{s['stance']:>12}  {q}")
        sign = STANCE_SIGN.get(s["stance"], 0)
        if sign > 0:
            supportive_power += s["power_1to5"]
        elif sign < 0:
            opposed_power += s["power_1to5"]

    print("\n=== Coalition Math ===")
    print(f"Total power among supportive/champion stakeholders: {supportive_power}")
    print(f"Total power among skeptical/opposed stakeholders:   {opposed_power}")
    if opposed_power >= supportive_power:
        print(">>> FLAG: opposed/skeptical power meets or exceeds supportive power.")
        print("    Having more supportive NAMES doesn't matter if they don't carry")
        print("    more actual POWER. This needs a deliberate coalition-building plan")
        print("    for the highest-power skeptical/opposed stakeholders before")
        print("    proceeding — not just broader 'stakeholder communication.'")
    else:
        print("Supportive coalition currently holds more power than opposition —")
        print("still worth a specific plan for the highest-power skeptics individually.")

    print("\n=== Engagement Strategy by Quadrant ===")
    print("MANAGE CLOSELY : involve directly in decisions, address concerns personally.")
    print("KEEP SATISFIED : minimal detail, but don't surprise them — they can block")
    print("                 even with low day-to-day interest if provoked.")
    print("KEEP INFORMED  : regular updates; they can become advocates if engaged well.")
    print("MONITOR        : light-touch, periodic check-in only.")


if __name__ == "__main__":
    main()
