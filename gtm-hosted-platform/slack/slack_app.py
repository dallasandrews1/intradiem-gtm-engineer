#!/usr/bin/env python3
"""
Intradiem GTM Slack app: sellers self-serve strike plans where they already work.

A seller types  /strikeplan amerihealth.com  in Slack and gets the account snapshot,
why-now, and a ready-to-personalize first touch per buying-committee persona, posted
back just to them. /strikeplan with no domain returns the ranked list.

This calls the hosted brain. Sellers never see the engine, the configs, or Clay.

Runs on Socket Mode, so no public URL is needed (good for an internal tool).
Env required:
    SLACK_BOT_TOKEN   xoxb-...   (bot token, scope: commands, chat:write)
    SLACK_APP_TOKEN   xapp-...   (app-level token, scope: connections:write)
    BRAIN_URL         https://your-brain-host         (default http://localhost:8000)
    BRAIN_API_KEY     the slack key from GTM_API_KEYS on the brain

Run:
    pip install slack_bolt requests
    python slack_app.py
"""
import os

import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

BRAIN = os.environ.get("BRAIN_URL", "http://localhost:8000")
KEY = os.environ.get("BRAIN_API_KEY", "")
DISCLAIMER = ("Draft on sample data. Verify the benchmark and peer claims and "
              "personalize before sending. Full committee and cadence in the Claude plugin.")

app = App(token=os.environ.get("SLACK_BOT_TOKEN", ""))


def brain_get(path):
    r = requests.get(BRAIN + path, headers={"X-API-Key": KEY}, timeout=20)
    r.raise_for_status()
    return r.json()


def format_plan(p):
    """Slack Block Kit: snapshot, why-now, and each persona's day-1 touch."""
    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": f"Strike plan: {p['company']}"}},
        {"type": "section", "text": {"type": "mrkdwn", "text":
            f"*{p['domain']}* · {p['industry']} · ~{p['agent_count']:,} agents on {p['acd']}/{p['wfm']}\n"
            f"Fit *{p['icp_total']}/100* (Tier {p['tier']}) · Recoverable *{p['roi_label']}/yr* "
            f"({p['roi_per_agent_label']}/agent) · Owner {p['seller']['seller_name'] if p.get('seller') else 'unassigned'}"}},
    ]
    why = "\n".join(f"• *{t['label']}*: {t['detail']}" for t in p.get("triggers", []))
    if why:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": f"*Why now*\n{why}"}})
    blocks.append({"type": "divider"})
    for m in p.get("committee", []):
        s1 = next((s for s in m.get("sequence", []) if s["day"] == 1), None)
        if not s1:
            continue
        body = s1["body"]
        if len(body) > 2800:
            body = body[:2800] + "…"
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text":
            f"*{m['role']}*\n_Day 1 · {s1['channel']} · {s1['subject']}_\n{body}"}})
    blocks.append({"type": "context", "elements": [{"type": "mrkdwn", "text": DISCLAIMER}]})
    return blocks


@app.command("/strikeplan")
def strikeplan(ack, respond, command):
    ack()
    domain = (command.get("text") or "").strip().lower()
    if not domain:
        try:
            accts = brain_get("/v1/strike")
        except Exception:
            respond("The strike engine is unreachable right now. Try again shortly.")
            return
        lines = ["*Strike list, ranked.* Run `/strikeplan <domain>` for the full plan.\n"]
        for a in accts:
            flag = " :fire:" if a.get("fresh") else ""
            lines.append(f"• *{a['company']}* ({a['domain']}) — fit {a['fit']}, {a['roi']}/yr — {a['top_trigger']}{flag}")
        respond("\n".join(lines))
        return
    try:
        plan = brain_get(f"/v1/strike/{domain}")
    except Exception:
        respond(f"Couldn't find `{domain}` in the target set. Run `/strikeplan` to see the list.")
        return
    respond(blocks=format_plan(plan), text=f"Strike plan for {plan['company']}")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN", "")).start()
