---
name: stakeholder-alignment
description: Maps stakeholders on power vs. interest via a bundled calculator that also checks coalition math — total power held by supporters vs. opponents, not just headcount — so a plan with lots of low-power supporters and one high-power skeptic isn't mistaken for a safely aligned org. Use whenever the user needs to plan how to align or communicate a decision across stakeholders, is worried about resistance to a change, or is counting supportive people without weighing how much organizational power each one actually holds.
---

# Stakeholder Alignment

## When to use
Use before rolling out any decision, strategy, or change that affects multiple parts of an organization, especially when the current plan is "communicate broadly and hope for buy-in" with no differentiated strategy per stakeholder, and no explicit accounting for the fact that one skeptical, high-power stakeholder can outweigh five enthusiastic, low-power ones.

## What it does
Places every relevant stakeholder on a power × interest grid via a bundled calculator, assigns an engagement strategy by quadrant, and — critically — computes coalition math: sums power (not headcount) among supportive/champion stakeholders versus skeptical/opposed ones, flagging when the opposition actually holds more real influence even if fewer people are on that side.

## Method
1. **List every stakeholder who can meaningfully help or block the decision**, not just the obvious org-chart approvers — include informal influencers who carry real power despite no formal authority.
2. **Score each on power (1-5)**: their actual ability to help, block, or resource the initiative — formal authority, budget control, informal influence, veto power.
3. **Score each on interest (1-5)**: how much this decision actually affects them or their team, independent of power.
4. **Assign a stance**: champion, supportive, neutral, skeptical, or opposed — based on their actual demonstrated position, not an assumed default of "probably fine with it."
5. **Run the bundled calculator** (`scripts/power_interest_grid.py`) to get the quadrant placement and engagement strategy per stakeholder, plus the coalition math: total power among supportive stakeholders vs. total power among skeptical/opposed ones.
6. **If the coalition math flags opposition power at or above supportive power, treat it as the headline finding**, not a footnote — this is the single most common blind spot in stakeholder planning: counting supportive names while the highest-power person in the room is quietly unconvinced.
7. **Build a specific, individual plan for every high-power skeptical or opposed stakeholder** — not a generic "communication plan," but the actual concern they hold, the specific evidence or concession that would move them, and who is the right person to have that conversation.
8. **Sequence engagement**: high-power stakeholders (manage closely / keep satisfied) generally need to move before a broad announcement, since a surprised high-power skeptic after the fact is far harder to bring around than one engaged early.

## Inputs
- List of stakeholders with power and interest scores and current stance
- Any known specific objections or concerns per skeptical/opposed stakeholder
- The decision or change being aligned around, and its timeline
- Config saved as JSON matching the format documented at the top of `scripts/power_interest_grid.py`

## Output format
Power-interest grid with quadrant and engagement strategy per stakeholder; coalition math (supportive power vs. opposed power) with explicit flag if opposition holds equal or greater power; individual engagement plan for each high-power skeptical/opposed stakeholder; recommended sequencing of engagement before any broad rollout.

## Example
A change initiative has four supportive stakeholders and one skeptical one — by headcount, alignment looks solid. Coalition math shows the skeptical stakeholder (the CFO) holds as much total power as all four supporters combined. The plan shifts from a broad kickoff announcement to a dedicated 1:1 with the CFO first, addressing the specific budget concern driving the skepticism, before any wider rollout — rather than proceeding on the false confidence of a 4:1 headcount ratio.

## Common pitfalls
- Counting supportive stakeholders by headcount instead of weighting by actual power, producing false confidence in alignment.
- Treating a high-power skeptic's silence as passive agreement instead of actively surfacing and addressing their concern.
- Running one generic communication plan for every stakeholder instead of a differentiated strategy by quadrant.
