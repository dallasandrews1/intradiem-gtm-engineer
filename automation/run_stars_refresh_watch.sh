#!/bin/zsh
# Unattended weekly stars-refresh-watcher run. Launched by com.dallasandrews.gtm.starsrefreshwatch (see ~/Library/LaunchAgents).
# Watches for the annual CMS Star Ratings release and stages the October refresh when it lands. Should go daily from early September.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the stars-refresh-watcher agent definition at /Users/dallasandrews/.claude/agents/stars-refresh-watcher.md exactly and do its job now: check whether CMS has published the new Star Ratings, compare against the last-known release, and if new, STAGE the October refresh.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only and staging only. Never re-run the universe rebuild, never overwrite the live universe file, never notify an account, never send.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/ (your dated log plus the .stars-refresh-state marker).
- Figure out today's date yourself, write the full log to automation/logs/stars-refresh-watch-<todays-date>.md: release status, and if triggered, the staged refresh checklist plus the wait-for-October notify list.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_stars_refresh_watch.out" 2>&1
