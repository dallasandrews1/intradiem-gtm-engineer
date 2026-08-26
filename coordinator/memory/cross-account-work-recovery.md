---
name: cross-account-work-recovery
description: How to recover/transfer in-progress work when the Enterprise Claude account runs out of usage mid-session (Clay work, Cowork conversation, code session)
metadata:
  type: reference
---

When the Intradiem Enterprise Claude account runs out of usage mid-work, nothing is lost — it's a transfer problem, not a recovery problem. The work lives in three places, each moved differently:

1. **Clay work (Cowork Chrome-extension edits)** — saved in Clay's CLOUD, tied to the Clay workspace login, NOT the Claude account. Claude usage running out can't touch it. Reopen Clay from personal Cowork (same Clay login), verify the table state on the page. Nothing to transfer.
2. **Cowork conversation** — copy/paste the prompts+answers over (or screenshot). This carries the DECISIONS/context, not the work itself. Note: Mem0 is OFF on Enterprise (compliance flag [[mem0-enterprise-compliance-flag-jul17]]), so a Cowork strategy session never auto-syncs anywhere — that's why it feels trapped.
3. **Claude Code session** — the real output is the FILES it wrote to disk (usage exhaustion deletes nothing), AND the full conversation is saved as a single `.jsonl` transcript that embeds every prompt, answer, and file the session wrote. To move it: on the machine that ran out (work Mac = `/Users/IntradiemDA`), copy the newest transcript to the Desktop then AirDrop it:
   `cp "$(ls -t ~/.claude/projects/*/*.jsonl | head -1)" ~/Desktop/code-session.jsonl`
   Then read that one file to reconstruct the whole session on the personal Mac.

Gotchas: `~/.claude` is a hidden folder (Finder won't show it — copy to Desktop first to AirDrop). macOS built-in `find` does NOT support `-printf` (Linux-only); use `ls -lt ~/.claude/projects/*/*.jsonl` instead. Work Mac has swarm plists unloaded, so its newest `.jsonl` is genuinely the interactive session, not a scheduled job. Path rewrite `/Users/IntradiemDA` → `/Users/dallasandrews` when moving files. See [[work-machine-transfer-gotchas]] and [[vscode-work-macbook-account-split]].
