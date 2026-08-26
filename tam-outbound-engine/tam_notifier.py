#!/usr/bin/env python3
"""
Intradiem TAM Notifier: each seller's daily strike list.

For every seller, it gathers their target accounts ranked by fit and why-now, and
delivers a short morning digest: which accounts are hot today, why, the ROI, and a
pointer to open the full plan. Dry-run by default (prints, sends nothing).

Usage:
    python tam_notifier.py                  # dry-run, print each seller's digest
    python tam_notifier.py --send --channel slack   # go live (needs SLACK_BOT_TOKEN)

Going live mirrors notifier.py in the signal engine: SLACK_BOT_TOKEN for Slack,
SMTP_* for email. Validate in dry-run first, and only turn on sending once the
plays have earned trust.
"""
import argparse
import json
import os
from datetime import date

import account_engine as eng

QUEUE_URL = "https://intradiem.dallasandrews.dev"


def by_seller(plays):
    groups = {}
    for p in plays:
        s = p.get("seller")
        if not s:
            continue
        groups.setdefault(s["seller_email"], {"name": s["seller_name"], "slack": s["seller_slack"],
                                              "email": s["seller_email"], "accounts": []})
        groups[s["seller_email"]]["accounts"].append(p)
    for g in groups.values():
        g["accounts"].sort(key=lambda x: (x["fresh"], x["tier"] == 1, x["icp_total"]), reverse=True)
    return groups


def format_digest(g):
    first = g["name"].split()[0]
    hot = [a for a in g["accounts"] if a["fresh"]]
    lines = [f"Morning {first}. {len(hot)} account(s) are hot today:"]
    for a in g["accounts"]:
        flag = "HOT" if a["fresh"] else "warm"
        trig = a["triggers"][0]["label"] if a["triggers"] else "no fresh trigger"
        lines.append(f"  [{flag}] {a['company']} - fit {a['icp_total']}, {a['roi_label']}/yr - {trig}")
    lines.append(f"Open a plan for the full committee and sequences: {QUEUE_URL}")
    return "\n".join(lines)


def send_slack(email, text):
    import urllib.request
    import urllib.parse
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise SystemExit("SLACK_BOT_TOKEN not set.")
    def call(method, params):
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(f"https://slack.com/api/{method}", data=data,
                                     headers={"Authorization": f"Bearer {token}"})
        return json.load(urllib.request.urlopen(req))
    u = call("users.lookupByEmail", {"email": email})
    if not u.get("ok"):
        raise RuntimeError(f"Slack lookup failed for {email}: {u.get('error')}")
    r = call("chat.postMessage", {"channel": u["user"]["id"], "text": text})
    if not r.get("ok"):
        raise RuntimeError(f"Slack send failed for {email}: {r.get('error')}")


def main():
    p = argparse.ArgumentParser(description="Daily strike list per seller")
    p.add_argument("--send", action="store_true")
    p.add_argument("--channel", choices=["slack", "email", "both"], default="slack")
    args = p.parse_args()

    plays, _ = eng.build_plays(eng.load_cfg(), date.today())
    groups = by_seller(plays)
    mode = "LIVE SEND" if args.send else "DRY RUN (nothing sent)"
    print("=" * 60)
    print(f"TAM strike-list digest  |  {mode}  |  {len(groups)} seller(s)")
    print("=" * 60)
    for g in groups.values():
        text = format_digest(g)
        print(f"\nTo: {g['name']}  via Slack {g['slack']} / {g['email']}")
        print("-" * 60)
        print(text)
        if args.send and args.channel in ("slack", "both"):
            send_slack(g["email"], text)
    if not args.send:
        print("\n\nDry run complete. Nothing sent. Add --send to deliver.")


if __name__ == "__main__":
    main()
