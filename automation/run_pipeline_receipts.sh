#!/bin/zsh
# Unattended weekly pipeline-receipts-tracker run. Launched by com.dallasandrews.gtm.pipelinereceipts (see ~/Library/LaunchAgents).
# Runs Thursday so the receipts summary is fresh for the Friday readout. Still run on-demand any time.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the pipeline-receipts-tracker agent definition at /Users/dallasandrews/.claude/agents/pipeline-receipts-tracker.md exactly and do its job now: read the receipts ledger Dallas maintains plus the credit ledger, and compute credits-in vs qualified replies/meetings-out per motion for the renewal case.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown and Friday readout read your log.
- Read-only. Never spend a credit, run a wave, or edit the ledger. If a ledger entry looks wrong, flag it, do not correct it.
- Count replies/meetings ONLY from automation/logs/credit_pipeline_receipts.md. Do not infer outcomes from an inbox. Surfaced vs realized never blended.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- Figure out today's date yourself, write the full summary to automation/logs/pipeline-receipts-<todays-date>.md.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_pipeline_receipts.out" 2>&1
