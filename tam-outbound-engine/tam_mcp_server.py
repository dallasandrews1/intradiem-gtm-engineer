#!/usr/bin/env python3
"""
Intradiem TAM Outbound MCP Server

Lets the team pull a ready-to-send account strike plan inside Claude, by domain.
Reads the same configs and data as account_engine.py, so the MCP, the dashboard,
and the daily digest never disagree.

Run manually:
    python tam_mcp_server.py

Claude Desktop config (claude_desktop_config.json):
    "intradiem-tam": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/tam-outbound-engine/tam_mcp_server.py"]
    }
"""
import json
from datetime import date

from mcp.server.fastmcp import FastMCP

import account_engine as eng

mcp = FastMCP("intradiem-tam")


def _plays():
    return eng.build_plays(eng.load_cfg(), date.today())


@mcp.tool()
def list_strike_accounts() -> str:
    """List target accounts ranked by fit and why-now, with ROI and the top trigger. Work the top of the list."""
    out = []
    for p in _plays():
        out.append({
            "company": p["company"], "domain": p["domain"], "fit": p["icp_total"],
            "tier": p["tier"], "fresh_trigger": p["fresh"], "roi": p["roi_label"],
            "top_trigger": p["triggers"][0]["label"] if p["triggers"] else None,
            "seller": p["seller"]["seller_name"] if p.get("seller") else None,
        })
    return json.dumps({"data_source": eng.get_data_source(), "accounts": out}, indent=2)


@mcp.tool()
def get_strike_plan(domain: str) -> str:
    """Get the full account strike plan for one domain: fit, ROI, why-now triggers, buying committee, and a ready-to-send sequence per persona."""
    match = next((p for p in _plays() if p["domain"] == domain), None)
    if not match:
        return json.dumps({"error": f"{domain} is not in the target set"})
    return json.dumps({"data_source": eng.get_data_source(), **match}, indent=2)


@mcp.tool()
def accounts_for_seller(seller_email: str) -> str:
    """Get the ranked strike list for one seller by email, so they can work their own queue."""
    mine = [p for p in _plays() if p.get("seller") and p["seller"]["seller_email"] == seller_email]
    if not mine:
        return json.dumps({"error": f"no accounts found for {seller_email}"})
    out = [{"company": p["company"], "domain": p["domain"], "fit": p["icp_total"],
            "roi": p["roi_label"], "fresh_trigger": p["fresh"]} for p in mine]
    return json.dumps({"data_source": eng.get_data_source(), "accounts": out}, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
