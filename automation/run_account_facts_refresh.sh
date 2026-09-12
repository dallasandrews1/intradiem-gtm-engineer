#!/bin/zsh
# Weekly account-facts refresh (live loop component 4). Launched by com.dallasandrews.gtm.accountfacts
# (Sunday 06:00) once Dallas loads the plist. Step 1 (deterministic): pick the universe domains due a
# refresh. Step 2 (Claude): fan out the researcher prompt, three accounts per agent, strongest model,
# JSON only, into automation/inbox/account_facts/<date>/. Step 3 (deterministic): validate + merge,
# DRY RUN until automation/config/account_facts.json says merge=true. Log-only, never DMs (rule 2).
set -uo pipefail
export LATE_RETRY=1
ROOT="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
cd "$ROOT"
TODAY=$(date +%Y-%m-%d)
LOG="automation/logs/account-facts-$TODAY.md"
INBOX="automation/inbox/account_facts/$TODAY"
mkdir -p "$INBOX" automation/logs
due=$(python3 automation/account_facts_merge.py --select)
if [ -z "$due" ]; then
  printf '# account-facts %s\n\nnothing due (every universe account has a fact under the age limit)\n' "$TODAY" >> "$LOG"
  exit 0
fi
printf '# account-facts %s\n\nselected for refresh: %s\n\n' "$TODAY" "$(printf '%s' "$due" | tr '\n' ' ')" >> "$LOG"
SINCE=$(date -v-120d +%Y-%m-%d)
"$ROOT/automation/lib/claude_net.sh" --model claude-fable-5-1 -p "$(cat <<PROMPT
Unattended scheduled run: weekly account-facts refresh for Intradiem's TAM engine. Log-only, no Slack, no sends, no credits.
1. The domains due a refresh, one per line:
$due
2. Read automation/prompts/account_facts_researcher.txt. Split the domains into groups of three and launch one signal-researcher agent per group, in parallel, on the strongest model, with that prompt filled in (TODAY=$TODAY, SINCE=$SINCE, ACCOUNTS=the group's domains with company names if you know them).
3. Save each agent's JSON array verbatim to $INBOX/<group-number>.json. Validate that each file parses as JSON before saving; if an agent returned prose, extract the array or write an empty array and note it.
4. Then run: python3 automation/account_facts_merge.py --inbox $INBOX   (dry run unless config says merge=true) and append its output to $LOG.
5. Modify nothing else. Do not edit tam_accounts.csv, triggers.csv or any config.
$(cat "$ROOT/automation/lib/log_resilience.txt" 2>/dev/null)
PROMPT
)" --dangerously-skip-permissions >> "automation/logs/_run_account_facts.out" 2>&1
