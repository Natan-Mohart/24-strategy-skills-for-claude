---
name: negotiation-prep
description: Prepares a negotiation by computing the actual Zone of Possible Agreement via a bundled BATNA calculator, and explicitly flags when no ZOPA exists so effort goes into restructuring the deal or walking away instead of grinding on a price gap that can't close. Use whenever the user is preparing for a negotiation (deal terms, salary, vendor contract, partnership), needs to set a walk-away price, or is about to negotiate without having named their BATNA or estimated the counterparty's.
---

# Negotiation Prep

## When to use
Use before any negotiation with real stakes — a deal, a vendor contract, a partnership term sheet, a compensation discussion — especially when the current prep amounts to "know your number and hold firm" with no stated BATNA (Best Alternative to a Negotiated Agreement) and no estimate of the other side's walk-away point.

## What it does
Computes the actual Zone of Possible Agreement (ZOPA) via a bundled calculator using your BATNA-derived reservation price and an estimate of the counterparty's reservation price, recommends an opening anchor that sits inside the ZOPA rather than outside it, and explicitly flags when no ZOPA exists at all — the single most useful thing a negotiation prep exercise can surface, since no amount of negotiating skill closes a gap that isn't actually there.

## Method
1. **Name your BATNA concretely**: what happens, in specific terms, if this negotiation fails entirely? A vague "we'd find another vendor" is not a BATNA; a specific alternative with its own real price and terms is.
2. **Derive your reservation price from the BATNA, not from an aspiration.** Your walk-away point is the value of your BATNA — going past it in the name of "not walking away empty-handed" destroys value versus your actual alternative, even if the deal in front of you feels like progress.
3. **Set your target price** — the number you'd genuinely be pleased with, distinct from your reservation price (the number below which you should walk).
4. **Estimate the counterparty's reservation price and target price** from whatever evidence is available: their known alternatives, public information, past deal patterns, market comparables. State the confidence level of this estimate explicitly — it's the least certain input and deserves to be treated that way.
5. **Run the bundled calculator** (`scripts/batna_zopa.py`) to compute the ZOPA and get a recommended opening anchor that sits inside it.
6. **If a ZOPA exists**, anchor near your target but inside the ZOPA — anchoring outside it (even in your own favor) risks being dismissed as not negotiating in good faith rather than being taken as an aggressive but serious opening.
7. **If no ZOPA exists, do not proceed to negotiate on price.** The calculator's explicit flag means one of three things: walk away to your BATNA, restructure the deal (financing terms, timeline, scope, bundled items) to create value that shifts one side's reservation price, or revisit your estimate of the counterparty's position since it may be wrong.
8. **Prepare for the parts a calculator can't model**: the specific concessions you're willing to trade (and in what order, since sequencing concessions signals different things than granting them all at once), and the two or three questions that would most improve your estimate of the counterparty's actual reservation price once the conversation starts.

## Inputs
- Your BATNA, stated concretely with its own value
- Your target price/terms
- Best available estimate of the counterparty's reservation and target price/terms, with a stated confidence level
- Config saved as JSON matching the format documented at the top of `scripts/batna_zopa.py`

## Output format
Your derived reservation price from your BATNA; the ZOPA range and midpoint if one exists; a recommended opening anchor; your walk-away price stated plainly; or, if no ZOPA exists, an explicit flag with the three response options (walk away, restructure, re-verify the estimate).

## Example
A buyer preparing to negotiate a contract sets a target of $400K, with a BATNA (an alternative vendor) worth $480K to them if this deal falls through. Estimating the seller's reservation price at $460K, the calculator shows a real ZOPA of $460K-$480K and recommends anchoring near $460K rather than the buyer's original $400K target, which the calculator shows was outside the actual zone of possible agreement — negotiating from an out-of-range target would have wasted the early rounds of the conversation on a number that was never achievable.

## Common pitfalls
- Walking into a negotiation with a target price but no derived reservation price, risking a deal that's worse than the real alternative.
- Continuing to negotiate on price when no ZOPA exists, instead of recognizing the deal needs to be restructured or walked away from.
- Treating the counterparty's estimated reservation price as certain instead of the least reliable input in the whole analysis.
