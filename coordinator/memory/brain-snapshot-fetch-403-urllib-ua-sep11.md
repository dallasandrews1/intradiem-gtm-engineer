---
name: brain-snapshot-fetch-403-urllib-ua-sep11
description: "Sep 11 2026, first live run of brain 2.1 on Render showed healthz ok:false with HTTP 403 from gtm-brain-state.pages.dev because Cloudflare rejects urllib's default Python-urllib user agent; fixed by a named User-Agent header in the fetcher, commit c027f12 on main, live on Render 19:48Z with healthz ok:true and freshness fresh"
metadata:
  type: project
---

Seen Sep 11 2026 19:43Z right after the Render service was re-bound to intradiem-gtm-engineer and built main commit 4ac3706 (mcp 1.30.0, version 2.1).

- Live `/healthz`: `{"ok":false,"version":"2.1","source":"url","freshness":"unavailable","error":"HTTPError: HTTP Error 403: Forbidden"}`. Unsigned `/mcp/` initialize returned 401 as intended.
- Cause verified with curl against `https://gtm-brain-state.pages.dev/gtm_state.json`: default curl UA 200, `Python-urllib/3.11` 403 (server: cloudflare, plain-text body), `intradiem-gtm-brain/2.1` 200. Cloudflare's default bot rules block the stock urllib agent; nothing in the brain's own auth is involved.
- Fix: `_read_snapshot()` in `gtm-hosted-platform/brain/app.py` now sends `User-Agent: intradiem-gtm-brain/2.1`. Tests 36/36 and 20/20 in `~/.venvs/intradiem`; local uvicorn run against the real URL returned healthz ok:true, freshness fresh, age 3.65h.
- DEPLOYED: commit c027f12 pushed to origin main Sep 11 19:47Z on Dallas's go; Render auto-built it (dep-dai5lilbedkc73ecli60) and reported live 19:48Z. Live healthz: ok:true, version 2.1, source url, freshness fresh, age 3.73h. Unsigned /mcp/ initialize still 401. Dallas ran the keyed tools/list from his terminal Sep 11 ~20:00Z: five tools returned (strike_list, get_strike_plan, list_signals, get_signals, impact_scorecard) over SSE, no 421, so the host-pinning fix is confirmed on Render. The brain is fully verified; next step is the Slack app install from the Sep 11 deploy sheet.

**Why:** the snapshot host is Cloudflare Pages and the fetcher is stdlib urllib; the combination had never been exercised before this deploy.
**How to apply:** any new HTTP fetch from the brain or an automation toward a Cloudflare-fronted host should set a named User-Agent. See [[brain-render-wrong-repo-binding-sep11]], [[brain-render-deploy-prereqs-sep11]].
