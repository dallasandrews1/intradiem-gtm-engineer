#!/usr/bin/env python3
"""Verified list CSV for the Cleveland Clinic marketing lane (Inger passes it to Nicole). The brief page was retired Sep 11 2026; the lane lives on Inger's page."""
import json, pathlib, shutil, csv, html as H
HERE = pathlib.Path(__file__).parent; BO = HERE.parent / "back_office_expansion"
d = json.loads((HERE / "data/save_room_cleveland_clinic.json").read_text()); plan = json.loads((HERE / "data/comms_plan_cleveland_clinic.json").read_text())
fonts = (BO / "_fonts_embed.css").read_text(); logo = (BO / "_logo_symbol.svg").read_text()
CSS = (HERE / "build_page.py").read_text().split('CSS = """')[1].split('"""')[0]
def e(s): return H.escape(str(s or ""))
INCLUDE_TRACKS = {"Stakeholder"}  # IT and RFP names only; sponsor line, executives, back-office and clinical names are out of the one-pager
EXCLUDE_WHY = {"Inger": "sponsor line, Inger only", "Hold, then exec": "executive note held; no marketing touch until it is sent", "Back office": "expansion track, separate sequence", "Nurture": "clinical or HR, no reason to receive a contact-center one-pager", "Bench": "clinical, out"}
# Verified list: Inger's names with verified or Salesforce email (excluding the sponsor line, which marketing never touches)
rows = []; excluded = []
for r in d["inger"]:
    em = r.get("email_validated") or r["email"]
    if not em or r["bridge"] == "departed": continue
    if r["track"] in INCLUDE_TRACKS:
        rows.append({"full_name": r["name"], "title": (r["title_live"] or r["title_inger"]).split(" (")[0], "email": em,
                     "email_source": "checked Sep 2026 (work-email verification)" if r.get("email_validated") else "Salesforce, checked Sep 2026",
                     "linkedin": r["linkedin"], "company": "Cleveland Clinic", "group": "IT and RFP"})
    else: excluded.append((r["name"], EXCLUDE_WHY.get(r["track"], r["track"])))
SPONSOR_LINE = {"rena thompson", "shantel adams", "linda reid", "mary kay pienta", "adam gilbert", "eric kokochak", "lisa yerian"}
known_marketable = [k for k in d["known"] if k["email"] and k["title"] and k["name"].lower() not in SPONSOR_LINE and "@" in k["email"]]
for k in known_marketable:
    rows.append({"full_name": k["name"], "title": k["title"], "email": k["email"], "email_source": "Salesforce (marketing's own records, not re-verified)", "linkedin": k["linkedin"],
                 "company": "Cleveland Clinic", "group": "Salesforce-known contact center and IT"})
out_csv = HERE / "data/Cleveland_Clinic_Verified_List_Nicole_Sep11.csv"
with open(out_csv, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
shutil.copy(out_csv, pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic - Verified List for Nicole - Sep 11.csv")
print(out_csv, "rows", len(rows))
