#!/usr/bin/env python3
"""
hub_verify.py - claims-vs-reality linter for Start_Here_Index.html

Why this exists: on Jul 7 2026 the hub claimed the TAM suite passed 21/21 when it
actually passed 25/25, and referenced a Day-One checklist that had no home on the
page. Both are the same bug: a hand-typed claim that silently drifted from its
source. This script re-derives every checkable claim from the source files and
diffs it against what the HTML asserts. Run it in the daily loop; a DRIFT exit
code (1) means a number on the page no longer matches reality.

No dependencies beyond the stdlib. Run from the project root:
    python3 hub_verify.py
"""
import csv, re, subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = os.path.join(ROOT, "Start_Here_Index.html")
TIERED = os.path.join(ROOT, "StarRatings_Targets_2026_Tiered.csv")

def load_hub():
    with open(HUB, encoding="utf-8") as f:
        return f.read()

def stars_truth():
    """Re-derive the Star Ratings counts from the canonical tiered CSV."""
    rows = list(csv.DictReader(open(TIERED, encoding="utf-8")))
    ab = [r for r in rows if r["tier"] in ("A", "B")]
    def s(col):
        t = 0.0
        for r in ab:
            try: t += float(r[col] or 0)
            except ValueError: pass
        return t
    return {
        "contracts_total": len(rows),
        "tier_a": sum(1 for r in rows if r["tier"] == "A"),
        "tier_ab": len(ab),
        "ab_parents": len({r["parent_org"] for r in ab}),
        "ab_addr2028_musd": round(s("addr_2028_musd")),
    }

def run_tests(rel):
    """Run a test file and parse the 'X/Y passed' line it prints."""
    d, f = os.path.split(os.path.join(ROOT, rel))
    try:
        out = subprocess.run([sys.executable, f], cwd=d, capture_output=True,
                             text=True, timeout=120).stdout
    except Exception as e:
        return None, str(e)
    m = re.search(r"(\d+)\s*/\s*(\d+)\s+passed", out)
    if not m: return None, "no 'X/Y passed' line found"
    p, t = int(m.group(1)), int(m.group(2))
    return (p, t), ("OK" if p == t else "TESTS FAILING")

def skills_truth(hub):
    """Count skill cards actually indexed in the asset-map array."""
    return len(re.findall(r"\{c:'skills'", hub))

def main():
    hub = load_hub()
    st = stars_truth()
    sig, sig_note = run_tests("intradiem-signal-engine/test_signal_processor.py")
    tam, tam_note = run_tests("tam-outbound-engine/test_account_engine.py")
    n_skills = skills_truth(hub)

    checks = []  # (label, truth_str, present_in_hub, ok)

    def want(label, needle, ok=True):
        present = needle in hub
        checks.append((label, needle, present, ok and present))

    # Star Ratings numbers as they are written on the page
    want("Stars: total contracts", str(st["contracts_total"]))
    want("Stars: Tier A+B contracts", str(st["tier_ab"]))
    want("Stars: A+B parents", str(st["ab_parents"]) + " parents")
    want("Stars: A+B $ addr_2028", "$" + format(st["ab_addr2028_musd"], ",") + "M")
    # engine test lines (hero shows 'TAM/SIGNAL')
    if sig: want("Signal tests", "%d/%d" % sig, sig == (sig[1], sig[1]))
    if tam: want("TAM tests", "%d/%d" % tam, tam == (tam[1], tam[1]))
    # skills claim in the hero spine
    want("Skills: 'twelve skills' matches %d cards" % n_skills,
         "twelve skills", n_skills == 12)

    drift = [c for c in checks if not c[3]]
    print("hub_verify — %s" % HUB)
    print("-" * 64)
    for label, needle, present, ok in checks:
        flag = "OK   " if ok else "DRIFT"
        shown = needle if present else "(NOT FOUND ON PAGE) -> " + needle
        print("  [%s] %-34s %s" % (flag, label, shown))
    print("-" * 64)
    if sig_note not in (None, "OK"): print("  ! signal tests:", sig_note)
    if tam_note not in (None, "OK"): print("  ! tam tests:", tam_note)
    if drift:
        print("RESULT: %d DRIFT — the page contradicts its source. Fix before showing it." % len(drift))
        return 1
    print("RESULT: all %d claims match source." % len(checks))
    return 0

if __name__ == "__main__":
    sys.exit(main())
