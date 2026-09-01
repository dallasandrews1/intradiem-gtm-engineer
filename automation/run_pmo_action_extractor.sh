#!/bin/zsh
# Unattended daily PMO action-item extraction (AI-enabled PMO goal, Product / Monday.com AI Initiatives).
# Launched by com.dallasandrews.gtm.pmoextractor (see ~/Library/LaunchAgents). Runs after meeting-capture
# and before the daily rundown so the day's register and validation queue are on disk when the rundown reads logs.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the pmo-action-extractor agent definition at /Users/dallasandrews/.claude/agents/pmo-action-extractor.md exactly and do its job now: resolve the window from automation/logs/.pmo-actions-state, read Otter, Outlook mail and calendar, and the Monday.com AI Initiatives board read-only, extract action items with owner, due date and verbatim evidence, dedup against automation/pmo/action_register.csv, append the register and the validation queue, report accuracy from graded rows, write the dated log, update the state file.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. No Slack, no email, no reply, no Monday update, no calendar change. You only write files. The daily rundown reads your log.
- Read-only on every source. Extract and flag only.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/ and automation/pmo/.
- If a source is unreachable in this headless run, say so plainly in the log and continue with the rest.
- Figure out today's date yourself, write the full log to automation/logs/pmo-actions-<todays-date>.md, and include the "Ran, N new items from M sources" line even when nothing is new so a silent failure is visible.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_pmo_action_extractor.out" 2>&1
