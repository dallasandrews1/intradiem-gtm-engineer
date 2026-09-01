#!/usr/bin/env python3
"""Live employment check for everyone on a set's maps, via Clay's managed routine "Enrich Person"
(function:t_0thx4ohpCNT3KNijyVo, 0.5 credit per person, last_refresh = today). The reliable field is `current_experience`:
empty means the person has left or retired; populated means still employed, and the company must match the account.
Verified Aug 31 2026 on two known-stale people (Waterman retired, King moved), both caught.

Usage: verify_live.py --set <name> [--go] [--bench]   (without --go prints the estimate only)
Writes <set>_live_check.csv and applies results to the candidates CSV (title refresh, exclusions for leavers)."""
import csv, json, os, re, subprocess, sys, time
from bo_set import load_set
from bo_titles import configure
from bo_gates import gate_reason
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]; ARGS = CFG["_args"]; configure(CFG)
ROUTINE = "function:t_0thx4ohpCNT3KNijyVo"; COST = 0.5
OUT = os.path.join(HERE, f"{CFG['_name']}_live_check.csv")

def clay(args, tries=3):
    for i in range(tries):
        r = subprocess.run(["clay"] + args, capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3 + 3 * i)
    return {}
def credits():
    d = clay(["credits"]); return d.get("balance") if isinstance(d, dict) else None
def norm(t): return re.sub(r"\s+", " ", (t or "")).strip()

rows = list(csv.DictReader(open(P["build_sheets_csv"])))
targets = [(r["account"], r["full_name"], r["linkedin_url"]) for r in rows if r["linkedin_url"]]
if "--bench" in ARGS:
    targets += [(r["account"], r["full_name"], r["linkedin_url"]) for r in csv.DictReader(open(P["bench_csv"])) if r["linkedin_url"]]
already = {}
if os.path.exists(OUT):
    for r in csv.DictReader(open(OUT)): already[(r["account"], r["full_name"])] = r
retry = "--retry" in ARGS
todo = [t for t in targets if (t[0], t[1]) not in already or (retry and already[(t[0], t[1])]["status"] == "no_result")]
CHUNK = 10 if retry else 20
print(f"{len(targets)} on maps with a URL, {len(already)} already checked, {len(todo)} to run: estimate {len(todo) * COST:.1f} credits")
if "--go" not in ARGS: sys.exit(0)

before = credits(); print("credits before:", before)
aliases = {a: [x.lower() for x in s.get("aliases", [a.split()[0]])] for a, s in CFG["accounts"].items()}
results = dict(already)
by_acct = {}
for a, n, u in todo: by_acct.setdefault(a, []).append((n, u))
for acct, items in by_acct.items():
    for chunk_i in range(0, len(items), CHUNK):
        chunk = items[chunk_i:chunk_i + CHUNK]
        payload = {"items": [{"id": f"p{i}", "inputs": {"Professional Profile URL": u}} for i, (n, u) in enumerate(chunk)]}
        start = clay(["routines", "runs", "start", ROUTINE, "--input", json.dumps(payload)])
        run_id = start.get("routineRunId") if isinstance(start, dict) else None
        if not run_id: print("start failed for", acct, start); continue
        res = {}
        for _ in range(20):
            res = clay(["routines", "runs", "get", run_id, "--wait", "60"])
            items_done = isinstance(res, dict) and all((d.get("status") in ("complete", "completed", "failed", "error")) for d in res.get("data", []))
            if isinstance(res, dict) and res.get("status") in ("complete", "completed", "failed", "error") and items_done and len(res.get("data", [])) >= len(chunk): break
            time.sleep(5)
        data = res.get("data", []) if isinstance(res, dict) else []
        RAW = os.path.join(HERE, "_live_raw"); os.makedirs(RAW, exist_ok=True)
        json.dump(res, open(os.path.join(RAW, f"{CFG['_name']}_{run_id}.json"), "w"))
        # match each result to its input by the profile slug the routine returns; never by position (results arrive in completion order)
        def slug(u): return re.sub(r"/+$", "", re.sub(r"^https?://(www\.)?linkedin\.com/in/", "", (u or "").strip().lower()))
        byslug = {}
        for d in data:
            ep0 = ((d.get("result") or {}).get("Enrich person") or {}) if isinstance(d, dict) else {}
            if ep0.get("url"): byslug[slug(ep0["url"])] = d
        def nk(x): return re.sub(r"[^a-z]", "", (x or "").split(",")[0].lower())
        byname = {}
        for d in data:
            ep0 = ((d.get("result") or {}).get("Enrich person") or {}) if isinstance(d, dict) else {}
            if ep0.get("name"): byname.setdefault(nk(ep0["name"]), []).append(d)
        for i, (n, u) in enumerate(chunk):
            d = byslug.get(slug(u), {})
            if not d and len(byname.get(nk(n), [])) == 1: d = byname[nk(n)][0]   # canonical URL differs from ours; unique name match in this run
            ep = ((d.get("result") or {}).get("Enrich person") or {}) if isinstance(d, dict) else {}
            cur = ep.get("current_experience") or []
            row = {"account": acct, "full_name": n, "linkedin_url": u, "status": "", "live_title": "", "live_company": "", "start_date": "", "last_refresh": ep.get("last_refresh", ""), "note": ""}
            if not ep:
                row["status"] = "no_result"; row["note"] = str(d.get("status", ""))[:80] if isinstance(d, dict) else ""
            elif not cur:
                le = ep.get("latest_experience") or {}
                row.update({"status": "left_or_retired", "live_title": le.get("title", ""), "live_company": le.get("company", ""), "note": f"no current experience; last role ended {le.get('end_date') or 'unknown'}"})
            else:
                match = [e for e in cur if any(al in (e.get("company") or "").lower() for al in aliases[acct])]
                if match:
                    e = max(match, key=lambda e: e.get("start_date") or "")
                    row.update({"status": "current", "live_title": e.get("title", ""), "live_company": e.get("company", ""), "start_date": e.get("start_date") or ""})
                    if len(cur) > 1: row["note"] = "also lists: " + "; ".join(f"{x.get('title')} at {x.get('company')}" for x in cur if x is not e)[:120]
                else:
                    e = max(cur, key=lambda e: e.get("start_date") or "")
                    row.update({"status": "left", "live_title": e.get("title", ""), "live_company": e.get("company", ""), "start_date": e.get("start_date") or "", "note": f"now at {e.get('company')}"})
            results[(acct, n)] = row
        with open(OUT, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["account", "full_name", "linkedin_url", "status", "live_title", "live_company", "start_date", "last_refresh", "note"]); w.writeheader(); w.writerows(results.values())
        print(f"{acct}: {len(chunk)} checked")
after = credits(); print("credits after:", after, "| spent:", (before - after) if before is not None and after is not None else "?")

# apply to candidates: refresh titles, exclude leavers, tag the source
cands = list(csv.DictReader(open(P["candidates"])))
def key(a, n): return (a, re.sub(r"[^a-z ]", "", n.split(",")[0].lower()).strip())
rk = {key(a, n): r for (a, n), r in results.items()}
st = {"refreshed": 0, "left": 0, "current": 0, "no_result": 0}
for c in cands:
    r = rk.get(key(c["account"], c["full_name"]))
    if not r: continue
    if r["status"] == "current":
        st["current"] += 1
        lt = norm(r["live_title"])
        if c["search_query"].startswith("manual"): lt = ""   # researched title outranks the LinkedIn headline; the leaver verdict still applies
        if lt and lt.lower() != norm(c["title"]).lower():
            c["title"] = lt; st["refreshed"] += 1
            g = gate_reason(lt, c["full_name"], CFG["accounts"].get(c["account"], {}), c.get("location", ""))
            if g: c["excluded_reason"] = f"live title fails gate ({g.replace('title_excluded_gate_','')}): {lt[:50]}"; st["regated"] = st.get("regated", 0) + 1
        if "live-verified" not in c["source"]: c["source"] = c["source"].split(" | ")[0] + " | live-verified"
    elif r["status"] in ("left", "left_or_retired"):
        c["excluded_reason"] = "no longer at account per live enrichment" + (f" ({r['note'][:70]})" if r["note"] else ""); st["left"] += 1
    else: st["no_result"] += 1
with open(P["candidates"], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(cands[0].keys())); w.writeheader(); w.writerows(cands)
print("applied:", st, "| rerun build_map_build_sheets.py to refill any opened slots (bench people are not live-checked until they land on a map)")
