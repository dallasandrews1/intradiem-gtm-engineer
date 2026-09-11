---
name: brain-mcp-421-host-pinning-sep11
description: "Sep 11 2026 finding, the live Render brain's /mcp almost certainly answers 421 Invalid Host header on every keyed call because FastMCP's default enables DNS-rebinding host pinning to localhost forms; fixed in app.py alongside the Slack identity auth door and the mcp<2 pin, staged not deployed"
metadata: 
  node_type: memory
  type: project
  originSessionId: 70ef698f-e87f-4dc7-8724-5e09a9fddce5
  modified: 2026-09-11T10:54:57.761Z
---

Found Sep 11 2026 while smoke-testing the Slack identity auth door through the real FastAPI + mcp stack.

- `FastMCP(...)` defaults host to 127.0.0.1, and on that default mcp >= 1.10 turns on `TransportSecuritySettings(enable_dns_rebinding_protection=True, allowed_hosts=["127.0.0.1:*","localhost:*","[::1]:*"])`. The matcher needs an exact entry or `<base>:<port>`; bare `localhost` fails and `intradiem-gtm-system.onrender.com` fails. Result: 421 "Invalid Host header" AFTER the key middleware passes, so an unauthenticated probe still shows 401 and hides it.
- Reproduced locally with Host = the Render hostname (13/13 smoke checks after the fix, 4 failures before). CONFIRMED FIXED on Render Sep 11 2026 ~20:00Z (keyed tools/list returned five tools, no 421). Before that deploy it was not confirmed on Render itself: the key lives only in Render's GTM_API_KEYS. The Sep 1 Cowork strike-room "could not load accounts" is consistent with this and was attributed to the connector at the time ([[strike-room-cowork-connector-gap-sep1]]).
- Fix in `gtm-hosted-platform/brain/app.py`: pass `transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False)` (import guarded for old mcp). The brain is public, HTTPS, and authenticated in its own middleware, so host pinning was never the right layer.
- Same staged deploy also carries: the Slack identity auth door (actor "slackbot", `auth: slack_identity` in the request log, secret in `SLACK_SIGNING_SECRET`), and `mcp>=1.12,<2` in requirements.txt because mcp 2.x renamed FastMCP to MCPServer and an unpinned rebuild crashes at import.
- Tests: `brain/test_brain_slack_auth.py` 20/20, `brain/test_brain_state.py` 36/36, plus a scratchpad end-to-end smoke (needs a py3.12 venv with the requirements; the system python3 is 3.9 and cannot install mcp).
- Deploy sheet: `~/Desktop/Intradiem Deliverables/Slackbot Brain Connect - Sep 11.html` (create Slack app from `gtm-hosted-platform/slack/slackbot_mcp_manifest.json`, secret into Render, deploy, verify keyed tools/list, only then install the app). Nothing committed, nothing deployed as of Sep 11.

**Why:** a keyed probe is the only thing that reveals the 421, and nobody had one in hand since the Sep 5 rewrite.
**How to apply:** after any brain deploy, run the keyed tools/list curl from the sheet, not just /healthz. See [[slack-surfaces-workflows-findings-sep10]].
