---
name: intradiem-backoffice-icp
description: "Back-office ICP builder for Mandate 3 (200+ back-office contacts) and the BOO launch universe. Holds the ICP straw-man hypothesis to bring to Scott Kemme, the back-office persona pain maps (claims ops, shared services, document processing, payment ops), qualification and dedup rules against install-base contacts, and the sourcing spec for the Clay persona pull. Trigger on: back-office ICP, who buys back office, 200 contacts, back-office personas, BOO targeting, source back-office contacts, prep for the Scott Kemme conversation, back-office qualification rules. Load proactively when any back-office sourcing, targeting, or BOO launch work begins."
---

## When this skill applies

- Preparing the ICP working session with Scott Kemme (week 1-2, BEFORE any contact is sourced)
- Designing or reviewing the Clay persona pull for back-office contacts
- Qualifying whether a sourced contact counts toward the 200
- Feeding the BOO launch kit its target universe

## The hard rule

**No contact gets sourced before the ICP conversation with Scott.** This skill's straw man exists to be corrected by him, not to bypass him. Bring it as "here's my hypothesis, tear it up," and record every correction; his edits ARE the ICP. Review the first fifty sourced contacts together before anything scales.

## The two universes (do not conflate)

1. **Inside existing customers (Mandate 3 proper):** contacts in the back offices of companies whose FRONT offices are already Intradiem customers. Front-office contacts cannot hand us these leads, so we source them ourselves via Clay, then run campaigns inside our own install base. This is the 200.
2. **Net-new back-office logos (BOO launch universe):** back-office-heavy companies with no Intradiem relationship. Same personas, different motion and different claims discipline (no customer-relationship warmth to lean on).

A contact counts toward the 200 ONLY if it belongs to universe 1, matches an ICP persona, and survives dedup.

## Straw-man ICP (v0, for Scott to correct)

**Firmographic hypothesis:** companies in the six verticals with 200+ back-office FTEs in transaction-processing functions; existing customers first, weighted by front-office deployment health (a struggling front-office account is a bad expansion target; check the signal engine's risk signals before including).

**Function hypothesis (where manual back-office work concentrates):**
- Claims processing and adjudication (insurance, healthcare)
- Payment operations, disputes, chargebacks (financial services)
- Order management, returns, fulfillment exceptions (retail)
- Service order and field dispatch processing (telecom, utilities)
- Document processing, underwriting support, onboarding/KYC (financial services, insurance)

**Persona hypothesis (titles to pull, Director and above):**
- VP/Director Back Office Operations, Operations Support
- VP/Director Shared Services
- VP/Director Claims Operations / Claims Transformation
- VP/Director Payment Operations
- Head of Operational Excellence / Process Improvement (secondary; often the internal champion, rarely the buyer)
- COO / SVP Operations (economic buyer tier; enters later in the sequence, never in the first pull)
- **Insurance economic-buyer tier (Naveen field intel, Aug 18 2026):** Chief Administrative Officer, SVP of Administration. Insurance-specific veto/economic titles; treat like the COO tier (later in sequence, never the first pull).
- **Insurance department reality (same source, from a CNI insider's org chart):** the insurance back office is organized as Actuarial (plus a feeder department) and Claims; Shared Services sits UNDER Claims, not beside it. So "Claims Shared Services" is the precise title string to pull, and Actuarial leadership (VP/Chief Actuary) is a valid secondary lane. Naveen has the department map written down; get the full version from him.

**Fit signal (field intel, Aug 18 2026):** Verint back-office tool in use = strong fit + displacement wedge; Nate reports users are widely unhappy with it. NICE is usually bundled free with front office and is harder to displace. Mirrored in the TAM engine as trigger `verint_backoffice`.

**Exclusions hypothesis:** pure front-office titles, IT/engineering titles (RPA owners are an objection source, not the buyer), contact-center titles already covered by the install-base relationship, functions under 50 FTEs.

## Pain map (for messaging downstream, per persona)

- **Claims / payment ops leaders:** backlog that regrows every Monday, aging queues, overtime spend, SLA penalties, quality-rework loops, seasonal surges staffed by guesswork.
- **Shared services leaders:** cost-per-transaction scrutiny, multi-function queues with no real-time visibility, utilization they cannot prove, hybrid-workforce oversight.
- **COO tier:** capacity without headcount, the invisible idle time already paid for, the fact that the back office has no equivalent of the contact center's real-time discipline. The core one-idea family: the back office runs on yesterday's report; the cost lives in what happens between reports.

All copy through the first-draft-engine and copy-sharpener gates; "workforce orchestration" and kin are product tells in this motion too.

## Dedup and hygiene rules

1. Dedup against the install-base contact set and any existing Clay tables BEFORE enrichment spend (clay-credit-steward pre-check applies; cheap columns before premium waterfalls).
2. One accountable owner per account motion: back-office campaigns inside a customer coordinate with that account's AE/CSM before any send. Their account, our machinery.
3. Every contact carries: universe tag (install-base vs net-new), persona_key, function, FTE-band estimate, source, sourced_date. The 200 is countable only because the tags exist from day one.
4. Suppression: accounts in active renewal escalation or open risk signals are excluded until the owner clears them.

## Workflow

1. **Prep the Scott session:** print the straw man above as a one-pager, framed as hypothesis. Capture his corrections live; version the ICP (v1 = post-Scott).
2. **Spec the Clay pull** from ICP v1: filters, title strings, caps per account, dedup keys. Credit pre-check before running.
3. **Sample fifty, review with Scott** (and the relevant CSM for install-base accounts). Tune. Then scale.
4. **Hand off:** qualified universe feeds Mandate 3 campaigns and the BOO launch kit's target list; pain map feeds the copy skills; counts feed the Friday readout.

## Output

- `BackOffice_ICP_v[N].md` (the living ICP, Scott's corrections logged with dates)
- `BackOffice_PersonaPull_Spec.md` (the Clay run spec)
- Counts and quality notes to the readout weekly
