#!/usr/bin/env python3
"""Grade rows in the PMO validation queue, one at a time, from the terminal.

    python3 automation/pmo/grade.py            # ungraded rows, in order
    python3 automation/pmo/grade.py --limit 20 # stop after 20 verdicts
    python3 automation/pmo/grade.py --stats    # just print precision so far

Keys:  c correct   o wrong_owner   d wrong_date   n not_an_action   u duplicate
       s skip (leave blank)   q save and quit
After a verdict you may type a short note, or press Enter for none.
Writes back to validation_queue.csv with every field quoted, columns unchanged.
The pmo-action-extractor reads the graded rows on its next run and reports precision.
"""
import csv, sys, pathlib, textwrap

Q = pathlib.Path(__file__).with_name("validation_queue.csv")
KEYS = {"c": "correct", "o": "wrong_owner", "d": "wrong_date", "n": "not_an_action", "u": "duplicate"}

def load():
    with Q.open(newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)

def save(fields, rows):
    tmp = Q.with_suffix(".tmp")
    with tmp.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)
    tmp.replace(Q)

def stats(rows):
    graded = [r for r in rows if r["verdict"].strip()]
    if not graded:
        print("0 graded, accuracy not yet measurable"); return
    correct = sum(1 for r in graded if r["verdict"] == "correct")
    counts = {v: sum(1 for r in graded if r["verdict"] == v) for v in KEYS.values() if v != "correct"}
    print(f"{len(graded)} graded, precision {correct/len(graded)*100:.0f}% ({correct} correct; "
          + ", ".join(f"{k} {v}" for k, v in counts.items()) + f"); {len(rows)-len(graded)} left")

def show(r, i, n):
    print("\n" + "=" * 78)
    print(f"[{i}/{n}] {r['id']}   owner: {r['owner']}   due: {r['due']} ({r['due_basis']})   {r['confidence']}")
    print("-" * 78)
    print(textwrap.fill("ACTION   " + r["action"], 78, subsequent_indent="         "))
    print(textwrap.fill("SOURCE   " + r["source_type"] + ": " + r["source_ref"] + "  (" + r["source_date"] + ")", 78, subsequent_indent="         "))
    print(textwrap.fill("EVIDENCE \"" + r["evidence"] + "\"", 78, subsequent_indent="         "))

def main():
    fields, rows = load()
    if "--stats" in sys.argv:
        stats(rows); return
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    todo = [r for r in rows if not r["verdict"].strip()]
    if not todo:
        print("Nothing left to grade."); stats(rows); return
    print(__doc__.split("Keys:")[1].strip() if False else "Keys: c correct  o wrong_owner  d wrong_date  n not_an_action  u duplicate  s skip  q quit")
    done = 0
    for i, r in enumerate(todo, 1):
        if limit and done >= limit: break
        show(r, i, len(todo))
        while True:
            k = input("verdict> ").strip().lower()
            if k in KEYS or k in ("s", "q"): break
            print("  c / o / d / n / u / s / q")
        if k == "q": break
        if k == "s": continue
        r["verdict"] = KEYS[k]
        note = input("note (Enter for none)> ").strip()
        if note: r["verdict_note"] = note
        done += 1
        save(fields, rows)
    save(fields, rows)
    print()
    stats(rows)

if __name__ == "__main__":
    main()
