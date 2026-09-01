#!/usr/bin/env python3
"""Merge URL-bridge results (Clay MCP find-and-enrich-list-of-contacts, 0 credits) into a set's candidates CSV.
Fills linkedin_url, refreshes the title from the live profile, excludes people who have left, benches people the
bridge could not find (Aug 25 rule: nobody goes on a rep-facing map until a live source confirms them), and records
multi-profile matches in the set's `dual` list. Run with --set <name>; the set lists `bridge_results` files."""
import csv, json, os, re, sys
from bo_set import load_set
from bo_titles import configure
from bo_gates import gate_reason
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]; configure(CFG)
def norm(t): return re.sub(r"\s+", " ", (t or "")).strip()
def key(a, n): return (a, re.sub(r"[^a-z ]", "", n.split(",")[0].lower()).strip())
res = {}
for f in CFG.get("bridge_results", []):
    p = os.path.join(HERE, f)
    if not os.path.exists(p): print("missing", f); continue
    for r in csv.DictReader(open(p)): res[key(r["account"], r["full_name"])] = r
cands = list(csv.DictReader(open(P["candidates"])))
stats = {"url": 0, "title_refreshed": 0, "left": 0, "not_found": 0, "dual": 0, "unmatched_results": 0}
seen = set(); dual = {tuple(x) for x in CFG.get("dual", [])}
for c in cands:
    k = key(c["account"], c["full_name"]); r = res.get(k)
    if not r: continue
    seen.add(k)
    st = (r.get("status") or "").strip().lower()
    if r.get("linkedin_url"): c["linkedin_url"] = r["linkedin_url"].strip(); stats["url"] += 1
    if st in ("current", "dual"):
        ft = norm(r.get("fresh_title"))
        if c["search_query"].startswith("manual"): ft = ""   # researched title (company source) outranks a LinkedIn headline
        if ft and ft.lower() != norm(c["title"]).lower():
            c["title"] = ft; stats["title_refreshed"] += 1
            g = gate_reason(ft, c["full_name"], CFG["accounts"].get(c["account"], {}), c.get("location", ""))
            if g: c["excluded_reason"] = f"live title fails gate ({g.replace('title_excluded_gate_','')}): {ft[:50]}"; stats["regated"] = stats.get("regated", 0) + 1
        if st == "dual": dual.add((c["account"], c["full_name"])); stats["dual"] += 1
        c["source"] = (c["source"].split(" | ")[0]) + " | bridged"
    elif st == "left":
        c["excluded_reason"] = "no longer at account per live profile" + (f" (now {norm(r.get('note'))[:60]})" if r.get("note") else ""); stats["left"] += 1
    elif st == "not_found":
        c["excluded_reason"] = "not found by live profile check; bench until Sales Nav confirms"; stats["not_found"] += 1
stats["unmatched_results"] = len(set(res) - seen)
with open(P["candidates"], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(cands[0].keys())); w.writeheader(); w.writerows(cands)
cfg_path = os.path.join(HERE, "sets", f"{CFG['_name']}.json"); raw = json.load(open(cfg_path))
raw["dual"] = sorted([list(x) for x in dual]); json.dump(raw, open(cfg_path, "w"), indent=1, ensure_ascii=False)
print(stats)
if stats["unmatched_results"]: print("results with no candidate row:", sorted(set(res) - seen)[:10])
