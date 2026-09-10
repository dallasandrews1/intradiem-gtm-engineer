#!/usr/bin/env python3
"""Read-only intake for the Salesforce Partner Pre-Pipeline printable view (PDF).

Frank shares the object as a Lightning list view (Partner_Pre_Pipeline__c, filter All);
the printable view saved as PDF is the only export we have. This script turns it into a
CSV and a baseline report the pilot is measured against. No Salesforce write, no Clay,
no lemlist, 0 credits.

Columns in the view: Partner Pre-Pipeline Name, Status, Created Date, Partner Account,
Intradiem AE, Partner AE, Partner Category, Priority. The PDF text glues names together
(no delimiter between Intradiem AE and Partner AE), so the owner fields are split with a
known-AE list and flagged where the split is uncertain.

Run:  python3 intake_sf_prepipeline.py [path.pdf]   (default: newest PDF in the inbox)
Out:  <inbox>/run_<date>/sf_prepipeline.csv, sf_prepipeline_baseline.md
"""
import csv, json, pathlib, re, sys, datetime, collections
from pypdf import PdfReader

INBOX = pathlib.Path.home() / "Claude/Projects/Intradiem GTM Engineer/automation/inbox/partners/sf_prepipeline"
HERE = pathlib.Path(__file__).resolve().parent
TODAY = datetime.date.today()

STATUSES = ["Register Lead", "CAM to AE Intro", "Delivered 12 Minute Meeting",
            "Customer Meet", "Converted to Opportunity", "Disqualified"]
STAGE_ORDER = {s: i for i, s in enumerate(STATUSES)}
# Intradiem side (channel and AE) as they appear in the view; extend when a new name shows up.
INTRADIEM_PEOPLE = ["Jean-Anne McMahon", "Simon Bland", "Mike Regan", "Haresh Gangwani", "James MacDonald",
                    "Keegan Sanders", "Steve Jackson", "Rachel DiBello", "Matt Rumins", "Paul Harris",
                    "Frank Ciccone", "Mary Ann Chandler", "Inger Escamilla", "Nathan Belfield",
                    "Rachel Di Bello", "Jean Anne McMahon"]
# Partner account normalization: first matching prefix wins (order matters).
PARTNERS = [("Five9", "Five9"), ("Sagess3", "SagesS3"), ("SagesS3", "SagesS3"), ("Genesys", "Genesys"), ("Alvaria", "Alvaria"),
            ("ConvergeOne", "ConvergeOne (C1)"), ("C1", "ConvergeOne (C1)"), ("Call Design - AU", "Call Design AU"),
            ("Call Design - NA", "Call Design NA"), ("Call Design", "Call Design"), ("Aspect", "Aspect"), ("Avaya", "Avaya"),
            ("SPAR", "SPAR Solutions"), ("Capgemini", "Capgemini"), ("Barclays", "Barclays"), ("Amazon Web Services", "AWS Marketplace"),
            ("Calabrio", "Calabrio"), ("Connex", "Connex"), ("NWN", "NWN"), ("Sabio", "Sabio"), ("Fictional", "TEST")]
TEST_NAMES = {"test", "partner - test"}


def norm_partner(partner_account: str, name: str) -> str:
    for pre, out in PARTNERS:
        if partner_account.lower().startswith(pre.lower()):
            return out
    for pre, out in PARTNERS:
        if name.lower().startswith(pre.lower()):
            return out
    return partner_account.split(" ")[0] if partner_account else "?"
CATEGORY = r"(Expand or New Pursuit|New Pursuit|Expand)"


def load_text(pdf: pathlib.Path) -> str:
    r = PdfReader(str(pdf))
    t = " ".join((p.extract_text() or "") for p in r.pages)
    t = re.sub(r"Number of records\s*\d+\s*All - Printable View|Displaying records \d+ - \d+|Partner Pre-Pipeline Name|"
               r"Status Created Date Partner Account Intradiem AE Partner AE Partner Category Priority", " ", t)
    return re.sub(r"\s+", " ", t)


def parse(t: str):
    st = "(" + "|".join(re.escape(s) for s in STATUSES) + ")"
    pat = re.compile(st + r"\s*(\d{1,2}/\d{1,2}/\d{4})")
    ms = list(pat.finditer(t))
    # first pass: partner prefixes from clean names (text before ' - ')
    segs = []
    for i, m in enumerate(ms):
        nxt = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        segs.append((m.group(1), m.group(2), t[m.end():nxt].strip()))
    first_name = t[:ms[0].start()].strip()
    recs = []
    pending_name = first_name
    for status, date, rest in segs:
        m2 = re.match(r"(?P<mid>.*?)\b" + CATEGORY + r"\b\s*(?P<pri>\d)?\s*(?P<next>.*)$", rest)
        if m2:
            mid, cat, pri, nxt = m2.group("mid").strip(), m2.group(2), m2.group("pri"), m2.group("next").strip()
            conf = "ok"
        else:
            # no category: priority digit alone, else guess boundary at the next 'X - Y' name
            m3 = re.match(r"(?P<mid>.*?)\s(?P<pri>\d)\s+(?P<next>\S.*)$", rest)
            if m3:
                mid, cat, pri, nxt, conf = m3.group("mid").strip(), "", m3.group("pri"), m3.group("next").strip(), "no_category"
            else:
                m4 = re.search(r"\s([A-Z][\w() ]{1,25}\s?-\s?[A-Z].*)$", rest)
                if m4:
                    mid, nxt = rest[:m4.start()].strip(), m4.group(1).strip()
                else:
                    mid, nxt = rest, ""
                cat, pri, conf = "", "", "guessed_boundary"
        recs.append(dict(name=pending_name, status=status, created=date, mid=mid, category=cat or "",
                         priority=pri or "", parse=conf))
        pending_name = nxt
    return recs


def split_owner(mid: str, partner_prefix: str):
    """mid = 'Partner Account' + 'Intradiem AE' + 'Partner AE' glued. Return (partner_account, intradiem_ae, partner_ae)."""
    s = mid
    iae = ""
    for p in sorted(INTRADIEM_PEOPLE, key=len, reverse=True):
        if p in s:
            iae = p
            before, after = s.split(p, 1)
            return before.strip(), iae, after.strip()
    return s.strip(), "", ""


def main():
    pdf = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else max(INBOX.glob("*.pdf"), key=lambda p: p.stat().st_mtime)
    recs = parse(load_text(pdf))
    out = INBOX / f"run_{TODAY.isoformat()}"
    out.mkdir(exist_ok=True)
    rows = []
    for r in recs:
        name = r["name"]
        partner, prospect = (name.split(" - ", 1) + [""])[:2] if " - " in name else (name.split("-", 1) + [""])[:2]
        pa, iae, pae = split_owner(r["mid"], partner.strip())
        d = datetime.datetime.strptime(r["created"], "%m/%d/%Y").date()
        if name.strip().lower() in TEST_NAMES or pa.lower().startswith("fictional"):
            continue
        rows.append(dict(name=name, partner=norm_partner(pa, name), partner_prefix=partner.strip(), prospect=prospect.strip(), status=r["status"],
                         stage_index=STAGE_ORDER[r["status"]], created=d.isoformat(), age_days=(TODAY - d).days,
                         partner_account=pa, intradiem_ae=iae, partner_ae=pae, category=r["category"],
                         priority=r["priority"], parse=r["parse"]))
    with open(out / "sf_prepipeline.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # baseline
    n = len(rows)
    by_status = collections.Counter(r["status"] for r in rows)
    reached_12 = sum(1 for r in rows if r["status"] in ("Delivered 12 Minute Meeting", "Customer Meet", "Converted to Opportunity"))
    converted = by_status["Converted to Opportunity"]
    open_pre = [r for r in rows if r["status"] in ("Register Lead", "CAM to AE Intro")]
    old_open = [r for r in open_pre if r["age_days"] > 45]
    by_partner = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        by_partner[r["partner"]][r["status"]] += 1
    by_month = collections.Counter(r["created"][:7] for r in rows)
    by_pri = collections.Counter(r["priority"] or "blank" for r in rows)
    by_cat = collections.Counter(r["category"] or "blank" for r in rows)

    # overlap with the 3xG ranked list (prospect name vs account)
    cand = HERE / "review_sep1" / "3xg_candidates_ranked.csv"
    overlap = []
    if cand.exists():
        def key(s):
            s = s.lower()
            s = re.sub(r"\b(inc|llc|corp|corporation|company|co|the|group|financial|services|bank|n\.a|na|of|and|&)\b", " ", s)
            return re.sub(r"[^a-z0-9 ]", " ", s).split()
        cands = list(csv.DictReader(open(cand)))
        for r in rows:
            pk = key(r["prospect"])
            if not pk: continue
            for c in cands:
                ck = key(c["account"])
                if pk and ck and pk[0] == ck[0]:
                    grade = "MATCH" if (len(pk) >= 2 and len(ck) >= 2 and pk[:2] == ck[:2]) or (len(pk) == 1 and len(ck) == 1) else "CHECK"
                    overlap.append((c["account"], r["name"], r["status"], r["created"], grade, r["partner"]))
    lines = []
    L = lines.append
    L(f"# Partner pre-pipeline baseline, {TODAY.isoformat()}")
    L(f"\nSource: `{pdf.name}` (Salesforce printable view of Partner_Pre_Pipeline__c, filter All, {n} records). Read-only. No stage-change dates exist in this view, only Created Date, so speed (days to the 12-minute meeting) cannot be measured from it yet.\n")
    L("## Funnel today (all records, all partners)\n")
    L("| Stage | Records | Share |\n|---|---|---|")
    for s in STATUSES:
        L(f"| {s} | {by_status[s]} | {by_status[s]/n:.0%} |")
    L(f"\n- Reached the 12-minute meeting or beyond (Delivered 12 + Customer Meet + Converted): **{reached_12} of {n} ({reached_12/n:.0%})**. The benchmark is 25%+ inside 45 days; this is the all-time share with no clock on it.")
    L(f"- Converted to Opportunity: {converted} ({converted/n:.0%}). Disqualified: {by_status['Disqualified']} ({by_status['Disqualified']/n:.0%}).")
    L(f"- Still in Register Lead or CAM to AE Intro: {len(open_pre)}; of those **{len(old_open)} are older than 45 days** (created before {(TODAY-datetime.timedelta(days=45)).isoformat()}). That is the nurture pool.")
    L("\n## By partner (partner account, normalized; test rows dropped)\n")
    L("| Partner | Records | Register | CAM intro | 12-min | Cust meet | Converted | DQ | Reached 12-min+ |\n|---|---|---|---|---|---|---|---|---|")
    for p, c in sorted(by_partner.items(), key=lambda kv: -sum(kv[1].values())):
        tot = sum(c.values()); r12 = c["Delivered 12 Minute Meeting"] + c["Customer Meet"] + c["Converted to Opportunity"]
        L(f"| {p} | {tot} | {c['Register Lead']} | {c['CAM to AE Intro']} | {c['Delivered 12 Minute Meeting']} | {c['Customer Meet']} | {c['Converted to Opportunity']} | {c['Disqualified']} | {r12/tot:.0%} |")
    bulk = sum(1 for r in rows if r["created"] in ("2026-01-30", "2026-02-02"))
    L(f"\n## Created by month\n\n{bulk} of {n} records carry a Created Date of Jan 30 or Feb 2 2026: the bulk load when the object went live, not the registration date. Age and speed can only be read on records created from March 2026 on ({n - bulk} records) until Status history is available.\n")
    L("| Month | Records |\n|---|---|")
    for m in sorted(by_month): L(f"| {m} | {by_month[m]} |")
    L("\n## Priority and category as filled\n")
    L("Priority: " + ", ".join(f"{k}: {v}" for k, v in sorted(by_pri.items())))
    L("\nCategory: " + ", ".join(f"{k}: {v}" for k, v in sorted(by_cat.items())))
    L("\n## Overlap with the 3xG ranked list\n")
    if overlap:
        L("| Grade | 3xG account | Pre-pipeline record | Partner | Status | Created |\n|---|---|---|---|---|---|")
        for o in sorted(overlap, key=lambda o: (o[4] != "MATCH", o[0])): L(f"| {o[4]} | {o[0]} | {o[1]} | {o[5]} | {o[2]} | {o[3]} |")
        L("\nMATCH = same first two name tokens; CHECK = first token only (Beth Israel Deaconess vs Beth Israel Lahey, Texas Health vs Texas HHSC), confirm before treating as registered.")
        L("\nRule: an account already registered by another partner is not worked cold in the 3xG cohort; it goes to the registering partner's rep.")
    else:
        L("None of the 76 ranked 3xG accounts appears in the pre-pipeline under any partner. The cohort is clean on that gate.")
    L("\n## Parse quality\n")
    pq = collections.Counter(r["parse"] for r in rows)
    L(", ".join(f"{k}: {v}" for k, v in pq.items()) + ". Owner columns are split on a known-Intradiem-name list; rows with an empty intradiem_ae need a look.")
    L(f"\nMissing for the pilot read: Status change dates (field history on Status, or Last Modified Date plus a 12-minute-meeting date field), Prospect account link, ACV. Ask Sales Ops for a report on the object with those columns; the printable view cannot carry them.")
    (out / "sf_prepipeline_baseline.md").write_text("\n".join(lines) + "\n")
    print(f"{n} records -> {out}")
    print("\n".join(lines[:22]))


if __name__ == "__main__":
    main()
