---
name: two-machine-sync-loop-aug31
description: "Aug 31 2026: the personal Mac and the work Mac (IntradiemDA) sync through the private GitHub repo automatically: sync_publish.sh runs on every SessionEnd here (throttled) and nightly 21:30, exporting the coordinator, committing coordinator/, pushing main, and logging uncommitted work for the rundown; sync_work_mac.sh start/end hooks on the work Mac pull+install and sweep memory back, commit, push; Dallas never has to remember to sync"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1164f90f-c0cb-4597-b831-24abf3f2ed45
  modified: 2026-09-01T04:06:37.066Z
---

Built Aug 31 2026 after the work Mac turned out to hold six weeks of unsynced files (recovered into main at 34d3957).

**Personal Mac (builder and scheduler):** `automation/sync_publish.sh` (pure bash, no Claude call). Wired as a `SessionEnd` hook in `~/.claude/settings.json` (async, 180s timeout, `--hook`) and as launchd `com.dallasandrews.gtm.syncpublish` daily 21:30 (`--force`). Steps: `coordinator/sync.sh export`; commit `coordinator/` only when more than manifest.json changed (manifest-only changes are reverted, so no noise commits); fetch; ff-pull if only behind; rebase only if ahead AND the tree is clean, else log DIVERGED and stop; push; then list uncommitted and unpushed work for the main checkout and every worktree into `automation/logs/sync-publish-<date>.md` with `evt: sync-publish-<date>#unpushed-work`. Never `git add -A` on the repo, never force, never resolves conflicts, throttled to once per 10 minutes, exit 0 always. Rundown reads it as source 13 ("Unpushed work" line under blockers).

**Work Mac (operator):** `automation/sync_work_mac.sh start|end`, added to that machine's `~/.claude/settings.json` as SessionStart and SessionEnd hooks (JSON in `coordinator/BOOTSTRAP_WORK_LAPTOP.md` step 3b; settings.json is not synced, so it is a one-time hand edit there). `start`: fetch, `pull --ff-only`, `sync.sh install` when behind. `end`: `sync.sh export-memory` (new reverse lane: copies memory files newer than the snapshot into `coordinator/memory` with `/Users/intradiemDA` rewritten back to `/Users/dallasandrews`, merges the index), `git add -A` guarded at 300 files, commit "Work Mac session <date>", rebase or ff, push. The work Mac never runs `sync.sh export` (it would snapshot rewritten paths and its work-only skills over the personal Mac's) and never loads launchd.

**Gotcha learned the same night:** `sync.sh export` copies `~/coordinator/AGENT_REGISTRY.md` over `coordinator/AGENT_REGISTRY.md`. The canonical registry is the `~/coordinator` copy; editing the repo copy gets overwritten on the next export (it dropped the pmoextractor rows once). Always edit `~/coordinator/AGENT_REGISTRY.md`.

**Why:** Dallas: "I just don't want to forget." The loop removes the manual export-commit-push and pull-install steps entirely; the only human moments are a DIVERGED line in the log or a "needs a human" line, which the rundown surfaces.

**How to apply:** when a session ends here, expect a coordinator commit if memory or skills changed. To publish immediately: `bash automation/sync_publish.sh --force`. Related: [[repo-committed-coordinator-package-aug26]], [[context-bus-cross-laptop-aug6]], [[work-machine-operational-jul20]], [[product-ai-goals-build-aug31]].
