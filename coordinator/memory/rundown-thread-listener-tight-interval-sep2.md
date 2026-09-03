---
name: rundown-thread-listener-tight-interval-sep2
description: "rundown-thread listener job fires far more often than intended (~every 10 min all day Sep 2 2026), and the widen-interval CONFIRM meant to fix it has sat unanswered 59+ hours"
metadata: 
  node_type: memory
  type: project
  originSessionId: ed9fb12d-5cf3-4475-b0b3-23e801ef6983
  modified: 2026-09-03T01:47:57.046Z
---

The `gtm-daily-rundown` thread listener (unattended scheduled job, reads the rundown DM thread for new Dallas replies) has been firing roughly every 10 minutes throughout Sep 2 2026, not on whatever longer cadence was intended. Each run appends a "no new replies" line to `automation/logs/rundown-thread-2026-09-02.md`, so that log has 60+ near-duplicate entries for the day.

The fix already exists: a `pending_confirms` entry tagged `widen-interval` in `automation/config/rundown_thread_state.json` proposes bumping `StartInterval` in `com.dallasandrews.gtm.rundownthreads.plist` from 600s to 1800s. It was raised ~2026-08-31 23:56 CDT and has never been confirmed by Dallas, so it's now well past the listener's own 48-hour staleness window (the listener will re-offer it, not auto-apply it, next time Dallas replies in-thread).

**Why:** the listener can only act on a CONFIRM inside the rundown Slack thread — it can't self-approve a plist change even though the fix is fully specced and low-risk (interval-only, no logic change).

**How to apply:** next time Dallas is in a live session (not an unattended run), flag that `widen-interval` is still open and offer to apply it directly, or prompt him to reply `CONFIRM widen-interval` in the rundown thread so the next scheduled run picks it up.
