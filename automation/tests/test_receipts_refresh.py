#!/usr/bin/env python3
"""Offline tests for receipts_refresh.py (scratch ledger, receipts, history, candidates; --no-clay)."""
import hashlib, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); AUTO = os.path.dirname(HERE)
RR = os.path.join(AUTO, "receipts_refresh.py")


def sha(p):
    return hashlib.sha1(open(p, "rb").read()).hexdigest()


def run():
    checks = []
    def check(n, c): checks.append((n, c))
    tmp = tempfile.mkdtemp(); out = os.path.join(tmp, "logs")
    receipts = os.path.join(tmp, "credit_pipeline_receipts.md")
    open(receipts, "w").write("# Credit -> Pipeline Receipts Ledger\n\n## Headline (update daily)\nAs of 2026-07-19: ~846 credits spent -> 23 sends, 2 replies.\n\n| 2026-07-18 | 71,221.1 | Stars wave 1 |\n| 2026-07-19 | 71,154.4 | tests |\n")
    ledger = os.path.join(tmp, "Clay_Credit_Ledger.md")
    open(ledger, "w").write("# Clay Credit Ledger\n\n## Ledger entries\n2026-07-10 · old · 12 credits · before the receipts date\n2026-09-05 · Verified tech-stack read · **1,875 Clay credits** · drained the prospect queue\n2026-09-09 · Back Office Maps, JW · **50.5 Clay credits** · Enrich Person\n2026-09-10 · UPT displacement committee build · free path first · 0 credits noted later\n2026-09-11 · Segment build · no figure on this line\n")
    history = os.path.join(tmp, "history.csv")
    open(history, "w").write("date,campaign_id,campaign,motion,rep,status,leads,not_launched,in_progress,email_touch,li_touch,replied,interested,bounced,unsubscribed,meetings,li_accepted,open_tasks,fingerprint\n"
                             "2026-09-12,cam_a,Stars A,Star Ratings,nathan,running,29,0,29,8,21,0,0,0,0,0,0,22,x\n"
                             "2026-09-13,cam_a,Stars A,Star Ratings,nathan,running,29,0,29,8,21,1,0,0,0,0,0,22,y\n"
                             "2026-09-13,cam_b,BO Ins,Back Office (customer lanes),nathan,running,33,0,33,2,31,1,1,0,0,1,0,33,z\n"
                             "2026-09-13,cam_c,UU Water,Rep-built,jack,running,5,1,4,4,0,0,0,1,0,0,0,0,w\n")
    cands = os.path.join(tmp, "cands.csv")
    open(cands, "w").write("date,campaign_id,campaign,metric,prior,now,evt\n2026-07-01,cam_a,Stars A,replied,0,1,campaign-scorecard-2026-07-01#old\n2026-09-13,cam_b,BO Ins,meetings,0,1,campaign-scorecard-2026-09-13#bo-ins-meetings\n")
    before = (sha(receipts), sha(ledger))
    cmd = [sys.executable, RR, "--date", "2026-09-14", "--out-dir", out, "--ledger", ledger, "--receipts", receipts, "--history", history, "--candidates", cands, "--no-clay"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    check("run exits 0", r.returncode == 0)
    log = open(os.path.join(out, "receipts-refresh-2026-09-14.md")).read() if r.returncode == 0 else ""
    check("never edits the receipts ledger or the credit ledger", (sha(receipts), sha(ledger)) == before)
    check("finds the receipts ledger's last date", "last dated entry: 2026-07-19" in log)
    check("sums only credit entries after that date", "1,925.5 credits with a figure" in log and "12 credits" not in log.split("PROPOSED")[1])
    check("counts undated-figure lines separately (a 0-credit line counts as priced)", "1 without" in log)
    check("aggregates the engine funnel per motion from the latest read", "| Star Ratings | 1 | 29 | 29 | 1 | 0 | 0 |" in log and "| Back Office (customer lanes) | 1 | 33 | 33 | 1 | 1 | 1 |" in log)
    check("keeps rep-built out of the headline funnel", "2 replies, 1 interested, 1 booked meetings" in log)
    check("only candidates newer than the ledger date are proposed, as CANDIDATE", "cam_b" not in log.split("Receipts (proposed")[0] and "meetings 0 -> 1 | CANDIDATE, unconfirmed" in log and "2026-07-01 | Stars A" not in log)
    check("cost per reply and per meeting computed from the same window", "963 credits per reply" in log and "1,926 credits per meeting" in log)
    check("approve line and evt id present", "APPROVE receipts-2026-09-14" in log and "evt: receipts-refresh-2026-09-14#receipts-2026-09-14" in log)
    pend = json.load(open(os.path.join(out, "receipts_refresh_pending.json")))
    check("pending json carries the block and id", pend["id"] == "receipts-2026-09-14" and pend["status"] == "pending" and "## Headline" in pend["block"])
    for n, c in checks:
        print(("  PASS  " if c else "  FAIL  ") + n)
    ok = sum(1 for _, c in checks if c)
    print("-" * 56); print(f"{ok}/{len(checks)} passed")
    if r.returncode != 0:
        print(r.stdout, r.stderr)
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(run())
