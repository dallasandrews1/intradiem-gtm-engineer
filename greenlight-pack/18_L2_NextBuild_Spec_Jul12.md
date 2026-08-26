# L2 next-build spec — parent-grain helper, closed loop, motion fork (Jul 12 2026)

Turnkey specs for the three structural moves left after the Jul 12 audit fixes. The live build is now correct, safe, and clean (customer leak closed, view de-cluttered, reference side green at 37/37). These are the moves that take it from correct to credit-efficient and measurable. The only one that spends credits is the first parent-grain sweep, held for explicit go and pre-estimated at ~260.

---

## A. Parent-grain helper table (R8) — credit efficiency, 0 credits to build

**BUILT Jul 12 (live, 0 credits).** The table `Parent_Signals_L2_seed` is live in the GTM Engine workbook: 29 parents (24 eligible + 5 customers tagged via a `seed_status` column, seeded from the canonical `parent_key` map), a `Lookup Multiple Rows in Other Table` to Accounts (Master) matched on `parent_key` (verified: Centene → 14 contracts, Humana → 10, every eligible parent resolved), and a `parent_intent_max` formula that rolls up the hottest contract's intent per parent (`reduce` over the looked-up records). Verified values: Centene 25, Clover / Devoted / Excellus 20, BlueShield CA / Clever Care 10, customers (Humana, HCSC) forced to 0. Auto-run OFF. This is the parent-grain hot-list and the surface the paid enrichments attach to at launch. What remains for the *credit-efficiency* half (below) is moving the paid enrichment columns onto this table (needs the parent domains) and flipping auto-run on at launch. The reporting rollup is done now.

**Why.** Every L2 signal (SEC, earnings, measure_slippage, leadership, hiring) is a parent-level fact, but Accounts (Master) is 98 contracts across 26 parents. Enriching per contract pays ~3.8x for the same parent fact. A full sweep at contract grain is ~1,176 credits; at parent grain it is ~260.

**Build steps (all free; Clay-internal imports, formulas, and lookups cost 0):**

1. New table in the GTM Engine workbook: `Parent Signals (L2)`. One row per `parent_key`. Seed the 26 eligible non-customer parents by importing the distinct `parent_key` + `parent_org` values from Accounts (Master) where `new_logo_eligible == "TRUE"` (Export the filtered view to CSV, re-import, or use "Write to table" from a de-duped view). Dedup on `parent_key`.
2. On this 26-row table, stand up the paid signal enrichments once: keyword-filtered Company Job Openings, the Claygent leadership column (reuse the tightened prompt verbatim), and later SEC/earnings. Each carries no customer rows by construction, so no run-condition is needed here.
3. `measure_slippage` computes here for free from the owned tiered CMS file (YoY movement on the call-center / CAHPS / complaints measures QO touches).
4. Back on Accounts (Master), replace the direct enrichment inputs with a `Lookup Single Row in Other Table` keyed `parent_key == parent_key` against `Parent Signals (L2)`, and repoint `intent_score`'s hiring / leadership / measure terms to read the looked-up values. Contract rows inherit their parent's signal for free.
5. Retire (hide, do not delete) the contract-grain Job Openings and leadership enrichment columns on Accounts (Master) once the lookup is wired, so nothing re-runs at contract grain.

**Credit note.** Building steps 1-5 is 0 credits. The first paid sweep on the 26 parents is pre-estimated at **~260** (26 x ~10: sec 3 + earnings 3 + leadership 2 + hiring 2 + measure 0). Pre-estimate, append a ledger row, then run. Held for explicit go. Turning auto-run back on is part of that go.

---

## B. The closed loop (U1) — the receipts, highest exec-narrative leverage

Today the layer goes signals -> intent and stops. There is no path from intent to outreach to reply to meeting to pipeline, and no cost-per-qualified-signal. That is the gap that makes the credit story "spent, tracked" instead of "spent, and here is what it bought." Spec:

1. **Intent -> outreach.** A view on Contacts filtered to parents whose Accounts (Master) `intent_status == "in_motion"` (never `excluded`/`graduated`/`dormant`) tiers which committee contacts sequence first. The customer gate guarantees no customer contact is ever in this view.
2. **Outcome writeback.** The sequencer's reply and meeting events (already captured in the campaign's events table) write back onto the parent row: `first_reply_date`, `meeting_booked_date`, `opp_created`. A `Lookup` from Accounts (Master) / Parent Signals to the events table surfaces the outcome next to the intent that drove it.
3. **Cost-per-qualified-signal.** On Parent Signals (L2), a formula: credits spent on that parent's signals (from the ledger cadence) divided by qualified replies attributed. Roll up to a portfolio `cost_per_qualified_reply` and `cost_per_meeting`. This is the renewal receipt: credits in, qualified replies and meetings out, per motion.
4. **Self-improving governance (U2).** Once outcomes are attributed, measure which signals actually preceded replies. Any signal whose cost-per-qualified-reply runs worse than 3x the portfolio average for two weeks gets downgraded to sampled use or retired in the config. The intent model then tunes itself on outcomes.

Keep "surfaced / estimated" (from the engines) and "realized" (from outcomes) as separate fields; never blend them into one number. This mirrors the impact engine's existing discipline.

**Build note.** Steps 1-2 are free (views + lookups). Step 3-4 are free (formulas). No credits. This is design + wiring, held until the sequencer is live and producing events.

---

## C. Motion dimension / back-office fork (U4) — scale without a rebuild

The config now carries `active_motion` and each signal a `motions` list; the scorer filters on it (verified: `claims_backlog` scores under `back_office`, not `star_ratings`). To stand up the back-office motion later without rebuilding:

1. Add the back-office signals to the same config with `"motions": ["back_office"]` (claims_backlog is already there; add shared-services / document-processing / payment-ops signals per the back-office ICP work with Scott Kemme).
2. Build a parallel `intent_score_bo` / `intent_status_bo` pair on the back-office target table using the same formula shape, reading the back-office signal columns. Same customer gate, same self-clean.
3. Set `active_motion` per table/view. One config, one scorer, two motions.

This is the difference between scaling by adding a config block and scaling by forking the whole engine. No credits; gated on the back-office ICP being ratified.

---

## Sequence

1. Build the parent helper structure (A1-A5). Free.
2. Wire `measure_slippage` + `sig_sec_filing` + `sig_earnings` on the helper. Free to wire.
3. Pre-estimate (~260), log, run the first parent-grain sweep. **Held for explicit go.**
4. Turn auto-run back on at parent grain.
5. When the sequencer is live: wire the closed loop (B1-B4). Free.
6. When the back-office ICP is ratified: fork the motion (C1-C3). Free.

Everything except step 3 is 0 credits. Step 3 is the one paid action and it waits on an explicit go.
