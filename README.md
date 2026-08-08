<div align="center">

# 24 Strategy Skills for Claude

**A consulting operating system for Claude, built on real McKinsey practice structure — not a generic prompting template.**

[![Skills](https://img.shields.io/badge/skills-24-B3221A)](#skill-index)
[![Domains](https://img.shields.io/badge/domains-6-1E3A8A)](#domains)
[![Calculators](https://img.shields.io/badge/bundled%20calculators-13-0F7A46)](#calculators)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

<img src="assets/overview.png" alt="24 Strategy Skills for Claude — overview" width="720">

</div>

## What this is

24 [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview), one folder per skill, organized into six domains that map to McKinsey's actual documented practice structure and their hypothesis-driven problem-solving method (define the problem, build a MECE issue tree, form hypotheses, prioritize, build a workplan, analyze, synthesize, communicate) instead of a generic "diagnose → communicate" template.

**13 of the 24 skills ship a bundled, tested Python calculator** — NPV/IRR, LTV:CAC, TAM/SAM/SOM, Van Westendorp pricing, spans and layers, GE-McKinsey 9-box, decision-tree expected value, risk scoring, BATNA/ZOPA, RICE, and synergy NPV — so the number-heavy skills compute a real answer instead of describing a method and leaving the math to you.

## Install

1. Download or clone this repo.
2. In Claude, open **Settings → Skills → Add → Upload a skill**.
3. Upload a skill's `SKILL.md` (or the whole skill folder, where supported). Repeat for each skill you want.
4. Skills trigger automatically based on their `description` when your conversation matches — no need to invoke them by name, though you can (`Use the market-mapping skill to size...`).

Skills with a bundled calculator include a `scripts/` folder — Claude runs these directly when the skill triggers in an environment with code execution.

## Domains

| # | Domain | Skills | Focus |
|---|--------|:---:|-------|
| 01 | [Problem Definition](#01--problem-definition) | 4 | Before anyone touches a solution |
| 02 | [Market & Competitive Analysis](#02--market--competitive-analysis) | 4 | Where the value actually sits |
| 03 | [Strategy & Corporate Finance](#03--strategy--corporate-finance) | 4 | Where bets and capital get decided |
| 04 | [Performance Transformation](#04--performance-transformation) | 4 | Turning strategy into delivered results |
| 05 | [Risk & Value Capture](#05--risk--value-capture) | 4 | Before it launches, and after |
| 06 | [Communication & Change](#06--communication--change) | 4 | Making the work survive the meeting |

---

### 01 · Problem Definition
*Builds the hypothesis tree first, tests it against a real fact base, then sizes what's at stake, before anyone touches a solution.*

| Skill | Use when | Output |
|---|---|---|
| [`situation-assessment`](skills/01-problem-definition/situation-assessment) | You need the real baseline before choosing a direction | Hypothesis tree, workplan, fact base, momentum read |
| [`growth-barriers`](skills/01-problem-definition/growth-barriers) | Growth stalled and teams are debating symptoms | The one binding constraint, sized |
| [`assumption-audit`](skills/01-problem-definition/assumption-audit) | A plan rests on beliefs nobody has tested | Assumption register and falsification tests |
| [`full-potential-diagnostic`](skills/01-problem-definition/full-potential-diagnostic) 🧮 | "There's room to improve" has no number attached | Dollar value at stake vs. top quartile |

### 02 · Market & Competitive Analysis
*Sizes the market, reads the customer, and models rivals by capability and incentive, not gut feel.*

| Skill | Use when | Output |
|---|---|---|
| [`market-mapping`](skills/02-market-competitive-analysis/market-mapping) 🧮 | You need a market size you can defend | Triangulated TAM, SAM, SOM plus white space |
| [`competitive-intel`](skills/02-market-competitive-analysis/competitive-intel) | You need to predict a rival's next move | Capability profile, pre-committed response |
| [`customer-segmentation`](skills/02-market-competitive-analysis/customer-segmentation) | Personas do not predict buying behavior | Jobs-based segments ranked by fit |
| [`unit-economics-health-check`](skills/02-market-competitive-analysis/unit-economics-health-check) 🧮 | LTV is calculated on a flat churn rate that never changes | Real LTV:CAC ratio and CAC payback period |

### 03 · Strategy & Corporate Finance
*McKinsey's own practice name. Turns options into real economics: NPV, pricing power, and where capital should actually go.*

| Skill | Use when | Output |
|---|---|---|
| [`strategic-options`](skills/03-strategy-corporate-finance/strategic-options) | Only one option has ever been developed | Weighted option set, staged recommendation |
| [`pricing-strategy`](skills/03-strategy-corporate-finance/pricing-strategy) 🧮 | Price is set by cost-plus guessing | Willingness-to-pay range, margin curve |
| [`business-case-builder`](skills/03-strategy-corporate-finance/business-case-builder) 🧮 | A case needs real economics, not a hunch | NPV, IRR, and a sensitivity grid |
| [`capital-reallocation-review`](skills/03-strategy-corporate-finance/capital-reallocation-review) 🧮 | Budget is last year's number plus a few percent | 9-box placement, reallocation plan |

### 04 · Performance Transformation
*The other real McKinsey practice name. Fixes decision rights and structure, then sequences delivery and the first 100 days.*

| Skill | Use when | Output |
|---|---|---|
| [`operating-model-design`](skills/04-performance-transformation/operating-model-design) | Decisions are slow and nobody owns them | RAPID map, structure recommendation |
| [`spans-layers-org-design`](skills/04-performance-transformation/spans-layers-org-design) 🧮 | The org feels top-heavy but nobody has priced it | Span of control by layer, cost of excess layers |
| [`initiative-prioritizer`](skills/04-performance-transformation/initiative-prioritizer) 🧮 | Too many initiatives, not enough capacity | RICE-ranked roadmap, cost of delay flagged |
| [`100-day-plan`](skills/04-performance-transformation/100-day-plan) | A new leader or deal needs an opening sequence | Listen, decide, launch plan with quick wins |

### 05 · Risk & Value Capture
*Stress tests the plan against reality before launch, then closes the loop with what actually happened after.*

| Skill | Use when | Output |
|---|---|---|
| [`war-gaming`](skills/05-risk-value-capture/war-gaming) 🧮 | Competitor reaction is genuinely uncertain | Expected value by option, worst case flagged |
| [`risk-mitigation`](skills/05-risk-value-capture/risk-mitigation) 🧮 | A risk list has no owners or scores | Likelihood, impact, and velocity matrix |
| [`synergy-case-builder`](skills/05-risk-value-capture/synergy-case-builder) 🧮 | A deal case assumes synergies land instantly | Ramped synergy NPV, net of integration cost |
| [`value-realization`](skills/05-risk-value-capture/value-realization) | A past case was never checked against what happened | Actual vs. plan by driver, cause of every gap |

### 06 · Communication & Change
*Pre-wires the room, sharpens the story, and turns a recommendation into a written decision someone actually signs.*

| Skill | Use when | Output |
|---|---|---|
| [`stakeholder-alignment`](skills/06-communication-change/stakeholder-alignment) 🧮 | Support is counted by headcount, not power | Power-interest grid, coalition math |
| [`narrative-builder`](skills/06-communication-change/narrative-builder) | The story needs to land in the first 60 seconds | Pyramid structure with SCR framing |
| [`decision-memo`](skills/06-communication-change/decision-memo) | A recommendation never quite gets a yes or no | One-page memo with a stated deadline |
| [`negotiation-prep`](skills/06-communication-change/negotiation-prep) 🧮 | Nobody has named a walk-away price before the room | Zone of possible agreement, recommended anchor |

🧮 = ships a bundled Python calculator in `scripts/`

## Calculators

Every calculator was run against a worked test case while this pack was built — the numbers in each skill's **Example** section are real output, not invented illustrations. A few examples of what they catch that a prose-only skill can't:

- `market-mapping/scripts/tam_sam_som.py` flags when a top-down and bottom-up market-size estimate disagree by more than 30%
- `business-case-builder/scripts/npv_case.py` returns a full revenue × discount-rate NPV sensitivity grid, not a single point estimate
- `war-gaming/scripts/decision_tree_ev.py` flags when the highest-expected-value option and the safest-worst-case option are different choices
- `stakeholder-alignment/scripts/power_interest_grid.py` computes coalition math by power, not headcount, and flags when opposition outweighs support
- `negotiation-prep/scripts/batna_zopa.py` tells you plainly when no Zone of Possible Agreement exists, instead of letting you negotiate on a gap that can't close

## Why this exists

Most "strategy skills for Claude" packs mirror the same six-phase consulting narrative with prose-only prompting frameworks and an identical topic list. This one:

- Uses McKinsey's actual documented hypothesis-driven method and real practice-area names, not a generic phase-by-phase template
- Runs situation assessment and hypothesis-tree building as one skill instead of two overlapping ones, hypothesis on day one, facts that test it second
- Includes topics a typical strategy-skill pack skips entirely: full-potential diagnostics, 100-day plans, M&A synergy cases, spans-and-layers org design, unit economics health checks, and negotiation prep
- Ships 13 tested Python calculators instead of zero
- Closes the loop: `value-realization` checks the projections that `business-case-builder`, `full-potential-diagnostic`, and `synergy-case-builder` produce against what actually happened, instead of generating forecasts and walking away from them

## Skill format

Every `SKILL.md` follows the same structure: **When to use → What it does → Method → Inputs → Output format → Example → Common pitfalls**, grounded in named frameworks (MECE, RAPID/DACI, Theory of Constraints, Van Westendorp, GE-McKinsey, RICE, Jobs-to-be-Done, real options, BATNA/ZOPA, spans and layers) instead of generic "brainstorm some ideas" instructions.

## Contributing

Found a gap, a bug in a calculator, or a skill that overlaps with another? Open an issue or a PR. Each skill is self-contained (`SKILL.md` + optional `scripts/`), so adding a 25th skill just means copying the structure of the closest existing one.

## License

[MIT](LICENSE) — use it, fork it, adapt it.

---

<div align="center">

Built by **Natan Mohart** · follow for more Claude and AI strategy content

</div>
