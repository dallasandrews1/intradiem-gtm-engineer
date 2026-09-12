#!/usr/bin/env python3
"""Signal review ledger: war-room staged signals -> unreviewed / approved / denied.

The war room stages signals to automation/logs/staged_signals.csv and never merges them. This
script gives each staged row a stable id, resolves its domain (0 credits), maps it to a trigger
family, and keeps the decision state in automation/config/signal_reviews.json. The snapshot
generator serves unreviewed signals labelled (no scoring, no copy); approved ones become cited
triggers through universe_from_audiences.merge_triggers; denied ones are remembered and dropped.

Usage:
    signal_review.py sync [--no-clay] [--staged path] [--ledger path] [--log path]
        ingest new staged rows, write the ledger, write automation/logs/signal-review-<date>.md
    signal_review.py decide --id sig-... --state approved|denied --via "rundown thread <ts>"
        record a decision (the rundown thread listener calls this on APPROVE/DENY replies)
    signal_review.py pending
        print unreviewed signals, one per line, id first (what the rundown carries)
"""
import argparse
import csv
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STAGED = os.path.join(HERE, "logs", "staged_signals.csv")
LEDGER = os.path.join(HERE, "config", "signal_reviews.json")
DOMAIN_CACHE = os.path.join(HERE, "logs", ".heat_domain_cache.json")
DENYLIST = os.path.join(ROOT, "tam-outbound-engine", "config", "customer_denylist.json")
LOG_FAMILY = "signal-review"

FAMILY_RULES = [
    ("verint_backoffice", r"\bverint\b"),
    ("qbp_earnings_pressure", r"(?=.*\bstars?\b|.*star ratings?)(?=.*(?:bonus|quality|cut[- ]?point|methodolog|\bqbp\b|medicare advantage))"),
    ("leadership_change", r"\b(?:cfo|ceo|coo|cio|cao|chief \w+ officer|president|group president|evp|svp)\b[^.]{0,120}\b(?:appoint|named|names|hire|hired|join|succeed|steps? down|retire|interim|leave|depart|transition|promot)|\b(?:appoint|named|hire|promot)\w*\b[^.]{0,80}\b(?:cfo|ceo|coo|cio|cao|chief|president)\b|leadership (?:change|transition|restructur|appointment)"),
    ("cost_mandate", r"cost (?:reduction|cut|saving|discipline|synerg|mandate)|efficien|sg&a|operating expense|\bopex\b|expense (?:growth|discipline|management)|layoff|redundan|warn notice|restructuring charge|margin (?:restoration|expansion)|positive operating leverage|administrative cost"),
    ("wfm_hiring", r"workforce management|real[- ]time analyst|\brta\b|hiring (?:a )?(?:class|wave|\d+)|recruit"),
    ("cc_expansion", r"expansion|expand|new (?:state|contract|market|contact cent|call cent|site)|open(?:s|ed|ing) (?:a|its|new)|adding \\d+ (?:seats|jobs|agents|roles)|contract (?:win|award)|acquisition|affiliat|merger|membership (?:growth|gain)|absorb|take over|takes over|enrol"),
    ("csat_pressure", r"complaint|satisfaction|outage|backlog|claims? (?:handling|delay|queue|backlog)|service (?:quality|standard|level)|call answer|wait time|cyber|penalt|consent order|regulator"),
]
PARK_PATTERNS = r"NON-TARGET|OFF-THESIS"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:24]


def load_json(p, default):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return default


def clay_bin():
    b = subprocess.run(["zsh", "-lc", "command -v clay"], capture_output=True, text=True).stdout.strip()
    if b:
        return b
    import glob
    c = sorted(glob.glob(os.path.expanduser("~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")))
    return c[-1] if c else "clay"


def norm_domain(v):
    v = (v or "").strip().lower()
    v = re.sub(r"^https?://", "", v).split("/")[0]
    return re.sub(r"^www\.", "", v)


def clean_org(org):
    o = re.split(r"\s+[—-]\s+|\s+/\s+|\s+\(", org or "")[0].strip()
    return re.sub(r",?\s+(inc\.?|incorporated|corp\.?|corporation|holdings?,?\s*inc\.?|plc|group)$", "", o, flags=re.I).strip()


def name_key(s):
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    s = re.sub(r"\b(inc|incorporated|corp|corporation|holdings?|plc|group|company|co|ltd|llc|the)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


ACCOUNT_TYPE_FIELD = "audf_0timw0xX6CfUdJXJznM"


def resolve_domain(org, cache, use_clay):
    """Org name -> (domain, SF account type) via the heat domain cache, then an Audiences org_name
    search that must match the cleaned name exactly (Capita must not resolve to Capital Group)."""
    key = (org or "").lower().strip()
    for k in (key, clean_org(org).lower()):
        if k in cache and isinstance(cache[k], str) and cache[k]:
            return cache[k], (cache.get("acct|" + cache[k]) or "")
    if not use_clay:
        return "", ""
    name = clean_org(org)
    flt = {"type": "GroupOp", "combinationMode": "And", "items": [{
        "type": "BinOp", "key": "org_name", "dataPath": ["account_entity_field_values", "field", "org_name"],
        "operator": "Contain", "value": name, "entityType": "ACCOUNT"}]}
    try:
        r = json.loads(subprocess.run([clay_bin(), "audiences", "records", "search-ids", "--entity-type", "companies",
                                       "--filter", json.dumps(flt), "--limit", "10"], capture_output=True, text=True, timeout=90).stdout)
        ids = r.get("data") or []
        dom, atype = "", ""
        if ids:
            g = json.loads(subprocess.run([clay_bin(), "audiences", "records", "get", "--entity-type", "companies",
                                           "--ids", ",".join(str(i) for i in ids)], capture_output=True, text=True, timeout=90).stdout)
            want = name_key(name)
            for x in g.get("data") or []:
                f = x.get("fields") or {}
                if name_key(f.get("org_name")) == want:
                    dom = norm_domain(f.get("normalized_domain") or f.get("domain"))
                    atype = f.get(ACCOUNT_TYPE_FIELD) or ""
                    break
        cache[key] = dom
        if dom:
            cache["acct|" + dom] = atype
        return dom, atype
    except Exception:
        return "", ""


def parse_row(raw):
    """Tolerate the staged file's drift: find the URL, the quote, the date wherever they landed."""
    vals = [v for v in raw.values() if v]
    url = next((v.strip() for v in [raw.get("url", "")] + vals if isinstance(v, str) and v.strip().startswith("http")), "")
    date = ""
    for v in [raw.get("fiscal_period", ""), raw.get("retrieved_date", "")] + vals:
        if not isinstance(v, str):
            continue
        m = re.search(r"(20\d\d-\d\d-\d\d)", v)
        if m:
            date = m.group(1)
            break
        m = re.search(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? \d{1,2},? 20\d\d)", v)
        if m:
            try:
                date = datetime.datetime.strptime(re.sub(r"(\w{3})\w*\.? (\d{1,2}),? (\d{4})", r"\1 \2 \3", m.group(1)), "%b %d %Y").date().isoformat()
                break
            except ValueError:
                pass
    quote = (raw.get("verbatim_quote") or "").strip()
    if len(quote) < 15:
        quote = max((v for v in vals if isinstance(v, str) and not v.startswith("http")), key=len, default="").strip()
    return url, date, quote


def classify(raw, quote):
    """Score every family: a match in the verbatim quote counts 2, in the angle/source line 1.
    Ties go to the earlier rule (verint, Stars, leadership, cost, hiring, expansion, service)."""
    meta = " ".join(str(raw.get(k, "")) for k in ("angle_line", "source_type"))
    if re.search(PARK_PATTERNS, meta + " " + quote + " " + str(raw.get("parent_org", ""))):
        return "", "parked: war room marked it non-target or off-thesis"
    best, best_score = "", 0
    for fam, pat in FAMILY_RULES:
        score = (2 if re.search(pat, quote, flags=re.I | re.S) else 0) + (1 if re.search(pat, meta, flags=re.I | re.S) else 0)
        if score > best_score:
            best, best_score = fam, score
    return (best, "") if best_score >= 2 else ("", "parked: no trigger family matched in the quote itself (needs a hand: resolve --family)")


def customer_match(org, domain, deny):
    if domain and domain in set(deny.get("domains", [])):
        return True
    n = re.sub(r"[^a-z0-9 ]", " ", (org or "").lower())
    return any(re.search(r"\b" + re.escape(a) + r"\b", n) for a in deny.get("name_aliases", []))


def sync(a):
    today = datetime.date.today()
    ledger = load_json(a.ledger, {"_doc": "Signal review ledger (automation/signal_review.py). States: unreviewed, approved, denied. Approve or deny by replying APPROVE <id> / DENY <id> in the rundown thread.", "signals": [], "parked": []})
    by_id = {s["id"]: s for s in ledger["signals"]}
    parked_ids = {p["id"] for p in ledger["parked"]}
    cache = load_json(a.domain_cache or DOMAIN_CACHE, {})
    deny = load_json(DENYLIST, {"domains": [], "name_aliases": []})
    new, parked_new = [], []
    try:
        rows = list(csv.DictReader(open(a.staged, newline="")))
    except OSError:
        rows = []
    for raw in rows:
        org = (raw.get("parent_org") or "").strip()
        url, date, quote = parse_row(raw)
        if not org or not (url or quote):
            continue
        sid = "sig-" + (date.replace("-", "") if date else "nodate") + "-" + slug(clean_org(org))[:18] + "-" + hashlib.sha1((url + quote[:80]).encode()).hexdigest()[:6]
        if sid in by_id or sid in parked_ids:
            continue
        fam, park = classify(raw, quote)
        domain, account_type = resolve_domain(org, cache, not a.no_clay)
        entry = {"id": sid, "org": org, "domain": domain, "trigger_type": fam, "date": date, "quote": quote[:400], "url": url,
                 "source_type": (raw.get("source_type") or "")[:80], "angle": (raw.get("angle_line") or "")[:200],
                 "staged_on": (raw.get("retrieved_date") or "")[:10], "seen": today.isoformat()}
        if not park:
            if not url:
                park = "parked: no URL"
            elif not date:
                park = "parked: no parsable date"
            elif customer_match(org, domain, deny) or account_type == "Customer":
                park = "parked: customer (denylist or SF Account Type)"
            elif not domain:
                park = "parked: no domain resolved (not in Audiences)"
        if park or not fam:
            entry["reason"] = park or "parked: no trigger family matched (needs a hand)"
            ledger["parked"].append(entry)
            parked_new.append(entry)
        else:
            entry["state"] = "unreviewed"
            entry["detail"] = ""
            ledger["signals"].append(entry)
            new.append(entry)
    ledger["updated"] = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    json.dump(ledger, open(a.ledger, "w"), indent=1)
    if not a.no_clay:
        try:
            json.dump(cache, open(a.domain_cache or DOMAIN_CACHE, "w"))
        except OSError:
            pass
    pending = [s for s in ledger["signals"] if s.get("state") == "unreviewed"]
    lines = [f"# {LOG_FAMILY} {today.isoformat()}", "",
             f"Ran {ledger['updated']}: {len(rows)} staged rows read, {len(new)} new unreviewed, {len(parked_new)} newly parked, "
             f"{len(pending)} awaiting review, {sum(1 for s in ledger['signals'] if s.get('state') == 'approved')} approved, "
             f"{sum(1 for s in ledger['signals'] if s.get('state') == 'denied')} denied.", ""]
    if pending:
        lines += ["## Awaiting review (reply APPROVE <id> or DENY <id> in the rundown thread)", ""]
        for s in pending:
            lines.append(f"- {s['id']} | {s['org']} ({s['domain']}) | {s['trigger_type']} | {s['date']} | \"{s['quote'][:140]}\" | {s['url']}")
            if s in new:
                lines.append(f"  evt: {LOG_FAMILY}-{today.isoformat()}#{s['id']}")
    else:
        lines += ["## Awaiting review", "", "- none"]
    if parked_new:
        lines += ["", "## Parked this run (not served, needs a hand or is out of scope)", ""]
        lines += [f"- {p['id']} | {p['org']} | {p['reason']}" for p in parked_new]
    log_path = a.log or os.path.join(HERE, "logs", f"{LOG_FAMILY}-{today.isoformat()}.md")
    with open(log_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[:4]))
    print(f"ledger {a.ledger}; log {log_path}")
    return 0


def decide(a):
    ledger = load_json(a.ledger, None)
    if not ledger:
        print("no ledger", file=sys.stderr)
        return 2
    hit = next((s for s in ledger["signals"] if s["id"] == a.id), None)
    if not hit:
        print(f"unknown signal id {a.id}", file=sys.stderr)
        return 2
    hit["state"] = a.state
    hit["decided_at"] = datetime.date.today().isoformat()
    hit["decided_via"] = a.via or "cli"
    ledger["updated"] = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    json.dump(ledger, open(a.ledger, "w"), indent=1)
    print(f"{a.id} -> {a.state} ({hit['org']}, {hit['trigger_type']}, {hit['date']})")
    return 0


def resolve(a):
    """Set the domain (and optionally the family) on a parked or live signal by hand, un-parking it."""
    ledger = load_json(a.ledger, None)
    if not ledger:
        print("no ledger", file=sys.stderr)
        return 2
    hit = next((s for s in ledger["signals"] if s["id"] == a.id), None)
    parked = next((p for p in ledger["parked"] if p["id"] == a.id), None)
    if not hit and not parked:
        print(f"unknown signal id {a.id}", file=sys.stderr)
        return 2
    e = hit or parked
    if a.domain:
        e["domain"] = norm_domain(a.domain)
    if a.family:
        e["trigger_type"] = a.family
    if parked and e.get("domain") and e.get("trigger_type") and e.get("url") and e.get("date"):
        ledger["parked"] = [p for p in ledger["parked"] if p["id"] != a.id]
        e.pop("reason", None)
        e["state"], e["detail"] = "unreviewed", e.get("detail", "")
        ledger["signals"].append(e)
    ledger["updated"] = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    json.dump(ledger, open(a.ledger, "w"), indent=1)
    print(f"{a.id}: domain={e.get('domain')} family={e.get('trigger_type')} state={e.get('state', 'parked')}")
    return 0


def pending(a):
    ledger = load_json(a.ledger, {"signals": []})
    for s in ledger["signals"]:
        if s.get("state") == "unreviewed":
            print(f"{s['id']} | {s['org']} | {s['trigger_type']} | {s['date']} | {s['quote'][:120]} | {s['url']}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync"); s.add_argument("--no-clay", action="store_true"); s.add_argument("--staged", default=STAGED); s.add_argument("--ledger", default=LEDGER); s.add_argument("--log"); s.add_argument("--domain-cache")
    d = sub.add_parser("decide"); d.add_argument("--id", required=True); d.add_argument("--state", required=True, choices=["approved", "denied", "unreviewed"]); d.add_argument("--via"); d.add_argument("--ledger", default=LEDGER)
    p = sub.add_parser("pending"); p.add_argument("--ledger", default=LEDGER)
    r = sub.add_parser("resolve"); r.add_argument("--id", required=True); r.add_argument("--domain"); r.add_argument("--family"); r.add_argument("--ledger", default=LEDGER)
    a = ap.parse_args()
    return {"sync": sync, "decide": decide, "pending": pending, "resolve": resolve}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
