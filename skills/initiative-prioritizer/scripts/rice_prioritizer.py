#!/usr/bin/env python3
"""
RICE prioritization (Reach x Impact x Confidence / Effort) plus a
cost-of-delay overlay, since RICE alone ignores urgency/sequencing.

Usage:
    python3 rice_prioritizer.py --config initiatives.json

initiatives.json shape:
{
  "initiatives": [
    {
      "name": "Onboarding redesign",
      "reach": 8000,
      "impact": 2,
      "confidence_pct": 80,
      "effort_person_weeks": 6,
      "monthly_value_if_delayed": 15000
    }
  ]
}
impact scale: 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal (standard RICE scale)
"""
import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    results = []
    for it in cfg["initiatives"]:
        rice = (it["reach"] * it["impact"] * (it["confidence_pct"] / 100)) / it["effort_person_weeks"]
        cod = it.get("monthly_value_if_delayed", 0)
        cd3 = cod * 3  # cost of a 3-month delay, a common sequencing lens
        results.append((it["name"], rice, it["effort_person_weeks"], cod, cd3))

    results.sort(key=lambda r: r[1], reverse=True)

    print("=== RICE Prioritization ===\n")
    print(f"{'Initiative':<28}{'RICE':>10}{'Effort(wk)':>12}{'CoD/mo':>12}{'CoD 3mo':>12}")
    print("-" * 76)
    for name, rice, effort, cod, cd3 in results:
        print(f"{name:<28}{rice:>10.1f}{effort:>12}{cod:>12,.0f}{cd3:>12,.0f}")

    print("\nRICE ranks by expected impact per unit of effort — it does NOT account")
    print("for urgency. Cross-check: an initiative with a lower RICE score but a high")
    print("cost of delay (e.g., a closing market window, a compliance deadline) may")
    print("still need to be sequenced earlier. Don't apply the RICE rank mechanically")
    print("without checking the CoD column against the calendar.")

    high_cod_low_rice = [r for r in results if r[3] > 0]
    high_cod_low_rice.sort(key=lambda r: r[3], reverse=True)
    if len(results) > 1:
        top_rice_name = results[0][0]
        top_cod_name = high_cod_low_rice[0][0] if high_cod_low_rice else None
        if top_cod_name and top_cod_name != top_rice_name:
            print(f"\n>>> FLAG: '{top_cod_name}' has the highest cost of delay but is not")
            print(f"    the top RICE-ranked item ('{top_rice_name}' is). Confirm the")
            print("    sequencing call explicitly rather than defaulting to RICE order.")


if __name__ == "__main__":
    main()
