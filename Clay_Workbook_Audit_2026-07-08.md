# GTM Engine Workbook Audit
**Date:** July 8, 2026, pre-9am review · **Workbook:** GTM Engine (wb_0thtlocqNeb46szQtAf), Intradiem workspace 1180800
**Method:** independent recompute from source CSVs, live inspection of all 6 tables and formulas in Clay, platform-level credit check. Nothing taken on faith from the build session.

## Verdict: GO for the 9am review

Every audit item passes. Two clarity fixes were made (column relabels, zero credits, reversible). One talking-point discipline applies: quote account-level dollars from the Accounts (Master) and CMS tables, not the contact-level QBP column, which carries prior-cycle figures and is now labeled as such.

---

## Pass/fail by audit item

### 1. Provenance: PASS (one flag, fixed)
- **CMS Star Ratings Import (L0):** 307/307 rows match StarRatings_Universe_2026_Canonical.csv exactly (spot-checked members, stars, gross and addressable QBP on rows 1-20; all values identical). primary_sources populated on all 307 rows ("CMS-2026-SR(Oct8-2025)+MeasureStars; CMS-Enr-Jun2026; KFF-QBP; MedPAC-2026").
- **Accounts (Master) (L1):** all 10 rows match GTM_Engine_Accounts_Seed_TierAB10.csv field-for-field, including the blank addr_2029plus on H4471. data_source stamp on every row.
- **Contacts (L3):** 22/22 rows match StarRatings_BuyingCommittee_Clay_Import.csv. Real people, real LinkedIn URLs, real enrichment statuses. Attribution tags intact (GTM Engine Sourced TRUE, star_ratings_cliff_edge, 2026-07-06) on all 22.
- **Reference tables (L4):** Product-Angle Map (8 rows) and ICP / Persona Rubric (10 rows) are targeting logic only. Every row stamped "config not data - not from Salesforce."
- **No Salesforce placeholders anywhere. No seeded engine numbers ($ surfaced, reply %, funnel counts) were imported into Clay.**
- **Flag (fixed):** the contact-level "Account Forgone QBP ($M)" and "Cliff-Edge Contracts" figures trace exactly to the Scored Targets (93) sheet of StarRatings_CliffEdge_Target_List.xlsx, the 2025-cycle cut built from Naveen's Apr 2026 workbook (Humana 8 contracts / $1,245.3M, UHC 12 / $466.0M, Centene 7 / $75.5M, CVS-Aetna 6 / $43.7M). The Accounts and CMS tables carry the rebuilt 2026-cycle universe (Humana gross $2,443.7M across 25 sub-4.0 contracts). Both are real and sourced, but they are different vintages of the same story sitting in one workbook. Fixed by renaming the two columns to "Account Forgone QBP ($M, 2025-cycle scored list)" and "Cliff-Edge Contracts (2025-cycle)" so the numbers are honest on their face.

### 2. Scoring: PASS, exact match on all 10 rows
Hand recompute from the seed CSV vs live formula output:

| Contract | addr_2028 | Recomputed fit | Live fit | Recomputed grade | Live grade |
|---|---|---|---|---|---|
| H5216 | 456.7 | 40 | 40 | C | C |
| H5619 | 277.0 | 40 | 40 | C | C |
| H0028 | 105.2 | 40 | 40 | C | C |
| H3312 | 64.7 | 40 | 40 | C | C |
| H1468 | 39.3 | 55 (faller +15) | 55 | B | B |
| H2775 | 33.7 | 40 | 40 | C | C |
| H0354 | 21.2 | 55 (faller +15) | 55 | B | B |
| H8889 | 22.2 | 40 | 40 | C | C |
| H4471 | 15.1 | 25 | 25 | C | C |
| H3038 | 12.2 | excluded | Excluded | Excluded | Excluded |

Formula text was also inspected directly, not just outputs, because the data never exercises the A (>=70), D (<20), or zero-2028 branches:
- fit_star: `(addr_2028>=20?40 : >=5?25 : >0?10:0) + (clin_star>=4?20:0) + (new_faller=="TRUE"?15:0) + (decision_maker_found=="TRUE"?25:0)` — matches spec.
- motion_exclude: `structural_exclude=="TRUE" || (addr_2028==0 && (addr_2029plus empty or 0))` — matches spec, untested branch included.
- grade: Excluded override, then A>=70 / B>=45 / C>=20 / else D — matches spec.
Molina (H3038) excludes on structural_exclude, and H4471 (addr_2028 = 15.1 with $0 current-year) correctly stays in-motion at grade C.

### 3. Guardrail: PASS
Verified Metrics / Claims, 6/6 rows, tiered exactly right:
1. Idle-time stat (12-18%): DO-NOT-SEND, sourced "proof.json (self-labeled placeholder)."
2. Peer/customer outcomes: DO-NOT-SEND until a verified reference exists.
3. Any Intradiem ROI/NRR not in the Value Repository: DO-NOT-SEND, "never cite from memory."
4. Engine seeded output ($ surfaced, reply %, funnel, grade distribution): DRY-RUN, amber-chip rule.
5. 15 meetings / 10x / 200+ contacts: TARGET, "provisional target to co-shape; never a commitment to defend."
6. 5,000 credits + 40+ data sources: VERIFIED, scoped as "internal process fact only; not a payer-facing outcome claim."
The stale 157/38 counts and the Intercom/Rippling proof points are gone from the live table, consistent with the integrity review. Nothing false is presented as fact.

### 4. Send gate: PASS
- critic_email_valid: `Email Status == "verified" ? PASS : FAIL`. Live result: 17 PASS, 5 FAIL, exactly matching the source Email Status distribution (17 verified; 3 enriching, 1 not found, 1 verify domain).
- human_approved: checkbox, all 22 unchecked.
- send_ready: `critic PASS && human_approved ? READY : HOLD`. All 22 rows read HOLD. The gate cannot flip without both conditions.

### 5. Safety: PASS, confirmed at platform level
- Clay Usage page (Settings > Usage > Workbooks): **GTM Engine = 0 credits used, 0 actions used.** Not just the ledger's claim; Clay's own accounting.
- Auto-run counter reads 0 on every table. No enrichment, waterfall, AI, or Message columns exist anywhere in the workbook; every column is a CSV import field, a native formula, or a checkbox.
- The "enriching" values in Email Status are static text imported from the Jul 6 pre-import run, not live jobs. Nothing is running.
- Nothing has been sent; there is no send integration in the workbook at all.
- Ledger updated with the audit line and the two renames; running total stays 0 of 5,000.

### 6. Fool-proofing: issues found, with status
1. **Two Stars vintages in one workbook** (Contacts 2025-cycle vs Accounts/CMS 2026-cycle). FIXED via column relabels. Demo discipline: quote dollars from Accounts (Master) or CMS import only.
2. **"Why Now" text still embeds the 2025-cycle numbers** ("Humana holds ~$1245M across 8 contracts"). Not fixed: restating 22 imported cells is a data edit I deliberately left alone before the review. Do not read Why Now aloud as current; it refreshes with the next buying-committee rebuild off the 2026 canonical.
3. **5 of 22 contacts lack a usable email** (critic correctly FAILs them). If asked "how many are sequence-ready," the honest number is 17 of 22, pending one gated enrichment pass.
4. **UnitedHealthcare (4 contacts) and Clover-type parents are in Contacts but not in the 10-row Accounts seed.** Correct answer if poked: the seed is the top slice of the 98-contract Tier A+B universe; the full set loads next, and the Accounts-to-Contacts wiring is deliberately gated.
5. **"5,000 Clay credits" vs the workspace Usage page showing a 72,000/yr plan (72,556.9 available).** The 5,000 is Dallas's motion-level allocation, not the workspace plan. The live guardrail already says "allocated" (not "purchased"), which is defensible, but align the number with Naveen before it appears in anything exec-facing.
6. **Medica: contacts CSV says 37.1, source sheet says 37.0.** Trivial rounding in the CSV build; live table faithfully matches its import file. No action needed beyond the vintage relabel already applied.
7. **claude-design-handoff/03_VERIFIED_METRICS file is now stale** (still lists Intercom/Rippling and 157/38 as VERIFIED). The live Clay guardrail is the corrected source of truth; update the handoff doc so no future build regresses.
8. **Deck cross-figures reconcile:** 98 Tier A+B contracts across 32 parents, $2,511.2M addr_2028 (the deck's "$2.5B," footnoted as Dallas's own analysis), 307-row universe. Humana in the golden-list site reads $1.08B vs $1,101.5M all-Humana addr_2028 in the tiered file, about 2% apart; check the site's rounding before showing site and workbook side by side.

---

## Fixes made during this audit (all zero-credit, reversible, no sends)
1. Renamed Contacts column "Account Forgone QBP ($M)" to "Account Forgone QBP ($M, 2025-cycle scored list)".
2. Renamed Contacts column "Cliff-Edge Contracts" to "Cliff-Edge Contracts (2025-cycle)".
3. Appended AUDIT and column_rename lines to clay_credit_ledger.csv.

## Still to address, in priority order
1. Align the "5,000 credits allocated" figure with Naveen (workspace plan is 72K/yr; his read on the motion budget governs).
2. Rebuild the buying-committee QBP context (and Why Now text) off the 2026 canonical universe at the next contact refresh; zero credits, but it edits imported data so it deserves its own pass.
3. Update claude-design-handoff/03_VERIFIED_METRICS_and_integrity_rules.md to match the live guardrail table.
4. Decide on the 5 unverified-email contacts. An email waterfall on 5 rows is a credit spend; estimate before running (roughly 2-10 credits depending on providers). Gated on your go.

## Gated next steps: confirmed still correctly deferred
- **Message Gen AI column: NOT BUILT.** No AI or prompt columns exist in any of the 6 tables. Stays gated until the Value Repository is connected.
- **Accounts-to-Contacts "Send Table Data" wiring: NOT BUILT.** The workbook canvas shows only CSV-import sources feeding each table; no write actions exist. Stays gated.

## Safe talking points for 9am
- 6 tables live in the Intradiem workspace, built for zero credits; Clay's own Usage page shows 0 credits and 0 actions against this workbook.
- 307-contract public CMS 2026 universe, provenance stamped per row; 10-account Tier A+B seed scoring live on native formulas; recomputed independently this morning and exact on all 10 rows.
- 22 real buying-committee contacts with attribution tags, feeding a working send gate: machine critic plus human checkbox, every row HOLD until a person approves. Human-before-send is demonstrable on real data, live.
- The guardrail table tiers every claim; placeholder stats are marked DO-NOT-SEND in the workbook itself, so the integrity rule is visible in the instrument, not just in a doc.
- Framing: a head start on the engine, standing up in our workspace, with the credit-spending layers deliberately gated behind alignment. Not a finished product; the ongoing build is the job.
- Dollars: quote $2.5B addressable-2028 across 98 Tier A+B contracts (32 parents), Humana as the largest concentration. Do not quote the contact-table QBP column; it is labeled 2025-cycle for a reason.
