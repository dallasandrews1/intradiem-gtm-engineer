---
name: rundown-job-outage-since-aug11
description: RESOLVED — the gtm-daily-rundown scheduled job had two outage windows (Aug 11-16, Aug 22-24) but has fired cleanly every day since Aug 25, confirmed through Aug 28
metadata: 
  node_type: memory
  type: project
  originSessionId: 036561f9-294c-4bc5-9857-c3cc47c76b40
  modified: 2026-08-28T13:00:47.762Z
---

The daily `gtm-daily-rundown` Slack DM (channel D0BAZ4NRVAN) had two separate outage windows. First: stopped after 8/11, resumed 8/17. Second: after the 8/21 08:02 CDT rundown, went silent through 8/24. Both share the same shape - a burst of same-day scheduled-job failures ("API Error: Connection closed mid-response," the class the Aug 15 [[late-crash-resilience-aug17]] fix targeted) followed by the rundown going fully silent for multiple days.

**Status as of 2026-08-28:** resolved. `rundown-dm-pointer.json` shows clean same-morning fires on 8/25, 8/26, 8/27, and 8/28 (each ~07:54 CDT), and both the 8/27 and 8/28 threads were read live via Slack and confirmed present with normal rundown content. No Dallas replies pending on either thread as of the 8/28 13:00 UTC listener check.

**How to apply:** Treat this outage as closed unless a future session finds a gap in `rundown-dm-pointer.json` again (no entry for a given weekday, or a live Slack check showing no new "Daily Rundown" message). If it recurs, re-open this memory and check whether `guarded_claude`/`LATE_RETRY` coverage was ever extended to the rundown job's own script, and whether the `stuck-run-severity-escalation` proposal (queued by agent-architect on 8/21) that targets this exact class ever got approved and built - neither was confirmed done as of this resolution.
