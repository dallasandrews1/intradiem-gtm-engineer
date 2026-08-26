---
name: war-room-recurring-api-crash
description: "The unattended daily war-room (and sometimes daily-rundown) launchd job has repeatedly crashed mid-response with no log written, silently losing days of signal coverage"
metadata: 
  node_type: memory
  type: project
  originSessionId: b5286e82-0af3-4cff-ad51-fb54b9774499
  modified: 2026-07-30T12:44:10.546Z
---

Starting the week of 2026-07-20, the unattended `run_war_room.sh` / `run_daily_rundown.sh` scheduled jobs have repeatedly died mid-response on an unrecovered "API Error: Connection closed mid-response" with no completion line and no dated log file produced. Confirmed occurrences: Jul 23 (war room), Jul 28 (both war-room AND daily-rundown died, no logs at all that day), Jul 29 (war-room again, rundown caught the gap after the fact). On 2026-07-30, two of three ad hoc research sub-agents launched to catch up on the Jul 28-29 gap also hit the identical crash on first attempt (both succeeded on retry).

**Why:** root cause not diagnosed as of 2026-07-30 — pattern looks like a transient upstream API issue rather than anything in the scripts themselves, since retries have consistently succeeded. But because the job produces no log at all on failure (rather than a partial one), a crash is invisible until the next day's rundown notices the missing file — real signal coverage (e.g. Centene's and Humana's Jul 28-29 earnings calls) was lost for two full days before the Jul 30 run caught up.

**How to apply:** Two fixes are already specced and sitting unbuilt in `proposal_ledger.md` (from the 2026-07-28 agent-architect run): `transient-api-failure-auto-retry` (mechanical retry wrapper — cheaper, addresses root cause) and `rundown-completion-watchdog` (detects a missing brief same-day instead of silently). Before assuming either is live, check `proposal_ledger.md` for Dallas's approval status. If this pattern recurs again after those are built, that's a signal the retry wrapper isn't sufficient and the underlying transient failure needs its own investigation.
