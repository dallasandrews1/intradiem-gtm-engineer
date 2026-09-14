#!/usr/bin/env python3
"""Turn a rep set's raw Clay search sweeps (sweeps/<set>/<account>.csv) into the candidates CSV the build sheets read.
Same schema as inger_backoffice_candidates.csv. Every row is kept with an excluded_reason so nothing is silently lost;
kept rows have a blank excluded_reason. LinkedIn URLs arrive later from the URL bridge (apply_url_bridge / MCP)."""
import csv, os, re, sys
from collections import defaultdict
from bo_set import load_set
from bo_titles import band, func, lane, is_root, topics, configure
from bo_gates import gate_reason
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]; configure(CFG)

def norm(t): return re.sub(r"\s+", " ", (t or "").replace("–", "-").replace("—", "-")).strip()

prev = {}
if os.path.exists(P["candidates"]):
    for r in csv.DictReader(open(P["candidates"])): prev[(r["account"], re.sub(r"[^a-z ]", "", r["full_name"].split(",")[0].lower()).strip())] = r
KEEP_REASON = re.compile(r"^(no longer at account|not found by live profile|live title fails gate)")
out = []
stats = defaultdict(lambda: defaultdict(int))
for acct, spec in CFG["accounts"].items():
    path = os.path.join(HERE, spec["sweep"])
    rows = list(csv.DictReader(open(path)))
    seen = {}
    def namekey(n): return re.sub(r"[^a-z ]", "", n.split(",")[0].lower()).strip()
    for r in rows:
        key = namekey(r["full_name"])
        if key in seen:
            seen[key]["tags"].add(r["query_tag"]); continue
        seen[key] = {"r": r, "tags": {r["query_tag"]}}
    for key, v in seen.items():
        r = v["r"]; t = norm(r["title"]); tl = t.lower()
        reason = gate_reason(t, r["full_name"], spec, r.get("location", ""))
        b = band(t)
        pr = prev.get((acct, re.sub(r"[^a-z ]", "", r["full_name"].split(",")[0].lower()).strip()))
        url = (r.get("linkedin_url") or "").strip(); src = CFG.get("candidate_default_source", "search")
        if pr:
            url = pr.get("linkedin_url", "")
            if "bridged" in pr.get("source", "") or "live-verified" in pr.get("source", ""):
                t = pr["title"]; src = pr["source"]
                if not reason: reason = gate_reason(t, r["full_name"], spec, r.get("location", ""))
            if KEEP_REASON.match(pr.get("excluded_reason", "")): reason = pr["excluded_reason"]
        stats[acct][reason or "kept"] += 1
        out.append({"account": acct, "full_name": r["full_name"].strip(), "title": t, "function_guess": func(t) if not reason else "",
                    "band_guess": band(t), "linkedin_url": url, "location": r.get("location", ""), "source": src,
                    "search_query": ",".join(sorted(v["tags"])) + " | " + r.get("company_name", ""), "excluded_reason": reason, "li_active": "", "li_last_post": "",
                    "clay_profile_id": r["clay_profile_id"], "start_date": r.get("start_date", "")})
TRIM = {(a, n): why for a, n, why in CFG.get("trim", [])}
for o in out:
    if (o["account"], o["full_name"]) in TRIM and not o["excluded_reason"]:
        o["excluded_reason"] = "trimmed on review: " + TRIM[(o["account"], o["full_name"])]
# hand-added people (web research with a source): kept unless a gate says otherwise, survive every rerun
for m in CFG.get("manual_add", []):
    a = m["account"]; t = norm(m["title"]); spec = CFG["accounts"].get(a, {})
    nk = re.sub(r"[^a-z ]", "", m["full_name"].split(",")[0].lower()).strip()
    hit = [o for o in out if o["account"] == a and re.sub(r"[^a-z ]", "", o["full_name"].split(",")[0].lower()).strip() == nk]
    if hit:   # already sourced: the researched title and URL win, and force clears a stale leaver verdict
        o = hit[0]; o["title"] = t; o["function_guess"] = func(t); o["band_guess"] = band(t); o["full_name"] = m["full_name"]   # researched casing wins over an all-lowercase sweep name
        if m.get("linkedin_url"): o["linkedin_url"] = m["linkedin_url"]
        if m.get("force") or not KEEP_REASON.match(o["excluded_reason"]): o["excluded_reason"] = ""   # a researched executive passes the title gates
        o["search_query"] = "manual | " + m.get("note", "")[:80]; o["source"] = o["source"].split(" | ")[0] + " | web research"
        continue
    pr = prev.get((a, nk)); url = m.get("linkedin_url") or (pr or {}).get("linkedin_url", "")
    reason = ""   # researched executives pass the title gates; only a live leaver verdict can hold them
    if pr and KEEP_REASON.match(pr.get("excluded_reason", "")) and not m.get("force"): reason = pr["excluded_reason"]
    if m.get("force"): reason = ""
    stats[a][reason or "kept"] += 1
    out.append({"account": a, "full_name": m["full_name"], "title": t, "function_guess": func(t) if not reason else "", "band_guess": band(t), "linkedin_url": url,
                "location": "", "source": (pr or {}).get("source") if pr and ("bridged" in (pr or {}).get("source", "") or "live-verified" in (pr or {}).get("source", "")) else m.get("source", "web research Aug 31"),
                "search_query": "manual | " + m.get("note", "")[:80], "excluded_reason": reason, "li_active": "", "li_last_post": "", "clay_profile_id": "", "start_date": ""})
with open(P["candidates"], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for a in CFG["accounts"]:
    s = stats[a]; print(f"{a}: kept {s['kept']} of {sum(s.values())} | " + ", ".join(f"{k.replace('title_excluded_gate_','')} {v}" for k, v in sorted(s.items(), key=lambda x: -x[1]) if k != "kept"))
print("written", P["candidates"], len(out), "rows")
