#!/bin/zsh
# Unattended daily war-room sweep. Launched by com.dallasandrews.gtm.warroom (see ~/Library/LaunchAgents).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
/intradiem-daily-war-room

This is an unattended scheduled run — nobody is watching live. Ground rules for this run only:
- Do not send, post, or message anyone except Dallas himself.
- Do not touch send gates, campaign settings, or any live Clay/Apollo data.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/. This includes StarRatings_Earnings_Signals_2026.csv and any other file the skill's own instructions might normally tell you to log triggers into — those are live pipeline inputs, not this run's to touch unattended.
- If you find something that would normally get logged to one of those live files, instead append it to automation/logs/staged_signals.csv (create with a header row if missing) using that file's own column shape, and say in your run log that it's staged for Dallas's review, not yet merged into the live file.
- Figure out today's date yourself, then write your full findings to automation/logs/war-room-<todays-date>.md in this project (create the file).
- Do NOT DM, post, or message anyone. The daily rundown (weekdays 7:50) is Dallas's single consolidated morning brief and reads this log. Write the log completely instead: the 3-5 highest-priority signals, anything staged, and a one-line "job ran" note even if nothing fired, so the rundown has everything it needs and a silent failure is still visible in the log.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_war_room.out" 2>&1
