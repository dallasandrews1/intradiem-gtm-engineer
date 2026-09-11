#!/usr/bin/env python3
"""
Intradiem GTM Brain: the hosted service every seller surface calls.

One service, owned by you, serving both engines and the impact scorecard. It serves two
things on the same host, same auth, same log:

  - a REST API  (/v1/...)   used by the Slack app and anything else
  - a remote MCP (/mcp)     used by the Claude plugin, so sellers install nothing

WHERE THE DATA COMES FROM (changed 2026-09-05)
----------------------------------------------
This service no longer imports the engines or reads their CSVs. It fetches ONE published
snapshot, gtm_state.json, over HTTP and serves that.

It used to `import account_engine` and read the CSVs the Dockerfile copied in at build
time, which meant the data was frozen at the last deploy and the only way to refresh it was
to rebuild the container. Nobody did, so it served July data into September: a Cowork run
got Centene at fit 43 Tier 3 with no agent count and no triggers, against a local engine
that had it at 88 Tier 1 with three sourced triggers, and copy reading "On ~0 agents that's
about $0 a year" under a subject line about a seven-figure number.

Now: the generator runs where the real data lives, publishes gtm_state.json, and refreshing
what sellers see is a file publish rather than a redeploy. Every response carries
`generated_at` and `freshness`, and past the age threshold the numbers are withheld instead
of served (see gtm_state.apply_gates). A missing number forces a question; a stale number
gets quoted.

Run locally:
    pip install -r requirements.txt
    GTM_STATE_PATH=./gtm_state.json GTM_API_KEYS="slack:KEY1,claude:KEY2" \
        uvicorn app:app --reload --port 8000

Environment:
    GTM_STATE_URL          published snapshot URL (production). Preferred.
    GTM_STATE_TOKEN        bearer token / service token for that URL, if it is not public.
    GTM_STATE_AUTH_HEADER  header name for the token, default "Authorization".
    GTM_STATE_PATH         local snapshot file (dev fallback, used if URL is unset).
    GTM_STATE_TTL_SECONDS  in-process cache TTL, default 300.
    GTM_STATE_MAX_AGE_HOURS       redact past this age, default 36.
    GTM_STATE_HARD_MAX_AGE_HOURS  refuse past this age, default 168.
    GTM_API_KEYS           "label:key,label:key". Unset runs open in dev and logs "dev".
"""
import datetime
import json
import os
import threading
import urllib.error
import urllib.request

from fastapi import FastAPI, Header, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from mcp.server.fastmcp import FastMCP

import gtm_state

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "logs", "requests.jsonl")

STATE_URL = os.environ.get("GTM_STATE_URL", "").strip()
STATE_PATH = os.environ.get("GTM_STATE_PATH", "").strip()
TTL = float(os.environ.get("GTM_STATE_TTL_SECONDS", "300"))
MAX_AGE = float(os.environ.get("GTM_STATE_MAX_AGE_HOURS", gtm_state.DEFAULT_MAX_AGE_HOURS))
HARD_MAX = float(os.environ.get("GTM_STATE_HARD_MAX_AGE_HOURS", gtm_state.DEFAULT_HARD_MAX_AGE_HOURS))


# ---------- shared helpers ----------
def load_keys():
    out = {}
    for pair in os.environ.get("GTM_API_KEYS", "").split(","):
        if ":" in pair:
            label, key = pair.split(":", 1)
            out[key.strip()] = label.strip()
    return out


def auth(x_api_key):
    keys = load_keys()
    if not keys:
        return "dev"
    if x_api_key not in keys:
        raise HTTPException(status_code=401, detail="invalid or missing API key")
    return keys[x_api_key]


def log(actor, path, extra=None):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    rec = {"ts": gtm_state.iso(gtm_state.utcnow()), "actor": actor, "path": path}
    if extra:
        rec.update(extra)
    with open(LOG, "a") as f:
        f.write(json.dumps(rec) + "\n")


# ---------- the snapshot ----------
_cache = {"state": None, "fetched_at": None, "error": None}
_lock = threading.Lock()


def _read_snapshot():
    """Fetch the snapshot from GTM_STATE_URL, or read GTM_STATE_PATH in dev.

    The snapshot carries seller emails, account scores and generated prospect-facing copy,
    so the transport supports auth rather than assuming a public URL. Set GTM_STATE_TOKEN
    and, if the host wants something other than a bearer token, GTM_STATE_AUTH_HEADER.
    Covers a private GitHub raw fetch, a Cloudflare Access service token, or a signed URL.
    """
    if STATE_URL:
        headers = {"Cache-Control": "no-cache", "Accept": "application/json"}
        token = os.environ.get("GTM_STATE_TOKEN", "").strip()
        if token:
            header_name = os.environ.get("GTM_STATE_AUTH_HEADER", "Authorization").strip()
            headers[header_name] = token if header_name != "Authorization" else f"Bearer {token}"
            if "api.github.com" in STATE_URL:
                # the contents API returns the file itself, not the JSON wrapper, with this
                headers["Accept"] = "application/vnd.github.raw"
        req = urllib.request.Request(STATE_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode("utf-8"))
    if STATE_PATH:
        with open(STATE_PATH) as f:
            return json.load(f)
    raise RuntimeError("neither GTM_STATE_URL nor GTM_STATE_PATH is set")


def get_state(force=False):
    """Fetch the snapshot, cached for TTL seconds.

    Fail CLOSED. If the snapshot cannot be read and nothing is cached, the endpoints raise
    503 rather than falling back to anything bundled in the image. A bundled fallback is
    exactly the frozen-copy failure this rewrite removes, so there is deliberately no such
    path: no snapshot means no answer, not an old answer.
    """
    now = gtm_state.utcnow()
    with _lock:
        fresh_cache = (_cache["state"] is not None and _cache["fetched_at"] is not None
                       and (now - _cache["fetched_at"]).total_seconds() < TTL)
        if fresh_cache and not force:
            return _cache["state"]
        try:
            state = _read_snapshot()
            _cache.update({"state": state, "fetched_at": now, "error": None})
            return state
        except (urllib.error.URLError, OSError, ValueError, RuntimeError) as e:
            _cache["error"] = f"{type(e).__name__}: {e}"
            if _cache["state"] is not None:
                # Serve the last good snapshot rather than nothing, but its own age still
                # runs it through the same redaction gate, so a fetch outage degrades into
                # withheld numbers instead of silently stale ones.
                return _cache["state"]
            raise


def _state_or_503():
    try:
        return get_state()
    except Exception:
        raise HTTPException(status_code=503, detail={
            "error": "snapshot unavailable",
            "detail": _cache["error"],
            "hint": "GTM_STATE_URL/GTM_STATE_PATH unreachable. The brain serves no bundled "
                    "fallback by design; regenerate and republish gtm_state.json.",
        })


def _gated(kind, engine_key):
    """Return (envelope, rows) with the freshness header and per-row redaction applied."""
    state = _state_or_503()
    env = gtm_state.envelope(state, max_age=MAX_AGE, hard_max=HARD_MAX)
    if env["freshness"] == "expired":
        raise HTTPException(status_code=503, detail={
            "error": "snapshot expired",
            "generated_at": env["generated_at"], "age_hours": env["age_hours"],
            "hint": f"Older than the {HARD_MAX}h hard limit. Regenerate and republish "
                    "gtm_state.json; nothing is served from a snapshot this old.",
        })
    engine = state.get("engines", {}).get(engine_key)
    if engine is None:
        err = state.get("errors", {}).get(engine_key, "engine missing from snapshot")
        raise HTTPException(status_code=503, detail={"error": f"{engine_key} unavailable",
                                                     "detail": err})
    rows = gtm_state.apply_gates(engine.get("accounts", []), kind,
                                 env["freshness"], env["age_hours"])
    env["data_source"] = engine.get("data_source")
    env["counts"] = engine.get("counts")
    if engine.get("note"):
        env["note"] = engine["note"]
    return env, rows


def _strike_list():
    env, rows = _gated("strike", "strike")
    slim = []
    for r in rows:
        row = {k: r[k] for k in (
            "company", "domain", "icp_total", "tier", "fresh", "roi_label", "seller",
            "source", "seed", "redacted", "redaction_reason") if k in r}
        # A scrubbed trigger has no `label` (that is prose, and prose is what scrubbing
        # removes), so name it by type instead of raising. The list must still say a
        # why-now exists even when it may not repeat what it claims.
        top = (r.get("triggers") or [None])[0]
        if not top:
            row["top_trigger"] = None
        elif top.get("label"):
            row["top_trigger"] = top["label"]
        else:
            row["top_trigger"] = f"{top.get('type', 'trigger')} (detail withheld: no source)"
        # `fit` and `roi` are aliases the Slack surface has always read. Keep them, and keep
        # them ABSENT on a redacted row so a consumer that does not check `redacted` fails
        # loudly on a missing key instead of quietly printing a withheld number as blank.
        if "icp_total" in row:
            row["fit"] = row["icp_total"]
        if "roi_label" in row:
            row["roi"] = row["roi_label"]
        slim.append(row)
    return {**env, "accounts": slim}


def _strike_plan(domain):
    env, rows = _gated("strike", "strike")
    m = next((r for r in rows if r["domain"] == domain), None)
    if m:
        return {**env, **m}
    state = _state_or_503()
    shut = next((e for e in state["engines"]["strike"].get("excluded", [])
                 if e["domain"] == domain), None)
    if shut:
        return {**env, **shut,
                "error": f"{shut['company']} is a confirmed customer ({shut['match']}); "
                         "no cold strike plan. Route as install-base expansion."}
    return None


def _signals_list():
    env, rows = _gated("signal", "signals")
    return {**env, "accounts": rows}


def _signal(domain):
    env, rows = _gated("signal", "signals")
    m = next((r for r in rows if r["domain"] == domain), None)
    return {**env, **m} if m else None


def _impact():
    state = _state_or_503()
    env = gtm_state.envelope(state, max_age=MAX_AGE, hard_max=HARD_MAX)
    if env["freshness"] == "expired":
        raise HTTPException(status_code=503, detail={"error": "snapshot expired",
                                                     "age_hours": env["age_hours"]})
    b = state.get("engines", {}).get("impact")
    if b is None:
        raise HTTPException(status_code=503, detail={
            "error": "impact unavailable",
            "detail": state.get("errors", {}).get("impact", "engine missing from snapshot")})
    if env["freshness"] in ("stale", "unknown"):
        # Surfaced-vs-realized is the one number that must never be quoted at an unknown
        # age; withhold the figures and keep only the source-health flags.
        return {**env, "data_complete": b.get("data_complete"), "sources": b.get("sources"),
                "redacted": ["net_new", "install_base", "realized",
                             "headline_opportunity_surfaced", "headline_opportunity_label"],
                "redaction_reason": env.get("warning")}
    return {**env, **b}


# ---------- remote MCP (for the Claude plugin) ----------
mcp_server = FastMCP("intradiem-gtm", stateless_http=True, streamable_http_path="/")

_FRESHNESS_NOTE = ("Every response carries generated_at, age_hours and freshness. If "
                   "freshness is not 'fresh', scores, ROI and generated copy have been "
                   "withheld and nothing in the response may be quoted. A row marked "
                   "seed:true is demonstration data, not a real account.")


@mcp_server.tool()
def strike_list() -> str:
    """List net-new target accounts ranked by fit and why-now, with ROI and the top trigger.

    Reads a dated snapshot; check `freshness` before using any figure."""
    return json.dumps(_strike_list() | {"_note": _FRESHNESS_NOTE}, indent=2)


@mcp_server.tool()
def get_strike_plan(domain: str) -> str:
    """Full strike plan for one domain: fit, ROI, why-now, buying committee, and a sequence per persona.

    Reads a dated snapshot; check `freshness` before using any figure."""
    m = _strike_plan(domain)
    return json.dumps((m or {"error": f"{domain} is not in the target set"}) | {"_note": _FRESHNESS_NOTE},
                      indent=2)


@mcp_server.tool()
def list_signals() -> str:
    """Install-base accounts with their firing expansion and risk signals.

    Reads a dated snapshot; check `freshness` before using any figure."""
    return json.dumps(_signals_list() | {"_note": _FRESHNESS_NOTE}, indent=2)


@mcp_server.tool()
def get_signals(domain: str) -> str:
    """Expansion and risk signals for one install-base account by domain.

    Reads a dated snapshot; check `freshness` before using any figure."""
    m = _signal(domain)
    return json.dumps((m or {"error": f"{domain} is not monitored"}) | {"_note": _FRESHNESS_NOTE},
                      indent=2)


@mcp_server.tool()
def impact_scorecard() -> str:
    """The GTM impact scorecard: opportunity surfaced, activity, and realized results.

    Surfaced and realized are separate and must never be blended."""
    return json.dumps(_impact() | {"_note": _FRESHNESS_NOTE}, indent=2)


mcp_app = mcp_server.streamable_http_app()


class KeyAuthMiddleware(BaseHTTPMiddleware):
    """Same API-key gate as the REST side, applied to the MCP endpoint, plus logging."""
    async def dispatch(self, request, call_next):
        keys = load_keys()
        if keys:
            key = request.headers.get("x-api-key") or \
                request.headers.get("authorization", "").replace("Bearer ", "").strip()
            if key not in keys:
                return JSONResponse({"error": "invalid or missing API key"}, status_code=401)
            log(keys[key], "/mcp")
        else:
            log("dev", "/mcp")
        return await call_next(request)


mcp_app.add_middleware(KeyAuthMiddleware)


from contextlib import asynccontextmanager  # noqa: E402


@asynccontextmanager
async def lifespan(_app):
    async with mcp_server.session_manager.run():
        yield


# ---------- REST API (for Slack and everything else) ----------
app = FastAPI(title="Intradiem GTM Brain", version="2.0", lifespan=lifespan)


@app.get("/healthz")
def healthz():
    """Liveness plus snapshot age, so a monitor can catch a stale brain without a key."""
    out = {"ok": True, "service": "intradiem-gtm-brain", "version": "2.0",
           "source": "url" if STATE_URL else ("path" if STATE_PATH else "unconfigured")}
    try:
        state = get_state()
        out.update(gtm_state.envelope(state, max_age=MAX_AGE, hard_max=HARD_MAX))
        out["ok"] = out.get("freshness") == "fresh"
    except Exception:
        out.update({"ok": False, "freshness": "unavailable", "error": _cache["error"]})
    return out


@app.get("/v1/strike")
def strike_list_rest(x_api_key: str = Header(default="")):
    actor = auth(x_api_key)
    log(actor, "/v1/strike")
    return _strike_list()


@app.get("/v1/strike/{domain}")
def strike_plan_rest(domain: str, x_api_key: str = Header(default="")):
    actor = auth(x_api_key)
    log(actor, "/v1/strike/{domain}", {"domain": domain})
    m = _strike_plan(domain)
    if not m:
        raise HTTPException(status_code=404, detail=f"{domain} is not in the target set")
    return m


@app.get("/v1/signals")
def signals_rest(x_api_key: str = Header(default="")):
    actor = auth(x_api_key)
    log(actor, "/v1/signals")
    return _signals_list()


@app.get("/v1/signals/{domain}")
def signals_domain_rest(domain: str, x_api_key: str = Header(default="")):
    actor = auth(x_api_key)
    log(actor, "/v1/signals/{domain}", {"domain": domain})
    m = _signal(domain)
    if not m:
        raise HTTPException(status_code=404, detail=f"{domain} is not monitored")
    return m


@app.get("/v1/impact")
def impact_rest(x_api_key: str = Header(default="")):
    actor = auth(x_api_key)
    log(actor, "/v1/impact")
    return _impact()


@app.post("/v1/refresh")
def refresh_rest(x_api_key: str = Header(default="")):
    """Drop the cache and re-fetch now, so a republish can be picked up without waiting
    out the TTL or restarting the service."""
    actor = auth(x_api_key)
    log(actor, "/v1/refresh")
    try:
        state = get_state(force=True)
    except Exception:
        raise HTTPException(status_code=503, detail={"error": "snapshot unavailable",
                                                     "detail": _cache["error"]})
    return gtm_state.envelope(state, max_age=MAX_AGE, hard_max=HARD_MAX)


# the Claude plugin connects here (remote MCP, no local install for sellers)
app.mount("/mcp", mcp_app)
