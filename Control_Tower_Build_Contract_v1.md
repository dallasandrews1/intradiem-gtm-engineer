# GTM Control Tower — Build Contract v1

**Owner:** Dallas Andrews
**Author of contract:** coordinator session (the brain), 2026-07-18
**Builder:** VS Code agent (the hands)
**Status:** contract only. Nothing is built yet. Build to this spec; do not improvise the schema.

---

## 0. Why this file exists

The VS Code agent proposed a "control tower for GTM execution." Six of its seven proposals already exist here as skills. This one is the real gap. But the tower is **not** a greenfield build. The state backbone already exists:

- `gtm-cohesion-layer/engine_state.json` — the designed single source of truth (18 top-level keys). Its own `_meta` says: *"One state file every dashboard reads from. Fixes dashboard drift."* That is the tower's spine.
- `impact/impact.json` — surfaced vs realized impact.
- `clay_credit_ledger.csv` — append-only credit burn.
- `Clay_Build_State_Registry.md` — present-tense ground truth for what is actually live in Clay.
- `tam-outbound-engine/account_plays.json` — per-account plays, triggers, ROI.
- `Readout_Log.md` — one line per Friday readout, with open asks.
- `salesforce-dashboard/*.html` — two earlier hardcoded mockups. **The tower supersedes these.** They hardcode values; that is the exact "dashboard drift" `engine_state.json` was created to kill.

The tower is a **read-and-render layer** over these sources. It writes nothing back to them.

---

## 1. The one law

**Never render seeded, stale, or unverified data as if it were fact.**

Right now `engine_state.json` `_meta.status` reads `"SEEDED — pre-access placeholders"` and every funnel number is `0` or `null`. A tower that renders those zeros as a live funnel is worse than no tower: it launders placeholders into apparent truth, which breaks the discipline the whole operation runs on (surfaced vs realized never blended; page-verbatim only; verified-claims gate).

Trust-state is therefore a **first-class field on every panel**, not a footnote. Every number the tower shows carries a visible status badge and a source-and-timestamp line. If a source is SEEDED or STALE, the tower says so loudly and does not let the number read as realized.

This law overrides every layout preference below. A blank honest panel beats a populated dishonest one.

---

## 2. Architecture

```
  SOURCES (read-only, owned by their existing writers)
    engine_state.json · impact.json · clay_credit_ledger.csv
    Clay_Build_State_Registry.md · account_plays.json · Readout_Log.md
        |
        v
  ASSEMBLER  (build_control_tower.py)   <-- VS Code builds this
    reads all sources, computes trust-state + staleness per source,
    emits ONE snapshot:  control_tower_state.json
        |
        v
  RENDER  (Control_Tower.html, self-contained)   <-- VS Code builds this
    reads control_tower_state.json, draws the panels, shows badges
        |
        v
  SCHEDULE  (launchd, alongside the existing 3 jobs)   <-- VS Code wires this
    regenerates the snapshot on a cadence + on demand
```

**Boundary that must hold:** the *logic* (motion rules, credit rules, verified-claims, brand) lives in coordinator skills and these source files. The tower only *reads and arranges*. When the tower needs a judgment (is this metric verified? is this claim sendable?), it does not decide; it reads the flag the owning system already set. The brain stays in coordinator; the hands render in VS Code. Do not port skill logic into the tower.

---

## 3. Source read contract

The assembler reads exactly these. Field paths are literal. If a path is missing, the panel shows `— (source field absent)`, never a guessed value.

| Source | Path | Format | Freshness signal | STALE threshold | Owning writer (keeps it fresh) |
|---|---|---|---|---|---|
| Engine state | `gtm-cohesion-layer/engine_state.json` | JSON | `_meta.last_updated`, `_meta.status` | funnel/list_health: 7d; deliverability: 24h | Conductor (weekly), reply-sync agent, deliverability monitor |
| Impact | `impact/impact.json` | JSON | `generated_at` | 7d | impact generator |
| Credit ledger | `clay_credit_ledger.csv` | CSV (append-only) | last row `date`; last row `running_total` + `budget_remaining` | 7d | clay-credit-steward skill (manual append) |
| Clay build state | `Clay_Build_State_Registry.md` | Markdown | `**Last verified:**` line in header | 3d | live Clay sweep (manual, per session) |
| Account plays | `tam-outbound-engine/account_plays.json` | JSON | `generated_at`; per-trigger `date` + `fresh` bool | 3d (signals decay) | TAM engine / war-room |
| Readout log | `Readout_Log.md` | Markdown | last dated line | 7d | naveen-weekly-readout skill |

**Exact fields the assembler pulls** (so the builder does not have to reverse-engineer the JSON):

- **engine_state.json**
  - `_meta.status`, `_meta.last_updated`, `_meta.schema_version`
  - `baseline.one_x_qualified_replies_per_week`, `baseline.ratified_with_naveen`, `baseline.deliverability_floor.{min_open_rate,max_spam_rate,max_bounce_rate}`
  - `list_health.accounts_by_motion.{star_ratings,star_ratings_tier_ab,star_ratings_universe_total,back_office}`, `list_health.contacts_total`, `list_health.contacts_qualified_back_office`, `list_health.contacts_target_back_office`, `list_health.clay_credits_remaining`, `list_health.last_enrichment_refresh`, `list_health.stale_records_over_30d`
  - `funnel.<motion>.{contacts_enriched,messages_sent,delivered,opens,replies,qualified_replies,meetings_booked,meetings_confirmed}` for each motion key present
  - `funnel.targets.{vetted_meetings,qualified_replies_per_week_10x,back_office_contacts}`
  - `deliverability.domains[]` (`domain,status,age_days,daily_cap,sent_today,open_rate,bounce_rate,spam_complaints,blacklisted`, skip rows where `example==true` unless nothing else exists), `deliverability.overall_health`, `deliverability.last_checked`, `deliverability.warm_contacts_protected`
  - `approval_queue.{pending,approved_today,rejected_today,edited_today}`, `approval_queue.items[]` (skip `example==true`)
  - `signals`, `attribution_contract`, `north_star`, `guardrails` (render as-is in a details block; do not interpret)
- **impact.json**: `headline_opportunity_label`, `net_new.{roi_surfaced_label,strike_plans,committee_contacts_mapped,sequence_messages_drafted}`, `net_new.breakdown[]`, `install_base.{accounts_monitored,accounts_with_signal,signals_firing,ae_routes,csm_routes}`, `realized.{logged_outcomes,meetings_booked,pipeline_created_label,revenue_won_label}`
- **clay_credit_ledger.csv**: last non-empty `running_total`, `budget_remaining`; sum of `credits_actual`; group `credits_actual` by a motion tag parsed from `table`/`note` if present (best-effort; if not parseable, show total only and say so)
- **Clay_Build_State_Registry.md**: per motion, the BUILT / PLANNED / BLOCKED status and any line containing `⚠️` (open bugs/blockers) from the Workbooks, Functions, and Workflows tables
- **account_plays.json**: for each account `company,tier,icp_total,why_now_raw,roi_label,fresh`, plus its highest-`score` trigger `{label,play,route_personas,date}`
- **Readout_Log.md**: last line's date, headline, asks, and whether it says `Response: pending`

---

## 4. Trust-state model

Every rendered value inherits a status from its source. The assembler stamps it; the render shows it as a badge.

| Status | Meaning | Trigger | Render rule |
|---|---|---|---|
| **SEEDED** | Placeholder, not real | source `_meta.status` contains "SEED", or value is a documented placeholder (funnel all-zero while sends==0) | Gray value + `SEEDED` badge + "do not trust" tooltip. Never counts toward a realized total. |
| **LIVE** | Real and fresh | freshness signal within threshold | Normal value + `LIVE` badge + "as of <timestamp>" |
| **STALE** | Real but past threshold | freshness signal older than threshold | Amber value + `STALE (Nd old)` badge |
| **REALIZED** | Outcome-backed | comes from a `realized`/attribution field | Green value + `REALIZED` badge. This is the only status allowed in the "Realized" column. |

**Hard rule from house style, enforced here:** surfaced and realized never share a cell, a total, or a color. The Funnel panel has two physically separate columns and they are never summed together.

---

## 5. Assembled snapshot schema (`control_tower_state.json`)

The assembler emits this; the render consumes only this. This is the contract's core artifact. Keep field names exact.

```json
{
  "generated_at": "<ISO8601, injected at runtime>",
  "overall": {
    "posture": "BUILD",                     // BUILD | LAUNCHING | LIVE — derived: BUILD while total messages_sent==0
    "headline": "string",                   // one honest sentence, e.g. "4 motions in build, 0 sends by design, 17% credits used"
    "gates": {
      "deliverability": "GREEN|AMBER|RED|UNKNOWN",
      "credit_budget": "GREEN|AMBER|RED",   // AMBER at 60% consumed (clay-credit-steward rule), RED at 85%
      "baseline_ratified": true
    }
  },
  "motions": [
    {
      "key": "star_ratings",
      "label": "Star Ratings",
      "build_state": "BUILT|PLANNED|BLOCKED",
      "universe": 98, "universe_trust": "LIVE",
      "contacts": 0,
      "funnel": { "sent":0,"delivered":0,"replies":0,"qualified_replies":0,"meetings_booked":0 },
      "funnel_trust": "SEEDED",
      "next_action": "string",              // from account_plays or registry; "—" if none
      "blockers": ["string"]                // ⚠️ lines from the Clay registry for this motion
    }
  ],
  "funnel_surfaced": { "roi_surfaced_label":"$41.6M","strike_plans":6,"messages_drafted":80,"committee_contacts":20,"trust":"SEEDED" },
  "funnel_realized":  { "meetings_booked":1,"pipeline_label":"$180K","revenue_label":"$0","logged_outcomes":2,"trust":"REALIZED" },
  "deliverability": { "overall":"warming","last_checked":"2026-06-24","domains":[], "floor":{}, "trust":"STALE" },
  "credits": { "spent":342,"remaining":4658,"budget":5000,"pct_consumed":0.068,"flag_60pct":false,"cost_per_qualified_reply":null,"trust":"LIVE" },
  "approval_queue": { "pending":0,"approved_today":0,"rejected_today":0,"items":[],"trust":"SEEDED" },
  "signals": [ { "company":"AmeriHealth Caritas","tier":1,"why_now":47.0,"roi_label":"$7.1M","top_play":"string","fresh":true } ],
  "blockers_and_asks": [
    { "type":"blocker","source":"Clay registry","text":"fn_email_verified Send-data-back returns empty result — single-session debug needed" },
    { "type":"ask","source":"Readout 2026-07-17","text":"1x baseline + attribution ratification — Response: pending" }
  ],
  "sources": [
    { "name":"engine_state","last_updated":"2026-07-13","status":"SEEDED","stale":true }
  ]
}
```

---

## 6. Panels (v1 vs v2)

Scoped to what is real **now**: motions in build, zero sends by design, seeded funnel. Do not build a big live-funnel dashboard that renders zeros — that fails the one law and contradicts Dallas's own operating guardrail ("do not build more infrastructure than the live wave needs").

**v1 (build these):**
1. **Header strip** — posture + honest one-line headline + the three gate lights (deliverability, credit budget, baseline ratified).
2. **Motion Board** — one row per motion (star_ratings, cost_mandate, wfm_adjacency, back_office; install_base shown as PLANNED). Columns: build_state, universe, contacts, funnel (badged SEEDED until sends>0), next action, blocker. This is the centerpiece; it is honest today because build-state is real even though funnel is not.
3. **Credit Budget** — spent / remaining / % of 5,000, 60% flag, cost-per-qualified-reply (blank until outcomes; show "awaiting outcomes", never 0).
4. **Deliverability Gate** — green only if every non-example domain meets the floor; gates whether volume may scale. Loud red/amber/green.
5. **Blockers & Asks** — open Clay bugs (⚠️ from registry), baseline-not-ratified, last readout's pending asks.

**v2 (after first live sends exist):**
6. **Funnel (surfaced | realized)** — two physically separate columns, never summed. Flip motion funnels from SEEDED to LIVE as `messages_sent` goes non-zero.
7. **Signals feed** — top N from account_plays, freshness-decayed.
8. **Approval queue** — live once the conductor drafts land in it.
9. **Readout readiness** — mirror of what naveen-weekly-readout will pull Friday, so there are no surprises.

---

## 7. Writers contract (the real dependency)

The tower is only as honest as its sources. Today the biggest gap is that `engine_state.json` is SEEDED and last touched 2026-07-13. The tower does not fix that; it exposes it. Keeping sources fresh stays with their existing owners:

- **engine_state.funnel / list_health** — conductor writes weekly; reply-sync updates funnel. Until live Clay/Salesforce/inbox access is wired, funnel stays SEEDED and the tower must badge it so.
- **engine_state.deliverability** — deliverability monitor; must be < 24h to show GREEN, else the gate reads UNKNOWN/STALE.
- **credit ledger** — clay-credit-steward appends on every run (already the discipline).
- **Clay_Build_State_Registry** — re-verified by live sweep each build session (already the discipline).

The tower should surface source staleness in its `sources[]` block so a stale spine is visible at a glance, not hidden behind confident-looking panels.

---

## 8. Guardrails (non-negotiable)

- **Read-only.** The tower never writes to any source, never sends, never flips a gate, never mutates Clay/Apollo/SF. Dry-run is the state of the world (BFM-5).
- **No number from memory.** Every value traces to a source file read this run, with timestamp (BFM-1). If a source is unreadable, the panel says so; it does not fall back to a prior value.
- **Verified-claims gate travels.** Any Intradiem metric the tower renders in a place that could be shown externally must carry its source; unverified figures render with the `[UNVERIFIED]` marker the repository already uses. The tower does not invent proof points.
- **Brand mode.** Internal operating tool → dallas-brand (blurple/creme). If a variant is ever exported for Naveen/leadership, it switches to official Intradiem brand. Default build is internal.
- **Scope honesty.** While sends==0, the tower's headline says so plainly. It does not dress up a pre-launch build as a running funnel.

---

## 9. Build handoff — what VS Code builds, and acceptance

**Deliverables (in this repo, matching existing patterns like `weekly_ops.py` + `automation/*.plist`):**
1. `build_control_tower.py` — assembler. Reads §3 sources, applies §4 trust-state, emits `control_tower_state.json` per §5. Pure read; no writes to sources.
2. `Control_Tower.html` — self-contained render (inline CSS/JS, no external calls), reads `control_tower_state.json`, draws §6 v1 panels with §4 badges.
3. `automation/run_control_tower.sh` + `com.dallasandrews.gtm.controltower.plist` — regenerate on a cadence (suggest daily, after the 7:15am war-room job) and on demand.
4. Short `README` in a `control-tower/` folder: how to run manually, where the snapshot lands, how to add a source.

**Acceptance criteria:**
- Running the assembler against the current SEEDED state produces a tower where **every funnel number is badged SEEDED**, the headline says sends are 0 by design, credits read 342 spent / 4,658 remaining, and the Clay `fn_email_verified` bug appears under Blockers. If any seeded zero renders as a plain LIVE number, it fails.
- The deliverability gate reads STALE/UNKNOWN (last_checked 2026-06-24 is well past 24h), not GREEN.
- Baseline-ratified gate reads false (matches `engine_state.baseline.ratified_with_naveen`).
- No source file is modified (git diff on sources is empty after a run).
- Opening the HTML with no server shows the panels (self-contained).

**What VS Code must NOT do:**
- Do not rebuild any coordinator skill (war-room, readout, launch-kit, objection handling). The tower reads their outputs; it does not re-implement them.
- Do not hardcode any metric into the HTML (that recreates the drift the two SF mockups have). Every value comes from `control_tower_state.json`.
- Do not add write-back, send, or Clay-mutation capability "for convenience."
- Do not run two agent sessions editing Clay concurrently (documented cause of garbled fixes in the registry).

---

## 10. Reconciliation with the existing mission-control dashboard

A personal command center already exists: `mission-control.html` (built 2026-06-23, expanded to 13 panels 2026-07-02; artifact id `dallas-mission-control`). Do not duplicate it. The two are different surfaces:

- **mission-control.html** = Dallas's inward/personal layer: relationship health, promise ledger, asks-of-Naveen, onboarding, gates with hard dates, outside-reads sensor. STATE is seeded + localStorage, updated by hand.
- **Control Tower** = the outward GTM-machine layer: motion build-state, funnel, credits, deliverability, blockers, read live from the source files.

They overlap on **credits** and **gates**. mission-control's own footnote already says `engine_state.json` is the single source of truth post go-live. So the correct relationship is: the Control Tower owns the live read of engine_state/ledger/deliverability and emits `control_tower_state.json`; mission-control should later bind its credit and gate panels to **that snapshot** instead of its own seeded STATE, so the two never drift. Until that rebind happens, the Control Tower is the authority for anything read live from source, and mission-control stays the authority for the personal/relationship layer it uniquely holds. Do not copy credit or gate logic into a second renderer.

---

## 11. One open decision for Dallas

Refresh model. Recommendation: **static snapshot regenerated by launchd** (assembler writes `control_tower_state.json`, HTML reads the file, cron regenerates daily + on demand). It matches the existing automation pattern, needs no running server, and opens anywhere. The alternative (a live local server reading sources on each page load) is more moving parts for no real gain while the funnel is still seeded. Build static now; revisit a live server only if you later want intra-day refresh during active sends.
