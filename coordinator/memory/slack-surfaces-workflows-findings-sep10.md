---
name: slack-surfaces-workflows-findings-sep10
description: "Sep 10 2026 verified read on Slack Workflow Builder, Surfaces, and the Slackbot MCP client against Dallas's existing Slack surfaces; what fits, what does not, and the one build that unlocks Slackbot reading the brain"
metadata: 
  node_type: memory
  type: project
  originSessionId: 70ef698f-e87f-4dc7-8724-5e09a9fddce5
  modified: 2026-09-10T20:35:39.801Z
---

Sep 10 2026, Dallas asked whether Slack custom workflows and dashboards are worth using. Intradiem's Slack plan has Workflow Builder webhooks and Slackbot Surfaces. Verified findings:

- Surfaces (Slackbot dashboards/reports) are STATIC snapshots. Slack help: "Surfaces are static files and don't currently pull in new data." Data sources are Slack content plus connected sources (MCP servers, enterprise search). Can be shared anywhere and added as a tab. Not a live dashboard; never a system of record.
- Workflow Builder has NO native outbound web-request step. Webhook triggers are inbound only (POST to hooks.slack.com starts a workflow; up to 20 flat variables: channel ID, user ID, user email, text; no nested JSON). Third-party "Workflow Buddy" adds outbound steps and would need admin app install.
- Slackbot MCP client needs a Streamable HTTP HTTPS endpoint, tools answer within 60 s, max 5 active servers per user, app manifest with `mcp:connect` scope and an `mcp_servers` block. Auth modes: none, `slack_identity_auth` (identity in `params._meta.slack`, verified via `X-Slack-Signature` + signing secret), DCR OAuth, manual OAuth. A static X-API-Key header is NOT supported.
- The brain on Render already serves MCP over Streamable HTTP at /mcp/ (FastMCP, stateless) behind KeyAuthMiddleware. Probe Sep 10: healthz 200, POST /mcp/ with no key returns 401. So Slackbot cannot connect today; the unlock is adding Slack-signature verification as an alternate pass in KeyAuthMiddleware plus a Slack app manifest with the mcp_servers block.
- UPDATE Sep 11 2026: the Slack identity auth door is BUILT and tested (staged, not deployed), manifest at gtm-hosted-platform/slack/slackbot_mcp_manifest.json, deploy sheet on the Desktop; see [[brain-mcp-421-host-pinning-sep11]] for the production defect found on the way.
- Existing channel-driven intake already exists: the rundown thread listener (launchd rundownthreads, 10 min poll, CONFIRM loop) and the lemlist relay DONE/SKIP/HOLD thread replies read hourly. A Workflow Builder form posting a fixed-format message into a channel one of these pollers reads is the zero-build rep intake path.

**Why:** Dallas wants Slack to earn a place without becoming a second engine; the single-morning-brief rule and no-duplicate-state rule still govern.
**How to apply:** Slack = trigger and display only. Rep intake = form to channel to existing poller. Slackbot-on-the-brain = build the signature-auth pass first, then a Surface from `get_strike_plan`. Never promise a live Surface. See [[single-morning-brief-rule]] and [[strike-room-cowork-connector-gap-sep1]].
