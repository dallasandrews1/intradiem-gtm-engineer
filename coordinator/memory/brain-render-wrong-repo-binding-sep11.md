---
name: brain-render-wrong-repo-binding-sep11
description: "Sep 11 2026 root cause, Render service intradiem-gtm-system deploys main of a DIFFERENT GitHub repo (dallasandrews1/intradiem-gtm-system, one Jun 13 commit 1b7b9c7 with unpinned mcp>=1.12), not intradiem-gtm-engineer; branch is already main and auto-deploy is on, so the fix is a repo re-bind in the Render dashboard, which the Render MCP connector cannot do"
metadata:
  type: project
---

Found Sep 11 2026 19:20Z via the Render MCP connector (workspace tea-d8mpusho3t8c73c45svg, service srv-d8mqfdmrnols73cvcck0).

- Service settings: repo `https://github.com/dallasandrews1/intradiem-gtm-system`, branch `main`, autoDeploy yes (trigger: commit), Docker runtime, dockerfilePath `gtm-hosted-platform/brain/Dockerfile`, context `.`, rootDir empty, health check `/healthz`, free plan, Oregon.
- That repo's `main` has exactly one commit, 1b7b9c7 "Add mcp to requirements" (Jun 13 2026). Every deploy in the service's history built that commit. The brief's "bound to an agents/* branch" theory was wrong; the branch was never the problem, the repo is.
- The correct code (614fa36 and later, mcp<2 pin, Slack auth door, host pinning off, version 2.1) lives on `main` of `dallasandrews1/intradiem-gtm-engineer`. Auto-deploy is on but watches the wrong repo, which is why pushes to intradiem-gtm-engineer never built.
- Both rebuilds of 1b7b9c7 on Sep 11 (16:24Z manual, 19:20Z after the GTM_STATE_URL save) resolved `mcp>=1.12` to mcp 2.2.0 and crashed at `from mcp.server.fastmcp import FastMCP`. Render kept the Jul 17 deploy (dep-d9cvitt8nd3s73cakteg) live; healthz still `{"ok":true,"service":"intradiem-gtm-brain"}`.
- GTM_STATE_URL set to `https://gtm-brain-state.pages.dev/gtm_state.json` via the connector Sep 11 19:20Z (merge write). The connector has no env-var READ tool, so GTM_API_KEYS and SLACK_SIGNING_SECRET presence is unverified from here.
- The Render MCP connector cannot change a service's repo or branch (only env vars, deploys, logs). Re-binding is a Render dashboard step: Settings > Build & Deploy > Repository. The Render GitHub app must be granted access to the private intradiem-gtm-engineer repo first.

- RESOLVED Sep 11 2026 19:43Z: Dallas re-bound the repo in the dashboard; Render auto-built main 4ac3706 with mcp 1.30.0 and reported live; healthz shows version 2.1 and the unsigned /mcp/ probe returns 401. Follow-on snapshot 403 in [[brain-snapshot-fetch-403-urllib-ua-sep11]].

**Why:** two repos with near-identical names; the Jun 13 interview-era repo got wired to Render and the Aug 26 private repo never was.
**How to apply:** re-bind the repo in the dashboard (branch main, Dockerfile path and root dir unchanged), which triggers a build of intradiem-gtm-engineer main; then verify healthz version 2.1 and the unsigned /mcp/ 401 probe, then the keyed tools/list. See [[brain-render-deploy-prereqs-sep11]], [[brain-mcp-421-host-pinning-sep11]].
