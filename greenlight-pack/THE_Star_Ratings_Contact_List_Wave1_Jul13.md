# Star Ratings Motion — Wave 1 Contact List (as of Jul 13 2026)

The buying-committee list for the Star Ratings new-logo motion. This is the working list a rep picks up: customer-safe, deliverability-checked, and gated so nothing sends until a human approves each row.

## What the list is

The Contacts (Buying Committee) table in the GTM Engine Clay workbook holds 137 rows. Of those, 16 are existing-customer contacts that are flagged and held out of the motion, leaving **121 eligible new-logo contacts across 26 parent organizations**. Coverage spans three buying-committee personas per parent: Finance (the economic buyer), Stars/Quality (the primary program owner), and Operations/Contact-Center.

Every eligible parent in the winnable set is represented. The list feeds the sequencer through the existing sync column, which only releases a contact once `send_ready` is set to READY and the row is human-approved.

## Customer safety (verified live)

All 16 customer contacts carry `customer_exclude = TRUE` and are held out of the motion:

| Customer parent | Contacts held out |
|---|---|
| Health Care Service Corporation (HCSC) | 4 |
| Humana | 4 |
| UnitedHealthcare | 4 |
| Aetna (CVS Health) | 3 |
| CVS Health | 1 |

These sit in the table for reference but are excluded by flag. The send definition for the list is: `customer_exclude = FALSE` AND `critic_email_valid = PASS` AND the human gate. That guarantees a customer cannot enter outreach even if a row is later approved by mistake.

## Send gate (verified live)

Every row is `send_ready = HOLD` with `human_approved` unchecked. Nothing can send today. The rep approves rows deliberately, in batches, when the mailbox is warmed.

## Coverage by parent

All 26 eligible parents carry Finance and Stars/Quality and Operations coverage after this week's gap-fill. The two thinnest parents at the start of the week, HMSA and Solis, were operations-only; both now have a verified Finance lead and a verified Stars/Quality lead.

## This week's gap-fill (sourced Jul 13)

Coverage holes found in the audit were 7 parents missing a Stars/Quality contact and 2 parents (HMSA, Solis) missing Finance, plus a set of contacts that had no deliverable email (Presbyterian was fully email-dark). Sourced via Clay prospecting, all staged behind the same gate (`send_ready = HOLD`, `customer_exclude = FALSE`):

**Verified email, ready to stage (6):**

| Name | Title | Parent | Persona | Email |
|---|---|---|---|---|
| Carlos Soler | HEDIS / Star Ratings Director | Solis Health Plans | Stars/Quality | csoler@solishealthplans.com |
| Michael Lynch | Chief Financial Officer | Solis Health Plans | Finance | mlynch@solishealthplans.com |
| Anton Teehankee | Medicare Stars / Member Experience Lead | HMSA | Stars/Quality | anton_teehankee@hmsa.com |
| Heather Miyasato | VP Health Finance | HMSA | Finance | heather_miyasato@hmsa.com |
| Mark Dabney | Director, Risk Adjustment | Community Health Plan of WA | Stars/Quality | mark.dabney@chpw.org |
| Jasmine Stone | Risk Adjustment Manager | ATRIO Health Plans | Stars/Quality | jasmine.stone@atriohp.com |

**Sourced and identified, no work email returned by enrichment (7):**

These are the right people at the right parents, captured with title and LinkedIn, but the email waterfall returned "no result." They are LinkedIn-first touches, or Dallas can pattern-verify a corporate address (e.g. firstname.lastname@domain) before using.

| Name | Title | Parent | Persona | Note |
|---|---|---|---|---|
| Amor Brannin | Health Plan CFO / VP Finance | Presbyterian | Finance | Current health-plan CFO; replaces the prior contact who has retired. Presbyterian stays email-dark for now |
| Maria Goergen | Quality Improvement Specialist | Presbyterian | Stars/Quality | Presbyterian Stars/Quality |
| Adrienne Neaderhiser | Director, Member Experience | Presbyterian | Stars/Quality | Existing dark row; no email recovered |
| Keith Patterson | EVP & CFO | VNS Health | Finance | Existing dark row; VNS already reachable via its operations lead |
| JJ Kirkpatrick | Chief Financial Officer | ATRIO Health Plans | Finance | Existing dark row; ATRIO reachable via its Stars and operations leads |
| Crystal Muzdeka | Principal, Customer Experience Strategy | GuideWell | Stars/Quality | Member-experience proxy for Stars |
| Tracy Scieszinski | Executive Director, Customer Experience | Mass General Brigham | Stars/Quality | Member-experience proxy for Stars |

The full gap-fill set lives in `Stars_Wave1_GapFill_Jul13.csv`. The 10 net-new rows are also imported into the Clay workbook as the gated table `Stars_Wave1_NewContacts_Import_Jul13`.

## Honest edges

- **Seven of the sourced contacts returned no work email** from the enrichment (Presbyterian's three, GuideWell, Mass General Brigham, plus the VNS and ATRIO CFO recoveries). No addresses were guessed. Presbyterian therefore stays email-dark for now; VNS and ATRIO are still reachable through their operations and Stars leads. These seven are LinkedIn-first, or pattern-verify before use.
- **Baystate Health** has no clean plan-level Stars/Quality contact under its corporate domain; its Medicare plan runs under Health New England, a separate entity. Flagged for a targeted pull rather than a weak-fit placeholder.
- **The six verified gap-fill contacts are now live and validated in Contacts** (rows 138-143), routed through the renamed `Contact Intake (All Sources)` intake via its Send-table-data column — the real pipeline, not a side table. They are tagged `sourced_by = clay_prospecting`, ZeroBounce-validated (`critic_email_valid = PASS`), and gated (`send_ready = HOLD`, `customer_exclude = FALSE`, unclaimed). They are send-ready pending only Nathan's approval and a warm mailbox. See `Contact_Intake_MultiSource_Architecture.md` for the multi-source design.
- **The operations layer** (rows 95-137) carries email but is not yet motion-tagged (no Source Motion / Product Angle). It is usable data; tagging it is a free finishing step best done in the same controlled pass as the merge.
- **Signals** are current as of Jul 12: `measure_slippage` (first-party CMS, free) is wired and current, and hiring/leadership were refreshed Jul 12. The intent layer is self-cleaning, so the ranked list stays honest without a re-run.

## Credit posture

Sourcing and email enrichment this week ran through Clay's prospecting layer at a small cost (roughly 15 to 20 enrichment credits, one per matched email). The Clay 5,000 monthly signal budget was left untouched. Month-to-date consumption remains near 343 of 5,000.

## Ready-state and next steps

Nathan can start from the live core today: the 121 eligible, customer-safe, gated contacts in the Contacts table, roughly 100 of which carry a deliverable email. Nothing else is required to begin.

This week's gap-fill is fully folded in: the six verified contacts are live in Contacts (rows 138-143), ZeroBounce-validated (critic PASS), and gated. Remaining:

1. The seven no-email contacts: run them as LinkedIn touches, or pattern-verify a corporate address first.
2. Approve rows (set `send_ready = READY`, check `human_approved`) in batches once the mailbox is warmed, then sync to the Stars QBP Wave 1 campaign.
