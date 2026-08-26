---
name: vscode-work-macbook-account-split
description: "Work MacBook VS Code setup: personal account for editor Settings Sync, separate Intradiem Claude Enterprise account for Claude Code auth — two different logins, not one"
metadata:
  type: project
---

Dallas is setting up VS Code on his Intradiem-issued work MacBook. Two logins are involved and they don't have to (and shouldn't) match:

1. **VS Code Settings Sync** (GitHub/Microsoft account) — controls editor UI, extensions, keybindings, snippets. Use the same personal account as his other machines so the editor experience carries over.
2. **Claude Code authentication** (Anthropic/Claude account) — Dallas already holds a separate Claude Enterprise account provisioned by Intradiem. Claude Code on the work MacBook logs in with that Enterprise account, not his personal one. This is the correct split for compliance/billing, not a workaround.

**Why:** personal usage stays on personal auth, work usage stays on the org's paid Enterprise seat. Settings Sync and Claude Code auth are independent systems in VS Code, so splitting them causes no technical conflict.

**How to apply / open threads:**
- `~/coordinator` (memory files, CLAUDE.md, skills — see [[vscode-coordinator-setup]]) does not travel with either account login. It's tied to the filesystem location, not to which Claude account is authenticated, so it still has to be physically copied to the work MacBook (AirDrop/git/etc.) regardless of this account split.
- Skill files under `.claude/skills/` are plain files and work under either account once the folder is copied over.
- Open question, not yet confirmed: whether the Intradiem Enterprise account provisions its own separate Mem0/memory backend, which would affect whether file-based memory in `~/coordinator` stays the single cross-machine source of truth. Ask Jason Dowden (AI Enablement) — see [[jason-ai-enablement-jul9]].
- **Jul 17 update:** Mem0 itself may not belong on the Enterprise account at all — Jason Jones flagged it as third-party-cloud in #ai the same day, with a local alternative (Total-Recall) not yet officially sanctioned. Don't enable Mem0 on the work MacBook until cleared. Full detail in [[mem0-enterprise-compliance-flag-jul17]].
