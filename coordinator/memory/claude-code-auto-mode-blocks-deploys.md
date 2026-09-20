---
name: claude-code-auto-mode-blocks-deploys
description: "Sep 20 2026: in auto permission mode the Claude Code classifier denies `wrangler pages deploy` as a Production Deploy even after Dallas delegates it; earlier sessions deployed under a different mode. Hand him automation/deploy_rep_pages.sh or get a Bash permission rule first."
metadata:
  type: reference
---

**What happened:** Sep 20 2026 evening, VS Code session in auto mode. Dallas delegated the open decisions, the first `npx wrangler pages deploy ... --force` was denied by the permission classifier with reason "Production Deploy", and so was a read-only link check run straight after it. Sessions earlier the same day deployed the same projects with the same command shape, so this is the session's permission mode, not the command.

**How to apply:**
- Never work around the denial. Say plainly that the harness blocked it, and that nothing was deployed.
- Two clean paths: Dallas runs `automation/deploy_rep_pages.sh maps`, then `rooms`, then `plans` (fail-closed, carries every standing deploy rule), or he adds a Bash permission rule for `npx wrangler pages deploy` (or changes mode) and then says deploy. Only edit permission settings on his explicit ask.
- Check at the START of a deploy-bearing thread whether deploys are permitted, so he is not told at the end.
- Be exact about what THIS session did versus earlier ones; he reasonably reads "Claude" as one continuous worker.

Related: [[wrangler-pages-force-delegation-trap]], [[shared-links-gate-sep20]].
