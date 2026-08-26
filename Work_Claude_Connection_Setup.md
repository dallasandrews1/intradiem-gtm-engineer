# Connecting Your Work Claude Account to the GTM Brain and Engines

You already have the brain live on Render. That changes the whole approach: you do not copy engines onto the work MacBook, you connect to the one hosted brain over the network. Same brain serves work Cowork, Greenlight, Slack, and the plugin. Machine-independent.

## The one thing to do first: set a real key

Right now `plugin.json` has `SET_THE_CLAUDE_KEY_HERE`. The brain authenticates on `X-API-Key` matching a `label:key` pair in the `GTM_API_KEYS` env var.

1. Render dashboard → your `intradiem-gtm-system` service → Environment.
2. Set `GTM_API_KEYS` to a comma list, one key per surface so the request log shows which surface drove usage:
   `claude:REALKEY1,slack:REALKEY2,greenlight:REALKEY3`
3. Save and let it redeploy.

Use a different key per surface. That is how `logs/requests.jsonl` tells you adoption by surface later.

## Primary path: connect work Claude/Cowork to the brain over remote MCP

The brain exposes an MCP endpoint at `/mcp`. This is the best way in, because it gives you the engine tools in any chat with zero local setup.

1. In your work Claude/Cowork: Settings → Connectors → Add custom connector (remote / HTTP MCP server).
2. URL: `https://intradiem-gtm-system.onrender.com/mcp`
3. Add header: `X-API-Key: REALKEY1` (the `claude:` key you set on Render).
4. Save and enable.

You now have `get_strike_plan`, `get_signals`, `strike_list`, `list_signals`, `impact_scorecard` available from your work account. Nothing was copied to the machine.

Fastest equivalent: your plugin `gtm-hosted-platform/plugin/intradiem-gtm/` is literally this config bundled. Install the plugin instead of hand-adding the connector if your work Cowork takes plugins. Just set the real key first.

Assumption to verify: that your work Cowork allows adding custom remote connectors. If it is locked to an approved list, ask Naveen or IT to allowlist your Render URL. The brain-over-HTTP path is the one that survives a locked-down environment, which is exactly why hosting it was the right call.

## Secondary path: local MCP servers (only if you want the full engine toolset locally)

The brain exposes five tools. The raw engines expose more (`add_monitored_account`, `score_all`, `accounts_for_seller`, etc.). If you want those directly:

1. Push the repo to Bitbucket, clone it onto the work MacBook.
2. Register the two stdio MCP servers in your work Claude/Cowork MCP config:
   - `intradiem-signals` → `python3 intradiem-signal-engine/intradiem_mcp_server.py`
   - `intradiem-tam` → `python3 tam-outbound-engine/tam_mcp_server.py`
3. These run against the cloned files on that machine, so the data lives on the work Mac.

Use this only for your own deep work. For anything shared (Greenlight agents, sellers), the hosted brain is the right surface.

## What to move vs what stays

- Move to Intradiem systems (Bitbucket, work Cowork): the engines, skills, config, Star Ratings data, Clay prompts. This is work product and belongs where it operates.
- Keep in your personal space: `dallas-brand`, the LinkedIn About files, interview-era 30-60-90 drafts.
- Curate what people see: engineering gets the repo; Naveen and the org get the polished leave-behinds (`GTM_Engineer_Operating_System`, `GTM_Engine_for_Naveen_Review.html`). No raw folder dumps.

## Key hygiene (do this before pushing to Bitbucket)

Do not commit real keys. Keep `SET_THE_CLAUDE_KEY_HERE` as the placeholder in `plugin.json` in the repo, and set the real key only in the connector config and in Render's env. If a real key ever lands in git history, rotate it on Render.

## Render free-tier caveat

Free instances sleep after inactivity, so the first call after idle can take 30 to 60 seconds to wake. If sellers or a Greenlight agent will hit it live, either move to a paid instance or add a keep-warm ping so the first request of the day is not slow.

## Today's connection steps, in order

1. Open `/healthz` in a browser to confirm the brain is awake.
2. Set the real `GTM_API_KEYS` on Render, redeploy.
3. Add the remote MCP connector (or install the plugin) in work Cowork with the real key.
4. Run one test call (`get_strike_plan` for an account you know) to confirm the round trip.
5. Then wire the same URL and key into the Signal-to-Play Greenlight agent.
