---
name: clay-credit-steward
description: "Clay credit budget steward for Intradiem's 5,000-credit allocation. Estimates credit cost BEFORE any enrichment run or new table build, maintains the append-only credit ledger, tracks burn by motion, computes cost-per-qualified-reply, flags at 60% consumed, and packages the renewal receipts story (credits in, qualified replies and meetings out). Trigger on: credit check, can we afford this run, clay budget, credit ledger, how many credits left, before building any new Clay table or adding enrichment columns, and weekly before the Friday readout. Load proactively whenever a Clay build or enrichment expansion is being planned."
---

## When this skill applies

- BEFORE any new Clay table build, enrichment column, or signal source is added (mandatory pre-check)
- Weekly, before the Friday readout (burn summary feeds it)
- When anyone asks what Clay costs, what is left, or whether a run is worth it
- When preparing the Clay renewal or expansion conversation

## Background

Intradiem purchased 5,000 Clay credits with an explicit mandate: exhaust them, show results, then decide on further investment. Credit stewardship is therefore not bookkeeping; it is the visible proof of judgment Naveen is watching for, and the receipts for the renewal ask. Signals and premium enrichments burn fast. Every credit spent must trace to a motion, and every motion must show what the credits bought.

## Standing rules

1. **No un-budgeted runs.** Every enrichment run gets a cost estimate BEFORE it executes: rows × columns × per-provider credit cost. If actuals are unknown, run a 10-row sample first and extrapolate.
2. **Budget by motion.** Star Ratings, back-office sourcing, and install-base whitespace each carry their own allocation. A motion overspending borrows explicitly, never silently.
3. **Tier your enrichments.** Cheap-and-broad first (firmographics), expensive-and-narrow (intent, technographics, waterfall email finding) only on rows that already cleared fit thresholds. Never run premium enrichment on an unscored list.
4. **The 60% flag.** At 3,000 credits consumed, produce the mid-burn review: yield per motion, what gets killed, what earns the remaining 40%.
5. **Kill criteria.** Any enrichment whose cost-per-qualified-reply runs worse than 3x the portfolio average for two consecutive weeks gets killed or downgraded to sampled use.
6. **Verify current Clay pricing mechanics before instructing.** Provider credit costs and UI change; check Clay's current docs rather than instructing from memory.

## The ledger

Maintain `Clay_Credit_Ledger.md` in the project folder, append-only:

`date · motion · table/run · rows · columns/providers · est_credits · actual_credits · purpose · yield note`

Plus a running header: total consumed, remaining, % burned, projected exhaustion date at current run rate.

## Workflow

1. **Pre-check (on any planned run):** estimate cost, name the motion, state what the run is expected to yield (contacts, signals, messages), get the go/no-go. If the run cannot articulate expected yield, it does not run.
2. **Post-run:** append actuals to the ledger. Actual vs estimate drift over 25% gets a one-line cause note.
3. **Weekly:** burn summary by motion, cost-per-enriched-contact, cost-per-qualified-reply where attribution exists, flags. Feed the Friday readout.
4. **At 60%:** mid-burn review document. At 85%: renewal packet drafting starts.
5. **Renewal packet:** credits in → contacts enriched → messages sent → qualified replies → meetings sourced → pipeline, by motion, with the ask sized to what proved out. Receipts, not projections.

## Output

- `Clay_Credit_Ledger.md` (append-only, the source of truth)
- Weekly: a short burn block for the readout (3-5 lines)
- On demand: pre-check verdicts in chat (estimate, budget impact, go/no-go recommendation)

## Posture

Numbers in the ledger are internal-operational, never prospect-facing. When speaking to Naveen: stewardship framing ("every motion has a credit budget, burn tracked weekly, receipts at renewal"), never scarcity framing. The story is judgment, not thrift.
