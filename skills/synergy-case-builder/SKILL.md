---
name: synergy-case-builder
description: Models M&A or partnership synergies with a bundled calculator that ramps cost and revenue synergies realistically over time, applies a confidence haircut to revenue synergies (historically far less reliable than cost synergies), and nets out integration costs to a true synergy-case NPV. Use whenever the user is building or reviewing a deal case, needs to size expected synergies from an acquisition or partnership, or has a synergy number that's presented as available immediately at full run-rate with no ramp, no haircut, and no integration cost netted out.
---

# Synergy Case Builder

## When to use
Use whenever a deal, merger, or major partnership needs its synergy case built or stress-tested — especially replacing a synergy number presented as a single figure available immediately, with no distinction between cost and revenue synergies, no ramp curve, and no integration cost netted against it. Synergy overstatement is one of the most common and best-documented causes of value destruction in M&A, and almost always traces back to exactly these three omissions.

## What it does
Separately models cost synergies (headcount, procurement, facilities — generally more controllable and historically more reliably captured) and revenue synergies (cross-sell, pricing power, channel access — historically captured at a much lower rate, since they depend on customer and market behavior outside management's direct control), ramps both realistically over multiple years rather than assuming immediate full run-rate, applies an explicit confidence haircut to revenue synergies, and nets integration costs to produce a true synergy-case NPV via a bundled calculator.

## Method
1. **Separate cost synergies from revenue synergies from the start** — never present a single blended synergy number, since the two categories have very different reliability and deserve very different scrutiny.
2. **Estimate run-rate annual value for each category** once fully phased in, built bottom-up from specific line items (headcount overlap by function, specific procurement categories, named cross-sell opportunities) — not a top-down "X% of combined revenue" rule of thumb.
3. **Build a realistic ramp curve for each category** — cost synergies typically ramp faster (often 50-70% captured within year one to two once headcount/procurement actions are taken) while revenue synergies typically ramp much slower (often minimal in year one, only reaching meaningful scale by year three or later, since new commercial motions take time to build).
4. **Apply an explicit confidence haircut to revenue synergies** — reflecting that revenue synergies are the category most often overstated in deal advocacy, since they're harder to isolate from organic growth that would have happened anyway and harder to attribute cleanly after the fact. A haircut below 30-40% deserves specific justification, not a default assumption of full realization.
5. **Estimate one-time integration costs by year** — severance, systems consolidation, rebranding, advisor fees — and net these against the gross synergy flows, since a synergy case that ignores its own cost of capture materially overstates the deal's actual economics.
6. **Run the bundled calculator** (`scripts/synergy_case.py`) to get the year-by-year net synergy flow, NPV by category, and net synergy-case NPV.
7. **Check the cost-vs-revenue synergy mix**: a synergy case leaning heavily on revenue synergies (post-haircut) carries materially more execution risk than one anchored primarily in cost synergies — flag this explicitly to the deal team and size confidence in the overall deal case accordingly, not just the synergy line.
8. **Feed the net synergy-case NPV into the overall deal's business case** (alongside standalone deal economics) rather than letting the synergy number silently inflate the headline deal rationale without its own scrutiny.

## Inputs
- Cost synergy run-rate estimate, built from specific line items
- Revenue synergy run-rate estimate, built from specific named opportunities
- Realistic ramp percentages by year for each category
- Confidence haircut for revenue synergies, with justification
- One-time integration costs by year
- Config saved as JSON matching the format documented at the top of `scripts/synergy_case.py`

## Output format
Year-by-year table of gross cost synergies, gross and haircut-adjusted revenue synergies, integration costs, and net flow; NPV by category and net synergy-case NPV; explicit flag if the revenue-synergy haircut looks too low; cost-vs-revenue synergy mix with an execution-risk read.

## Example
A deal advocacy presentation claims $23M in "day-one" synergies. Rebuilding the case with a realistic ramp and a 50% haircut on the revenue synergy component shows the net synergy-case NPV is $28.2M over four years — a real number, but one that only becomes visible once integration costs are netted out and the revenue synergies are appropriately discounted for their historical unreliability; the raw undiscounted, unhaircut run-rate figure would have materially overstated what the deal is actually worth in year one.

## Common pitfalls
- Presenting synergies as available at full run-rate from day one, ignoring both the realistic ramp and the integration cost required to get there.
- Applying the same confidence level to revenue synergies as to cost synergies, when the two categories have very different historical realization rates.
- Never netting one-time integration costs against the gross synergy value, overstating the deal's true near-term economics.
