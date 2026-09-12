#!/usr/bin/env python3
"""Generate gtm_state.json: the one snapshot every hosted surface reads.

Runs where the engines and the real data live (this machine, nightly off
automation/sync_publish.sh), NOT inside the brain container. The brain fetches the
published file over HTTP, so refreshing the seller-facing data is a file publish, not a
container rebuild. That is the whole point: before this, the only way to change what the
brain served was to redeploy it, so nobody did, and it served July data into September.

Usage:
    python3 build_gtm_state.py                     # write ./gtm_state.json
    python3 build_gtm_state.py --output PATH       # write somewhere else
    python3 build_gtm_state.py --print             # dump to stdout, write nothing
"""
import argparse
import datetime
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for _p in ("tam-outbound-engine", "intradiem-signal-engine", "impact"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import gtm_state  # noqa: E402

REVIEWS = os.path.join(ROOT, "automation", "config", "signal_reviews.json")
UNIVERSE_CFG = os.path.join(ROOT, "tam-outbound-engine", "config", "universe.json")


def rebuild_universe():
    """Live loop (2026-09-11): regenerate the strike universe from the Audiences segment before
    scoring, when config/universe.json says source=audiences. Fails closed: on any error the last
    written CSVs stay and the snapshot carries errors["universe"] so the brain can say so."""
    try:
        cfg = json.load(open(UNIVERSE_CFG))
    except (OSError, ValueError):
        return None
    if cfg.get("source") != "audiences":
        return "csv"
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tam-outbound-engine", "universe_from_audiences.py")],
                       capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout).strip().splitlines()[-1] if (r.stderr or r.stdout).strip() else f"exit {r.returncode}")
    return "audiences"


def load_reviews():
    try:
        return json.load(open(REVIEWS))
    except (OSError, ValueError):
        return {"signals": []}


def unreviewed_by_domain(reviews):
    out = {}
    for sg in reviews.get("signals", []):
        if sg.get("state") != "unreviewed" or not sg.get("domain"):
            continue
        out.setdefault(sg["domain"], []).append({
            "id": sg["id"], "state": "unreviewed", "trigger_type": sg.get("trigger_type"), "date": sg.get("date"),
            "quote": sg.get("quote"), "url": sg.get("url"), "org": sg.get("org"),
            "note": "Unreviewed war-room signal: context only. It does not score and no copy is written from it. "
                    "Reply APPROVE <id> or DENY <id> in the rundown thread.",
        })
    return out


def build_strike():
    import account_engine
    # build_plays returns (plays, excluded). The brain used to treat the tuple as a list of
    # rows, so /v1/strike raised TypeError on every call. Unpack it here, once. 2026-09-05.
    plays, excluded = account_engine.build_plays(account_engine.load_cfg(),
                                                 datetime.date.today())
    # score_account drops the `source` column when it builds a trigger record, so provenance
    # does not survive into the play. Re-attach it by (domain, type, date) so the brain can
    # scrub an UNCITED trigger's prose specifically, instead of taking the whole row's word
    # for it. The trigger that made this necessary ("won two new Medicaid state contracts")
    # was seeded and contradicted by the account's public record. 2026-09-05.
    trig_src = {}
    for t in account_engine.load_csv("triggers.csv"):
        trig_src[(t["domain"], t.get("trigger_type"), t.get("date"))] = (t.get("source") or "").strip()
    reviews = load_reviews()
    unrev = unreviewed_by_domain(reviews)
    rows = []
    for p in plays:
        rows.append({
            "company": p["company"], "domain": p["domain"], "industry": p.get("industry"),
            "icp_total": p["icp_total"], "tier": p["tier"], "dims": p.get("dims"),
            "fresh": p["fresh"], "why_now_raw": p.get("why_now_raw"),
            "agent_count": p.get("agent_count"),
            "roi_annual": p.get("roi_annual"), "roi_label": p.get("roi_label"),
            "roi_per_agent": p.get("roi_per_agent"),
            "roi_per_agent_label": p.get("roi_per_agent_label"),
            "acd": p.get("acd"), "wfm": p.get("wfm"), "tech": p.get("tech"),
            "triggers": [dict(t, source=trig_src.get((p["domain"], t.get("type"), t.get("date")), ""))
                         for t in p.get("triggers", [])],
            "committee": p.get("committee", []),
            "seller": (p["seller"] or {}).get("seller_name") if p.get("seller") else None,
            "seller_email": (p["seller"] or {}).get("seller_email") if p.get("seller") else None,
            # Provenance, per row. `seed` is the engine's own gate (account source, a
            # positive agent count, and a source on every trigger).
            "source": p.get("source", ""),
            "seed": bool(p.get("seed")),
            # Live loop: staged war-room signals awaiting Dallas's decision ride the row as
            # context. Never scored, never in copy; approved ones re-enter as cited triggers.
            "unreviewed_signals": unrev.get(p["domain"], []),
        })
    return {
        "data_source": account_engine.get_data_source(),
        "review": {"unreviewed": sum(1 for sg in reviews.get("signals", []) if sg.get("state") == "unreviewed"),
                   "approved": sum(1 for sg in reviews.get("signals", []) if sg.get("state") == "approved"),
                   "denied": sum(1 for sg in reviews.get("signals", []) if sg.get("state") == "denied")},
        "accounts": rows,
        "excluded": excluded,
        "counts": {"accounts": len(rows), "seed": sum(1 for r in rows if r["seed"]),
                   "customer_excluded": len(excluded),
                   "unreviewed_signals": sum(len(r["unreviewed_signals"]) for r in rows)},
    }


def build_signals():
    import signal_processor
    rows = signal_processor.process()
    declared = signal_processor.get_data_source()
    # The signal engine has no per-row provenance: data/accounts.csv carries no `source`
    # column and config/thresholds.json declares the whole file 'mock'. Rather than let the
    # brain serve seeded utilisation and renewal clocks as real, every row inherits the
    # declared tag. When accounts.csv becomes a real reporting export, flip that flag and
    # add a per-row source column here, the same shape the TAM engine already uses.
    seeded = declared != "live"
    out = []
    for r in rows:
        out.append({**r, "seed": seeded,
                    "source": "" if seeded else r.get("source", "")})
    return {
        "data_source": declared,
        "accounts": out,
        "counts": {"accounts": len(out), "seed": sum(1 for r in out if r["seed"])},
        "note": ("Per-row provenance is not yet wired in this engine; rows inherit the "
                 "engine-level tag." if seeded else ""),
    }


def build_impact(strike, signals):
    """Score impact on the universe we just built, never on the files on disk.

    impact_engine reads two intermediates, tam-outbound-engine/data/tam_plays.json and
    intradiem-signal-engine/data/signals.json, which are written by run_daily.sh whenever it
    last ran. On 2026-09-05 tam_plays.json was five days old and predated the
    customer-exclusion gate, so "net-new opportunity surfaced" counted Health Care Service
    Corporation, a confirmed customer, and omitted Centene, the only cited account in the
    universe. Same stale-intermediate failure as the brain's own, one layer down.

    So: write the two intermediates fresh from the run in progress, into a temp dir, point
    impact_engine at those, and restore. No side effects on the repo's data folders.
    """
    import impact_engine
    tmp = tempfile.mkdtemp(prefix="gtm_state_impact_")
    tam_path = os.path.join(tmp, "tam_plays.json")
    sig_path = os.path.join(tmp, "signals.json")
    with open(tam_path, "w") as f:
        json.dump({"generated_at": gtm_state.iso(gtm_state.utcnow()),
                   "accounts": strike["accounts"],
                   "excluded_customers": strike["excluded"]}, f, default=str)
    with open(sig_path, "w") as f:
        json.dump({"generated_at": gtm_state.iso(gtm_state.utcnow()),
                   "data_source": signals["data_source"],
                   "accounts": signals["accounts"]}, f, default=str)
    real_tam, real_sig = impact_engine.TAM, impact_engine.SIGNALS
    try:
        impact_engine.TAM, impact_engine.SIGNALS = tam_path, sig_path
        b = impact_engine.build()
    finally:
        impact_engine.TAM, impact_engine.SIGNALS = real_tam, real_sig
        shutil.rmtree(tmp, ignore_errors=True)
    # The universe is mostly seed rows, so the headline is an estimate built on
    # demonstration data. Say so on the payload rather than leaving a confident dollar
    # figure to be read at face value.
    seed = strike["counts"]["seed"]
    total = strike["counts"]["accounts"]
    b["basis"] = {
        "accounts": total, "seed_accounts": seed,
        "customer_excluded": strike["counts"]["customer_excluded"],
        "note": (f"{seed} of {total} accounts behind this figure are seed rows with no "
                 "`source`. Opportunity surfaced is an estimate on demonstration data, not "
                 "a pipeline number." if seed else
                 "Every account behind this figure carries a source."),
    }
    return b


def build():
    state = {
        "schema_version": gtm_state.SCHEMA_VERSION,
        "generated_at": gtm_state.iso(gtm_state.utcnow()),
        "generator": "gtm-hosted-platform/brain/build_gtm_state.py",
        "engines": {},
        "errors": {},
    }
    try:
        state["universe"] = rebuild_universe() or "csv"
    except Exception as e:
        state["universe"] = "stale"
        state["errors"]["universe"] = f"universe rebuild failed, last CSV kept: {type(e).__name__}: {e}"
    for name, fn in (("strike", build_strike), ("signals", build_signals)):
        try:
            state["engines"][name] = fn()
        except Exception as e:
            # Fail loud per engine, never poison the whole snapshot: a broken impact export
            # must not take the strike universe offline with it.
            state["errors"][name] = f"{type(e).__name__}: {e}"
    # impact is scored on the two engines above, so it only runs if both produced a universe
    if "strike" in state["engines"] and "signals" in state["engines"]:
        try:
            state["engines"]["impact"] = build_impact(state["engines"]["strike"],
                                                      state["engines"]["signals"])
        except Exception as e:
            state["errors"]["impact"] = f"{type(e).__name__}: {e}"
    else:
        state["errors"]["impact"] = "skipped: an upstream engine failed to build"
    return state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=os.path.join(HERE, "gtm_state.json"))
    ap.add_argument("--print", dest="to_stdout", action="store_true")
    a = ap.parse_args()
    state = build()
    text = json.dumps(state, indent=2, default=str)
    if a.to_stdout:
        print(text)
        return 0
    os.makedirs(os.path.dirname(os.path.abspath(a.output)), exist_ok=True)
    with open(a.output, "w") as f:
        f.write(text + "\n")
    s = state["engines"].get("strike", {}).get("counts", {})
    g = state["engines"].get("signals", {}).get("counts", {})
    print(f"wrote {a.output}")
    print(f"  generated_at {state['generated_at']}")
    print(f"  strike   {s.get('accounts', 0)} accounts ({s.get('seed', 0)} seed, "
          f"{s.get('customer_excluded', 0)} customer-excluded)")
    print(f"  signals  {g.get('accounts', 0)} accounts ({g.get('seed', 0)} seed)")
    if state["errors"]:
        print(f"  ERRORS: {state['errors']}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
