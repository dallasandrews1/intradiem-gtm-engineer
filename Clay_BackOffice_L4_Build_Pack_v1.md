# Back Office Motion — L4 Build Pack (v1.0, Jul 16 2026)

**The one-pass transcription spec for the Back Office Motion workbook's messaging layer: token map, column config, run conditions, campaign settings, gates, and the Wave 1 plan.** Built files-first per the structure law (Golden Standard §1); transcribe into Clay in one pass via Chrome, verify live. Companion: `Clay_MessageGen_SystemPrompt_BackOffice_v1.md` (the prompt + critic text this pack wires).

**Design goal:** Stars-level personalization (per-persona routing, why-now, disclosed figures, LinkedIn post hook) with the blank-input failure class engineered OUT. Every rule in Section 2 exists because of a documented Stars breakage: the snake_case unify fields that wiped on every Contacts row (Jul 15), "Some inputs missing" hard-fails on optional chips, and campaign-side overrides reverted by sync re-runs.

---

## 0. Live state this pack builds on (verify via Chrome before transcribing; the live page wins)

- Workbook: **Back Office Motion** (wb_0ti4jh8ATmjiCowc7JM). Universe table: 101 install-base accounts, `intent_score_bo` + `intent_status_bo` + 6 `sig_bo_*` checkbox columns live. Gates at rest: `fo_risk_flag` FALSE, `owner_cleared` FALSE.
- People table: 59 sourced contacts (auto-named "Senior Claims Executives UK US"), email waterfall + ZeroBounce complete, 86 credits meter-verified.
- Not yet built: persona/tag hygiene on the people table, the token layer, MessageGen + critic, campaigns. That is this pack.
- Nothing here spends credits or touches the GTM Engine workbook. Every paid or send-adjacent step is explicitly gated below.

## 1. Prerequisite hygiene queue (0 credits, do first)

1. Rename the people table → **BO_Contacts**.
2. `persona_key` formula column from Job Title, rubric-canonical keys only (`ref_ICP_Persona_Rubric.csv`): claims/appeals/grievance/utilization → `bo_claims`; payment/disputes/collections/document/shared services/enrollment/underwriting/revenue cycle → `bo_shared`; COO/operations/CFO/finance → `coo_finance`; anything else → `out_of_icp`.
3. `function` formula column (claims / payment ops / disputes / shared services / enrollment / RCM / doc processing) from the same title strings; MessageGen uses it to name their world.
4. Flag-and-hold the known sample noise as `out_of_icp` (IT and HR flavored Shared Services matches, the Humana Medical Director) rather than deleting; the owner review sees them.
5. `dup_vs_contacts` lookup flag vs Contacts (Buying Committee) (Lisa Stephens / Humana is the confirmed suspect).
6. Tag columns, set once, read-only after: `universe` = install_base, `source_motion` = back_office, `sourced_date` = 2026-07-14, `sourced_by` = clay_find_people, `parent_account` (lookup to universe table).
7. Wave columns: `wave_number` (blank until assigned), `wave_status` (staged / enriched / drafted / launched / done), `msgs_prompt_version`.
8. Export the owner review sheet (all 59 with persona_key, function, flags) for the Scott/AE 50-contact review. The review gates SENDING and SCALING, not drafting.

## 2. The token layer (the anti-blank architecture)

Six rules, each mapped to the failure it prevents:

| # | Rule | Failure it prevents |
|---|---|---|
| 1 | **Bind MessageGen chips directly to origin columns** (Find People originals, typed columns, Lookups). No formula-intermediary rename layer: do not build snake_case mirror columns of populated originals just to feed tokens. The token map in the prompt file names the binding per token. | The Jul 15 Stars wipe: a snake_case unify layer recomputed against a re-sent source and blanked on every row, killing MessageGen's whole input map. Fewer moving columns, nothing to wipe. |
| 2 | Where a derived value is genuinely needed (`persona_key`, `function`, coalesces), it is ONE formula column reading only stable in-table originals, never chained formula-on-formula, and never a column a source re-send can overwrite. | Dependency-chain blanking; one recompute cascading through the token map. |
| 3 | **Every optional chip: Required-to-run OFF.** Optional set: `li_recent_post_hook`, `why_now_bo`, `disclosed_figure`, `disclosed_figure_source`, `fo_deployment_note`. | "Some inputs missing" hard-fails that blank cells and wipe existing drafts on re-run (Golden Standard §15). |
| 4 | **`tokens_ready` gate column** (formula, 0 credits): TRUE only when every REQUIRED token is non-empty — First Name, Job Title, Company, `persona_key` (≠ out_of_icp), `email_status` = valid, `source_motion` = back_office. MessageGen's run condition requires it. | The error message class entirely: generation cannot fire on an incomplete row. Incomplete rows collect in a "Blocked: tokens" view to be fixed as DATA, not as copy. |
| 5 | Block-on-empty inside the prompt (never print a blank, placeholder, or token name; per-token fallback rules). | Rendered emails with holes or leaked snake_case names. |
| 6 | **only-run-if-empty on every paid enrichment; never re-run MessageGen or sync over a wave carrying campaign-side per-lead overrides.** Draft fixes happen per-lead in the campaign; permanent fixes at source are a separate, post-launch task. | Double-spend, non-deterministic re-rolls reintroducing figure errors, and override reverts. |

### Column spec (BO_Contacts, transcribe in this order)

| Column | Type | Source / formula sketch | Run condition | Credits |
|---|---|---|---|---|
| persona_key | Formula | title-string map per §1.2 | always | 0 |
| function | Formula | title-string map per §1.3 | always | 0 |
| parent_account, tier, vertical | Lookup | BO universe table by company/domain | always | 0 |
| fo_risk_flag, owner_cleared | Lookup | BO universe table (account-grain gates) | always | 0 |
| why_now_bo | Text (manual/agent-fill later) | dated evidence line for the fired `sig_bo_*` signal; account-grain, filled at wave time | n/a (input) | 0 now |
| disclosed_figure / _source | Text | prospect's own stated number + source, captured at wave research | n/a (input) | 0 |
| fo_deployment_note | Text or Lookup | what their front office runs (from install-base/SF knowledge) | n/a (input) | 0 |
| li_recent_post_hook | Enrichment ("Get a person's professional posts and shares") + relevance filter | per contact | `tokens_ready && wave_status == "staged" && fo_risk_flag != TRUE` | PAID, wave-only |
| tokens_ready | Formula | AND of required-token checks per rule 4 | always | 0 |
| MessageGen Email 1 (BO) | AI (Claude Sonnet 5) | prompt file §2 | `tokens_ready == TRUE && source_motion == "back_office" && fo_risk_flag != TRUE && wave_status == "staged"` | PAID (AI), wave-only |
| Draft Audit (BO) / msg1_critic_bo | AI (GPT critic) | prompt file §4 | `MessageGen Email 1 (BO)` non-empty | PAID (AI), wave-only |
| Sync leads to campaign (BO P1/P2) | Campaign sync | per lane | `msg1_critic_bo == "PASS" && owner_cleared == TRUE && !bdr_claimed && email_status == "valid" && source_motion == "back_office"` | 0 |

Auto-run OFF on every paid column; runs are manual, per wave slice, after the ledger row exists. Verify the current Clay UI before transcribing any click-by-click (§15 gotchas apply: no Create Claygent, read fresh Sent At after sync, run-condition preview grid lies).

## 3. Personalization parity checklist (what "same level as Stars" means here)

| Layer | Stars implementation | BO implementation (this pack) |
|---|---|---|
| Persona routing | P1 Stars/Quality vs P2 Finance | bo_claims / bo_shared / coo_finance, three lead structures |
| Account why-now | QBP window + CMS math | fired `sig_bo_*` signal evidence, dated, 90-day freshness rule |
| Personalizing number | CMS-derived QBP dollars (public data) | **prospect-disclosed figures ONLY** (no public-math equivalent exists; the qualitative frame is the sanctioned fallback, never an estimate) |
| Warm asset | none (cold) | fo_deployment_note: their own front office runs Intradiem (BO's structural advantage over Stars) |
| Individual hook | li_recent_post_hook, optional, relevance-filtered | identical column and rules, per-contact, wave-gated |
| Figure gate | Terra v3 critic + PASS sync condition | Draft Audit (BO) critic + PASS-AND-owner_cleared sync condition |

## 4. Campaign settings (build in Draft, nothing launches)

- **Lanes:** one campaign per persona. `BO P1 - Claims Ops` (bo_claims), `BO P2 - Shared Services & Payment Ops` (bo_shared). `coo_finance` contacts are NOT a Day-1 lane: they enter on day 3+ via a third small campaign (`BO P3 - Ops & Finance`) after their account's P1/P2 contact is in motion, per ICP ("economic buyer enters later, never the first touch").
- **Sequence:** the 5-touch, ~9-business-day house standard (Email 1 → LinkedIn connect → voicemail + LinkedIn message → Email 2 new angle → breakup). Merge fields point at the MessageGen output fields; Email 2 and breakup copy get drafted through first-draft-engine → copy-sharpener before any wave launches (separate task, not this pack).
- **Settings:** plain text (no open tracking, ever), same-company pause ON, staggered committee entry (never two lanes at one account on Day 1), sender = the owning rep (never Dallas), sender webhook OFF until deliverability is green, ~20 sends/day starting ceiling.
- **Hard rules carried from Stars:** never "Save" a Contacts-sourced campaign (expand via load list only); per-lead overrides are campaign-side and revert on sync re-run, so no sync re-runs after overrides exist; verify fresh `Sent At` per row after any sync.

## 5. Wave 1 plan + credit gate (HELD until explicit go)

- **Universe status:** sourced once (59 in BO_Contacts from the 15 Tier-1 sample accounts). Wave 1 pulls from this standing table; no new sourcing. The scale-to-200 pull (~300 cr re-priced) is a separate, later decision gated on the owner review.
- **Wave 1 slice:** 30 to 40 of the 59: rows with `tokens_ready` TRUE, `persona_key` ≠ out_of_icp, `dup_vs_contacts` clear, prioritized by accounts the owner review clears first. Set `wave_number` = 1, `wave_status` = staged, `msgs_prompt_version` = bo_v1.0.
- **Credit estimate (to be confirmed by a 10-row sample before the full slice, per governance):** li_recent_post_hook ~1 to 2 cr × ~40 = 40 to 80 cr; MessageGen + critic AI runs ≈ 40 to 80 cr combined. **Wave 1 ≈ 100 to 160 credits**, inside the ~1,414 remaining of the BO allocation (86 of ~1,500 used). Ledger row appended BEFORE the run; >25% drift → re-estimate and note cause.
- **Order of operations:** hygiene (§1) → owner review export → 10-row priced sample → ledger row → Wave 1 enrich + generate + critic → census every draft → per-lead fixes → load lanes (Draft) → owner_cleared flips per account → launch only on explicit approval → **schedule the Wave 2 check (~9 business days out) before calling Wave 1 launched.** No Wave 2 until Wave 1 replies are read; learnings bump the prompt version first.
- **Sequencing note (Jul 16):** everything in this pack is file-side today. No MessageGen, sync, or enrichment runs anywhere, and the GTM Engine workbook stays untouched per the standing freeze around the Thursday launch window.

## 6. Definition of done (Stars parity, per the Runbook)

A live self-cleaning BO_Contacts segment (persona + valid email + gates), a MessageGen prompt built to the v2.2.3 contract with only prospect-own or verified numbers, a critic gating sync on PASS AND owner_cleared, personalized 5-touch persona-lane sequences in Draft, wave and attribution tags wired, `tokens_ready` making input errors structurally impossible, and nothing sent. If any layer is thinner than its Stars equivalent, it is not done.
