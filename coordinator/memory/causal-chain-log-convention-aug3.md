---
name: causal-chain-log-convention-aug3
description: Adopted 2026-08-03 - evt/chain causal-chain convention for automation logs, plus the Harmoniq trigger/condition/action framing doc; broker/framework migration explicitly rejected
metadata:
  type: project
---

On 2026-08-03 Dallas evaluated external advice about event-driven agent architectures (event bus, LangGraph/mcp-agent migration, webhook tunnels) and decided the swarm already covers it. Two things were adopted, the rest explicitly rejected.

**Adopted 1, causal-chain log convention.** Canonical spec: `Intradiem GTM Engineer/automation/LOG_CONVENTION.md`. Any log item another job might act on mints `evt: <family>-<YYYY-MM-DD>#<slug>` at FIRST surfacing (carried signals keep their original id); downstream entries cite `chain: <evt>`. Ids live in `automation/logs/` only, never in the rundown DM or anything Naveen- or prospect-facing; CSVs put the id in an existing source/notes column, never a new column. Wired into: war-room skill, gtm-daily-rundown skill (log + proposal ledger entries), competitor-displacement-watch agent, AGENT_REGISTRY.md governing rule 5, and a CLAUDE.md working-conventions bullet (both copies).

**Adopted 2, Harmoniq vocabulary framing.** `Intradiem GTM Engineer/GTM_Swarm_Harmoniq_Framing.md`: internal storytelling reference mapping the swarm to Harmoniq's trigger/condition/action architecture (providers→scheduled jobs+logs, triggers→signal taxonomy, conditions→gates, actions→HOLD drafts, rule audit trail→evt/chain). Referenced from the naveen-weekly-readout skill for architecture storytelling. Prep material only, never a send.

**Rejected (do not re-propose):** streaming broker (Redis/NATS), framework migration (LangGraph, CrewAI, mcp-agent), webhook tunnel to the laptop. Scheduled sweeps plus log-and-consolidate is the correct latency and preserves the single-morning-brief rule.

**Also fixed in passing:** the war-room SKILL.md mirror copies had drifted (mirror was newer); adopted the newer version into the coordinator and corrected its stale "DMs Dallas on Slack" line to log-only per the single-morning-brief rule. Skill edits go to `coordinator/.claude/skills/` then cp to `~/.claude/skills/` (plain copies, not symlinks; check for drift before overwriting).

Related: [[agent-registry-and-architect]]
