#!/usr/bin/env python3
"""
M&A synergy case calculator: models cost + revenue synergies against a
realistic ramp curve (synergies rarely arrive day 1), nets out one-time
integration costs, and computes NPV of the synergy case specifically —
separate from the standalone deal economics, which is where most synergy
cases get inflated.

Usage:
    python3 synergy_case.py --config synergies.json

synergies.json shape:
{
  "discount_rate_pct": 10,
  "years": 4,
  "cost_synergies": {
    "run_rate_annual_value": 15000000,
    "ramp_pct_by_year": [30, 70, 100, 100]
  },
  "revenue_synergies": {
    "run_rate_annual_value": 8000000,
    "ramp_pct_by_year": [10, 35, 70, 100],
    "confidence_haircut_pct": 50
  },
  "integration_costs": {
    "one_time_costs_by_year": [12000000, 4000000, 1000000, 0]
  }
}
confidence_haircut_pct on revenue synergies reflects that revenue synergies
are historically far less reliable than cost synergies (harder to control,
easier to attribute to something else) — cost synergies default to no
haircut since they're the more controllable, historically more reliable
category, but you can add one if there's specific reason to.
"""
import argparse
import json


def npv(flows, rate_pct):
    r = rate_pct / 100
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(flows))


def money(x):
    return f"${x:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    years = cfg["years"]
    rate = cfg["discount_rate_pct"]

    cs = cfg["cost_synergies"]
    cost_flows_gross = [cs["run_rate_annual_value"] * cs["ramp_pct_by_year"][y] / 100 for y in range(years)]

    rs = cfg.get("revenue_synergies")
    haircut = rs.get("confidence_haircut_pct", 0) / 100 if rs else 0
    rev_flows_gross = (
        [rs["run_rate_annual_value"] * rs["ramp_pct_by_year"][y] / 100 for y in range(years)]
        if rs else [0] * years
    )
    rev_flows_haircut = [f * (1 - haircut) for f in rev_flows_gross]

    ic = cfg.get("integration_costs", {}).get("one_time_costs_by_year", [0] * years)

    net_flows = [
        cost_flows_gross[y] + rev_flows_haircut[y] - ic[y]
        for y in range(years)
    ]

    print("=== M&A Synergy Case ===\n")
    print(f"{'Year':<6}{'Cost Syn.':>14}{'Rev Syn (gross)':>18}{'Rev Syn (haircut)':>19}{'Integ. Cost':>14}{'Net':>14}")
    print("-" * 90)
    for y in range(years):
        print(f"{y+1:<6}{cost_flows_gross[y]:>14,.0f}{rev_flows_gross[y]:>18,.0f}"
              f"{rev_flows_haircut[y]:>19,.0f}{ic[y]:>14,.0f}{net_flows[y]:>14,.0f}")

    total_net_synergy_npv = npv(net_flows, rate)
    total_cost_synergy_npv = npv(cost_flows_gross, rate)
    total_rev_synergy_npv = npv(rev_flows_haircut, rate)
    total_integration_cost_npv = npv(ic, rate)

    print("-" * 90)
    print(f"\nNPV of cost synergies:              {money(total_cost_synergy_npv)}")
    print(f"NPV of revenue synergies (haircut {haircut*100:.0f}%): {money(total_rev_synergy_npv)}")
    print(f"NPV of integration costs:           -{money(total_integration_cost_npv)}")
    print(f"NET SYNERGY CASE NPV:                {money(total_net_synergy_npv)}")

    if rs and haircut < 0.3:
        print(f"\n>>> NOTE: revenue synergy haircut is only {haircut*100:.0f}%. Historically,")
        print("    revenue synergies are realized far less reliably than cost synergies")
        print("    (harder to isolate from baseline growth, dependent on customer/market")
        print("    behavior outside management's direct control). Confirm this haircut")
        print("    is evidence-based, not just optimism carried over from deal advocacy.")

    cost_share = total_cost_synergy_npv / (total_cost_synergy_npv + total_rev_synergy_npv) * 100 \
        if (total_cost_synergy_npv + total_rev_synergy_npv) != 0 else 0
    print(f"\nCost synergies are {cost_share:.0f}% of total synergy NPV (post-haircut).")
    print("A deal case leaning heavily on revenue synergies carries materially more")
    print("execution risk than one anchored in cost synergies — size confidence accordingly.")


if __name__ == "__main__":
    main()
