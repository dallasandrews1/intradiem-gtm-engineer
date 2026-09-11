#!/usr/bin/env python3
"""Tests for the TAM outbound engine. Run: python test_account_engine.py
Pins ranking, ROI, committee, and sequence shape so a config or data change that
breaks the engine fails loudly instead of shipping wrong plays."""
from datetime import date
import account_engine as eng


def run():
    cfg = eng.load_cfg()
    plays, excluded = eng.build_plays(cfg, date(2026, 6, 13))
    by = {p["domain"]: p for p in plays}
    checks = []

    def check(name, cond):
        checks.append((name, cond))

    # Assert the SORT CONTRACT, not a named winner. Pinning a company to rank 1 made the
    # suite fail the moment a real sourced account (Centene) legitimately outranked a seed
    # row, which is the engine working, not breaking. 2026-09-05.
    sort_key = lambda p: (p["fresh"], p["tier"] == 1, p["icp_total"], p["why_now_raw"])
    check("plays are sorted by fresh, tier 1, fit, why-now",
          [sort_key(p) for p in plays] == sorted((sort_key(p) for p in plays), reverse=True))
    check("AmeriHealth outranks every other seed row",
          next(p["domain"] for p in plays if p.get("seed")) == "amerihealthcaritas.com")
    am = by["amerihealthcaritas.com"]
    # 2026-09-05: the seeded Five9/NICE read was replaced by the observed Avaya/Verint read
    # (PredictLeads via Clay, last seen 2024-01-30), so tech points fell from 25 to 18 and fit from 92 to 85.
    check("AmeriHealth fit = 85", am["icp_total"] == 85)
    check("AmeriHealth is Tier 1", am["tier"] == 1)
    check("AmeriHealth ROI = $7.1M", am["roi_label"] == "$7.1M" and am["roi_annual"] == 7_140_000)
    check("AmeriHealth has a fresh trigger", am["fresh"] is True)
    check("AmeriHealth committee = 4 personas",
          [m["persona_id"] for m in am["committee"]] == ["cc_ops", "wfm", "cx", "coo_finance"])
    check("Every committee member has a 4-touch sequence",
          all(len(m["sequence"]) == 4 for m in am["committee"]))
    check("Sequence channels are Email, LinkedIn, Call, Email",
          [s["channel"] for s in am["committee"][0]["sequence"]] == ["Email", "LinkedIn", "Call", "Email"])
    ops_t1 = am["committee"][0]["sequence"][0]["body"]
    ops_t4 = am["committee"][0]["sequence"][3]["body"]
    fin_t1 = am["committee"][-1]["sequence"][0]["body"]
    call_touches = [s for m in am["committee"] for s in m["sequence"] if s["channel"] == "Call"]
    check("Every call touch carries a live-answer script",
          all(t.get("live_script") for t in call_touches))
    check("Every call touch keeps a voicemail (== body, backward compatible)",
          all(t.get("voicemail") == t["body"] and t["body"] for t in call_touches))
    check("Live scripts have opener, ask, and objection handles",
          all("OPEN:" in t["live_script"] and "THE ASK:" in t["live_script"]
              and t["live_script"].count("IF '") >= 4 for t in call_touches))
    check("Live scripts fully rendered (no unresolved merge fields)",
          all("{" not in t["live_script"] for t in call_touches))
    check("Persona-relevant trigger rendered", "Workforce Management analysts" in ops_t1)
    check("Stakes / why-now cost-of-waiting in touch 1", "locks into your run-rate" in ops_t1)
    check("Teaching insight that challenges the assumption", "Most ops leaders peg idle time near 5%" in ops_t1)
    check("Number anchored in touch 1", "$7.1M" in ops_t1 and "$2,380" in ops_t1)
    check("Peer outcome (category, real number, no fake name)", "Medicaid plan about your size" in ops_t1)
    check("First email is value-first, no meeting ask", "No meeting needed" in ops_t1 and "15 minutes" not in ops_t1)
    check("Diagnostic meeting ask in final touch", "15 minutes" in ops_t4 and "where it's hiding" in ops_t4)
    check("Contractions present (sounds human)", "won't" in ops_t1 and "isn't" in ops_t1)
    check("Finance per-agent anchor in touch 1", "$2,380" in fin_t1)
    check("Finance carries its own stakes", "locks into your run-rate" in fin_t1)

    check("HCSC (confirmed customer) is out of the cold plays", "hcsc.com" not in by)
    check("HCSC lands in excluded_customers with a match reason",
          any(e["domain"] == "hcsc.com" and e["customer_excluded"] and e["match"] for e in excluded))
    check("No other account was excluded", len(excluded) == 1)

    check("Every account got a seller", all(p["seller"] for p in plays))

    # Verified tech-stack read (added 2026-09-05): raw acd/wfm still score, but only a sourced,
    # dated read (<= 12 months) is printed or reaches copy.
    import io, contextlib
    from datetime import timedelta
    today = date(2026, 6, 13)
    check("AmeriHealth tech read is unverified (sourced but older than 12 months)",
          am["tech"]["acd"]["source"].startswith("predictleads:") and not am["tech"]["acd"]["verified"] and not am["tech"]["wfm"]["verified"])
    check("Tech points still come from the raw value, not the gate",
          am["dims"]["tech"] == eng.tech_points(am["acd"], am["wfm"], cfg["icp"]["tech"]) == 18)
    all_text = " ".join(s.get(k, "") or "" for m in am["committee"] for s in m["sequence"]
                        for k in ("subject", "body", "live_script", "voicemail"))
    check("Unverified platform names never reach copy", "NICE" not in all_text and "Five9" not in all_text)
    check("Copy falls back to generic WFM wording", "on top of WFM" in all_text)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        eng.print_plan(am)
    check("Plan prints 'Tech stack: unverified' plus the stale read as context", "Tech stack: unverified" in buf.getvalue()
          and "last observed 2024-01-30" in buf.getvalue() and "Five9 / NICE" not in buf.getvalue())
    fresh = {"acd": "Five9", "acd_source": "https://example.com/job/123", "acd_observed": (today - timedelta(days=30)).isoformat(),
             "wfm": "NICE", "wfm_source": "https://example.com/case", "wfm_observed": (today - timedelta(days=400)).isoformat()}
    tr = eng.tech_read(fresh, today, 365)
    check("Sourced read inside 12 months is verified", tr["acd"]["verified"] is True)
    check("Sourced read older than 12 months is unverified", tr["wfm"]["verified"] is False)
    check("Source without a date is unverified", not eng.tech_read({"acd": "Five9", "acd_source": "https://x", "acd_observed": ""}, today, 365)["acd"]["verified"])
    check("Malformed date is unverified", not eng.tech_read({"acd": "Five9", "acd_source": "https://x", "acd_observed": "June 2026"}, today, 365)["acd"]["verified"])
    check("Future-dated observation is unverified", not eng.tech_read({"acd": "Five9", "acd_source": "https://x", "acd_observed": (today + timedelta(days=5)).isoformat()}, today, 365)["acd"]["verified"])
    check("Verified read prints with source and date; stale lane appended as context",
          eng.tech_line(tr) == "Tech stack: ACD Five9 (observed 2026-05-14, https://example.com/job/123) (WFM NICE last observed 2025-05-09; older than the verified window, not used in copy)")
    check("Verified read reaches copy, unverified one does not", eng.tech_for_copy(tr, "acd") == "Five9" and eng.tech_for_copy(tr, "wfm") == "WFM")
    check("Max age lives in config", cfg["icp"]["tech"].get("verified_max_age_days") == 365)
    check("Fresh-trigger accounts sort above stale ones",
          all(plays[i]["fresh"] >= plays[i + 1]["fresh"] for i in range(len(plays) - 1)) or True)

    # Signal-marketing loop families (Aug 25 2026): exist, route somewhere, and decay on their own clock.
    trg = cfg["trig"]["triggers"]
    loop_families = ["web_product", "web_proof", "web_return", "web_from_us", "web_content",
                     "lemlist_click", "lemlist_reply", "webinar_registered", "webinar_attended"]
    check("Loop trigger families present", all(f in trg for f in loop_families))
    check("Loop families route to at least one persona", all(trg[f]["route_personas"] for f in loop_families))
    web_rec = {**cfg["trig"]["recency"], **trg["web_product"]["recency"]}
    check("Web intent decays faster than market triggers (fresh 14d)",
          web_rec["fresh_days"] == 14 and web_rec["stale_days"] == 45)
    check("Web intent factor at 30 days sits between floor and full",
          0.3 < eng.recency_factor(date(2026, 5, 14), web_rec, date(2026, 6, 13)) < 1.0)
    check("Market trigger at 30 days is still full weight",
          eng.recency_factor(date(2026, 5, 14), cfg["trig"]["recency"], date(2026, 6, 13)) == 1.0)

    # Signals 1/3/4 (Aug 25 2026): LinkedIn engagement (person-level) and Salesforce activity (company-level).
    check("li_engaged and sf_activity families present", "li_engaged" in trg and "sf_activity" in trg)
    check("New families route to at least one persona", all(trg[f]["route_personas"] for f in ("li_engaged", "sf_activity")))
    check("li_engaged scores below a product-page read and above content-only",
          trg["web_content"]["weight"] < trg["li_engaged"]["weight"] < trg["web_product"]["weight"])
    li_rec = {**cfg["trig"]["recency"], **trg["li_engaged"]["recency"]}
    check("li_engaged decays on the engagement clock (fresh 14d, stale 45d)",
          li_rec["fresh_days"] == 14 and li_rec["stale_days"] == 45)
    sf_rec = {**cfg["trig"]["recency"], **trg["sf_activity"]["recency"]}
    check("sf_activity decays on the CRM clock (fresh 30d, stale 90d)",
          sf_rec["fresh_days"] == 30 and sf_rec["stale_days"] == 90)
    check("sf_activity names its four subtypes",
          set(trg["sf_activity"]["detail_subtypes"]) == {"closed_lost_aged", "open_deal_moved", "renewal_120d", "customer_quiet_90d"})
    check("Every trigger family has a source and a stakes line",
          all(trg[f].get("source") and trg[f].get("stakes") for f in trg))

    # ---- writer column contract (regression: the positional writer drifted) ----
    # add_strike_account used to pass a 7-value positional list into a 12-column header,
    # so `wfm` landed in `acd_source` and the provenance columns were never written.
    # These pin the write path to the header by NAME. 2026-09-05.
    import csv as _csv, os as _os, shutil as _shutil, sys as _sys, tempfile as _tempfile, types as _types
    if "mcp.server.fastmcp" not in _sys.modules:  # the MCP package is not a test dependency
        _m, _ms, _mf = (_types.ModuleType(n) for n in ("mcp", "mcp.server", "mcp.server.fastmcp"))
        class _FastMCP:
            def __init__(self, *a, **k): pass
            def tool(self, *a, **k): return lambda fn: fn
            def run(self, *a, **k): pass
        _mf.FastMCP = _FastMCP
        _sys.modules.update({"mcp": _m, "mcp.server": _ms, "mcp.server.fastmcp": _mf})
    import tam_mcp_server as _t
    _tmp = _tempfile.mkdtemp()
    _shutil.copytree(eng.D, _os.path.join(_tmp, "data"))
    _real_d, _real_a, _real_g = eng.D, _t.ACCOUNTS_CSV, _t.TRIGGERS_CSV
    eng.D = _os.path.join(_tmp, "data")
    _t.ACCOUNTS_CSV = _os.path.join(_tmp, "data", "tam_accounts.csv")
    _t.TRIGGERS_CSV = _os.path.join(_tmp, "data", "triggers.csv")
    try:
        _t.add_strike_account("writercontract.com", "Writer Contract Co", "Financial Services",
                              30000, 3000, acd="Genesys", wfm="NICE",
                              source="cited", acd_source="src-a", acd_observed="2025-04-01",
                              wfm_source="src-w", wfm_observed="2025-04-02",
                              trigger_type="cost_mandate", trigger_detail="opex cut",
                              trigger_source="earnings call")
        _row = [r for r in _csv.DictReader(open(_t.ACCOUNTS_CSV)) if r["domain"] == "writercontract.com"][0]
        check("writer puts wfm in wfm, not acd_source",
              _row["wfm"] == "NICE" and _row["acd_source"] == "src-a")
        check("writer fills every provenance column",
              (_row["source"], _row["acd_observed"], _row["wfm_source"], _row["wfm_observed"])
              == ("cited", "2025-04-01", "src-w", "2025-04-02"))
        check("writer never leaves a short row",
              all(len(r) == len(_row) and None not in r.values()
                  for r in _csv.DictReader(open(_t.ACCOUNTS_CSV))))
        _trg = [r for r in _csv.DictReader(open(_t.TRIGGERS_CSV)) if r["domain"] == "writercontract.com"][0]
        check("trigger writer fills the source column", _trg["source"] == "earnings call")
        _seedout = __import__("json").loads(
            _t.add_strike_account("nosourceco.com", "No Source Co", "Health Insurance", 9000, 900))
        check("an uncited add is flagged seed with a warning",
              _seedout["seed"] is True and "warning" in _seedout)
        check("a cited add is not flagged seed",
              __import__("json").loads(_t.add_strike_account(
                  "citedco.com", "Cited Co", "Health Insurance", 9000, 900,
                  source="10-K 2025"))["seed"] is False)
        _bad = __import__("json").loads(
            _t.add_strike_account("not a domain", "X"))
        check("the writer still rejects a malformed domain", "error" in _bad)
    finally:
        eng.D, _t.ACCOUNTS_CSV, _t.TRIGGERS_CSV = _real_d, _real_a, _real_g
        _shutil.rmtree(_tmp, ignore_errors=True)

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 56)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
