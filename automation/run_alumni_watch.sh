#!/bin/zsh
# Unattended weekly alumni-champion-watch run. Launched by com.dallasandrews.gtm.alumniwatch (see ~/Library/LaunchAgents).
# Watches former-customer alumni rosters for job changes (the Jeffrey Foss / Citizens pattern) and logs flags for the daily rundown.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the alumni-champion-watch agent definition at /Users/dallasandrews/.claude/agents/alumni-champion-watch.md exactly and do its job now: try the SalesNav alert-email surface first (Outlook via the Microsoft 365 MCP; if unavailable this run, log the BLOCKED line and fall back to the web method), cross-match named contacts against ALL live rosters per the definition, and flag job changes landing inside a TAM.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only everywhere except automation/logs/. Never contact anyone, never touch Clay or Lemlist.
- If no roster file exists yet, write the one-line log and exit cleanly.
- Figure out today's date yourself, write the full log to automation/logs/alumni-watch-<todays-date>.md.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_alumni_watch.out" 2>&1
