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
import csv
import json
import os
import re
from datetime import date

from mcp.server.fastmcp import FastMCP

import account_engine as eng

mcp = FastMCP("intradiem-tam")

HERE = os.path.dirname(os.path.abspath(__file__))
ACCOUNTS_CSV = os.path.join(HERE, "data", "tam_accounts.csv")
TRIGGERS_CSV = os.path.join(HERE, "data", "triggers.csv")


def _plays():
    plays, _ = eng.build_plays(eng.load_cfg(), date.today())
    return plays


def _excluded():
    _, excluded = eng.build_plays(eng.load_cfg(), date.today())
    return excluded


def _append_row(path, values):
    """Append one row to a CSV by HEADER NAME, never by position.

    The old writer passed a positional list. tam_accounts.csv has 12 columns and the list
    had 7, so `wfm` landed in `acd_source` and the three provenance columns were never
    written at all. Any column added to the header would have silently shifted it again.
    Binding to the header makes that class of drift impossible: unknown keys raise, and
    columns the caller did not supply are written empty rather than absorbing the next
    value. Added 2026-09-05.
    """
    with open(path, newline="") as f:
        header = next(csv.reader(f))
    unknown = set(values) - set(header)
    if unknown:
        raise ValueError(f"{os.path.basename(path)} has no column(s): {', '.join(sorted(unknown))}")
    with open(path, "a", newline="") as f:
        csv.DictWriter(f, fieldnames=header).writerow({k: values.get(k, "") for k in header})
    return header


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
    shut = next((e for e in _excluded() if e["domain"] == domain), None)
    if shut:
        return json.dumps({"error": f"{shut['company']} is a confirmed customer ({shut['match']}); "
                           "no cold strike plan. Route as install-base expansion."})
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


@mcp.tool()
def add_strike_account(domain: str, company: str, industry: str = "Health Insurance",
                       employees: int = 0, agent_count: int = 0,
                       acd: str = "Unknown", wfm: str = "Unknown",
                       source: str = "", acd_source: str = "", acd_observed: str = "",
                       wfm_source: str = "", wfm_observed: str = "",
                       trigger_type: str = "", trigger_detail: str = "",
                       trigger_source: str = "") -> str:
    """Add a net-new account to the strike universe (writes data/tam_accounts.csv; optional first
    trigger to data/triggers.csv). The account is scored on the next read, so it appears in the
    strike room immediately. Adds data only; sends stay behind the critic and human gates.

    Pass `source` (and `trigger_source` with a trigger). A row with no citation is SEED: it
    scores, but nothing on it may reach a prospect, a seller, a slide or a recording."""
    domain = (domain or "").strip().lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9.-]*\.[a-z]{2,}", domain):
        return json.dumps({"error": f"'{domain}' is not a valid domain"})
    if not (company or "").strip():
        return json.dumps({"error": "company name is required"})
    with open(ACCOUNTS_CSV, newline="") as f:
        rows = list(csv.DictReader(f))
    if any(r["domain"].strip().lower() == domain for r in rows):
        return json.dumps({"error": f"{domain} is already in the target set"})
    try:
        _append_row(ACCOUNTS_CSV, {
            "domain": domain, "company": company.strip(), "industry": industry.strip(),
            "employees": int(employees or 0), "agent_count": int(agent_count or 0),
            "acd": acd.strip() or "Unknown", "acd_source": acd_source.strip(),
            "acd_observed": acd_observed.strip(), "wfm": wfm.strip() or "Unknown",
            "wfm_source": wfm_source.strip(), "wfm_observed": wfm_observed.strip(),
            "source": source.strip(),
        })
    except ValueError as e:
        return json.dumps({"error": str(e)})
    trigger_added = False
    if trigger_type.strip() and trigger_detail.strip():
        _append_row(TRIGGERS_CSV, {
            "domain": domain, "trigger_type": trigger_type.strip(),
            "detail": trigger_detail.strip(), "date": date.today().isoformat(),
            "source": trigger_source.strip(),
        })
        trigger_added = True
    match = next((p for p in _plays() if p["domain"] == domain), None)
    shut = next((e for e in _excluded() if e["domain"] == domain), None)
    if shut:
        return json.dumps({
            "added": domain, "company": company.strip(), "trigger_added": trigger_added,
            "scored": None, "customer_excluded": True, "match": shut["match"],
            "note": "Row written, then held by the customer-exclusion gate. No cold plan; "
                    "route as install-base expansion.",
        }, indent=2)
    seed = bool(match and match.get("seed"))
    out = {
        "added": domain, "company": company.strip(), "trigger_added": trigger_added,
        "seed": seed,
        "scored": {"fit": match["icp_total"], "tier": match["tier"], "roi": match["roi_label"]} if match else None,
        "note": "Row appended to tam_accounts.csv; scoring is live on next read. No sends: critic + human gates unchanged.",
    }
    if seed:
        # The old return advertised fit/tier/ROI on a row with no citation and said nothing
        # about it, so a caller could read a confident number off unsourced data. Added 2026-09-05.
        out["warning"] = ("SEED row: no `source` on the account" + (" or the trigger" if trigger_added else "")
                          + ". It scores, but nothing on this row may reach a prospect, a seller, "
                            "a slide or a recording until the source column is filled.")
    return json.dumps(out, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
