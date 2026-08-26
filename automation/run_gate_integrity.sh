#!/bin/zsh
# Unattended weekly gate-integrity-auditor run. Launched by com.dallasandrews.gtm.gateintegrity (see ~/Library/LaunchAgents).
# Weekly backstop; still run on-demand before any wave load.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the gate-integrity-auditor agent definition at /Users/dallasandrews/.claude/agents/gate-integrity-auditor.md exactly and do its job now: read REAL rows from each live motion table via Clay and prove no current customer can reach a cold send and the shared Functions still hold.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only. Never edit a Function/gate/row, never run a wave, never spend credits, never flip send-ready.
- REAL rows only. If a table is unreadable, mark that motion UNVERIFIED rather than substituting a synthetic pass.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- Figure out today's date yourself, write the full verdict to automation/logs/gate-integrity-<todays-date>.md. Any customer-exclusion FLAG goes first and loud.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_gate_integrity.out" 2>&1
