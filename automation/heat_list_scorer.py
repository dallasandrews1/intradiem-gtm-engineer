#!/usr/bin/env python3
"""heat-list-scorer: the signal-marketing loop's scoring job.

Reads every intent source we already have (Clay Website Intent table, lemlist relay
log, war-room staged signals, TAM triggers.csv, webinar routes stamped on Audiences),
scores each company against the TAM engine's trigger taxonomy (config/triggers.json,
per-family decay), assigns a lane, and:

  - stamps the five Clay Heat fields on the Audiences COMPANY record through the
    "Heat Stamp" workflow's webhook (live_stamp=true only),
  - fires Lane A (rep alert with Approve/Deny in the rep's Slack channel) through the
    "Heat Lane A" workflow's webhook (live_lane_a=true only),
  - writes automation/logs/heat-list-<date>.md, which the daily rundown reads.

DRY RUN BY DEFAULT (automation/config/heat_loop.json: dry_run=true). In dry run nothing
leaves this machine except read-only Clay CLI calls (0 credits). Everything that would
have been posted is written verbatim to the log.

Never DMs anyone. Never sends email. Never touches Salesforce. Never spends a credit.
Config over code: weights, decay, page classes, thresholds, ids all live in config.

Usage:
    python3 automation/heat_list_scorer.py            # scheduled run (dry unless config says live)
    python3 automation/heat_list_scorer.py --dry-run  # force dry run regardless of config
    python3 automation/heat_list_scorer.py --domain molinahealthcare.com   # score one company, print
"""
import argparse
import csv
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta

AUTO_DIR = os.path.dirname(os.path.abspath(__file__))          # .../automation (untracked; lives in the main checkout)
MAIN = os.path.dirname(AUTO_DIR)                                 # the main repo root: config, logs, state, cohort files
ROOT = os.environ.get("HEAT_ROOT") or MAIN                       # engine config root; HEAT_ROOT points at a worktree until merge
CFG_PATH = os.path.join(AUTO_DIR, "config", "heat_loop.json")
TRIG_PATH = os.path.join(ROOT, "tam-outbound-engine", "config", "triggers.json")
WEB_PATH = os.path.join(ROOT, "tam-outbound-engine", "config", "web_intent.json")
LOG_DIR = os.path.join(AUTO_DIR, "logs")


def P(rel):
    """Resolve a repo-relative path: automation/ and motions/ against the main checkout, engine data against ROOT."""
    base = MAIN if rel.startswith(("automation/", "motions/")) else ROOT
    return os.path.join(base, rel)
TODAY = date.today()
LOG_FAMILY = "heat-list"


# ---------------------------------------------------------------- helpers
def load(p):
    with open(p) as f:
        return json.load(f)


def clay_bin():
    b = subprocess.run(["zsh", "-lc", "command -v clay"], capture_output=True, text=True).stdout.strip()
    if b:
        return b
    cands = sorted(glob.glob(os.path.expanduser("~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")))
    return cands[-1] if cands else "clay"


CLAY = clay_bin()


def clay(*args, timeout=120):
    """Run a Clay CLI command, return parsed JSON or {"_error": ...}. Read-only unless stated."""
    try:
        out = subprocess.run([CLAY, *args], capture_output=True, text=True, timeout=timeout)
        return json.loads(out.stdout, strict=False)
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)[:200]}


def norm_domain(x):
    if not x:
        return ""
    x = str(x).strip().lower()
    x = re.sub(r"^https?://", "", x)
    x = re.sub(r"^www\.", "", x)
    return x.split("/")[0].split("?")[0]


def parse_date(s):
    if not s:
        return None
    s = str(s).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s[: len(fmt) + (7 if "%f" in fmt else 0)], fmt).date()
        except ValueError:
            continue
    m = re.search(r"(20\d\d-\d\d-\d\d)", s)
    return datetime.strptime(m.group(1), "%Y-%m-%d").date() if m else None


def recency_factor(d, rec, today=TODAY):
    days = (today - d).days
    if days <= rec["fresh_days"]:
        return 1.0
    if days >= rec["stale_days"]:
        return rec["stale_floor"]
    span = rec["stale_days"] - rec["fresh_days"]
    return round(1.0 - (1.0 - rec["stale_floor"]) * (days - rec["fresh_days"]) / span, 3)


def slug(domain):
    return re.sub(r"[^a-z0-9]+", "-", domain.lower()).strip("-")[:40]


# ---------------------------------------------------------------- state
class State:
    def __init__(self, path):
        self.path = path
        try:
            self.d = load(path)
        except Exception:  # noqa: BLE001
            self.d = {"first_seen": {}, "alerted": {}, "lane": {}}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.d, f, indent=1)


# ---------------------------------------------------------------- sources
def events_from_web_intent(cfg, web):
    """Sessions from the Clay Website visitor tracking table -> events. 0 credits (rows list).

    Verified shape (t_0tkbo3tEWnp4abaaaTb, 2026-08-25, one row per visit): the source column's cell value is an
    object with .domain and .websiteEvents (a list; each event carries .path plus, per Clay's docs, timing,
    referrer and UTM fields whose exact keys we read defensively). Row Created At is the visit date fallback."""
    wi = cfg["web_intent"]
    tid = (wi.get("table_id") or "").strip()
    if not tid:
        return [], ["web intent: table id not set in automation/config/heat_loop.json (pixel step pending), source skipped"]
    src_col, dom_col, created_col = wi.get("source_column"), wi.get("domain_column"), wi.get("created_at_column", "f_created_at")
    if not src_col:
        cols = clay("tables", "columns", "get", tid)
        for c in (cols.get("data", cols.get("columns", [])) if isinstance(cols, dict) else []):
            if c.get("type") == "source":
                src_col = c.get("id")
            if "domain" in (c.get("name") or "").lower():
                dom_col = dom_col or c.get("id")
    notes, rows, cursor, pages = [], [], None, 0
    while True:
        r = clay("tables", "rows", "list", tid, "--limit", "100", *(["--cursor", cursor] if cursor else []))
        if "_error" in r:
            notes.append(f"web intent: rows read stopped: {r['_error']}")
            break
        rows.extend(r.get("data", []))
        cursor = r.get("cursor")
        pages += 1
        if not cursor or pages > 60:
            break

    def cell(row, cid):
        c = (row.get("cells") or {}).get(cid) or {}
        return c.get("value")

    def first_key(obj, *needles):
        for k, v in (obj or {}).items():
            if any(n in k.lower() for n in needles) and v not in (None, ""):
                return v
        return None

    sessions, unkeyed = [], set()
    for row in rows:
        src = cell(row, src_col) if src_col else None
        if isinstance(src, str):
            try:
                src = json.loads(src)
            except ValueError:
                src = {}
        src = src or {}
        d = norm_domain(src.get("domain") or (cell(row, dom_col) if dom_col else ""))
        if not d:
            continue
        events = src.get("websiteEvents") or src.get("events") or []
        paths = [str(e.get("path") or e.get("url") or "") for e in events if isinstance(e, dict)]
        paths = [re.sub(r"^https?://[^/]+", "", p) or "/" for p in paths if p] or ["/"]
        ev0 = events[0] if events and isinstance(events[0], dict) else {}
        for k in ev0:
            unkeyed.add(k)
        when = (parse_date(first_key(ev0, "time", "date", "occurred", "start")) or parse_date(first_key(src, "time", "date", "start"))
                or parse_date(cell(row, created_col)) or parse_date(row.get("updatedAt")) or TODAY)
        sessions.append({
            "domain": d, "paths": paths, "date": when,
            "referrer": str(first_key(ev0, "referr") or first_key(src, "referr") or ""),
            "utm_source": str(first_key(ev0, "utm_source", "utmsource") or first_key(src, "utm_source", "utmsource") or ""),
            "utm_campaign": str(first_key(ev0, "utm_campaign", "utmcampaign") or first_key(src, "utm_campaign", "utmcampaign") or ""),
            "utm_medium": str(first_key(ev0, "utm_medium", "utmmedium") or first_key(src, "utm_medium", "utmmedium") or ""),
        })
    notes.append(f"web intent: {len(rows)} rows read from {tid}, {len(sessions)} visits with a domain"
                 + (f"; event keys seen: {sorted(unkeyed)}" if unkeyed else "; no events yet (pixel not live or no visitors)"))
    return classify_sessions(sessions, web), notes


def classify_sessions(sessions, web):
    classes = {k: [re.compile(p, re.I) for p in v] for k, v in web["classes"].items()}
    ignore = [re.compile(p, re.I) for p in web["ignore_paths"]]
    hints = [(re.compile(k, re.I), v) for k, v in web.get("product_page_hint", {}).items()]
    fu = web["from_us"]
    events = []
    by_domain = defaultdict(list)
    for s in sessions:
        by_domain[s["domain"]].append(s)
    for d, ss in by_domain.items():
        ss.sort(key=lambda x: x["date"])
        for i, s in enumerate(ss):
            fams, topics = set(), []
            for p in s["paths"]:
                if any(rx.search(p) for rx in ignore):
                    continue
                for fam in ("web_product", "web_proof", "web_content"):
                    if any(rx.search(p) for rx in classes[fam]):
                        fams.add(fam)
                        break
                for rx, hint in hints:
                    if rx.search(p) and hint not in topics:
                        topics.append(hint)
            from_us = (
                any(k in s["utm_source"].lower() for k in fu["utm_source_any"])
                or any(s["utm_campaign"].startswith(pfx) for pfx in fu["utm_campaign_prefix"])
                or any(k in s["referrer"].lower() for k in fu["referrer_contains"])
            )
            if from_us:
                fams.add("web_from_us")
            returns = sum(1 for prev in ss[:i] if (s["date"] - prev["date"]).days <= web["web_return"]["window_days"])
            if returns >= 1:
                fams.add("web_return")
            for fam in fams:
                events.append({"domain": d, "family": fam, "date": s["date"],
                               "detail": (", ".join(topics) if topics else "; ".join(s["paths"][:3]))[:160],
                               "source": "web"})
    return events


def events_from_relay_logs(cfg):
    """lemlist relay dry-run/live logs -> click/reply events. Best effort: needs an email or domain in the line."""
    events, notes = [], []
    files = sorted(glob.glob(P(cfg["sources"]["relay_log_glob"])))[-14:]
    for f in files:
        d = parse_date(os.path.basename(f)) or TODAY
        try:
            txt = open(f, errors="ignore").read()
        except OSError:
            continue
        for line in txt.splitlines():
            low = line.lower()
            fam = None
            if "replied" in low or "reply" in low or "emailsreplied" in low:
                fam = "lemlist_reply"
            elif "click" in low:
                fam = "lemlist_click"
            if not fam:
                continue
            m = re.search(r"[\w.+-]+@([\w-]+(?:\.[\w-]+)+)", line)
            dom = norm_domain(m.group(1)) if m else ""
            if not dom:
                m2 = re.search(r"\b([a-z0-9-]+\.(?:com|net|org|co\.uk|ca|io|health|bank))\b", low)
                dom = norm_domain(m2.group(1)) if m2 else ""
            if dom and dom not in cfg["exclusion"]["personal_email_domains"]:
                events.append({"domain": dom, "family": fam, "date": d, "detail": line.strip()[:140], "source": "lemlist_relay"})
    notes.append(f"lemlist relay: {len(files)} log files scanned, {len(events)} click/reply events with a resolvable domain")
    return events, notes


def events_from_triggers_csv(cfg):
    events, notes = [], []
    p = P(cfg["sources"]["triggers_csv"])
    try:
        with open(p, newline="") as f:
            for r in csv.DictReader(f):
                d = parse_date(r.get("date"))
                if d:
                    events.append({"domain": norm_domain(r["domain"]), "family": r["trigger_type"], "date": d,
                                   "detail": (r.get("detail") or "")[:140], "source": "triggers_csv"})
        notes.append(f"triggers.csv: {len(events)} trigger rows")
    except OSError:
        notes.append("triggers.csv: not found")
    return events, notes


def events_from_staged_signals(cfg, cache):
    """War-room staged signals carry parent_org, not domain; resolve via Audiences org_name (0 credits) with a cache."""
    events, notes = [], []
    p = P(cfg["sources"]["staged_signals_csv"])
    try:
        rows = list(csv.DictReader(open(p, newline="", errors="ignore")))
    except OSError:
        return [], ["staged_signals.csv: not found"]
    unresolved = 0
    for r in rows:
        org = (r.get("parent_org") or "").strip()
        d = parse_date(r.get("retrieved_date"))
        if not org or not d or (TODAY - d).days > 120:
            continue
        dom = resolve_org_domain(org, cache)
        if not dom:
            unresolved += 1
            continue
        text = ((r.get("angle_line") or "") + " " + (r.get("source_type") or "")).lower()
        if any(k in text for k in ("severance", "cost", "efficiency", "layoff", "reduction", "margin")):
            fam = "cost_mandate"
        elif any(k in text for k in ("cfo", "cmo", "ceo", "coo", "chief", "appoint", "succession", "names ")):
            fam = "leadership_change"
        elif any(k in text for k in ("hiring", "workforce management", "wfm")):
            fam = "wfm_hiring"
        else:
            fam = "qbp_earnings_pressure"
        events.append({"domain": dom, "family": fam, "date": d, "detail": (r.get("angle_line") or "")[:140], "source": "war_room"})
    notes.append(f"staged_signals.csv: {len(rows)} rows, {len(events)} mapped to a domain, {unresolved} unresolved orgs (cached for next run)")
    return events, notes


def resolve_org_domain(org, cache):
    key = org.lower()
    if key in cache:
        return cache[key]
    needle = re.sub(r"\b(holdings?|inc|corp|corporation|company|group|plc|llc|co)\b\.?", "", key).strip()
    needle = needle.split(",")[0].strip()[:40]
    if len(needle) < 3:
        cache[key] = ""
        return ""
    flt = {"type": "GroupOp", "combinationMode": "And", "items": [{
        "type": "BinOp", "key": "org_name", "dataPath": ["account_entity_field_values", "field", "org_name"],
        "operator": "Contain", "value": needle, "entityType": "ACCOUNT"}]}
    r = clay("audiences", "records", "search-ids", "--entity-type", "companies", "--filter", json.dumps(flt))
    ids = (r.get("data") or [])[:5] if isinstance(r, dict) else []
    dom = ""
    if ids:
        g = clay("audiences", "records", "get", "--entity-type", "companies", "--ids", ",".join(str(i) for i in ids))
        for rec in (g.get("data") or []):
            f = rec.get("fields", {})
            cand = norm_domain(f.get("normalized_domain") or f.get("domain"))
            if cand:
                dom = cand
                break
    cache[key] = dom
    return dom


def events_from_webinar(cfg, state):
    """People stamped Clay Webinar Route=bdr_review -> webinar_registered per company domain (first-seen date persisted)."""
    events, notes = [], []
    seg = cfg["audiences"]["segments"].get("webinar_leads")
    pf = cfg["audiences"]["people_fields"]
    if not seg:
        return [], ["webinar: segment id missing"]
    ids, cursor, pages = [], None, 0
    while True:
        r = clay("audiences", "records", "search-ids", "--entity-type", "people", "--audience-id", seg, *(["--cursor", cursor] if cursor else []))
        if "_error" in r:
            notes.append(f"webinar: search stopped: {r['_error']}")
            break
        ids.extend(r.get("data", []))
        cursor = r.get("cursor")
        pages += 1
        if not cursor or pages > 40:
            break
    doms = defaultdict(int)
    for i in range(0, len(ids), 100):
        g = clay("audiences", "records", "get", "--entity-type", "people", "--ids", ",".join(str(x) for x in ids[i:i + 100]))
        for rec in (g.get("data") or []):
            f = rec.get("fields", {})
            if (f.get(pf["webinar_route"]) or "") != "bdr_review":
                continue
            dom = norm_domain(f.get(pf["company_domain"]) or (f.get("email") or "").split("@")[-1])
            if dom and dom not in cfg["exclusion"]["personal_email_domains"]:
                doms[dom] += 1
    fs = state.d.setdefault("first_seen", {})
    for dom, n in doms.items():
        k = f"webinar_registered|{dom}"
        fs.setdefault(k, TODAY.isoformat())
        events.append({"domain": dom, "family": "webinar_registered", "date": parse_date(fs[k]) or TODAY,
                       "detail": f"{n} registrant(s) in the BDR-review pool", "source": "audiences_webinar"})
    notes.append(f"webinar: {len(ids)} registrants scanned, {len(doms)} companies with a bdr_review registrant")
    return events, notes


# ---------------------------------------------------------------- scoring + lanes
def score_domain(evts, trig, cfg):
    rec_global = trig["recency"]
    fams = trig["triggers"]
    total, reasons, fresh_topics, personas = 0.0, [], [], []
    cap = cfg["thresholds"]["web_return_cap"]
    ret_used = 0
    for e in sorted(evts, key=lambda x: x["date"], reverse=True):
        meta = fams.get(e["family"])
        if not meta:
            continue
        if e["family"] == "web_return":
            if ret_used >= cap:
                continue
            ret_used += 1
        rec = {**rec_global, **meta.get("recency", {})}
        rf = recency_factor(e["date"], rec)
        contrib = meta["weight"] * rf
        total += contrib
        reasons.append(f"{e['source']}:{e['family']} {e['detail'][:60]} ({e['date'].isoformat()}, +{contrib:.0f})")
        if e["family"].startswith("web_") and e["detail"] and e["detail"] not in fresh_topics:
            fresh_topics.append(e["detail"])
        for p in meta.get("route_personas", []):
            if p not in personas:
                personas.append(p)
    return min(100, round(total)), reasons[:8], fresh_topics[:3], personas


def company_record(domain, cache):
    key = f"rec|{domain}"
    if key in cache:
        return cache[key]
    flt = {"type": "GroupOp", "combinationMode": "And", "items": [{
        "type": "BinOp", "key": "normalized_domain", "dataPath": ["account_entity_field_values", "field", "normalized_domain"],
        "operator": "Contain", "value": domain, "entityType": "ACCOUNT"}]}
    r = clay("audiences", "records", "search-ids", "--entity-type", "companies", "--filter", json.dumps(flt))
    ids = (r.get("data") or [])[:3] if isinstance(r, dict) else []
    rec = {}
    if ids:
        g = clay("audiences", "records", "get", "--entity-type", "companies", "--ids", ",".join(str(i) for i in ids))
        for x in (g.get("data") or []):
            f = x.get("fields", {})
            if norm_domain(f.get("normalized_domain") or f.get("domain")) == domain:
                rec = {"id": x.get("recordId"), **f}
                break
        if not rec and g.get("data"):
            x = g["data"][0]
            rec = {"id": x.get("recordId"), **x.get("fields", {})}
    cache[key] = rec
    return rec


def install_base_domains(cfg, cache):
    if "install_base" in cache:
        return set(cache["install_base"])
    tid = cfg["exclusion"]["install_base_table"]
    cols = clay("tables", "columns", "get", tid)
    dom_col = None
    for c in (cols.get("data", cols.get("columns", [])) if isinstance(cols, dict) else []):
        if "domain" in (c.get("name") or "").lower():
            dom_col = c.get("id")
            break
    doms, cursor, pages = set(), None, 0
    while dom_col:
        r = clay("tables", "rows", "list", tid, "--limit", "100", *(["--cursor", cursor] if cursor else []))
        for row in r.get("data", []) if isinstance(r, dict) else []:
            v = ((row.get("cells") or {}).get(dom_col) or {}).get("value")
            if v:
                doms.add(norm_domain(v))
        cursor = r.get("cursor") if isinstance(r, dict) else None
        pages += 1
        if not cursor or pages > 10:
            break
    for f in cfg["exclusion"].get("denylist_files", []):
        p = P(f)
        if os.path.exists(p):
            for r in csv.DictReader(open(p, newline="", errors="ignore")):
                for k in ("domain", "Domain", "company_domain"):
                    if r.get(k):
                        doms.add(norm_domain(r[k]))
    cache["install_base"] = sorted(doms)
    return doms


def named_domains(cfg):
    doms = set()
    for key in ("tam_accounts_csv", "stars_tiered_csv"):
        p = P(cfg["sources"][key])
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p, newline="", errors="ignore")):
            for k in ("domain", "Domain", "parent_domain", "website"):
                if r.get(k):
                    doms.add(norm_domain(r[k]))
    return doms


def assign_lane(domain, score, rec, cfg, ib, named, in_sequence):
    ex = cfg["exclusion"]
    th = cfg["thresholds"]
    if domain in ex["our_domains"] or domain in ex["personal_email_domains"] or domain in ex["competitor_domains"]:
        return "excluded", "our domain / personal / competitor"
    if domain in ex["partner_domains"]:
        return "excluded", "partner domain (alliances lane, not ours)"
    at = (rec.get(cfg["audiences"]["company_fields"]["account_type"]) or "")
    if at in ("Customer", "Partner") or domain in ib:
        return "customer_am", f"customer-exclusion union hit (SF Account Type={at or 'n/a'}, install-base={'yes' if domain in ib else 'no'})"
    is_named = domain in named or bool(rec.get("sfdc_owner_id")) or domain in in_sequence
    if domain in in_sequence and score > 0:
        return "rep", "live-sequence account came back"
    if score >= th["rep_min"] and is_named:
        return "rep", "named account over the rep threshold"
    industry = rec.get("industry") or ""
    emp = rec.get("employee_count") or 0
    try:
        emp = int(float(emp))
    except (TypeError, ValueError):
        emp = 0
    fit = (industry in th["icp_industries"]) or emp >= th["icp_min_employees"] or domain in named
    if score >= th["cohort_min"] and fit:
        return "cohort", f"ICP-fit (industry={industry or 'n/a'}, employees={emp or 'n/a'}) over the cohort threshold"
    if score >= th["rep_min"] and not is_named:
        return "cohort", "hot but unnamed: cohort lane (rep lane needs an owner or roster)"
    return "hold", "below thresholds or not ICP-fit"


def in_sequence_domains(cfg):
    """Companies currently in a live lemlist sequence. Source: the relay's dry-run/live logs (lead emails). Best effort."""
    doms = set()
    for f in sorted(glob.glob(P(cfg["sources"]["relay_log_glob"])))[-30:]:
        for m in re.finditer(r"[\w.+-]+@([\w-]+(?:\.[\w-]+)+)", open(f, errors="ignore").read()):
            d = norm_domain(m.group(1))
            if d and d not in cfg["exclusion"]["personal_email_domains"]:
                doms.add(d)
    return doms


def suggest_contacts(domain, personas, cfg, limit=6):
    """Known ICP contacts at the company from Audiences (0 credits). Net-new sourcing is the cutter's job."""
    pf = cfg["audiences"]["people_fields"]
    flt = {"type": "GroupOp", "combinationMode": "And", "items": [
        {"type": "BinOp", "key": "normalized_domain", "dataPath": ["account_entity_field_values", "field", "normalized_domain"],
         "operator": "Contain", "value": domain, "entityType": "ACCOUNT"}]}
    r = clay("audiences", "records", "search-ids", "--entity-type", "people", "--filter", json.dumps(flt))
    ids = (r.get("data") or [])[:100] if isinstance(r, dict) else []
    out = []
    if ids:
        g = clay("audiences", "records", "get", "--entity-type", "people", "--ids", ",".join(str(i) for i in ids))
        for rec in (g.get("data") or []):
            f = rec.get("fields", {})
            pk = f.get(pf["persona_key"]) or ""
            title = f.get(pf["enriched_title"]) or f.get("title") or ""
            if pk and pk in cfg["thresholds"]["icp_personas"]:
                rank = 0 if pk in personas else 1
            elif re.search(r"\b(vp|vice president|director|head|chief|svp|evp)\b", title, re.I):
                rank = 2
            else:
                continue
            out.append((rank, {"name": f"{f.get('first_name', '')} {f.get('last_name', '')}".strip(), "title": title,
                               "email": f.get("email") or "", "persona": pk, "linkedin": f.get("linkedin_url") or ""}))
    out.sort(key=lambda x: x[0])
    return [x[1] for x in out[:limit]]


# ---------------------------------------------------------------- outputs
def post_webhook(url, payload, live, log):
    if not live:
        log.append(f"    would POST {url.split('/')[-1][:8]}...: {json.dumps(payload)[:300]}")
        return True
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", "-H", "Content-Type: application/json",
                        "-d", json.dumps(payload), url], capture_output=True, text=True, timeout=60)
    ok = r.stdout.strip().startswith("2")
    log.append(f"    POST {'ok' if ok else 'FAILED ' + r.stdout.strip()}: {payload.get('domain')}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--domain", help="score one domain and print")
    ap.add_argument("--no-clay", action="store_true", help="skip every Clay CLI call (offline test)")
    a = ap.parse_args()

    cfg, trig, web = load(CFG_PATH), load(TRIG_PATH), load(WEB_PATH)
    dry = a.dry_run or cfg.get("dry_run", True)
    live_stamp = cfg.get("live_stamp", False) and not dry
    live_lane_a = cfg.get("live_lane_a", False) and not dry
    os.makedirs(LOG_DIR, exist_ok=True)
    state = State(P(cfg["sources"]["state_file"]))
    try:
        cache = load(P(cfg["sources"]["domain_cache"]))
    except Exception:  # noqa: BLE001
        cache = {}
    if a.no_clay:
        global clay  # noqa: PLW0603
        clay = lambda *args, **kw: {"_error": "offline (--no-clay)", "data": []}  # noqa: E731

    notes, events = [], []
    for fn in (lambda: events_from_web_intent(cfg, web), lambda: events_from_relay_logs(cfg),
               lambda: events_from_triggers_csv(cfg), lambda: events_from_staged_signals(cfg, cache),
               lambda: events_from_webinar(cfg, state)):
        ev, n = fn()
        events.extend(ev)
        notes.extend(n)

    by_dom = defaultdict(list)
    for e in events:
        if e["domain"]:
            by_dom[e["domain"]].append(e)
    if a.domain:
        by_dom = {a.domain: by_dom.get(a.domain, [])}

    ib = install_base_domains(cfg, cache) if not a.no_clay else set()
    named = named_domains(cfg)
    seq = in_sequence_domains(cfg)

    results = []
    for dom, evts in by_dom.items():
        score, reasons, topics, personas = score_domain(evts, trig, cfg)
        rec = company_record(dom, cache) if not a.no_clay else {}
        lane, why = assign_lane(dom, score, rec, cfg, ib, named, seq)
        results.append({"domain": dom, "score": score, "lane": lane, "why": why, "reasons": reasons,
                        "topics": topics, "personas": personas, "rec": rec, "events": len(evts)})
    results.sort(key=lambda r: (-r["score"], r["domain"]))

    # rolloff: previously stamped domains that produced nothing this run
    prev_lanes = state.d.get("lane", {})
    seen = {r["domain"] for r in results}
    rolloff = [d for d, l in prev_lanes.items() if d not in seen and l not in ("hold", "excluded")]

    log = [f"# Heat List: {TODAY.isoformat()} ({'DRY RUN' if dry else 'LIVE'}; stamp={'on' if live_stamp else 'off'}, lane A={'on' if live_lane_a else 'off'})", ""]
    log.append("Scored by tam-outbound-engine/config/triggers.json + web_intent.json; lanes per automation/config/heat_loop.json. "
               "Read-only over Clay (0 credits). Fields stamped through the Heat Stamp workflow only when live.")
    log.append("")
    log.append("## Sources")
    log += [f"- {n}" for n in notes]
    counts = defaultdict(int)
    for r in results:
        counts[r["lane"]] += 1
    log += ["", "## Lanes", f"- ran, {len(results)} companies scored: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + (f"; {len(rolloff)} rolled off" if rolloff else "")]

    stamp_url = cfg["workflows"]["heat_stamp"]["webhook_url"]
    lane_url = cfg["workflows"]["lane_a"]["webhook_url"]
    alerted = state.d.setdefault("alerted", {})
    log += ["", "## Lane A: rep alerts (same day)"]
    any_a = False
    for r in results:
        if r["lane"] != "rep":
            continue
        last = alerted.get(r["domain"])
        if last and (TODAY - parse_date(last)).days < cfg["thresholds"]["rep_realert_days"] and "came back" not in r["why"]:
            log.append(f"- {r['domain']}: score {r['score']}, already alerted {last}, skipped (re-alert window)")
            continue
        any_a = True
        country = (r["rec"].get("location_country") or "default")
        rep = cfg["rep_by_country"].get(country, cfg["rep_by_country"]["default"])
        contacts = suggest_contacts(r["domain"], r["personas"], cfg) if not a.no_clay else []
        top = trig["triggers"].get(next((e.split(":")[1].split(" ")[0] for e in r["reasons"] if ":" in e), ""), {})
        stakes = top.get("stakes") or ""
        lines = [f"*{r['rec'].get('org_name') or r['domain']}* is warm (heat {r['score']}).",
                 "What we saw: " + "; ".join(x.split(" (")[0].split(":", 1)[1] for x in r["reasons"][:3]) + ".",
                 (f"Why now: {stakes}" if stakes else ""),
                 "Suggested names: " + ("; ".join(f"{c['name']} ({c['title']})" for c in contacts) if contacts else "none on file, cutter will source"),
                 "Approve = push these into your sequence with the topic as the icebreaker. Deny = hold 7 days."]
        summary = "\n".join(x for x in lines if x)
        payload = {"domain": r["domain"], "company": r["rec"].get("org_name") or r["domain"], "rep_channel": cfg["channels"][rep],
                   "summary": summary, "campaign_id": cfg["cohort"]["lemlist_campaign_ids"].get(rep, ""),
                   "lead_email": contacts[0]["email"] if contacts else "", "lead_first_name": (contacts[0]["name"].split(" ")[0] if contacts else ""),
                   "lead_last_name": (" ".join(contacts[0]["name"].split(" ")[1:]) if contacts else ""),
                   "lead_linkedin_url": contacts[0]["linkedin"] if contacts else "",
                   "signal_note": ("your team's work on " + r["topics"][0]) if r["topics"] else ""}
        log.append(f"- {r['domain']} -> #{rep} ({r['why']})")
        log.append("  " + summary.replace("\n", "\n  "))
        post_webhook(lane_url, payload, live_lane_a, log)
        if live_lane_a:
            alerted[r["domain"]] = TODAY.isoformat()
        log.append(f"  evt: {LOG_FAMILY}-{TODAY.isoformat()}#{slug(r['domain'])}")
    if not any_a:
        log.append("- none this run")

    log += ["", "## Stamps (Audiences company fields)"]
    for r in results:
        payload = {"domain": r["domain"], "heat_score": r["score"], "heat_reasons": " | ".join(r["reasons"]),
                   "heat_lane": r["lane"], "heat_updated": TODAY.isoformat(), "heat_cohort": (state.d.get("cohort", {}) or {}).get(r["domain"], "")}
        log.append(f"- {r['domain']}: {r['score']} {r['lane']} ({r['why']}); {r['events']} events")
        post_webhook(stamp_url, payload, live_stamp, log)
        if r["lane"] in ("rep", "cohort", "customer_am") and not any(e.startswith("web:") for e in r["reasons"]) and r["score"] >= cfg["thresholds"]["cohort_min"]:
            pass
        if r["lane"] in ("rep", "cohort", "customer_am"):
            log.append(f"  evt: {LOG_FAMILY}-{TODAY.isoformat()}#{slug(r['domain'])}")
    for d in rolloff:
        payload = {"domain": d, "heat_score": 0, "heat_reasons": "rolled off (no events in window)", "heat_lane": "hold",
                   "heat_updated": TODAY.isoformat(), "heat_cohort": ""}
        log.append(f"- {d}: rolled off to hold")
        post_webhook(stamp_url, payload, live_stamp, log)

    log += ["", "## customer_am (route to the AM clearance sheet, never cold)"]
    cam = [r for r in results if r["lane"] == "customer_am"]
    log += [f"- {r['domain']}: {r['score']}; " + "; ".join(x.split(' (')[0] for x in r['reasons'][:2]) for r in cam] or ["- none"]
    log += ["", "## Top 15 by heat"]
    log += [f"- {r['domain']} {r['score']} [{r['lane']}] " + "; ".join(x.split(' (')[0] for x in r['reasons'][:2]) for r in results[:15]] or ["- none"]

    if live_stamp:
        state.d["lane"] = {r["domain"]: r["lane"] for r in results}
    state.save()
    with open(P(cfg["sources"]["domain_cache"]), "w") as f:
        json.dump(cache, f)
    out = os.path.join(LOG_DIR, f"{LOG_FAMILY}-{TODAY.isoformat()}.md")
    with open(out, "w") as f:
        f.write("\n".join(log) + "\n")
    print("\n".join(log[:6]))
    print(f"... written {out}")
    if a.domain:
        print(json.dumps(results, default=str, indent=1)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
