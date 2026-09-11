#!/bin/zsh
# Unattended weekly account-health-watch run. Launched by com.dallasandrews.gtm.accounthealth (STAGED Sep 10 2026, not loaded).
# Refreshes churn-risk account evidence and runs the scorer; writes automation/logs/account-health-<date>.md for the daily rundown.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the account-health-watch agent definition at /Users/dallasandrews/.claude/agents/account-health-watch.md exactly and do its job now: refresh each configured account's evidence file from the Success Plan notes, the newest adoption deck, Sales Navigator alert emails, Otter and the PMO tracker export, then run automation/account_health_score.py.

This is an unattended scheduled run. Ground rules for this run only:
- Message NOBODY. You only write files; the daily rundown reads your log.
- Read-only everywhere except the evidence files under motions/churn_risk_save_plan/data/ and automation/logs/. Never touch Clay, lemlist or Salesforce.
- If a source is unavailable, log the BLOCKED line and continue.
- Figure out today's date yourself; the scorer names the log automation/logs/account-health-<today>.md.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_account_health_watch.out" 2>&1
