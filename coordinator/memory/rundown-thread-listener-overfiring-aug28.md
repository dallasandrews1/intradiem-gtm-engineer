---
name: rundown-thread-listener-overfiring-aug28
description: "GTM Daily Rundown thread listener job is firing far more often than needed, ~10min intervals with 50+ zero-reply checks logged in one day (Aug 28 2026)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 05dfc886-92b1-46d0-918f-ccc7bbe5694c
  modified: 2026-08-28T20:57:39.436Z
---

As of 2026-08-28, `automation/logs/rundown-thread-<date>.md` shows the rundown-thread-listener unattended job running roughly every 10 minutes since 07:07 CDT, logging "no new replies" 50+ times in a single day with zero Dallas replies in either the Aug 27 or Aug 28 rundown DM thread.

**Why:** each run burns a Slack thread read + full coordinator-context load even on a quiet day. At a 10-minute cadence this is a lot of token spend for a listener whose only job is to catch Dallas's in-thread replies, which are infrequent.

**How to apply:** flag to Dallas that the launchd/cron interval for this listener should probably be widened (e.g. 30-60min) unless there's a reason it needs near-real-time pickup. Don't fix it unilaterally (job scheduling config is outside this listener's file-write scope) — surface it in the rundown or when Dallas is next in a live session. Check `automation/logs/rundown-thread-*.md` timestamps to confirm current cadence before recommending a specific new interval.
