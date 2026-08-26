#!/usr/bin/env python3
"""Build the Back Office Account Map roster for Inger's 12 accounts.

Inputs
  automation/inbox/salesnav/inger/transcribed/map_*.csv   (AM Relationship Map transcriptions)
  motions/back_office_expansion/inger_known_layer_people.csv (Salesforce-known contacts, 0-credit Audiences pull)
  Back_Office_*_Jul26.csv at the main repo root                (the 285 net-new pull; only Goldman/MetLife/Prudential overlap)

Output
  motions/back_office_expansion/BO_AccountMap_Roster_Inger.csv
  motions/back_office_expansion/inger_roster_summary.md

Gates (in order; fail any and the row holds for the AM)
  1 known_to_intradiem   : on the AM's map with a CRM badge, or matches a Salesforce contact by name/email
  2 sponsor_line_conflict: reports to the same leader as a known contact (map cards only; sourced rows = unknown)
  3 band                 : SVP..Director in a back-office function, or a distinct-line top officer (CAO-type)
Nothing here spends a credit or touches Clay/Lemlist. Roster only.
"""
import csv, glob, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.expanduser("~/Claude/Projects/Intradiem GTM Engineer")
INBOX = os.path.join(MAIN, "automation/inbox/salesnav/inger/transcribed")
KNOWN = os.path.join(HERE, "inger_known_layer_people.csv")
OUT = os.path.join(HERE, "BO_AccountMap_Roster_Inger.csv")
SUMMARY = os.path.join(HERE, "inger_roster_summary.md")
AM = "Inger Escamilla"

ACCOUNT_ALIASES = {
    "assurant": "Assurant", "cleveland clinic": "Cleveland Clinic", "cox": "Cox Communications",
    "directv": "DIRECTV", "guardian": "Guardian Life", "goldman": "Goldman Sachs", "mckesson": "McKesson",
    "metlife": "MetLife", "prudential": "Prudential Financial", "rogers": "Rogers Communications",
    "travelers": "Travelers", "zurich": "Zurich North America",
}

def canon_account(name):
    n = (name or "").lower()
    for k, v in ACCOUNT_ALIASES.items():
        if k in n:
            return v
    return name.strip()

def norm(s):
    """first+last token key, credentials and middle initials stripped, so 'John L. Bertrand' == 'John Bertrand'"""
    n = re.sub(r"[,(].*$", "", s or "")
    n = re.sub(r"\b(mba|cpa|jr|sr|ii|iii|phd|clms|rmc|cep|arm|msf|rhia|dnp|rn|ne-bc|faan|lssbb|pmp|pspo|cma|cpcu|cris|ccla)\b\.?", "", n, flags=re.I)
    t = [x for x in re.sub(r"[^a-z ]", "", n.lower()).split() if len(x) > 1]
    return (t[0] + t[-1]) if len(t) >= 2 else (t[0] if t else "")

# ---- band + function inference from title text -------------------------------------------------
BAND_RULES = [
    ("EVP", r"\b(evp|executive vice president)\b"),
    ("SVP", r"\b(svp|senior vice president|sr\.? vice president|sr\.? vp)\b"),
    ("Director", r"\b(avp|assistant vice president|director|dir\.?|directora)\b"),   # AVP sits at Director level in practice
    ("VP", r"\b(vp|vice president|head of|global head|managing director|md)\b"),
    ("C", r"\b(chief|ceo|coo|cfo|cao|cio|cto|chro|president|chairman|chairwoman)\b"),
    ("Manager", r"\b(manager|mgr|lead|supervisor|specialist|analyst|engineer|coordinator|associate|representative|agent|expert)\b"),
]
BACK_OFFICE = r"(shared services|claims|fraud|payment|payments|disputes|billing|collections|underwriting|appeals|procurement|accounts payable|accounts receivable|treasury|finance operations|financial operations|back office|back-office|administration|administrative|operations|document|processing|enrollment|servicing|settlement|reconciliation)"
CONTACT_CENTER = r"(contact center|call center|customer care|customer service|customer experience|cx|workforce management|wfm|workforce planning|voice services|service delivery|omnichannel|support center)"
TECH = r"(technology|engineer|software|it\b|information|data|digital|architect|network|systems|infrastructure|analytics|learning|training|enablement|hr\b|human resources|talent|real estate|facilit|marketing|sales|legal|counsel|risk|compliance|audit)"

def infer_band(title):
    t = (title or "").lower()
    for band, rx in BAND_RULES:
        if re.search(rx, t):
            return band
    return "Unknown"

def infer_function(title):
    t = (title or "").lower()
    if re.search(CONTACT_CENTER, t):
        return "contact_center"
    if re.search(BACK_OFFICE, t):
        return "back_office"
    if re.search(TECH, t):
        return "tech_or_other"
    return "unknown"

def in_band(band):
    return band in ("SVP", "VP", "Director")

# ---- load known layer -----------------------------------------------------------------------------
known_names = defaultdict(set)   # account -> {norm name}
known_emails = set()
known_rows = 0
if os.path.exists(KNOWN):
    for r in csv.DictReader(open(KNOWN)):
        known_rows += 1
        known_names[canon_account(r.get("account"))].add(norm(r.get("full_name")))
        e = (r.get("email") or "").strip().lower()
        if e:
            known_emails.add(e)

# ---- load map transcriptions ----------------------------------------------------------------------
maps = []
for f in sorted(glob.glob(os.path.join(INBOX, "map_*.csv"))):
    for r in csv.DictReader(open(f)):
        r["_file"] = os.path.basename(f)
        r["account"] = canon_account(r.get("account"))
        maps.append(r)

# ---- load the Jul 26 sourced rows for the overlapping accounts ------------------------------------
sourced = []
for f in glob.glob(os.path.join(MAIN, "Back_Office_*_Jul26.csv")):
    lane = os.path.basename(f).replace("Back_Office_", "").replace("_Jul26.csv", "")
    for r in csv.DictReader(open(f)):
        acct = canon_account(r.get("Company"))
        if acct in ("Goldman Sachs", "MetLife", "Prudential Financial"):
            sourced.append({"account": acct, "full_name": r["Full Name"], "title": r["Job Title"],
                            "email": r.get("Work Email", ""), "linkedin_url": r.get("LinkedIn Profile", ""),
                            "lane": lane})

# ---- assemble --------------------------------------------------------------------------------------
cols = ["account", "am_owner", "full_name", "title", "title_truncated", "function", "band", "reports_to",
        "tree_depth", "source", "crm_badge", "known_to_intradiem", "sponsor_line_conflict", "band_ok",
        "gate_result", "owner_cleared", "sequence_state", "email", "linkedin_url", "notes"]
out = []

# map-derived rows, grouped per account to compute conflict lines
by_acct = defaultdict(list)
for r in maps:
    by_acct[r["account"]].append(r)

for acct, rows in by_acct.items():
    canvas = [r for r in rows if (r.get("source") or "map") == "map"]
    parent_of = {r["full_name"]: (r.get("reports_to") or "") for r in canvas}
    # every card the AM placed on her map is known to Intradiem by definition (placeholder cards included);
    # the CRM badge only tells us whether Salesforce has the record too
    is_known = {r["full_name"]: True for r in canvas}
    # leaders who have at least one known direct report = the sponsor lines
    sponsor_leaders = {parent_of[n] for n, k in is_known.items() if k and parent_of.get(n)}
    for r in rows:
        name = r["full_name"]
        src = r.get("source") or "map"
        k = is_known.get(name, norm(name) in known_names.get(acct, set()))
        leader = parent_of.get(name, "")
        conflict = "yes" if (leader and leader in sponsor_leaders) or (name in sponsor_leaders) else ("no" if src == "map" else "unknown")
        band = infer_band(r.get("title"))
        func = infer_function(r.get("title"))
        band_ok = "yes" if in_band(band) else ("top_officer" if band in ("C", "EVP") else "no")
        if k:
            gate = "KNOWN_do_not_touch"
        elif conflict == "yes":
            gate = "CONFLICT_am_decides"
        elif band_ok == "no":
            gate = "HOLD_below_band"
        elif func == "contact_center":
            gate = "HOLD_contact_center_line"
        else:
            gate = "CANDIDATE"
        out.append({
            "account": acct, "am_owner": AM, "full_name": name, "title": r.get("title", ""),
            "title_truncated": r.get("title_truncated", ""), "function": func, "band": band,
            "reports_to": leader, "tree_depth": r.get("tree_depth", ""), "source": f"am_map:{src}",
            "crm_badge": r.get("crm_status", ""), "known_to_intradiem": "yes" if k else "no",
            "sponsor_line_conflict": conflict, "band_ok": band_ok, "gate_result": gate,
            "owner_cleared": "pending_owner" if gate == "CANDIDATE" else "", "sequence_state": "",
            "email": "", "linkedin_url": "", "notes": r.get("notes", ""),
        })

# sourced rows (Jul 26 pull) for the three overlapping accounts
map_names = {(r["account"], norm(r["full_name"])) for r in out}
for s in sourced:
    key = (s["account"], norm(s["full_name"]))
    if key in map_names:
        continue  # already represented by the AM's map row
    k = norm(s["full_name"]) in known_names.get(s["account"], set()) or (s["email"] or "").lower() in known_emails
    band = infer_band(s["title"]); func = infer_function(s["title"])
    band_ok = "yes" if in_band(band) else ("top_officer" if band in ("C", "EVP") else "no")
    if k:
        gate = "KNOWN_do_not_touch"
    elif band_ok == "no":
        gate = "HOLD_below_band"
    elif func == "contact_center":
        gate = "HOLD_contact_center_line"
    else:
        gate = "CANDIDATE"
    out.append({
        "account": s["account"], "am_owner": AM, "full_name": s["full_name"], "title": s["title"],
        "title_truncated": "no", "function": func, "band": band, "reports_to": "", "tree_depth": "",
        "source": f"clay_jul26:{s['lane']}", "crm_badge": "", "known_to_intradiem": "yes" if k else "no",
        "sponsor_line_conflict": "unknown", "band_ok": band_ok, "gate_result": gate,
        "owner_cleared": "pending_owner" if gate == "CANDIDATE" else "", "sequence_state": "",
        "email": s["email"], "linkedin_url": s["linkedin_url"], "notes": "reports_to unknown until placed on the AM map",
    })

out.sort(key=lambda r: (r["account"], r["gate_result"] != "CANDIDATE", r["band"], r["full_name"]))
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(out)

# ---- summary ----------------------------------------------------------------------------------------
lines = [f"# Inger roster summary\n", f"Known layer rows loaded: {known_rows}. Map files: {len(glob.glob(os.path.join(INBOX, 'map_*.csv')))}. Roster rows: {len(out)}.\n",
         "| Account | map cards | known | conflict | candidates | held (band/CC) | sourced Jul26 |", "|---|---|---|---|---|---|---|"]
accts = sorted({r["account"] for r in out})
for a in accts:
    rs = [r for r in out if r["account"] == a]
    mc = sum(1 for r in rs if r["source"].startswith("am_map:map"))
    kn = sum(1 for r in rs if r["gate_result"] == "KNOWN_do_not_touch")
    cf = sum(1 for r in rs if r["gate_result"] == "CONFLICT_am_decides")
    cd = sum(1 for r in rs if r["gate_result"] == "CANDIDATE")
    hd = sum(1 for r in rs if r["gate_result"].startswith("HOLD"))
    sc = sum(1 for r in rs if r["source"].startswith("clay_jul26"))
    lines.append(f"| {a} | {mc} | {kn} | {cf} | {cd} | {hd} | {sc} |")
lines.append("\n## Sponsor-line leaders per account (rule 1: nobody who reports into these is touched without the AM)\n")
for a in accts:
    canvas = [r for r in out if r["account"] == a and r["source"] == "am_map:map"]
    leaders = []
    for r in canvas:
        if r["tree_depth"] == "0" or any(c["reports_to"] == r["full_name"] for c in canvas):
            leaders.append(f"{r['full_name']} ({r['title'][:40]})")
    funcs = sorted({r["function"] for r in canvas})
    lines.append(f"- **{a}**: {'; '.join(leaders)}. Map functions: {', '.join(funcs)}.")
missing = [a for a in ACCOUNT_ALIASES.values() if a not in accts]
if missing:
    lines.append(f"\nNo map transcribed yet for: {', '.join(missing)}")
open(SUMMARY, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
