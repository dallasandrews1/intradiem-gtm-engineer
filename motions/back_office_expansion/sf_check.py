#!/usr/bin/env python3
"""Salesforce presence check for a set's shortlist (Aug 25 method, 0 credits): match every bridged candidate against ALL
Audiences people by LinkedIn slug (anchor Contain on /in/<slug>), then by exact first+last name. Writes the set's sf_check
CSV in the Inger schema. 'yes' = same LinkedIn profile is in Salesforce (anywhere, any employer); 'possible' = name-only
match (high confidence when the SF record sits on this account, medium when the company text matches, low otherwise).
Run with --set <name> [--only-map] ; reads the candidates CSV (kept rows with a URL)."""
import csv, json, os, re, subprocess, sys, time
from bo_set import load_set
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]
F = {"title": "title", "company": "audf_0tkdvkhYzHJGF3NrfqG", "acct": "audf_0timw68Jf4dTsQQqq38", "status": "audf_0timw8mQ9wKWoXv23X5",
     "source": "audf_0timw8gjiJpc5Kmdocm", "owner": "audf_0timw93AWnwkAbNguBv", "email": "email", "li": "linkedin_url", "fn": "first_name", "ln": "last_name"}
ACCT_IDS = {a: set(s.get("sf_account_ids", [])) for a, s in CFG["accounts"].items()}

def clay(args, tries=4):
    for i in range(tries):
        r = subprocess.run(["clay"] + args, capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        if "rate" in (r.stderr + r.stdout).lower(): time.sleep(6 + 4 * i); continue
        time.sleep(1.5)
    return {}

def bin_(key, op, val): return {"type": "BinOp", "key": key, "dataPath": ["contact_entity_field_values", "field", key], "operator": op, "value": val, "entityType": "CONTACT"}
def group(items, mode="And"): return {"type": "GroupOp", "combinationMode": mode, "items": items}
def search(flt, limit=10):
    d = clay(["audiences", "records", "search-ids", "--entity-type", "people", "--filter", json.dumps(flt), "--limit", str(limit)])
    return d.get("data", []) if isinstance(d, dict) else []
def get(ids):
    if not ids: return []
    d = clay(["audiences", "records", "get", "--entity-type", "people", "--ids", ",".join(str(i) for i in ids[:100])])
    return d.get("data", []) if isinstance(d, dict) else []

def slug_of(url):
    m = re.search(r"linkedin\.com/in/([^/?#]+)", url or "", re.I)
    return m.group(1).strip().lower() if m else ""
def split_name(n):
    n = re.sub(r"\(.*?\)", "", n.split(",")[0]).strip()
    parts = [p for p in re.split(r"\s+", n) if p and not re.fullmatch(r"[A-Z]\.?|MBA|CPA|PMP|CPCU|Jr\.?|Sr\.?|II|III", p)]
    return (parts[0], parts[-1]) if len(parts) >= 2 else (parts[0] if parts else n, "")

cands = [r for r in csv.DictReader(open(P["candidates"])) if not r["excluded_reason"].strip() and r["linkedin_url"]]
if "--only-map" in CFG["_args"]:
    onmap = {(r["account"], r["full_name"]) for r in csv.DictReader(open(P["build_sheets_csv"]))}
    cands = [r for r in cands if (r["account"], r["full_name"]) in onmap]
out = []; n = 0
for c in cands:
    n += 1
    slug = slug_of(c["linkedin_url"]); ids = search(group([bin_(F["li"], "Contain", f"/in/{slug}")]), 5) if slug else []
    method = "linkedin_slug" if ids else ""
    if not ids:
        fn, ln = split_name(c["full_name"])
        if fn and ln:
            ids = search(group([bin_(F["fn"], "Equal", fn), bin_(F["ln"], "Equal", ln)]), 10); method = "exact_name" if ids else ""
    recs = get(ids)
    row = {"account": c["account"], "full_name": c["full_name"], "linkedin_url": c["linkedin_url"], "in_salesforce": "no", "match_confidence": "",
           "sf_matched_name": "", "sf_company": "", "sf_title": "", "sf_email": "", "sf_lead_status": "", "sf_lead_source": "", "sf_owner": "", "sf_account_id": "",
           "match_method": method, "notes": "no LinkedIn or exact-name hit in Audiences people"}
    if recs:
        # prefer the record on this account, then any record whose company text names the account
        def score(r):
            f = r["fields"]; a = str(f.get(F["acct"]) or ""); comp = str(f.get(F["company"]) or "").lower()
            return (a in ACCT_IDS.get(c["account"], set()), c["account"].split()[0].lower() in comp)
        best = max(recs, key=score); f = best["fields"]; on_acct, comp_match = score(best)
        row.update({"sf_matched_name": f"{f.get(F['fn']) or ''} {f.get(F['ln']) or ''}".strip(), "sf_company": str(f.get(F["company"]) or ""), "sf_title": str(f.get(F["title"]) or ""),
                    "sf_email": str(f.get(F["email"]) or ""), "sf_lead_status": str(f.get(F["status"]) or ""), "sf_lead_source": str(f.get(F["source"]) or ""),
                    "sf_owner": str(f.get(F["owner"]) or ""), "sf_account_id": str(f.get(F["acct"]) or "")})
        if method == "linkedin_slug":
            row["in_salesforce"] = "yes"; row["match_confidence"] = "high"; row["notes"] = f"same LinkedIn profile in Salesforce ({len(recs)} record{'s' if len(recs) > 1 else ''})" + ("; on this account" if on_acct else "")
        else:
            row["in_salesforce"] = "possible"; row["match_confidence"] = "high" if on_acct else ("medium" if comp_match else "low")
            row["notes"] = f"exact name match only ({len(recs)} record{'s' if len(recs) > 1 else ''}); " + ("on this account" if on_acct else ("company text matches" if comp_match else "different company or blank"))
    out.append(row)
    if n % 25 == 0: print(f"{n}/{len(cands)}", file=sys.stderr)
with open(P["sf_check"], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), "checked |", dict(Counter((r["in_salesforce"], r["match_confidence"]) for r in out)))
