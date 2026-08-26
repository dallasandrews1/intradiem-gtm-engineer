# Back-office motion — ICP v1 built, universe wired, pull ready (Jul 13 2026)

Follows `20_BackOffice_Motion_Fork_Jul13`. That stood up the engine fork on a straw-man; this replaces the straw-man with a real, execution-ready ICP and target universe. The motion is now built and waiting on one thing: the credit go on the pull.

## What changed from v0 → v1

v0 was a hypothesis to bring to Scott. v1 is built from evidence and does not wait on him — grounded in:

- **The real install base** — SF Active Customers export (101 accounts), which IS universe 1 (front-office customers whose back offices we target).
- **The real product** — Back Office Optimizer's actual functions (claims, appeals/UM, payment ops, disputes, collections, doc processing, underwriting, coding, RCM, scheduling, order mgmt).
- **Intradiem's own taxonomy** — the house persona rubric (`ref_ICP_Persona_Rubric.csv`) and product-angle map (`ref_Product_Angle_Map.csv`), which already route these functions to BOO and define the buyer personas (`bo_claims`, `bo_shared`, `coo_finance`).

The Scott conversation becomes a 50-contact quality review, not a build gate.

## Built (all 0 credits)

1. **`BackOffice_ICP_v1.md`** — execution-ready ICP: firmographics, tiered account universe, personas, exclusions, pain map, signal taxonomy, qual/dedup rules, credit posture. Supersedes v0.
2. **`BackOffice_Target_Universe_v1.csv`** — all 101 install-base accounts classified and tiered: 56 Tier 1 (payers, FS/banking, insurance, BPO), 35 Tier 2 (providers, utilities, telco), 10 Tier 3 (retail, travel, review). Each row tagged with vertical, primary function, product angle, personas, contact cap, and the engine gate fields.
3. **Engine wired to the real universe** — `intradiem-signal-engine/data/l2_accounts_backoffice.csv` is now the 101 real accounts. Verified run: all 101 score the install-base base (10), all held `pending_owner`, 0 sendable until an AE/CSM clears. Tests still 61/61 green.
4. **`BackOffice_PersonaPull_Spec.md`** — the Clay run: title strings per persona, caps to land ~200 (Tier 1 first), dedup keys, enrichment tiering, tag schema, credit pre-estimate.
5. **Ledger row** — persona pull pre-estimated (sample ~150–250, full ~600–900 credits), logged as **HELD, 0 consumed**, inside the ~1,500/mo back-office allocation.

## Now LIVE in Clay (built via browser, Jul 13, 0 credits)

The motion is no longer just an engine spec — the table exists in Clay. Separate workbook **Back Office Motion** (isolated from the GTM Engine / Stars workbook, one workbook per motion), table **BackOffice_Target_Universe_v1**:

- 101 real install-base accounts imported (all 16 tag columns), Tier 1 sorted to top.
- `intent_score_bo` (Number, formula): `fo_risk_flag=="TRUE" ? 0 : (install_base=="TRUE" ? 10 : 0)` — the inverted gate, computing 10 for every current-customer row (the exact opposite of the Stars table, where a customer is forced to 0).
- `intent_status_bo` (formula): suppressed_risk / grade_lift(≥40) / in_motion / pending_owner / dormant — currently **pending_owner** for all 101 (base score present, no owner cleared yet).
- Gate fields at correct resting state: `fo_risk_flag=FALSE`, `owner_cleared=FALSE` for all — nothing sendable until a real AE/CSM clears it. No enrichment run; 0 credits.
- `total_licenses` cleaned: switched to Text and cleared the 8 `#Error!` cells that came in from the SF export (Citicorp, Goldman, PNC, CVS Health PBM, Auto & General, Travelers, Cleveland Clinic, Charter). Source CSV also de-errored via sed.

**Signal columns wired (Jul 13, 0 credits).** Added the 6 back-office signals as checkbox inputs — `sig_bo_cost_mandate`, `sig_sla_penalty`, `sig_bo_hiring`, `sig_bpo_transition`, `sig_claims_backlog`, `sig_transaction_surge` — all unchecked at rest. Extended `intent_score_bo` to sum them on top of the base with the fo_risk gate: `fo_risk_flag=="TRUE" ? 0 : (install_base?10 + cost_mandate?20 + sla_penalty?20 + bo_hiring?15 + bpo_transition?15 + claims_backlog?10 + transaction_surge?10)` (max = 100 exactly, no cap needed). Verified live by checking two signals on one row → score 10→50, status pending_owner→grade_lift, then reverted. Signals are the credit-gated inputs: a human sets them now, the paid enrichment populates them at go. Table stays 10/pending_owner at rest.

Workbook: `app.clay.com/workspaces/1180800/workbooks/wb_0ti4jh8ATmjiCowc7JM`.

## The one open decision

The credit go on the persona pull. Sample 50 → lock the per-contact rate → review with owners → scale to 200. That is a spend decision and therefore yours to trigger. Everything up to it — ICP, universe, engine, spec, credit plan — is done and waiting.

## Sequence from go

1. **Go** → run the 50-contact sample (Tier 1). *(first credit spend)*
2. Review the 50 with AE/CSM owners; tune title strings / caps; clear accounts (`owner_cleared`).
3. Scale to ~200 across Tier 1.
4. Contacts land in the engine table → signals attach → per-contact copy via first-draft-engine → copy-sharpener → verified-metrics.
5. Counts + cost-per-contact into the Friday readout; wire the closed loop once the sequencer produces events.
