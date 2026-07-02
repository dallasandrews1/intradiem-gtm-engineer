# Persona pull runbook (Day-1 execution)

Why this is a Day-1 task, not pre-start: Apollo is free-tier blocked on the connector here, and the 157 existing contacts (the dedup baseline) live in Intradiem's Clay, which you get July 6. Running before then would be blind sourcing with no dedup. This runbook makes Day 1 pure execution. Target set and priority are in `StarRatings_PersonaPull_RunConfig_TierAB.csv` (32 parents, $2,511M addressable in the 2028 window; tiered on addr_2028).

## Step 0: before pulling
1. Export the 157 existing contacts from company Clay/Salesforce. This is the dedup baseline.
2. Confirm the 13 `VERIFY` domains in the run config (long-tail parents) resolve to the right org in Apollo/Clay before searching by domain; org-name search is the fallback.
3. Apply exclusions already decided: skip Horizon (no live sub-4.0 contracts) and BCBS Alabama (0% addressable). For Molina, pull only D-SNP/MMP contracts, not straight-MAPD (see targeting flags).

## Step 1: persona filters (run per parent)

Persona 1 (VP Stars/Quality):
- Include titles: Stars, Star Ratings, Stars Improvement, Medicare Stars, Quality Improvement, Quality Performance, CAHPS, Member Experience (with Quality/Medicare), HEDIS, Quality & Risk Adjustment, Medicare Quality, Health Plan Quality.
- Exclude: Provider Quality, Hospital Quality, Clinical Quality (unless with Stars/Medicare/plan), Quality Assurance (IT/QA), Quality Engineer, standalone Pharmacy Quality, standalone Accreditation.
- Seniority: Director+, bias VP+. Accept Senior Director at parents under 100k sub-4.0 members.
- Provider-owned parents (Presbyterian, Intermountain, Lumeris, IEHP, L.A. Care, CalOptima): filter to the health-plan entity, not the delivery system.

Persona 2 (Finance/Actuary):
- Include: CFO, Chief Actuary, VP Actuarial, VP Finance, SVP Finance, Head of Medicare Finance, Medicare Segment CFO, VP Financial Planning (plan entity), Treasurer only at parents under 50k members.
- Exclude: Controller, Accounting, Audit, Tax, Investor Relations, Procurement, Revenue Cycle, analyst/manager below Director.
- Seniority: VP+ default; Director+ only for Director-Medicare-Finance / Director-Actuarial at parents under 100k members.
- Large-parent segment rule (the `persona2_segment_rule` column): target the Medicare-segment finance lead or Chief Actuary, never the corporate CFO. Explicit for Humana, UnitedHealth, Centene, CVS/Aetna, Elevance, HCSC.

## Step 2: dedup and gap logic
1. Map each of the 157 to a parent via domain (primary) or fuzzy name (fallback); flag unmatched for review, don't drop.
2. Classify each existing contact against the Persona 1/2 include-exclude specs. A contact matching neither = zero coverage even though it inflates the raw 157.
3. A parent-persona cell is covered only if the parent has >= 1 classified contact at/above the seniority floor. For the six large parents, Persona 2 needs the segment-level match; a corporate CFO does not cover the cell.
4. Fill order = uncovered cells sorted by the parent's Tier A+B addressable (already the sort order of the run config).

## Step 3: pull caps
Per the run config `contact_cap_rule`: 3 contacts per uncovered persona cell for parents >= $20M addressable, 2 below. Re-run the matrix after import; this audit is repeatable.

## Step 4: output schema (with the collision fix)
```
First Name,Last Name,Full Name,Job Title,Company,Company Domain,LinkedIn URL,Email,Email Status,Seniority Tier,Account Forgone QBP ($M),Cliff-Edge Contracts,Persona Key,Why Now,Source Motion,Sourced Date,GTM Engine Sourced
```
- `Company` = parent org exactly as in the universe file (join key).
- `Account Forgone QBP ($M)` = parent-level ADDRESSABLE sum, one decimal (the number copy uses).
- `Persona Key` = `stars_quality` or `medicare_finance`. NOTE: this replaces Fable's "Product Angle" suggestion. Do NOT write the persona key into Product Angle; that token is approved-Intradiem-claims-only in the message prompt. Leave Product Angle out of this pull entirely.
- `Why Now` = earnings_angle_line or quality-pride wedge from `StarRatings_Earnings_Signals_2026.csv`, blank if neither.
- `Email Status` = Apollo's raw value (verified / likely / unavailable), untouched. The deliverability monitor keys off it; don't let Clay overwrite it during enrichment.
- `Source Motion` = `star_ratings`; `GTM Engine Sourced` = `TRUE` (attribution).

## Note
This is the dry-run of the enrichment waterfall Naveen wants proven before wider Clay spend. Run it on Tier A+B first (32 parents), measure hit rate and email-verification rate, then decide on volume.
