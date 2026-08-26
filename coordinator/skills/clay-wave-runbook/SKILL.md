---
name: clay-wave-runbook
description: Wave discipline for every Clay campaign. Enforces "source the full universe once, process in waves" and runs the per-wave checklist. Trigger on any Clay contact-volume decision or wave action - add contacts, load leads, fill the campaign, expand the campaign, next wave, wave 2, new batch, re-run enrichment, sync leads, how many contacts, load the rest, when do we go back, or starting/scaling any motion (Stars, Cost-Mandate, WFM-Adjacency, Install-Base, Back Office). Load proactively whenever a Clay build, campaign load, or launch is discussed. Canonical rules live in Clay_Golden_Standard.md section 16 and New_Motion_Build_Runbook.md at the project root - this skill enforces, those docs govern; if they disagree, the docs win.
---

# Clay Wave Runbook

## The doctrine (one rule, two halves)
**Source once:** the FULL applicable universe is found, deduped, tagged, and loaded into
the standing Clay tables at motion kickoff. Discovery never happens twice. Later waves
PULL from the standing table - they never go back out hunting. Signal-defined universes
stay alive via the intent layer (new accounts enter as signals fire); that is refresh,
not re-sourcing.

**Process in waves:** paid enrichment, MessageGen + critic, campaign load, and sync run
only on the active wave slice of 30-50 contacts, tracked by `wave_number` and
`wave_status` (staged / enriched / drafted / launched / done) on Contacts.

Why 30-50: observed defect rate on Stars waves was 10-18% (3/38 census FAILs, 4 drafts
needing per-lead overrides). At 30-50 that is an afternoon of surgical fixes; at full
scale it is dozens of fragile campaign-side overrides that one sync re-run wipes.

## If the motion is not named
Ask which motion/table before acting. One question, then proceed.

## The per-wave checklist (run in order, no skips)
1. **Pick the slice** from the standing universe (30-50, priority-ordered). Set `wave_number`.
2. **Credit gate:** estimate via clay-credit-steward, write the ledger row BEFORE any paid run.
3. **Enrich** the slice only (only-run-if-empty, tiered, optional inputs Required-to-run OFF).
4. **Generate:** MessageGen + companion critic. Stamp the prompt version on the wave.
5. **Census** the drafts. Fix FAILs per-lead at campaign level; data mismatches are DATA
   fixes, never force-passes.
6. **Load + sync** to the persona campaigns. Verify `Sent At` on the live page, not the grid tick.
   NEVER re-run sync over a wave carrying campaign-side per-lead overrides.
7. **Launch** only on explicit approval in that session (Draft + critic PASS + human approval).
8. **Schedule the successor:** create the next-wave check (~9 business days out, when the
   sequence completes) as a scheduled task or dated runbook entry. A wave is NOT "launched"
   until this exists.
9. **Before the next wave:** read the prior wave's reply data first. Learnings go into the
   MessageGen prompt (bump the version) before the new slice generates.

## Hard NOs
- No enrichment or MessageGen across the whole universe "to get it done."
- No new wave while the prior wave's replies are unread.
- No sync re-run on a campaign holding per-lead overrides.
- No wave without a ledger row, and no launch without a scheduled successor.
