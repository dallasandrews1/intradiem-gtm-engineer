---
name: rundown-job-outage-since-aug11
description: The gtm-daily-rundown scheduled job has now failed to fire in two separate windows (Aug 11-16, and again Aug 22-25 ongoing, day 5); it resumed and ran cleanly Aug 17-21 in between
metadata: 
  node_type: memory
  type: project
  originSessionId: 036561f9-294c-4bc5-9857-c3cc47c76b40
  modified: 2026-08-25T12:26:31.062Z
---

The daily `gtm-daily-rundown` Slack DM (channel D0BAZ4NRVAN) has had two separate outage windows, not one continuous one. First outage: stopped after 8/11, resumed 8/17 (per `rundown-dm-pointer.json`, which has clean entries for 8/17 through 8/21, each with a normal thread and Dallas replies handled same-day). Second outage: after the 8/21 08:02 CDT rundown, no new "Daily Rundown" message has posted as of repeated live Slack checks through 2026-08-25 (day 5 of this second outage, Aug 22-25; confirmed again by the rundown-thread-listener run, which also found no reply activity to process since there's no live thread). The 8/21 rundown itself was already flagged "degraded" - war room, Friday/Naveen readout, gate-integrity, deliverability-watch, and stars-refresh-watch all failed their scheduled runs that same day on "API Error: Connection closed mid-response," the same failure class the Aug 15 [[late-crash-resilience-aug17]] fix targeted. That points to the rundown job itself now being hit by the same or a related unguarded-crash pattern, not a config regression.

**Why:** Both windows share the same shape - a burst of same-day scheduled-job failures that includes the rundown, followed by the rundown going fully silent (not degraded-but-posting, just absent) for multiple consecutive days. The `guarded_claude`/`LATE_RETRY` wrapper work closed the first window's root cause for 12 wrapped jobs as of 8/15, but evidently doesn't fully cover whatever is now killing the rundown job specifically starting 8/22.

**How to apply:** Before trusting `automation/logs/rundown-dm-pointer.json` or this memory as current, verify against a live Slack read of D0BAZ4NRVAN - the pointer file only updates when the job actually fires, so silence there is itself the signal. If a future session finds the rundown has resumed, update this memory with the new resume date rather than assuming the outage is permanent - it has already self-resolved once. If still down, surface as the top blocker: this is Dallas's only automated morning ping per [[single-morning-brief-rule]], so a silent outage means zero automated swarm signal reaches him. Check whether `guarded_claude`/`LATE_RETRY` coverage has been extended to the rundown job's own script, and whether the `stuck-run-severity-escalation` proposal (queued by agent-architect on 8/21) that targets this exact class ever got approved and built.
