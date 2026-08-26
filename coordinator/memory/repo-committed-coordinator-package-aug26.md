---
name: repo-committed-coordinator-package-aug26
description: Aug 26 2026, the engine repo's seven weeks of uncommitted work (566 files) was committed on main in seven groups, the worktree branch merged (tests 39/39), and a versioned coordinator/ folder (CLAUDE.md, 19 skills, 17 agents, 286 memory files, sync.sh) now ships with the repo; push staged, not run
metadata:
  type: project
---

On 2026-08-26 the main checkout of `~/Claude/Projects/Intradiem GTM Engineer` went from 30 modified plus 566 untracked files (everything since Jul 6) to a clean tree: seven grouped commits on `main` (gitignore, engines, automation swarm, skills and value repository, Clay build system, motions and strike rooms, leadership deliverables), then the `agents/vs-code-agents-window-usage` branch merged with `--no-ff` (triggers.json conflict resolved to the `coo_finance` persona key; TAM tests 39/39). Still no remote: the push is staged in `coordinator/BOOTSTRAP_WORK_LAPTOP.md` step 0 (option A private GitHub `dallasandrews1/intradiem-gtm-engineer` via `gh repo create`, option B Bitbucket) for Dallas to run.

Gitignore now excludes `automation/config/*.env` (LEMLIST_API_KEY), `.wrangler/`, `*.bak`, the stray `ziltSwKH` zip, the superseded `work-migration-pack/` (holds interview-era memory copies; relocate it out of the workspace), `*TAIS*`, and `linkedin-about*`. Wrappers were already clean: they read `$LEMLIST_API_KEY` from the env file, nothing inline.

`coordinator/` in the repo is a snapshot carrier: `sync.sh export` sweeps the harness memory stores (`~/.claude/projects/<slug>/memory`, which had drifted again to 61 + 34 + 5 files outside `~/coordinator/memory`) back into `~/coordinator/memory`, merges indexes via `merge_index.py`, snapshots skills (minus `dallas-brand`, `health-outcomes`), agents, workflows, memory (minus interview-status, TAIS profile, sustain, brazen), and refuses on any secret pattern. `sync.sh install` on the work Mac places everything, rewrites `/Users/dallasandrews` to the local home, and symlinks the harness memory dir to `~/coordinator/memory`.

**Why:** the work MacBook (IntradiemDA) only ever got a Jul 20 AirDrop plus context-bus memory deltas; the repo itself and the harness-path memory never travelled, and there was no git remote at all.

**How to apply:** before any push, run `coordinator/sync.sh export`, commit `coordinator/`, push. Treat the repo clone as the baseline and the context bus as the delta. First build on the work Mac is the Salesforce attribution loop (GTM Engineering Lead Source, three SF fields, reply-sync agent). Related: [[context-bus-cross-laptop-aug6]], [[memory-store-consolidation-jul20]], [[work-macbook-username-intradiemda]], [[pipeline-council-context-aug24]].
