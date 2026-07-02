# Intradiem GTM plugin

Lets a seller ask Claude in plain language for strike plans and signals. It connects
to the hosted GTM brain, so there is nothing to install and no data on the seller's
machine.

## Set it up (owner, once)

Edit `.claude-plugin/plugin.json` and set two values:

- `url` → your brain's MCP endpoint, e.g. `https://brain.dallasandrews.dev/mcp`
- `X-API-Key` → the `claude` key from the brain's `GTM_API_KEYS`

Then zip the `intradiem-gtm` folder and distribute it. Sellers install the plugin and
start asking. `RULES_OF_THE_ROAD.md` ships with it.

## Two transport options

- **Remote (default, in plugin.json above): install-free.** The plugin is just a URL
  and a key. Best for a wide rollout. Requires the brain to be hosted and reachable.
- **Local stdio (fallback): `mcp/gtm_client.py`.** A small client that runs on the
  seller's machine and needs `python3` with `mcp` and `requests`. Use it only if you
  cannot expose the brain over the network. To switch to it, replace the `mcpServers`
  block with:

  ```json
  "mcpServers": {
    "intradiem-gtm": {
      "command": "python3",
      "args": ["${CLAUDE_PLUGIN_ROOT}/mcp/gtm_client.py"],
      "env": { "BRAIN_URL": "https://YOUR-BRAIN-HOST", "BRAIN_API_KEY": "THE_CLAUDE_KEY" }
    }
  }
  ```

## What sellers can ask

"strike plan for AmeriHealth", "what's hot today", "who do I target at Navient",
"any expansion risk on Centene", "show me the impact numbers". The included skill
tells Claude how to use the tools and always carries the verify-before-send guardrail.
