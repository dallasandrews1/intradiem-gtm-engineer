#!/usr/bin/env python3
"""Assembles data/save_room_cleveland_clinic.json from the three contact layers, the health evidence,
the 30/60/90, and the open items (PMO tracker schema). Re-run after any source changes."""
import csv, json, pathlib, re, datetime
HERE = pathlib.Path(__file__).parent; DATA = HERE / "data"; DATA.mkdir(exist_ok=True)
BO = HERE.parent / "back_office_expansion"
TODAY = "2026-09-10"

# Layer 1: Salesforce-known (Audiences pull, Aug 25 2026, 0 credits)
known = [r for r in csv.DictReader(open(BO / "inger_known_layer_people.csv")) if r["account"].lower().startswith("cleveland")]
def clean(n): return re.sub(r"\s+", " ", (n or "")).strip()
known_rows = [{"name": clean(r["full_name"]), "title": clean(r["title"]), "email": (r["email"] or "").strip().lower(),
               "linkedin": r["linkedin_url"], "lead_status": r["lead_status"], "source": "Salesforce (Audiences, Aug 25 2026)"}
              for r in known if clean(r["full_name"]) and clean(r["full_name"]).lower() != "not provided" and "@" not in clean(r["full_name"]) and " " in clean(r["full_name"])]

# Email pattern from the known layer: <last><first initial>@ccf.org (27 of 35 parseable; numeric suffix on collisions)
def infer_email(name):
    parts = [p for p in re.split(r"[\s\-]+", re.sub(r"\(.*?\)|,.*$", "", name).lower()) if p and p not in ("f.", "md", "mba")]
    if len(parts) < 2: return ""
    return f"{parts[-1]}{parts[0][0]}@ccf.org"

# Layer 2: Inger's research (PDF, Sep 10 2026) with the zero-credit Clay bridge result
inger = [
 # name, Inger's title, bridge result title, linkedin, bridge status, layer, save role, track
 ("Rena Thompson", "Director, Enterprise Contact Center Operations", "Senior Director of Operations (Salesforce)", "", "in Salesforce", "known", "Sponsor. Owns the savings conversation.", "Inger"),
 ("Scott Faini", "IT Product Director, Unified Communications", "Sr. Director Unified Communications (Salesforce)", "", "in Salesforce", "known", "RFP voice. Platform continuity.", "Stakeholder"),
 ("Katherine Neal", "IT Director and Product Owner, Access Innovations", "Senior IT Solutions Architect, Patient Access, Patient Experience and Revenue Cycle Management (since Jul 2025)", "https://www.linkedin.com/in/kate-neal95/", "found, title differs", "new", "RFP evaluator, technical. Title on LinkedIn is architect, not director.", "Stakeholder"),
 ("Bob Ganem", "ITD Director and Product Owner", "ITD Director Product Owner (since Jun 2022)", "https://www.linkedin.com/in/bob-ganem-92509921/", "found, confirmed", "new", "RFP evaluator", "Stakeholder"),
 ("Leslie Chom", "Director and Product Owner, Patient and Caregiver Computing", "Retired (LinkedIn headline, Sep 11 2026)", "https://www.linkedin.com/in/leslie-chom-2067473/", "departed", "new", "Retired. Off the list.", "Off"),
 ("Terri Horan", "Product Owner, Patient Journey (Digital Health)", "Product Owner Patient Journey, Digital Health (since Sep 2018)", "https://www.linkedin.com/in/terri-horan-b0474851/", "found, confirmed", "new", "Patient-experience angle on agent time", "Stakeholder"),
 ("Dennis Laraway", "EVP and Chief Financial Officer", "EVP and CFO since Mar 2023 (Cleveland Clinic newsroom)", "", "confirmed on the web", "new", "Economic buyer. Only after the reviewed number holds.", "Hold, then exec"),
 ("Bill Peacock", "EVP and Chief of Operations", "EVP, Chief of Operations (Cleveland Clinic leadership page)", "", "confirmed on the web", "new", "Top of operations. Mary Ann's touch, same gate.", "Hold, then exec"),
 ("Kelly Hancock", "EVP, Chief Caregiver Officer and Chief Administrative Officer", "on the back-office map, card 20", "https://www.linkedin.com/in/k-kelly-hancock-dnp-rn-ne-bc-faan-93325974/", "on back-office map", "map", "Distinct line from the sponsor. Expansion, not the save.", "Back office"),
 ("Emily Monteleone", "Director of Strategic Workforce Planning", "on the back-office map, card 17", "https://www.linkedin.com/in/emily-monteleone-52631a2a/", "on back-office map", "map", "Workforce planning lane", "Back office"),
 ("Rebecca Vance", "Senior HR Director, Connected Care, Nursing and Pharmacy", "Senior Director, HR Services (since May 2024)", "https://www.linkedin.com/in/rebeccalvance/", "found, confirmed", "new", "Caregiver office, consulted on workforce", "Nurture"),
 ("Meredith Foxx", "SVP and Enterprise Chief Nursing Officer", "Senior Vice President (since Jun 2020)", "https://www.linkedin.com/in/meredith-foxx-4306b7108/", "found, confirmed", "new", "Triage lines, burnout. Low fit for the save.", "Nurture"),
 ("Sonya Pease", "Chief of Quality, Safety and Patient Experience, Florida", "Chief Quality, Safety and Patient Experience Officer, Cleveland Clinic Florida (since Jun 2019)", "https://www.linkedin.com/in/sonya-pease-md-mba-cpxp-fasa-35685222/", "found, confirmed", "new", "Regional, clinical", "Bench"),
 ("F. Scott Ross", "Hospital operations, Florida", "Chief Medical Officer, Fort Lauderdale (since May 2021)", "https://www.linkedin.com/in/scott-ross-1717ba1a6/", "found, title differs", "new", "Regional clinical leadership, not operations as written", "Bench"),
 ("Richard Rothman", "Indian River, quality improvement", "VP and Chief Medical Officer, Indian River Hospital", "https://www.linkedin.com/in/richardrothmanmd/", "found, confirmed", "new", "Regional", "Bench"),
 ("David (surname not given)", "Florida Market", "", "", "cannot search", "new", "Needs a surname", "Bench"),
]
VALIDATED = {"Bob Ganem":"rganem@ccf.org","Terri Horan":"horant@ccf.org","Katherine Neal":"nealk@ccf.org","Rebecca Vance":"vancer@ccf.org",
             "Meredith Foxx":"foxxm@ccf.org","Sonya Pease":"peases@ccf.org","F. Scott Ross":"scottr@ccf.org",
             "Dennis Laraway":"larawayd@ccf.org","Bill Peacock":"peacockw@ccf.org","Richard Rothman":"rr@ccf.org",
             "Kelly Hancock":"hancockk@ccf.org","Emily Monteleone":"monteleonee@ccf.org"}  # Clay Work Email routine, Sep 10-11 2026, 12 of 12 searchable, 6.9 credits
inger_rows = []
for n, t_inger, t_live, url, status, layer, role, track in inger:
    email_known = next((k["email"] for k in known_rows if k["name"].lower().split()[-1] == n.lower().split()[-1] and k["name"].lower().split()[0][:3] == n.lower().split()[0][:3]), "")
    inger_rows.append({"name": n, "title_inger": t_inger, "title_live": t_live, "linkedin": url, "bridge": status, "layer": layer,
                       "role": role, "track": track, "email": email_known,
                       "email_inferred": "" if (email_known or layer not in ("new", "map") or status in ("cannot search", "departed") or n in VALIDATED) else infer_email(n),
                       "email_validated": VALIDATED.get(n, "")})

# Layer 3: the back-office map (Aug 25 2026, 20 cards)
bo = [r for r in csv.reader(open(BO / "BO_Map_Build_Sheets_Inger.csv")) if r and r[0] == "Cleveland Clinic"]
bo_rows = [{"card": r[2], "depth": r[3], "name": r[4], "title": r[5], "level": r[6], "function": r[7], "reports_to": r[8], "linkedin": r[10], "flag": r[12], "lane": r[16] if len(r) > 16 else ""} for r in bo]

# Health evidence: reason code -> status + evidence lines (source, date, line)
health = {
 "as_of": TODAY, "overall": "RED",
 "codes": [
  {"code": "Value dispute", "status": "RED", "evidence": [
    ("Success Plan notes", "2025-11-06", "Success review stopped at slide five; customer challenged savings accuracy, unmet feature commitments and open cases, said extra staff was needed to run Intradiem."),
    ("Success Plan, Active sheet", "2025-11-18", "Investment Return Review and Agreement opened, priority High, no status recorded since."),
    ("Sep 2026 adoption deck", "2026-09-07", "Deck still reports $719K YTD savings and 1.9x; the customer has not agreed the method.")]},
  {"code": "Sponsor silence", "status": "RED", "evidence": [
    ("Success Plan notes", "2025-11-11", "Weekly meeting cancelled by Shantel."),
    ("Success Plan notes", "2025-12-17", "Adoption review cancelled by Shantel; deck sent instead."),
    ("Success Plan notes", "2025-12-30", "Weekly meeting cancelled (Mary Kay)."),
    ("Inger, Sep 10 call", "2026-09-10", "Rena accepts meetings then cancels day-of or the day before; Shantel declines any new-product conversation and will not name contacts.")]},
  {"code": "Adoption decline", "status": "RED", "evidence": [
    ("Sep 2026 adoption deck", "2026-09-07", "Dynamic session accept 17.8% against a 75% goal; 10% of agents receiving dynamic sessions against 80%; 7% of agents coached against 80%."),
    ("Success Plan, Active sheet", "2026-06-12", "End of Shift rules paused; Leave Early rules paused the same day, reason not recorded."),
    ("Success Plan, Active sheet", "2024-12-10", "Enhanced Staffing (VTO and VOT) on hold: current Verint version not compatible."),
    ("Sep 2026 adoption deck", "2026-09-07", "13 of 17 contracted use cases deployed. Bright spots: coaching acceptance 83%, AUX self-cure 94%.")]},
  {"code": "Open case aging", "status": "YELLOW", "evidence": [
    ("Success Plan notes", "2025-11-18", "Four open cases: 00322148, 00321545, 00321947, 00321814."),
    ("Success Plan notes", "2025-12-16", "SSO token expiry issue may not resolve until after the new year; case 323900 (agents kicked out of the IDE) opened 12/11."),
    ("Success Plan, Active sheet", TODAY, "Open Cases section is empty; current case status has to be confirmed with Amy.")]},
  {"code": "Executive change", "status": "GREEN", "evidence": [
    ("Sales Nav bridge", "2026-08-25", "Michael Waterman retired, removed from the map. No change recorded for Thompson, Adams, Yerian or Faini."),
    ("Clay bridge", TODAY, "Katherine Neal is a Senior IT Solutions Architect since Jul 2025, not the director title in the research.")]},
  {"code": "Competitive event", "status": "RED", "evidence": [
    ("Inger, Sep 10 call", "2026-09-10", "RFP out for the CCaaS stack. Harmonic migration conversations starting. Read: one-year renewal, migration, then exit unless the experience changes.")]},
  {"code": "Renewal clock", "status": "RED", "evidence": [
    ("Inger, Sep 10 call", "2026-09-10", "Renewal in January 2027; two options presented, none signed. 113 days to Jan 1.")]},
 ]}

plan = [
 ("To Oct 10", "Settle the number, staff the room", "ROI line-by-line with Shantel closes (Amy, Matt). Case closure dates in writing. Coach Now supervisors on record. Save Room live, owners assigned in Inger's brainstorm, digest starts the Monday after."),
 ("To Nov 9", "Continuity with the RFP evaluators", "Faini, Ganem, Horan and Neal hear platform continuity from Inger and one technical voice. Harmonic presented as continuity, not a project. Executive review with Yerian. CFO note only if the reviewed number holds."),
 ("To Dec 9", "Option chosen, expansion separated", "Renewal option selected. Hancock line approached as back-office expansion, on its own track, after the renewal conversation is stable."),
]

# Open items in the PMO Progress tracker schema (Project Task Tracker.csv export, Sep 10 2026)
TRACKER_COLS = ["Project Name","Task Name","Task Description","Task Due Date","Task Progress","Assigned To","Notes","Additional Assignees","Archive?","Link to Item","Edit Task"]
items = [
 ("Investment Return Review", "Align on investment-return method and validate the savings line by line with Shantel", "10/10/2026", "In progress", "Amy Johnson;Matt McConnell", "Open since 11/18/2025 (Success Plan, priority High). Committed at the 11/6/2025 success review."),
 ("Investment Return Review", "Review the original business case against current performance; set savings expectations the customer accepts", "10/10/2026", "Not started", "Mary Ann Chandler;Matt McConnell", "11/6/2025 commitment."),
 ("Open Cases", "Confirm status of cases 00322148, 00321545, 00321947, 00321814, 323900 and give CCF a closure timeline in writing", "9/25/2026", "Not started", "Amy Johnson", "Open Cases section of the Success Plan is empty as of 9/8/2026."),
 ("Paused Rules", "Record why End of Shift and Leave Early rules were paused 6/12/2026 and what would restart them", "9/25/2026", "Not started", "Amy Johnson", "Success Plan Active sheet."),
 ("User Proof", "Collect two-sentence statements from supervisors using Coach Now (83% acceptance) and teams self-curing AUX alerts", "10/10/2026", "Not started", "Amy Johnson;Inger Escamilla", "Inger's bottom-up track. Feeds the impact summary for Rena."),
 ("RFP Continuity", "Platform-continuity conversation with Scott Faini, Bob Ganem, Terri Horan and Katherine Neal", "11/9/2026", "Not started", "Inger Escamilla", "Verified line: sits on top of the existing WFM, integrates with Genesys Cloud, NICE and others. Katherine Neal is an architect, not a director. Leslie Chom not found at the domain; confirm in Sales Nav."),
 ("Harmonic Migration", "Present the migration as continuity, with the customer's open issues carried into the plan", "11/9/2026", "Not started", "Amy Johnson;Matt McConnell", "Inger: a bad migration experience is the exit trigger."),
 ("Executive Review", "Executive review with Lisa Yerian; CFO and COO notes only after the reviewed savings number holds", "11/9/2026", "Not started", "Mary Ann Chandler;Inger Escamilla", "Dennis Laraway and Bill Peacock not found at the domain by the free bridge; confirm in Sales Nav."),
 ("Save Room", "Cleveland Clinic Save Room live; weekly health watcher and Monday owner digest running", "9/19/2026", "In progress", "Dallas Andrews", "Page built 9/10/2026. Watcher staged, not loaded."),
 ("Contact Validation", "Validated work emails for the seven net-new names the free bridge found", "9/10/2026", "Completed", "Dallas Andrews", "Done 9/11/2026: 12 of 12 searchable names verified via the Clay Work Email routine, 6.9 credits. Leslie Chom shows retired on LinkedIn and is off the list; the Florida \"David\" has no surname."),
 ("Brainstorm", "Cleveland Clinic save brainstorm with Clint, Nicole and leadership; owners assigned live from this list", "9/25/2026", "Not started", "Inger Escamilla", "Sep 10 call. Dallas to attend with the Save Room."),
 ("Nurture", "Monthly one-pager to known contacts in lemlist; stakeholder sequence to net-new names after Inger clears them", "10/10/2026", "Not started", "Dallas Andrews;Nicole Garcia", "No loads until cleared. Content from marketing."),
]
open_items = [dict(zip(TRACKER_COLS, ["Cleveland Clinic", tn, td, due, prog, who, notes, "", "No", "", ""])) for tn, td, due, prog, who, notes in items]
with open(DATA / "Cleveland_Clinic_PMO_Tracker_Import.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=TRACKER_COLS); w.writeheader(); w.writerows(open_items)

out = {"account": "Cleveland Clinic", "sf_account_id": "001V5000006bHWPIA2", "domain": "clevelandclinic.org", "email_domain": "ccf.org",
       "am": "Inger Escamilla", "success_manager": "Amy Johnson", "customer_owner": "Shantel Adams", "sponsor": "Rena Thompson",
       "renewal": "January 2027", "as_of": TODAY, "known": known_rows, "inger": inger_rows, "bo_map": bo_rows, "health": health, "plan": plan, "open_items": open_items,
       "email_validation": {"date": TODAY, "method": "Clay Work Email routine (function t_0thx4ovuPGp8sjH2hPP) fed LinkedIn URL + name + ccf.org", "found": 12, "of": 12, "credits": 6.9, "runs": ["run_0tl610sVtNRxiYNudRU", "run_0tl611qBZshzes8yvyC", "run_0tl76g5N43Ag7w8Cooe", "run_0tl76klBXcafpRbffsk"]},
       "email_pattern": {"pattern": "<last><first initial>@ccf.org", "basis": "27 of 35 parseable Salesforce emails; numeric suffix on collisions (adamss8, reidl2)"}}
(DATA / "save_room_cleveland_clinic.json").write_text(json.dumps(out, indent=1))
# Evidence file the watcher scores
(DATA / "evidence_cleveland_clinic.json").write_text(json.dumps({"account": "Cleveland Clinic", "renewal_date": "2027-01-01", "as_of": TODAY, "codes": health["codes"]}, indent=1))
print("known", len(known_rows), "inger", len(inger_rows), "bo", len(bo_rows), "items", len(open_items))
print("net-new:", sum(1 for r in inger_rows if r["layer"]=="new"), "found:", sum(1 for r in inger_rows if r["bridge"].startswith("found")), "inferred emails:", sum(1 for r in inger_rows if r["email_inferred"]))
for r in inger_rows:
    if r["email_inferred"]: print("  ", r["name"], r["email_inferred"])
