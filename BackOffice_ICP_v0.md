# Back-Office ICP — v0 straw-man (Jul 13 2026)

**Status: v0, unratified.** This is the hypothesis, not the ICP. Every line here is written to be corrected by Scott Kemme; his edits become v1. Nothing gets sourced against this until that conversation happens. Standing up the *engine* around it (config, scorer, table architecture) is done and costs nothing; sourcing the 200 contacts is the one paid step, held for ICP ratification.

## The two universes — do not conflate

1. **Install-base back office (Mandate 3, the 200).** Contacts in the *back* offices of companies whose *front* offices are already Intradiem customers. We source them ourselves (front-office contacts can't hand these over), then run campaigns inside our own install base. This is the motion the engine fork is built for.
2. **Net-new back-office logos (BOO launch universe).** Back-office-heavy companies with no Intradiem relationship. Same personas, different motion, no customer warmth to lean on, stricter claims discipline.

A contact counts toward the 200 only if it is universe 1, matches a persona below, and survives dedup.

## Why the engine treats this motion differently (the fork, not a copy)

The Stars motion self-cleans by dropping customers to zero — a current customer is not a new-logo target. The install-base back-office motion **inverts** that: the customer's back office *is* the target, so `customer_flag` is not an exclusion here. In its place:

- **Front-office risk suppresses.** An existing customer in active renewal escalation or open front-office risk is a bad expansion target; it drops to intent 0 (`suppressed_risk`) until the account owner clears it. Reads the signal engine's risk read.
- **The warm relationship is a base score.** Every qualified install-base account surfaces at a base intent (`install_base`, 10) before any external signal fires — the analogue of the Stars new-faller base, so the list is never empty while signals accrue.
- **Owner-cleared is a send gate, not an intent kill.** A back-office campaign inside a customer coordinates with that account's AE/CSM before any send. An uncleared account still scores and counts; it just isn't sendable yet (`pending_owner`).

This is encoded in `motion_overrides.back_office` in `l2_intent_signals.json` and verified in the test suite (61/61), including a parity guard that the Stars motion is unchanged.

## Firmographic hypothesis

Companies across the six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities) with 200+ back-office FTEs in transaction-processing functions. Existing customers first, weighted by front-office deployment health — check the signal engine's risk signals before including; a struggling front-office account is a bad expansion target.

## Function hypothesis (where manual back-office work concentrates)

- Claims processing and adjudication (insurance, healthcare)
- Payment operations, disputes, chargebacks (financial services)
- Order management, returns, fulfillment exceptions (retail)
- Service-order and field-dispatch processing (telecom, utilities)
- Document processing, underwriting support, onboarding/KYC (financial services, insurance)

## Persona hypothesis (Director and above)

| persona_key | Titles | Role in the deal |
|---|---|---|
| `bo_claims` | VP/Director Claims Operations, Claims Transformation, Adjudication | Primary pain owner |
| `shared_services` | VP/Director Shared Services, Back Office Operations, Operations Support | Primary buyer |
| `payment_ops` | VP/Director Payment Operations, Disputes, Chargebacks | Primary pain owner (FS) |
| `doc_processing` | VP/Director Document Processing, Underwriting Support, Onboarding/KYC | Secondary pain owner |
| `ops_excellence` | Head of Operational Excellence / Process Improvement | Champion, rarely the buyer |
| `coo_finance` | COO, SVP Operations | Economic buyer — enters later, never in the first pull |

## Exclusions hypothesis

Pure front-office titles; IT/engineering titles (RPA owners are an objection source, not the buyer); contact-center titles already covered by the install-base relationship; functions under 50 FTEs.

## Pain map (feeds the copy skills downstream, per persona)

- **Claims / payment ops leaders:** backlog that regrows every Monday, aging queues, overtime spend, SLA penalties, quality-rework loops, seasonal surges staffed by guesswork.
- **Shared services leaders:** cost-per-transaction scrutiny, multi-function queues with no real-time visibility, utilization they can't prove, hybrid-workforce oversight.
- **COO tier:** capacity without headcount, the invisible idle time already paid for, the fact that the back office has no equivalent of the contact center's real-time discipline. The one-idea family: *the back office runs on yesterday's report; the cost lives in what happens between reports.*

## Signal taxonomy (the moat, wired into the engine now)

Six back-office buying signals score under `active_motion = back_office`:

| signal | pts | tier | reads |
|---|---|---|---|
| `bo_cost_mandate` | 20 | 1 | public cost-out / efficiency / restructuring mandate (buyer naming the problem) |
| `sla_penalty_backlog` | 20 | 1 | regulatory/contractual SLA penalty or mandated backlog remediation |
| `bo_hiring_cluster` | 15 | 2 | ≥3 back-office reqs (claims/payment/processing/shared services) in trailing 30d |
| `bpo_transition` | 15 | 2 | BPO contract change / in-sourcing / outsourcing RFP (workforce in flux) |
| `claims_backlog_news` | 10 | 2 | claims backlog / operational-strain news |
| `transaction_volume_surge` | 10 | 2 | enrollment/claims/payment volume surge |

Tier 1 fires an account into outreach; Tier 2 raises priority within the fired set. Same recency and cap behavior as the Stars motion.

## Dedup, hygiene, tags

1. Dedup against the install-base contact set and existing Clay tables **before** enrichment spend (credit-steward pre-check; cheap columns before premium waterfalls).
2. One accountable owner per account motion; back-office campaigns inside a customer coordinate with that account's AE/CSM before any send. Their account, our machinery.
3. Every contact carries: `universe` (install-base vs net-new), `persona_key`, `function`, `fte_band`, `source`, `sourced_date`. The 200 is countable only because the tags exist from day one.
4. Suppression: accounts in active renewal escalation or open risk are excluded until the owner clears them (`fo_risk_flag` / `owner_cleared` in the engine).

## What's ratified vs open (bring to Scott)

Open questions to hand him as "tear this up":

- Is the 200 FTE floor right, or does it exclude mid-market back offices worth pursuing?
- Which vertical leads — is healthcare claims the wedge, or is FS payment ops the faster path?
- Is `coo_finance` really late-sequence, or does the economic buyer need to be in the first pull for this motion?
- Are there install-base accounts he'd hard-exclude regardless of signal (strategic sensitivities the risk flag won't catch)?
- Confirm the AE/CSM coordination rule and who clears an account.

Log every correction with a date; v1 = post-Scott.

## Output chain

`BackOffice_ICP_v0.md` (this) → correct with Scott → `BackOffice_ICP_v1.md` → persona-pull spec → sample 50, review → scale → feeds Mandate 3 campaigns + the BOO launch kit; pain map feeds the copy skills; counts feed the Friday readout.
