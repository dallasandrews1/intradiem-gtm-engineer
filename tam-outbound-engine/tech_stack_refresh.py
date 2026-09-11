#!/usr/bin/env python3
"""Refresh the verified tech-stack read for TAM accounts from Clay (PredictLeads).

One Clay action run per domain (1 credit). Dry-run by default: prints what it found and what it
would write. --write updates data/tam_accounts.csv (acd/wfm, *_source, *_observed) for the domains
it read. Vendor list, lanes and the action id live in config/tech_vendors.json.

Run:  python3 tech_stack_refresh.py --domain amerihealthcaritas.com          (dry run, 1 credit)
      python3 tech_stack_refresh.py --domain a.com --domain b.com --write
      python3 tech_stack_refresh.py --all --write                            (one credit per account; confirm first)
"""
import argparse
import csv
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "tam_accounts.csv")
CFG = json.load(open(os.path.join(HERE, "config", "tech_vendors.json")))
MAX_AGE_DAYS = json.load(open(os.path.join(HERE, "config", "icp_weights.json")))["tech"]["verified_max_age_days"]
FIELDS = ["domain", "company", "industry", "employees", "agent_count",
          "acd", "acd_source", "acd_observed", "wfm", "wfm_source", "wfm_observed",
          "source"]  # `source` is the row-level provenance the SEED guard reads; never drop it


def clay_bin():
    """Resolve the clay CLI without depending on the caller's PATH.

    Cowork and launchd both run with a PATH that does not carry the Claude Code plugin
    cache, so a bare `clay` is not found there. Same fallback the automation wrappers use
    (see automation/run_credit_check.sh). Added 2026-09-05.
    """
    found = shutil.which("clay")
    if found:
        return found
    cands = sorted(glob.glob(os.path.expanduser(
        "~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")), key=os.path.getmtime, reverse=True)
    return cands[0] if cands else "clay"


def run_action(domain):
    a = CFG["clay_action"]
    inputs = {"unparsedDomain": domain,
              "technologyNameFilter": ", ".join(CFG["filter"]),
              "useExactTechnologyMatch": True}
    try:
        out = subprocess.run([clay_bin(), "workflows", "actions", "test", a["packageId"], a["actionKey"],
                              "--inputs", json.dumps(inputs)], capture_output=True, text=True)
    except FileNotFoundError:
        return None, ("clay CLI not found. Install or sign in with the Clay plugin, "
                      "or run this from a shell where `clay` is on PATH.")
    try:
        d = json.loads(out.stdout)
    except json.JSONDecodeError:
        return None, f"clay error: {out.stdout[:200] or out.stderr[:200]}"
    if "error" in d:
        return None, f"clay error: {d['error'].get('message')}"
    return d.get("result", {}).get("technologies") or [], None


CANON = {k.lower(): v for k, v in CFG["canonical"].items()}
LANES = {lane: {n.lower() for n in names} for lane, names in CFG["lane"].items()}


def classify(techs):
    """Most recently seen vendor per lane; PredictLeads titles vary in case (Nice, Calabrio One), so match lowercased.
    Ties on last-seen date go to the higher PredictLeads score."""
    best = {"acd": None, "wfm": None}
    for t in techs:
        title = t.get("title", "")
        canon = CANON.get(title.lower())
        if not canon:
            continue
        seen = (t.get("last_seen_at") or "")[:10]
        key = (seen, float(t.get("score") or 0))
        for lane, names in LANES.items():
            if title.lower() in names and (best[lane] is None or key > best[lane]["_key"]):
                best[lane] = {"value": canon, "raw": title, "observed": seen,
                              "source": f"predictleads:{t.get('url') or ''}", "_key": key}
    return best


def stale(observed):
    """True when a read is older than the window copy is allowed to name a vendor from."""
    if not observed:
        return True
    try:
        d = datetime.date.fromisoformat(observed[:10])
    except ValueError:
        return True
    return (datetime.date.today() - d).days > MAX_AGE_DAYS


def cached_read(row):
    """A row's existing lane reads, when both source and a fresh observed date are present."""
    out = {}
    for lane in ("acd", "wfm"):
        val, src, obs = row.get(lane), row.get(f"{lane}_source"), row.get(f"{lane}_observed")
        if val and val != "Unknown" and src and obs and not stale(obs):
            out[lane] = {"value": val, "observed": obs, "source": src}
    return out


def lookup(domains, as_json, force, by):
    """Read-only platform lookup for ANY domain, in or out of the CSV.

    This is the shared entry point the skills call. It never writes, so a skill can
    establish an account's contact-centre platform without touching engine data.
    """
    results, spend = {}, 0
    for dom in domains:
        row = by.get(dom)
        if row and not force:
            hit = cached_read(row)
            if hit:
                results[dom] = {"read": hit, "credits": 0, "from": "tam_accounts.csv"}
                continue
        techs, err = run_action(dom)
        spend += CFG["clay_action"]["credits_per_run"]
        if err:
            results[dom] = {"error": err, "credits": CFG["clay_action"]["credits_per_run"]}
            continue
        read = {k: {kk: vv for kk, vv in v.items() if kk != "_key"}
                for k, v in classify(techs).items() if v}
        results[dom] = {"read": read, "credits": CFG["clay_action"]["credits_per_run"], "from": "predictleads"}

    if as_json:
        print(json.dumps({"max_age_days": MAX_AGE_DAYS, "credits_spent": spend,
                          "results": results}, indent=2))
        return
    for dom, r in results.items():
        print(f"\n{dom}  ({r['credits']} credit{'' if r['credits'] == 1 else 's'}"
              f"{', from ' + r['from'] if r.get('from') else ''})")
        if r.get("error"):
            print(f"  {r['error']}")
            continue
        if not r["read"]:
            print("  no read. Copy says \"on top of the WFM they already run\" and never guesses a vendor.")
        for lane, v in r["read"].items():
            flag = "  STALE, do not name this vendor in copy" if stale(v["observed"]) else ""
            print(f"  {lane}: {v['value']}  (observed {v['observed']}, {v['source']}){flag}")
    print(f"\nCredits spent: {spend}. Reads older than {MAX_AGE_DAYS} days may not be named in copy.")


def main():
    ap = argparse.ArgumentParser(description="Verified tech-stack reads from Clay (PredictLeads)")
    ap.add_argument("--domain", action="append", help="domain to refresh (repeatable)")
    ap.add_argument("--all", action="store_true", help="every account in tam_accounts.csv")
    ap.add_argument("--write", action="store_true", help="write results back to the CSV (default: dry run)")
    ap.add_argument("--lookup", action="append", metavar="DOMAIN",
                    help="read-only lookup for ANY domain, in the CSV or not. Never writes. "
                         "This is the entry point the skills use.")
    ap.add_argument("--json", action="store_true", help="with --lookup, emit structured output")
    ap.add_argument("--force", action="store_true", help="with --lookup, re-read even when a fresh cached read exists")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(CSV, newline="")))
    by = {r["domain"]: r for r in rows}

    if args.lookup:
        return lookup(args.lookup, args.json, args.force, by)

    targets = [r["domain"] for r in rows] if args.all else (args.domain or [])
    if not targets:
        ap.error("give --lookup, --domain or --all")
    unknown = [d for d in targets if d not in by]
    if unknown:
        sys.exit(f"not in tam_accounts.csv: {', '.join(unknown)}. "
                 f"Use --lookup for a read-only check on a domain that has no row yet.")

    per = CFG["clay_action"]["credits_per_run"]
    print(f"Credit estimate: {len(targets)} run(s) x {per} = {len(targets) * per} credits"
          f"{'' if args.write else ' (dry run: nothing written)'}")
    changed = 0
    for dom in targets:
        techs, err = run_action(dom)
        if err:
            print(f"{dom}: {err}")
            continue
        read = classify(techs)
        hits = ", ".join(f"{t.get('title')} (last seen {(t.get('last_seen_at') or '')[:10]})" for t in techs) or "none"
        print(f"\n{dom}: {hits}")
        for lane in ("acd", "wfm"):
            r = read[lane]
            if r:
                print(f"  {lane}: {r['value']} <- {r['raw']}, observed {r['observed']}")
                if args.write:
                    by[dom][lane] = r["value"]
                    by[dom][f"{lane}_source"] = r["source"]
                    by[dom][f"{lane}_observed"] = r["observed"]
                    changed += 1
            else:
                print(f"  {lane}: no read (row left as is)")
    if args.write:
        with open(CSV, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in FIELDS})
        print(f"\nwrote {changed} lane value(s) to {os.path.relpath(CSV, HERE)}")


if __name__ == "__main__":
    main()
