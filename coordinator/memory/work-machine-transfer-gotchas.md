---
name: work-machine-transfer-gotchas
description: Lessons from the Jul 20 work-Mac (IntradiemDA) transfer — the two traps that cost the most time and how to avoid them next time.
metadata:
  type: feedback
---

Jul 20 2026: completed the coordinator + engine-repo transfer to the work MacBook (IntradiemDA). Two traps ate significant time; encode them into any future transfer runbook.

**Trap 1 — placing the coordinator folder is the load-bearing step, and it's easy to skip.** Skills, the global CLAUDE.md, and the memory index all derive from `~/coordinator`. If the coordinator folder isn't moved into `~/coordinator` first, the skills mirror and CLAUDE.md copy silently produce nothing (skills=0, CLAUDE.md missing) and the path-rewrite skips coordinator because it isn't there yet. **Order: place `~/coordinator` FIRST, then wire globals, then rewrite, then verify.** The verify command must check `~/coordinator/memory/MEMORY.md` and `skills dirs > 0` explicitly, or a skipped coordinator goes unnoticed.

**Trap 2 — `unzip` prompts, and pasting a multi-line block feeds the next commands into its prompt.** `unzip file.zip` asks `replace...? [y]es,[n]o,[A]ll,[N]one,[r]ename` when files exist; if you paste the placement `cp` lines with it, they become "invalid response" answers and nothing runs. **Fix: always use `unzip -oq file.zip` (overwrites silently) and run it on its OWN line, then paste the rest.** When any terminal command gets stuck at a prompt or a `>` continuation line, **Control-C** clears the whole queued buffer; use it before re-running.

**Also:** hand Dallas commands as single physical lines (semicolons, no trailing `\` line-continuation). Backslash-continued multi-line pastes leave the shell hanging at a `>` prompt. macOS filesystem is case-insensitive, so `IntradiemDA` vs `intradiemDA` resolved fine. Related: [[work-macbook-username-intradiemda]], [[memory-store-consolidation-jul20]].
