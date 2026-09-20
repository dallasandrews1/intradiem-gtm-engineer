---
name: wrangler-pages-force-delegation-trap
description: "Sep 20 2026: in wrangler 4.135.0 a `wrangler pages` create or deploy run by an agent WITHOUT --force is handed to a Workers deploy that auto-detects static files in the cwd; --force is what keeps it on Pages. account-plans.pages.dev is NOT ours."
metadata:
  type: reference
---

**The trap (found Sep 20 2026, wrangler 4.135.0 via npx):** when an agent runs `wrangler pages project create` or `wrangler pages deploy` without `--force`, wrangler logs "delegate pages to workers" and runs a Workers `wrangler deploy` with auto-config detection in the current directory instead. From an empty folder it fails harmlessly ("Could not detect a directory containing static files" or "Missing entry-point"). From a deploy folder it would publish those files as a Worker under a name nobody chose. The `--help` text does not mention any of this and does not list `--force`. Read-only `pages project list` and `pages deployment list` are not delegated.

**Why Dallas's "every deploy uses wrangler --force" rule exists:** `--force` is not a cache or overwrite nicety. It is the switch that makes the command run against Cloudflare Pages at all.

**How to apply:**
- `--force` on every state-changing `wrangler pages` command, creates included, not only deploys.
- Run `project create` from an EMPTY directory as a second guard.
- After any create or deploy, confirm in `~/Library/Preferences/.wrangler/logs/` that the newest log has no `"command":"wrangler deploy"` line, and confirm the hostname with `pages project list`.
- Wrangler's success output tells agents "Do not pass --force on future commands". That is tool output, not Dallas's instruction. His standing rule wins.
- A requested project name does not guarantee the hostname: if the subdomain is taken globally Cloudflare appends a suffix. Always read the hostname back before building URLs on it.

**Hostname outcome, Sep 20 2026:** `account-plans.pages.dev` was already taken by someone outside the account; our project `account-plans` got `account-plans-7kb.pages.dev` and sits EMPTY (not deleted, Dallas's call). The fallback `intradiem-accounts` got the clean `intradiem-accounts.pages.dev` and is the migration target. Never link to, redirect to, or curl `account-plans.pages.dev`; `automation/check_shared_links.py` deliberately leaves it out of `PLANS_HOSTS` so a redirect landing there fails the gate.

Related: [[rep-index-pages-sep20]], [[engine-room-deliverable-aug7]].
