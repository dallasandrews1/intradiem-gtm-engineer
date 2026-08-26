Task: build the Cost-Mandate / Efficiency Clay workbook (Motion 1, `cost_mandate_xvert`), the first of the three new motions after Star Ratings and Back Office. Build it to the SAME level of excellence as the live Star Ratings workbook, rung for rung. Do not ship a lighter cost-mandate analog. The Star Ratings build is the quality bar: an 8-layer table architecture, a point-scored self-cleaning intent layer, a persona-routed MessageGen system prompt with a companion figure-integrity critic, and 5-touch multi-channel personalized sequences. Match that depth.

## Study these first as the reference standard (do not build from memory, mirror their depth)
- `Clay_Engine_Full_Architecture.md`: the 8-layer L0 to L8 table map (Sources, Accounts Master, L2 Signals write-back, Contacts, Message Gen, Send Queue critic+approval, Outreach Sync, Reply/Attribution, AE Worklist). Your motion reuses L5 to L8; you are building L0 to L4 for cost-mandate.
- `Clay_MessageGen_SystemPrompt_v2.md`: the MessageGen system prompt (v2.2.1) AND its companion Terra v3 critic. This is the personalization standard you must match: token/column map, persona routing, a core position, number discipline, block-on-empty, fallback-per-token, banned words, no em dashes, worked examples.
- `StarRatings_Wave1_Persona_Sequences_Jul13.md`: the 5-touch, two-lane, merge-field-driven sequence standard with per-touch angle shifts and staggered committee entry.
- `greenlight-pack/16_L2_Signal_Monitoring_Spec_Jul11.md`: the L2 intent layer, point-valued signals, `intent_score`/`intent_status` formulas, the customer-exclusion kill switch, run-conditions, parent-grain cost control.
- `Motion_Roadmap_Next3_2026-07-15.md` (Motion 1 + Shared guardrails) and memory note motion-roadmap-next3-jul15 for the ratified decisions.
- `04-value-repository/Intradiem_Value_Repository.md` for the only claims allowed in copy.
- Then sweep the live Clay workspace via Chrome and read the actual Accounts Master, L2 columns, Contacts, MessageGen column, and critic column so you mirror the live wiring, not just the docs.

## The one design difference that makes this harder than Stars (get this right or the whole thing is off-standard)
Star Ratings personalizes on the prospect's own CMS-derived forgone-QBP dollar, public and verifiable per contract. Cost-Mandate has NO equivalent verified per-account number. So the personalization figure must be the prospect's OWN disclosed number, never an Intradiem-computed one:
- Lead the number on the prospect's own disclosed figure: their stated efficiency or cost-takeout target, the size of an announced RIF, the margin or cost-to-serve language from their earnings, or the count of open reqs. That is their number, quotable and dated.
- The specific fired signal + workforce size carry the rest of the personalization (which mandate, how big the floor).
- NEVER lead with, or include, an Intradiem-computed savings, ROI, recovered-capacity, or idle-percent number. Those are DO-NOT-SEND placeholders. The only Intradiem numbers allowed are verified-repository stats: Humana (healthcare accounts) and the by-vertical public stats labeled "public," used as a proof beat, never as the personalization dollar.
- Block-on-empty (mirror the Stars rule): if there is no prospect-disclosed figure, do NOT fabricate one and do NOT fall back to an Intradiem estimate. Fall back to the qualitative frame (recover idle capacity already on the payroll, no new headcount, no transformation project) with no dollar.

## Skills to run
- cognitive-calibration fires first on its own.
- clay-credit-steward BEFORE any enrichment run: estimate credits, name the motion, state expected yield, get my go/no-go, log a ledger row. No un-budgeted runs.
- intradiem-verified-metrics as the proof gate on every claim.
- intradiem-first-draft-engine then intradiem-copy-sharpener to write the MessageGen copy and the sequence touches.

## Build the layers (mirror L0 to L4; reuse L5 to L8)

**L1 Accounts (net-new cross-vertical universe).** New rows on Accounts Master tagged `motion = cost_mandate`, `is_current_customer` gated out. Firmographic + technographic waterfall (vertical, employee_count, revenue_band, contact-center and/or back-office presence, workforce size), `fit_score`. Enrich cheap-and-broad first; only-run-if-empty and conditional-run on every paid column.

**L2 Cost Signals (point-scored, self-cleaning, mirror the Stars intent layer).** Build the four triggers as point-valued columns, not concepts: `sig_efficiency_mandate_public`, `sig_rif`, `sig_margin_pressure`, `sig_hiring_freeze` (and route `wfm_hiring` in). Give each a point value and tier (Tier 1 fires outreach, Tier 2 raises priority), then an `intent_score` rollup and an `intent_status` formula with the customer-exclusion kill switch inside the score itself (`customer_flag == TRUE => 0/excluded`), exactly like the Stars L2. Put a `new_logo_eligible == TRUE` run-condition on every paid signal column so credits never fire on a customer row. Store points/tiers/thresholds in config (l2 intent signals json), never in the formula text. Reference-scorer + tests parity if you touch the repo side.

**L3 Contacts (Buying Committee segment).** Persona-filtered people on the finance/COO and ops lanes, email waterfall + ZeroBounce (reject invalid), `customer_flag` exclusion, `source_motion = cost_mandate`, `gtm_engine_sourced`/`sourced_date` set at creation read-only, `persona_key` (`cost_finance` / `cost_ops`), `reply_status`, `variant_id`.

**L4a MessageGen (build a cost-mandate system prompt to the v2.2.1 standard).** A full system prompt, not a one-line angle. It must have:
- A token/column map (first_name, job_title, company, vertical, workforce_size, `disclosed_figure` + `disclosed_figure_source` + `disclosed_figure_date`, `top_signal`, `signal_fired_date`, `product_angle` approved-claims-only, `source_motion = cost_mandate` guardrail).
- Persona routing from job_title: Finance/COO leads with the prospect's own disclosed cost figure as the stakes; Ops leads with the mechanism (recover idle capacity on the existing floor), figure late.
- A CORE POSITION never violated: recover idle labor already on the payroll, no new headcount, no transformation project, bookable this fiscal period; concede explicitly that this is not a re-org or a rip-and-replace.
- NUMBER DISCIPLINE per the design note above: the only dollar/percent that may appear is the prospect's own disclosed figure (attributed and dated) or a verified-repository proof stat (Humana / by-vertical public, labeled). Block-on-empty. Never an Intradiem-computed number.
- Copy rules copied from the Stars prompt: no em dashes, contractions always, one idea, front-load, prospect is the hero, the meeting is their idea (offer the artifact, never ask for time), brand-light, the full banned-words list, uncontracted "I would"/"I am" are AI tells.
- Fallback-per-token (never print a blank, placeholder, or token name) and 2 worked examples (one Finance, one Ops).

**L4b Companion critic (build a cost-mandate Terra critic, stricter than Stars).** A separate audit column that PASSes only when every number is either the prospect's own disclosed figure (attributed) or a correctly-attributed verified-repository stat. FAIL any Intradiem-computed savings, ROI, recovered-capacity, idle-percent, or invented figure; FAIL a company-level figure scoped to one unit; FAIL any unlabeled vertical stat. Wire `&&{{msg1_critic Status}} == "PASS"` into the sync run-condition so a FAIL can never sync. Cost-mandate copy is the most tempting place to fabricate a savings number, so this critic is the primary guardrail, not a formality.

**L4c Sequences (5-touch, two lanes, mirror the Stars cadence).** Two lanes, Finance/COO and Ops, each a 5-touch multi-channel cadence (Email 1 with 2 to 3 signal-assigned opener variants, LinkedIn connect, Voicemail + LinkedIn same day, Email 2 new angle, Breakup), merge-field driven off the same tokens so MessageGen personalizes per lead, per-touch angle shift (never a recycled Day 1), signature discipline, staggered committee entry (one lane leads, the other 1 to 2 days behind), distinct bodies and CTAs per committee member. Embed the objection quick-handles (We-Have-WFM, No-Budget, Send-Info, Bad-Timing) from the objection-handler skill.

**L5 to L8 (reuse, do not rebuild).** Route into the existing Send Queue (critic + human approval), Outreach Sync (sender webhook OFF until deliverability green), Reply/Attribution (`reply_status`, funnel, cost per qualified reply, attribution at creation), and AE Worklist. Just add `source_motion = cost_mandate` tags and the reference-table lookups (Verified Metrics, Product-Angle Map, Variant Library).

## Guardrails (hard)
- Exclude current customers via `customer_flag`; pull the customer exclusion list as source of truth. Net-new motion.
- Dry-run and gate-fed: leads sit in Draft until human approval + `msg1_critic` PASS. Nothing sends. Sender is the assigned rep, not me.
- Build tables/columns via Chrome; the Clay MCP cannot create tables. Verify the current Clay UI before any click-by-click; do not instruct from memory.
- Tier enrichment: firmographics broad; waterfall/technographic/signal enrichment only on rows that cleared fit. Parent-grain the paid signals if the universe is contract or subsidiary grain (Stars saved ~3x this way). Sample 10 rows to confirm any unknown per-provider cost before the full run.
- The verified-claims rule lives in both `config/proof.json` and the Clay critic with the same wording.

## Build sequence (prove on a slice, same order as the architecture doc)
1. Read the reference artifacts and sweep live Clay; confirm you are mirroring the Stars layers.
2. Resolve the open scope decision below with me before sourcing.
3. Credit pre-check on a 10-row slice, get my go/no-go, log the ledger row.
4. L1 Accounts (universe + fit) on the slice, then L2 cost signals + intent rollup, verify the customer kill switch zeroes a customer row.
5. L3 Contacts on the slice (persona + valid email + exclusion).
6. L4a MessageGen system prompt, then L4b critic, then run the slice and audit: regen, critic, sync only on PASS, read every rendered draft.
7. L4c sequences pasted as the campaign steps, Draft only, both lanes, staggered.
8. Wire L5 to L8 tags and reference lookups. Sender webhook stays OFF.
9. Update `Clay_Credit_Ledger.md` with actuals; note drift over 25 percent.

## Definition of done
A live, self-cleaning cost-mandate list (fit + point-scored intent, customers auto-excluded in the score), a persona-routed MessageGen system prompt whose only numbers are prospect-disclosed or verified, a companion critic gating sync on PASS, two 5-touch personalized sequences in Draft, and the reply/attribution tags wired, all at the Star Ratings depth. Nothing sent. Match the Stars workbook; if any layer is thinner than its Stars equivalent, it is not done.

## Two decisions that are mine to make (ask me, do not guess)
1. Universe seed source: the cross-vertical net-new universe needs a source (Star Ratings came from CMS, Back Office from the customer file). Ask whether it comes from Sales Navigator, Apollo, an existing TAM export, or a fresh Clay company search on the cost/efficiency signals, and how large the first wave should be.
2. Persona-key convention: RESOLVED 2026-07-15. Canonical = the ICP rubric keys; the engine was normalized from `finance` to `coo_finance` (tests 25/25 green). Use `coo_finance` for the finance/COO persona, do not reintroduce `finance`. No need to ask this again.
