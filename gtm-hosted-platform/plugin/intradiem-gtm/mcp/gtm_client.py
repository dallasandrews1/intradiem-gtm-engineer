#!/usr/bin/env python3
"""
Intradiem GTM plugin MCP client.

A thin tool layer that calls the hosted GTM brain over HTTP. Sellers install the
plugin and ask in plain language; this turns those asks into brain calls. It holds
no engine logic and no data, so nothing the seller can see or change. The brain,
configs, and Clay stay with you.

Env (set in plugin.json or the environment):
    BRAIN_URL       https://your-brain-host
    BRAIN_API_KEY   the 'claude' key from the brain's GTM_API_KEYS
"""
import json
import os

import requests
from mcp.server.fastmcp import FastMCP

BRAIN = os.environ.get("BRAIN_URL", "http://localhost:8000")
KEY = os.environ.get("BRAIN_API_KEY", "")
mcp = FastMCP("intradiem-gtm")


def _get(path):
    r = requests.get(BRAIN + path, headers={"X-API-Key": KEY}, timeout=20)
    if r.status_code == 404:
        return {"error": r.json().get("detail", "not found")}
    r.raise_for_status()
    return r.json()


@mcp.tool()
def strike_list() -> str:
    """List net-new target accounts ranked by fit and why-now, with ROI and the top trigger."""
    return json.dumps(_get("/v1/strike"), indent=2)


@mcp.tool()
def get_strike_plan(domain: str) -> str:
    """Get the full account strike plan for one domain: fit, ROI, why-now, buying committee, and a ready-to-send sequence per persona."""
    return json.dumps(_get(f"/v1/strike/{domain}"), indent=2)


@mcp.tool()
def list_signals() -> str:
    """List install-base accounts with their firing expansion and risk signals."""
    return json.dumps(_get("/v1/signals"), indent=2)


@mcp.tool()
def get_signals(domain: str) -> str:
    """Get expansion and risk signals for one install-base account by domain."""
    return json.dumps(_get(f"/v1/signals/{domain}"), indent=2)


@mcp.tool()
def impact_scorecard() -> str:
    """Get the GTM impact scorecard: opportunity surfaced, activity, and realized results."""
    return json.dumps(_get("/v1/impact"), indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
