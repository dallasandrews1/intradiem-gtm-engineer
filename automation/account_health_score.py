#!/usr/bin/env python3
"""Account-health scorer. Reads automation/config/account_health.json and each account's evidence file,
computes status per reason code and overall, and writes automation/logs/account-health-<date>.md with evt anchors.
Deterministic, log-only. Usage: python3 automation/account_health_score.py [--date YYYY-MM-DD] [--dry-run]"""
import json, pathlib, datetime, sys, argparse
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument("--date"); ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
today = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
cfg = json.loads((ROOT / "automation/config/account_health.json").read_text())
fam = cfg["log_family"]; out = ROOT / "automation/logs" / f"{fam}-{today}.md"
RANK = {"GREEN": 0, "YELLOW": 1, "RED": 2}
lines = [f"# Account health watch, {today}", "", f"RUN COMPLETE {datetime.datetime.now():%H:%M} (scorer; evidence as recorded in each account's evidence file)", ""]
prev = sorted((ROOT / "automation/logs").glob(f"{fam}-*.md"))
prev = [p for p in prev if p.name != out.name]
prev_state = {}
if prev:
    for l in prev[-1].read_text().splitlines():
        if l.startswith("state: "):
            try: prev_state = json.loads(l[7:])
            except Exception: pass
state = {}
for acct in cfg["accounts"]:
    ev_path = ROOT / cfg["evidence_dir"] / f"evidence_{acct['slug']}.json"
    if not ev_path.exists():
        lines += [f"## {acct['name']}", f"BLOCKED: no evidence file at {ev_path.relative_to(ROOT)}", ""]; continue
    ev = json.loads(ev_path.read_text())
    codes = {c["code"]: c for c in ev["codes"]}
    # Renewal clock is computed, never hand-set
    days = (datetime.date.fromisoformat(acct["renewal_date"]) - today).days
    rc = cfg["reason_codes"]["Renewal clock"]
    codes.setdefault("Renewal clock", {"code": "Renewal clock", "evidence": []})
    codes["Renewal clock"]["status"] = "RED" if days <= rc["red_days_to_renewal"] else "YELLOW" if days <= rc["yellow_days_to_renewal"] else "GREEN"
    codes["Renewal clock"]["computed"] = f"{days} days to {acct['renewal_date']}"
    reds = [k for k, c in codes.items() if c["status"] == "RED"]
    overall = "RED" if any(k in reds for k in ("Value dispute", "Renewal clock", "Competitive event")) or len(reds) >= 3 \
        else "YELLOW" if any(c["status"] in ("YELLOW", "RED") for c in codes.values()) else "GREEN"
    slug = acct["slug"].replace("_", "-")
    lines += [f"## {acct['name']}: {overall} ({len(reds)} of {len(codes)} codes red, {codes['Renewal clock']['computed']})",
              f"AM {acct['am']}, SM {acct['success_manager']}, sponsor {acct['sponsor']}, customer owner {acct['customer_owner']}", ""]
    for k, c in codes.items():
        was = prev_state.get(acct["slug"], {}).get(k)
        change = f" (was {was})" if was and was != c["status"] else ""
        lines.append(f"- **{k}: {c['status']}**{change}")
        for src, dt, line in c.get("evidence", [])[:3]:
            lines.append(f"  - {src}, {dt}: {line}")
        if c.get("computed"): lines.append(f"  - computed: {c['computed']}")
        if change or (not was and c["status"] == "RED"):
            lines.append(f"  - evt: {fam}-{today}#{slug}-{k.lower().replace(' ', '-')}")
    lines.append("")
    state[acct["slug"]] = {k: c["status"] for k, c in codes.items()} | {"overall": overall}
    if overall == "RED":
        lines += [f"Overall RED. Save Room: motions/churn_risk_save_plan/Cleveland_Clinic_Save_Room_Sep10.html. Open items: {cfg['evidence_dir']}/Cleveland_Clinic_PMO_Tracker_Import.csv.",
                  f"evt: {fam}-{today}#{slug}-overall-red" if prev_state.get(acct["slug"], {}).get("overall") != "RED" else f"chain: {fam}-{prev[-1].name[len(fam)+1:-3] if prev else today}#{slug}-overall-red", ""]
lines += ["Digest: " + cfg["digest"]["status"] + ". Nobody was messaged; the daily rundown reads this file.", "", "state: " + json.dumps(state)]
text = "\n".join(lines) + "\n"
if a.dry_run: print(text)
else:
    out.write_text(text); print(f"wrote {out.relative_to(ROOT)}")
