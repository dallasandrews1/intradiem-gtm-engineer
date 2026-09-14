#!/usr/bin/env python3
"""Offline tests for campaign_scorecard.py (fixture campaigns, seeded history, scratch dirs, no network)."""
import csv, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); AUTO = os.path.dirname(HERE)
SC = os.path.join(AUTO, "campaign_scorecard.py")


def leads(**kw):
    out = []
    for state, n in kw.items():
        system = {"scanned": "review", "reviewed": "reviewed", "emailsBounced": "done",
                  "variableUnsubscribed": "unsubscribed"}.get(state, "inProgress")
        out += [{"state": state, "stateSystem": system}] * n
    return out


def run():
    checks = []
    def check(n, c): checks.append((n, c))
    tmp = tempfile.mkdtemp(); out = os.path.join(tmp, "logs"); council = os.path.join(tmp, "council")
    fx = os.path.join(tmp, "fx.json")
    stalled_fp = "emailsSent=8|linkedinVisitDone=21"
    fixture = {
        "campaigns": {
            "cam_stall": {"name": "Stars - Fresh Pool / Quality (Nate)", "status": "running", "rep": "nathan",
                          "leads": leads(linkedinVisitDone=21, emailsSent=8), "open_tasks": 22},
            "cam_move": {"name": "BO Expansion - Insurance (Nate)", "status": "running", "rep": "nathan",
                         "leads": leads(linkedinVisitDone=30, emailsReplied=2, interested=1), "open_tasks": 33},
            "cam_draft": {"name": "DWO Executives - Live Pool (Nate)", "status": "paused", "rep": "nathan",
                          "leads": leads(scanned=803), "open_tasks": 0},
            "cam_rep": {"name": "UU Water", "status": "running", "rep": "jack",
                        "leads": leads(emailsSent=4, reviewed=1, emailsBounced=1, variableUnsubscribed=1), "open_tasks": 0},
        },
        "relay": {"cam_move": {"meetingBooked": 1, "linkedinInvitationAccepted": 3}},
        "seed_history": [
            {"date": "2026-09-09", "campaign_id": "cam_stall", "campaign": "x", "status": "running", "open_tasks": "22", "fingerprint": stalled_fp, "replied": "0", "interested": "0", "meetings": "0"},
            {"date": "2026-09-10", "campaign_id": "cam_stall", "campaign": "x", "status": "running", "open_tasks": "22", "fingerprint": stalled_fp, "replied": "0", "interested": "0", "meetings": "0"},
            {"date": "2026-09-11", "campaign_id": "cam_stall", "campaign": "x", "status": "running", "open_tasks": "22", "fingerprint": "", "replied": "0", "interested": "0", "meetings": "0"},
            {"date": "2026-09-12", "campaign_id": "cam_move", "campaign": "y", "status": "running", "open_tasks": "33", "fingerprint": "linkedinVisitDone=31", "replied": "0", "interested": "0", "meetings": "0"},
        ],
    }
    json.dump(fixture, open(fx, "w"))
    capf = os.path.join(tmp, "cap.json")
    json.dump({"mailboxes": {"main@x.com": {"rep": "nathan", "daily_cap": 30, "active_from": "2026-08-31"},
                             "second@x.com": {"rep": "nathan", "daily_cap": 30, "active_from": "2026-09-25", "ramp": [{"from": "2026-09-25", "daily_cap": 15}, {"from": "2026-10-02", "daily_cap": 30}]},
                             "jack@x.com": {"rep": "jack", "daily_cap": 30, "active_from": "2026-07-01", "note": "UNVERIFIED"}},
               "default_mailbox_by_rep": {"nathan": "main@x.com", "jack": "jack@x.com"},
               "campaign_mailbox": {"cam_draft": "second@x.com"}}, open(capf, "w"))
    cmd = [sys.executable, SC, "--fixture", fx, "--out-dir", out, "--council-dir", council, "--date", "2026-09-13", "--capacity", capf]
    r = subprocess.run(cmd, capture_output=True, text=True)
    check("run exits 0", r.returncode == 0)
    log = open(os.path.join(out, "campaign-scorecard-2026-09-13.md")).read() if r.returncode == 0 else ""
    check("stalled campaign is flagged with days and an evt id",
          "STALLED 4d: Stars - Fresh Pool / Quality (Nate)" in log and "evt: campaign-scorecard-2026-09-13#stars-fresh-pool-quality-stalled" in log)
    check("moving campaign is not flagged stalled", not any(l.startswith("- STALLED") and "BO Expansion - Insurance" in l for l in log.splitlines()))
    check("draft campaign has no verdict", "| DWO Executives - Live Pool (Nate) | DWO Executives | nathan | paused | 803 | 0 |" in log and "STALLED 0d" not in log)
    check("replied/interested/meetings become receipts candidates", all(m in log for m in ("replied 0 -> 2", "interested 0 -> 1", "meetings 0 -> 1")))
    cand = os.path.join(out, "receipts_candidates.csv")
    check("receipts_candidates.csv written with evt ids", os.path.exists(cand) and sum(1 for _ in csv.DictReader(open(cand))) == 3
          and all(row["evt"].startswith("campaign-scorecard-2026-09-13#") for row in csv.DictReader(open(cand))))
    hist = list(csv.DictReader(open(os.path.join(out, "campaign_scorecard_history.csv"))))
    check("history keeps seed rows plus one row per campaign for today", sum(1 for h in hist if h["date"] == "2026-09-13") == 4 and len(hist) == 8)
    r2 = subprocess.run(cmd, capture_output=True, text=True)
    hist2 = list(csv.DictReader(open(os.path.join(out, "campaign_scorecard_history.csv"))))
    check("re-running the same day replaces, never duplicates", len(hist2) == 8)
    check("second run mints no new receipts candidates", sum(1 for _ in csv.DictReader(open(cand))) == 3)
    cc = list(csv.DictReader(open(os.path.join(council, "GTM_Engineering_Scorecard_2026-09.csv"))))
    stars = [c for c in cc if c["Campaign"].startswith("Stars")][0]
    check("council CSV carries launched, touches, replies, source", stars["Leads launched"] == "29" and stars["Leads at email step"] == "8"
          and stars["Leads at LinkedIn step"] == "21" and stars["Source"] == "GTM Engineering" and stars["Opportunities (Salesforce)"] == "")
    rep = [c for c in cc if c["Campaign"] == "UU Water"][0]
    check("rep-built campaign is labelled, bounces and unsubscribes counted", rep["Motion"] == "Rep-built" and rep["Bounced"] == "1" and rep["Unsubscribed"] == "1" and rep["Leads launched"] == "6")
    check("headline separates engine campaigns from rep-built", "Engine campaigns mapped: 3" in log and "rep-built mapped: 1" in log)
    check("capacity: future mailbox reports start date, ramp cap and days to drain", "- second@x.com: 803 waiting leads across 1 campaigns, starts 2026-09-25, then 54 days for one touch at 15/day (ramp: 15/day from 2026-09-25, 30/day from 2026-10-02)" in log)
    check("capacity: live mailbox with nothing waiting reports 0 days", "- main@x.com: 0 waiting leads across 0 campaigns, from today, 0 days for one touch at 30/day" in log)
    check("capacity: unverified cap is labelled", "jack@x.com: 1 waiting leads across 1 campaigns, from today, 1 days for one touch at 30/day UNVERIFIED cap" in log)
    check("capacity: engine total waiting line", "Engine total waiting: 803 leads" in log)
    dwo = [c for c in cc if c["Campaign"].startswith("DWO")][0]
    check("council CSV carries mailbox and days to drain", dwo["Mailbox"] == "second@x.com" and dwo["Days to drain (alone)"] == "54")
    check("history rows carry mailbox and waiting", any(h.get("mailbox") == "second@x.com" and h.get("waiting") == "803" for h in hist2))
    check("never-launched leads are counted", "Loaded but never launched (engine): 803 leads across 1 campaigns" in log)
    for n, c in checks:
        print(("  PASS  " if c else "  FAIL  ") + n)
    ok = sum(1 for _, c in checks if c)
    print("-" * 56); print(f"{ok}/{len(checks)} passed")
    if r.returncode != 0:
        print(r.stdout, r.stderr)
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(run())
