<div align="center">

# 24 Strategy Skills for Claude

**A consulting operating system for Claude, built on real McKinsey practice structure, not a generic prompting template.**

<img src="assets/overview.png" alt="24 Strategy Skills for Claude — overview" width="720">

</div>

24 [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for Claude, one folder per skill, each a `SKILL.md` plus, for the quantitative ones, a bundled Python calculator. Built around McKinsey's actual documented problem-solving method (define the problem, build a MECE issue tree, form hypotheses, prioritize, build a workplan, analyze, synthesize, communicate) and their real practice-area names, instead of a generic "diagnose → communicate" template.

**13 of the 24 skills ship a tested Python calculator** - NPV/IRR, LTV:CAC, TAM/SAM/SOM, Van Westendorp pricing, spans and layers, GE-McKinsey 9-box, decision-tree expected value, risk scoring, BATNA/ZOPA, RICE, and synergy NPV, so the number-heavy skills compute a real answer instead of describing a method and leaving the math to you.

**Contributions welcome!** Found a gap, a calculator bug, or have a skill to add? See [Contributing](#contributing).

## What are Skills?

Skills are markdown files that give Claude specialized knowledge and a repeatable method for a specific task. When Claude has access to these, it recognizes when a conversation matches a skill's `description` and applies that skill's method automatically, no need to invoke it by name, though you can (`Use the market-mapping skill to size this opportunity`).

## How the skills fit together

`situation-assessment` and `assumption-audit` sit at the start of any real engagement. `full-potential-diagnostic` and `business-case-builder` size what a decision is worth in dollars. `value-realization` is the only skill in the pack that looks backward, it closes the loop by checking what the projection-producing skills predicted against what actually happened.

```
                    ┌───────────────────────────────────────┐
                    │         situation-assessment           │
                    │   (hypothesis tree + fact base first)  │
                    └───────────────────┬─────────────────────┘
                                        │
   ┌─────────────┬──────────────┬───────┼────────┬──────────────┬──────────────┐
   ▼             ▼              ▼       ▼        ▼              ▼              ▼
┌─────────┐ ┌──────────┐ ┌────────────┐ ┌──────────────┐ ┌───────────┐ ┌──────────────┐
│Problem  │ │Market &  │ │Strategy &  │ │Performance   │ │Risk &     │ │Communication │
│Def.     │ │Competitive│ │Corp Finance│ │Transformation│ │Value Cap. │ │& Change      │
├─────────┤ ├──────────┤ ├────────────┤ ├──────────────┤ ├───────────┤ ├──────────────┤
│growth-  │ │market-   │ │strategic-  │ │operating-    │ │war-gaming │ │stakeholder-  │
│ barriers│ │ mapping  │ │ options    │ │ model-design │ │risk-      │ │ alignment    │
│full-    │ │competitiv│ │pricing-    │ │spans-layers  │ │ mitigation│ │narrative-    │
│ potential│ │e-intel   │ │ strategy   │ │initiative-   │ │synergy-   │ │ builder      │
│         │ │customer- │ │business-   │ │ prioritizer  │ │ case      │ │decision-memo │
│         │ │ segment  │ │ case       │ │100-day-plan  │ │value-     │ │negotiation-  │
│         │ │unit-econ │ │capital-    │ │              │ │ realization│ │ prep         │
│         │ │          │ │ realloc    │ │              │ │(checks →) │ │              │
└─────────┘ └──────────┘ └─────┬──────┘ └──────┬───────┘ └─────┬─────┘ └──────────────┘
                               │               │                │
                               └───────────────┴────────────────┘
                     value-realization checks these three against actuals
```

## Available Skills

| Skill | Description |
|---|---|
| [`100-day-plan`](skills/100-day-plan) | The real post-close/new-leader sequence, listen, decide, launch, with quick wins built in |
| [`assumption-audit`](skills/assumption-audit) | Surfaces load-bearing assumptions, scores evidence quality, designs falsification tests |
| [`business-case-builder`](skills/business-case-builder) 🧮 | Driver-based NPV/IRR/payback with a real sensitivity grid |
| [`capital-reallocation-review`](skills/capital-reallocation-review) 🧮 | GE-McKinsey 9-box scoring plus measured capital-reallocation intensity |
| [`competitive-intel`](skills/competitive-intel) | Capability/incentive/constraint competitor modeling, pre-committed responses |
| [`customer-segmentation`](skills/customer-segmentation) | Jobs-to-be-Done segmentation, attractiveness × right-to-win scoring |
| [`decision-memo`](skills/decision-memo) | One-page Bezos-style decision memo engineered to force a yes/no |
| [`full-potential-diagnostic`](skills/full-potential-diagnostic) 🧮 | Sizes the $ value-at-stake vs. top-quartile benchmark, metric by metric |
| [`growth-barriers`](skills/growth-barriers) | Theory of Constraints funnel diagnosis; isolates the ONE binding constraint |
| [`initiative-prioritizer`](skills/initiative-prioritizer) 🧮 | RICE scoring with a cost-of-delay sequencing overlay |
| [`market-mapping`](skills/market-mapping) 🧮 | Triangulated TAM/SAM/SOM, flags top-down vs. bottom-up disagreement |
| [`narrative-builder`](skills/narrative-builder) | Pyramid Principle + Situation-Complication-Resolution restructuring |
| [`negotiation-prep`](skills/negotiation-prep) 🧮 | Computes the real Zone of Possible Agreement, flags when none exists |
| [`operating-model-design`](skills/operating-model-design) | RAPID/DACI decision rights, 7S coherence check, capability gaps |
| [`pricing-strategy`](skills/pricing-strategy) 🧮 | Van Westendorp price sensitivity + elasticity revenue/margin modeling |
| [`risk-mitigation`](skills/risk-mitigation) 🧮 | Likelihood × impact × velocity risk matrix, flags unmitigated critical risks |
| [`situation-assessment`](skills/situation-assessment) | Day-1 MECE hypothesis tree and workplan, then three-lens fact triangulation |
| [`spans-layers-org-design`](skills/spans-layers-org-design) 🧮 | Measures span of control by layer, prices the cost of excess management layers |
| [`stakeholder-alignment`](skills/stakeholder-alignment) 🧮 | Power-interest grid with coalition math (power, not headcount) |
| [`strategic-options`](skills/strategic-options) | Forces genuinely distinct options, weighted scoring, real-options staging |
| [`synergy-case-builder`](skills/synergy-case-builder) 🧮 | M&A synergy NPV with realistic ramp curves and a revenue-synergy confidence haircut |
| [`unit-economics-health-check`](skills/unit-economics-health-check) 🧮 | LTV:CAC and CAC payback using a realistic churn-decay curve |
| [`value-realization`](skills/value-realization) | Closes the loop: checks projections from other skills against what actually happened |
| [`war-gaming`](skills/war-gaming) 🧮 | Decision-tree expected value, flags EV-best vs. maximin-best divergence |

🧮 = ships a bundled Python calculator in `scripts/`

## Skill Categories

### 01 · Problem Definition
Before anyone touches a solution.
`situation-assessment` · `growth-barriers` · `assumption-audit` · `full-potential-diagnostic`

### 02 · Market & Competitive Analysis
Where the value actually sits.
`market-mapping` · `competitive-intel` · `customer-segmentation` · `unit-economics-health-check`

### 03 · Strategy & Corporate Finance
Where bets and capital get decided. McKinsey's own practice name.
`strategic-options` · `pricing-strategy` · `business-case-builder` · `capital-reallocation-review`

### 04 · Performance Transformation
Turning strategy into delivered results. The other real McKinsey practice name.
`operating-model-design` · `spans-layers-org-design` · `initiative-prioritizer` · `100-day-plan`

### 05 · Risk & Value Capture
Before it launches, and after.
`war-gaming` · `risk-mitigation` · `synergy-case-builder` · `value-realization`

### 06 · Communication & Change
Making the work survive the meeting.
`stakeholder-alignment` · `narrative-builder` · `decision-memo` · `negotiation-prep`

## Calculators

Every calculator was run against a worked test case while this pack was built, the numbers in each skill's **Example** section are real output, not invented illustrations. A few examples of what they catch that a prose-only skill can't:

- `market-mapping/scripts/tam_sam_som.py` flags when a top-down and bottom-up market-size estimate disagree by more than 30%
- `business-case-builder/scripts/npv_case.py` returns a full revenue × discount-rate NPV sensitivity grid, not a single point estimate
- `war-gaming/scripts/decision_tree_ev.py` flags when the highest-expected-value option and the safest-worst-case option are different choices
- `stakeholder-alignment/scripts/power_interest_grid.py` computes coalition math by power, not headcount, and flags when opposition outweighs support
- `negotiation-prep/scripts/batna_zopa.py` tells you plainly when no Zone of Possible Agreement exists, instead of letting you negotiate on a gap that can't close

## Installation

### Option 1: Claude.ai / Claude Desktop

Settings → Skills → Add → Upload a skill → select a skill's `SKILL.md` (or its folder, where supported). Repeat per skill, or upload all 24.

### Option 2: Claude Code — CLI install

```bash
npx skills add Natan-Mohart/24-strategy-skills-for-claude
```

Installs into `.claude/skills/` (project) or `~/.claude/skills/` (personal) depending on how you answer the CLI prompt. Claude Code picks up `SKILL.md` files automatically in the next session.

### Option 3: Claude Code — clone and copy

```bash
git clone https://github.com/Natan-Mohart/24-strategy-skills-for-claude.git
cp -r 24-strategy-skills-for-claude/skills/* ~/.claude/skills/
```

### Option 4: Fork and customize

Fork this repo, edit any `SKILL.md` or `scripts/*.py` to fit your own business, then install from your fork using either option above.

## Skill format

Every `SKILL.md` follows the same structure: **When to use → What it does → Method → Inputs → Output format → Example → Common pitfalls**, grounded in named frameworks (MECE, RAPID/DACI, Theory of Constraints, Van Westendorp, GE-McKinsey, RICE, Jobs-to-be-Done, real options, BATNA/ZOPA, spans and layers) instead of generic "brainstorm some ideas" instructions.

## Why this exists

Most "strategy skills for Claude" packs mirror the same six-phase consulting narrative with prose-only prompting frameworks and an identical topic list. This one:

- Uses McKinsey's actual documented hypothesis-driven method and real practice-area names
- Runs situation assessment and hypothesis-tree building as one skill instead of two overlapping ones, hypothesis on day one, facts that test it second
- Includes topics a typical strategy-skill pack skips entirely: full-potential diagnostics, 100-day plans, M&A synergy cases, spans-and-layers org design, unit economics health checks, and negotiation prep
- Ships 13 tested Python calculators instead of zero
- Closes the loop: `value-realization` checks the projections that `business-case-builder`, `full-potential-diagnostic`, and `synergy-case-builder` produce against what actually happened

## Contributing

Found a gap, a bug in a calculator, or a skill that overlaps with another? See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) - use it, fork it, adapt it.

---

<div align="center">

Built by **Natan Mohart** · follow for more Claude and AI strategy content

</div>
