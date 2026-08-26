---
name: memory-store-consolidation-jul20
description: Memory was split across two dirs; recent writes landed outside the coordinator folder. Consolidated Jul 20 2026 into coordinator/memory/ so one airdrop carries everything.
metadata:
  type: project
---

On 2026-07-20, a freshness check before airdropping the coordinator folder to Dallas's work MacBook found the file-based memory was split across TWO directories:

1. `~/coordinator/memory/` — the durable store per CLAUDE.md, travels with an airdrop of `~/coordinator`. Holds MEMORY.md (the index).
2. `~/.claude/projects/-Users-dallasandrews-coordinator/memory/` — the harness-injected memory path. The SessionStart memory prompt points here, so recent session writes (11 files, including the freshest Jul 20 work: voicefix-two-pass, stars-live-table-dollar-wiring, invoke-workflow-trigger-inputschema, and several feedback rules) were landing OUTSIDE the coordinator folder and would NOT travel with an airdrop.

Fix applied: copied all 11 external files into `~/coordinator/memory/`, repointed the 6 external-path index links to local filenames, and added index pointers for 13 previously-unindexed files (the 5 newly-copied + 8 pre-existing local orphans). Result: 111 files, every one indexed, every pointer resolves inside the folder. One airdrop of `~/coordinator` now carries the complete memory store.

**How to apply:** Write file-based memory to `~/coordinator/memory/` (the durable store), NOT the harness `~/.claude/projects/.../memory/` path, even when the SessionStart prompt names the latter. Files in `~/coordinator/memory/` win. If a session writes to the external path, sweep it back into `~/coordinator/memory/` before any airdrop or handoff. Related: [[feedback_surface-split-rule]], [[mem0-sync-gap-jul17]].
