---
name: account-health-pmo-tracker-path-wrong-sep14
description: "account_health.json's configured pmo_tracker_export path points at the wrong CSV, so Cleveland Clinic overdue items compute as zero"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2bac41f5-57a2-431b-a4f4-ae3d9b3ae421
  modified: 2026-09-14T12:13:19.482Z
---

`automation/config/account_health.json`'s `sources.pmo_tracker_export` points at
`motions/churn_risk_save_plan/data/Project Task Tracker.csv`, which contains 33 rows all
Project Name "ADT" - zero Cleveland Clinic rows. The account-health-watch agent run on
2026-09-14 computed zero overdue items for Cleveland Clinic from this source, silently,
because the configured file has none of its rows.

The account's real PMO rows live in a sibling file,
`motions/churn_risk_save_plan/data/Cleveland_Clinic_PMO_Tracker_Import.csv`, which the
agent used only as an unconfigured cross-reference (nearest due 9/19 and 9/25/2026, one
past-due row already Completed).

**Why:** account_health.json was likely stamped from an ADT-account template and never
repointed per-account. If more accounts get added to this watch, each needs its own
correct `pmo_tracker_export` path or the field needs to become per-account-aware; a config
that resolves to a file with zero matching rows looks identical to "no overdue items"
downstream (log, rundown) with no error surfaced.

**How to apply:** before trusting any account-health-watch overdue-items section as
real, verify `sources.pmo_tracker_export` in `automation/config/account_health.json`
actually contains rows for that account. Fix the Cleveland Clinic entry to point at
`Cleveland_Clinic_PMO_Tracker_Import.csv` when doing config maintenance on this watch.
