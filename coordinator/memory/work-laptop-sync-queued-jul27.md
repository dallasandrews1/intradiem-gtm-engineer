---
name: work-laptop-sync-queued-jul27
description: Dallas is pasting the 3 graph-engineering build prompts on this machine now; everything built/upgraded needs to transfer to the work MacBook (IntradiemDA) + Enterprise Claude Code account right after
metadata:
  type: project
---

2026-07-27: Dallas started pasting the 3 copy-paste prompts from [[graph-engineering-audit-jul27]] (model tiering retrofit across the 3 `.claude/workflows/*.js` scripts, new `gate-integrity-fanout.js` workflow, WFM-Adjacency Clay Workflow fan-out race fix) to build them on this (personal) machine.

**Explicit standing instruction: right after this build session, transfer everything accomplished/built/upgraded over to the work laptop and Enterprise Claude Code account.** That means the new/changed workflow scripts, any new agent files, `AGENT_REGISTRY.md` updates, and the new memory files from this session, not just the Clay-side changes (those are already live in Clay's cloud and don't need a file transfer, only the local coordinator/repo files do).

**Why:** the work Mac (IntradiemDA, Enterprise Cowork) is a separate physical filesystem from this personal Mac; nothing placed in `~/coordinator` or the Intradiem GTM Engineer repo here appears there automatically. See [[work-machine-operational-jul20]] (work Mac mirrors personal Mac as of Jul 20) and [[work-machine-transfer-gotchas.md|work-machine-transfer-gotchas]] for the two known traps: place `~/coordinator` FIRST on the work Mac before anything else or skills/CLAUDE.md/rewrites silently no-op, and every path needs a `/Users/dallasandrews` to `/Users/IntradiemDA` rewrite pass (see [[work-macbook-username-intradiemda]]).

**How to apply:** once the 3 builds land and are verified on this machine, proactively remind Dallas to run the transfer rather than waiting for him to ask, and hand him the exact file list (new/changed paths) so the transfer isn't a guess.
