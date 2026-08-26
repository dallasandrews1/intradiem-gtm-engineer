#!/usr/bin/env python3
"""Reply Engine v1 — classify a prospect reply, draft the reframe response, print the SOP checklist.

Dry-run by default and by design: this script NEVER sends anything. It classifies,
drafts from config templates, and tells the human exactly what to do next
(including flipping bdr_claimed on the Contacts row, which drops send_ready
READY -> HOLD via the live formula and pauses the automated cadence).

Usage:
    python3 reply_engine.py --reply "we just rolled out NICE last year"            # classify + draft
    python3 reply_engine.py --reply "..." --contact "Jane Doe" --account humana.com
    python3 reply_engine.py --reply "..." --output Humana_Objection_Response.md    # write the response doc
    python3 reply_engine.py --list                                                 # show the taxonomy

All thresholds, trigger phrases, and copy live in config/reply_categories.json.
Do not hardcode categories or templates here.
"""
import argparse
import json
import os
import re
import sys
from datetime import date, timedelta

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "reply_categories.json")

# Classification guardrails (structural, not business logic; business logic lives in config)
MIN_SCORE = 1          # at least one phrase hit
AMBIGUITY_GAP = 0      # if top two categories tie, route to manual review


def load_config(path=CONFIG_PATH):
    with open(path) as f:
        return json.load(f)


def normalize(text):
    return re.sub(r"\s+", " ", text.lower().replace("’", "'")).strip()


def classify(reply_text, config):
    """Score each category by trigger-phrase hits. Longer phrases weigh more.

    Returns (category_dict, score, hits, runner_up) — category is the
    'unclassified' sentinel when no confident match exists.
    """
    text = normalize(reply_text)
    scores = []
    for cat in config["categories"]:
        hits = [p for p in cat["trigger_phrases"] if p in text]
        # weight: 1 point per hit + 1 bonus per multi-word phrase (more specific)
        score = sum(1 + (1 if " " in p else 0) for p in hits)
        scores.append((score, cat, hits))
    scores.sort(key=lambda s: s[0], reverse=True)
    top_score, top_cat, top_hits = scores[0]
    runner_score, runner_cat, _ = scores[1]
    if top_score < MIN_SCORE:
        return config["unclassified"], 0, [], None
    if top_score - runner_score <= AMBIGUITY_GAP and runner_score > 0:
        # tie -> not confident enough to auto-draft
        return config["unclassified"], top_score, top_hits, (top_cat["key"], runner_cat["key"])
    return top_cat, top_score, top_hits, None


def fill_template(template, fields):
    body = template["body"]
    for k, v in fields.items():
        body = body.replace("{{%s}}" % k, v)
    return template["subject"], body


def sop_checklist(contact, account):
    who = contact or "<contact>"
    acct = account or "<account>"
    return [
        "1. CLASSIFY  - confirm the category above matches the reply's real objection (read the whole thread).",
        "2. DRAFT     - run the draft through intradiem-copy-sharpener; verified-claims gate on any figure.",
        "3. APPROVE   - Nathan reads and okays the final text. It sends from Nathan's mailbox, his voice, his name.",
        "4. CLAIM     - in Clay Contacts (Buying Committee), check bdr_claimed on %s's row. send_ready drops READY -> HOLD automatically; the cadence stops touching them." % who,
        "5. PAUSE     - confirm 'Pause leads at the same company on reply' held for %s (P2 has it ON; P1 gets it at launch)." % acct,
        "6. LOG       - closed-loop cols on the Contacts row: outcome=replied, category, response_sent date. Append to impact/outcomes.csv (date, account, type=reply, value, note).",
        "7. FOLLOW-UP - calendar the category's named follow-up date. No orphan replies.",
    ]


def build_response_doc(reply_text, contact, account, cat, score, hits, subject, body, ambiguous):
    today = date.today().isoformat()
    fu = cat.get("follow_up", {})
    fu_date = (date.today() + timedelta(days=fu.get("days", 14))).isoformat()
    lines = []
    lines.append("# %s — Objection Response (%s)" % (account or "Account", today))
    lines.append("")
    lines.append("## Objection captured")
    lines.append("> %s" % reply_text.strip())
    lines.append("")
    lines.append("Source: email reply · Contact: %s · Account: %s" % (contact or "UNKNOWN", account or "UNKNOWN"))
    lines.append("")
    lines.append("## Classification")
    lines.append("- Category: **%s** (key: `%s`)" % (cat["label"], cat["key"]))
    lines.append("- Risk level: %s · Confidence score: %d · Matched: %s" % (cat.get("risk_level", "n/a"), score, ", ".join(hits) or "none"))
    if ambiguous:
        lines.append("- AMBIGUOUS between `%s` and `%s` — MANUAL REVIEW before drafting." % ambiguous)
    lines.append("- Root cause: %s" % cat.get("root_cause", "n/a"))
    lines.append("- Strategy: %s" % cat.get("strategy", "n/a"))
    lines.append("")
    if subject:
        lines.append("## Draft response (Nathan's voice — sharpen before send)")
        lines.append("")
        lines.append("Subject: %s" % subject)
        lines.append("")
        lines.append(body)
        lines.append("")
    lines.append("## Follow-up strategy")
    lines.append("- %s (target date: %s)" % (fu.get("action", "Manual: set per category."), fu_date))
    lines.append("")
    lines.append("## SOP checklist")
    for item in sop_checklist(contact, account):
        lines.append("- [ ] %s" % item)
    lines.append("")
    lines.append("*Generated by reply-engine v1. Nothing sends from this tool; the human gate is the point.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Reply Engine v1 (classify + draft; never sends)")
    ap.add_argument("--reply", help="The prospect's reply text (quote it)")
    ap.add_argument("--contact", default="", help="Contact name")
    ap.add_argument("--account", default="", help="Account name or domain")
    ap.add_argument("--first-name", default="", help="Override first name for the merge field")
    ap.add_argument("--output", help="Write the [Account]_Objection_Response.md doc to this path")
    ap.add_argument("--list", action="store_true", help="Print the category taxonomy and exit")
    args = ap.parse_args()

    config = load_config()

    if args.list:
        print("Reply Engine v1 — %d categories (config/reply_categories.json)" % len(config["categories"]))
        for c in config["categories"]:
            print("  %-16s %-28s risk=%-6s triggers=%d" % (c["key"], c["label"], c["risk_level"], len(c["trigger_phrases"])))
        return 0

    if not args.reply:
        ap.error("--reply is required (or use --list)")

    cat, score, hits, ambiguous = classify(args.reply, config)

    subject, body = None, None
    if cat["key"] != "unclassified":
        first = args.first_name or (args.contact.split()[0] if args.contact else "{{first_name}}")
        reengage = (date.today() + timedelta(days=cat.get("follow_up", {}).get("days", 30))).strftime("%B %d")
        fields = {
            "first_name": first,
            "reengage_date": reengage,
            "wfm_vendor": _guess_vendor(args.reply) or "your WFM",
            "artifact_link": "<one-pager or interactive artifact link>",
        }
        subject, body = fill_template(cat["template"], fields)

    doc = build_response_doc(args.reply, args.contact, args.account, cat, score, hits, subject, body, ambiguous)
    print(doc)

    if args.output:
        with open(args.output, "w") as f:
            f.write(doc + "\n")
        print("\n[written] %s" % args.output, file=sys.stderr)
    return 0


def _guess_vendor(text):
    for v in ("Verint", "NICE", "Calabrio", "Genesys", "Assembled", "Playvox"):
        if v.lower() in text.lower():
            return v
    return None


if __name__ == "__main__":
    sys.exit(main())
