# Back-Office Sample Pull — Receipt + Next Wiring (Jul 14 2026)

## What ran tonight (Dallas's go), meter-verified 86 credits total

Three Find People searches into the **Back Office Motion** workbook, all scoped to the 15 Tier-1 sample accounts by domain identifiers (the Sample_50_Accounts table couldn't drive the source directly: Clay's "table of companies" input needs URL/domain identifiers, and that table only carries names — add a `domain` column before the 200-scale run so the table drives the source):

| Search | Persona | Filters | Results |
|---|---|---|---|
| 1 | bo_claims | 7 title strings, Director+, US+UK, limit 2/company | 19 |
| 2 | bo_shared | 10 title strings, Director+, US+UK, limit 2/company | 24 |
| 3 | coo_finance | 5 title strings, VP+, US+UK, limit 1/company | 15 |

All 58 (+1 append artifact = 59 rows) landed in ONE person table, then: Work Email waterfall (11 providers, 100% run) and ZeroBounce validation (100% run). Majority = verified valid work emails; the No-Email-Found / invalid minority is itself sample data (email findability was one of the three questions the sample exists to answer).

**Measured economics: 86 credits / 59 contacts ≈ 1.46 per finished contact. Full 200-pull re-prices at ~300 credits (was estimated 600-900).**

## The room-ready line

"The back-office motion sourced its first 59 real buyers across 15 Tier-1 accounts last night for 86 credits, every email machine-verified, and nothing can send until an account owner clears it. The full 200-contact universe now costs about 300 credits, measured, not estimated."

## Hygiene queue (0 credits, next Clay session or VS Code-planned)

1. **Rename the table**: Clay auto-named it "Senior Claims Executives UK US"; it holds all 3 personas. Rename to `BO_Sample_People`. (Breadcrumb dropdown → Rename.)
2. **persona_key formula column**: tag each row bo_claims / bo_shared / coo_finance by title match (same strings as the searches).
3. **dup_vs_contacts flag**: Lookup vs Contacts (Buying Committee) on LinkedIn URL. Known suspect: Lisa Stephens (Humana SVP Ops) appears in both tables. ≤3 expected.
4. **Tag schema per spec**: parent_account, universe=install_base, sourced_date=2026-07-14, source=clay_find_people; fo_risk_flag + owner_cleared=FALSE (gates already live on the Target Universe table).
5. **Owner review sheet**: export the 59 (name, title, company, persona, email status, dup flag) for the AE/CSM + Scott 50-contact quality review. Review tunes title strings, then the scale-to-200 decision (~300 credits, one word).

## Quality notes for the review (observed during the pull)

Hit quality strong at payers (Directors of Claims, Claims Ops, UM, Appeals at Humana/Molina/Elevance/UHC/Aetna) and at coo_finance (President/COO Medicare at Aetna, COO UnitedHealthcare, CFO Capita). Known noise to prune in review: a few IT-flavored titles matched on "Shared Services"/"Payment" (e.g. Global IT VP at MetLife, HR Shared Services at Humana), and one clinical-ish title (Medical Director, Humana). That pruning IS the title-string tuning the sample was for.

## VS Code handoff briefs (repo work, parallel tabs, per Jason's pattern)

- **Reply Engine v1**: config/reply_categories.json mirroring intradiem-objection-handler's 7 categories + per-category response templates in Nathan's voice + SOP: classify → draft → send from Nathan → flip bdr_claimed on Contacts → log outcome on the closed-loop cols. Build before first sends flow.
- **Install-base expansion fork**: motion_overrides.install_base in intradiem-signal-engine/config/l2_intent_signals.json (warm-base like back_office, fo_risk suppresses, owner_cleared gates), fixtures + tests to green, keeping Stars parity guard.
- **October flywheel**: refresh_oct_release.py skeleton: ingest new CMS ZIP (cp1252!), rebuild movement joins, emit refreshed universe CSVs + drift report; October = re-import, re-grade, new fallers enter, graduates self-clean.
- **BOO launch kit v0**: compile from intradiem-launch-kit skill: positioning brief, enablement one-pager, sequence set skeleton, Tom-facing campaign brief; feeds September GA.

*Everything above is 0-credit until a pull or sweep is explicitly logged and fired. Ledger: Clay_Credit_Ledger.md (rows appended 2026-07-14).*
