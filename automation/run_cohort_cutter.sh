#!/bin/zsh
# cohort-cutter: Lane B of the signal-marketing loop. Weekly Tuesday 08:00 launch; the script itself enforces the
# bi-weekly anchor (heat_loop.json cohort.anchor_tuesday + interval_days) and exits on off-weeks. 0 credits.
# DRY RUN until automation/config/heat_loop.json says otherwise. Writes cohort files + a log; never sends anything.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export PATH="$(ls -td $HOME/.claude/plugins/cache/clay-plugins/clay/*/bin | head -1):/opt/homebrew/bin:/usr/local/bin:$PATH"
WT="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer.worktrees/vs-code-agents-window-usage"
[ -f "$WT/tam-outbound-engine/config/web_intent.json" ] && [ ! -f tam-outbound-engine/config/web_intent.json ] && export HEAT_ROOT="$WT"
python3 automation/cohort_cutter.py >> "automation/logs/_run_cohort_cutter.out" 2>&1
