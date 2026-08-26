#!/bin/zsh
# Unattended weekly competitor-displacement-watch run. Launched by com.dallasandrews.gtm.competitorwatch (see ~/Library/LaunchAgents).
# Reads the week's war-room logs (does not re-scan the web) and turns competitor mentions into displacement briefs.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the competitor-displacement-watch agent definition at /Users/dallasandrews/.claude/agents/competitor-displacement-watch.md exactly and do its job now: read the week's war-room logs for competitor mentions and turn each into a displacement brief.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only, internal briefs only. Never contact a prospect, never send.
- Do not re-scan the web; consume what the war-room logs already surfaced.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- Figure out today's date yourself, write the full log to automation/logs/competitor-displacement-<todays-date>.md, or a plain "no fresh competitor mentions this week" line if there are none.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_competitor_watch.out" 2>&1
