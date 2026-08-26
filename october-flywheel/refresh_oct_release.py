#!/usr/bin/env python3
"""October CMS release refresh flywheel — SKELETON (v0, Jul 14 2026).

When CMS drops the 2027 Star Ratings (expected Oct 2026), the whole Stars motion
re-grades itself from one input: the new ratings ZIP. This script is the flywheel:

    ingest new CMS ZIP  ->  rebuild movement joins  ->  emit refreshed universe
    CSVs + a drift report. New fallers enter the motion; graduates self-clean
    (the engine's kill switch does the dropping, this script does the re-scoring
    inputs).

STATUS: skeleton. Stage functions are stubbed where the 2027 file layout is
unknowable until CMS publishes it. Everything that CAN be locked now is locked:
CLI, pipeline order, encoding discipline, join keys, output contracts, and the
drift-report shape. Fill the marked TODOs against the real ZIP in October.

HARD-WON LESSONS ENCODED (do not relearn these):
  * CMS CSVs are cp1252, NOT utf-8. Every read here forces encoding="cp1252".
  * Join on contract_id (H####), never on parent/marketing names (they drift).
  * Star cells contain junk like "Not enough data" — parse defensively.
  * Parent names change season to season; keep a manual alias map.

Usage (October):
    python3 refresh_oct_release.py --zip 2027_star_ratings.zip --dry-run   # stages + drift, writes nothing
    python3 refresh_oct_release.py --zip 2027_star_ratings.zip            # full refresh, writes outputs/
    python3 refresh_oct_release.py --check                                # verify current inputs exist

Outputs (all under --outdir, default ./output_2027/):
    CMS_Star_Movement_26v27.csv        movement join (this year vs last, slippage flags)
    StarRatings_Universe_2027.csv      refreshed universe (re-graded, re-tiered)
    l2_accounts_stars_2027.csv         engine swap-in (account, star, new_faller, customer_flag)
    Drift_Report_2027.md               who fell in, who graduated out, tier moves, QBP shifts
"""
import argparse
import csv
import io
import os
import sys
import zipfile
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# ---- input contracts (current-cycle files this refresh joins against) --------
PRIOR_MOVEMENT = os.path.join(REPO, "greenlight-pack", "CMS_Star_Movement_25v26.csv")
PRIOR_UNIVERSE = os.path.join(REPO, "StarRatings_Universe_2026_Canonical.csv")
CUSTOMER_EXCLUDE = os.path.join(REPO, "greenlight-pack", "Active_Customers_SF_Jul10.csv")

ENCODING = "cp1252"          # CMS discipline: never utf-8 on their files
GRADUATED_STAR = 4.0         # keep in sync with l2_intent_signals.json self_cleaning
CLIFF_STAR = 3.5

# Parent orgs rename between cycles; map new-name -> canonical-name here as found.
PARENT_ALIASES = {
    # "CVS Health Corporation": "Aetna/CVS Health",   # example shape
}


def parse_star(v):
    """CMS star cells contain 'Not enough data', 'Plan too new', blanks. Defensive."""
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def read_cms_csv(raw_bytes):
    """Every CMS file goes through here so cp1252 is impossible to forget."""
    return list(csv.DictReader(io.StringIO(raw_bytes.decode(ENCODING, errors="replace"))))


# ---- stage 1: ingest ----------------------------------------------------------
def ingest_zip(zip_path):
    """Open the CMS ZIP, locate the summary-rating and domain-star tables.

    TODO(Oct): CMS renames member files every cycle. Locate by fuzzy match on
    'Summary Rating' / 'Domain' / 'Measure' in member names, then map columns:
      contract_id, parent_org, marketing_name, overall_star_2027,
      domain stars for HD3 (member experience) and HD5 (customer service).
    Returns {contract_id: {..parsed fields..}}
    """
    out = OrderedDict()
    with zipfile.ZipFile(zip_path) as z:
        names = z.namelist()
        print("[ingest] ZIP members:")
        for n in names:
            print("   ", n)
        # TODO(Oct): pick the right members, e.g.:
        # summary = read_cms_csv(z.read(<summary_member>))
        # domains = read_cms_csv(z.read(<domain_member>))
        # for row in summary: out[row["Contract ID"]] = {...parse_star...}
    if not out:
        print("[ingest] SKELETON: member mapping not wired yet — see TODO(Oct).")
    return out


# ---- stage 2: movement join ---------------------------------------------------
def build_movement(new_rows, prior_movement_path=PRIOR_MOVEMENT):
    """Join 2027 stars onto the 2026 picture by contract_id.

    Emits one row per contract with:
      overall_star_2026, overall_star_2027, star_delta_26to27,
      new_faller (was >= 4.0, now < 4.0  OR newly landed at the 3.5 cliff),
      graduated (was < 4.0, now >= 4.0),
      measure_slippage (delta < 0 AND (HD5 <= 3.0 OR HD3 <= 3.0)), with a
      traceable measure_slippage_why string — same definition as 25v26.
    """
    prior = {}
    with open(prior_movement_path, encoding=ENCODING) as f:
        for row in csv.DictReader(f):
            prior[row["contract_id"]] = row

    movement = []
    for cid, nr in new_rows.items():
        pr = prior.get(cid, {})
        old = parse_star(pr.get("overall_star_2026"))
        new = parse_star(nr.get("overall_star_2027"))
        delta = (new - old) if (old is not None and new is not None) else None
        graduated = old is not None and new is not None and old < GRADUATED_STAR <= new
        new_faller = old is not None and new is not None and (
            (old >= GRADUATED_STAR and new < GRADUATED_STAR) or (old > CLIFF_STAR and new == CLIFF_STAR)
        )
        # TODO(Oct): measure_slippage needs the NEW cycle's HD5/HD3 domain stars
        movement.append({
            "contract_id": cid,
            "parent_org": PARENT_ALIASES.get(nr.get("parent_org", ""), nr.get("parent_org", "")),
            "marketing_name": nr.get("marketing_name", ""),
            "overall_star_2026": old,
            "overall_star_2027": new,
            "star_delta_26to27": round(delta, 1) if delta is not None else "",
            "new_faller": "TRUE" if new_faller else "FALSE",
            "graduated": "TRUE" if graduated else "FALSE",
            "measure_slippage": "TODO",
            "measure_slippage_why": "",
        })
    # contracts that vanished from the CMS file (terminated/merged) still matter:
    for cid, pr in prior.items():
        if cid not in new_rows:
            movement.append({**{k: pr.get(k, "") for k in ("contract_id", "parent_org", "marketing_name")},
                             "overall_star_2026": pr.get("overall_star_2026"),
                             "overall_star_2027": "", "star_delta_26to27": "",
                             "new_faller": "FALSE", "graduated": "FALSE",
                             "measure_slippage": "FALSE",
                             "measure_slippage_why": "contract absent from 2027 file (terminated/merged?)"})
    return movement


# ---- stage 3: refreshed universe + engine swap-in ------------------------------
def build_universe(movement):
    """Re-grade and re-tier: joins movement onto the prior canonical universe
    (members, QBP economics carry until re-modeled), recomputes tiers.

    TODO(Oct): QBP forgone-dollar recompute needs fresh enrollment + benchmark
    data; v0 carries prior economics forward with a 'stale_econ' flag so the
    refresh never silently presents old dollars as new.
    """
    universe, engine_rows = [], []
    prior = {}
    if os.path.exists(PRIOR_UNIVERSE):
        with open(PRIOR_UNIVERSE, encoding=ENCODING) as f:
            for row in csv.DictReader(f):
                prior[row["contract_id"]] = row
    customers = set()
    if os.path.exists(CUSTOMER_EXCLUDE):
        with open(CUSTOMER_EXCLUDE, encoding=ENCODING, errors="replace") as f:
            for row in csv.DictReader(f):
                # TODO(Oct): confirm the customer-file join key (parent name normalize)
                customers.add((row.get("Account Name") or "").strip().lower())

    for m in movement:
        star = parse_star(m["overall_star_2027"])
        pr = prior.get(m["contract_id"], {})
        universe.append({**m, "members": pr.get("members", ""),
                         "gross_forgone_qbp_musd": pr.get("gross_forgone_qbp_musd", ""),
                         "econ_status": "stale_econ_carryforward"})
        engine_rows.append({
            "account": m["parent_org"] or m["marketing_name"],
            "overall_star_2026": m["overall_star_2027"],  # engine field name is generic star-of-record
            "new_faller": m["new_faller"],
            "customer_flag": "TRUE" if (m["parent_org"] or "").strip().lower() in customers else "FALSE",
        })
    return universe, engine_rows


# ---- stage 4: drift report -----------------------------------------------------
def drift_report(movement):
    fell = [m for m in movement if m["new_faller"] == "TRUE"]
    grad = [m for m in movement if m["graduated"] == "TRUE"]
    gone = [m for m in movement if m["overall_star_2027"] == "" and m["overall_star_2026"] not in ("", None)]
    lines = ["# October Refresh Drift Report (2026 -> 2027)", ""]
    lines.append("New fallers entering the motion: %d" % len(fell))
    for m in fell:
        lines.append("  - %s (%s) %s -> %s" % (m["parent_org"], m["contract_id"], m["overall_star_2026"], m["overall_star_2027"]))
    lines.append("")
    lines.append("Graduates self-cleaning out: %d" % len(grad))
    for m in grad:
        lines.append("  - %s (%s) %s -> %s" % (m["parent_org"], m["contract_id"], m["overall_star_2026"], m["overall_star_2027"]))
    lines.append("")
    lines.append("Contracts absent from the new file (investigate): %d" % len(gone))
    lines.append("")
    lines.append("Next actions: swap l2_accounts_stars CSV into the engine, re-run scorer + tests,")
    lines.append("re-import refreshed universe to Clay (parent grain!), be first in the inbox at any")
    lines.append("'wait for October' account with their published movement (reply-engine follow-up).")
    return "\n".join(lines)


def write_csv(path, rows):
    if not rows:
        print("[write] SKELETON: no rows for %s (stages not wired yet)" % os.path.basename(path))
        return
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("[write] %s (%d rows)" % (path, len(rows)))


def main():
    ap = argparse.ArgumentParser(description="October CMS release refresh flywheel (skeleton)")
    ap.add_argument("--zip", help="path to the new CMS Star Ratings ZIP")
    ap.add_argument("--outdir", default=os.path.join(HERE, "output_2027"))
    ap.add_argument("--dry-run", action="store_true", help="run stages, write nothing")
    ap.add_argument("--check", action="store_true", help="verify current-cycle inputs exist and parse")
    args = ap.parse_args()

    if args.check:
        ok = True
        for p in (PRIOR_MOVEMENT, PRIOR_UNIVERSE, CUSTOMER_EXCLUDE):
            exists = os.path.exists(p)
            ok &= exists
            print("[check] %s %s" % ("ok " if exists else "MISSING", p))
        if os.path.exists(PRIOR_MOVEMENT):
            with open(PRIOR_MOVEMENT, encoding=ENCODING) as f:
                n = sum(1 for _ in csv.DictReader(f))
            print("[check] prior movement rows: %d" % n)
        return 0 if ok else 1

    if not args.zip:
        ap.error("--zip is required (or use --check)")

    new_rows = ingest_zip(args.zip)
    movement = build_movement(new_rows)
    universe, engine_rows = build_universe(movement)
    report = drift_report(movement)
    print(report)

    if args.dry_run:
        print("\n[dry-run] nothing written")
        return 0
    os.makedirs(args.outdir, exist_ok=True)
    write_csv(os.path.join(args.outdir, "CMS_Star_Movement_26v27.csv"), movement)
    write_csv(os.path.join(args.outdir, "StarRatings_Universe_2027.csv"), universe)
    write_csv(os.path.join(args.outdir, "l2_accounts_stars_2027.csv"), engine_rows)
    with open(os.path.join(args.outdir, "Drift_Report_2027.md"), "w") as f:
        f.write(report + "\n")
    print("[done] refresh outputs in %s" % args.outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
