# Back-Office Sample-50 Run Sheet (staged Jul 13 2026)

The one-word-go spec for the first back-office contact pull. Everything is decided; nothing here spends credits until the run is explicitly triggered. This is the sample that turns the full-pull estimate from a guess into a measured rate and produces the 50 real names to review with account owners before scaling to 200.

## The cohort (15 Tier-1 accounts, deduped to parents)

Chosen for vertical + company-type spread so the sample tests whether the title strings generalize, not just whether they work at one payer.

| Vertical | Accounts | Primary persona |
|---|---|---|
| Healthcare Payer (6) | Aetna, Humana, Elevance Health, Cigna, UnitedHealthcare, Molina Healthcare | `bo_claims` |
| Financial Services (5) | JPMorgan Chase, Wells Fargo, Goldman Sachs, Synchrony Financial, US Bancorp | `bo_shared` |
| Insurance (2) | MetLife, Prudential Financial | `bo_claims` / `bo_shared` |
| BPO / Outsourcer (2) | Capita, Foundever (Sitel) | `bo_shared` |

Full per-account caps and title strings live in `BackOffice_Sample50_Accounts.csv` (imported to Clay as the **Sample_50_Accounts** table). Target: **~49 contacts at caps** (2 primary-persona + 1 COO per account, 3 on the two BPOs and the two biggest anchors).

## Title queries (per persona, Director+ / COO tier VP+)

- **`bo_claims`:** "VP Claims" OR "Director Claims" OR "Claims Operations" OR "VP Appeals" OR "Director Grievances" OR "Utilization Management"
- **`bo_shared`:** "VP Payment Operations" OR "Director Payment Ops" OR "Disputes" OR "Collections" OR "Document Processing" OR "Shared Services" OR "Enrollment Operations" OR "Revenue Cycle" OR "VP Back Office"
- **`coo_finance`:** "Chief Operating Officer" OR "SVP Operations" OR "VP Operations" (1 per account, never the first touch)

## Enrichment order (credit-steward rule: cheap-and-broad before expensive-and-narrow)

1. **Find people** (source) into a new people table off Sample_50_Accounts, filtered by the title queries, capped per account. Identity/title/LinkedIn only.
2. **Dedup** against Contacts (Buying Committee) on account + LinkedIn URL. Drop anyone already in the install-base contact set.
3. **Work-email waterfall** only on the fit-cleared, deduped rows.
4. **ZeroBounce** verify the emails.
5. Tag every contact: `parent_account`, `universe=install_base`, `persona_key`, `function`, `fte_band` (est), `source`, `sourced_date`.

Skip mobile/phone this pass — email-first.

## Credit pre-estimate (held; the one paid action)

- ~3–5 credits per enriched-and-verified contact → **~150–250 credits** for the 50.
- Inside the ~1,500/mo back-office allocation (~4,657 remaining). Ledger row already logged as HELD, 0 consumed.
- **Drift rule:** if the measured per-contact cost differs from estimate by >25%, re-estimate the full 200 before scaling and note the cause in the ledger.

## What the sample measures (the reason it goes first)

1. **Real per-contact credit cost** → replaces the 600–900 full-pull guess with a fact.
2. **ICP hit quality** → do the title strings return actual back-office buyers (VP Claims Ops) or noise (junior processors, wrong function)? Per vertical.
3. **Email findability** → what % of back-office directors at big payers/banks resolve a verified work email.

## Go-time checklist (one word = go)

1. Confirm credit go (this is the spend decision).
2. Run Find people on Sample_50_Accounts with the title queries + caps.
3. Dedup → waterfall → ZeroBounce on cleared rows.
4. Append actuals to `Clay_Credit_Ledger.md` (cost, hit rate, email %).

## After the 50 land (the review, not a build gate)

Review the 50 with the account owners (AE/CSM) and — per your call — Scott: are these the right people, right seniority, right function, per account? Tune title strings / caps. Clear the accounts (`owner_cleared`). **Then** scale to ~200 across Tier 1, and only then build per-contact copy through first-draft-engine → copy-sharpener → verified-metrics.

## Not doing yet (deliberately)

No campaign, no copy, no full 200. Copy is built from the real contacts once we see who they are; a template before the names is the thing that makes back-office outreach generic.
