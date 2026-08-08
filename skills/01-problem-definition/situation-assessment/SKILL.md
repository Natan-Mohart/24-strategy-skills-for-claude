---
name: situation-assessment
description: Runs the full day-1-to-diagnosis arc of a real strategy engagement — a MECE hypothesis tree built before any data is pulled, then three-lens fact triangulation that proves or kills each hypothesis, with every finding tagged fact/inference/unknown and a workplan naming who closes the open questions. Use this at the literal start of any strategy engagement, whenever leadership is debating solutions before agreeing on the problem, whenever a broad fuzzy question needs to become a structured testable plan, or whenever the user asks "what's actually going on" with a business, team, or metric.
---

# Situation Assessment

## When to use
Use at the literal start of any strategy or problem-solving engagement, before any data has been pulled and before any direction has been proposed. Also use whenever leadership has a vague sense something is wrong but hasn't diagnosed it, when two people describe "what's happening" in materially different terms with neither view checked against data, or when a previous fix didn't work — which usually means the team solved for a plausible-sounding cause instead of the evidenced one.

## What it does
Runs the two phases a real engagement actually goes through in order, instead of jumping straight to data collection. Phase one: build the issue tree and an initial hypothesis at each node, before any analysis exists, so the work that follows is targeted rather than open-ended. Phase two: triangulate real evidence across three independent lenses to prove or kill each hypothesis, tagging every finding fact, inference, or unknown, so nothing downstream gets built on an unverified assumption. The output is a workplan-backed fact base anchored to one decision question, not a data dump.

## Method

### Phase 1 — Frame and hypothesize (before any data is pulled)
1. **Frame with SCQ (Situation-Complication-Question)**: state the shared situation, name the complication that broke the status quo, and write the single decision question this assessment must answer. One question, not a general review.
2. **Build the top-level issue tree**: decompose the decision question into 3-5 MECE branches, no overlapping coverage, no gaps. Test MECE-ness explicitly — could one piece of evidence plausibly sit under two branches? If so, redraw the boundary. Decompose one level further until nodes are concretely testable (not "the market is attractive," but "five-year CAGR exceeds our hurdle rate").
3. **Write an initial hypothesis at every testable node** — your best current guess at the answer, based on whatever partial evidence or experience already exists. This is the hypothesis-driven discipline real strategy work depends on: form a working answer early, then spend the engagement trying to disprove it, rather than researching everything and hoping a conclusion emerges at the end.
4. **Name the specific analysis that would prove or kill each hypothesis** — the exact data pull, interview, or calculation, not a vague "look into this." A hypothesis with no attached falsification analysis isn't yet actionable.
5. **Prioritize nodes by decision impact**: which hypotheses, if wrong, would actually change the final recommendation? Analyze those first — don't spread effort evenly across every branch.
6. **Build the workplan**: owner, data source, and target completion date per prioritized analysis — this is what turns the tree from a diagram into a running project.

### Phase 2 — Triangulate and test (the analysis itself)
7. **Triangulate three independent lenses** for every prioritized hypothesis: financial (revenue, margin, cash), market (share, demand signals, positioning), operational (throughput, quality, cost-to-serve). A financial symptom often has an operational root cause — check all three before concluding.
8. **Disaggregate before trusting an average.** Pull every lens by segment, cohort, region, or product line — a sharp localized problem hides inside a healthy blended number.
9. **Tag every finding fact (directly verified), inference (reasoned from adjacent data), or unknown (plausible, no evidence yet)** — this is the step teams skip, and it's the one that stops an assumption from silently becoming a "finding." Update each hypothesis's status: proven, killed, or still open.
10. **Plot findings on an impact × certainty 2x2.** High-impact/high-certainty is load-bearing and must be addressed. High-impact/low-certainty is the top priority to investigate next. Low-impact gets parked regardless of certainty.
11. **Curate, don't dump.** The deliverable is the ranked handful of findings that bear on the decision question, not every data point collected.
12. **Close with the resolution path** for any hypothesis still open: the specific next analysis that would convert it from inference or unknown into fact.

## Inputs
- The decision question, or the vague concern to be sharpened into one
- Financial performance by segment/product line
- Market data: share trend, demand signals, competitive positioning
- Operational metrics relevant to the business
- Available team capacity to run the workplan

## Output format
One-sentence decision question → MECE hypothesis tree with initial guesses and named proving analyses → prioritized workplan (owner, source, date) → fact base by lens with momentum read → issue tree updated with fact/inference/unknown tags per hypothesis → impact×certainty 2x2 → ranked open questions with the next analysis to close each.

## Example
"Why has growth stalled" becomes the decision question "should we prioritize fixing retention, re-accelerating acquisition, or both, in the next two quarters?" The tree splits into Acquisition / Activation / Retention / Pricing, each with an initial hypothesis. Under Retention, the hypothesis is "retention has dropped specifically in the cohort onboarded via the new self-serve flow," with the proving analysis named on day 1 (cohort retention curves by onboarding path, owner: analytics lead, due day 4). Phase 2 triangulation confirms the decline is real and concentrated exactly there — not evenly spread, as a pricing problem would be — so "pricing caused it" gets tagged killed, and "concentrated in the self-serve cohort" gets tagged fact, ready for the next phase of work.

## Common pitfalls
- Pulling data before the hypothesis tree exists, producing a pile of interesting-but-unstructured findings with no clear path to a recommendation.
- Building a tree that isn't actually MECE, so findings can't be cleanly attributed to one branch and synthesis gets muddled.
- Treating inference as fact, letting an assumption quietly become the foundation of the whole strategy.
- Analyzing every branch equally instead of prioritizing by decision impact, which wastes the scarcest resource on a real engagement: time.
- Reporting every data point instead of the curated set that answers the decision question.
