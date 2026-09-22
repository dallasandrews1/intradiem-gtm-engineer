---
name: mem0-search-quota-exhausted-sep22
description: Mem0 plugin search quota hit 1000/1000 on Sep 22 2026 and resets Oct 1 2026; every search_memories call errors until then
metadata:
  type: reference
---

On Sep 22 2026 both mem0 search calls returned "Usage quota exceeded for this billing period" (quota_limit 1000, quota_used 1000, quota_reset 2026-10-01). File-based memory in this folder is the durable source of truth per CLAUDE.md, so nothing was lost.

**How to apply:** until Oct 1 2026 skip the mem0 searches the hook asks for and read `MEMORY.md` plus the relevant memory files instead; do not retry the calls. Re-check on the first session in October.
