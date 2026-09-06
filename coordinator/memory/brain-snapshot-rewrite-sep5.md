---
name: brain-snapshot-rewrite-sep5
description: Sep 5 2026 - hosted GTM brain rebuilt to read a published gtm_state.json snapshot instead of CSVs baked into the container; stale figures now withheld, not served. Render redeploy still open.
metadata:
  type: project
---

The hosted brain (`intradiem-gtm-system.onrender.com`) served July data into September because
the Dockerfile copied the engine CSVs into the image, so data froze at build time and the only
refresh path was a redeploy. Rebuilt Sep 5 2026.

**What changed**
- `brain/build_gtm_state.py` scores all three engines where the real data lives and emits one
  `gtm_state.json`; `brain/app.py` fetches it over HTTP (`GTM_STATE_URL`, token supported) and
  imports no engine. Refresh is now a file publish, not a redeploy.
- `brain/gtm_state.py` is the shared contract. Every response carries `generated_at`/`age_hours`/
  `freshness`. Past 36h, or on any uncited (`seed`) row, fit/tier/ROI/agent_count and generated
  copy are WITHHELD with a reason. Past 168h the brain returns 503. No bundled fallback: no
  snapshot means 503, never an old answer.
- Trigger prose (`detail`/`play`/`stakes`) is scrubbed PER TRIGGER when it has no source, so a
  row that is seed only for a missing agent_count keeps its sourced why-now.
- `brain/publish_gtm_state.sh` stages by default (`--deploy` to push); nightly
  `automation/sync_publish.sh` regenerates and stages, log-only.
- Slack surface made freshness-aware; it crashed on the new shape and on redacted rows.

**Bugs found and fixed along the way**
- `add_strike_account` wrote 7 positional values into a 12-column header, so `wfm` landed in
  `acd_source`. Now writes by header name. See [[gate-integrity-fn-send-ready-not-shared]].
- `/v1/strike` was hard-broken (TypeError): `build_plays` returns `(plays, excluded)` and app.py
  treated the tuple as rows.
- The impact scorecard read a stale `tam_plays.json` that predated the customer-exclusion gate,
  so "net-new opportunity surfaced" counted HCSC, a confirmed customer, and omitted Centene.
  Impact is now scored on the universe built in the same run.

**Still open:** the Render service runs the old build; the strike-sequence skill's "use the local
CLI, not the MCP" warning stands until it is redeployed. Tests: 60 TAM / 14 signal / 36 brain.
Related: [[audiences-strike-universe-refresh-sep5]], [[feedback-best-model-every-account]].
