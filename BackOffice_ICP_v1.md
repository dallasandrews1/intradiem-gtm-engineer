# Back-Office ICP — v1 (execution-ready, Jul 13 2026)

**Status: v1, execution-ready.** Built from real evidence, not a straw-man: the actual Intradiem install base (SF Active Customers export, 101 accounts), the Back Office Optimizer product definition, and Intradiem's own house persona rubric (`ref_ICP_Persona_Rubric.csv`) and product-angle map (`ref_Product_Angle_Map.csv`). Supersedes `BackOffice_ICP_v0.md`. The engine, the target-account universe, and the persona-pull spec are all wired to this. The single remaining decision is the credit go on the pull — nothing else is gated.

Owner checkpoint preserved by design, not as a blocker: the first 50 sourced contacts get reviewed with the account owners (AE/CSM) before the pull scales. That review protects reply rates and install-base relationships; it is a quality gate, not a build gate.

## The motion in one line

Sell **Back Office Optimizer** into the back offices of companies whose **front offices already run Intradiem** — expansion inside a warm install base, sourced by us because front-office contacts can't hand these leads over. Mandate 3's 200 contacts come from here.

## Why this is a fork, not a copy (the engine already enforces it)

The Stars motion drops customers to zero. This motion **inverts** that — the customer *is* the target:

- `customer_flag` is **not** an exclusion here.
- `fo_risk_flag` suppresses (an account in renewal escalation or open front-office risk is a bad expansion target) until the owner clears it.
- `install_base` is a warm base score of 10 — every qualified account surfaces before any external signal fires, so the list is never empty.
- `owner_cleared` is a send gate: an account scores and counts, but isn't sendable until its AE/CSM signs off.

Encoded in `motion_overrides.back_office`; verified 61/61 in the test suite with a Stars-parity guard.

## Product grounding (what we're actually selling)

Back Office Optimizer applies Intradiem's real-time workforce automation to structured back-office production work: **claims processing, appeals/grievances, utilization management, payment operations, disputes, collections, document processing, underwriting support, enrollment, medical coding, patient scheduling, billing/RCM, order management and fulfillment exceptions.** The platform watches live queues and backlogs and acts automatically — reassigning tasks, triggering training in idle windows, rebalancing workloads in seconds.

Public positioning claims (Intradiem website, **public-site not repository-verified** — do not use as Intradiem-verified proof in prospect copy without clearing the verified-metrics gate): ~$7 returned per $1, payback under 3 months, 6–10% productivity lift in weeks; one large health/wellness org cited 18.4% productivity boost and 15.4× ROI. The only repository-verified customer story remains Humana (contact-center). Treat all back-office ROI as unverified until sourced; the ICP does not depend on it.

## Firmographic definition

Existing-customer accounts (universe 1) with material back-office transaction-processing operations in the six verticals, prioritized by how concentrated and regulated that back-office work is. FTE floor: target functions of ~200+ back-office FTEs; sample and confirm rather than hard-gating on estimated headcount.

## Target-account universe (real, built — `BackOffice_Target_Universe_v1.csv`)

All 101 install-base accounts classified and tiered. Every row is a real current customer; the back office is the expansion surface.

| Tier | Accounts | Verticals | Primary back-office function → angle |
|---|---|---|---|
| **1 (lead)** | 56 | Healthcare Payer (20), Financial Services/Banking (25), Insurance (9), BPO/Outsourcer (2) | Claims / appeals / grievances / UM; payment ops / disputes / collections; multi-function BPO → **BOO** |
| **2 (expansion)** | 35 | Healthcare Provider (18), Utilities (9), Telco/Cable (8) | RCM / coding / scheduling / billing; billing / service-order processing → **BOO** |
| **3 (opportunistic)** | 10 | Retail (3), Travel (3), Review/unmapped (4) | Order mgmt / returns / fulfillment exceptions → **BOO** |

Tier 1 alone (56 accounts × up to 4 contacts) is enough to fill the 200. The pull runs **Tier 1 first**; Tier 2 is the expansion bucket; Tier 3 is opportunistic and only sourced if a signal fires.

Named Tier-1 anchors already in the base: Aetna/UHG/Humana/Elevance/Cigna/CVS/Molina/HCSC/Optum (payers); JPMorgan, Wells Fargo, Goldman Sachs, TD, RBC, US Bancorp, PNC, Synchrony, SoFi (FS/banking); MetLife, Prudential, Guardian, Travelers, Farmers, Assurant (insurance); Capita, Foundever (BPO). These are warm logos — the front office is already a customer.

**Provider caveat (built into the tiering):** several provider rows (Kaiser deployments, etc.) are clinical-side footprints. Provider back-office = revenue cycle, coding, billing, scheduling — *not* clinical. Confirm with the CSM that a back-office motion fits before sourcing a heavily-clinical account; the tiering flags providers as Tier 2 for exactly this reason.

## Personas (house rubric, Director+ / VP+)

| persona_key | Titles to pull | Role |
|---|---|---|
| `bo_claims` | VP/Director Claims, Claims Operations, Appeals, Grievances, Utilization Management | Primary pain owner (payer/insurance) |
| `bo_shared` | VP/Director Payment Operations, Disputes, Collections, Document Processing, Shared Services, Enrollment, Underwriting Support, RCM | Primary buyer (FS, provider, BPO) |
| `coo_finance` | COO, SVP/VP Operations, CFO, VP Finance (cost owner) | Economic buyer — enters later in the sequence, never the first touch |

**Exclusions (hard):** IT/Security (CIO, CTO, VP IT — RPA owners are an objection source, not the buyer); Clinical (CMO, nursing); Legal/Compliance; Sales/Marketing/HR; contact-center titles already covered by the front-office relationship; functions under ~50 FTEs.

## Pain map (feeds the copy skills at launch, per persona)

- **`bo_claims`:** backlog that regrows every Monday, aging claims/appeals queues, TAT and SLA penalties, overtime spend, quality-rework loops, seasonal/enrollment surges staffed by guesswork.
- **`bo_shared`:** cost-per-transaction scrutiny, multi-function queues with no real-time visibility, utilization they can't prove, disputes/collections aging, hybrid-workforce oversight.
- **`coo_finance`:** capacity without headcount; the idle time already being paid for; the fact that the back office has no equivalent of the contact center's real-time discipline. The one-idea family: **the back office runs on yesterday's report; the cost lives in what happens between reports.**

Product tells ("workforce orchestration" and kin) stay out of the copy in this motion too; all sends run first-draft-engine → copy-sharpener → verified-metrics gate.

## Signal taxonomy (wired, scores under `active_motion = back_office`)

`bo_cost_mandate` (20/T1), `sla_penalty_backlog` (20/T1), `bo_hiring_cluster` (15/T2), `bpo_transition` (15/T2), `claims_backlog_news` (10/T2), `transaction_volume_surge` (10/T2). Tier 1 fires an account into outreach; Tier 2 raises priority within the fired set. Same recency/cap behavior as Stars.

## Qualification, dedup, hygiene

1. Dedup against the install-base contact set and existing Clay tables **before** enrichment spend (credit-steward pre-check; cheap columns before premium waterfalls).
2. One accountable owner per account motion; back-office campaigns inside a customer coordinate with that account's AE/CSM before any send. `owner_cleared` enforces this in the engine.
3. Every sourced contact carries: `universe` (install_base), `persona_key`, `function`, `fte_band` estimate, `source`, `sourced_date`, `parent_account`. The 200 is countable only because the tags exist from contact one.
4. Suppression: accounts in active renewal escalation or open risk (`fo_risk_flag`) are excluded until the owner clears them.

## What's built and waiting vs. the one open decision

**Built (0 credits):** ICP v1 (this), the tiered real target universe (`BackOffice_Target_Universe_v1.csv`), the engine fork wired to the real universe (101 accounts scoring, base + gates live), the signal taxonomy, and the persona-pull spec (`BackOffice_PersonaPull_Spec.md`).

**The one open decision:** the credit go on the persona pull that sources the ~200 contacts. Pre-estimated in the pull spec, ledger-ready, sample-50-then-scale. That's a spend decision, so it's yours to trigger — everything up to it is done.
