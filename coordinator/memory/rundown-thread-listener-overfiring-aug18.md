---
name: rundown-thread-listener-overfiring-aug18
description: "UNRESOLVED as of 2026-08-28 — the gtm-daily-rundown thread-listener job still fires every ~10 minutes all day, bloating automation/logs/rundown-thread-<date>.md with dozens of near-identical \"no new replies\" lines; first seen 2026-08-18, still happening 10 days later"
metadata: 
  node_type: memory
  type: project
  originSessionId: e9157be0-ac8b-49df-b874-9a101ad9030a
  modified: 2026-08-28T16:42:06.897Z
---

On 2026-08-18, `automation/logs/rundown-thread-2026-08-18.md` accumulated 50+ near-identical "no new replies" entries between 07:01 CDT and 17:22 CDT, roughly one every 10-11 minutes. Every run correctly found no new Dallas replies and posted nothing to Slack, so no harm to Dallas, but the cadence is far tighter than a rundown-reply listener needs to be and the log is now noisy for anything (like the daily rundown) that reads it.

**Still happening 2026-08-28:** `automation/logs/rundown-thread-2026-08-28.md` shows the same pattern - runs roughly every 10 minutes from 07:07 CDT through at least 11:41 CDT (25+ entries by midday), one of which self-flagged "cadence still excessive (~90+ runs today)". No misfire this time (both the Aug 27 and Aug 28 rundown threads genuinely had zero replies each check), just continued over-polling. The scheduling fix from the original finding was never applied.

One run at 11:32 CDT on 8/18 did misfire in a different way: it briefly treated its own prior Claude-authored reply (ts 1787005186.665519, signed "Sent using Claude") as a new Dallas instruction, because the Slack "From" field shows Dallas Andrews/U0BB0VCHDCH for both human and bot-authored messages in this self-DM. It posted an acknowledgment reply, then a later run caught and logged the correction, and added that ts to `processed_reply_ts`. The content of the accidental reply was accurate, so it was left in place.

**Why:** No scheduling cadence has been fixed for this job. Whatever cron/launchd config triggers it appears to run far more often than needed for a Slack-reply listener, and the "From" field alone is not a reliable way to distinguish Dallas from Claude in this DM. The signature line "Sent using Claude" is the reliable discriminator.

**How to apply:** If asked to debug rundown-thread-listener noise, log bloat, or accidental self-replies, start here. Two separate fixes worth considering: (1) widen the poll interval for this specific job - check the launchd/cron config that triggers `rundown-thread-listener`, it's been running ~6x too often for 10+ days with nobody fixing the schedule itself, (2) always check for the "Sent using Claude" signature suffix before treating any thread message as Dallas-authored, never rely on the Slack "From" field alone in this DM.
