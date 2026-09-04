---
name: council-feed-and-stamp-plans-sep4
description: Sep 4 2026, council meeting CSV emitter (automation/council_meeting_feed.py, Genna's Cold outreach schema) and per-campaign Salesforce stamp plans (automation/lead_source_stamp_plan.py, 11 CSVs / 1,141 rows) built; no Salesforce write path exists, Sierra's Lead Source ticket is the gate
metadata:
  type: project
---
`python3 automation/council_meeting_feed.py --month 2026-09` reads impact/outcomes.csv (type=meeting) plus booked-meeting lines in the main repo's automation/logs/credit_pipeline_receipts.md and writes motions/pipeline_council/GTM_Engineering_Meetings_<month>.csv with Name | Account | Date of Meeting | Category | AE | ISR | Meeting Complete | Status | Source | Stage | Channel (Source and Channel always GTM Engineering; Category Anchor for TAM tier A). Zero rows for Aug and Sep as of Sep 4. `python3 automation/lead_source_stamp_plan.py` exports every Nate lemlist campaign's leads (plus the DWO load plan) with Lead Source / Lead Origin = GTM Engineering and Primary Campaign Source `GTM Eng - <motion> - <lane>` into motions/pipeline_council/stamp_plans/.

**Why:** lemlist has no CRM integration on the team and the repo has no Salesforce write; until the picklist value ships (Sierra's ticket, OKR O1 KR1 by Sep 12), the stamp plan CSV is the handoff so nothing lands in Cold or Digital.

**How to apply:** run the feed by the 2nd business day each month and hand the CSV to Genna; re-run the stamp plan after every load. Related: [[pipeline-council-context-aug24]].
