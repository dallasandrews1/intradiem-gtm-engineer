---
name: rundown-thread-listener-excessive-cadence-aug28
description: "rundown-thread-listener scheduled job fired ~every 10 min all day Aug 28 2026 (30+ runs, all zero-reply quiet runs), self-flagged once already the evening before"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7b3675b7-8a5a-45c4-af9f-7574fd18d289
  modified: 2026-08-28T17:25:14.286Z
---

The `gtm-daily-rundown` thread-listener job (the unattended agent that checks the rundown DM thread for new Dallas replies) ran roughly every 10 minutes continuously from 07:07 CDT through at least 12:24 CDT on 2026-08-28 — 30+ runs logged in `automation/logs/rundown-thread-<date>.md`, every single one finding zero new replies. One of those runs (11:20:30 CDT) self-flagged the same pattern referencing an even earlier flag at 21:56:59 on 2026-08-27, so this is not a one-off, it's an ongoing misconfiguration.

**Why:** Per the job's own instructions, a quiet run (no new replies) posts nothing to Slack and only appends one log line — so this isn't spamming Dallas directly, but it's burning a run (and tokens) roughly 6x/hour for no benefit, and the excessive log noise makes `rundown-thread-<date>.md` harder to scan for the runs that actually mattered. A listener checking a DM thread doesn't need sub-hourly polling — 10-15 min would already be generous.

**How to apply:** Next live session, check whatever triggers this job (launchd plist / cron / scheduled-task config for the rundown-thread-listener) and widen the interval, or confirm whether this is expected behavior from a different scheduling layer (e.g. it's meant to be event-triggered but is falling back to polling). Cross-check against [[rundown-job-outage-since-aug11]] — that memory is about the *parent* daily rundown DM not firing at all; this is a different, narrower issue about the *reply-listener* sub-job over-firing. Once fixed, this memory can be deleted.
