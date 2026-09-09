---
name: rundown-job-outage-since-aug11
description: RECURRING — gtm-daily-rundown scheduled job has had three outage windows (Aug 11-16, Aug 22-24, and Sep 9 missed entirely); fired cleanly Aug 25 through Sep 8 in between
metadata: 
  node_type: memory
  type: project
  originSessionId: 036561f9-294c-4bc5-9857-c3cc47c76b40
  modified: 2026-09-09T21:13:49.743Z
---

The daily `gtm-daily-rundown` Slack DM (channel D0BAZ4NRVAN) has had three separate outage windows, same failure shape each time - a burst of same-day scheduled-job failures ("API Error: Connection closed mid-response," the class the Aug 15 [[late-crash-resilience-aug17]] fix targeted) followed by the rundown going silent.

**History:** stopped after 8/11, resumed 8/17. Second gap: after 8/21, silent through 8/24, resumed 8/25. Fired cleanly every weekday 8/25 through 9/8 (confirmed live via Slack reads at multiple checkpoints). **Third gap: Sep 9 2026 - the rundown never posted at all.** Verified at 16:13 CDT (8+ hours past the normal ~07:54 CDT fire time) via live Slack read of channel D0BAZ4NRVAN: latest message in the channel is still Sep 8's rundown, no `rundown-dm-pointer.json` entry exists for 9/9. The Aug 15 LATE_RETRY fix and the Aug 15 [[late-crash-resilience-aug17]] incremental-logging contract evidently don't fully cover this job, or a new failure mode appeared.

**How to apply:** Treat this as a recurring, not resolved, failure mode - the job has now missed in 3 separate windows across a month despite an interim fix. Before trusting `rundown-dm-pointer.json` as current, live-check the Slack channel directly if the most recent entry is more than 1 business day old. If Sep 10's rundown also fails to fire, escalate: this is no longer an isolated blip and needs the `stuck-run-severity-escalation` proposal (queued by agent-architect 8/21, still unconfirmed as ever built) or equivalent monitoring, since nothing currently pages Dallas when the job itself goes silent - the listener that reads this thread only reacts to replies on a message that was never sent.
