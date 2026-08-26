# Contacts (Buying Committee) coverage, Star Ratings new-logo motion

Status as of Jul 9 2026. Table `Contacts (Buying Committee)` in the GTM Engine workbook, 94 rows. Nothing sends, sequencer untouched, Wave 1 approvals still HOLD.

## What is true right now

The table is a complete, validated buying-committee list for the new-logo Star Ratings motion across every eligible Tier A and Tier B parent, with two named parent gaps and one persona gap that are yours to decide on before we call it fully exhaustive.

- 94 contacts: 72 from the Jul 8 SalesNav persona pull (Stars/Quality and Finance/Actuary), 22 from the original Jul 6 cliff-edge committee (contact-center and back-office operations leaders).
- 27 new-logo-eligible Tier A+B parents. 25 of them carry contacts. 2 carry none yet (below).
- The 5 install-base parents (Humana, UnitedHealth, CVS/Aetna, Elevance, Molina) are excluded from this motion on purpose. They are not gaps. Their existing-customer contacts already in the table move to the expansion lane, not new-logo outreach.

## Coverage by eligible parent

Valid email = ZeroBounce returned a deliverable mailbox. Personas present are the ones actually sourced at that parent.

| Parent | Tier | Contacts | Valid email | Personas present | Persona not yet sourced |
|---|---|---|---|---|---|
| Cambia Health Solutions | A | 3 | 2 | coo_finance, stars_quality | cc_ops |
| Centene | A | 8 | 5 | coo_finance, stars_quality, cc_ops | none |
| Clever Care Health Plan | A | 5 | 5 | coo_finance, stars_quality | cc_ops |
| Clover Health | A | 3 | 3 | coo_finance, stars_quality | cc_ops |
| Health Care Service Corp | A | 4 | 1 | coo_finance, stars_quality, cc_ops | none |
| Imperial Health Plan | A | 3 | 3 | coo_finance, stars_quality | cc_ops |
| Medica | A | 8 | 7 | coo_finance, stars_quality, cc_ops | none |
| Presbyterian Healthcare Services | A | 3 | 0 | coo_finance, stars_quality | cc_ops |
| Visiting Nurse Service of NY (VNS) | A | 3 | 0 | coo_finance, stars_quality | cc_ops |
| Zing Health | A | 2 | 2 | coo_finance, stars_quality | cc_ops |
| ATRIO Health Plans | B | 1 | 0 | coo_finance | stars_quality, cc_ops |
| **Athena Healthcare Holdings (Solis Health Plans)** | B | 0 | 0 | none | all three |
| Baystate Health | B | 1 | 1 | coo_finance | stars_quality, cc_ops |
| Blue Shield of California | B | 3 | 3 | coo_finance, stars_quality | cc_ops |
| CareFirst | B | 3 | 3 | coo_finance, stars_quality | cc_ops |
| Community Health Plan of WA | B | 2 | 2 | coo_finance | stars_quality, cc_ops |
| Devoted Health | B | 5 | 5 | coo_finance, stars_quality | cc_ops |
| GuideWell (Florida Blue) | B | 2 | 2 | coo_finance | stars_quality, cc_ops |
| **Hawaii Medical Service Assn (HMSA)** | B | 0 | 0 | none | all three |
| IEHP | B | 2 | 2 | coo_finance, stars_quality | cc_ops |
| Lifetime Healthcare (Excellus) | B | 3 | 0 | coo_finance, stars_quality | cc_ops |
| L.A. Care | B | 4 | 2 | coo_finance, stars_quality | cc_ops |
| Lumeris (Essence) | B | 3 | 2 | coo_finance, stars_quality | cc_ops |
| Mass General Brigham | B | 2 | 1 | coo_finance | stars_quality, cc_ops |
| NYC Health + Hospitals | B | 3 | 2 | coo_finance, stars_quality | cc_ops |
| CalOptima (Orange County HA) | B | 3 | 3 | coo_finance, stars_quality | cc_ops |
| Point32Health | B | 3 | 3 | coo_finance, stars_quality | cc_ops |

## The gaps, and why

1. Two eligible parents have zero contacts: **Athena Healthcare Holdings (Solis Health Plans)** and **Hawaii Medical Service Association (HMSA)**. Both are single-contract Tier B parents that the persona pull skipped on domain resolution. They need a manual pull.

2. **cc_ops (contact-center and back-office operations) is thin.** It only appears at Centene, HCSC, and Medica, because those are the parents where the original committee already sat. The Jul 8 persona pull deliberately ran only Stars/Quality and Finance/Actuary. Every other eligible parent has no operations leader yet. Since Queue Optimizer is the operations angle, this is the persona to decide on: do we source a cc_ops leader at each eligible parent, or lead with Stars and Finance and let them route us in.

3. **Four parents have contacts but no reachable email yet:** Presbyterian, VNS, Lifetime/Excellus, and ATRIO. Their sourced contacts all came back "not found" on the email waterfall, so validation had nothing to check. They need an email re-source, not new names.

## Exclusions, stated plainly

- **Install-base parents** (Humana, UnitedHealth, CVS/Aetna, Elevance, Molina): out of the new-logo motion per the Jul 8 call. Not gaps.
- **Gated at the staging layer**: 13 SalesNav rows never promoted (OUTSIDE_ICP or DUPLICATE against the install base).
- **No email**: 16 of 94 rows carry no email (12 new persona-pull contacts plus 4 originals still enriching or not found).
- **Invalid email**: 8 rows validated as bad mailboxes (see below). They stay in the table but will not pass the send gate.

## Email validation (authorized spend, done)

ZeroBounce ran on the 78 rows that carried an email, at 0.1 credits per row via the Clay-managed account.

- 67 valid and deliverable (3 of those sit on catch-all domains, lower confidence: Gandhi, Maroney, Hermosillo).
- 8 invalid, mailbox not found: Xiaoping Ding, Lisa Pattison, Thomas M. (the address was a truncated `m@lacare.org`), Angela Martinez, Robert Friedrichs, Dominic Turpin, Afzal S., Rolande Odeniyi.
- 3 unknown, greylisted (temporary defer, not a confirmed fail): Armen Akopyan, Max Barry, Mary Cooper.
- 16 skipped with no email, not billed.

`critic_email_valid` now reads off the validation result, so it shows PASS for the 67 deliverable rows and FAIL for the rest. This does not move anything toward sending. `send_ready` stays HOLD on all 94 because `human_approved` is unchecked.

Credits: 7.8 spent. Running total 150.1 of the 5,000 allocation. Ledger updated with the pre-estimate and actual.

## QBP columns (Dallas public-data analysis, now populated for every parent)

The three account-context columns (Cliff-Edge Contracts, Account Forgone QBP, Why Now) were hardcoded to the original five parents and rendered blank for the 72 new rows. They now compute for every parent off `parent_key`, using the same 2026-cycle cut that produced the original five constants: contracts at exactly 3.5 stars, one half-star under the 4.0 bonus line, summing gross forgone QBP and the customer-service-addressable slice from the public CMS 2026 Star Ratings release. The Humana reproduction matches to the cent (14 contracts, 1,776.3M forgone, 568.9M addressable), so the method is confirmed, not guessed.

Nine eligible parents sit at 3.0 stars with no 3.5-star cliff contract this cycle (CalOptima, L.A. Care, Lumeris, IEHP, Presbyterian, Zing, Community Health Plan of WA, ATRIO, Baystate). For those the Why Now says so honestly and frames them as a longer-horizon Stars play rather than inventing a same-cycle cliff number. Every figure in these columns is public-data analysis, labeled as such in the cell text, never presented as an Intradiem-verified number.

---

# Gap-fill pull spec (manual export, for Dallas)

Everything below is what the table is missing. The pull itself is your manual SalesNav export.

## A. Two parents, all personas

| Parent | Domain | Personas to pull | Notes |
|---|---|---|---|
| Athena Healthcare Holdings (Solis Health Plans) | solishealthplans.com | coo_finance, stars_quality, cc_ops | Tier B, 1 contract H0982, 3.5-star cliff, ~6.4M addressable. Parent org name is Athena Healthcare Holdings; the plan brand is Solis. |
| Hawaii Medical Service Association (HMSA) | hmsa.com | coo_finance, stars_quality, cc_ops | Tier B, 1 contract H3832, 3.5-star cliff, ~5.5M addressable. |

## B. cc_ops (operations) leader at each eligible parent that lacks one

Only if we decide to lead with operations. Titles: VP/SVP/Director of Contact Center Operations, Customer Service, Member Services Operations, Claims Operations, or COO of the health plan. Parents needing a cc_ops contact: Cambia, Clever Care, Clover, Imperial, Presbyterian, VNS, Zing, ATRIO, Baystate, Blue Shield of California, CareFirst, Community Health Plan of WA, Devoted, GuideWell, IEHP, Lifetime/Excellus, L.A. Care, Lumeris, Mass General Brigham, NYC Health + Hospitals, CalOptima, Point32Health.

## C. Email re-source for contacts already in the table

These have names but no reachable email. Re-run the email step, do not re-pull names.

- No email at all (12 new): Erin Conway-Habes, Keith Patterson, Brian Dellinger, Ryan Barrett, Adrienne Neaderhiser, JJ Kirkpatrick, Tricia L. Roberts, Dale Maxwell, Ann Pentkowski, Christina B. Lomax, Kyle Nyskohus, Vincent McDermott.
- Invalid email, need a fresh find (8): Xiaoping Ding, Lisa Pattison, Thomas M., Angela Martinez, Robert Friedrichs, Dominic Turpin, Afzal S., Rolande Odeniyi.
- Greylisted, likely retryable (3): Armen Akopyan, Max Barry, Mary Cooper.
- Originals still enriching or not found (4): Mark Riddlesworth, Corey Taliaferro, Anthony Portela, Bob Wadsworth.

Whole parents that are name-covered but email-dark: Presbyterian, VNS, Lifetime/Excellus, ATRIO.

---

## Open items I did not touch (yours to sequence)

- **Sync leads to campaign** enrichment still maps off an aux column (`New Column (2)`). It is a HOLD draft at 0 percent run and I did not run it, but the field mapping should be repointed to the real display columns before any launch so merge fields resolve correctly.
- Aux ground-truth columns (`bk First Name`, `New Column (2..11)`, the lowercase auto-extract set) are left visible. They are the pasted-ground-truth store; hiding them is cosmetic and can wait.
- The three QBP column description boxes still describe the old Company-keyed logic. The live formula is the source of truth and is correct, but do not click Regenerate on those columns or it will rebuild the old five-parent logic. Worth updating the descriptions when convenient.
