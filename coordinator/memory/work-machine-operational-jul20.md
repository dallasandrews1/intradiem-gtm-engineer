---
name: work-machine-operational-jul20
description: Jul 20 2026 — the work MacBook (IntradiemDA, Enterprise Cowork) is fully set up and mirrors the personal Mac; Clay live on the Enterprise workspace.
metadata:
  type: project
---

On 2026-07-20 the work MacBook (username IntradiemDA, Intradiem Claude Enterprise account) was brought to full parity with the personal Mac via AirDrop transfer:

- `~/coordinator` placed (memory 116 entries, master CLAUDE.md, 20 skills), globals wired to `~/.claude/` (CLAUDE.md + skills mirror), 13 agents in `~/.claude/agents/`.
- Engine repo `~/Claude/Projects/Intradiem GTM Engineer` and `~/Claude/Projects/Clay Builds and Strategy` placed and accessible (also granted via settings additionalDirectories).
- All hardcoded `/Users/dallasandrews` paths rewritten to `/Users/IntradiemDA`.
- Clay plugin installed, `clay login` to the ENTERPRISE workspace confirmed (`clay workflows list` returns; 7 custom gates visible: fn_eligible, fn_tokens_ready, fn_draft_critic, fn_draft_clean, fn_email_verified, fn_persona_key, fn_send_ready).
- Green-light passed: coordinator session reads MEMORY.md, lists skills, sees the engine repo.

Standing posture on the work machine: Mem0 stays OFF (compliance hold, plugin disabled in settings); other MCP connectors (Otter/Gmail/Drive/Slack) await IT approval; the scheduled swarm `.plist` jobs are NOT loaded there (personal Mac remains the scheduler to avoid double morning DMs). Clay UI automation is now driven from the work-machine session. Related: [[work-macbook-username-intradiemda]], [[work-machine-transfer-gotchas]], [[mem0-enterprise-compliance-flag-jul17]].
