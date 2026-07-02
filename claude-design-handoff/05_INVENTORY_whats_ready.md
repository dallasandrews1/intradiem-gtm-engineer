# INVENTORY — everything that's ready (for Section 09 index)
All built pre-access, runs dry-run/seeded today, goes live Jul 6 by wiring marked hooks — no structural change.

## Engines (Python, verified runnable)
- **Cohesion conductor** (`gtm-cohesion-layer/conductor.py`) — the 7-stage weekly orchestrator with maker→critic→human gates, WIP/throughput/operator-test guardrails, and a 12-assertion `--preflight` go-live gate. Fail-closed: refuses to run live until preflight is green.
- **TAM / outbound engine** (`tam-outbound-engine/`) — new-logo strike accounts: fit/tier scoring, fresh-trigger detection, ROI, seller routing. Exposed via the `intradiem-tam` MCP.
- **Signal engine** (`intradiem-signal-engine/`) — install-base expansion/risk signals (automation-volume drop, champion change, CRM-not-connected back-office wedge, seat utilization, coaching/rule gaps), owner-routed. Exposed via the `intradiem-signals` MCP.
- **Impact engine** (`impact/`) — instrumentation scorecard ($ surfaced, signals, pipeline), source-tagged. [outputs are DRY-RUN/seeded]
- **Single source of truth** (`engine_state.json`) — every dashboard reads it; the conductor writes it. Kills dashboard drift.

## Dashboards / live artifacts
- **Command Center** — canonical live front door (gates, approvals, deliverability, variant winners, attribution credit).
- **Golden List** — accounts scored/graded board.
- **Control Plane** — install-base white-space (the 200 back-office wedge).
- **ROI Calculator** — live economic-impact tool.
- **Mission Control** — daily personal tracker.
- **Day-1 Audit Console** — Salesforce-schema refit checklist for go-live.
- Local dev twins: control_tower / attribution_dashboard / approval_queue / deliverability_monitor / variant_tracker (read engine_state.json; promote to live on Jul 6 wired to Salesforce).

## Build specs & packs (Day-1 accelerators)
- **GTM Engine Build Spec** — Golden List schema, enrichment waterfall, signal library, attribution schema (the standing north-star spec the conductor re-reads each run).
- **Clay Build Pack** — click-by-click rebuild (~2 hrs): tables, columns, waterfalls, fit/intent/grade formulas, signal columns, source-tag writes, webhooks. Built in free trial, templated into Intradiem.
- **Attribution Loop Spec** — reply-sync agent (reply → classify → status → funnel, source-scoped) = the credit-line keystone.
- **Message-variant starter pack** — 3 variants/segment.
- **Q3 Bulletproof Operating Plan** + **Weekly Conductor Runbook** — the 8-week pilot mapped with premortem fixes and the weekly cadence.

## Skills library (GTM-engineer skills, ready to invoke)
- **intradiem-signal-to-play** — one account signal → synchronized Marketing brief + Sales alert + personalized outreach.
- **intradiem-roi-business-case** — CFO/economic-buyer 1-page impact statement from call data.
- **intradiem-competitive-intel** — competitor mention → counter-narrative wedge brief.
- **intradiem-content-engine** — one source asset → multi-channel content set.
- **intradiem-verified-metrics** — citation-discipline source of truth for any Intradiem number.
- Plus the cognitive-calibration + strategic-premortem thinking layers that gate the work.

## Scheduled automations (running now, dry-run)
- **daily-signal-scan** — weekday 7am prioritized strike + expansion briefing.
- **weekly-gtm-conductor** — Monday 8am preflight + conductor run + Command Center refresh, with gate/guardrail reporting.

## Day-1 / Week-1 order of operations (the only go-live work)
1. **Ratify attribution in writing with Naveen** — credit at the qualified-reply/meeting-sourced line + 3 Salesforce fields + 1× baseline. (The do-nothing-else move.)
2. Build Clay from the Build Pack on a 10-row test slice; confirm ICP/scoring with Naveen + Scott Kemme.
3. Stand up deliverability warmup → monitor green before any volume.
4. Flip the conductor live (preflight must be green); wire Clay/sender/Salesforce hooks; keep the Monday schedule.
5. First real run: small, 3 variants/segment, human-approved, instrumented.

**Bottom line:** nothing here needs to be built — it needs to be wired to real data. Pre-access work = design/spec/content. Go-live work = four preflight checklist items.
