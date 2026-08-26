# Back-Office Persona Pull Spec (Clay run, gated on ICP v1)
**Gates, in order:** (1) Scott session produces ICP v1. (2) Credit pre-check logged to ledger (est. 1,000-1,400 credits for 200-250 contacts, per 02_Credit_Spend_Plan.md). (3) 10-row calibration sample. (4) 50-contact review with Scott + relevant CSMs. (5) Scale.

## Table architecture (mirrors the Star Ratings build, zero new patterns)
- **BackOffice_Accounts (L1):** install-base account list with function flags, FTE-band estimate, front-office health check (signal engine read), AE/CSM owner, suppression flag. Seeded free from CRM export/CSM roster; NO enrichment until accounts are ICP-v1 qualified.
- **BackOffice_Staging (find-people output):** the only credit-spending table. Title filters from ICP v1; caps per account (default 6, Scott to confirm) so no single account eats the pull.
- Staging flows into **Contacts (Buying Committee)** via Exports → Send table data → Send row for each item in a list (per 04_Wiring_Runbook.md Wire 3), so every back-office contact lands behind the SAME L5 gate: critic_email_valid, human_approved, send_ready = HOLD.

## Attribution stamp (set as constants on staging before sending)
GTM Engine Sourced = TRUE · Source Motion = back_office_install_base (or back_office_boo for universe 2) · Sourced Date = run date · universe tag · persona_key (bo_claims / bo_shared / bo_payment / coo_finance) · function · fte_band. The 200 is countable because these exist from row one.

## Dedup keys (run BEFORE enrichment spend)
1. LinkedIn URL exact match against Contacts (Buying Committee) and the install-base contact set (Maya_DropIn "Contacts @ Companies" included).
2. Email domain + normalized full name as the fallback key.
3. Cheap columns first: title/persona routing on imported data costs nothing; email waterfall only on rows that survive dedup AND match ICP v1.

## Qualification checklist (a row counts toward the 200 only if ALL true)
- universe = install_base
- persona_key matches an ICP v1 INCLUDE row (the live ICP / Persona Rubric table extends with the bo_* personas on green light; EXCLUDE rows never sourced)
- Director+ seniority (COO tier excluded from first pull)
- survives dedup; account not suppressed; AE/CSM coordination noted
- attribution stamp complete

## Handoffs
Qualified universe feeds Mandate 3 campaigns and the BOO launch kit target list. Counts and quality notes feed the Friday readout. Pain map feeds first-draft-engine when messaging starts; nothing sends without the human gate, same as everywhere else.
