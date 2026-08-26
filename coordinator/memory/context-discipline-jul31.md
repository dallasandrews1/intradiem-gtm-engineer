---
name: context-discipline-jul31
description: Full-page render reads and a bloated memory index were blowing the context window and making sessions unresumable ("Prompt is too long")
metadata:
  type: feedback
---

Jul 31 2026: Dallas hit "Prompt is too long" on every session resume and could not work. Diagnosed three stacked causes.

1. **Full-page render reads are the killer.** Design and deck sessions render a PNG and Read it back to check layout. `brief_centene.png` was 1280x10400, roughly 17,750 tokens for one read. Session `e1c6317f` ran 28 Reads totaling 3.82 MB, mostly PNG iterations. Ten render-check loops make a session unrecoverable.
2. **Resuming dead sessions.** Coordinator held 174 MB of transcripts, six over 5 MB (largest 21 MB). `--continue` lands on the newest, has to rebuild the whole transcript, and fails before compaction can run. Fix applied: transcripts over 5 MB moved to `~/.claude/session-archive/` so the resume picker cannot reach them. Nothing deleted.
3. **MEMORY.md had stopped being an index.** 50 KB, 156 lines, 143 of them over 200 characters carrying full paragraphs instead of hooks. Injected at every session start plus Read 27 more times. Rewritten to one-line hooks, backup at `memory/MEMORY.md.bak-jul31`.

**Why:** context is a hard ceiling, not a soft cost. A single oversized image read is worth more tokens than the entire instruction set, and once a transcript passes the window there is no recovery path from inside the session.

**How to apply:**
- Never Read a full-page render of a long document. Downscale first (`sips -Z 1000 in.png --out small.png`) or crop to the region in question.
- Prefer reading the HTML or markdown source over a screenshot of it. Only screenshot when the question is genuinely visual (spacing, color, layout).
- Cap any render check at roughly 1000px on the long edge unless legibility of small text is the point.
- One render check per iteration, not a gallery. Delete scratchpad PNGs once the check passes.
- Keep MEMORY.md to one line per memory. Content goes in the memory file, never in the index.
- Start fresh sessions between unrelated tasks rather than continuing one long thread. See [[usage-optimization-config-jul24]].
- If a session is already too long to resume, pull what you need straight from the `.jsonl` in `~/.claude/session-archive/` instead of trying to load it. See [[cross-account-work-recovery]].
