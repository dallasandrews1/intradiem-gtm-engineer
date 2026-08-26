---
name: surface-split-rule
description: "Repo/file work can run in Cowork or VS Code, but whichever surface does it must sync memory the same day. Clay UI work is browser work, no Claude surface clicks it natively."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cowork-jul10-2026
---

Repo/file work can run in either Cowork or VS Code, but whichever surface does it must sync memory the same day (the Jul 10 2026 memory-sync session, this one, is that sync in action). Clay UI work (purge, wires, sync runs, campaign settings) is browser work; no Claude surface clicks it natively, options are Dallas clicking from a runbook or Claude driving Chrome via the extension.

**Why:** Dallas works across multiple Claude surfaces (Cowork, VS Code with Mem0, Claude-in-Chrome). Without a same-day sync discipline, work done in one surface becomes invisible to sessions running in another, exactly the gap this session's step 1 verification caught (Mem0 had zero real project memories despite weeks of work happening in other surfaces).

**How to apply:** After any substantive repo/file work in Cowork or VS Code, sync the memory/*.md files into Mem0 before the session ends (or early in the next session touching that surface). For Clay UI changes, log the change in the relevant project memory file (e.g. [[contacts-table-finalized-jul9]], [[clay-tables-not-live-yet]]) since no surface can natively verify Clay's current UI state except by re-checking it live. Ties to [[three-surface-sync]] (the analogous rule for the three HTML surfaces) and [[jason-ai-enablement-jul9]] (the VS Code + Mem0 pattern this rule protects).
