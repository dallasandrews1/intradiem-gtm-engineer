#!/bin/zsh
# Unattended daily GTM rundown for Dallas. Launched by com.dallasandrews.gtm.dailyrundown (see ~/Library/LaunchAgents).
# Runs after the morning war room so its log is on disk. Refreshes the control-tower state first
# (safe read-only aggregation) so gates/blockers/motions are current when the brief composes.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"

python3 build_control_tower.py >> "automation/logs/_run_daily_rundown.out" 2>&1 || true

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
/gtm-daily-rundown

This is an unattended scheduled run — nobody is watching live. Ground rules for this run only:
- Do not send, post, or message anyone except Dallas himself (search for his own Slack user, not a channel).
- Do not touch send gates, campaign settings, skills, system prompts, or any live Clay/Apollo data.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/. You read control_tower_state.json, the registry, engine_state.json/impact.json, the credit ledger, account_plays.json, and today's war-room log, but you never edit them.
- Also read today's swarm log outputs in automation/logs/ and fold them into the brief: swarm-health-<today>.md (lead the brief with a one-line swarm-health status: which jobs fired, which logs are MISSING), meeting-capture-<today>.md (new-meeting captures, drafted follow-ups, missing-record flags), the [AGENT] proposals in proposal_ledger.md, gate-integrity-<recent>.md (any customer-exclusion FLAG goes near the top as a blocker), pipeline-receipts-<recent>.md, deliverability-watch-<recent>.md, competitor-displacement-<recent>.md, stars-refresh-watch-<recent>.md, and table-hygiene-<today>.md (redundant/orphaned/rotted columns + safe-delete plans; lead any ROTTED finding). Also the outbound-execution logs: lemlist-relay-<today>.md and lemlist-pulse-<today>.md (replies land as top-priority items, meetingBooked is a receipts event, bounces/unsubscribes are same-day hygiene), action-brief-<today>.md (which rep briefs composed or skipped), and brief-thread-ingest-<recent>.md (any HOLD is a same-day action item for Dallas near the top: the rep believes outreach paused and nothing auto-pauses until Dallas pauses the lead in Lemlist), and context-bus-<recent>.md (the cross-laptop context drop: report it in ONE line saying whether the last drop pushed cleanly and how many sessions it carried, so Dallas knows the work Mac has something current to pull; surface a #push-failed or #stage-failed evt as a blocker, and surface any open thread it carried forward that nothing else in today's logs has closed). Not every log exists every day (some are weekly); silently skip the ones that are absent, but if swarm-health reports a MISSING upstream log, surface that.
- Never render a SEEDED or stale value as live fact. Any Intradiem metric must pass the verified-claims gate or be marked [UNVERIFIED]. Do not invent numbers to fill a section.
- Figure out today's date yourself, then write the full brief to automation/logs/daily-rundown-<todays-date>.md (create the file).
- Append any idea that implies a skill/gate/automation change to automation/logs/proposal_ledger.md as a PROPOSAL only. Do not make the change.
- Also read rundown-thread-<recent>.md (yesterday's thread conversation with Dallas): fold in anything he asked for, confirmed, or left pending there, and surface any pending CONFIRM from automation/config/rundown_thread_state.json as an open item.
- Then send Dallas one Slack DM with the ranked brief (tight version) plus the log file path. If a top gate or blocker is open, put it in the first line. If the run degraded (a state file missing or the war-room log absent), say so in the DM so a silent failure never reads as all-clear. End the DM with one line: "Reply in this thread to dig into or act on anything here."
- After the DM sends, record where it landed so the thread listener can find it: append {"date": "<today>", "channel": "<DM channel id>", "ts": "<message ts>"} to automation/logs/rundown-dm-pointer.json (create the file as a JSON array if absent, keep prior entries). If the send tool did not return a ts, read the DM conversation back to get the ts of the message you just sent. This pointer is how replies to the rundown reach the listener; do not skip it.
PROMPT
)" --dangerously-skip-permissions >> "automation/logs/_run_daily_rundown.out" 2>&1
