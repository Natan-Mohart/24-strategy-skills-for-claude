# Contributing

PRs and issues are welcome.

## Adding a new skill

1. Copy the structure of the closest existing skill (e.g. `skills/situation-assessment/`).
2. Every `SKILL.md` needs YAML frontmatter with `name` (matches the folder name exactly) and `description` (states both what the skill does and when to trigger it — be specific about trigger phrases, since Claude uses this to decide when to apply the skill).
3. Follow the body structure every other skill uses: **When to use → What it does → Method → Inputs → Output format → Example → Common pitfalls**.
4. If the skill is quantitative, add a `scripts/` folder with a tested Python script. No external dependencies beyond the standard library unless there's a strong reason — keep it runnable anywhere.
5. Add the skill to the README: the alphabetical table, the relevant category section, and the badge count at the top if the total changes.
6. Test any calculator against a realistic worked example before submitting — paste the actual output into the skill's **Example** section rather than inventing illustrative numbers.

## Improving an existing skill

- Keep the same structure; don't remove sections.
- If you're fixing a calculator, include the before/after output of your test case in the PR description.
- If a change affects how a skill cross-references another (e.g. `value-realization` referencing `business-case-builder`), check that the reference is still accurate after your edit.

## Reporting a bug

Open an issue with: which skill, what you expected, what happened instead, and (for calculator bugs) the input that triggers it.

## Scope

This pack is intentionally opinionated toward real consulting methodology (McKinsey's documented practice structure) rather than generic "brainstorm some ideas" prompting. New skills should teach a specific, named method — not just describe a topic.
