# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is Dallas Andrews' working directory for the **GTM Engineer** role at Intradiem (started Jul 6 2026, reports to Naveen Thilagan). It is not a single application - it's a mix of:

1. **Runnable Python "engines"** that score accounts and generate GTM plays (the actual code).
2. **A hosted platform** (FastAPI brain + Slack bot + Claude plugin) that exposes those engines to sellers.
3. **Claude Agent Skills** (`SKILL.md` files) that encode repeatable GTM workflows.
4. **A large body of markdown/HTML/CSV** - strategy docs, dashboards, target-account lists, and interview-era artifacts - that are content, not code. Don't try to "build" or lint these; read them for context when a task touches the business logic they describe.

Start with `_START_HERE_Index.md` for the current operating context and read order. Files under "Superseded" in that index are interview-era and should not be treated as current instructions.

## The core engines (where the real logic lives)

Three independent, config-driven Python engines, each with the same shape: a `data/` folder you swap for real exports, a `config/` folder you tune (never hardcode thresholds/logic in the `.py`), and a script that prints JSON or writes an output file another surface reads.

### `intradiem-signal-engine/` - install-base expansion & risk signals
- Run: `python3 signal_processor.py` (summary), `--domain X` (one account), `--output data/signals.json` (feed dashboard), `--suppress` (apply 14-day suppression window)
- Test: `python3 test_signal_processor.py` (14 checks)
- Six signals (seat_utilization, coaching_coverage, rule_engine_active, crm_not_connected = expansion → routes AE/CSM; automation_volume_drop, champion_job_change = risk). Routing priority: AE > CSM > HOLD.
- Swap-in data lives in `data/accounts.csv`; thresholds/routes/suppression window live in `config/thresholds.json`.
- `intradiem_mcp_server.py` exposes the same engine as MCP tools (`get_expansion_signals`, `list_monitored_accounts`, `score_all`, `add_monitored_account`).
- `notifier.py` routes firing signals to the owner in `data/owners.csv` - dry-run by default, `--send --channel slack` needs `SLACK_BOT_TOKEN`.
- `run_daily.sh` chains score → refresh dashboard → notifier dry-run digest; scheduled via the included launchd plist (`com.intradiem.signals.daily.plist`) at 7am, or cron as a fallback.

### `tam-outbound-engine/` - net-new account scoring & strike plans
- Run: `python3 account_engine.py` (ranked list), `--plan <domain>` (full strike plan), `--top N`, `--output account_plays.json`
- Test: `python3 test_account_engine.py` (21 checks)
- Fit score (0-100) = industry + contact-center scale + tech stack + pain (pain derives from trigger strength/freshness; triggers decay from full weight inside 30 days to a floor past 120 days). ROI is computed per account from agent count via `config/roi_model.json`.
- Data: `data/tam_accounts.csv` (firmographics), `data/triggers.csv` (buying triggers), `data/sellers.csv` (ownership).
- Config: `config/icp_weights.json` (fit scoring), `config/triggers.json` (the trigger→persona taxonomy - this is the moat), `config/personas.json`, `config/sequences.json`, `config/roi_model.json`.
- `tam_mcp_server.py` exposes `list_strike_accounts`, `get_strike_plan(domain)`, `accounts_for_seller(email)`.
- `tam_notifier.py` - same dry-run/`--send --channel slack` pattern as the signal engine's notifier.
- **All dollar/ROI figures generated here are self-labeled placeholders, not verified Intradiem numbers** - see Verified-claims discipline below before anything reaches prospect-facing copy.

### `impact/` - the ELT scorecard
- Run: `python3 impact_engine.py` / `--output impact.json`
- Reads outputs of the other two engines (`../intradiem-signal-engine/data/signals.json`, `../tam-outbound-engine/data/tam_plays.json`) plus `./outcomes.csv` (real results you append: `date, account, type, value, note`).
- Keep **"opportunity surfaced"** (estimated, from the engines) and **"realized"** (only from `outcomes.csv`) separate - never blend them into one number.

### `gtm-cohesion-layer/` - the orchestrator tying the three engines together
- `conductor.py` is the weekly-push orchestrator: Refresh → Re-score → Scan signals → Draft → Approve(HUMAN) → Send(gated) → Instrument. Calls the three engines above read-only/best-effort (a missing engine logs "skip", never poisons the run).
- `conductor.py --preflight` runs every go-live assertion (attribution ratified, baseline set, deliverability green, engine contracts intact, security cadence current, WIP sane) and must print **READY** before `DRY_RUN` is flipped to `False`.
- `engine_state.json` is the single source of truth every dashboard (`control_tower.html`, `attribution_dashboard.html`, `approval_queue.html`, `variant_tracker.html`, `deliverability_monitor.html`) reads and the conductor writes. Don't let a dashboard hold its own duplicate state.
- Design principles baked into the conductor (treat as non-negotiable when editing it): **fail-closed** (a stage error stops the run, never silently sends), **human gate** before any send, **deliverability gate** (send stage skipped unless green), **measurement before volume**.

## `gtm-hosted-platform/` - "one brain, many surfaces"

The principle: the owner (Dallas) owns the brain (engines + config + data); sellers only get a thin, read-only surface (Slack or Claude plugin) that cannot alter thresholds, triggers, or copy.

```
Slack app ─┐
Claude plugin ┼──> brain/app.py (FastAPI, hosted)  ──> the two engines + impact
Salesforce (v2) ┘        auth (X-API-Key) + request log (brain/logs/requests.jsonl)
```

- **Brain** (`brain/app.py`): FastAPI service. `docker build -f gtm-hosted-platform/brain/Dockerfile -t intradiem-gtm-brain .` from the **project root** (engine folders must be in build context), or `pip install -r requirements.txt && uvicorn app:app`. Auth via `GTM_API_KEYS` env var (`label:key` comma list - one key per surface so the log shows which surface drove usage). Endpoints: `/v1/strike`, `/v1/strike/{domain}`, `/v1/signals`, `/v1/signals/{domain}`, `/v1/impact`, all requiring `X-API-Key`.
- **Slack** (`slack/slack_app.py`): Socket Mode app, `/strikeplan [domain]` slash command, calls the brain via `BRAIN_URL`/`BRAIN_API_KEY`.
- **Claude plugin** (`plugin/intradiem-gtm/`): remote (URL + key in `.claude-plugin/plugin.json`) by default; `mcp/gtm_client.py` is the local-stdio fallback if the brain can't be exposed over the network. Ships `RULES_OF_THE_ROAD.md` and a bundled skill (`skills/strike-plans/SKILL.md`) that always carries the verify-before-send guardrail.

## Claude Agent Skills (top-level `SKILL.md` folders)

`intradiem-signal-to-play/`, `intradiem-competitive-intel/`, `intradiem-content-engine/`, `intradiem-roi-business-case/` are Claude Agent Skills, invoked by trigger phrases described in their frontmatter `description`. When editing one, keep the frontmatter `description` field packed with the trigger phrasing - that's what makes the skill auto-load. They all share the same scope reminder: Intradiem sells Dynamic Workforce Orchestration across **contact centers AND back offices**, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities) - never frame it as just a "call center" tool.

## Verified-claims discipline (applies everywhere prospect-facing copy is generated)

`VERIFICATION_AUDIT.md` is the standing audit of this rule and is worth rereading before touching any engine that generates outbound copy. The rule: only figures confirmed in the Intradiem Value Repository (the `intradiem-verified-metrics` skill - lives outside this repo, in the environment-only value-repository) may be presented as Intradiem-verified. Concretely:
- Anything generated by `tam-outbound-engine`'s ROI model, `config/roi_model.json`, `config/proof.json`, or `engine_state.json` seeded/example values is a **placeholder assumption**, not a verified customer or company number - never let it read as Intradiem-confirmed in prospect-facing copy.
- Peer/customer outcome claims must exist in the Repo with source; never invent or paraphrase one into something stronger than its source.
- Mark anything unconfirmed as `[UNVERIFIED]` rather than silently including it.
- This is why the cohesion layer's Stage 4b "critic" gate and the plugin's "verify before send" guardrail exist - don't bypass or remove them when editing the conductor or the plugin skill.

## Brand

**Current kit (Jul 30 2026). This SUPERSEDES `intradiem-brand-kit.md`, which is history.**
Canonical spec: `~/coordinator/memory/intradiem-brandkit-current-jul30.md`. Reference
implementations in this repo: `dwo-html-deck/` (all three files).

- **Type:** Roboto (400/500/700/900) for body and display, headlines at weight 900 with
  `letter-spacing: -.02em`. Roboto Mono (500/600) for eyebrows, labels and table headers,
  uppercase. NOT Playfair Display, NOT DM Sans, NOT JetBrains.
- **Core tokens:** `--forest:#014637` `--green:#2DB56E` `--green-600:#228752`
  `--green-300:#7BD3A0` `--orange:#F58220` `--ink:#202020` `--sidebar:#F5F4F2`
  `--line:#E0E0E0`, radius 8px.
- **Signature moves:** forest hero surfaces with a radial green glow; eyebrows in green
  (green-600 on light, green-300 on dark); **orange `#F58220` is the action/priority
  accent only**, never a body color; forest statbands with green-300 numerals; `.gate`
  (green left border) versus `.callout` (orange left border) carrying the safe-versus-caution
  convention.
- **Logo:** the official mark as an inline SVG `<symbol id="ilogo" viewBox="0 0 187 46">`.
  Copy it verbatim from `dwo-html-deck/DWO_Deck_Update_Guide.html`. Wordmark paths use
  `currentColor`, so set it to `#014637` on light and `#FFFFFF` on dark heroes. Never ship
  an Intradiem deliverable with no logo.
- **Anti-patterns that shipped once and must not repeat:** improvised ASCII glyphs standing
  in for icons, hand-picked off-token greens, and a deliverable with no logo anywhere.

`#FE5000` was the older kit's primary and is **retired**. If you find it in a file, that file
predates Jul 30 2026 and should not be used as a style reference.

Do not use the personal `dallas-brand` blurple/creme palette on Intradiem-context work; that
kit is for Dallas's internal personal work only.

## Working conventions specific to this repo

- **Config over code.** Every engine is explicit that thresholds/weights/copy belong in `config/*.json`, not hardcoded in the `.py` files. When asked to change scoring or routing behavior, edit config first and only touch the engine script if the config schema itself needs to change.
- **Dry-run by default.** Both notifiers (`notifier.py`, `tam_notifier.py`) and the conductor (`DRY_RUN = True`) default to preview-only. Never flip a script to actually send (`--send`, `DRY_RUN=False`) without the user explicitly asking for it - these hit Slack/email/prospects.
- **Data swap points are documented per engine** (see each engine's README) - when asked to "go live" with real data, that means replacing the named CSVs, not changing engine logic.
- **`_archive/` is historical** (old HTML mockups, a stray `.tmp`/lockfile) - don't treat it as current unless the user points there specifically.

## Mem0 sync discipline (Cowork sessions especially)

Dallas keeps a persistent memory system in a separate `coordinator` project (`~/coordinator/memory/*.md` + Mem0 cloud, `user_id=dallasandrews`, `app_id=coordinator`). This repo is where most of the actual GTM work happens, so it's also where memory sync most often gets missed.

**If you are a Cowork session:** there is no automatic hook here — the Claude Code CLI plugin that auto-syncs to Mem0 does not run inside Cowork. You must proactively call the Mem0 connector tool (`add_memory`, `user_id=dallasandrews`, `app_id=coordinator`, `infer=false`) yourself, in the same turn as any material decision, build, status change, or piece of feedback from Dallas — don't wait to be asked. This already failed once (a full week, Jul 11-17 2026, went uncaptured because no session remembered to do this — see the `mem0-sync-gap-jul17` memory) so treat this as load-bearing, not optional.

**If you are a Claude Code CLI/VS Code session:** the global Mem0 plugin hook covers you automatically; no action needed beyond normal use.

A daily scheduled task also runs as a safety net in case a live session skips this (see `mem0-sync-gap-jul17` for why the net exists) — it is not a substitute for syncing live when you can.
