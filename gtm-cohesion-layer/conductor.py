#!/usr/bin/env python3
"""
Weekly Conductor — the one push that runs the GTM motion end-to-end.
Sequences: Refresh -> Re-score -> Scan signals -> Draft -> Approve(HUMAN) -> Send(gated) -> Instrument.

WIRED to the existing engines (read-only, seeded data, safe to run now):
  - intradiem-signal-engine/signal_processor.py  -> process()        [Stage 3 Signals]
  - tam-outbound-engine/account_engine.py        -> build_plays()    [Stage 2 Re-score]
  - impact/impact_engine.py                       -> build()          [Stage 7 Instrument]

Design principles (non-negotiable):
  - FAIL-CLOSED: a stage that errors stops the run; it never silently sends.
  - HUMAN GATE: Stage 5 (Approve) requires human release. The conductor only PREPARES sends.
  - DELIVERABILITY GATE: Stage 6 (Send) is skipped unless deliverability == "green".
  - MEASUREMENT BEFORE VOLUME: scoring must compute before drafting at volume.
  - ENGINE CALLS ARE BEST-EFFORT: if an engine/its data isn't available (pre-access),
    the stage logs "skipped" and the run continues. No engine failure poisons the motion.

DRY_RUN governs only the SEND side. Engine reads run either way.
Live (Jul 6+): set DRY_RUN=False + wire the TODO(live) hooks to Clay / sender / Salesforce.
"""
import json, os, importlib.util, datetime, traceback, argparse, re, hashlib

DRY_RUN = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # project folder; engines are siblings of gtm-cohesion-layer/
STATE_PATH = os.path.join(HERE, "engine_state.json")
SPEC_PATH = os.path.join(ROOT, "GTM_Engine_Build_Spec.md")  # the standing spec, reread every run (gap 3)

# GAP 2 — verified-claims gate. Flags quantified assertions ($ / % / "N points" / "Nx") that a
# "too nice" draft engine may fabricate. Time-to-meeting durations (min/minutes/days) are NOT matched.
CLAIM_PATTERNS = [
    r"\$\s?\d[\d,.]*\s?(?:k|m|b|million|billion)?\b",
    r"\d+(?:\.\d+)?\s?%",
    r"\b\d+(?:\.\d+)?\s?points?\b",
    r"\b\d+(?:\.\d+)?x\b",
]

ENGINES = {
    "signal": os.path.join(ROOT, "intradiem-signal-engine", "signal_processor.py"),
    "tam":    os.path.join(ROOT, "tam-outbound-engine", "account_engine.py"),
    "impact": os.path.join(ROOT, "impact", "impact_engine.py"),
}


# ---- infra ------------------------------------------------------------------
def load_state():
    with open(STATE_PATH) as f:
        return json.load(f)


def save_state(s):
    s["_meta"]["last_updated"] = datetime.date.today().isoformat()
    with open(STATE_PATH, "w") as f:
        json.dump(s, f, indent=2)


def log(stage, msg, status="ok"):
    tag = "DRY" if DRY_RUN else "LIVE"
    print(f"[{tag}] {stage:<12} {status.upper():<6} {msg}")


def load_engine(key):
    """Import an engine module by file path; return None if missing."""
    path = ENGINES[key]
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(f"engine_{key}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def grade_of(fit, fresh):
    if fit >= 70 and fresh:
        return "A"
    if fit >= 70:
        return "B"
    if fit >= 50:
        return "C"
    return "D"


def mark_degraded(s, stage, reason):
    """Record that a stage could not produce real output. A degraded run is allowed to finish
    (best-effort, pre-access), but it must NOT look healthy: drafting is held to a test slice and
    the run status carries a DEGRADED flag. Silent partial success is the failure we're preventing."""
    s.setdefault("conductor", {}).setdefault("degraded_stages", [])
    s["conductor"]["degraded_stages"].append({"stage": stage, "reason": reason})


# ---- Stages -----------------------------------------------------------------
def stage_spec_reread(s):
    """GAP 3 — anti-drift (loop-engineering step 10 / 'goal drift over long sessions').
    State says where the engine IS; the standing spec says where it's GOING. Reread the spec every
    run so 'don't do X' constraints can't silently evaporate at turn 47 of a multi-week sequence.
    Detect spec changes by hash, log them, and re-assert the single in-scope motion (spec <-> WIP)."""
    ns = s.setdefault("north_star", {})
    digest = None
    if os.path.exists(SPEC_PATH):
        with open(SPEC_PATH, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()[:12]
    prev = ns.get("spec_hash")
    ns["spec_file"] = os.path.basename(SPEC_PATH)
    ns["spec_present"] = digest is not None
    if digest is None:
        log("0 Spec", f"governing spec {os.path.basename(SPEC_PATH)} NOT FOUND -> running on last-known constraints", "warn")
        mark_degraded(s, "0 Spec", "governing spec file missing")
    else:
        if prev and prev != digest:
            ns.setdefault("drift_log", []).insert(0, {"changed": datetime.date.today().isoformat(), "from": prev, "to": digest})
            ns["drift_log"] = ns["drift_log"][:8]
            log("0 Spec", f"spec CHANGED ({prev} -> {digest}) -> constraints re-read; review north_star before scaling", "warn")
        else:
            log("0 Spec", f"spec re-read ok ({digest}); {len(ns.get('immovable_constraints', []))} constraints anchored")
        ns["spec_hash"] = digest
        ns["last_reread"] = datetime.date.today().isoformat()
    # Re-assert: exactly one scaling motion is in scope this cycle (spec + WIP-of-one agree).
    scaling = [m for m, st in s.get("guardrails", {}).get("wip", {}).get("motions", {}).items() if st == "scaling"]
    ns["in_scope_motion"] = scaling[0] if len(scaling) == 1 else None
    if len(scaling) != 1:
        log("0 Spec", f"in-scope motion ambiguous ({scaling or 'none'}) -> critic will hold off-scope drafts", "warn")
    return s


def stage_refresh(s):
    # TODO(live): call enrichment/refresh agent on Clay rows with last_refreshed > 30d.
    log("1 Refresh", "re-enrich stale rows; update last_refreshed")
    return s


def stage_rescore(s):
    """Re-score accounts via the TAM engine; write grade distribution to state."""
    try:
        tam = load_engine("tam")
        if not tam:
            log("2 Re-score", "tam engine not found -> skipped (scoring degraded)", "skip")
            mark_degraded(s, "2 Re-score", "tam engine not found")
            return s
        plays = tam.build_plays(tam.load_cfg(), datetime.date.today())
        dist = {"A": 0, "B": 0, "C": 0, "D": 0}
        for p in plays:
            dist[grade_of(p.get("icp_total", 0), p.get("fresh", False))] += 1
        s["list_health"]["accounts_by_grade"] = dist
        s["list_health"]["accounts_total"] = len(plays)
        log("2 Re-score", f"{len(plays)} accounts graded  A:{dist['A']} B:{dist['B']} C:{dist['C']} D:{dist['D']}")
    except Exception as e:
        log("2 Re-score", f"engine error -> skipped ({e}) (scoring degraded)", "skip")
        mark_degraded(s, "2 Re-score", f"engine error: {e}")
    return s


def stage_scan_signals(s):
    """Scan signals via the signal engine; write top signals + counts to state."""
    try:
        sig = load_engine("signal")
        if not sig:
            log("3 Signals", "signal engine not found -> skipped (signals degraded)", "skip")
            mark_degraded(s, "3 Signals", "signal engine not found")
            return s
        results = sig.process()
        fired = [r for r in results if r.get("signals_fired", 0) > 0]
        top = sorted(fired, key=lambda r: -r["signals_fired"])[:5]
        s["signals"]["last_scan"] = datetime.datetime.now().isoformat(timespec="minutes")
        s["signals"]["tier1_active"] = sum(1 for r in fired if r.get("primary_routing", "").upper().startswith(("TIER1", "FIRE", "AE")))
        s["signals"]["top_signals"] = [
            {"company": r["company"], "signals_fired": r["signals_fired"], "route": r.get("primary_routing", "")}
            for r in top
        ]
        log("3 Signals", f"{len(results)} accounts scanned, {sum(r['signals_fired'] for r in fired)} signals firing across {len(fired)} accounts")
    except Exception as e:
        log("3 Signals", f"engine error -> skipped ({e}) (signals degraded)", "skip")
        mark_degraded(s, "3 Signals", f"engine error: {e}")
    return s


def stage_draft(s):
    # MEASUREMENT BEFORE VOLUME: if scoring or signals degraded this run, we have no trustworthy
    # targeting, so we must NOT draft at volume. Hold to a test slice and block volume explicitly.
    deg = {d["stage"] for d in s.get("conductor", {}).get("degraded_stages", [])}
    measurement_failed = bool(deg & {"2 Re-score", "3 Signals"})
    if measurement_failed:
        s["approval_queue"]["volume_blocked"] = True
        log("4 Draft", f"measurement degraded ({', '.join(sorted(deg & {'2 Re-score','3 Signals'}))}) "
                       f"-> TEST SLICE ONLY, volume blocked", "block")
    elif not s["baseline"]["ratified_with_naveen"]:
        s["approval_queue"]["volume_blocked"] = True
        log("4 Draft", "baseline not ratified -> drafting test slice only, volume blocked", "warn")
    else:
        s["approval_queue"]["volume_blocked"] = False
        log("4 Draft", "generate 3 variants/segment -> approval_queue (NO SEND)")
    # TODO(live): first-draft-engine -> copy-sharpener; honor volume_blocked (test slice vs full).
    return s


def stage_critic(s):
    """GAP 2 — independent maker/checker gate (loop-engineering steps 9 & 12).
    Runs BETWEEN draft and human approval. The agent that DRAFTS is not the agent that PASSES.
    OBJECTIVE checks only (deliverability, ICP/persona, in-scope motion, verified-claims, length) so it
    never becomes 'two optimists agreeing'. Held drafts never reach Dallas's queue -> shrinks the human
    bottleneck (serves throughput_by_operator). FAIL-CLOSED: a draft that can't be evaluated is HELD."""
    aq = s.setdefault("approval_queue", {})
    items = aq.get("items", [])
    ns = s.get("north_star", {})
    approved_claims = {a.lower() for a in ns.get("approved_claims", [])}
    max_len = ns.get("draft_max_chars", 600)
    in_scope = ns.get("in_scope_motion")  # set by stage_spec_reread; None => ambiguous
    checked = passed = held = 0
    held_items = []
    for it in items:
        if it.get("status") not in ("pending", "critic_held"):
            continue  # already resolved by a human; never re-judge a human decision
        checked += 1
        reasons = []
        draft = (it.get("draft") or "")
        if it.get("email_status") != "valid":
            reasons.append(f"email_status={it.get('email_status')!r} (not deliverable)")
        if (it.get("persona_match") or "").lower() in ("", "out"):
            reasons.append("persona_match Out/missing (outside ICP)")
        if not it.get("top_signal"):
            reasons.append("no firing signal")
        mk = "back_office" if "back" in (it.get("motion", "").lower()) else "star_ratings"
        if in_scope and mk != in_scope:
            reasons.append(f"motion '{it.get('motion')}' out of scope this cycle (in-scope: {in_scope})")
        flagged = []
        for pat in CLAIM_PATTERNS:
            for m in re.findall(pat, draft, flags=re.I):
                tok = m.strip()
                if tok and tok.lower() not in approved_claims:
                    flagged.append(tok)
        if flagged:
            reasons.append("unverified figure(s): " + ", ".join(sorted(set(flagged))) + " — verify vs intradiem-verified-metrics")
        if not draft.strip():
            reasons.append("empty draft")
        elif len(draft) > max_len:
            reasons.append(f"draft {len(draft)} chars > {max_len} cap")
        if reasons:
            it["critic_status"] = "held"
            it["critic_reasons"] = reasons
            it["status"] = "critic_held"
            held += 1
            held_items.append({"id": it.get("id"), "reasons": reasons})
        else:
            it["critic_status"] = "pass"
            it["critic_reasons"] = []
            if it.get("status") == "critic_held":
                it["status"] = "pending"  # a previously-held draft that now passes returns to the human queue
            passed += 1
    # TODO(live): augment this OBJECTIVE gate with a verifier SUBAGENT (different model/instructions,
    #   no exposure to the draft engine's reasoning) for subjective brand/voice. The hard gate stays
    #   objective above, so the loop never becomes the maker grading its own homework.
    aq["pending"] = sum(1 for it in items if it.get("status") == "pending")
    aq["critic_held"] = held
    s["critic"] = {
        "checked": checked, "passed": passed, "held": held,
        "held_rate": round(held / checked, 4) if checked else 0,
        "held_items": held_items,
        "last_run": datetime.datetime.now().isoformat(timespec="minutes"),
    }
    detail = f"{checked} drafted -> {passed} pass to human, {held} held (never reach human)"
    if held_items:
        detail += "; held: " + ", ".join(h["id"] for h in held_items)
    log("4b Critic", detail, "gate" if held else "ok")
    return s


def stage_approve(s):
    pending = s["approval_queue"]["pending"]
    log("5 Approve", f"{pending} item(s) awaiting human release in approval queue", "gate")
    log("5 Approve", "conductor STOPS here until Dallas approves/edits/rejects")
    return s


def stage_send(s):
    health = s["deliverability"]["overall_health"]
    if health != "green":
        log("6 Send", f"deliverability={health} -> SEND SKIPPED (premortem P1 guard)", "block")
        return s
    # ATTRIBUTION ASSERTION (live): never send an approved item that isn't stamped with a
    # known operator. A blank/unknown released_by silently corrupts the bottleneck share AND
    # the operator-test streak, so we refuse the whole batch rather than send unattributed.
    # Raising here is caught by run() -> FAIL-CLOSED: status=failed, nothing sends.
    if not DRY_RUN:
        valid = set()
        for o in s.get("guardrails", {}).get("throughput_by_operator", {}).get("operators", []):
            valid.add(o.get("name")); valid.add(o.get("id"))
        valid.discard(None)
        approved = [it for it in s["approval_queue"].get("items", []) if it.get("status") == "approved"]
        bad = [it for it in approved if it.get("released_by") not in valid]
        if bad:
            ids = ", ".join(it.get("id", "?") for it in bad)
            raise RuntimeError(
                f"SEND ABORTED (fail-closed): {len(bad)} approved item(s) [{ids}] have a blank or "
                f"unknown released_by. Every send must be attributed to a known operator "
                f"({sorted(v for v in valid if v)}). Fix released_by before any send.")
    # TODO(live): hand approved rows to Nate's sender.
    log("6 Send", "send approved rows only (all attributed)")
    return s


def compute_draft_quality(s):
    """GAP 1 — cost-per-accepted-change (loop-engineering step 11). Rolls approval_queue.resolved_ledger
    into the loop's real health metric: clean_accept (loop saved the work) vs edited_then_approved (a
    human had to rewrite -> the loop did NOT save that work) vs rejected (waste). acceptance_rate below
    the floor means the DRAFT ENGINE is the bottleneck, not the gate. Returns (rate, below_floor)."""
    aq = s.get("approval_queue", {})
    ledger = aq.get("resolved_ledger", [])
    dq = s.setdefault("draft_quality", {})
    floor = dq.get("floor", 0.5)
    norm = {"clean_accept": "clean_accept", "clean": "clean_accept",
            "edited": "edited_then_approved", "edited_then_approved": "edited_then_approved",
            "rejected": "rejected", "reject": "rejected"}

    def blank():
        return {"clean_accept": 0, "edited_then_approved": 0, "rejected": 0}

    def rate(d):
        res = d["clean_accept"] + d["edited_then_approved"] + d["rejected"]
        return round(d["clean_accept"] / res, 4) if res else None

    agg, by = blank(), {}
    for e in ledger:
        k = norm.get(e.get("outcome"))
        if not k:
            continue
        agg[k] += 1
        by.setdefault(e.get("variant_id", "?"), blank())[k] += 1

    resolved = sum(agg.values())
    ar = rate(agg)
    dq["floor"] = floor
    dq["clean_accept"] = agg["clean_accept"]
    dq["edited_then_approved"] = agg["edited_then_approved"]
    dq["rejected"] = agg["rejected"]
    dq["resolved"] = resolved
    dq["acceptance_rate"] = ar
    dq["below_floor"] = bool(ar is not None and ar < floor)
    dq["example"] = bool(ledger) and all(e.get("example") for e in ledger)
    dq["by_variant"] = {
        v: {**d, "resolved": d["clean_accept"] + d["edited_then_approved"] + d["rejected"],
            "acceptance_rate": rate(d), "below_floor": bool(rate(d) is not None and rate(d) < floor)}
        for v, d in by.items()
    }
    return ar, dq["below_floor"]


def stage_instrument(s):
    """Reply-sync (live) + refresh the impact scorecard from the impact engine."""
    # TODO(live): reply-sync agent updates funnel + reply_status (source-scoped).
    try:
        imp = load_engine("impact")
        if imp:
            d = imp.build()
            sources = d.get("sources", {})
            data_complete = d.get("data_complete", True)
            s["impact"] = {
                "opportunity_surfaced": d.get("headline_opportunity_label"),
                "strike_plans": d["net_new"].get("strike_plans"),
                "committee_contacts_mapped": d["net_new"].get("committee_contacts_mapped"),
                "sequence_messages_drafted": d["net_new"].get("sequence_messages_drafted"),
                "expansion_signals": d["install_base"].get("signals_firing"),
                "meetings_booked": d["realized"].get("meetings_booked"),
                "pipeline_created": d["realized"].get("pipeline_created_label"),
                "sources": sources,
                "data_complete": data_complete,
                "refreshed": datetime.date.today().isoformat(),
            }
            if not data_complete:
                missing = [k for k, v in sources.items() if not v]
                log("7 Instrument", f"impact inputs MISSING {missing} -> numbers are partial, not trustworthy", "block")
                mark_degraded(s, "7 Instrument", f"impact sources missing: {missing}")
            else:
                log("7 Instrument", f"impact refreshed: {s['impact']['opportunity_surfaced']} surfaced, {s['impact']['expansion_signals']} expansion signals")
        else:
            log("7 Instrument", "impact engine not found; reply-sync stub only", "skip")
            mark_degraded(s, "7 Instrument", "impact engine not found")
    except Exception as e:
        log("7 Instrument", f"impact engine error -> skipped ({e})", "skip")
        mark_degraded(s, "7 Instrument", f"impact engine error: {e}")
    log("7 Instrument", "reply-sync -> funnel, reply_status (gtm_engine_sourced only)")
    # Experiment loop: pick the winning variant per segment by qualified-reply rate.
    exp = s.get("experiments", {})
    vs = exp.get("active_variants", [])
    min_n = exp.get("min_sample", 40)
    if vs:
        by_seg = {}
        for v in vs:
            v["qr_rate"] = round(v["qualified_replies"] / v["sent"], 4) if v.get("sent") else 0
            by_seg.setdefault(v["segment"], []).append(v)
        winners = []
        for seg, group in by_seg.items():
            eligible = [v for v in group if v.get("sent", 0) >= min_n]
            for v in group:
                v["status"] = "testing"  # reset, recompute below
            if eligible:
                best = max(eligible, key=lambda v: v["qr_rate"])
                best["status"] = "winner"
                winners.append(f"{best['variant_id']} ({best['qr_rate']*100:.1f}% QR)")
                for v in eligible:
                    if v is not best and v["qr_rate"] * 2 < best["qr_rate"]:
                        v["status"] = "retire"
            else:
                for v in group:
                    v["status"] = "under_sample"
        exp["winning_variant"] = winners[0] if len(winners) == 1 else (winners or None)
        log("7 Experiments", f"winners: {', '.join(winners) if winners else 'none yet (under min sample)'}")
    # GAP 1 — recompute the loop's real health metric: cost per accepted change.
    ar, below = compute_draft_quality(s)
    if ar is None:
        log("7 Draft-quality", "no resolved drafts yet -> acceptance rate not yet measurable")
    elif below:
        log("7 Draft-quality", f"ACCEPTANCE {ar*100:.0f}% < floor {s['draft_quality']['floor']*100:.0f}% -> "
                               f"the DRAFT ENGINE is the bottleneck (you're re-doing work the loop should save), not the gate", "warn")
    else:
        log("7 Draft-quality", f"acceptance {ar*100:.0f}% (>= floor {s['draft_quality']['floor']*100:.0f}%); "
                               f"{s['draft_quality']['clean_accept']} clean / {s['draft_quality']['edited_then_approved']} edited / {s['draft_quality']['rejected']} rejected")
    return s


def _owner_releases(ops, ot):
    """Sum the OWNER's releases, identifying the owner by the stable is_owner flag.
    Returns (owner_release_count, integrity_error_or_None).
    NEVER match the owner by display-name string: in production released_by may be an
    email/SSO name, and a missed string-match would silently count the owner's releases as
    'team' -> the bottleneck alarm would never fire. So: flag first, fail loud otherwise."""
    flagged = [o for o in ops if o.get("is_owner") is True]
    if len(flagged) == 1:
        return sum(o.get("released_this_week", 0) for o in flagged), None
    if len(flagged) > 1:
        return (sum(o.get("released_this_week", 0) for o in flagged),
                f"{len(flagged)} operators flagged is_owner=true; exactly one is required")
    # No flag set — fall back to id/name match but flag it as a config gap (do not trust silently).
    oid, oname = ot.get("owner_id"), ot.get("owner_name")
    match = [o for o in ops if (oid and o.get("id") == oid) or (oname and o.get("name") == oname)]
    if match:
        return (sum(o.get("released_this_week", 0) for o in match),
                "owner identified by id/name fallback — set is_owner=true on exactly one operator record")
    return 0, "OWNER NOT IDENTIFIABLE — no operator has is_owner=true and owner_id/owner_name match nothing"


def roll_weekly_window(s):
    """LIVE-ONLY weekly reset of operator throughput (premortem F1 integrity).
    Without this, released_this_week accumulates forever and 'share this week' silently
    becomes 'share all-time'. Snapshots the closing week to last_week, then zeroes counters.
    Skipped in DRY_RUN so the seeded demo scenario stays stable. Does NOT touch operator-test
    streaks (those are multi-week by design)."""
    if DRY_RUN:
        return s
    tp = s.get("guardrails", {}).get("throughput_by_operator")
    if not tp:
        return s
    today = datetime.date.today()
    ws = tp.get("window_start")
    start = None
    if ws:
        try:
            start = datetime.date.fromisoformat(ws)
        except Exception:
            start = None
    if start is None or (today - start).days >= 7:
        tp["last_week"] = {
            "window_start": ws,
            "window_end": today.isoformat(),
            "operators": [{"name": o.get("name"), "released": o.get("released_this_week", 0)} for o in tp.get("operators", [])],
            "total": tp.get("total_released_this_week", 0),
            "dallas_share": tp.get("dallas_share", 0.0),
            "alarm": tp.get("alarm", False),
        }
        for o in tp.get("operators", []):
            o["released_this_week"] = 0
        tp["total_released_this_week"] = 0
        tp["dallas_share"] = 0.0
        tp["alarm"] = False
        tp["window_start"] = today.isoformat()
        log("0 Window", f"weekly throughput window rolled; new week starts {today.isoformat()}")
    return s


def check_security(s):
    """GAP 4 — security tax (loop-engineering step 14). An unattended loop is an unattended attack
    surface. Enforced as a CADENCE, not memory: warn loudly when the permission audit is overdue or
    log sanitization is off. This SURFACES in dry-run (warning) but preflight makes it a go-live FAIL,
    so you can't run live volume on stale permissions."""
    sec = s.get("security")
    if not sec:
        return s
    interval = sec.get("audit_interval_days", 30)
    last = sec.get("last_permission_audit")
    due_in, overdue = None, True
    if last:
        try:
            elapsed = (datetime.date.today() - datetime.date.fromisoformat(last)).days
            due_in, overdue = interval - elapsed, elapsed >= interval
        except Exception:
            overdue = True
    sec["audit_overdue"] = overdue
    sec["days_until_audit"] = due_in
    if overdue:
        log("0 Security", f"PERMISSION RE-AUDIT OVERDUE (last={last or 'never'}, every {interval}d): re-check "
                          f"connector scopes, log sanitization, and skill sources before live volume.", "warn")
    else:
        log("0 Security", f"permissions audited {last}; next due in {due_in}d")
    if not sec.get("log_sanitization_enabled", False):
        log("0 Security", "log sanitization OFF -> secrets/PII can scatter into unmonitored logs (step 14). Enable before live.", "warn")
    return s


def check_wip(s):
    """Anti-sprawl gate (premortem Failure #3). Runs BEFORE the motion.
    At most scaling_limit motions may be 'scaling'; everything else waits in backlog."""
    g = s.get("guardrails", {})
    wip = g.get("wip")
    if not wip:
        return s
    scaling = [m for m, st in wip.get("motions", {}).items() if st == "scaling"]
    limit = wip.get("scaling_limit", 1)
    wip["violation"] = len(scaling) > limit
    if wip["violation"]:
        log("0 WIP", f"VIOLATION: {len(scaling)} motions scaling ({', '.join(scaling)}); limit is {limit}. "
                     f"Park all but one in backlog before building.", "block")
    else:
        log("0 WIP", f"{len(scaling)}/{limit} motion scaling ({scaling[0] if scaling else 'none'}); rest in backlog", "gate")
    return s


def stage_guardrails(s):
    """Premortem tripwires, recomputed from state every run so the dashboards never drift.
    (1) throughput-by-operator: is Dallas the bottleneck?  (2) operator-test: has the team
    run it unaided long enough to call it overhauled?  (3) WIP-of-one re-check."""
    g = s.get("guardrails")
    if not g:
        log("8 Guardrails", "no guardrails block -> skipped", "skip")
        return s

    # (1) Throughput by operator — Dallas-bottleneck alarm (premortem F1).
    #     INTEGRITY: identify the owner by the is_owner FLAG, never by display-name string.
    #     A name-string match fails open (owner's releases miscounted as team -> alarm never fires).
    tp = g.get("throughput_by_operator", {})
    ot = g.get("operator_test", {})
    ops = tp.get("operators", [])
    total = sum(o.get("released_this_week", 0) for o in ops)
    owner_dallas, integ = _owner_releases(ops, ot)
    ceiling = tp.get("dallas_share_ceiling", 0.2)
    tp["total_released_this_week"] = total
    tp["dallas_share"] = round(owner_dallas / total, 4) if total else 0.0
    tp["integrity_error"] = integ
    tp["alarm"] = bool(total and tp["dallas_share"] > ceiling) or bool(integ)
    if integ:
        # Can't trust who released -> fail LOUD and conservative (assume bottleneck), never silent.
        log("8 Guardrails", f"INTEGRITY ERROR: {integ} -> alarm forced on (do not scale).", "block")
    elif tp["alarm"]:
        log("8 Guardrails", f"BOTTLENECK ALARM: Dallas released {tp['dallas_share']*100:.0f}% of batches "
                            f"(ceiling {ceiling*100:.0f}%). Operable-by-Dallas, not the team — fix before scaling.", "block")
    else:
        log("8 Guardrails", f"operator throughput ok: Dallas {tp['dallas_share']*100:.0f}% of {total} releases "
                            f"(ceiling {ceiling*100:.0f}%)")

    # (2) Operator-test — is the motion operable by the team yet? (premortem F1 definition of done)
    ot = g.get("operator_test", {})
    need = ot.get("required_team_releases", 2)
    for motion, rec in ot.get("by_motion", {}).items():
        streak = rec.get("consecutive_team_releases", 0)
        rec["status"] = "operable" if streak >= need else "not_yet_operable"
        log("8 Guardrails", f"operator-test [{motion}]: {streak}/{need} unaided team releases -> {rec['status']}")

    # (3) WIP-of-one — keep violation flag consistent at end of run too (premortem F3).
    wip = g.get("wip", {})
    scaling = [m for m, st in wip.get("motions", {}).items() if st == "scaling"]
    wip["violation"] = len(scaling) > wip.get("scaling_limit", 1)
    return s


STAGES = [stage_spec_reread, stage_refresh, stage_rescore, stage_scan_signals,
          stage_draft, stage_critic, stage_approve, stage_send, stage_instrument, stage_guardrails]


def _check_tam():
    try:
        tam = load_engine("tam")
        if not tam:
            return ("tam_contract", False, "tam engine module not found")
        plays = tam.build_plays(tam.load_cfg(), datetime.date.today())
        if not plays:
            return ("tam_contract", False, "build_plays returned empty")
        missing = {"icp_total", "fresh"} - set(plays[0].keys())
        return ("tam_contract", not missing,
                "scoring contract intact" if not missing else f"missing keys {missing}")
    except Exception as e:
        return ("tam_contract", False, f"error: {e}")


def _check_signal():
    try:
        sig = load_engine("signal")
        if not sig:
            return ("signal_contract", False, "signal engine module not found")
        res = sig.process()
        if not res:
            return ("signal_contract", False, "process() returned empty")
        missing = {"company", "signals_fired", "primary_routing"} - set(res[0].keys())
        return ("signal_contract", not missing,
                "signal contract intact" if not missing else f"missing keys {missing}")
    except Exception as e:
        return ("signal_contract", False, f"error: {e}")


def _check_impact():
    try:
        imp = load_engine("impact")
        if not imp:
            return ("impact_contract", False, "impact engine module not found")
        d = imp.build()
        missing = {"net_new", "install_base", "realized", "data_complete"} - set(d.keys())
        if missing:
            return ("impact_contract", False, f"missing keys {missing}")
        if not d.get("data_complete"):
            absent = [k for k, v in d.get("sources", {}).items() if not v]
            return ("impact_contract", False, f"upstream inputs missing: {absent}")
        return ("impact_contract", True, "impact contract intact, all sources present")
    except Exception as e:
        return ("impact_contract", False, f"error: {e}")


def preflight(s):
    """Day-one go-live gate. Runs every assertion the live motion depends on and returns
    (ready, checks). ready=True only if ALL checks pass. run() refuses to operate in live mode
    (DRY_RUN=False) unless this returns ready — you cannot flip to live on a portfolio that
    would fail silently. `python conductor.py --preflight` prints the full report and exits
    nonzero if not ready."""
    checks = []

    def chk(name, ok, detail):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})

    g = s.get("guardrails", {})

    chk("state_structure",
        bool(g.get("operator_test") and g.get("throughput_by_operator") and g.get("wip")),
        "guardrails block (operator_test / throughput / wip) present")

    _, integ = _owner_releases(g.get("throughput_by_operator", {}).get("operators", []),
                               g.get("operator_test", {}))
    chk("owner_identity", integ is None, integ or "exactly one operator flagged is_owner=true")

    ac = s.get("attribution_contract", {})
    fl = ac.get("fields_live_in_salesforce", {})
    chk("attribution_ratified",
        bool(s.get("baseline", {}).get("ratified_with_naveen") and ac.get("ratified_in_writing")
             and fl and all(fl.values())),
        "baseline ratified + attribution ratified in writing + 3 Salesforce fields live")

    b = s.get("baseline", {})
    t = s.get("funnel", {}).get("targets", {})
    chk("baseline_set",
        bool(b.get("one_x_qualified_replies_per_week") and t.get("qualified_replies_per_week_10x")),
        "1x baseline + 10x target are numeric (not null) so throughput is measurable")

    chk("deliverability_green",
        s.get("deliverability", {}).get("overall_health") == "green",
        "deliverability.overall_health == green (premortem P1 send gate)")

    for fn in (_check_tam, _check_signal, _check_impact):
        chk(*fn())

    wip = g.get("wip", {})
    scaling = [m for m, st in wip.get("motions", {}).items() if st == "scaling"]
    chk("wip_sane", len(scaling) <= wip.get("scaling_limit", 1),
        f"{len(scaling)}/{wip.get('scaling_limit', 1)} motions scaling (anti-sprawl)")

    valid = set()
    for o in g.get("throughput_by_operator", {}).get("operators", []):
        valid.add(o.get("name")); valid.add(o.get("id"))
    valid.discard(None)
    approved = [it for it in s.get("approval_queue", {}).get("items", []) if it.get("status") == "approved"]
    bad = [it.get("id") for it in approved if it.get("released_by") not in valid]
    chk("approval_attribution", bool(valid) and not bad,
        "operator vocab set and every approved item attributed"
        if (valid and not bad) else f"vocab_empty={not valid}, unattributed={bad}")

    # GAP 4 — security tax: a stale permission audit or disabled log-sanitization is a go-live blocker.
    sec = s.get("security", {})
    last = sec.get("last_permission_audit")
    audit_current = False
    if last:
        try:
            audit_current = (datetime.date.today() - datetime.date.fromisoformat(last)).days < sec.get("audit_interval_days", 30)
        except Exception:
            audit_current = False
    scopes_reviewed = all(c.get("least_privilege_reviewed") for c in sec.get("connector_scopes", [])) if sec.get("connector_scopes") else False
    chk("security_audit_current",
        audit_current and sec.get("log_sanitization_enabled", False) and scopes_reviewed,
        "permission audit within interval + log sanitization on + all connector scopes least-privilege reviewed (step 14)")

    # GAP 3 — the governing spec must be present so the loop can re-anchor each run (anti-drift).
    chk("spec_present", os.path.exists(SPEC_PATH),
        f"governing spec {os.path.basename(SPEC_PATH)} present for per-run reread")

    return all(c["ok"] for c in checks), checks


def print_preflight():
    s = load_state()
    ready, checks = preflight(s)
    print("\n=== CONDUCTOR PREFLIGHT — go-live readiness gate ===")
    for c in checks:
        print(f"  [{'PASS' if c['ok'] else 'FAIL'}] {c['name']:<22} {c['detail']}")
    print("-" * 64)
    if ready:
        print("VERDICT: READY — all checks pass. Safe to set DRY_RUN=False.")
    else:
        fails = [c["name"] for c in checks if not c["ok"]]
        print(f"VERDICT: NOT READY — {len(fails)} blocker(s): {', '.join(fails)}.")
        print("Fix every FAIL before flipping DRY_RUN=False. Live runs are blocked until then.")
    return ready


def run():
    # LIVE GATE: never operate live on a portfolio that would fail silently.
    if not DRY_RUN:
        ready, checks = preflight(load_state())
        if not ready:
            print("\n=== LIVE RUN BLOCKED — preflight failed (fail-closed) ===")
            for c in checks:
                if not c["ok"]:
                    print(f"  [FAIL] {c['name']:<22} {c['detail']}")
            print("Refusing to run live until all checks pass. "
                  "Run `python conductor.py --preflight` for the full report.\n")
            return
    s = load_state()
    started = datetime.datetime.now().isoformat(timespec="seconds")
    print(f"\n=== Weekly Conductor run @ {started}  (DRY_RUN={DRY_RUN}) ===")
    s.setdefault("conductor", {})["degraded_stages"] = []  # reset per run; populated by mark_degraded
    s = roll_weekly_window(s)  # live-only: reset weekly throughput window before counting
    s = check_security(s)      # gap 4: surface overdue permission audit / log-sanitization before the motion
    s = check_wip(s)           # anti-sprawl gate fires before the motion runs
    completed = []
    try:
        for fn in STAGES:
            s = fn(s)
            completed.append(fn.__name__)
    except Exception:  # FAIL-CLOSED on anything unexpected outside a stage's own guard
        log("ABORT", traceback.format_exc().splitlines()[-1], "error")
        s["conductor"]["last_run_status"] = "failed"
    else:
        base = "completed (dry-run)" if DRY_RUN else "completed"
        deg = s.get("conductor", {}).get("degraded_stages", [])
        if deg:
            base += f" — DEGRADED ({len(deg)}: {', '.join(d['stage'] for d in deg)})"
            log("STATUS", "run finished DEGRADED — outputs are partial; do not treat as healthy", "warn")
        s["conductor"]["last_run_status"] = base
    s["conductor"]["last_run"] = started
    s["conductor"].setdefault("runs", []).insert(0, {
        "started": started, "status": s["conductor"]["last_run_status"],
        "stages_completed": completed, "dry_run": DRY_RUN,
    })
    s["conductor"]["runs"] = s["conductor"]["runs"][:12]
    save_state(s)
    print(f"=== done: {s['conductor']['last_run_status']} ===\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Weekly GTM Conductor")
    ap.add_argument("--preflight", action="store_true",
                    help="run go-live readiness checks and exit (nonzero if not ready)")
    args = ap.parse_args()
    if args.preflight:
        raise SystemExit(0 if print_preflight() else 1)
    run()
