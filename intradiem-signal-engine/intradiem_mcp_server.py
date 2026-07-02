#!/usr/bin/env python3
"""
Intradiem GTM Signal MCP Server

Wraps the signal processor so Claude (or anyone on the team using Claude/Cowork)
can query live expansion and risk signals as tool calls. Reads the same
data/accounts.csv and config/thresholds.json as the processor, so the MCP and
the dashboard never drift.

Run manually:
    python intradiem_mcp_server.py            # stdio transport for Claude Desktop

Claude Desktop config (claude_desktop_config.json):
    "mcpServers": {
      "intradiem-signals": {
        "command": "python3",
        "args": ["/ABSOLUTE/PATH/intradiem_mcp_server.py"]
      }
    }
"""
import json

from mcp.server.fastmcp import FastMCP

import signal_processor as engine

mcp = FastMCP("intradiem-signals")


@mcp.tool()
def get_expansion_signals(domain: str) -> str:
    """Get expansion and risk signals for one Intradiem account by domain."""
    results = engine.process()
    match = next((r for r in results if r["domain"] == domain), None)
    if not match:
        return json.dumps({"error": f"{domain} is not a monitored account"})
    return json.dumps({"data_source": engine.get_data_source(), **match}, indent=2)


@mcp.tool()
def list_monitored_accounts() -> str:
    """List every account currently monitored, with how many signals are firing."""
    results = engine.process()
    summary = [
        {"company": r["company"], "domain": r["domain"],
         "signals_fired": r["signals_fired"], "primary_routing": r["primary_routing"]}
        for r in results
    ]
    return json.dumps({"data_source": engine.get_data_source(), "accounts": summary}, indent=2)


@mcp.tool()
def score_all() -> str:
    """Score every monitored account and return the full signal set, sorted by signals firing."""
    results = sorted(engine.process(), key=lambda r: -r["signals_fired"])
    return json.dumps({"data_source": engine.get_data_source(), "accounts": results}, indent=2)


@mcp.tool()
def add_monitored_account(
    domain: str, company: str, licensed_seats: int, active_seats: int,
    total_agents: int, agents_coached: int, coaching_sessions_per_day: int,
    available_rules: int, active_rules: int, wfm_connected: bool,
    crm_connected: bool, wfm_days_active: int, automation_vol_current: int,
    automation_vol_prev1: int, automation_vol_prev2: int,
    champion_changed: bool, days_to_renewal: int,
) -> str:
    """Add an account to the monitored set by appending a row to accounts.csv, then score it."""
    import csv
    import os
    row = {
        "domain": domain, "company": company, "licensed_seats": licensed_seats,
        "active_seats": active_seats, "total_agents": total_agents,
        "agents_coached": agents_coached, "coaching_sessions_per_day": coaching_sessions_per_day,
        "available_rules": available_rules, "active_rules": active_rules,
        "wfm_connected": str(bool(wfm_connected)).lower(),
        "crm_connected": str(bool(crm_connected)).lower(),
        "wfm_days_active": wfm_days_active, "automation_vol_current": automation_vol_current,
        "automation_vol_prev1": automation_vol_prev1, "automation_vol_prev2": automation_vol_prev2,
        "champion_changed": str(bool(champion_changed)).lower(), "days_to_renewal": days_to_renewal,
    }
    exists = os.path.exists(engine.DEFAULT_DATA)
    with open(engine.DEFAULT_DATA, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not exists:
            writer.writeheader()
        writer.writerow(row)
    match = next((r for r in engine.process() if r["domain"] == domain), None)
    return json.dumps({"added": domain, "result": match}, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
