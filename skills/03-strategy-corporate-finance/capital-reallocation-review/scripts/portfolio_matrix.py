#!/usr/bin/env python3
"""
GE-McKinsey 9-box portfolio matrix (industry attractiveness x competitive
strength) — a strict upgrade on the old 2-factor BCG matrix, which collapses
"attractiveness" to growth rate alone and "strength" to relative share alone.

Usage:
    python3 portfolio_matrix.py --config portfolio.json

portfolio.json shape:
{
  "attractiveness_weights": {"market_growth": 0.3, "market_size": 0.2, "profitability": 0.3, "competitive_intensity_inverse": 0.2},
  "strength_weights": {"relative_share": 0.3, "margin_vs_peers": 0.3, "brand_strength": 0.2, "capability_fit": 0.2},
  "business_units": [
    {
      "name": "Core Product",
      "revenue": 40000000,
      "attractiveness_scores": {"market_growth": 6, "market_size": 8, "profitability": 7, "competitive_intensity_inverse": 5},
      "strength_scores": {"relative_share": 8, "margin_vs_peers": 7, "brand_strength": 8, "capability_fit": 9}
    }
  ]
}
Scores are 1-10 per factor. Weights within each axis should sum to 1.0.
"""
import argparse
import json


def weighted_score(scores, weights):
    return sum(scores[k] * weights[k] for k in weights) 


def zone(attractiveness, strength):
    # scores are on a 1-10 scale
    high, mid = 6.7, 3.4
    a = "high" if attractiveness >= high else ("mid" if attractiveness >= mid else "low")
    s = "high" if strength >= high else ("mid" if strength >= mid else "low")
    grid = {
        ("high", "high"): "INVEST/GROW",
        ("high", "mid"): "INVEST/GROW",
        ("mid", "high"): "INVEST/GROW",
        ("high", "low"): "SELECTIVE (build strength or exit)",
        ("mid", "mid"): "SELECTIVE (hold, fund selectively)",
        ("low", "high"): "SELECTIVE (harvest strength, low growth)",
        ("mid", "low"): "HARVEST/DIVEST",
        ("low", "mid"): "HARVEST/DIVEST",
        ("low", "low"): "HARVEST/DIVEST",
    }
    return grid[(a, s)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    aw = cfg["attractiveness_weights"]
    sw = cfg["strength_weights"]
    total_rev = sum(bu["revenue"] for bu in cfg["business_units"])

    print("=== GE-McKinsey 9-Box Portfolio Review ===\n")
    print(f"{'Business Unit':<20}{'Rev Share':>10}{'Attract.':>10}{'Strength':>10}  Zone")
    print("-" * 85)
    results = []
    for bu in cfg["business_units"]:
        a = weighted_score(bu["attractiveness_scores"], aw)
        s = weighted_score(bu["strength_scores"], sw)
        z = zone(a, s)
        rev_share = bu["revenue"] / total_rev * 100
        results.append((bu["name"], rev_share, a, s, z))
        print(f"{bu['name']:<20}{rev_share:>9.1f}%{a:>10.1f}{s:>10.1f}  {z}")

    print("\n=== Portfolio-Level Read ===")
    invest = [r for r in results if "INVEST" in r[4]]
    harvest = [r for r in results if "HARVEST" in r[4]]
    invest_rev = sum(r[1] for r in invest)
    harvest_rev = sum(r[1] for r in harvest)
    print(f"Revenue in INVEST/GROW zone: {invest_rev:.1f}%")
    print(f"Revenue in HARVEST/DIVEST zone: {harvest_rev:.1f}%")
    if harvest_rev > 40:
        print(">>> FLAG: over 40% of revenue sits in harvest/divest zones.")
        print("    The portfolio is over-weighted toward declining positions —")
        print("    capital reallocation toward the invest zone should be a priority.")


if __name__ == "__main__":
    main()
