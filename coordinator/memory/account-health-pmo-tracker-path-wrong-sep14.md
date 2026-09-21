---
name: account-health-pmo-tracker-path-wrong-sep14
description: "account_health.json's configured pmo_tracker_export path points at the wrong CSV, so Cleveland Clinic overdue items compute as zero — still unfixed as of Sep 21, now hiding a real overdue task"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2bac41f5-57a2-431b-a4f4-ae3d9b3ae421
  modified: 2026-09-21T12:12:09.542Z
---

`automation/config/account_health.json`'s `sources.pmo_tracker_export` points at
`motions/churn_risk_save_plan/data/Project Task Tracker.csv`, which contains 33 rows all
Project Name "ADT" - zero Cleveland Clinic rows. The account-health-watch agent run on
2026-09-14 computed zero overdue items for Cleveland Clinic from this source, silently,
because the configured file has none of its rows. **Still unfixed as of the 2026-09-21
run** ([[control-tower-animated-rebuild-sep15]] era config never touched this file).

The account's real PMO rows live in a sibling file,
`motions/churn_risk_save_plan/data/Cleveland_Clinic_PMO_Tracker_Import.csv`, which the
agent used only as an unconfigured cross-reference. On 2026-09-21 that cross-reference
now shows a REAL past-due, not-yet-completed item: **Save Room, owner Dallas Andrews,
due 9/19/2026, still "In progress."** Cleveland Clinic stayed overall RED this run (5 of
7 reason codes red, unchanged from Sep 14) - this overdue item is not reflected anywhere
the scorer or the daily rundown reads.

**Why:** account_health.json was likely stamped from an ADT-account template and never
repointed per-account. A config that resolves to a file with zero matching rows looks
identical to "no overdue items" downstream (log, rundown) with no error surfaced - and
now it's actively masking a past-due task owned by Dallas himself.

**How to apply:** before trusting any account-health-watch overdue-items section as
real, verify `sources.pmo_tracker_export` in `automation/config/account_health.json`
actually contains rows for that account. Fix the Cleveland Clinic entry to point at
`Cleveland_Clinic_PMO_Tracker_Import.csv` - this is now overdue itself since it's
hiding a real overdue task (the Save Room build) from the one place Dallas would see it.
