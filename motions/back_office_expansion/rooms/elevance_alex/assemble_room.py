#!/usr/bin/env python3
"""Assembles data/expansion_room_elevance.json for Alex Bauer's Elevance Health expansion room: account facts, the reorg,
Alex's relationship map (30 cards, Sep 11 transcription), the two back-office maps (set alex, live-checked Sep 11),
the Salesforce-known layer (303 people across 18 plan accounts), validated emails, and the marketing CSV. Re-run after any source change."""
import csv, json, pathlib, re, collections
HERE = pathlib.Path(__file__).parent; DATA = HERE / "data"; BO = HERE.parent.parent
INBOX = pathlib.Path.home() / "Claude/Projects/Intradiem GTM Engineer/automation/inbox/salesnav/alex/transcribed/map_01.csv"
TODAY = "2026-09-11"
def clean(s): return re.sub(r"\s+", " ", (s or "")).strip()

# Alex's relationship map (customer side, contact-center line)
STALE = {"Maurice Pardo": "has left Elevance Health (map header flag)", "Amish Patel": "card shows GuideWell as employer", "Kumar Gudavalli": "card shows SCAN as employer", "Che Thompson": "card shows Hyundai Motor Group Metaplant America"}
am = [{"name": r["full_name"], "title": clean(r["title"]), "reports_to": r["reports_to"], "depth": r["tree_depth"], "crm": r["crm_status"],
       "placeholder": "placeholder" in (r["notes"] or "").lower(), "stale": STALE.get(r["full_name"], ""), "entity": ("Carelon" if "carelon" in (r["title"] + r["notes"]).lower() else ("WellPoint" if "wellpoint" in (r["title"] + r["notes"]).lower() else ""))}
      for r in csv.DictReader(open(INBOX))]
sponsor_line = [a["name"] for a in am if any(b["reports_to"] == a["name"] for b in am)]

# The two back-office maps
bo = [r for r in csv.DictReader(open(BO / "BO_Map_Build_Sheets_Alex.csv"))]
bo_rows = [{"account": r["account"], "map": r["map_name"], "card": int(r["order"]), "depth": int(r["depth"]), "name": r["full_name"], "title": r["title"], "level": r["level"],
            "function": r["function"], "reports_to": r["reports_up_to"], "linkedin": r["linkedin_url"], "flag": r["badge_check"], "lane": r["lane"], "note": r["note"]} for r in bo]
bench = [r for r in csv.DictReader(open(BO / "BO_Map_Bench_Alex.csv"))]
removed = [r for r in csv.DictReader(open(BO / "alex_backoffice_candidates.csv")) if r["excluded_reason"].startswith(("trimmed on review", "no longer at account", "not found by live", "live title fails"))]

# Salesforce-known layer, grouped by the plan account it sits under
known = [r for r in csv.DictReader(open(BO / "alex_known_layer_people.csv")) if clean(r["full_name"]) and " " in clean(r["full_name"]) and "@" not in r["full_name"]]
cos = {r["matched_name"]: r for r in csv.DictReader(open(BO / "alex_known_layer_companies.csv"))}
by_co = collections.defaultdict(list)
for r in known: by_co[r["sf_company"]].append({"name": clean(r["full_name"]), "title": clean(r["title"]), "email": (r["email"] or "").lower(), "linkedin": r["linkedin_url"], "lead_status": r["lead_status"]})
known_groups = sorted(({"sf_company": k, "sf_account_id": cos.get(k, {}).get("sf_account_id", ""), "account_type": cos.get(k, {}).get("account_type", "") or "blank", "side": "Carelon" if re.search(r"carelon|beacon|ingenio", k, re.I) else "Elevance Health", "people": sorted(v, key=lambda x: x["name"])} for k, v in by_co.items()), key=lambda g: -len(g["people"]))
FRONT = re.compile(r"contact cent|call cent|customer care|customer service|member service|workforce management|\bwfm\b|real time|realtime|intraday|scheduling|forecast|service operations|customer experience|\bcx\b|ivr|telephony", re.I)
sponsor_names = {a["name"].lower() for a in am}
mkt = []
for g in known_groups:
    for p in g["people"]:
        why = ""
        if p["name"].lower() in sponsor_names: why = "sponsor line, relationship map"
        elif FRONT.search(p["title"]): why = "contact-center title, sponsor's world"
        elif not p["email"]: why = "no email in Salesforce"
        mkt.append({"account": g["sf_company"], "sf_account_id": g["sf_account_id"], "name": p["name"], "title": p["title"], "email": p["email"], "lead_status": p["lead_status"], "include": "no" if why else "yes", "reason": why, "source": "Salesforce (Audiences, Sep 11 2026); marketing's own data, not re-verified"})
out_csv = pathlib.Path.home() / "Desktop/Intradiem Deliverables/Elevance Health - Known Layer for Marketing - Sep 11.csv"
with open(out_csv, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(mkt[0].keys())); w.writeheader(); w.writerows(mkt)

# Validated emails from the Work Email routine (Sep 11 2026)
validated = {}; runinfo = {}
rp = DATA / "_email_runs/result.json"
if rp.exists():
    d = json.loads(rp.read_text())
    for x in d.get("data", []):
        em = (x.get("result") or {}).get("Work Email") or ""
        validated[x["id"]] = em
    try:
        b = json.loads((DATA / "_email_runs/balance_before.json").read_text())["balance"]; a = json.loads((DATA / "_email_runs/balance_after.json").read_text())["balance"]
        runinfo = {"date": TODAY, "method": "Clay Work Email routine fed LinkedIn URL + name + elevancehealth.com", "found": sum(1 for v in validated.values() if v), "of": len(validated), "credits": round(b - a, 1)}
    except Exception: runinfo = {"date": TODAY, "found": sum(1 for v in validated.values() if v), "of": len(validated)}
ID = {"felicia-norwood": "Felicia Norwood", "blake-main": "Blake Main", "melissa-wise": "Melissa Wise", "holly-huffman": "Holly Huffman", "nicole-keating": "Nicole Keating, MBA, CLP, CSA", "kathy-talnose": "Kathy Talnose", "traci-caldwell": "Traci G.", "natasha-lefear": "Natasha Lefear"}
PATTERN = re.compile(r"^[a-z]+\.[a-z\-']+@(elevancehealth|anthem)\.com$|^[a-z]+[a-z]@elevancehealth\.com$")
emails = {}
for k, n in ID.items():
    em = validated.get(k, "")
    last = re.sub(r"[^a-z]", "", n.split(",")[0].split()[-1].lower())
    st = "validated" if em and PATTERN.match(em) else ("off-pattern, rejected" if em else "not found")
    if st == "validated" and last not in em.split("@")[0].replace(".", ""): st = "validated, surname differs; confirm"   # Holly Huffman came back as holly.pennington (LinkedIn slug hollymcneely)
    emails[n] = {"email": em, "status": st}
for r in bo_rows:
    if r["name"] in emails: r["email"] = emails[r["name"]]["email"] if emails[r["name"]]["status"].startswith("validated") else ""; r["email_status"] = emails[r["name"]]["status"]

facts = [
 ("Contract", "December 2016 Anthem, Inc. Master Services Agreement and Order Form: a 350-seat proof of concept scaling to 3,500 rollout seats, $836,000 total order value, staffing and coaching modules with implementation services; term through May 2018 with automatic renewal. Current seats, ACV, renewal date and live modules: not confirmed.", "Alex's account plan, sources 1 and 2 (fully executed contract documents)"),
 ("Salesforce", "No parent Elevance Health or Anthem Inc. record. The customer lives as 18 plan and subsidiary accounts (Amerigroup 106 known people, Anthem BCBS Virginia 35, Empire BCBS 32, Beacon Health Options 28, Carelon Health 26, Anthem BCBS Missouri 21, BCBS Wisconsin 18, and eleven smaller), 303 known people, nearly all under one owner, Account Type Prospect or blank. Customer status comes from the install base.", "Audiences read, Sep 11 2026, 0 credits"),
 ("Leadership, Feb 26 2026", "Mark Kaye (EVP and CFO) added Carelon oversight; Felicia Norwood (EVP, Chief Health Benefits Officer) took the newly consolidated Health Benefits organization; Peter Haytaian left the Carelon presidency effective May 4.", "Elevance Health newsroom, Feb 26 2026"),
 ("Leadership, Mar 31 2026", "Aimée Dailey President, Government Business; Kristy Duffey President, Carelon Health; Will Feest President, Carelon Insights and COO, Carelon; William Fleming Chief Growth and Strategy Officer, Carelon; Darrell Oliveira CFO, Carelon; Jeff Plante CFO, Health Benefits.", "Elevance Health newsroom, Mar 31 2026"),
 ("Q2 2026", "Operating revenue $49.8 billion; Health Benefits $42.7 billion; Carelon $19.2 billion, up 6 percent; benefit expense ratio 89.7 percent, up 80 basis points; medical membership down about 469,000 sequentially with Medicare Advantage, Medicaid and ACA attrition anticipated; opex up on targeted workforce investment; FY2026 adjusted EPS guidance raised to at least $27.", "Elevance Q2 2026 results, Jul 15 2026, via Alex's account plan"),
 ("AI program", "Ratnakar Lavu, EVP and Chief Digital and Information Officer, owns the AI roadmap, which includes claims-processing automation and internal productivity tools alongside member-facing AI. This is the in-house automation program the back-office conversation will meet, not a card on the map.", "Fortune, Feb 25 2026; MedCity News, Feb 2026"),
 ("Relationship map", "Alex's Elevance Health map holds 30 cards, all on the contact-center line (Boudreaux, Norwood, Kendrick, Backofen, Wade and the workforce teams under them), with Carelon people as placeholder cards. Four cards need a refresh.", "Sales Navigator, shared Sep 11 2026"),
]

out = {"account": "Elevance Health", "am": "Alex Bauer", "as_of": TODAY, "sponsor_line": sponsor_line,
       "am_map": am, "bo_maps": bo_rows, "bench_count": len(bench), "removed": [{"account": r["account"], "name": r["full_name"], "title": r["title"], "why": r["excluded_reason"]} for r in removed],
       "known_groups": known_groups, "known_total": len(known), "marketing_csv": {"path": str(out_csv), "rows": len(mkt), "included": sum(1 for m in mkt if m["include"] == "yes")},
       "emails": emails, "email_validation": runinfo, "facts": [{"k": k, "line": l, "source": s} for k, l, s in facts]}
(DATA / "expansion_room_elevance.json").write_text(json.dumps(out, indent=1))
print("am", len(am), "sponsor line", len(sponsor_line), "| bo", len(bo_rows), "removed", len(removed), "| known", len(known), "groups", len(known_groups), "| mkt rows", len(mkt), "included", out["marketing_csv"]["included"], "| emails", {k: v["status"] for k, v in emails.items()})
