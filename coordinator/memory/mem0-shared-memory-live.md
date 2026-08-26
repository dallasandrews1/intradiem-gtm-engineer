---
name: mem0-shared-memory-live
description: "Mem0 MCP connector connected in Cowork Jul 10 2026; standing rule to write material updates same-turn — see mem0-sync-gap-jul17 for why this didn't hold"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ae72b755-62cd-4b73-ad51-f7a044e93bc7
---

Mem0 MCP connector connected in Cowork Jul 10 2026, round-trip verified. STANDING RULE: write material updates to Mem0 (add_memory, infer=false, metadata name/type) in the same turn as any local memory write, unprompted — it's the shared ledger between Cowork and VS Code/CLI sessions.

**Why:** Dallas works across Cowork and VS Code; without same-turn writes, one surface's context goes stale relative to the other and he has to re-explain state.

**How to apply:** After any material change (decision, build, status shift) in a Cowork session, call add_memory alongside any local file write. Full backfill of the coordinator corpus done Jul 10 (~29 memories). **Update Jul 17 2026:** this rule did not hold for a full week (Jul 11-17) — see [[mem0-sync-gap-jul17]] for the actual mechanism (Cowork has no auto-hook, only a connector call the model must remember to make) and the fix applied (explicit CLAUDE.md instruction in the Intradiem GTM Engineer project). Ties to [[vscode-coordinator-setup]].
