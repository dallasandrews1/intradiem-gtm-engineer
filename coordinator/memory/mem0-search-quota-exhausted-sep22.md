---
name: mem0-search-quota-exhausted-sep22
description: "Mem0 search_memories hit its 1000-call billing-period quota on Sep 22 2026, resets Oct 1 2026 — search calls error until then"
metadata: 
  node_type: memory
  type: project
  originSessionId: 42e015cc-90ae-4b94-8c5c-f09e870995f6
  modified: 2026-09-22T07:14:06.005Z
---

As of 2026-09-22 (first observed ~07:12 UTC during a scheduled lemlist-relay run), `search_memories` on both `mcp__claude_ai_Mem0__search_memories` and `mcp__plugin_mem0_mem0__search_memories` returns a quota-exceeded error: `quota_limit: 1000, quota_used: 1000, quota_reset: 2026-10-01T00:00:00+00:00`.

**Why:** the account's monthly search quota (1000 calls) was used up before the billing period reset.

**How to apply:** any session or scheduled job that tries `search_memories` this month should expect it to fail and not treat that as a blocker — fall back to the file-based coordinator memory (`~/.claude/projects/.../memory/*.md` + `MEMORY.md`), which is the durable source of truth per the global CLAUDE.md anyway. `add_memory` uses a separate ADD quota and was not observed to be exhausted — writes may still work. Don't burn time retrying search_memories or treating the error as something to fix; just proceed without it until 2026-10-01.
