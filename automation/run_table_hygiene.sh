#!/bin/zsh
# Unattended daily table-hygiene sweep. Launched by com.dallasandrews.gtm.tablehygiene (see ~/Library/LaunchAgents).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the table-hygiene agent definition at /Users/dallasandrews/.claude/agents/table-hygiene.md exactly and do its job now: sweep the tables listed in automation/config/table_hygiene_targets.md for redundant, orphaned, and ID-rotted columns, and produce the safe-delete plan (dependents + re-point map + delete order) for each removal candidate.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only. Never delete or edit a column, never run an enrichment, never touch a gate. You flag and plan; Dallas presses delete.
- Never recommend deleting a column whose dependents you could not read — flag it for manual review instead.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- If a table is unreadable (Enterprise-gated/access), say so and skip it; do not guess its columns.
- Figure out today's date yourself, write the full report to automation/logs/table-hygiene-<todays-date>.md, lead with anything ROTTED, and include a one-line "ran, swept N tables" note even if all clean so a silent failure is visible.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_table_hygiene.out" 2>&1
