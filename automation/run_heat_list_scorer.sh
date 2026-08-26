#!/bin/zsh
# heat-list-scorer: signal-marketing loop scoring job (motions/signal_marketing_loop/). Launched twice on weekdays
# (07:20 before the rundown, 13:00) by com.dallasandrews.gtm.heatlist. Pure Python, no Claude call, 0 credits.
# DRY RUN until automation/config/heat_loop.json says otherwise. Never DMs anyone; the daily rundown reads the log.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export PATH="$HOME/.claude/plugins/cache/clay-plugins/clay/2.6.0/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
# Until the vs-code-agents-window-usage branch merges, engine config (web_* families, web_intent.json) lives in the worktree:
WT="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer.worktrees/vs-code-agents-window-usage"
[ -f "$WT/tam-outbound-engine/config/web_intent.json" ] && [ ! -f tam-outbound-engine/config/web_intent.json ] && export HEAT_ROOT="$WT"
python3 automation/heat_list_scorer.py >> "automation/logs/_run_heat_list_scorer.out" 2>&1
