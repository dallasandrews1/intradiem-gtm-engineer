#!/usr/bin/env python3
"""Refresh the TAM strike universe from Clay Audiences. DRY RUN by default.

Why: data/tam_accounts.csv has been 7 hand-maintained rows since the engine's first commit,
while the real universe lives in Clay Audiences. The hosted brain served those 7 rows into
September. This is the free half of closing that gap.

Cost: reading Audiences is the workspace's own synced data and costs 0 credits. Verified
2026-09-05: a full 2,287-record pull left the balance unchanged at 62,657.5. The only
field with no free source is `agent_count`, which is what the report at the end prices.

    python3 refresh_from_audiences.py                 # dry run, report only
    python3 refresh_from_audiences.py --cache PATH    # reuse a saved pull
    python3 refresh_from_audiences.py --write PATH    # write the proposed CSV (still not live)

Nothing here overwrites data/tam_accounts.csv. Promoting the proposal is a separate,
deliberate step.
"""
import argparse
import collections
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "config")

# Audiences workspace field ids (from `clay audiences fields list --entity-type companies`)
FIELD = {
    "account_type": "audf_0timw0xX6CfUdJXJznM",
    "acd": "audf_0tkv9tyqFQ6H2g2ESvx",
    "acd_seen": "audf_0tkv9ty3of7Ng2tHFev",
    "wfm": "audf_0tkv9tzQXmR5ZVaK4Mc",
    "read_date": "audf_0tkveafXRVwUeNNaBzs",
    "read_status": "audf_0tkvfh8ewDEMJp9w4of",
    "rep_confirmed": "audf_0tkveafmZS5BQqgqYuQ",
}

# Only a clearly-cold account may enter a cold universe. Customer and Churned are the
# exclusion gate; Partner is not a prospect; a BLANK account type is unknown, and unknown
# fails closed here rather than being assumed cold.
COLD_ONLY = {"Prospect"}

# icp_weights.scale_bands floor for a meaningful score. Below 1,000 employees an account
# scores 5 of 25 on scale and will not clear Tier 2 on any realistic trigger.
MIN_EMPLOYEES = 1000


def clay(*args):
    r = subprocess.run(["clay", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"clay {' '.join(args)}: {r.stderr.strip()[:200]}")
    return json.loads(r.stdout)


def pull_companies():
    ids, cursor = [], None
    while True:
        a = ["audiences", "records", "search-ids", "--entity-type", "companies", "--limit", "500"]
        if cursor:
            a += ["--cursor", cursor]
        d = clay(*a)
        batch = d.get("data", [])
        ids += batch
        cursor = d.get("cursor")
        if not batch or not cursor:
            break
    recs = []
    for i in range(0, len(ids), 100):
        recs += clay("audiences", "records", "get", "--entity-type", "companies",
                     "--ids", ",".join(str(x) for x in ids[i:i + 100])).get("data", [])
    return recs


def f(rec, key):
    return (rec["fields"].get(key) or "") if isinstance(rec.get("fields"), dict) else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", help="read a saved pull instead of calling Clay")
    ap.add_argument("--write", help="write the proposed CSV here (never tam_accounts.csv)")
    a = ap.parse_args()

    recs = json.load(open(a.cache)) if a.cache and os.path.exists(a.cache) else pull_companies()
    imap = json.load(open(os.path.join(C, "audiences_industry_map.json")))
    icp = json.load(open(os.path.join(C, "icp_weights.json")))["industry_points"]

    drop = collections.Counter()
    rows = []
    for r in recs:
        acct = str(f(r, FIELD["account_type"])).strip()
        dom = str(r["fields"].get("normalized_domain") or r["fields"].get("domain") or "").strip().lower()
        try:
            emp = int(r["fields"].get("employee_count") or 0)
        except (TypeError, ValueError):
            emp = 0
        if acct not in COLD_ONLY:
            drop[f"account_type={acct or '(blank)'}"] += 1
            continue
        if not dom:
            drop["no domain"] += 1
            continue
        if emp < MIN_EMPLOYEES:
            drop[f"employees < {MIN_EMPLOYEES}"] += 1
            continue
        raw_ind = str(r["fields"].get("industry") or "").strip()
        ind = imap["map"].get(raw_ind, imap["default"])
        acd, wfm = str(f(r, FIELD["acd"])).strip(), str(f(r, FIELD["wfm"])).strip()
        seen, read_date = str(f(r, FIELD["acd_seen"])).strip(), str(f(r, FIELD["read_date"])).strip()
        rows.append({
            "domain": dom,
            "company": str(r["fields"].get("org_name") or "").strip(),
            "industry": ind,
            "employees": emp,
            # No free source for agent_count. Left 0 on purpose: account_engine.is_seed
            # treats a non-positive agent count as seed, so these rows score but carry no
            # ROI and no copy until it is filled. That is the intended fail-safe, not a gap
            # to paper over with a guess.
            "agent_count": 0,
            "acd": acd or "Unknown",
            "acd_source": "PredictLeads via Clay Audiences" if acd else "",
            "acd_observed": seen or read_date,
            "wfm": wfm or "Unknown",
            "wfm_source": "PredictLeads via Clay Audiences" if wfm else "",
            "wfm_observed": seen or read_date,
            "source": (f"Salesforce via Clay Audiences, company record read {read_date or 'n/a'}; "
                       f"industry '{raw_ind}' mapped to '{ind}'; employees {emp:,} per Audiences. "
                       "agent_count NOT sourced."),
            "_raw_industry": raw_ind,
            "_has_tech": bool(acd or wfm),
        })

    print(f"Audiences companies read : {len(recs)}  (0 credits, workspace's own synced data)")
    print(f"Candidate cold universe  : {len(rows)}")
    print("\nExcluded:")
    for k, v in drop.most_common():
        print(f"   {v:>5}  {k}")

    print("\nBy ICP industry (points):")
    for ind, n in collections.Counter(r["industry"] for r in rows).most_common():
        print(f"   {n:>5}  {ind:<22} {icp.get(ind, icp.get('Other'))} pts")

    tech = sum(1 for r in rows if r["_has_tech"])
    print(f"\nTech stack already read  : {tech} of {len(rows)} ({tech*100//max(len(rows),1)}%) "
          f"- already paid for: the Sep 5 PredictLeads drain, 1,852 credits")
    print(f"Missing a tech read      : {len(rows)-tech}")

    print("\n--- WHAT THIS COSTS ---")
    print("  Everything above: 0 credits. Audiences reads are free and were verified free.")
    print(f"  Every one of the {len(rows)} rows lands SEED, because agent_count has no free")
    print("  source and is_seed treats a non-positive agent count as unsourced. Seeded rows")
    print("  score but the brain withholds their fit, ROI and copy, so the refresh alone")
    print("  does not put a single quotable account in front of a seller.")
    print("\n  agent_count is the only thing standing between this universe and a usable one.")
    print("  Pricing it needs a decision from Dallas, so nothing here spends a credit.")

    if a.write:
        import csv
        cols = ["domain", "company", "industry", "employees", "agent_count", "acd",
                "acd_source", "acd_observed", "wfm", "wfm_source", "wfm_observed", "source"]
        with open(a.write, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            for r in rows:
                w.writerow({k: r[k] for k in cols})
        print(f"\nProposal written to {a.write} ({len(rows)} rows).")
        print("data/tam_accounts.csv is UNTOUCHED. Promoting it is a separate step.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
