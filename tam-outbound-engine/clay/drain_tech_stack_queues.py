#!/usr/bin/env python3
"""Drain the Tech stack read work queues through the Clay workflow, ten companies at a time.

Runs the customer queue first, then the prospect queue. After every batch it waits until the
queue has shrunk by the batch size before starting the next one, so a broken step can never
re-run the same companies (that mistake cost 70 credits on Sep 5). It stops on two stalls or
more than two failed runs in a batch. One PredictLeads credit per company.

Run from anywhere:
    python3 tam-outbound-engine/clay/drain_tech_stack_queues.py            # runs until both queues are empty
    python3 tam-outbound-engine/clay/drain_tech_stack_queues.py --minutes 9  # one bounded chunk, rerun to continue
Ctrl-C is safe at any point; the in-flight batch finishes on Clay's side and the queue keeps its state.
Progress and totals print to the terminal and append to data/tech_stack_drain.log.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
LOG = os.path.join(DATA, "tech_stack_drain.log")
STATE = os.path.join(DATA, "tech_stack_drain_state.json")
WF = "wf_0tkv9u0BKvNYsV4NsQx"
QUEUES = [
    ("customer", "audseg_0tkvgivRoHnytvdRk9J", 200),      # SF Customer accounts not yet read (81 on Sep 5)
    ("prospect", "audseg_0tkv9vq4SZBjZdJuiYi", 1900),     # SF Prospect accounts not yet read (1,743 on Sep 5)
]


def cl(*a):
    q = subprocess.run(["clay", *a], capture_output=True, text=True)
    return q.stdout or q.stderr


def count(sid):
    for _ in range(3):
        try:
            return json.loads(cl("audiences", "records", "search-count", "--entity-type", "companies",
                                 "--audience-id", sid))["count"]
        except Exception:
            time.sleep(3)
    return None


def failed_recent(sid, since):
    try:
        d = json.loads(cl("workflows", "runs", "list", WF, "--audience-segment", sid, "--limit", "30")).get("data", [])
    except Exception:
        return 0
    return sum(1 for r in d if r.get("status") == "failed" and r.get("createdAt", "") > since)


def log(m):
    line = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {m}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=0, help="stop after this many minutes (0 = run to empty)")
    args = ap.parse_args()
    budget = args.minutes * 60
    t0 = time.time()
    try:
        state = json.load(open(STATE))
    except Exception:
        state = {"spent": {}, "stopped": {}}

    for name, sid, cap in QUEUES:
        if state["stopped"].get(name):
            log(f"[{name}] previously stopped: {state['stopped'][name]} (delete {STATE} to reset)")
            continue
        spent = state["spent"].get(name, 0)
        c = count(sid)
        log(f"[{name}] queue {c}, spent so far {spent}, cap {cap}")
        stalls = 0
        while c and c > 0 and spent < cap and (not budget or time.time() - t0 < budget):
            n = min(10, c)
            before = c
            since = datetime.datetime.utcnow().isoformat()
            cl("workflows", "runs", "test", WF, "--audience-segment", sid, "--limit", str(n))
            spent += n
            state["spent"][name] = spent
            json.dump(state, open(STATE, "w"))
            drained = False
            for _ in range(36):
                time.sleep(5)
                c = count(sid)
                if c is not None and c <= before - n:
                    drained = True
                    break
            f = failed_recent(sid, since)
            if not drained:
                stalls += 1
                log(f"[{name}] batch {n}: {before} -> {c} did NOT drain (stall {stalls}, failed runs {f})")
                if stalls >= 2:
                    state["stopped"][name] = "two stalls"
                    break
                time.sleep(20)
                c = count(sid)
                continue
            stalls = 0
            if f > 2:
                log(f"[{name}] stopping: {f} failed runs in the batch")
                state["stopped"][name] = f"{f} failed runs"
                break
            if spent % 100 < 10:
                log(f"[{name}] {spent} credits, queue {c}")
        json.dump(state, open(STATE, "w"))
        log(f"[{name}] end of pass: spent {spent}, queue {count(sid)}")
        if budget and time.time() - t0 >= budget:
            log("time budget reached; rerun to continue")
            break
    log("DONE")


if __name__ == "__main__":
    main()
