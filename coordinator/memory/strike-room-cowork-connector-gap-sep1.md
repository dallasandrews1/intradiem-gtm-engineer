---
name: strike-room-cowork-connector-gap-sep1
description: "Sep 1 2026 - work-Mac Cowork strike room artifact fails \"could not load accounts\"; artifact owned by the Enterprise account, intradiem-gtm connector not enabled there; brain on Render verified alive"
metadata: 
  node_type: memory
  type: project
  originSessionId: dec5e70c-3215-404e-972c-ae9046856fa8
  modified: 2026-09-01T19:11:17.092Z
---

Sep 1 2026: the strike room artifact in Cowork on the work Mac shows "could not load accounts". Diagnosis from the personal Mac:

- The artifact is NOT owned by the personal account (not in the 14-artifact list, shared listing empty), so it belongs to the work/Enterprise Claude account and can only be read/republished from a session there.
- The backend it needs is ALIVE: the intradiem-gtm brain at https://intradiem-gtm-system.onrender.com/mcp (FastMCP, 5 tools: strike_list, get_strike_plan(domain), list_signals, get_signals(domain), impact_scorecard), gated by the X-API-Key header (same GTM_API_KEYS as REST). First response after idle took ~12s (Render cold start) - one retry before calling it broken.
- The repo copy of the plugin config (gtm-hosted-platform/plugin/intradiem-gtm/.claude-plugin/plugin.json) carries the placeholder SET_THE_CLAUDE_KEY_HERE; the real key lives in Render's GTM_API_KEYS env, not in git.
- Enabling the connector in Cowork is an account/machine action on the work Mac; a copy-paste fix prompt was handed to Dallas for a Cowork session there (read the artifact's mcp capability manifest first, then enable or republish to match). Related: [[two-machine-sync-loop-aug31]].
