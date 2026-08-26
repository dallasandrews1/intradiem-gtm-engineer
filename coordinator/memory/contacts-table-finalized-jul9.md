---
name: contacts-table-finalized-jul9
description: "Jul 9 2026 Contacts (Buying Committee) Clay table finalized: 94 rows, QBP formulas rekeyed to parent_key, ZeroBounce validation run, critic flipped, coverage note written"
metadata: 
  node_type: memory
  type: project
  originSessionId: a985e1b3-83a3-4b00-96d5-4eb5b23bd194
---

Contacts (Buying Committee) table (t_0thtm73HHxyiupTuepK, workbook wb_0thtlocqNeb46szQtAf, workspace 1180800) finalized Jul 9 2026. This supersedes the "tables not stood up" framing in [[clay-tables-not-live-yet]] for THIS table; it is live and fully built.

What changed Jul 9:
- The 3 QBP formula columns (Cliff-Edge Contracts, Account Forgone QBP, Why Now) were rekeyed from `{{Company}}` (only matched 5 parents) to `{{parent_key}}` with a full 29-parent-key map, so they compute for all 94 rows. Method reproduced exactly: 3.5-star cliff cut of StarRatings_Targets_2026_Tiered.csv (Humana verifies to 14 / 1776.3 / 568.9). 9 parents at 3.0 stars have no cliff contract; Why Now says so honestly. Numbers are Dallas public-data analysis, labeled in-cell, never Intradiem-verified. Full map: greenlight-pack/Contacts_QBP_2026Cycle_AllParents.csv.
- Email validation RAN (authorized): ZeroBounce (Clay-managed, 0.1/row) on 78 emailed rows = 7.8 credits. Running total 150.1 of 5000. Results: 67 valid (3 catch-all), 8 invalid mailbox_not_found, 3 greylisted, 16 no-email skipped. Details greenlight-pack/Validation_Results_Jul9.csv.
- critic_email_valid repointed from Email Status=="verified" to the ZeroBounce {{Status}}=="valid". Now PASS for the 67 deliverable rows. send_ready still HOLD on all 94 (human_approved unchecked). Nothing sent.
- data_source display column corrected from the wrong "Clay enrichment run Jul 6" to an honest two-cohort static string.
- Coverage: 27 new-logo-eligible Tier A+B parents, 25 covered. 2 true gaps (Athena/Solis, HMSA). cc_ops persona thin (only Centene/HCSC/Medica). 4 parents name-covered but email-dark (Presbyterian, VNS, Excellus/Lifetime, ATRIO). Full note + gap-fill spec: greenlight-pack/09_Contacts_Coverage_and_GapSpec_Jul9.md.

Jul 9 later — gap-fill expansion (Dallas authorized more credit spend for qualified leads):
- Sourced 44 cc_ops/operations leaders via Clay Find People (free import), waterfalled their emails (~48cr) in the pull table, promoted 43 to Contacts. Contacts now 137 rows (was 94). Parent-level gaps CLOSED: Solis (solishealthplans), HMSA, Presbyterian (phs), VNS, plus the cc_ops persona across ~22 eligible parents. All 43 behind HOLD gate; nothing sent.
- OPEN BLOCKER: the 43 promoted rows have BLANK canonical Email/Email Status/Source Motion/Sourced Date in Contacts. Emails were found and live in the pull table (Healthcare Quality Leadership Medicare Stars) but did NOT thread through the 2-hop promote (pull->staging->Contacts) into the Contacts Email field. Re-ran the Send table data wire with Email checked + update-existing ON (0cr) = did not populate; emails stuck in a staging column the wire's Email mapping isn't reading. Verified via record panel (Christina O./Devoted, Pedro Rivera/NYC H+H = Email blank). Validate Email reads aux New Column (8), also blank for new rows, so ZeroBounce found nothing new to validate.
- FIX DONE Jul 9 (Dallas said "run it now", chose the free path): built Lookup Single Row in Other Table on Contacts keyed LinkedIn URL == pull table (Healthcare Quality Leadership Medicare Stars) -> Record Found for all 43 (0 credits, Clay-internal). Built coalesce formula column (default name "Formula") = `{{Email}} || {{Lookup Single Row in Other Table (2)}}?.record?.Email` = single email_final for all 137. Repointed Validate Email (ZeroBounce) input from New Column (8) to that coalesce column and ran 59 out-of-date rows (5.9 credits). Result: the 43 new cc_ops rows now carry validated emails — majority Valid, a few Invalid (Michael Sobetzko, Jenni Harlow), 2 Missing where waterfall found none (Sherman Card, Jayesh Patel). Running total ~204cr of 5000. Everything still HOLD; nothing sent; all auto-run OFF.
- HYGIENE DONE (Jul 9, via Claude in Chrome, 0 credits): coalesce column renamed to email_final; "Sync leads to campaign" remapped so email_final feeds the campaign Email field (old blank canonical Email source unchecked from the sync); saved with "Save and don't run", all rows still "Run condition not met". Canonical plain Email column stays blank for the 43 new rows by design (email_final is the single source of truth for validation and the sequencer merge).

Drift risks / handed off (not done):
- The 3 QBP columns' top DESCRIPTION boxes still describe old Company logic. Live formula is correct; do NOT click Regenerate or it rebuilds the 5-parent version.
- "Sync leads to campaign" enrichment still maps off aux New Column (2); repoint before any launch. HOLD/0% run, do not run.
- Aux ground-truth columns left visible (cosmetic).
- Clay UI mechanic learned: the two-box formula editors accept pasted `{{token}}` as a chip; the single-reference boxes (Email Status, data_source) turn a pasted formula into STATIC TEXT. Use "/" insertion for chips in single-reference boxes, or just paste plain static text.
