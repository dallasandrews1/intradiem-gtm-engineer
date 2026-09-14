#!/usr/bin/env python3
"""Checks for polar_intake.py. Run: python3 automation/test_polar_intake.py (uses a temp inbox, touches no real log)."""
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = HERE / "polar_intake.py"
CONFIG = json.loads((HERE / "config" / "polar_tasks.json").read_text())["tasks"]
passed = 0
failed = 0


def check(name, cond, detail=""):
    global passed, failed
    if cond:
        passed += 1
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} {detail}")


def run(inbox, *extra):
    return subprocess.run([sys.executable, str(SCRIPT), "--inbox", str(inbox), *extra], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as td:
    inbox = pathlib.Path(td) / "polar"
    inbox.mkdir()

    print("1. empty inbox")
    r = run(inbox)
    check("exit 0", r.returncode == 0, r.stderr)
    check("says nothing new", "nothing new" in r.stdout, r.stdout)

    print("2. registered task with report and a missing expected file")
    t = inbox / "wfm-l3-lookup-rebind"
    t.mkdir()
    (t / "report.md").write_text("# report\nRow value now shows the Company Domain chip.\nRan on 524 rows.\n")
    (t / "after.png").write_bytes(b"\x89PNG fake")
    r = run(inbox)
    check("dry run exits 0", r.returncode == 0, r.stderr)
    check("names the task title", CONFIG["wfm-l3-lookup-rebind"]["title"].split(":")[0] in r.stdout, r.stdout)
    check("optional-download note when expect is empty", "optional downloads" in r.stdout, r.stdout)
    check("carries the verifier", "VERIFICATION OWED (gate-integrity-auditor)" in r.stdout, r.stdout)
    check("mints an evt id", "evt: polar-intake-" in r.stdout and "#wfm-l3-lookup-rebind" in r.stdout, r.stdout)
    check("cites the chain", "chain: gate-integrity-2026-08-20#wfm-l3-customer-lookup-inert" in r.stdout, r.stdout)
    check("quotes the report as a claim", "a claim until verified" in r.stdout and "Ran on 524 rows." in r.stdout, r.stdout)
    check("dry run writes no state", not (inbox / ".intake-state").exists())

    print("3. unregistered folder")
    u = inbox / "something-else"
    u.mkdir()
    (u / "x.csv").write_text("a,b\n1,2\n")
    r = run(inbox, "--task", "something-else")
    check("marked UNREGISTERED", "UNREGISTERED" in r.stdout, r.stdout)
    check("--task filters to that folder only", "wfm-l3-lookup-rebind" not in r.stdout, r.stdout)

    print("4. state prevents double logging (apply into the temp inbox only)")
    # Redirect the log dir by running from a temp cwd is not supported; instead check state semantics via a second dry run after a manual state write.
    state = {"files": [{"task": "wfm-l3-lookup-rebind", "path": "x", "sha": __import__("hashlib").sha256((t / "report.md").read_bytes()).hexdigest(), "processed": "2026-09-13"}]}
    (inbox / ".intake-state").write_text(json.dumps(state))
    r = run(inbox, "--task", "wfm-l3-lookup-rebind")
    check("already-seen report.md skipped", "report.md`" not in r.stdout, r.stdout)
    check("unseen after.png still listed", "after.png" in r.stdout, r.stdout)

    print("5. paste mode")
    r = subprocess.run([sys.executable, str(SCRIPT), "--paste", "stars-resurrection-stray-steps"], input="REPORT stars-resurrection-stray-steps\nDeleted two STRAY steps.\nCampaign status: running.\n", capture_output=True, text=True)
    check("paste dry run exits 0", r.returncode == 0, r.stderr)
    check("paste quotes the block as a claim", "as pasted (a claim until verified)" in r.stdout and "Deleted two STRAY steps." in r.stdout, r.stdout)
    check("paste carries the lemlist verifier", "VERIFICATION OWED (lemlist-lead-integrity)" in r.stdout, r.stdout)
    check("paste mints evt", "#stars-resurrection-stray-steps" in r.stdout, r.stdout)
    r = subprocess.run([sys.executable, str(SCRIPT), "--paste", "nope-task"], input="x\n", capture_output=True, text=True)
    check("paste unknown slug is UNREGISTERED", "UNREGISTERED" in r.stdout, r.stdout)

    print("6. registry sanity")
    for slug, reg in CONFIG.items():
        check(f"{slug} has sheet, verifier, verifier_agent, report", all(k in reg for k in ("sheet", "verifier", "verifier_agent", "report")))
        check(f"{slug} sheet file exists", (HERE.parent / reg["sheet"]).exists(), reg["sheet"])

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
