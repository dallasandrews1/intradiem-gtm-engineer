#!/usr/bin/env python3
"""Refresh the live register block in AI_PMO_Extractor.src.html from the PMO files.

Reads automation/pmo/validation_queue.csv and automation/logs/.pmo-actions-state in the
main checkout, keeps Dallas-owned rows that are not past due and name nobody but Naveen,
and rewrites everything between <!--PMO_ROWS--> and <!--/PMO_ROWS--> plus the stat
placeholders. Run before build_pages.py after each extractor run.
"""
import csv, html, pathlib, re, datetime

MAIN = pathlib.Path("/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer")
Q = MAIN / "automation/pmo/validation_queue.csv"
STATE = MAIN / "automation/logs/.pmo-actions-state"
SRC = pathlib.Path(__file__).with_name("AI_PMO_Extractor.src.html")

rows = list(csv.DictReader(Q.open()))
today = datetime.date.today().isoformat()
graded = [r for r in rows if r["verdict"]]
correct = sum(1 for r in graded if r["verdict"] == "correct")
prec = round(100 * correct / len(graded)) if graded else 0
breakdown = {v: sum(1 for r in graded if r["verdict"] == v) for v in ("wrong_owner", "wrong_date", "not_an_action", "duplicate")}
by_src = {s: sum(1 for r in rows if r["source_type"] == s) for s in ("otter", "email", "calendar", "monday")}

others = {n for r in rows for n in r["owner"].split() if r["owner"] not in ("Dallas", "unassigned", "Naveen")}
others |= {"Melissa", "Chris", "Jeremy", "Eric", "Connor"}
def names_other(r):
    t = r["action"] + " " + r["evidence"]
    return any(re.search(r"\b" + re.escape(n) + r"\b", t) for n in others)
shown = [r for r in rows if r["owner"] == "Dallas"
         and not (r["due"] not in ("none stated", "") and r["due"] < today)
         and not names_other(r)]
mine = sum(1 for r in rows if r["owner"] == "Dallas")

def cell(r):
    verdict = r["verdict"] or "not yet graded"
    cls = {"correct": "ok", "": "na"}.get(r["verdict"], "bad")
    due = r["due"] + ("" if r["due_basis"] == "explicit" or r["due"] == "none stated" else " (inferred)")
    return ("<tr><td class=\"id\">%s</td><td>%s</td><td class=\"st\">%s</td><td>%s</td><td class=\"ev\">&ldquo;%s&rdquo;</td><td class=\"st\">%s</td><td class=\"v %s\">%s</td></tr>"
            % (html.escape(r["id"][-3:]), html.escape(r["action"]), html.escape(due), html.escape(r["source_type"]),
               html.escape(r["evidence"][:160]), html.escape(r["confidence"]), cls, html.escape(verdict)))

block = "<!--PMO_ROWS-->\n" + "\n".join(cell(r) for r in shown) + "\n<!--/PMO_ROWS-->"
t = SRC.read_text()
t = re.sub(r"<!--PMO_ROWS-->.*?<!--/PMO_ROWS-->", block, t, flags=re.S)
stats = {
    "TOTAL": str(len(rows)), "GRADED": str(len(graded)), "CORRECT": str(correct), "PREC": str(prec),
    "SHOWN": str(len(shown)), "MINE": str(mine), "STATE": STATE.read_text().strip()[:16].replace("T", " "),
    "OTTER": str(by_src["otter"]), "EMAIL": str(by_src["email"]), "CAL": str(by_src["calendar"]), "MON": str(by_src["monday"]),
    "WD": str(breakdown["wrong_date"]), "WO": str(breakdown["wrong_owner"]), "NA": str(breakdown["not_an_action"]), "DUP": str(breakdown["duplicate"]),
    "TODAY": datetime.date.today().strftime("%b %-d %Y"),
}
for k, v in stats.items():
    t = re.sub(r"(<!--S:%s-->).*?(<!--/S-->)" % k, r"\g<1>%s\g<2>" % v, t, flags=re.S)
SRC.write_text(t)
print("rows shown %d of %d Dallas-owned, %d total; graded %d, precision %d%%" % (len(shown), mine, len(rows), len(graded), prec))
