---
name: cloudflare-mcp-oauth-needs-interactive
description: Cloudflare plugin is installed; the four auth servers only authorize in an interactive Claude session
metadata: 
  node_type: memory
  type: reference
  originSessionId: 763cd25f-8518-4f97-902c-aef2e72804fb
  modified: 2026-08-06T20:34:17.790Z
---

Dallas has the Cloudflare setup done: marketplace `cloudflare` (github cloudflare/skills) and plugin `cloudflare@cloudflare` v1.0.0, user scope, enabled. All five MCP servers are registered in `~/.claude/plugins/cache/cloudflare/cloudflare/1.0.0/.mcp.json` — `cloudflare-api`, `-docs`, `-bindings`, `-builds`, `-observability`.

Only `cloudflare-docs` works without auth. The other four authorize through a browser OAuth flow that "triggers automatically on first Cloudflare tool use," so a **non-interactive session can never complete it** and will see them as unavailable. This is not a broken setup and re-running the install does not fix it.

**How to apply:** In a non-interactive session, don't claim the setup is missing and don't reinstall. Say the handshake needs an interactive session, and hand over the paste-back prompt plus the dashboard fallback. There is no wrangler CLI and no `CLOUDFLARE_API_TOKEN` on this machine, so the CLI path needs installing first. Deploy convention is one folder per Pages project with `index.html`, a branded `404.html`, and a `_headers` file carrying noindex. See [[deliverables-folder-convention]].
