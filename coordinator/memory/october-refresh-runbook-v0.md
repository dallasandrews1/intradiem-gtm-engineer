---
name: october-refresh-runbook-v0
description: "October CMS Stars refresh runbook (v0, Jul 14) sets up the recurring annual re-score cycle: download, wire member map, dry-run, full run, re-import at parent grain, notify every wait-for-October account within 48 hours"
metadata:
  node_type: memory
  type: project
  originSessionId: catchup-jul17-2026
---

`october-flywheel/RUNBOOK_October_Refresh.md` (v0, Jul 14 2026) is the recurring annual process for when CMS publishes new Star Ratings each October (expected early-to-mid Oct 2026 for 2027 ratings): download → wire the member map (the one real manual step since CMS renames files every cycle) → dry-run until drift looks sane → full run produces four outputs (movement report, refreshed universe, engine swap-in CSV, drift report) → data-only swap into the signal engine → Clay re-import **at parent grain, never contract grain** (a cost mistake already made once, see [[clay-build-audit-jul12]]) → every account that got a "wait for October" objection reply gets their own movement emailed within 48 hours, a promise the reply-engine's `wait_for_october` follow-up already makes (see [[reply-engine-v1-built]]) → log to war room, Friday readout, and memory.

Graduates (accounts that cross 4.0 and self-clean out) are framed as a self-cleaning success story, not a loss. Nothing in the refresh sends anything on its own; it only re-scores. Ties to [[star-ratings-universe-vintage]] (the standing "always re-pull each October" rule this runbook operationalizes).
