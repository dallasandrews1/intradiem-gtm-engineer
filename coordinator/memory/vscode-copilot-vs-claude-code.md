---
name: vscode-copilot-vs-claude-code
description: Decision — no paid GitHub Copilot needed alongside Claude Code Max 20x; keep all agent work in one harness.
metadata:
  type: feedback
---

Dallas already pays for **Claude Code Max 20x** (do not re-pitch Claude pricing tiers to him). His "VS Code Agents / write to agents in the same window / worth a paid account?" question is about **GitHub Copilot** (VS Code's native AI: inline completion, chat, agent mode, parallel agent sessions), not Claude.

**Decision / guidance given 2026-07-18:** No paid Copilot needed for the GTM build.
- Copilot agent mode + chat overlaps Claude Code and is weaker for his orchestration/GTM work; two agent surfaces that don't share state or memory = fragmentation, not leverage.
- The only non-redundant Copilot layer is inline ghost-text autocomplete while hand-typing code (Claude Code is conversational, no passive completion). Free Copilot tier covers light use; pay (~$10/mo Individual) only if he hits the completion cap while hand-writing engine code.
- "Coordinating other agents" is done via the instruction layer Claude Code owns (skills, CLAUDE.md, `.claude/agents/` subagent defs), not by cross-writing to a Copilot chat. One harness.

**Why:** he's building one coordinated brain (the supervised orchestrator). A second paid agent surface splits it.

**How to apply:** keep every agent/orchestration job in Claude Code Max 20x; free Copilot only as an optional autocomplete complement. The underused levers that actually matter are inside Claude Code already: the Workflow tool (phase-2 orchestrator substrate), subagents, hooks. See [[gtm-daily-rundown-jul18]] and [[vscode-work-macbook-account-split]].
