---
name: jack-uk-campaigns-zero-tasks-since-aug19
description: "Jack's two UK Lemlist campaigns (Insurance/FS, Airlines) have shown zero open tasks on every daily-action-brief run since 2026-08-19"
metadata: 
  node_type: memory
  type: project
  originSessionId: db63e693-fbdd-43db-8006-b29f2be6fbee
  modified: 2026-08-24T07:37:53.168Z
---

Jack's two live Lemlist campaigns — Insurance/FS (`cam_nwKASgttBM6QT8XGq`) and Airlines (`cam_fHGtNHbbj7LmThFgX`) — have returned zero open tasks via `/api/tasks?filters=%5B%5D` on every daily-action-brief dry run since 2026-08-19 (confirmed again 2026-08-24, five consecutive due-runs). All open tasks in that endpoint the whole period belong to Nathan's Blitz campaigns (Citizens, The Hartford) instead. Zero replies too, per the relay's inbox checks.

**Why:** The action-brief job (automation/config/action_brief.json) composes nothing for a brief with zero tasks and zero replies (silence-on-empty rule), so Jack's brief has been silently skipping for at least 5 days running. That's expected behavior for the job, but 5+ days of zero tasks on both UK campaigns looks less like "caught up" and more like an upstream lead-load or sequence-activation stall — Jack's campaigns may not actually be feeding new manual tasks the way Nathan's Blitz motion is.

**How to apply:** If asked about Jack's UK motion status or why his channel has been quiet, don't assume it's just the lemlist plan gate (that affects Nathan's autopilot visibility too, but not task counts). Worth checking whether Insurance/FS and Airlines sequences are actually live/loaded with leads, not just assuming the silence-on-empty skip is benign. See `lemlist-approval-status` for the broader plan-gate context this sits alongside.
