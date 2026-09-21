---
name: sf-freshness-gate-sep21
description: No-connector Salesforce fix: builders fail closed on an unread pre-pipeline record; scheduled report email feeds Last Modified; staged, Outlook leg unproven
metadata:
  type: project
---

Built Sep 21 2026 after [[frank-assurant-package-sep16]] was found 15 days behind Frank's record. IT is pushing back hard on a Salesforce MCP connector, so nothing here uses one.

- Gate: `motions/shared/sf_freshness.py`, registry `automation/config/sf_record_reads.json` (frank/assurant read Sep 21; keegan/vanguard and alex/pnc registered, never read). States FRESH, STALE, MISSING, NA, UNREGISTERED. Stale on a stage move in stage_history.csv, a Last Modified date from the report feed, or a read older than 14 days on an open stage. Wired into Frank's Assurant room and brief (both stamp "Salesforce record read <date>"), Keegan's build_rooms.py and build_briefs.py, Alex's build_rooms.py. Exit 2; `--allow-stale` builds anyway. A record counts as read only via `--mark-read` after the record PAGE was printed to PDF (inbox `automation/inbox/partners/sf_records/`) and the package rebuilt from it.
- Side effect to expect: Keegan's and Alex's builders now stop until the Vanguard (Sagess3 Vanguard Group) and PNC (Genesys - PNC) record pages are read, or `--allow-stale` is passed.
- Feed: `automation/sf_report_intake.py` (dry run default, `--apply`, `--check-only`), agent `sf-report-intake`, runner `automation/run_sf_report_intake.sh`, plist `com.dallasandrews.gtm.sfreportintake` weekdays 7:15 written and NOT loaded. Log family `sf-prepipeline-watch`, rundown source 21, registry row added. Tests: `automation/test_sf_freshness.py`, 16 checks.
- Click sheet: `motions/partner_channel/Salesforce_Report_Subscription_Click_Sheet_Sep21.md`. Deliberately NOT a Polar task: no AI browser in Salesforce while IT objects. Report `GTM Pre-Pipeline Changed Last 7 Days`, no Notes column (Salesforce cuts long text at 255 chars in subscription exports, known issue).
- Unproven: whether the M365 connector reaches an email attachment, and what the subscription email body looks like. No such email existed Sep 21. Do not load the plist until one real email has been ingested with a matching row count.
- Parser fix same day: `intake_sf_prepipeline.py` matched "Customer Meet" inside Salesforce's real label "Scheduling 2nd Customer Meet" and glued "Scheduling 2nd" onto 11 record names. Fixed; run_2026-09-20 regenerated as of its own date; stage_history.csv cleaned; still 9 moves. The Sep 20 intake HAD caught Assurant's stage move; nothing connected it to the builders.

**Why:** the data was already in the repo; the miss was that no builder had to look at it.
**How to apply:** any new rep package builder calls `sf_require("<rep>/<account>")` and registers the package, with rec_key null and a reason when no pre-pipeline record exists.
