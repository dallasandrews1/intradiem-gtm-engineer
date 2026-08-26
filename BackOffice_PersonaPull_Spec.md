# Back-Office Persona-Pull Spec (Jul 13 2026)

The Clay run that sources the ~200 Mandate 3 contacts against the ICP v1 target universe. Ready to execute; the one action that spends credits, so it runs on your explicit go. Built to the credit-steward discipline: sample 50, lock the actual per-contact rate, then scale.

## Input

- **Account universe:** `BackOffice_Target_Universe_v1.csv` (101 install-base accounts, tiered). Run **Tier 1 first** (56 accounts) — it alone fills the 200.
- **ICP:** `BackOffice_ICP_v1.md` (personas, exclusions, functions).

## Pull parameters per persona

Source Director+ / VP+ only. Dedup against the existing install-base contact set and the live Contacts (Buying Committee) table before any enrichment spend.

| persona_key | Title strings (OR) | Cap / account |
|---|---|---|
| `bo_claims` | "VP Claims", "Director Claims", "Claims Operations", "VP Appeals", "Director Grievances", "Utilization Management", "VP Claims Transformation" | 2 |
| `bo_shared` | "VP Payment Operations", "Director Payment Ops", "Disputes", "Collections", "Document Processing", "Shared Services", "Enrollment Operations", "Underwriting Support", "Revenue Cycle", "VP Back Office" | 2 |
| `coo_finance` | "Chief Operating Officer", "SVP Operations", "VP Operations", "CFO", "VP Finance" | 1 (never the first touch) |

Per-account total cap ≈ 4–5. Tier 1 (56 × ~4) ≈ 200+ addressable; the pull stops at ~200 by exhausting Tier 1, holding Tier 2 as the expansion bucket.

## Hard exclusions (drop at source)

IT/Security (CIO, CTO, VP IT — RPA owners); Clinical (CMO, nursing); Legal/Compliance; Sales/Marketing/HR; contact-center titles already covered by the front-office relationship; functions under ~50 FTEs.

## Enrichment tiering (credit-steward rule 3: cheap-and-broad before expensive-and-narrow)

1. **Free / cheap first:** contact identity, title, LinkedIn, company match, persona tag. Filter to fit BEFORE spending.
2. **Waterfall only on rows that cleared fit:** work-email waterfall, then ZeroBounce verification (email-first; skip mobile/phone this pass).
3. Never run the waterfall on an unscored or out-of-ICP row.

## Tag schema (every sourced contact carries these — the 200 is countable because of them)

`parent_account`, `universe` (=install_base), `persona_key`, `function`, `fte_band` (est), `source`, `sourced_date`, `fo_risk_flag` (from signal-engine risk read), `owner_cleared` (default FALSE).

## Credit pre-estimate (placeholder — provider-dependent, lock via sample)

Per-contact cost is provider-dependent, so this is an estimate to be replaced by measured actuals, not a committed number.

- **Assumption:** ~3–5 credits per enriched-and-verified contact (identity cheap + email waterfall + ZeroBounce), waterfall run only on fit-cleared rows.
- **Sample (run first):** 50 contacts → **~150–250 credits**. This locks the real per-contact rate.
- **Full 200 (projected):** **~600–900 credits**, inside the ~1,500/month back-office allocation (~4,657 remaining this month). ≈ 12–18% of the month's budget at the high end.
- **Drift rule:** if sample actuals differ from estimate by >25%, re-estimate the full pull before scaling and note the cause in the ledger.

## Run sequence (on explicit go)

1. Pre-check: confirm the estimate above against Clay's current per-provider pricing (rule 6 — verify live, don't instruct from memory), append the ledger row as an actual once the sample runs.
2. **Sample 50** (Tier 1, spread across `bo_claims` / `bo_shared` / a few `coo_finance`). Measure per-contact cost and match quality.
3. **Review the 50 with the account owners** (AE/CSM) — quality gate on fit and on which accounts are cleared to contact. Tune title strings / caps.
4. **Scale to ~200** across Tier 1, holding Tier 2 for expansion.
5. Append actuals to `Clay_Credit_Ledger.md`; counts feed the Friday readout.

## After contacts land (built and waiting)

Contacts flow into the engine's back-office table (base score + `owner_cleared` gate already live), then per-contact copy is generated at launch through first-draft-engine → copy-sharpener → verified-metrics, off the ICP v1 pain map. No prospect-facing back-office proof is used until it clears the verified-metrics gate (only Humana/contact-center is repository-verified today).
