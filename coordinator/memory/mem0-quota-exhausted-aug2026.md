---
name: mem0-quota-exhausted-aug2026
description: "Mem0 cloud search/add quota was exhausted as of 2026-08-06, resets 2026-09-01"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6b58d10c-ecdd-43b2-9e68-5ec0e4ceb3a2
  modified: 2026-08-06T12:05:03.200Z
---

Mem0 (`user_id=dallasandrews`, `app_id=coordinator`) returned "Usage quota exceeded for this billing period" on both `search_memories` calls on 2026-08-06 (quota_limit 1000, quota_used 1000, resets 2026-09-01T00:00:00Z).

**Why:** billing-period cap hit, not a config/auth problem — retrying or reconnecting won't help until reset.

**How to apply:** until 2026-09-01, sessions should proceed on file-based memory only (`memory/*.md` + `MEMORY.md`) without treating a Mem0 search/add failure as an error to fix — it's expected. File-based memory is the durable source of truth per CLAUDE.md anyway, so this is a degradation, not a blocker. Re-check after 2026-09-01 to confirm quota reset before relying on Mem0 again.
