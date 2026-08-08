#!/usr/bin/env python3
"""
Pricing calculator: Van Westendorp Price Sensitivity Meter analysis +
simple price elasticity revenue/margin optimizer.

Usage:
    python3 pricing_calculator.py --config pricing.json

pricing.json shape:
{
  "van_westendorp": {
    "too_cheap":   [10, 12, 15, 9, 11, 14, 13, 10, 12, 8],
    "cheap":       [20, 22, 25, 19, 21, 24, 23, 20, 22, 18],
    "expensive":   [35, 38, 40, 33, 36, 39, 37, 34, 38, 32],
    "too_expensive": [50, 55, 58, 48, 52, 56, 54, 49, 53, 47]
  },
  "elasticity": {
    "current_price": 29,
    "current_volume": 1000,
    "elasticity_coefficient": -1.8,
    "unit_cost": 9,
    "price_test_range": [19, 24, 29, 34, 39, 44]
  }
}

elasticity_coefficient is %change in volume / %change in price (negative,
typically -0.5 to -3 depending on category). If you don't have an estimated
coefficient, run a real price test before trusting this section.
"""
import argparse
import json
import statistics


def van_westendorp(vw):
    """
    Approximate the four VW curves using the median of each response set as
    a simple proxy for the crossing points (a lightweight version of the
    full cumulative-distribution method used in a dedicated survey tool).
    """
    too_cheap = statistics.median(vw["too_cheap"])
    cheap = statistics.median(vw["cheap"])
    expensive = statistics.median(vw["expensive"])
    too_expensive = statistics.median(vw["too_expensive"])

    # Point of Marginal Cheapness ~ where too_cheap crosses expensive
    pmc = (too_cheap + expensive) / 2
    # Point of Marginal Expensiveness ~ where cheap crosses too_expensive
    pme = (cheap + too_expensive) / 2
    # Optimal Price Point ~ where too_cheap crosses too_expensive
    opp = (too_cheap + too_expensive) / 2
    # Indifference Price Point ~ where cheap crosses expensive
    ipp = (cheap + expensive) / 2

    return pmc, pme, opp, ipp


def elasticity_table(el):
    p0 = el["current_price"]
    q0 = el["current_volume"]
    e = el["elasticity_coefficient"]
    cost = el["unit_cost"]
    rows = []
    for p1 in el["price_test_range"]:
        pct_price_change = (p1 - p0) / p0
        pct_volume_change = e * pct_price_change
        q1 = q0 * (1 + pct_volume_change)
        revenue = p1 * q1
        margin = (p1 - cost) * q1
        rows.append((p1, q1, revenue, margin))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    if "van_westendorp" in cfg:
        vw = cfg["van_westendorp"]
        n = len(vw["too_cheap"])
        pmc, pme, opp, ipp = van_westendorp(vw)
        print("=== Van Westendorp Price Sensitivity (n={}) ===\n".format(n))
        print(f"Point of Marginal Cheapness (floor, below = quality doubt): ${pmc:.2f}")
        print(f"Optimal Price Point (most acceptable):                      ${opp:.2f}")
        print(f"Indifference Price Point (neutral median):                  ${ipp:.2f}")
        print(f"Point of Marginal Expensiveness (ceiling, above = too costly): ${pme:.2f}")
        print(f"\nAcceptable price range: ${pmc:.2f} - ${pme:.2f}")
        print("Note: this uses median-crossing approximation, not full cumulative")
        print("distributions. For a launch-critical decision, validate with the full")
        print("survey method (n=100+) before finalizing.\n")

    if "elasticity" in cfg:
        el = cfg["elasticity"]
        rows = elasticity_table(el)
        print("=== Price Elasticity: Revenue & Margin by Price Point ===\n")
        print(f"{'Price':>8}{'Volume':>10}{'Revenue':>14}{'Margin':>14}")
        best_rev = max(rows, key=lambda r: r[2])
        best_margin = max(rows, key=lambda r: r[3])
        for p1, q1, revenue, margin in rows:
            flag = ""
            if p1 == best_rev[0]:
                flag += "  <- max revenue"
            if p1 == best_margin[0]:
                flag += "  <- max margin"
            print(f"${p1:>7.2f}{q1:>10.0f}${revenue:>12,.0f}${margin:>12,.0f}{flag}")
        print(f"\nElasticity coefficient used: {el['elasticity_coefficient']} "
              f"({'elastic' if el['elasticity_coefficient'] < -1 else 'inelastic'})")


if __name__ == "__main__":
    main()
