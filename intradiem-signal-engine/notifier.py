#!/usr/bin/env python3
"""
Intradiem Signal Notifier

Routes firing signals to the AE or CSM who owns the account, via Slack DM or email.

Dry-run by default: it prints exactly what it would send and to whom, and sends
nothing. That is the safe way to validate routing and message copy before any real
rep gets pinged.

Ownership comes from data/owners.csv (domain -> AE and CSM, with Slack handle and
email). In the role you replace that file with a Salesforce owner export and the
routing becomes real with no code change.

Usage:
    python notifier.py                     # dry-run, print what would be sent
    python notifier.py --channel slack     # preview only the Slack DMs
    python notifier.py --send --channel slack   # actually send (needs SLACK_BOT_TOKEN)
    python notifier.py --send --channel email   # actually send (needs SMTP_* env vars)

Going live later:
    Slack  -> set SLACK_BOT_TOKEN (a bot token with chat:write and users:read.email)
    Email  -> set SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SMTP_FROM
    The suppression window in config/thresholds.json plus notified_state.json stop
    the same signal pinging the same owner twice inside the window.
"""
import argparse
import csv
import json
import os
from datetime import datetime, timezone, timedelta

import signal_processor as engine

HERE = os.path.dirname(os.path.abspath(__file__))
OWNERS_PATH = os.path.join(HERE, "data", "owners.csv")
NOTIFIED_PATH = os.path.join(HERE, "data", "notified_state.json")
QUEUE_URL = "https://intradiem.dallasandrews.dev"


def load_owners(path=OWNERS_PATH):
    owners = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            owners[r["domain"]] = {
                "AE": {"name": r["ae_name"], "email": r["ae_email"], "slack": r["ae_slack"]},
                "CSM": {"name": r["csm_name"], "email": r["csm_email"], "slack": r["csm_slack"]},
            }
    return owners


def load_notified(path=NOTIFIED_PATH):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_notified(state, path=NOTIFIED_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2)


def already_notified(state, domain, sig_type, email, window_days, now):
    key = f"{domain}|{sig_type}|{email}"
    last = state.get(key)
    if last and now - datetime.fromisoformat(last) < timedelta(days=window_days):
        return True
    return False


def build_groups(results, owners, state, window_days, now, dedup=True):
    """Group firing signals by recipient. Returns (groups, missing_owner_domains)."""
    groups = {}
    missing = []
    for r in results:
        if r["signals_fired"] == 0:
            continue
        orec = owners.get(r["domain"])
        if not orec:
            missing.append(r["domain"])
            continue
        for sig in r["signals"]:
            for role in sig["route"].split("+"):
                owner = orec.get(role)
                if not owner:
                    continue
                if dedup and already_notified(state, r["domain"], sig["type"], owner["email"], window_days, now):
                    continue
                g = groups.setdefault(owner["email"], {
                    "name": owner["name"], "email": owner["email"],
                    "slack": owner["slack"], "roles": set(), "items": [],
                })
                g["roles"].add(role)
                g["items"].append({
                    "company": r["company"], "domain": r["domain"], "role": role,
                    "type": sig["type"], "value": sig["value"],
                    "reason": sig["reason"], "route": sig["route"],
                })
    return groups, missing


def format_message(group):
    first = group["name"].split()[0]
    n = len(group["items"])
    head = f"Hi {first}, {n} signal{'s' if n != 1 else ''} routed to you:"
    lines = []
    for it in group["items"]:
        lines.append(
            f"  - {it['company']} ({it['domain']}): {it['type']} {it['value']}. "
            f"{it['reason']} Route: {it['route']}."
        )
    return head + "\n" + "\n".join(lines) + f"\n  Open the queue: {QUEUE_URL}"


def send_slack(slack_handle, email, text):
    """Live Slack DM. Resolves the user by email, then posts a direct message."""
    import urllib.request
    import urllib.parse
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise SystemExit("SLACK_BOT_TOKEN not set. Cannot send Slack messages.")
    def call(method, params):
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(
            f"https://slack.com/api/{method}", data=data,
            headers={"Authorization": f"Bearer {token}"})
        return json.load(urllib.request.urlopen(req))
    lookup = call("users.lookupByEmail", {"email": email})
    if not lookup.get("ok"):
        raise RuntimeError(f"Slack lookup failed for {email}: {lookup.get('error')}")
    user_id = lookup["user"]["id"]
    res = call("chat.postMessage", {"channel": user_id, "text": text})
    if not res.get("ok"):
        raise RuntimeError(f"Slack send failed for {email}: {res.get('error')}")


def send_email(to_email, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    host = os.environ.get("SMTP_HOST")
    if not host:
        raise SystemExit("SMTP_HOST not set. Cannot send email.")
    msg = MIMEText(text)
    msg["Subject"] = subject
    msg["From"] = os.environ.get("SMTP_FROM", "signals@intradiem.com")
    msg["To"] = to_email
    with smtplib.SMTP(host, int(os.environ.get("SMTP_PORT", "587"))) as s:
        s.starttls()
        if os.environ.get("SMTP_USER"):
            s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
        s.send_message(msg)


def main():
    p = argparse.ArgumentParser(description="Route firing signals to owning AE/CSM")
    p.add_argument("--send", action="store_true", help="actually send (default is dry-run)")
    p.add_argument("--channel", choices=["slack", "email", "both"], default="both")
    p.add_argument("--owners", default=OWNERS_PATH)
    args = p.parse_args()

    cfg = engine.load_config(engine.DEFAULT_CONFIG)
    window = cfg.get("suppression_days", 14)
    now = datetime.now(timezone.utc)

    results = engine.process()
    owners = load_owners(args.owners)
    state = load_notified()
    groups, missing = build_groups(results, owners, state, window, now, dedup=True)

    mode = "LIVE SEND" if args.send else "DRY RUN (nothing sent)"
    print("=" * 60)
    print(f"Intradiem Signal Notifier  |  {mode}  |  channel: {args.channel}")
    print(f"{len(groups)} owner(s) to notify, window {window} days")
    print("=" * 60)

    if missing:
        print(f"\nNo owner on file for: {', '.join(sorted(set(missing)))} (skipped)\n")

    for g in groups.values():
        text = format_message(g)
        targets = []
        if args.channel in ("slack", "both"):
            targets.append(f"Slack {g['slack']}")
        if args.channel in ("email", "both"):
            targets.append(f"email {g['email']}")
        print(f"\nTo: {g['name']}  ({' / '.join(sorted(g['roles']))})  via {', '.join(targets)}")
        print("-" * 60)
        print(text)

        if args.send:
            subject = "Intradiem signals routed to you"
            if args.channel in ("slack", "both"):
                send_slack(g["slack"], g["email"], text)
            if args.channel in ("email", "both"):
                send_email(g["email"], subject, text)
            for it in g["items"]:
                state[f"{it['domain']}|{it['type']}|{g['email']}"] = now.isoformat()

    if args.send:
        save_notified(state)
        print("\nSent and recorded. Re-running inside the window will skip these.")
    else:
        print("\n\nDry run complete. Nothing was sent. Add --send to deliver for real.")


if __name__ == "__main__":
    main()
