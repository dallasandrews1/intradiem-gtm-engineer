---
name: lemlist-activities-plan-gate-aug14
description: "Lemlist /api/activities route started returning HTTP 402 (emailPro-plan-only) on 2026-08-14, breaking the hourly lemlist-to-Slack relay job at step 1"
metadata: 
  node_type: memory
  type: project
  originSessionId: 896ac857-2e46-4c92-ad41-a83545bdb792
  modified: 2026-08-14T23:38:35.631Z
---

As of the 2026-08-14 16:37 PDT hourly run, `GET https://api.lemlist.com/api/activities?limit=100` (workspace key `tea_h82tSpLDH9vt59tkJ`) returns HTTP 402 with body `"route is available starting emailPro plan"` instead of the normal activity-array payload. `automation/config/lemlist.env` had already flagged this key as a trial "ending ~Aug 13 2026" — the 402 lines up with that trial lapsing/downgrading a day later. The sibling call, `GET /api/tasks?filters=%5B%5D`, still returns HTTP 200 normally — only the Activities route is gated, not the whole API.

**Why:** the relay job (`automation/config/lemlist_channels.json` + the unattended hourly prompt) depends entirely on the Activities feed for steps 2-6 (diff against `seen_activity_ids`, detect actionable events, compose/post to Slack, append new ids). With Activities gated, every hourly run will keep failing at step 1 and produce a "BLOCKED, needs Dallas" log entry (see `automation/logs/lemlist-relay-2026-08-14.md`) instead of a normal quiet or active run, until the plan is upgraded or the trial renewed.

**How to apply:** don't read a "no new events"-style log entry from this job on/after 2026-08-14 as a genuine quiet period — check whether it's actually the 402 plan-gate first. This needs Dallas to fix on the Lemlist billing side (upgrade to emailPro or renew trial); no code/config change in this repo resolves it. Once fixed, verify by re-running the activities curl and confirming HTTP 200 before trusting the relay's output again. Related but distinct from [[lemlist-relay-campaign-map-gap-aug7]] (a routing-config gap, not an API outage).
