#!/bin/zsh
# Unattended weekly deliverability-watch run. Launched by com.dallasandrews.gtm.deliverabilitywatch (see ~/Library/LaunchAgents).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the deliverability-watch agent definition at /Users/dallasandrews/.claude/agents/deliverability-watch.md exactly and do its job now: check mailbox warmup status/age, whether deliverability is the gating blocker, and state the data gap.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown and Friday readout read your log.
- Read-only. Never flip the send gate, never mark a mailbox warm, never launch. Do not invent a warmup percentage.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- Figure out today's date yourself, write the full log to automation/logs/deliverability-watch-<todays-date>.md, and give a plain "green / not yet / stale" read plus what data it still needs.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_deliverability_watch.out" 2>&1
