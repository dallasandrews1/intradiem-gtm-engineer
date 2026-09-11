#!/bin/zsh
# Unattended Monday owner-digest run. Launched by com.dallasandrews.gtm.ownerdigest (STAGED Sep 10 2026, not loaded).
# Composes per-owner open items from the PMO tracker rows + account-health log, creates Outlook DRAFTS only, writes the log the rundown reads.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the owner-digest agent definition at /Users/dallasandrews/.claude/agents/owner-digest.md exactly and do its job now: run automation/owner_digest.py, then create an Outlook DRAFT for each entry in the log's DRAFTS block after confirming the address, and append the draft ids to the log.

This is an unattended scheduled run. Ground rules for this run only:
- DRAFTS ONLY. Never send. Message nobody on Slack. The daily rundown carries Dallas's block.
- Read-only everywhere except automation/logs/ and Dallas's Outlook Drafts folder.
- If Outlook is unavailable, log the BLOCKED line and finish.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_owner_digest.out" 2>&1
