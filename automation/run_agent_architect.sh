#!/bin/zsh
# Unattended daily swarm-architect run. Launched by com.dallasandrews.gtm.agentarchitect (see ~/Library/LaunchAgents).
# Runs after the war room (7:15) so today's log is on disk, and before the daily rundown (7:50) so its
# proposals are in the ledger when the rundown composes the single morning brief.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Follow the agent-architect agent definition at /Users/dallasandrews/.claude/agents/agent-architect.md exactly and do its job now: study the current swarm and Dallas's live GTM work, then propose the next agents worth adding.

This is an unattended scheduled run — nobody is watching live. Ground rules for this run only:
- Message NOBODY. No Slack DM, no email, no post, to anyone including Dallas. You only write files. The daily rundown (weekdays 7:50) is Dallas's single consolidated morning brief and it reads your output.
- Route to no external recipient ever. Any proposal you write must respect the standing rule that nothing in this swarm messages anyone but Dallas right now; a proposal that would notify an AE, CSM, prospect, or any third party is dead on arrival.
- Read-only. Do not touch send gates, campaign settings, skills, system prompts, the registry, or any live Clay/Apollo data. You propose and spec; you never build an agent, write an agent file, or load a plist.
- Read coordinator/AGENT_REGISTRY.md FIRST so you never propose a duplicate.
- Do not write to, append to, or modify ANY file in this repo except inside automation/logs/.
- Append your ranked proposals (2 to 4 strong ones, best first) to automation/logs/proposal_ledger.md, each tagged [AGENT], grounded in something real you observed this run. If nothing new clears the bar today, append nothing to the ledger and say so in your run log — do not invent filler.
- Figure out today's date yourself, then write your full findings to automation/logs/agent-architect-<todays-date>.md (create the file), including a one-line "job ran" note even if you proposed nothing, so a silent failure is still visible in the log.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_agent_architect.out" 2>&1
