---
name: rundown-listener-excessive-cadence-aug28
description: "The gtm-daily-rundown thread listener job has been firing at ~10-minute intervals all day since Aug 28 2026, not on a reasonable poll cadence"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4f54ded0-0976-4b2e-9548-d995b623063f
  modified: 2026-08-28T23:41:22.775Z
---

The rundown-thread listener (the unattended job that checks the daily rundown DM thread for Dallas's replies) has been firing roughly every 10 minutes continuously since 07:07 CDT on 2026-08-28 — 70+ logged runs by 18:41 CDT, every single one finding zero new replies. The job's own log (`automation/logs/rundown-thread-2026-08-28.md`) has self-flagged this excessive cadence repeatedly since 21:56:59 on 2026-08-27, with no fix applied as of this writing.

**Why:** whatever cron/launchd schedule drives this listener is misconfigured to run far more often than needed — a reply-check listener doesn't need 10-minute resolution, especially against a DM that gets one message a day. Each run costs tokens for zero information gain on a quiet day.

**How to apply:** if Dallas asks why token usage looks high, or asks about this listener's schedule, point him at the actual cron/launchd config for the rundown-thread-listener job (not a file this listener run is allowed to touch — its hard file rule only permits editing `automation/logs/*` and `automation/config/rundown_thread_state.json`). The fix is a schedule-config change outside this job's own permissions, likely a launchd plist or cron entry running every ~10 min instead of e.g. hourly. Related: [[rundown-job-outage-since-aug11]] is a different, unrelated issue (the rundown DM itself failing to post) — don't conflate the two.
