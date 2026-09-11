---
name: slack-gtm-brain-app-created-sep11
description: "Sep 11 2026, the \"Intradiem GTM Brain\" Slack app exists in the Intradiem workspace (created from slackbot_mcp_manifest.json, scope mcp:connect, MCP Servers page present); workspace app install is admin-approval gated (button reads Request to Workspace Install), gate verified clear Sep 11 ~20:10Z, Dallas cleared to request"
metadata: 
  node_type: memory
  type: project
  originSessionId: 70ef698f-e87f-4dc7-8724-5e09a9fddce5
  modified: 2026-09-11T15:50:16.199Z
---

Dallas created the Slack app "Intradiem GTM Brain" on Sep 11 2026 from `gtm-hosted-platform/slack/slackbot_mcp_manifest.json`. Confirmed from his screen:

- OAuth & Permissions shows one bot scope, `mcp:connect`, described as connecting to MCP servers at intradiem-gtm-system.onrender.com, so the `mcp_servers` manifest block was accepted.
- Sidebar has an "MCP Servers" page (labelled New) under Features.
- The install control reads **Request to Workspace Install**: app approval is on for the Intradiem workspace and an admin must approve. Not clicked as of Sep 11. Ordering rule from the deploy sheet: request install only after the brain with the Slack auth door and the 421 host fix is live ([[brain-mcp-421-host-pinning-sep11]]).
- Signing Secret lives under Basic Information, App Credentials. Goes to Render as `SLACK_SIGNING_SECRET`, never into chat or the repo.

**Why:** the admin gate adds a wait; whoever approves apps should be identified before the request goes out.
**How to apply:** after the deploy passes the keyed tools/list check, Dallas clicks Request to Workspace Install; confirmation of the Slackbot connection comes from the MCP Servers page or a first plain-language ask in Slackbot. See [[slack-surfaces-workflows-findings-sep10]].

**Update Sep 11 2026 ~20:10Z:** install gate verified live (healthz version 2.1 source url, snapshot 200, /mcp/ 401 unauthenticated, keyed tools/list passed earlier). Dallas told he is clear to click Request to Workspace Install. Still untested on Render: the real Slack signature pass (only exercised after install). Snapshot correction: republished 20:12Z with the 16-account sourced universe (0 seed), so first answers carry real scores; signals engine still 6 seed accounts.

**Update Sep 11 2026 evening:** Dallas SUBMITTED the Request to Workspace Install with a two-paragraph note that says the service runs on his own Render account. Awaiting admin approval. Public Distribution and OAuth Redirect URLs (Manage Distribution page) are deliberately left untouched: single-workspace app, never distribute publicly.

**Open gaps as of Sep 11 evening:** (1) admin approval; (2) Slack signature pass unexercised on Render until the first Slackbot ask, verify via request log actor slackbot; (3) snapshot freshness: nightly sync_publish only STAGES, brain withholds past 36h, so the 20:12Z publish goes stale Sunday Sep 13 morning unless --deploy is wired into the nightly (offered, Dallas's call, outward-facing); (4) signal engine data still the 6-account seed. Parked from Sep 10: Workflow Builder form-to-channel rep intake, Surfaces beyond the step 7 test.
