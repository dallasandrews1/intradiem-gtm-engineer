#!/usr/bin/env python3
"""
Intradiem GTM Brain: the hosted service every seller surface calls.

One service, owned by you, wrapping both engines and the impact scorecard. It serves
two things on the same host, same auth, same log:

  - a REST API  (/v1/...)   used by the Slack app and anything else
  - a remote MCP (/mcp)     used by the Claude plugin, so sellers install nothing

Sellers never touch the engine, the configs, or Clay. They send a domain and get a
plan. Every call is logged (requests.jsonl): your audit trail and adoption metric.

Run locally:
    pip install -r requirements.txt
    GTM_API_KEYS="slack:KEY1,claude:KEY2" uvicorn app:app --reload --port 8000

Auth: send header  X-API-Key: <key>  matching one in GTM_API_KEYS ("label:key,..").
Unset GTM_API_KEYS runs open in dev mode and logs the caller as "dev".
"""
import datetime
import json
import os
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Header, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from mcp.server.fastmcp import FastMCP

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for _p in ("tam-outbound-engine", "intradiem-signal-engine", "impact"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import account_engine        # noqa: E402  net-new strike plans
import signal_processor      # noqa: E402  install-base signals
import impact_engine         # noqa: E402  scorecard

LOG = os.path.join(HERE, "logs", "requests.jsonl")


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
    rec = {"ts": datetime.datetime.utcnow().isoformat() + "Z", "actor": actor, "path": path}
    if extra:
        rec.update(extra)
    with open(LOG, "a") as f:
        f.write(json.dumps(rec) + "\n")


def _plays():
    return account_engine.build_plays(account_engine.load_cfg(), datetime.date.today())


def _strike_list():
    return [
        {"company": p["company"], "domain": p["domain"], "fit": p["icp_total"],
         "tier": p["tier"], "fresh": p["fresh"], "roi": p["roi_label"],
         "top_trigger": p["triggers"][0]["label"] if p["triggers"] else None,
         "seller": p["seller"]["seller_name"] if p.get("seller") else None}
        for p in _plays()
    ]


def _strike_plan(domain):
    return next((p for p in _plays() if p["domain"] == domain), None)


def _signal(domain):
    return next((r for r in signal_processor.process() if r["domain"] == domain), None)


# ---------- remote MCP (for the Claude plugin) ----------
mcp_server = FastMCP("intradiem-gtm", stateless_http=True, streamable_http_path="/")


@mcp_server.tool()
def strike_list() -> str:
    """List net-new target accounts ranked by fit and why-now, with ROI and the top trigger."""
    return json.dumps(_strike_list(), indent=2)


@mcp_server.tool()
def get_strike_plan(domain: str) -> str:
    """Full strike plan for one domain: fit, ROI, why-now, buying committee, and a sequence per persona."""
    m = _strike_plan(domain)
    return json.dumps(m or {"error": f"{domain} is not in the target set"}, indent=2)


@mcp_server.tool()
def list_signals() -> str:
    """Install-base accounts with their firing expansion and risk signals."""
    return json.dumps(signal_processor.process(), indent=2)


@mcp_server.tool()
def get_signals(domain: str) -> str:
    """Expansion and risk signals for one install-base account by domain."""
    m = _signal(domain)
    return json.dumps(m or {"error": f"{domain} is not monitored"}, indent=2)


@mcp_server.tool()
def impact_scorecard() -> str:
    """The GTM impact scorecard: opportunity surfaced, activity, and realized results."""
    return json.dumps(impact_engine.build(), indent=2)


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


@asynccontextmanager
async def lifespan(_app):
    async with mcp_server.session_manager.run():
        yield


# ---------- REST API (for Slack and everything else) ----------
app = FastAPI(title="Intradiem GTM Brain", version="1.1", lifespan=lifespan)


@app.get("/healthz")
def healthz():
    return {"ok": True, "service": "intradiem-gtm-brain"}


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
    return signal_processor.process()


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
    return impact_engine.build()


# the Claude plugin connects here (remote MCP, no local install for sellers)
app.mount("/mcp", mcp_app)
