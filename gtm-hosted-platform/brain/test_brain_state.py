#!/usr/bin/env python3
"""Tests for the brain's snapshot contract. Run: python3 test_brain_state.py

Pins the three properties the 2026-09-05 rewrite exists to guarantee:
  1. the brain never serves a figure without saying how old it is,
  2. past the age threshold, and on any uncited row, figures are WITHHELD, not served,
  3. with no snapshot the brain returns nothing rather than something bundled and old.

The web layer is stubbed: fastapi/starlette/mcp are not installable in every environment
and none of them are what broke. Everything under test here is the freshness and redaction
logic in gtm_state.py plus the endpoint helpers in app.py.
"""
import datetime
import json
import os
import sys
import tempfile
import types

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _stub_web_layer():
    if "fastapi" in sys.modules:
        return

    class HTTPException(Exception):
        def __init__(self, status_code, detail=None):
            super().__init__(f"{status_code}: {detail}")
            self.status_code, self.detail = status_code, detail

    def Header(default=""):
        return default

    class FastAPI:
        def __init__(self, *a, **k): pass
        def _deco(self, *a, **k): return lambda fn: fn
        get = post = _deco
        def mount(self, *a, **k): pass

    fa = types.ModuleType("fastapi")
    fa.FastAPI, fa.Header, fa.HTTPException = FastAPI, Header, HTTPException

    class BaseHTTPMiddleware:
        def __init__(self, *a, **k): pass

    sm = types.ModuleType("starlette.middleware.base"); sm.BaseHTTPMiddleware = BaseHTTPMiddleware
    sr = types.ModuleType("starlette.responses")
    sr.JSONResponse = lambda *a, **k: None

    class FastMCP:
        def __init__(self, *a, **k): self.session_manager = None
        def tool(self, *a, **k): return lambda fn: fn
        def streamable_http_app(self):
            class _A:
                def add_middleware(self, *a, **k): pass
            return _A()

    mf = types.ModuleType("mcp.server.fastmcp"); mf.FastMCP = FastMCP
    sys.modules.update({
        "fastapi": fa,
        "starlette": types.ModuleType("starlette"),
        "starlette.middleware": types.ModuleType("starlette.middleware"),
        "starlette.middleware.base": sm,
        "starlette.responses": sr,
        "mcp": types.ModuleType("mcp"),
        "mcp.server": types.ModuleType("mcp.server"),
        "mcp.server.fastmcp": mf,
    })
    return HTTPException


_stub_web_layer()
import gtm_state          # noqa: E402
import app as brain       # noqa: E402
from fastapi import HTTPException  # noqa: E402


def snapshot(age_hours=1.0, seed_second=True):
    gen = gtm_state.utcnow() - datetime.timedelta(hours=age_hours)
    def acct(dom, seed):
        return {"company": dom.split(".")[0].title(), "domain": dom, "industry": "Health Insurance",
                "icp_total": 88, "tier": 1, "dims": {"industry": 25}, "fresh": True,
                "why_now_raw": 25, "agent_count": 10000, "roi_annual": 23800000,
                "roi_label": "$23.8M", "roi_per_agent": 2380, "roi_per_agent_label": "$2,380",
                "acd": "Genesys", "wfm": "Verint", "tech": {},
                "triggers": [
                    {"label": "cost mandate", "type": "cost_mandate", "detail": "d", "play": "p",
                     "stakes": "s", "source": "Q2 2026 earnings call"},
                    {"label": "won contracts", "type": "cc_expansion", "detail": "invented",
                     "play": "p", "stakes": "s", "source": ""}],
                "committee": [{"persona_id": "coo", "sequence": [{"day": 1, "body": "copy"}]}],
                "seller": "Nate", "seller_email": "n@x.com",
                "source": "" if seed else "10-K 2025", "seed": seed}
    return {
        "schema_version": gtm_state.SCHEMA_VERSION,
        "generated_at": gtm_state.iso(gen),
        "engines": {
            "strike": {"data_source": "mixed",
                       "accounts": [acct("cited.com", False), acct("seedco.com", seed_second)],
                       "excluded": [{"company": "HCSC", "domain": "hcsc.com",
                                     "customer_excluded": True, "match": "denylist"}],
                       "counts": {"accounts": 2, "seed": 1, "customer_excluded": 1}},
            "signals": {"data_source": "mock",
                        "accounts": [{"company": "Sync", "domain": "sync.com", "signals_fired": 1,
                                      "primary_routing": "AE", "signals": [{"type": "seat_utilization"}],
                                      "seed": True, "source": ""}],
                        "counts": {"accounts": 1, "seed": 1}},
            "impact": {"headline_opportunity_surfaced": 41650000,
                       "headline_opportunity_label": "$41.6M", "net_new": {"accounts_targeted": 6},
                       "install_base": {}, "realized": {}, "data_complete": True,
                       "sources": {"tam_plays": True}},
        },
        "errors": {},
    }


def use(state):
    """Point the brain at a temp snapshot file and clear its cache."""
    fd, path = tempfile.mkstemp(suffix=".json")
    with os.fdopen(fd, "w") as f:
        json.dump(state, f)
    brain.STATE_URL = ""
    brain.STATE_PATH = path
    brain._cache.update({"state": None, "fetched_at": None, "error": None})
    return path


def run():
    checks = []
    def check(name, cond):
        checks.append((name, bool(cond)))

    # ---- 1. a fresh snapshot serves figures, and always says how old it is ----
    use(snapshot(age_hours=1.0))
    out = brain._strike_list()
    check("fresh response carries generated_at, age_hours and freshness",
          out["generated_at"] and out["age_hours"] is not None and out["freshness"] == "fresh")
    cited = next(a for a in out["accounts"] if a["domain"] == "cited.com")
    check("a cited row keeps its fit and ROI when fresh",
          cited.get("icp_total") == 88 and cited.get("roi_label") == "$23.8M")
    check("a cited row is not marked redacted", "redacted" not in cited)

    # ---- 2. an uncited row is redacted even in a fresh snapshot ----
    seedrow = next(a for a in out["accounts"] if a["domain"] == "seedco.com")
    check("a seed row loses fit, tier and ROI",
          "icp_total" not in seedrow and "tier" not in seedrow and "roi_label" not in seedrow)
    check("a seed row keeps its identity", seedrow["company"] and seedrow["domain"] == "seedco.com")
    check("a seed row says what was removed and why",
          "icp_total" in seedrow["redacted"] and "demonstration data" in seedrow["redaction_reason"])
    plan = brain._strike_plan("seedco.com")
    check("a seed strike plan drops the generated committee copy", "committee" not in plan)
    check("a cited strike plan keeps the committee",
          "committee" in brain._strike_plan("cited.com"))

    # ---- 3. past the threshold everything is redacted, with a warning ----
    use(snapshot(age_hours=100.0))
    out = brain._strike_list()
    check("a stale snapshot is labelled stale", out["freshness"] == "stale")
    check("a stale snapshot carries a do-not-quote warning",
          "withheld" in out["warning"] and "quote" in out["warning"])
    check("a stale snapshot redacts the CITED row too",
          all("icp_total" not in a for a in out["accounts"]))
    check("the stale reason names the age and the threshold",
          "100" in out["accounts"][0]["redaction_reason"]
          and "36" in out["accounts"][0]["redaction_reason"])
    imp = brain._impact()
    check("a stale impact scorecard withholds surfaced and realized",
          "headline_opportunity_surfaced" not in imp and "net_new" not in imp)
    check("a stale impact scorecard keeps the source-health flags",
          imp["data_complete"] is True and imp["sources"] == {"tam_plays": True})

    # ---- 4. past the hard limit nothing is served at all ----
    use(snapshot(age_hours=1000.0))
    try:
        brain._strike_list(); expired = False
    except HTTPException as e:
        expired = e.status_code == 503 and e.detail["error"] == "snapshot expired"
    check("a snapshot past the hard limit returns 503, not a redacted body", expired)

    # ---- 5. a broken clock is never read as fresh ----
    s = snapshot(); s["generated_at"] = "not-a-timestamp"
    use(s)
    out = brain._strike_list()
    check("an unparseable timestamp is 'unknown', not 'fresh'", out["freshness"] == "unknown")
    check("an unparseable timestamp still redacts",
          all("icp_total" not in a for a in out["accounts"]))
    s = snapshot(age_hours=-48.0)   # dated in the future
    use(s)
    check("a future-dated snapshot is not trusted", brain._strike_list()["freshness"] == "unknown")

    # ---- 6. no snapshot means no answer, never a bundled one ----
    brain.STATE_URL = ""
    brain.STATE_PATH = "/nonexistent/gtm_state.json"
    brain._cache.update({"state": None, "fetched_at": None, "error": None})
    try:
        brain._strike_list(); failed_closed = False
    except HTTPException as e:
        failed_closed = e.status_code == 503 and e.detail["error"] == "snapshot unavailable"
    check("an unreachable snapshot fails closed with 503", failed_closed)
    # The docstring still NAMES account_engine (it explains the old failure), so grep the
    # parsed imports rather than the text.
    import ast as _ast
    _tree = _ast.parse(open(os.path.join(HERE, "app.py")).read())
    _imported = set()
    for _n in _ast.walk(_tree):
        if isinstance(_n, _ast.Import):
            _imported.update(a.name.split(".")[0] for a in _n.names)
        elif isinstance(_n, _ast.ImportFrom) and _n.module:
            _imported.add(_n.module.split(".")[0])
    check("the brain imports no engine, so it ships no bundled fallback data",
          not ({"account_engine", "signal_processor", "impact_engine"} & _imported))

    # ---- 7. signals inherit the engine tag; the excluded customer stays excluded ----
    use(snapshot(age_hours=1.0))
    sig = brain._signals_list()
    check("a mock-tagged signal row is redacted", "signals" not in sig["accounts"][0])
    check("the signals payload reports its engine data_source", sig["data_source"] == "mock")
    shut = brain._strike_plan("hcsc.com")
    check("a confirmed customer returns the exclusion, not a cold plan",
          shut["customer_excluded"] is True and "install-base" in shut["error"])

    # ---- 8. the tuple bug that broke /v1/strike ----
    check("strike_list returns rows, not the (plays, excluded) tuple",
          isinstance(brain._strike_list()["accounts"], list)
          and all(isinstance(a, dict) for a in brain._strike_list()["accounts"]))

    # ---- 8b. trigger prose is gated per trigger, not per row ----
    # A seeded trigger ("won two new Medicaid state contracts") once reached a strike plan
    # for an account whose public record said the opposite. detail/play/stakes are what the
    # sequence copy is written from, so an uncited trigger must not carry them, and a row
    # that is seed only for a missing agent_count must not lose its SOURCED why-now signal.
    use(snapshot(age_hours=1.0))
    cited_plan = brain._strike_plan("cited.com")
    by_type = {t["type"]: t for t in cited_plan["triggers"]}
    check("a sourced trigger keeps its prose on a cited row",
          by_type["cost_mandate"].get("detail") == "d" and "redacted" not in by_type["cost_mandate"])
    check("an uncited trigger loses detail, play and stakes",
          not any(k in by_type["cc_expansion"] for k in ("detail", "play", "stakes")))
    check("an uncited trigger says why it was scrubbed",
          "no source" in by_type["cc_expansion"]["redaction_reason"])
    check("an uncited trigger keeps its type for routing",
          by_type["cc_expansion"]["type"] == "cc_expansion")
    use(snapshot(age_hours=100.0))
    stale_trigs = brain._strike_plan("cited.com")["triggers"]
    check("a stale snapshot scrubs even a SOURCED trigger's prose",
          all("detail" not in t for t in stale_trigs))

    # ---- 9. impact is scored on the live gated universe, not a stale intermediate ----
    # impact_engine reads tam_plays.json, which run_daily.sh writes whenever it last ran. On
    # 2026-09-05 that file was five days old and predated the customer-exclusion gate, so the
    # scorecard counted HCSC (a confirmed customer) and omitted Centene (the only cited row).
    import build_gtm_state
    live = build_gtm_state.build()
    check("the generator produced a strike universe", not live["errors"].get("strike"))
    live_strike, live_impact = live["engines"]["strike"], live["engines"].get("impact", {})
    excluded_domains = {e["domain"] for e in live_strike["excluded"]}
    excluded_names = {e["company"] for e in live_strike["excluded"]}
    breakdown = {x["company"] for x in live_impact.get("net_new", {}).get("breakdown", [])}
    check("no customer-excluded account reaches the strike universe",
          not ({a["domain"] for a in live_strike["accounts"]} & excluded_domains))
    check("no customer-excluded account reaches the impact breakdown",
          not (breakdown & excluded_names))
    check("impact states how much of its figure rests on seed rows",
          "seed_accounts" in live_impact.get("basis", {})
          and live_impact["basis"]["accounts"] == live_strike["counts"]["accounts"])
    check("impact still self-labels its basis UNVERIFIED",
          live_impact.get("surfaced_basis") == "UNVERIFIED")
    check("a generator run leaves the engines' data files alone",
          not os.path.exists(os.path.join(HERE, "..", "..", "tam-outbound-engine", "data",
                                          "tam_plays.json.tmp")))
    check("every strike row carries provenance fields",
          all("source" in a and "seed" in a for a in live_strike["accounts"]))

    # ---- live loop (2026-09-11): unreviewed war-room signals ride the row as context ----
    unrev = [{"id": "sig-20260904-cambia-4fa040", "state": "unreviewed", "trigger_type": "cc_expansion",
              "date": "2026-09-04", "quote": "Arkansas regulators approved the affiliation", "url": "https://example.com/x",
              "org": "Cambia Health Solutions", "note": "context only"}]
    seed_row = {"domain": "x.com", "company": "X", "icp_total": 70, "tier": 2, "roi_label": "$1M", "agent_count": 500,
                "source": "", "seed": True, "triggers": [], "unreviewed_signals": unrev}
    cited_row = {**seed_row, "source": "cited", "seed": False}
    gated = gtm_state.apply_gates([seed_row, cited_row], "strike", "fresh", 1.0)
    check("unreviewed signals survive the seed redaction (they carry their own source)",
          gated[0]["unreviewed_signals"] == unrev and "icp_total" not in gated[0])
    check("unreviewed signals survive on a cited row and carry no scoring fields",
          gated[1]["unreviewed_signals"] == unrev and not any(k in unrev[0] for k in ("icp_total", "fit", "roi_label", "tier")))
    check("every unreviewed signal carries id, quote and url",
          all(sg.get("id") and sg.get("quote") and sg.get("url") for r in gated for sg in r["unreviewed_signals"]))
    check("live strike snapshot counts unreviewed signals and reports review states",
          "unreviewed_signals" in live_strike.get("counts", {}) and set(live_strike.get("review", {})) == {"unreviewed", "approved", "denied"})
    check("live snapshot names its universe source",
          live.get("universe") in ("audiences", "csv", "stale"))

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 62)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
