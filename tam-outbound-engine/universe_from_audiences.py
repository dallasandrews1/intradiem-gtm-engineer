#!/usr/bin/env python3
"""Build the strike universe from a saved Clay Audiences segment at build time (0 credits).

Regenerates data/tam_accounts.csv and data/sellers.csv and MERGES data/triggers.csv from:
  - the Audiences company record (employee_count, industry, SF owner, CC/WFM platform reads),
  - data/account_facts.json (sourced facts from the weekly refresh; they override and cite),
  - config/sf_owners.json (SF owner id -> seller),
  - automation/config/signal_reviews.json (approved war-room signals -> cited triggers).

Provenance rule is unchanged: every row gets a `source`; agent_count is a public figure when the
facts ledger has one, else a banded ESTIMATE that says so. account_engine.is_seed still gates.

Usage:
    python3 universe_from_audiences.py                 # build into data/ (per config/universe.json)
    python3 universe_from_audiences.py --dry-run       # build into data/_universe_dryrun/ and report
    python3 universe_from_audiences.py --fixture f.json  # offline: records from a JSON fixture
    python3 universe_from_audiences.py --create-segment  # create the saved segment once, write its id

Fails closed: any Clay error leaves data/ untouched and exits 2, so the last good universe keeps
serving (the generator records `universe: stale`).
"""
import argparse
import csv
import datetime
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CFG_PATH = os.path.join(HERE, "config", "universe.json")
IND_MAP = os.path.join(HERE, "config", "audiences_industry_map.json")
VENDORS = os.path.join(HERE, "config", "tech_vendors.json")
OWNERS = os.path.join(HERE, "config", "sf_owners.json")
FACTS = os.path.join(HERE, "data", "account_facts.json")
REVIEWS = os.path.join(ROOT, "automation", "config", "signal_reviews.json")
ACCOUNT_COLS = ["domain", "company", "industry", "employees", "agent_count", "acd", "acd_source", "acd_observed",
                "wfm", "wfm_source", "wfm_observed", "source", "sf_owner_id", "sixsense_stage", "sixsense_intent",
                "heat_lane", "heat_score"]
TRIGGER_COLS = ["domain", "trigger_type", "detail", "date", "source"]
SELLER_COLS = ["domain", "seller_name", "seller_email", "seller_slack"]
AGGREGATORS = ("layoffhedge.com", "theofficialboard.com", "rocketreach.co", "nerdwallet.com", "zoominfo.com",
               "craft.co", "wikipedia.org")


def load_json(p, default=None):
    try:
        with open(p) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def clay_bin():
    for c in (os.environ.get("CLAY_BIN"), "clay"):
        if not c:
            continue
        b = subprocess.run(["zsh", "-lc", f"command -v {c}"], capture_output=True, text=True).stdout.strip()
        if b:
            return b
    cands = sorted(__import__("glob").glob(os.path.expanduser("~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")))
    return cands[-1] if cands else "clay"


def clay(*args, timeout=120):
    out = subprocess.run([clay_bin(), *args], capture_output=True, text=True, timeout=timeout)
    try:
        d = json.loads(out.stdout)
    except ValueError:
        raise RuntimeError(f"clay {' '.join(args[:3])}: non-JSON output: {(out.stdout or out.stderr)[:200]}")
    if isinstance(d, dict) and d.get("error"):
        raise RuntimeError(f"clay {' '.join(args[:3])}: {d['error']}")
    return d


def norm_domain(v):
    v = (v or "").strip().lower()
    v = re.sub(r"^https?://", "", v).split("/")[0]
    return re.sub(r"^www\.", "", v)


def band(n):
    return next(pts for lo, pts in [(10000, 25), (5000, 22), (2500, 18), (1000, 12), (0, 5)] if n >= lo)


def segment_filter(cfg):
    f = cfg["fields"]

    def b(key, op, val):
        return {"type": "BinOp", "key": key, "dataPath": ["account_entity_field_values", "field", key],
                "operator": op, "value": val, "entityType": "ACCOUNT"}
    return {"type": "GroupOp", "combinationMode": "And", "items": [
        b(f["account_type"], "Equal", "Prospect"),
        b("employee_count", "GreaterThanOrEqual", cfg["min_employees"]),
        {"type": "GroupOp", "combinationMode": "Or", "items": [b("industry", "Equal", v) for v in cfg["icp_industries"]]},
        {"type": "GroupOp", "combinationMode": "Or", "items": [
            *([b(f["cc_platform_last_seen"], "GreaterThanOrEqual", (datetime.date.today() - datetime.timedelta(days=cfg.get("read_max_age_days", 365))).isoformat())] if cfg.get("include_platform_reads") else []),
            b(f["sixsense_6qa"], "True", ""),
            b(f["heat_lane"], "Equal", "rep"),
            b(f["heat_lane"], "Equal", "cohort"),
        ]},
    ]}


def fetch_records(cfg):
    seg = cfg["segment"]["id"]
    ids, cursor = [], None
    while True:
        args = ["audiences", "records", "search-ids", "--entity-type", "companies", "--limit", "500"]
        args += ["--audience-id", seg] if seg else ["--filter", json.dumps(segment_filter(cfg))]
        if cursor:
            args += ["--cursor", cursor]
        r = clay(*args)
        ids += r.get("data", [])
        cursor = r.get("cursor")
        if not cursor or len(ids) > 20000:
            break
    recs = []
    for i in range(0, len(ids), 100):
        g = clay("audiences", "records", "get", "--entity-type", "companies", "--ids", ",".join(str(x) for x in ids[i:i + 100]))
        for x in g.get("data", []):
            recs.append({"id": x.get("recordId"), **(x.get("fields") or {})})
    return recs


def fetch_facts_backed(cfg, facts, have, today):
    """Accounts with a fresh filing-grade fact or a fresh trigger in the ledger stay in the universe even
    when the segment's intent filter drops them (research is not thrown away by a filter tweak).
    Still Prospect-only: the record's SF Account Type is checked, customers never enter."""
    max_age = cfg.get("facts_max_age_days", 90)
    want = []
    for dom, f in facts.items():
        if dom in have or dom in cfg.get("exclude_domains", {}):
            continue
        try:
            age = (today - datetime.date.fromisoformat(f.get("facts_updated", "1970-01-01"))).days
        except ValueError:
            continue
        fresh_fact = bool((f.get("employees") or {}).get("url")) and age <= max_age
        fresh_trig = any((today - datetime.date.fromisoformat(t["date"][:10])).days <= 120 for t in f.get("triggers", []) if t.get("date"))
        if fresh_fact and (fresh_trig or (f.get("employees") or {}).get("value")):
            want.append(dom)
    out = []
    for dom in want:
        flt = {"type": "GroupOp", "combinationMode": "And", "items": [{
            "type": "BinOp", "key": "normalized_domain", "dataPath": ["account_entity_field_values", "field", "normalized_domain"],
            "operator": "Contain", "value": dom, "entityType": "ACCOUNT"}]}
        r = clay("audiences", "records", "search-ids", "--entity-type", "companies", "--filter", json.dumps(flt), "--limit", "3")
        ids = r.get("data") or []
        if not ids:
            continue
        g = clay("audiences", "records", "get", "--entity-type", "companies", "--ids", ",".join(str(i) for i in ids))
        for x in g.get("data") or []:
            fl = x.get("fields") or {}
            if norm_domain(fl.get("normalized_domain") or fl.get("domain")) == dom and (fl.get(cfg["fields"]["account_type"]) or "") == "Prospect":
                out.append({"id": x.get("recordId"), "_facts_backed": True, **fl})
                break
    return out


def parse_platforms(s, canon, lane):
    best = {"acd": None, "wfm": None}
    for m in re.finditer(r"([^,()]+?)\s*\((\d{4}-\d{2}-\d{2})\)", s or ""):
        raw, d = m.group(1).strip(), m.group(2)
        ln = "acd" if raw in lane["acd"] else "wfm" if raw in lane["wfm"] else None
        if ln and (best[ln] is None or d > best[ln][1]):
            best[ln] = (canon.get(raw, raw), d)
    return best


def build_rows(recs, cfg, facts, owners, today):
    ind_map = load_json(IND_MAP, {"map": {}, "default": "Other"})
    vend = load_json(VENDORS, {"canonical": {}, "lane": {"acd": [], "wfm": []}})
    f = cfg["fields"]
    accounts, sellers, report = [], [], {"unmapped_owner_ids": {}, "excluded": [], "facts_used": 0, "estimates": 0, "stale_facts": 0}
    max_age = cfg.get("facts_max_age_days", 90)
    for r in recs:
        dom = norm_domain(r.get("normalized_domain") or r.get("domain"))
        if not dom:
            continue
        if dom in cfg.get("exclude_domains", {}):
            report["excluded"].append(f"{dom}: {cfg['exclude_domains'][dom]}")
            continue
        industry = ind_map["map"].get((r.get("industry") or "").strip(), ind_map.get("default", "Other"))
        fact = (facts.get(dom) or {})
        try:
            aud_emp = int(float(r.get("employee_count") or 0))
        except (TypeError, ValueError):
            aud_emp = 0
        fe = fact.get("employees") or {}
        fact_age = None
        if fact.get("facts_updated"):
            try:
                fact_age = (today - datetime.date.fromisoformat(fact["facts_updated"])).days
            except ValueError:
                fact_age = None
        fresh_fact = fe.get("value") and fe.get("url") and (fact_age is not None and fact_age <= max_age)
        if fe.get("value") and fe.get("url") and not fresh_fact:
            report["stale_facts"] += 1
        if fresh_fact:
            employees = int(fe["value"])
            emp_src = (f"employees {employees:,} as of {fe.get('as_of', '')} per {fe['url']} "
                       f"(\"{(fe.get('quote') or '').strip()}\", facts_updated {fact['facts_updated']})")
            report["facts_used"] += 1
        elif aud_emp > 0:
            employees = aud_emp
            emp_src = (f"employees {employees:,} per the Clay Audiences company record (employee_count, "
                       f"record updated {str(r.get('updated_at', ''))[:10]}, read {today.isoformat()}); no filing-grade fact on file")
        else:
            report["excluded"].append(f"{dom}: no employee count on the Audiences record and no fact")
            continue
        if fact.get("industry") in ind_map["map"].values():
            industry = fact["industry"]
        cc = fact.get("contact_center") or {}
        if cc.get("value") and cc.get("url"):
            agents = int(cc["value"])
            agent_note = f"agent_count {agents:,} is a PUBLIC figure: {cc.get('basis', '')} ({cc['url']})"
        else:
            ratio = cfg["agent_ratio"].get("by_domain", {}).get(dom, cfg["agent_ratio"].get(industry, cfg["agent_ratio"]["Other"]))
            agents = max(100, int(round(employees * ratio / 100.0)) * 100)
            lo, hi = band(int(agents * 0.7)), band(int(agents * 1.3))
            agent_note = (f"agent_count {agents:,} is a banded ESTIMATE, not a disclosed figure: employees x {ratio:.2f} "
                          f"({industry}); scale band {'robust' if lo == hi else 'SENSITIVE'} at +/-30% ({lo} vs {hi} pts)")
            report["estimates"] += 1
        plat = parse_platforms(r.get(f["cc_platforms_all"], ""), vend["canonical"], vend["lane"])
        row = {"domain": dom, "company": (fact.get("company") or r.get("org_name") or dom), "industry": industry,
               "employees": employees, "agent_count": agents, "sf_owner_id": r.get("sfdc_owner_id", ""),
               "sixsense_stage": r.get(f["sixsense_stage"], ""), "sixsense_intent": r.get(f["sixsense_intent"], ""),
               "heat_lane": r.get(f["heat_lane"], ""), "heat_score": r.get(f["heat_score"], "")}
        for lane in ("acd", "wfm"):
            if plat[lane]:
                v, d = plat[lane]
                row[lane], row[f"{lane}_source"], row[f"{lane}_observed"] = v, f"predictleads:{cfg['vendor_urls'].get(v, '')}", d
            else:
                row[lane], row[f"{lane}_source"], row[f"{lane}_observed"] = "Unknown", "", ""
        src = f"{emp_src}. {agent_note}."
        if fact.get("notes"):
            src += f" Note: {fact['notes']}"
        row["source"] = src
        accounts.append(row)
        ov = (owners.get("_overrides_by_domain") or {}).get(dom)
        own = ov or owners.get(r.get("sfdc_owner_id") or "", {})
        if own and own.get("seller_name"):
            sellers.append({"domain": dom, "seller_name": own["seller_name"], "seller_email": own.get("seller_email", ""),
                            "seller_slack": own.get("seller_slack", "")})
        elif r.get("sfdc_owner_id"):
            report["unmapped_owner_ids"].setdefault(r["sfdc_owner_id"], []).append(dom)
    accounts.sort(key=lambda a: a["domain"])
    return accounts, sellers, report


def merge_triggers(existing, domains, facts, reviews, today):
    """Union of existing rows, facts-ledger triggers and APPROVED signals, keyed by (domain, type, date). Never deletes."""
    key = lambda t: (t["domain"], t["trigger_type"], t["date"])
    out = {key(t): t for t in existing if t.get("domain")}
    added = 0
    for dom in domains:
        for t in (facts.get(dom) or {}).get("triggers") or []:
            if not (t.get("url") and t.get("quote") and t.get("date") and t.get("trigger_type")):
                continue
            if any(a in t["url"] for a in AGGREGATORS):
                continue
            row = {"domain": dom, "trigger_type": t["trigger_type"], "detail": t.get("detail", ""), "date": t["date"],
                   "source": f"{t['quote'].strip()} ({t['url']}, retrieved {(facts.get(dom) or {}).get('facts_updated', today.isoformat())})"}
            if key(row) not in out:
                out[key(row)] = row
                added += 1
    for s in (reviews or {}).get("signals", []):
        if s.get("state") != "approved" or s.get("domain") not in domains:
            continue
        row = {"domain": s["domain"], "trigger_type": s["trigger_type"], "detail": s.get("detail", ""), "date": s["date"],
               "source": f"{s['quote'].strip()} ({s['url']}; approved {s.get('decided_at', '')} via rundown thread, {s['id']})"}
        if key(row) not in out:
            out[key(row)] = row
            added += 1
    rows = sorted(out.values(), key=lambda t: (t["domain"], t["date"]))
    return rows, added


def write_csv(path, cols, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--fixture", help="JSON list of Audiences company records (offline)")
    ap.add_argument("--create-segment", action="store_true")
    ap.add_argument("--update-segment", action="store_true", help="push segment_filter(cfg) to the saved segment")
    ap.add_argument("--out", help="output dir (default data/, or data/_universe_dryrun with --dry-run)")
    a = ap.parse_args()
    cfg = load_json(CFG_PATH)
    if not cfg:
        print("config/universe.json missing or invalid", file=sys.stderr)
        return 2
    today = datetime.date.today()
    if a.create_segment:
        r = clay("audiences", "create", "--entity-type", "companies", "--name", cfg["segment"]["name"],
                 "--description", "Strike universe read by tam-outbound-engine/universe_from_audiences.py at build time. Edit this filter to shape the universe.",
                 "--filter", json.dumps(segment_filter(cfg)))
        sid = (r.get("data") or r).get("id")
        cfg["segment"]["id"] = sid
        json.dump(cfg, open(CFG_PATH, "w"), indent=2)
        print(f"segment created: {sid} -> written to config/universe.json")
        return 0
    if a.update_segment:
        clay("audiences", "update", cfg["segment"]["id"], "--filter", json.dumps(segment_filter(cfg)))
        n = clay("audiences", "records", "search-count", "--entity-type", "companies", "--audience-id", cfg["segment"]["id"])
        print(f"segment {cfg['segment']['id']} filter updated; now {n.get('count')} companies")
        return 0
    if cfg.get("source") != "audiences" and not a.fixture:
        print("universe.json source is not 'audiences'; nothing regenerated")
        return 0
    out_dir = a.out or (os.path.join(HERE, "data", "_universe_dryrun") if a.dry_run else os.path.join(HERE, "data"))
    os.makedirs(out_dir, exist_ok=True)
    facts = (load_json(FACTS, {}) or {}).get("facts", {})
    try:
        recs = json.load(open(a.fixture)) if a.fixture else fetch_records(cfg)
        if not a.fixture and cfg.get("include_facts_backed", True):
            recs += fetch_facts_backed(cfg, facts, {norm_domain(r.get("normalized_domain") or r.get("domain")) for r in recs}, today)
    except Exception as e:  # fail closed: leave the last universe in place
        print(f"UNIVERSE FETCH FAILED, data/ untouched: {e}", file=sys.stderr)
        return 2
    owners = load_json(OWNERS, {}) or {}
    reviews = load_json(REVIEWS, {}) or {}
    accounts, sellers, report = build_rows(recs, cfg, facts, owners, today)
    if not accounts:
        print("UNIVERSE EMPTY, data/ untouched", file=sys.stderr)
        return 2
    existing = []
    tpath = os.path.join(HERE, "data", "triggers.csv")
    if os.path.exists(tpath):
        with open(tpath, newline="") as f:
            existing = list(csv.DictReader(f))
    domains = {x["domain"] for x in accounts}
    triggers, added = merge_triggers(existing, domains, facts, reviews, today)
    write_csv(os.path.join(out_dir, "tam_accounts.csv"), ACCOUNT_COLS, accounts)
    write_csv(os.path.join(out_dir, "sellers.csv"), SELLER_COLS, sellers)
    write_csv(os.path.join(out_dir, "triggers.csv"), TRIGGER_COLS, triggers)
    facts_backed = sum(1 for r in recs if r.get("_facts_backed"))
    summary = {"built_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z", "records": len(recs),
               "accounts": len(accounts), "sellers": len(sellers), "triggers": len(triggers), "triggers_added": added,
               "segment_id": cfg["segment"]["id"], "facts_backed_added": facts_backed, "out_dir": out_dir, **report}
    json.dump(summary, open(os.path.join(out_dir, "universe_build.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "unmapped_owner_ids"}, indent=1))
    if report["unmapped_owner_ids"]:
        print("unmapped SF owner ids (fill config/sf_owners.json):")
        for k, v in report["unmapped_owner_ids"].items():
            print(f"  {k}: {len(v)} accounts, e.g. {', '.join(v[:3])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
