# Clay Day-1 build order (reconciled with the refreshed motion)

This sequences the July-6 Clay build and supersedes the stale assumptions in `gtm-cohesion-layer/Clay_Build_Pack.md`. Use the Build Pack for the column-level UI mechanics; use this doc for what data feeds what and what changed since it was written. Build order and gates are unchanged: measurement before volume, prove on a slice, human before send.

UI caveat: the Build Pack's column configs were written before access. Confirm current Clay feature names in Clay's own docs as you go (for example, moving rows table-to-table is "Send Table Data" under Actions, not a "Write to Table" column). Do not build from the Build Pack's exact click labels without checking.

## Inputs (which canonical file seeds which table)
| Clay table | Seed file | Note |
|---|---|---|
| CMS Star Ratings Import | `StarRatings_Universe_2026_TimePhased.csv` | Canonical universe. Supersedes `StarRatings_Universe_2026_Canonical.csv` (that file is locked and lacks the 5 time-phased columns; use the TimePhased file). Already filtered to sub-4.0. Carries cs_star, clin_star, gross, addressable, pct, overall_star_2026 PLUS addr_2028_musd, addr_2029plus_musd, pct_2028, pct_2029plus, wavg_2026. In-window filter already applied; keep the formula only for future raw-CMS re-imports. |
| Accounts (priority + exclusions) | `StarRatings_Targets_2026_Tiered.csv` | Supplies `tier` (A/B/C/Unscored) and `new_faller`. Start the build on Tier A+B only. |
| Contacts | `StarRatings_PersonaPull_Runbook.md` + `..._RunConfig_TierAB.csv` | Day-1 persona pull; dedup against the 157 first. |
| Message Gen (AI column) | `Clay_MessageGen_SystemPrompt_v2.md` | Paste the prompt; apply the column map in that file. |
| Signals | `tam-outbound-engine/config/triggers.json` + `StarRatings_Earnings_Signals_2026.csv` | Three scored plays now, see step 5. |
| Exclusions | `StarRatings_Targeting_Flags_2026.md` | Horizon, BCBS Alabama, Molina-MAPD. |

## Deltas that override the Build Pack
1. Universe: do not load "38 + 157." Load the 307-row canonical universe (Tier A+B first) and the real 157 export for dedup.
2. Accounts data model: add `cs_star`, `clin_star`, `gross_forgone_qbp_musd`, `addressable_forgone_qbp_musd`, `addressable_pct`, `overall_star_2026`, `tier`, `new_faller`, plus the time-phased columns `addr_2028_musd`, `addr_2029plus_musd`, `pct_2028`, `pct_2029plus`, `wavg_2026`. These did not exist when the Build Pack's `fit_star` was written. Rank the live motion on `addr_2028_musd` (the influenceable window, scored through Dec 2026), not the PY2027 `addressable_forgone_qbp_musd`. DONE: `StarRatings_Targets_2026_Tiered.csv` and the persona-pull run config are now re-tiered on addr_2028 (Tier A+B = 98 contracts, 32 parents, $2,511M). fit_star bands (delta 3) run on addr_2028 to match.
3. Star Ratings fit score: replace the old `qbp_avg_stars`-band formula. Rank on the live-window dollar (`addr_2028_musd`, the figure Persona 2 copy now leads with) and fit signals. Bands hold; 2028-window totals run ~18% above current-model, not enough to re-band:
   ```
   fit_star =
     ( addr_2028_musd >= 20 ? 40 : addr_2028_musd >= 5 ? 25 : addr_2028_musd > 0 ? 10 : 0 )
     + ( clin_star >= 4.0 ? 20 : 0 )        // clinical-clean = whole gap is ours
     + ( new_faller ? 15 : 0 )              // fresh pain, uncontested
     + ( director_plus_stars_or_finance_found ? 25 : 0 )
   ```
4. Motion exclusions (new formula column `motion_exclude`, true = never source):
   - `pct_2028 == 0 AND pct_2029plus == 0` (gap is clinical across every window we can influence). NOT `addressable_pct == 0`: that older rule wrongly drops 20 contracts, incl. H4471 Anthem ($15.1M) and H5322 UHC ($10.2M), that are zero on current ratings but become addressable once the measures shift. BCBS Alabama H0104/H1347 stay excluded (all three windows are 0).
   - Parent is Horizon (already absent from the universe; belt and suspenders).
   - Molina straight-MAPD contracts (per targeting flags); keep Molina D-SNP/MMP.
5. Signals: the Build Pack's Tier-1 "Stars in filings / earnings mention" is now the wired `qbp_earnings_pressure` signal (routes finance/cc_ops), and there is a second scored play, `quality_identity_gap` (routes cx/cc_ops), for accounts whose public quality brand contradicts a sub-4.0 CS score. Feed the `angle_line` text from `StarRatings_Earnings_Signals_2026.csv` (lookup by parent) into the account's `why_now`. Earnings sweep is done through batch 2: Medica and HMSA fire `qbp_earnings_pressure`; VNS, Imperial, Devoted route to `quality_identity_gap`; Cambia and PacificSource hold at zero pending summer rate filings; Zing came up empty (QBP math only). Only Horizon (exited) and BCBS Alabama (excluded) are legitimately unswept, and neither is in the motion.
6. New table, Message Gen (L4), sits between Contacts and Send Queue. It did not exist in the Build Pack. One AI column runs the v2 system prompt; inputs are the mapped tokens from `Clay_MessageGen_SystemPrompt_v2.md`. Persona routing is off `job_title`; the persona key goes in its own `persona_key` column, never in `product_angle`.

## Ordered build (Day 1)
1. Confirm Salesforce attribution fields exist: `gtm_engine_sourced`, `source_motion`, `sourced_date`. If missing, flag to Naveen as a build. (Build Pack §9.1)
2. Export the 157 existing contacts (dedup baseline) and the CMS-derived universe. Build `CMS Star Ratings Import` and load the 307; load the 157 into the dedup/Install-Base path.
2b. Non-customer filter (do not skip). Naveen's motion is non-customer plans only; the 307 universe includes current Intradiem customers. Intersect the universe against the install-base list and route any customer sub-4.0 contracts to the back-office/install-base path, not this new-logo motion. This is the Build Pack's `is_current_customer == false` gate, which the time-phased file does NOT pre-apply.
3. Build `Accounts` identity and base, then add the refreshed columns from delta 2. (Build Pack §3a, extended)
4. Build the enrichment waterfall exactly as the Build Pack §3b/3c specifies ("only run if empty," conditional runs), so credits are protected.
5. Add `fit_star` (delta 3), `motion_exclude` (delta 4), then `intent_score`, `top_signal`, `grade`. Run on a 10-row Tier A+B slice first (start with Humana H5216, H5619, H0028). Verify grade computes and excluded rows drop.
6. Build `Contacts` per Build Pack §4, but run the persona pull from the runbook: filters, dedup against the 157, caps, and the `persona_key` column. Verify the three attribution tags lock and never overwrite. (Build Pack §4c)
7. Build the `Message Gen` table (delta 6): paste the v2.1 prompt (window beat, payment-year clause, time-stamped UHC line, addr_2028 lead for Persona 2), wire the column map, generate two rows (one Persona 1, one Persona 2) and eyeball against the v2.1 worked examples before going wider. The examples in the prompt file are now v2.1.
8. Build `Send Queue` and the three webhooks. Point webhook #1 at the approval queue. Leave webhook #3 (sender) OFF until deliverability is green. (Build Pack §7)
9. Ratify with Naveen and Scott before lifting the test-slice cap: scoring weights, the addressability cut as the ranking basis, attribution definition, the back-office ICP, and the call-center rule-text check (C33/D01 already out for 2028 ratings; raise as a joint check on his onboarding page's attribution-window framing, since the copy would otherwise inherit that claim). (Build Pack §9.7)
10. Turn on Tier-1 signals (scheduled: the October CMS re-import, the earnings/filings sweep). Hold Tier 2/3. (Build Pack §9.8)
11. First real run: 3 variants on a Tier A+B segment, small, human-approved, deliverability watched. (Build Pack §9.9)

## Gates (unchanged, fail-closed)
Preflight must be green before any volume: attribution ratified, baseline set, deliverability green. The conductor already refuses to run live until these pass. Do not lift the test-slice cap until step 9 is done.

## First-week target order
Humana ($1,083M Tier A+B in the 2028 window) → UnitedHealth → CVS/Aetna → Centene → Elevance → HCSC. New-faller contracts inside those parents first, since the pain is fresh and Nate's old-list outreach does not cover them.
