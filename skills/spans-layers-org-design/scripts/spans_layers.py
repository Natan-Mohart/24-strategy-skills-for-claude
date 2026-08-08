#!/usr/bin/env python3
"""
Spans & Layers calculator: measures average span of control by management
layer, flags layers with an inefficiently narrow span against a benchmark,
and prices the annual cost of carrying more layers than the benchmark
organization design would need.

Usage:
    python3 spans_layers.py --config org.json

org.json shape:
{
  "benchmark_span_by_layer_type": {"executive": 5, "middle_management": 6, "frontline_management": 8},
  "avg_fully_loaded_manager_cost": 145000,
  "layers": [
    {"layer_number": 1, "title": "C-suite", "layer_type": "executive", "manager_count": 1, "direct_reports": 6},
    {"layer_number": 2, "title": "VPs", "layer_type": "executive", "manager_count": 6, "direct_reports": 22},
    {"layer_number": 3, "title": "Directors", "layer_type": "middle_management", "manager_count": 22, "direct_reports": 68},
    {"layer_number": 4, "title": "Managers", "layer_type": "middle_management", "manager_count": 68, "direct_reports": 210},
    {"layer_number": 5, "title": "Team leads", "layer_type": "frontline_management", "manager_count": 90, "direct_reports": 340}
  ]
}
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

    benchmarks = cfg["benchmark_span_by_layer_type"]
    manager_cost = cfg["avg_fully_loaded_manager_cost"]
    layers = cfg["layers"]

    total_managers = sum(l["manager_count"] for l in layers)
    total_ics = layers[-1]["direct_reports"] if layers else 0

    print("=== Spans & Layers Analysis ===\n")
    print(f"{'Layer':<6}{'Title':<18}{'Managers':>10}{'Reports':>10}{'Avg Span':>10}{'Benchmark':>11}{'Read':>14}")
    print("-" * 85)

    total_excess_managers = 0
    for l in layers:
        span = l["direct_reports"] / l["manager_count"] if l["manager_count"] else 0
        bench = benchmarks.get(l["layer_type"], 6)
        read = "OK" if span >= bench * 0.85 else "NARROW"
        print(f"{l['layer_number']:<6}{l['title']:<18}{l['manager_count']:>10}{l['direct_reports']:>10}"
              f"{span:>10.1f}{bench:>11}{read:>14}")
        if span < bench:
            # managers needed at benchmark span vs actual managers = excess
            managers_needed_at_benchmark = l["direct_reports"] / bench
            excess = l["manager_count"] - managers_needed_at_benchmark
            if excess > 0:
                total_excess_managers += excess

    print(f"\nTotal managers across all layers: {total_managers}")
    print(f"Total layers: {len(layers)}")
    print(f"Total individual contributors (below lowest layer): {total_ics}")

    annual_cost_of_excess = total_excess_managers * manager_cost
    print(f"\nEstimated excess management positions (actual vs. benchmark span): {total_excess_managers:.1f}")
    print(f"Estimated annual cost of excess layers: {money(annual_cost_of_excess)}")

    narrow_layers = [l for l in layers if (l["direct_reports"] / l["manager_count"] if l["manager_count"] else 0) < benchmarks.get(l["layer_type"], 6) * 0.85]
    if narrow_layers:
        print(f"\n>>> FLAG: {len(narrow_layers)} layer(s) have spans meaningfully narrower than")
        print("    benchmark. This usually means either genuine complexity that justifies")
        print("    closer supervision, or organizational layering added for reasons other")
        print("    than actual span requirements (legacy structure, title inflation, avoiding")
        print("    a difficult consolidation conversation). Confirm which before acting.")
    else:
        print("\nNo layers flagged as meaningfully narrow versus benchmark.")


if __name__ == "__main__":
    main()
