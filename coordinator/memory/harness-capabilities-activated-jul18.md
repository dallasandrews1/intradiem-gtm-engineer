---
name: harness-capabilities-activated-jul18
description: Subagents, a Workflow, and an instruction-changelog hook activated Jul 18 to back the phase-2 orchestrator.
metadata:
  type: project
  date: 2026-07-18
---

Dallas asked to activate every underused harness capability. Done 2026-07-18 (he already drives the VS Code agent; the gap was the harness features, not the editor).

**Subagents** (`~/.claude/agents/`, mirrored to `coordinator/.claude/agents/`): `signal-researcher` (read-only web research, fan out per account/motion), `clay-operator` (Clay CLI/MCP build+enrich, checks existing workflows first, never flips a gate), `gtm-copy-reviewer` (adversarial copy QA, verified-claims gate). Each scoped to one work mode so the orchestrator can fan out. Invoke via the Agent tool with subagent_type, or Claude auto-delegates.

**Workflow** (`coordinator/.claude/workflows/gtm-proposal-sweep.js`, mirrored to `~/.claude/workflows/`): read-only phase-2 embryo. Fans out 5 strategist lenses over current GTM state, dedups, returns ranked proposals; flags which touch the guardrail layer (those stay one-tap approvals). Registered and invocable (`enableWorkflows: true` already set). UNTESTED until first invocation. Run with the `ultracode` keyword or the Workflow tool.

**Hook** (`~/.claude/settings.json`, PostToolUse on Write|Edit): auto-appends every edit to a skill / agent / workflow / CLAUDE.md to `coordinator/logs/instruction-changelog.md` (UTC-timestamp, action, path). This is the "how the motion got smarter" audit trail. Pipe-tested, jq-validated, and PROVEN firing live in-session (no restart needed). Manage/disable via `/hooks`.

**Reload behavior (verified live Jul 18):** skills, workflows, and hooks HOT-LOAD mid-session (gtm-daily-rundown, gtm-proposal-sweep, and the PostToolUse hook all worked without restart). Custom SUBAGENTS in ~/.claude/agents do NOT — `clay-operator` returned "agent type not found" the same session it was created. To use new subagents, restart the session (reopen the Claude Code panel in the VS Code extension, or run `claude` fresh). Not blocking; use general-purpose until restart.

**Not activated (nothing to turn on):** MCP servers (Otter/Gmail/Drive already connected, used on demand). Underused, worth reaching for: Otter transcripts → intradiem-roi-business-case.

Ties into [[gtm-daily-rundown-jul18]] (phase 1) and [[vscode-copilot-vs-claude-code]] (keep it one harness).
