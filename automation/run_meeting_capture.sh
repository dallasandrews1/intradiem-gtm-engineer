#!/bin/zsh
# Unattended daily meeting-capture run. Launched by com.dallasandrews.gtm.meetingcapture (see ~/Library/LaunchAgents).
# Runs before the war room so any drafted follow-ups and missing-record flags are on disk for the daily rundown.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the meeting-capture agent definition at /Users/dallasandrews/.claude/agents/meeting-capture.md exactly and do its job now: scan Otter for new transcripts, capture outcomes/next-steps/economic data, draft the follow-ups, and flag any meeting with no record.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. No Slack, no email, no post, to anyone including Dallas. You only write files. The daily rundown reads your log.
- Read-only on the source. Draft and flag only, never send, never edit CRM, never contact anyone.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/ (your dated log plus the .meeting-capture-state timestamp file).
- If Otter is unreachable in this headless run, say so plainly in the log rather than producing nothing.
- Figure out today's date yourself, write the full log to automation/logs/meeting-capture-<todays-date>.md, and include a one-line "ran, N new meetings" note even if nothing new so a silent failure is visible.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_meeting_capture.out" 2>&1
