#!/usr/bin/env python3
"""Merge researcher JSON (automation/inbox/account_facts/<date>/*.json) into
tam-outbound-engine/data/account_facts.json.

Validation before anything merges: employees and contact_center need a URL and a verbatim quote
(or basis), trigger rows need url + quote + date + family, aggregator-only citations are rejected,
dates must parse. Dry-run by default (prints the diff, writes nothing) until
automation/config/account_facts.json has "merge": true.

Usage:
    account_facts_merge.py [--inbox DIR] [--apply] [--select]   # --select prints the domains due a refresh
"""
import argparse
import datetime
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FACTS = os.path.join(ROOT, "tam-outbound-engine", "data", "account_facts.json")
ACCOUNTS = os.path.join(ROOT, "tam-outbound-engine", "data", "tam_accounts.csv")
CFG = os.path.join(HERE, "config", "account_facts.json")
INBOX = os.path.join(HERE, "inbox", "account_facts")
AGGREGATORS = ("layoffhedge.com", "theofficialboard.com", "rocketreach.co", "nerdwallet.com", "zoominfo.com",
               "craft.co", "wikipedia.org")
FAMILIES = {"wfm_hiring", "cc_expansion", "cost_mandate", "leadership_change", "csat_pressure",
            "qbp_earnings_pressure", "quality_identity_gap", "verint_backoffice"}
TODAY = datetime.date.today()


def load(p, default):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return default


def valid_date(s):
    try:
        datetime.date.fromisoformat(str(s)[:10])
        return True
    except ValueError:
        return False


def validate(r):
    """Return (clean_record, problems). A record with no usable employees and no usable triggers is dropped."""
    problems = []
    out = {"company": r.get("company"), "industry": r.get("industry"), "notes": (r.get("notes") or "")[:600]}
    e = r.get("employees") or {}
    if e and e.get("value") and e.get("url") and (e.get("quote") or "").strip():
        if any(a in e["url"] for a in AGGREGATORS) and "stockanalysis.com" not in e["url"]:
            problems.append("employees cited to an aggregator, dropped")
            out["employees"] = None
        else:
            out["employees"] = {"value": int(e["value"]), "as_of": str(e.get("as_of", ""))[:10], "url": e["url"], "quote": e["quote"].strip()[:300]}
    else:
        out["employees"] = None
        if e:
            problems.append("employees missing url or quote, dropped")
    cc = r.get("contact_center") or None
    if cc and cc.get("value") and cc.get("url") and cc.get("basis"):
        out["contact_center"] = {"value": int(cc["value"]), "basis": cc["basis"][:300], "url": cc["url"]}
    else:
        out["contact_center"] = None
    trig = []
    for t in r.get("triggers") or []:
        if not (t.get("url") and (t.get("quote") or "").strip() and t.get("date") and t.get("trigger_type") in FAMILIES):
            problems.append(f"trigger dropped (missing url/quote/date or unknown family): {str(t.get('trigger_type'))} {str(t.get('date'))}")
            continue
        if any(a in t["url"] for a in AGGREGATORS):
            problems.append(f"trigger dropped (aggregator source): {t['url']}")
            continue
        if not valid_date(t["date"]) or datetime.date.fromisoformat(t["date"][:10]) > TODAY:
            problems.append(f"trigger dropped (bad or future date): {t['date']}")
            continue
        trig.append({"trigger_type": t["trigger_type"], "date": t["date"][:10], "detail": (t.get("detail") or "")[:240],
                     "quote": t["quote"].strip()[:300], "url": t["url"]})
    out["triggers"] = trig
    if not out["employees"] and not trig and not out["contact_center"]:
        return None, problems + ["nothing usable, record dropped"]
    return out, problems


def select_due(cfg):
    facts = load(FACTS, {"facts": {}}).get("facts", {})
    max_age = cfg.get("max_age_days", 90)
    due = []
    import csv
    try:
        rows = list(csv.DictReader(open(ACCOUNTS)))
    except OSError:
        rows = []
    for r in rows:
        d = r["domain"]
        f = facts.get(d)
        if not f or not f.get("facts_updated"):
            due.append(d)
            continue
        try:
            age = (TODAY - datetime.date.fromisoformat(f["facts_updated"])).days
        except ValueError:
            age = 10 ** 6
        if age > max_age or not f.get("employees"):
            due.append(d)
    return due[: cfg.get("max_per_run", 21)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inbox", default=None)
    ap.add_argument("--apply", action="store_true", help="write even if config merge=false")
    ap.add_argument("--select", action="store_true")
    a = ap.parse_args()
    cfg = load(CFG, {"merge": False, "max_age_days": 90, "max_per_run": 21})
    if a.select:
        print("\n".join(select_due(cfg)))
        return 0
    inbox = a.inbox or max(glob.glob(os.path.join(INBOX, "*")), default=None)
    if not inbox or not os.path.isdir(inbox):
        print("no inbox folder to merge")
        return 0
    store = load(FACTS, {"facts": {}})
    facts = store.setdefault("facts", {})
    merged, dropped, log = 0, 0, []
    for f in sorted(glob.glob(os.path.join(inbox, "*.json"))):
        try:
            recs = json.load(open(f))
        except ValueError as e:
            log.append(f"- {os.path.basename(f)}: invalid JSON, skipped ({e})")
            continue
        for r in recs if isinstance(recs, list) else []:
            dom = (r.get("domain") or "").lower().strip()
            if not dom:
                continue
            clean, problems = validate(r)
            if clean is None:
                dropped += 1
                log.append(f"- {dom}: DROPPED ({'; '.join(problems)})")
                continue
            prev = facts.get(dom, {})
            clean["facts_updated"] = TODAY.isoformat()
            clean["facts_source"] = f"account-facts refresh {os.path.basename(inbox)}"
            # keep a previously known public contact-centre figure if the new pass found none
            if not clean["contact_center"] and prev.get("contact_center"):
                clean["contact_center"] = prev["contact_center"]
            # union triggers by (type, date), newest pass wins on text
            seen = {(t["trigger_type"], t["date"]): t for t in prev.get("triggers", [])}
            for t in clean["triggers"]:
                seen[(t["trigger_type"], t["date"])] = t
            clean["triggers"] = sorted(seen.values(), key=lambda t: t["date"], reverse=True)[:8]
            facts[dom] = clean
            merged += 1
            log.append(f"- {dom}: employees {clean['employees']['value'] if clean['employees'] else 'n/a'}, "
                       f"cc {'public' if clean['contact_center'] else 'estimate'}, triggers {len(clean['triggers'])}"
                       + (f" ({'; '.join(problems)})" if problems else ""))
    write = a.apply or cfg.get("merge")
    if write:
        json.dump(store, open(FACTS, "w"), indent=1)
    head = f"account-facts merge {TODAY.isoformat()}: {merged} merged, {dropped} dropped, {'WRITTEN' if write else 'DRY RUN, nothing written (automation/config/account_facts.json merge=false)'}"
    print(head)
    print("\n".join(log))
    os.makedirs(os.path.join(HERE, "logs"), exist_ok=True)
    with open(os.path.join(HERE, "logs", f"account-facts-{TODAY.isoformat()}.md"), "a") as fh:
        fh.write(f"# account-facts {TODAY.isoformat()}\n\n{head}\n\n" + "\n".join(log) + f"\n\nevt: account-facts-{TODAY.isoformat()}#merge\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
