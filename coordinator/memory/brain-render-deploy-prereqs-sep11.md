---
name: brain-render-deploy-prereqs-sep11
description: "Sep 11 2026, the Render brain still runs the pre-Sep-5 build (healthz has no version field), Render does NOT auto-deploy from main, and the gtm_state.json snapshot has NEVER been published (gtm-brain-state.pages.dev does not exist), so a Manual Deploy of main today would fail closed with 503s until GTM_STATE_URL points at a live snapshot"
metadata: 
  node_type: memory
  type: project
  originSessionId: 70ef698f-e87f-4dc7-8724-5e09a9fddce5
  modified: 2026-09-11T16:04:41.797Z
---

State on Sep 11 2026 after pushing commit 614fa36 (Slack auth door, host fix, mcp<2 pin) to origin main:

- Live `/healthz` returns only `{"ok":true,"service":"intradiem-gtm-brain"}`: no `version`, no freshness. That is the pre-Sep-5 code. Render did not build the Sep 5 rewrite and did not build 614fa36 either, so auto-deploy from main is OFF (or the service is bound to a different branch). Manual Deploy is the path.
- The new brain fetches `GTM_STATE_URL` and has no bundled fallback. The snapshot has never been published: `https://gtm-brain-state.pages.dev/gtm_state.json` does not resolve and `wrangler pages project list` shows no such project (only gtm-operating-map and the other page projects). Deploying the new code before a snapshot URL exists = every data endpoint 503, healthz `ok:false`.
- A fresh staged snapshot exists at `~/Desktop/Intradiem Deliverables/deploy-gtm-brain-state/` (nightly sync_publish regenerates it; Sep 11 10:50 generated_at). It is 6 accounts, all 6 seed rows ([[tam-seed-data-never-swapped-sep5]]), so the brain would withhold fit/ROI/copy on every row with a SEED reason. The connection would work; the numbers would all read withheld.
- PUBLISHED Sep 11 2026 ~16:05Z on Dallas's go: Pages project gtm-brain-state created with `wrangler pages project create --force` (the un-forced path delegates to Workers-Pages and refuses a folder with no html), deployed from the Desktop staging folder, https://gtm-brain-state.pages.dev/gtm_state.json serves 200 with X-Robots-Tag noindex and 60s cache. Nightly sync_publish still only STAGES; re-publish is `publish_gtm_state.sh --deploy` (add --force to the create step only if the project is ever recreated).
- Publishing is outward-facing by design (`publish_gtm_state.sh --deploy` creates a PUBLIC Pages project; the file carries seller emails, account scores and generated prospect copy). Wrangler on the personal Mac is logged in as andrewsdallas3@gmail.com, account 37eeacfb..., so the publish is one command once Dallas says go. Authenticated alternative: any HTTPS host plus `GTM_STATE_TOKEN` (the fetcher sends it as a bearer).
- Render env needed for the new build: `GTM_STATE_URL` (plus `GTM_STATE_TOKEN` if authenticated), `GTM_API_KEYS` (already set), `SLACK_SIGNING_SECRET` (Dallas added Sep 11, Save only).

**Why:** three separate gaps (no auto-deploy, no published snapshot, all-seed data) each looked like "the brain is alive" from the outside.
**How to apply:** order is publish snapshot, set GTM_STATE_URL in Render, Manual Deploy, healthz shows version 2.1 and `source: url`, keyed tools/list passes, then Slack install request. See [[brain-mcp-421-host-pinning-sep11]], [[brain-snapshot-rewrite-sep5]].
