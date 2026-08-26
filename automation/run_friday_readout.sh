#!/bin/zsh
# Unattended Friday readout draft. Launched by com.dallasandrews.gtm.fridayreadout (see ~/Library/LaunchAgents).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
/naveen-weekly-readout

This is an unattended scheduled run — nobody is watching live. Ground rules for this run only:
- This produces a DRAFT only. Do not send or post anything to Naveen or any Slack channel. Dallas reviews and sends this himself, every time, no exceptions.
- Do not touch send gates, campaign settings, or any live Clay/Apollo data.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/ — this run reads engine_state.json/impact.json/the credit ledger/war-room logs but never edits them.
- Figure out today's date yourself, then write both the Slack-length message and the one-page brief to automation/logs/naveen-readout-<todays-date>.md in this project (create the file).
- Do NOT DM, post, or message anyone. Write the draft to the log path below. Friday's daily rundown (7:50) will surface "Naveen readout draft ready" with the path in the single morning brief. Do not paste the draft content into any channel or thread Naveen could see.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_friday_readout.out" 2>&1
