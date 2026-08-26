---
name: mem0-sync-gap-jul17
description: "STANDING DIAGNOSIS: Mem0 auto-sync only fires in Claude Code/VS Code sessions (global plugin hook); Cowork has no local hook, only a manual MCP connector the model must proactively call — this is why Cowork work goes stale in Mem0"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 070cc632-174f-4c32-b9d7-50f80b21e0e6
---

Jul 17 2026 root-cause check (Dallas: "mem0 shit ain't keeping up with my changes in here and in cowork"): confirmed zero Mem0 memories of any kind were created between the Jul 10 backfill session (08:43am) and Jul 17, despite a full week of substantive work happening in the `Intradiem GTM Engineer` project via Cowork (L2 intent layer, back-office motion fork, Stars Wave 1 launch, Norton meeting, Cost Mandate builds, UK expansion, Motion Roadmap, Clay Golden Standard).

**Why:** The Mem0 plugin (`mem0@mem0-plugins`) is enabled globally in `~/.claude/settings.json`, so any Claude Code CLI/VS Code session — in ANY project directory — gets the SessionStart/Stop hooks automatically; no per-project enablement needed. Cowork (claude.ai's hosted product) is architecturally different: it has no local hooks.json mechanism at all. It only has the `mcp__claude_ai_Mem0__*` connector tools, which require the model to proactively call `add_memory` mid-session. If a Cowork session doesn't do that (or the connector isn't authorized that session), nothing lands in Mem0 no matter how much real work happens — this is NOT a bug to "fix" in the sense of enabling a hook; there is no hook to enable on Cowork's side.

**How to apply:** For any Cowork session working in a project without CLI-plugin-style auto-sync, the project's own CLAUDE.md must carry an explicit, standing instruction telling the model to call the Mem0 connector's `add_memory` proactively after material updates (decisions, builds, status changes), mirroring what the CLI plugin does automatically. Added this instruction to the `Intradiem GTM Engineer` project's CLAUDE.md on Jul 17 2026. Re-verify periodically (spot-check `get_memories` with `created_at >= <last known date>` for zero results) rather than assuming the instruction alone guarantees compliance — Cowork models can still skip it. Supersedes the "verify VS Code reads that scope" open question in [[mem0-shared-memory-live]]: the scope was never the issue, the absence of any hook mechanism in Cowork was. Ties to [[surface-split-rule]].
