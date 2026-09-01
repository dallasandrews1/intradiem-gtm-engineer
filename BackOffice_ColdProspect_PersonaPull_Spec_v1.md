# Back Office COLD Prospect Sourcing Pull — Spec v1 (Jul 31 2026)

**Purpose:** source the net-new, non-customer account + contact universe for Nate's back-office cold blitz lane. This is Universe 2 (net-new back-office logos), the opposite of the built Clay back-office motion (Universe 1, install-base expansion). Different gate direction, different claims discipline, different home table.

**Why this exists:** the Jul 31 split verified the entire built "Back Office Motion" workbook is `install_base` (current customers, Savannah/AM lane). Nate's cold lane has zero accounts in Clay. This pull builds them.

**Owner split:** Dallas engineers and runs the agent-buildable steps (account seed, `clay search`, dedup gate, signal enrich). The UI-only steps (find-people config, email waterfall wiring, MessageGen columns, campaign attach) get a click-by-click UI sheet when we move to build. Nate never sources; he runs the daily brief.

---

## 0. The three hard rules this pull inverts vs the install-base motion

| Rule | Install-base BO motion (built) | This COLD pull |
|---|---|---|
| Customer status | `customer_flag` is NOT an exclusion; customer IS the target | `fn_eligible` ON: a current customer is EXCLUDED, hard |
| Warm-base beat | "your contact center already runs Intradiem" is the asset | FORBIDDEN. No warm-base beat. Wedge is the homegrown-tracker / WFM-throw-in reframe + the account's own signal |
| Send gate | `owner_cleared` (AE/CSM signs off) | real-row customer-exclusion check the morning of first send; no AE clearance needed (net-new, unowned) |

`source_motion = back_office_cold` on every account and contact, so the two universes never cross-contaminate a campaign.

---

## 1. Home table: stamp from the Golden New-Logo Scaffold

Do NOT build in the install-base "Back Office Motion" workbook. Stamp a fresh workbook from the neutralized donor:

- **Donor:** `Golden New-Logo Scaffold` (wb_0tib7v5msZ2qYbGc4AC). L1 accounts/universe = `t_0tib7x9pjMe9Givg4Dm` (firmographic structure, 0 rows). L3 = `t_0tib7yp7mNKKYX4imrW` (50-col send-ready pipeline, 0 rows).
- **New workbook name:** `Back Office Cold (New-Logo)`.
- **Carry from the donor:** `fn_eligible` wired into every paid column's run condition and the intent score (this is what makes it a cold lane); the 50-col send-readiness pipeline; the critic + voice-audit columns.
- **Stamp trap (documented):** Clay's Duplicate-table action BLANKS all three AI-column prompts (MessageGen / Draft Audit / Voice Audit). Re-populate all three on stamp. See `WFM_Adjacency_Clone_Pack_v1_CORRECTION.md`.
- **MessageGen:** clone `Clay_MessageGen_SystemPrompt_BackOffice_v1.md` and STRIP the warm-base beat section entirely; replace the opener hierarchy with signal-first (account's own why-now) → wedge reframe. Keep the number-discipline law (no Intradiem back-office figure; Humana healthcare-only, contact-center-framed; prospect's own dated figures only). Stamp `msgs_prompt_version = bo_cold_v1.0`.

Alternative if the golden stamp fights us: `motion-stamp` skill builds the same shape from the canonical library in minutes. Golden-scaffold first; motion-stamp is the fallback.

---

## 2. Stage A — the account universe (build BEFORE any contact)

Two-signal method: curated fit seed, then rank by fired signal. A pure firmographic spray over-returns and burns credits on front-office-only companies. HCSC is the template: it qualifies on fit (huge non-customer payer with a claims back office) AND on signal (Cigna integration, Moody's flag, $1.9B loss, CMS clock, live WFM hire).

### A1. Seed the account list (research + `clay search`, ~0 credits to assemble)
Target ~40-60 net-new back-office-heavy accounts, healthcare-payer lane FIRST (sharpest signals, Humana proof travels there), then FS/banking, insurance, BPO. Seed sources:
- `clay search` companies dataset: US, 5,000+ employees, industries = health insurance / banking / insurance / BPO. Treat the return as candidates, not the list.
- Research-built named operators per vertical (the install-base universe was built from real evidence, not a spray; mirror that).
- **First account is HCSC** (already researched, non-customer confirmed, signal-hot). It seeds sprint 1.

### A2. Dedup + exclusion gate (free formulas/lookups, MANDATORY before any spend)
- Add `Install Base Lookup BO Universe` (lookup vs the 101-account install-base universe) + `Customer Flag` (manual, text) columns, then run `fn_eligible`. Only `eligible = TRUE` accounts survive.
- Dedup against: the 101 install-base accounts, the full current-customer exclusion list, and the Stars/WFM/Cost-Mandate universes (don't double-work an account another motion owns).
- **Entity/acquisition flag (do not skip):** `fn_eligible` matches on domain/name and will miss books-of-business that changed hands. Cigna is an install-base customer, but HCSC acquired Cigna's Medicare business (closed Mar 2025) and HCSC is a clean non-customer. Any account touching an acquisition gets a manual `entity_note` and a human clear before it counts. Same trap as the BMO Canadian-parent case.

### A3. Signal enrich (cheap, prioritizes the survivors) — PAID, gated on `eligible = TRUE`
- `Company News` (back-office / claims / cost-takeout / restructuring keywords) and `Company Job Openings` (claims processing, workforce management, back-office, real-time ops keywords). ~2-2.5 cr/result.
- Populate `why_now_bo` (dated signal line) + a simple `bo_signal_score`. Accounts with a fired, dated signal enter the first sprints; the rest are the bench.

---

## 3. Stage B — the buying committee (Director+ , 4 seats, cold framing)

Only on `eligible = TRUE` accounts. Personas and title strings carry from `BackOffice_Persona_Rebuild_UISheet_Jul23.md` (Mary Ann-validated), Director+ hard gate.

| persona_key | Seat | Titles (from the rebuild sheet) | Cap/account |
|---|---|---|---|
| `ops_leader` | In the fire | VP/Director Claims, Claims Operations, Appeals, Grievances, UM; VP/Dir Payment Ops, Disputes, Collections, Shared Services, Enrollment, RCM | 1-2 |
| `bo_product_owner` | Tool owner | Director+ Workforce Management/Planning/Engagement, Real-Time Operations, Back Office Workforce, Middle Office Product Owner | 1 |
| `bo_claims_it` | Tool decision | Director+ Claims Technology/Systems/Applications, Operations Technology, Business Systems | 1 |
| `exec_coo` | Strategizing | COO, SVP/EVP Operations, Head of Operations | 1 |

- **Hard gate:** Director, Sr Director, VP, SVP, EVP, C-level only. Exclude Manager/Analyst/Specialist/Coordinator/Lead (Mary Ann's line).
- **`wfm_status` segmentation:** `wfm_deployed` accounts source all four; `no_wfm` accounts skip `bo_product_owner`. Seed blank = treat as `wfm_deployed` until confirmed.
- Committee size 4-8/account. Nobody added to hit a number.
- Cold framing note baked into the contact tags: `warm_base_beat = FALSE` (belt-and-suspenders so MessageGen can't reach for the install-base asset).

---

## 4. Stage C — enrichment waterfall (tiered, cheap-before-premium)

1. **Free first (0 cr):** `persona_key` (fn_persona_key), `function`, `seniority_gate`, `fn_eligible`, dedup lookups. Drop `out_of_icp` and below-Director rows HERE, before any spend.
2. **Paid, only on survivors:** email waterfall + ZeroBounce verify (~1.5 cr/contact, ledger-verified from the 59-contact / 86-cr install-base run). `fn_email_verified` gate.
3. **Phones:** Clay does no phone numbers. Flag ZoomInfo as the separate source for voicemail/call touches (the blitz needs numbers). Not in this Clay pull.
4. **Wave-only, per-contact:** `li_recent_post_hook` (relevance-filtered), Required-to-run OFF, fired only on staged wave rows.

---

## 5. Credit pre-estimate (live balance 60,844, pulled Jul 31; 5,000/mo is the self-imposed operating budget)

Per-provider working rates from `Clay_Credit_Ledger.md`: company enrich ~2 cr, news/jobs signal ~2-2.5 cr/result, email waterfall + ZeroBounce ~1.5 cr/contact, formulas + internal lookups 0.

| Step | Scope | Est. credits |
|---|---|---|
| **Sample (HCSC only)** | 1 account signals + ~6-8 contacts email/verify | **~15** |
| **Sprint-1 batch** | ~12 accounts: enrich + news + jobs (~4.5 cr/acct) + ~60 contacts email/verify (~90) | **~145** |
| **Full universe** | ~50 accounts + ~250-300 contacts | **~575-650** |

- Trivial against the 60,844 balance; the 5,000/mo budget is the real governor, so pace it: sample → sprint-1 batch → scale only after the criteria hold.
- **Sample-first gate:** run HCSC alone, eyeball the ~6-8 contacts for seniority/function/fit before spending on the batch. This is the credit-disciplined equivalent of the "sample 50 then scale" rule.
- Log every run in `Clay_Credit_Ledger.md` under motion `back_office_cold`.

---

## 6. The gate-semantics law (load-bearing, real rows only)

`fn_eligible` depends on real null-vs-empty column semantics, and `Customer Flag` is stored as TEXT `"TRUE"`, not a boolean. A synthetic `--input` smoke test can "prove" the gate excludes customers while a real row slips one into the cold campaign. So:
- `--input` is fine for building/testing the pull structure.
- The FINAL customer-exclusion validation runs on REAL rows (the actual sourced accounts), the morning of first send, never on synthetic data. This is the last gate before Nate's first touch.

---

## 7. Build order (dependency-correct, nothing lands before its prerequisite)

1. Stamp `Back Office Cold (New-Logo)` from the golden scaffold; re-populate the 3 AI prompts; strip the warm-base beat from MessageGen. *(agent + UI)*
2. Assemble the account seed (HCSC first, then the healthcare-payer lane). *(agent: `clay search` + research)*
3. Wire `Install Base Lookup` + `Customer Flag` + `fn_eligible`; dedup; flag entity/acquisition cases. *(agent, free)*
4. Signal enrich the `eligible = TRUE` survivors; populate `why_now_bo` + `bo_signal_score`. *(agent, paid, gated)*
5. **HCSC sample:** find-people the 4 seats on HCSC only, Director+ gate, ~6-8 contacts; email/verify; human eyeball. *(UI find-people + agent enrich, ~15 cr)*
6. On sample pass: scale to the sprint-1 batch (~12 signal-hot accounts). *(UI + agent)*
7. Real-row exclusion check → hand the first two accounts to the daily brief. *(agent, send-morning gate)*

Steps 1 and 5 need Dallas's hands in Clay (find-people config, MessageGen paste, campaign attach); those get a UI sheet at build time. Everything else is agent-run from here.

---

## 8. What this pull is NOT
- Not a re-source of the install-base universe (that's built and owned by Savannah/AM).
- Not a send. Every output stops at the human approval gate + the real-row exclusion check.
- Not a home for any Intradiem back-office outcome number (none is approved). Humana is healthcare-only, contact-center-framed; otherwise the prospect's own dated figures or the qualitative wedge.
