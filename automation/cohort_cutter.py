#!/usr/bin/env python3
"""cohort-cutter: Lane B of the signal-marketing loop. Every other Tuesday (anchor in config),
freeze the cohort once and ship it to two places on one clock: the lemlist wave and the
LinkedIn Matched Audience, under one Salesforce campaign name, with a holdout.

What it does (dry run by default, automation/config/heat_loop.json):
  1. Parity check: runs only on the anchor Tuesday and every interval_days after it (--force overrides).
  2. Pool = companies in the Heat Cohort pool segment (Clay Heat Lane = cohort) UNION the domains in
     cohort.extra_domains_file (this fortnight's planned lemlist wave, one domain per line).
  3. Expand to people from Audiences (0 credits): ICP persona first, Director+ titles second, up to
     contacts_per_account. Customer-exclusion union applied again here (belt and braces).
  4. 300-matchable check (LinkedIn's floor). Short = write the manifest as WAITING and stop.
  5. Holdout by account (sha1 parity): test arm = ads + sequence, holdout arm = sequence only.
  6. Write: manifest, ads CSV (test arm, LinkedIn list-upload columns), holdout CSV, lemlist draft-load
     CSV (both arms, cohort id + arm as custom fields), Salesforce stamp plan CSV (Lead Source = GTM
     Engineering, Primary Campaign Source = the cohort campaign name). No writes anywhere but files.
  7. Log automation/logs/cohort-cutter-<date>.md for the rundown.

Live mode (never flipped here): creates the per-cohort segments, posts Clay Heat Cohort stamps through
the Heat Stamp webhook, and hands the lemlist CSV to the rep's draft campaign. Sends are never automated.

Usage:
    python3 automation/cohort_cutter.py            # scheduled (parity-checked)
    python3 automation/cohort_cutter.py --force    # cut today regardless of parity (still dry unless config says live)
    python3 automation/cohort_cutter.py --dry-run --force
"""
import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import heat_list_scorer as H  # reuse the CLI wrapper, domain helpers, exclusion union  # noqa: E402

ROOT = H.ROOT
P = H.P
TODAY = date.today()
LOG_FAMILY = "cohort-cutter"


def cohort_id(d):
    return f"GTMENG-{d.isoformat()}"


def on_schedule(cfg, today):
    anchor = datetime.strptime(cfg["cohort"]["anchor_tuesday"], "%Y-%m-%d").date()
    if today < anchor:
        return False, f"before anchor {anchor}"
    delta = (today - anchor).days
    ok = delta % cfg["cohort"]["interval_days"] == 0
    return ok, f"{delta} days since anchor, interval {cfg['cohort']['interval_days']}"


def pool_domains(cfg, log):
    seg = cfg["audiences"]["segments"]["cohort_pool"]
    ids, cursor, pages = [], None, 0
    while True:
        r = H.clay("audiences", "records", "search-ids", "--entity-type", "companies", "--audience-id", seg, *(["--cursor", cursor] if cursor else []))
        if "_error" in r:
            log.append(f"- pool segment read stopped: {r['_error']}")
            break
        ids.extend(r.get("data", []))
        cursor = r.get("cursor")
        pages += 1
        if not cursor or pages > 40:
            break
    doms = {}
    for i in range(0, len(ids), 100):
        g = H.clay("audiences", "records", "get", "--entity-type", "companies", "--ids", ",".join(str(x) for x in ids[i:i + 100]))
        for rec in (g.get("data") or []):
            f = rec.get("fields", {})
            d = H.norm_domain(f.get("normalized_domain") or f.get("domain"))
            if d:
                doms[d] = {"id": rec.get("recordId"), **f}
    log.append(f"- Heat Cohort pool segment: {len(ids)} companies, {len(doms)} with a domain")
    extra = P(cfg["cohort"]["extra_domains_file"])
    n_extra = 0
    if os.path.exists(extra):
        for line in open(extra):
            d = H.norm_domain(line.strip())
            if d and not line.startswith("#"):
                doms.setdefault(d, {})
                n_extra += 1
    log.append(f"- extra wave domains file: {n_extra} domains ({cfg['cohort']['extra_domains_file']})")
    return doms


def people_at(domain, cfg, limit):
    pf = cfg["audiences"]["people_fields"]
    flt = {"type": "GroupOp", "combinationMode": "And", "items": [
        {"type": "BinOp", "key": "normalized_domain", "dataPath": ["account_entity_field_values", "field", "normalized_domain"],
         "operator": "Contain", "value": domain, "entityType": "ACCOUNT"}]}
    r = H.clay("audiences", "records", "search-ids", "--entity-type", "people", "--filter", json.dumps(flt))
    ids = (r.get("data") or [])[:200] if isinstance(r, dict) else []
    rows = []
    for i in range(0, len(ids), 100):
        g = H.clay("audiences", "records", "get", "--entity-type", "people", "--ids", ",".join(str(x) for x in ids[i:i + 100]))
        for rec in (g.get("data") or []):
            f = rec.get("fields", {})
            title = f.get(pf["enriched_title"]) or f.get("title") or ""
            pk = f.get(pf["persona_key"]) or ""
            email = (f.get("email") or "").strip()
            if pk in cfg["thresholds"]["icp_personas"]:
                rank = 0
            elif re.search(r"\b(chief|evp|svp|vp|vice president|head of|director)\b", title, re.I):
                rank = 1
            else:
                continue
            if (f.get(pf["triage"]) or "") in ("competitor", "internal", "personal"):
                continue
            rows.append((rank, {"record_id": rec.get("recordId"), "first_name": f.get("first_name") or "", "last_name": f.get("last_name") or "",
                                "email": email, "title": title, "persona": pk, "linkedin": f.get("linkedin_url") or "",
                                "country": f.get("location_country") or "", "lead_source": f.get(pf["lead_source"]) or "",
                                "owner_id": f.get(pf["owner_id"]) or ""}))
    rows.sort(key=lambda x: (x[0], 0 if x[1]["email"] else 1))
    return [x[1] for x in rows[:limit]]


def write_csv(path, rows, cols):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = H.load(H.CFG_PATH)
    dry = a.dry_run or cfg.get("dry_run", True)
    live_stamp = cfg.get("live_stamp", False) and not dry
    log = [f"# Cohort cutter: {TODAY.isoformat()} ({'DRY RUN' if dry else 'LIVE'})", ""]
    ok, why = on_schedule(cfg, TODAY)
    if not ok and not a.force:
        log.append(f"- ran, off-week ({why}); no cut. Next cut: see anchor + interval in heat_loop.json")
        return finish(log)
    cid = cohort_id(TODAY)
    camp = f"{cfg['cohort']['sf_campaign_prefix']} - {cfg['cohort']['motion_label']} - {cid}"
    log += [f"Cohort id `{cid}`, Salesforce campaign `{camp}` ({why}{', forced' if a.force else ''}).", "", "## Pool"]
    try:
        cache = H.load(P(cfg["sources"]["domain_cache"]))
    except Exception:  # noqa: BLE001
        cache = {}
    doms = pool_domains(cfg, log)
    ib = H.install_base_domains(cfg, cache)
    ex = cfg["exclusion"]
    kept, dropped = {}, []
    for d, rec in doms.items():
        at = rec.get(cfg["audiences"]["company_fields"]["account_type"]) or ""
        if d in ib or at in ("Customer", "Partner") or d in ex["competitor_domains"] or d in ex["partner_domains"] or d in ex["our_domains"]:
            dropped.append((d, at or ("install-base" if d in ib else "excluded domain")))
            continue
        kept[d] = rec
    log.append(f"- exclusion union: {len(dropped)} dropped ({', '.join(f'{d} [{r}]' for d, r in dropped[:10])}{'...' if len(dropped) > 10 else ''})")
    log.append(f"- {len(kept)} accounts eligible")

    people, per_acct = [], defaultdict(int)
    for d, rec in kept.items():
        for p in people_at(d, cfg, cfg["cohort"]["contacts_per_account"]):
            p["domain"] = d
            p["company"] = rec.get("org_name") or d
            people.append(p)
            per_acct[d] += 1
    matchable = [p for p in people if p["email"]]
    short = [d for d in kept if per_acct[d] < 3]
    log += ["", "## People", f"- {len(people)} people across {len(per_acct)} accounts; {len(matchable)} with a work email (LinkedIn-matchable)",
            f"- {len(short)} accounts with fewer than 3 known contacts (free sourcing pass needed before the cut is final): {', '.join(short[:15])}{'...' if len(short) > 15 else ''}"]

    floor = cfg["cohort"]["min_matchable"]
    outdir = P("motions/signal_marketing_loop/cohorts")
    os.makedirs(outdir, exist_ok=True)
    if len(matchable) < floor:
        log += ["", f"## WAITING: {len(matchable)} matchable < {floor} floor. No cut. Options: run the free sourcing pass on the short accounts, add planned-wave domains to {cfg['cohort']['extra_domains_file']}, or wait a week."]
        write_manifest(outdir, cid, camp, cfg, log, kept, people, waiting=True)
        return finish(log)

    # holdout by account
    test, hold = [], []
    for d in kept:
        arm = "test" if int(hashlib.sha1(d.encode()).hexdigest(), 16) % 100 < cfg["cohort"]["holdout_share"] * 100 else "holdout"
        (test if arm == "test" else hold).append(d)
    for p in people:
        p["arm"] = "test" if p["domain"] in test else "holdout"
        p["cohort_id"] = cid
        p["sf_campaign"] = camp
        p["lead_source"] = p["lead_source"] or "GTM Engineering"
    t0 = TODAY
    clock = {"T0 ads audience ships": t0, "T+2 LinkedIn live": t0 + timedelta(days=cfg["cohort"]["ads_live_lag_days"]),
             "T+5 email 1": t0 + timedelta(days=cfg["cohort"]["email1_lag_days"]), "T+25 ads off": t0 + timedelta(days=cfg["cohort"]["ads_off_lag_days"])}
    log += ["", "## Split", f"- test (ads + sequence): {len(test)} accounts, {sum(1 for p in people if p['arm'] == 'test')} people",
            f"- holdout (sequence only): {len(hold)} accounts, {sum(1 for p in people if p['arm'] == 'holdout')} people",
            "", "## Clock"] + [f"- {k}: {v.isoformat()}" for k, v in clock.items()]

    ads_cols = ["email", "first_name", "last_name", "company", "title", "country"]
    write_csv(os.path.join(outdir, f"{cid}_ads_linkedin.csv"), [p for p in matchable if p["arm"] == "test"], ads_cols)
    write_csv(os.path.join(outdir, f"{cid}_holdout.csv"), [p for p in people if p["arm"] == "holdout"], ads_cols + ["domain", "persona"])
    lem_cols = ["email", "firstName", "lastName", "companyName", "linkedinUrl", "jobTitle", "cohort_id", "arm", "sf_campaign", "persona"]
    lem_rows = [{"email": p["email"], "firstName": p["first_name"], "lastName": p["last_name"], "companyName": p["company"], "linkedinUrl": p["linkedin"],
                 "jobTitle": p["title"], "cohort_id": cid, "arm": p["arm"], "sf_campaign": camp, "persona": p["persona"]} for p in people]
    write_csv(os.path.join(outdir, f"{cid}_lemlist_draft_load.csv"), lem_rows, lem_cols)
    sf_cols = ["record_id", "email", "domain", "lead_source", "primary_campaign_source", "arm"]
    write_csv(os.path.join(outdir, f"{cid}_salesforce_stamp_plan.csv"),
              [{"record_id": p["record_id"], "email": p["email"], "domain": p["domain"], "lead_source": "GTM Engineering", "primary_campaign_source": camp, "arm": p["arm"]} for p in people], sf_cols)
    log += ["", "## Files", f"- {outdir}/{cid}_ads_linkedin.csv (test arm, LinkedIn list-upload columns; Clay Ads sync uses the segment instead)",
            f"- {outdir}/{cid}_holdout.csv", f"- {outdir}/{cid}_lemlist_draft_load.csv (both arms; rep imports into the DRAFT campaign, launch is theirs)",
            f"- {outdir}/{cid}_salesforce_stamp_plan.csv (Lead Source + Primary Campaign Source; applied only after the field mapping is read back once)"]

    # cohort stamp on companies (live only), per-cohort segments (live only)
    stamp_url = cfg["workflows"]["heat_stamp"]["webhook_url"]
    log += ["", "## Stamps and segments"]
    for d in kept:
        arm = "test" if d in test else "holdout"
        H.post_webhook(stamp_url, {"domain": d, "heat_cohort": f"{cid}|{arm}", "heat_lane": "cohort", "heat_score": 0, "heat_reasons": "", "heat_updated": TODAY.isoformat()}, live_stamp, log) if live_stamp else None
    if not live_stamp:
        log.append(f"    would stamp Clay Heat Cohort = '{cid}|test' / '{cid}|holdout' on {len(kept)} companies via the Heat Stamp webhook")
    seg_note = (f"    would create segments 'Heat Cohort {cid} - ads' (Clay Heat Cohort = {cid}|test) and 'Heat Cohort {cid} - holdout' via clay audiences create; "
                "the ads segment is the Clay Ads -> LinkedIn Matched Audience source (300 floor, ~48h)")
    log.append(seg_note)
    if not dry:
        cf = cfg["audiences"]["company_fields"]["heat_cohort"]
        for arm, name in (("test", f"Heat Cohort {cid} - ads"), ("holdout", f"Heat Cohort {cid} - holdout")):
            flt = {"type": "GroupOp", "combinationMode": "And", "items": [{"type": "BinOp", "key": cf, "dataPath": ["account_entity_field_values", "field", cf],
                                                                             "operator": "Equal", "value": f"{cid}|{arm}", "entityType": "ACCOUNT"}]}
            r = H.clay("audiences", "create", "--entity-type", "companies", "--name", name, "--description", f"Signal-marketing loop cohort {cid}, {arm} arm. Campaign {camp}.", "--filter", json.dumps(flt))
            log.append(f"    segment {name}: {r.get('id') or r.get('_error')}")
    state = H.State(P(cfg["sources"]["state_file"]))
    if live_stamp:
        state.d.setdefault("cohort", {}).update({d: f"{cid}|{'test' if d in test else 'holdout'}" for d in kept})
        state.save()
    write_manifest(outdir, cid, camp, cfg, log, kept, people, waiting=False, test=test, hold=hold, clock=clock)
    log.append(f"evt: {LOG_FAMILY}-{TODAY.isoformat()}#{cid.lower()}")
    return finish(log)


def write_manifest(outdir, cid, camp, cfg, log, kept, people, waiting, test=(), hold=(), clock=None):
    p = os.path.join(outdir, f"{cid}.md")
    lines = [f"# Cohort {cid}{' (WAITING, not cut)' if waiting else ''}", "", f"Salesforce campaign: `{camp}`", f"Motion: {cfg['cohort']['motion_label']}",
             f"Cut date: {TODAY.isoformat()}", f"Accounts: {len(kept)}; people: {len(people)}; matchable: {sum(1 for x in people if x['email'])}", ""]
    if not waiting:
        lines += ["## Arms", f"- test (ads + sequence): {len(test)}: " + ", ".join(sorted(test)), f"- holdout (sequence only): {len(hold)}: " + ", ".join(sorted(hold)), "", "## Clock"]
        lines += [f"- {k}: {v.isoformat()}" for k, v in (clock or {}).items()]
        lines += ["", "## Scorecard (fill at T+30)", "| metric | test | holdout |", "|---|---|---|",
                  "| people | | |", "| ad impressions / CTR / spend | | n/a |", "| site sessions from cohort accounts | | |",
                  "| lemlist delivered / clicks / replies / positive | | |", "| meetings | | |", "| opps / ACV (candidates until confirmed) | | |",
                  "| cost per meeting incl. ad share (Cold baseline $3,402) | | |"]
    lines += ["", "## Log excerpt"] + log[-12:]
    with open(p, "w") as f:
        f.write("\n".join(lines) + "\n")
    log.append(f"- manifest: {p}")


def finish(log):
    os.makedirs(H.LOG_DIR, exist_ok=True)
    out = os.path.join(H.LOG_DIR, f"{LOG_FAMILY}-{TODAY.isoformat()}.md")
    with open(out, "w") as f:
        f.write("\n".join(log) + "\n")
    print("\n".join(log))
    print(f"... written {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
