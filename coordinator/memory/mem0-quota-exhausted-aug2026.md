---
name: mem0-quota-exhausted-aug2026
description: "Mem0 cloud search/add quota exhausted again on 2026-09-02 (1000/1000, resets 2026-10-01); file memory is the only working store this month"
metadata:
  type: project
---

Mem0 (`user_id=dallasandrews`) returned "Usage quota exceeded for this billing period" on `search_memories` on 2026-08-06 (reset 2026-09-01) and AGAIN on 2026-09-02, one day into the new period (quota_limit 1000, quota_used 1000, next reset 2026-10-01T00:00:00Z). The Sep 1 reset was consumed within a day, most likely by the automatic hook sync and the nightly safety-net job.

**Why:** billing-period cap, not auth. Retrying will not help until the reset, and the burn rate means the cap will hit early every month unless the plan changes or the automatic sync is throttled.

**How to apply:** proceed on file-based memory only (`memory/*.md` + `MEMORY.md`) and treat Mem0 search/add failures as expected, not errors. Worth raising with Dallas once: either upgrade the plan or turn the hook to manual adds so the 1,000 calls last the month.
