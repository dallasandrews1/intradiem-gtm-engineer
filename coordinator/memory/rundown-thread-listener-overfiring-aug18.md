---
name: rundown-thread-listener-overfiring-aug18
description: "The gtm-daily-rundown thread-listener job has been firing every ~10-11 minutes all day (2026-08-18), not on a reasonable poll interval, bloating automation/logs/rundown-thread-<date>.md with 50+ near-identical \"no new replies\" lines"
metadata: 
  node_type: memory
  type: project
  originSessionId: e9157be0-ac8b-49df-b874-9a101ad9030a
  modified: 2026-08-18T22:22:35.507Z
---

On 2026-08-18, `automation/logs/rundown-thread-2026-08-18.md` accumulated 50+ near-identical "no new replies" entries between 07:01 CDT and 17:22 CDT, roughly one every 10-11 minutes. Every run correctly found no new Dallas replies and posted nothing to Slack, so no harm to Dallas, but the cadence is far tighter than a rundown-reply listener needs to be and the log is now noisy for anything (like the daily rundown) that reads it.

One run at 11:32 CDT did misfire in a different way: it briefly treated its own prior Claude-authored reply (ts 1787005186.665519, signed "Sent using Claude") as a new Dallas instruction, because the Slack "From" field shows Dallas Andrews/U0BB0VCHDCH for both human and bot-authored messages in this self-DM. It posted an acknowledgment reply, then a later run caught and logged the correction, and added that ts to `processed_reply_ts`. The content of the accidental reply was accurate, so it was left in place.

**Why:** No scheduling cadence has been fixed for this job. Whatever cron/launchd config triggers it appears to run far more often than needed for a Slack-reply listener, and the "From" field alone is not a reliable way to distinguish Dallas from Claude in this DM. The signature line "Sent using Claude" is the reliable discriminator.

**How to apply:** If asked to debug rundown-thread-listener noise, log bloat, or accidental self-replies, start here. Two separate fixes worth considering: (1) widen the poll interval for this specific job, (2) always check for the "Sent using Claude" signature suffix before treating any thread message as Dallas-authored, never rely on the Slack "From" field alone in this DM.
