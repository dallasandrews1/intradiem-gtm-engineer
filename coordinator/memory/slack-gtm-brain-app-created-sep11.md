---
name: slack-gtm-brain-app-created-sep11
description: "Sep 11 2026, the \"Intradiem GTM Brain\" Slack app exists in the Intradiem workspace (created from slackbot_mcp_manifest.json, scope mcp:connect, MCP Servers page present); workspace app install is admin-approval gated (button reads Request to Workspace Install), not yet requested"
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
