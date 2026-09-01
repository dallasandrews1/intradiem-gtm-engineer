# Agent Registry — Dallas's Autonomous GTM Swarm

Single source of truth for every agent, scheduled job, workflow, and cloud routine working for Dallas. Lives in the coordinator so it travels with every workspace. Update this file whenever an agent is added, retired, loaded, unloaded, or rewired.

Last reconciled against the live system: 2026-07-27 (launchctl list cross-check; the 2026-07-19 status column had gone stale, 7 jobs marked "LOAD PENDING" were actually already loaded).

Five governing rules for anything in here:
1. **Nobody but Dallas.** (Standing as of 2026-07-19.) Nothing in this swarm messages, routes, DMs, emails, or posts to anyone but Dallas himself. No AE, CSM, prospect, rep, or third party. Any job with an external send path stays in dry-run / preview-only until Dallas explicitly lifts this. A proposal that would notify a third party is dead on arrival.
2. **Single morning brief.** The `gtm-daily-rundown` (weekdays 7:50, one Slack DM) is the ONLY automated morning ping. Every other job does its work and writes a LOG; the rundown reads the logs and consolidates. Nothing else DMs Dallas independently.
3. **Read-only by default.** No agent flips a send gate, spends credits, or runs a wave without an explicit ask.
4. **Log, don't notify.** A new notification-producing job wires its output as a source the rundown reads.
5. **Chain the logs.** (Standing as of 2026-08-03.) Per `Intradiem GTM Engineer/automation/LOG_CONVENTION.md`: a log item another job might act on mints an `evt:` id at first surfacing; anything produced because of an upstream item cites it with `chain:`. Ids live in logs only, never in the rundown DM or anything Naveen- or prospect-facing. Every new agent spec inherits this.

---

## 1. Scheduled autonomous jobs (launchd, local — fire on their own)

These run without a prompt. All live in `Intradiem GTM Engineer/automation/` unless noted.

| Job (launchd label) | Schedule | What it does | Writes to | Status |
|---|---|---|---|---|
| `com.dallasandrews.gtm.warroom` | Weekdays 7:15 | Signal scan across the target universes (32 Stars parents, back-office list, named accounts); ranks Priority 1-4, maps each to a play | `automation/logs/war-room-YYYY-MM-DD.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.agentarchitect` | Weekdays 7:35 | Studies the swarm + live GTM work, proposes 2-4 new agents into the ledger (after war room lands, before rundown reads it) | `automation/logs/agent-architect-*.md` + `[AGENT]` entries in `proposal_ledger.md` | **LOADED** (2026-07-19) — muted into the rundown |
| `com.dallasandrews.gtm.dailyrundown` | Weekdays 7:50 | Composes the ONE ranked morning Slack DM from all logs; seeds the proposal ledger | Slack DM + `daily-rundown-*.md` | **LOADED** — the only morning ping |
| `com.dallasandrews.gtm.creditcheck` | Thursday 7:00 | Live Clay credit balance + cost-per-motion + receipts | `automation/logs/credit-check-*.md`, `credit_pipeline_receipts.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.fridayreadout` | Friday 6:00 | Drafts the Naveen weekly manager readout | `automation/logs/naveen-readout-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.meetingcapture` | Weekdays 7:05 | Scans Otter for new transcripts, drafts follow-ups, flags meetings with no record | `meeting-capture-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.pmoextractor` | Weekdays 7:25 | Read-only action-item extractor for the Product "AI enabled PMO" goal (Monday item 12664120782): reads Otter, Outlook mail + calendar, and the Monday AI Initiatives board, appends `automation/pmo/action_register.csv` and `validation_queue.csv` (verdict blank, Dallas grades), reports precision from graded rows | `pmo-actions-*.md` | **LOADED 2026-08-31** — muted into the rundown (source 12) |
| `com.dallasandrews.gtm.syncpublish` | Daily 21:30, plus a SessionEnd hook on every Claude Code session (throttled 10 min) | Two-machine sync publisher, pure bash, no Claude call: `sync.sh export`, commit `coordinator/` when more than the manifest changed, fast-forward or clean-tree rebase from origin, push main, then report uncommitted or unpushed work across the main checkout and every worktree | `sync-publish-*.md` | **LOADED 2026-08-31** — muted into the rundown (source 13); work Mac half is `automation/sync_work_mac.sh start|end` via that machine's hooks, no launchd there |
| `com.dallasandrews.gtm.swarmheartbeat` | Weekdays 7:45 | Pure-bash check that each job fired and its log landed; rundown leads with it | `swarm-health-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.gateintegrity` | Monday 7:20 | Weekly customer-leak backstop, reads REAL Clay rows (also on-demand before a wave). **Recommend re-pointing this slot at the `gate-integrity-fanout` workflow below** (parallel fan-out + adversarial re-verify, ~11 min vs serial, caught a real confirmed leak on its first live run 2026-07-27) instead of the serial `gate-integrity-auditor` subagent | `gate-integrity-*.md` | **LOADED** — muted into the rundown; still runs the OLD serial subagent until re-pointed |
| `com.dallasandrews.gtm.pipelinereceipts` | Thursday 7:20 | Weekly renewal-receipts summary, ready for the Friday readout (also on-demand) | `pipeline-receipts-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.deliverabilitywatch` | Monday 7:10 | Weekly mailbox-warmth / deliverability-gate watch | `deliverability-watch-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.competitorwatch` | Wednesday 7:10 | Weekly displacement briefs built from the war-room logs (no web re-scan) | `competitor-displacement-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.starsrefreshwatch` | Monday 6:40 | Weekly CMS Stars-release watch; stages the October refresh when it lands. Extended 2026-08-07 with the committee-coverage-gap rank: Tier A+B parents with zero/partial buying-committee coverage, ranked by addressable forgone QBP, as the priority queue for Dallas's manual SalesNav pulls (27 of 32 uncovered at build) | `stars-refresh-watch-*.md` | **LOADED** — muted into the rundown |
| `com.dallasandrews.gtm.tablehygiene` | Weekdays 6:50 | Sweeps target tables for redundant/orphaned/ID-rotted columns; produces safe-delete plans (dependents + re-point map + order) | `table-hygiene-*.md` | **LOADED 2026-08-03** (plist copied to `~/Library/LaunchAgents`, `launchctl list` confirmed exit 0; first fire next weekday 6:50) |
| `com.dallasandrews.gtm.alumniwatch` | Tuesday 7:15 | Weekly job-change watch, upgraded 2026-08-07 to salesnav-alert-triage: primary surface is SalesNav alert emails in Outlook (M365 MCP), fallback is the original WebSearch slice; cross-matches ALL live rosters (alumni, UK named accounts, Stars committee, Keegan TAM), not alumni only. Extended 2026-08-15 with committee-seat-integrity-watch: also cross-matches the ~28 leadership-visible seats in the ICP Buying Committees payload (`Committee Hover Cards - Aug 10.json`); a hit there is automatic P1 `COMMITTEE-SEAT-STALE` | `automation/logs/alumni-*.md` | **LOADED** — upgraded 2026-08-07, extended 2026-08-15; alert surface conditional on M365 MCP auth in headless runs (logs BLOCKED + falls back cleanly), on Dallas's hand-made SalesNav saved-search alerts, and on the Keegan alumni CSV |
| `com.dallasandrews.gtm.rundownthreads` | Every 600s | Rundown thread listener; ingests DONE/SKIP/HOLD/CONFIRM replies into `rundown_thread_state.json` | `automation/logs/rundown-thread-*.md` | **LOADED 2026-08-03** — muted into the rundown; registered 2026-08-06 |
| `com.dallasandrews.gtm.lemlistrelay` | Hourly (:10) | Lemlist relay + brief-thread ingest; polls campaign/reply state and the rep brief threads. Rebuilt MCP-first 2026-08-15: the trial ended Aug 13 and REST /api/activities went plan-gated (only /api/tasks survives), so replies now come from the lemlist MCP inbox/stats tools with a loud `BLOCKED-PLAN-GATE` line if neither surface is available | `automation/logs/brief-thread-ingest-*.md`, `.lemlist-relay-stats.json` snapshot | **LOADED 2026-08-01** — muted into the rundown; registered 2026-08-06; MCP-first 2026-08-15 |
| `com.dallasandrews.gtm.actionbrief` | Daily 2:20, 3:20, 7:30 | Per-rep Daily Action Brief composer (replies to draft, tasks to run, autopilot sends in full) posted to rep channels; gated by `live` flag in `automation/config/action_brief.json` | `automation/logs/action-brief-*.md` | **LOADED 2026-08-15** (was built-but-unregistered); `live=false`, DRY RUN until Dallas flips it |
| `com.dallasandrews.gtm.contextbus` | Weekdays 12:30, 17:00, 21:00 | Publishes the cross-laptop context drop: memory delta, changed assets, and distilled human sessions (skips the 400+ `sdk-cli` swarm transcripts), then Claude writes the digests and rewrites `INBOX.md` and it pushes to the private `dallasandrews1/context-bus` repo the work Mac pulls | `automation/logs/context-bus-*.md` + `~/context-bus` (git push) | **LOADED 2026-08-06** — muted into the rundown; never DMs |
| `com.dallasandrews.gtm.controltower` | Daily 7:30 | Renders the control tower from `engine_state.json` | control tower HTML | **plist exists, NOT LOADED** — intentionally held until the registry re-stamp post WFM-Adjacency fix |
| `com.intradiem.signals.daily` | Daily 7:00 | Signal-engine L2 intent scorer; `run_daily.sh` runs the notifier as DRY-RUN ONLY (writes a digest, sends nothing) | `intradiem-signal-engine/logs/digest_*.txt` | **plist exists, NOT LOADED** — keep the notifier dry-run; do NOT flip to `--send` (Rule 1: nobody but Dallas) |

> Reconcile check: run `launchctl list | grep -iE "gtm|intradiem"`. As of 2026-07-27, all 12 `com.dallasandrews.gtm.*` jobs show up loaded (warroom, dailyrundown, creditcheck, fridayreadout, agentarchitect, meetingcapture, swarmheartbeat, gateintegrity, pipelinereceipts, deliverabilitywatch, competitorwatch, starsrefreshwatch). Only `controltower`, `tablehygiene`, and the `com.intradiem.signals.daily` cloud/local routine remain unloaded. To activate a held job: copy its plist into `~/Library/LaunchAgents/` if it isn't there yet, then `launchctl load <path-to-plist>`. **DECIDED 2026-07-27: these are personal-Mac-only, permanently.** None of this scheduling exists on the work MacBook (IntradiemDA), and it stays that way, Dallas confirmed on-demand-only for that machine to avoid double-firing the single-morning-brief rule (two Slack DMs, two war-room scans). The work laptop's role is Clay UI plus ad hoc Claude Code sessions, never a second scheduling home.
>
> **Context bus, and why it does not break the rule above (2026-08-06).** `com.dallasandrews.gtm.contextbus` is the personal-Mac publisher only. The work Mac's half is `~/context-bus/bin/ingest.sh`, run **by hand**, pull-only, and it is deliberately NOT a launchd job there, exactly per the Jul 27 decision. The bus is one-directional in its automated half: the personal Mac pushes, the work Mac only ever pulls, nothing auto-uploads from the work machine. Reverse transfers use `~/context-bus/bin/handoff.sh`, which makes no Claude call at all so it still works when the Enterprise account's usage is exhausted, which is the exact moment it is needed.
>
> **Firing reality (verified 2026-07-19, Sunday):** all five jobs show `runs = 0` in `launchctl print`. This is CORRECT, not a failure — they were loaded Fri Jul 17 afternoon and Sat/Sun have no weekday schedule, so no scheduled window has passed yet. First real unattended fire is **Mon Jul 20**. Proof it worked: dated logs (`war-room-2026-07-20.md`, `daily-rundown-2026-07-20.md`) appear after ~8am Mon. Until a job has fired once, we have loaded-not-proven, not proven-working. Do not re-flag `runs = 0` as a bug without first checking the calendar against the load date.
>
> **Wake / sleep reality (corrected Jul 19):** the Mac sleeps after 1 min idle. A repeating power-on wake is set (`pmset repeat wakepoweron MTWRF 05:55`, confirmed) BUT this alone does NOT make the 6:00-7:50 jobs fire on time — the Mac wakes at 5:55, idles, and sleeps again by ~5:56, so jobs whose time passes while it's asleep are deferred by launchd and run (coalesced) at the next wake, i.e. when Dallas opens the laptop. So today's real behavior is FIRE-ON-OPEN: the morning jobs run shortly after Dallas starts his day, not at the wall-clock minute. RESOLVED (Jul 19): Dallas keeps the Mac plugged in, lid open, so the fix is `sudo pmset -c sleep 0` (never system-sleep on AC). With that set the Mac stays awake overnight and every morning job fires at its exact scheduled time; the 5:55 wake remains as a harmless safety net. Undo never-sleep with `sudo pmset -c sleep 1` (or any minutes), undo the wake with `sudo pmset repeat cancel`.

---

## 2. On-demand subagents (delegated workers, `.claude/agents/`)

Mirrored in both `~/.claude/agents/` and `coordinator/.claude/agents/`. Invoked by delegation, not scheduled. A session restart is needed before a newly added subagent is invocable.

| Agent | Job | Reads | Writes | Guardrail |
|---|---|---|---|---|
| `clay-operator` | Clay build + enrichment specialist; inspects tables, runs/extends existing workflows/functions | Clay MCP + CLI | Clay (config only) | Never flips a send gate |
| `credit-strategist` | Credit + motion-ROI judgment; Run/Hold/Kill per motion weighted to early wins | `clay credits`, credit logs, registry | rundown log | Read-only, never spends |
| `gtm-copy-reviewer` | Adversarial copy QA against the verified-claims + CTA/voice gates | copy files | verdict | Read-only, never sends |
| `signal-researcher` | Read-only web research, fan-out per account/motion for war room + signal plays | web | structured findings | Never writes live pipeline |
| `agent-architect` | Proposes NEW agents by studying what Dallas does across Claude/Cowork/Code | this registry, memory, skills, logs | proposal ledger `[AGENT]` tags | Read-only, proposes never builds |
| `reply-triage` | Classifies an inbound reply and drafts a peer-level reframe in the rep's voice (registers Reply Engine v1 + objection-handler skill) | reply text + account research | draft (returned) | Read-only, never sends |
| `gate-integrity-auditor` | Reads REAL rows via Clay to prove no current customer can reach a cold send and shared gates still hold; run before any wave | live Clay motion tables, SF exclusion list | verdict (returned/log) | Read-only, real-rows-only, never edits a gate |
| `pipeline-receipts-tracker` | Credits-in vs qualified replies/meetings-out per motion for the renewal case; run before the Friday readout | credit_pipeline_receipts.md ledger, credit ledger | receipts summary (returned/log) | Read-only, surfaced vs realized never blended |
| `meeting-capture` | Otter transcript capture, follow-up drafts, missing-record flags (also scheduled weekdays 7:05) | Otter, calendar/notes | draft + log | Read-only, drafts never sends |
| `pmo-action-extractor` | Action items with owner, due, verbatim evidence from notes, mail, calendar, Monday; dedup; validation queue for accuracy grading (also scheduled weekdays 7:25) | Otter, M365 mail + calendar, Monday board 18418380280 | `automation/pmo/*.csv` + log | Read-only, never sends or creates tasks; follow-up automation gated on graded precision |
| `deliverability-watch` | Mailbox-warmth / deliverability-gate watch (also scheduled Mon 7:10) | `deliverability_status.md` (Nathan's mailbox, hand-mirrored from Clay Campaigns) | log | Read-only, never flips gate |
| `competitor-displacement-watch` | Displacement briefs from war-room competitor mentions (also scheduled Wed 7:10) | war-room logs | briefs + log | Read-only, internal only |
| `stars-refresh-watcher` | Watches CMS for the Stars release, stages the October refresh (also scheduled Mon 6:40) | CMS web, october-refresh-runbook | log | Read-only, stages never runs universe |
| `table-hygiene` | Flags redundant/orphaned/ID-rotted columns + the safe-delete re-point plan (also scheduled weekdays 6:50) | tables in table_hygiene_targets.md | log | Read-only, never deletes/edits a column |
| `lemlist-lead-integrity` | Pre-send integrity sweep of loaded lemlist leads: wrong-company emails that never bounce, misrouted leads, unrendered `{{variables}}`, silently-failed enrichment batches, leftover TEST rows. Run before any wave launch | lemlist campaigns/leads (read tools) | verdict (returned) + `lemlist-integrity-*.md` | Read-only, never enriches, never spends a credit, never sends |
| `salesnav-csv-intake` | Ingests a hand-pulled SalesNav CSV from `automation/inbox/salesnav/` (or a named path), identifies the owning roster, fills named gaps, dedups, enforces existing gates (Director+ for back-office), writes the roster diff, logs the coverage delta. Built 2026-08-07 | dropped CSV + live roster files | target roster (diff in place) + `## SalesNav intake` section in `pipeline-receipts-*.md` | Never touches SalesNav/LinkedIn itself; stops at the roster file, never loads Clay/lemlist, never spends, never invents a gate rule |
| `icp-committee-page-builder` | Stamps expansions/recasts of the ICP Buying Committees site (the Aug 13 leadership-hit deliverable): sources the committee, builds the payload delta, runs the strict customer-exclusion gate on net-new accounts, regenerates + headless-render-verifies, stages the deploy command. Built 2026-08-15 off three expansion asks in the deliverable's first 10 days | payload JSON, `Active_Customers_SF_Jul10.csv`, Apollo/Clay photo playbook, web seat-verification | staged files under `deploy-icp-committees/_staging/` + handoff note | Never runs `wrangler pages deploy`, never edits live `index.html` in place; ambiguous customer status (US Bank/Elavon pattern) flagged never decided; recursive payload walk mandatory (retail_variant trap) |

> `reply-triage` stays on-demand only: to fire autonomously it needs an inbox source to watch (Gmail/Outlook MCP + a reply-detection step), which isn't wired yet. Build that when reply volume justifies it; until then paste the reply in.

---

## 3. Multi-agent workflows (run on demand, `.claude/workflows/`)

| Workflow | What it does |
|---|---|
| `gtm-proposal-sweep.js` | Read-only fan-out that surfaces strategy proposals into the proposal ledger (phase-2 embryo of the orchestrator loop) |
| `war-room-fanout.js` | Parallel account-level signal research feeding the war room |
| `motion-workflow-build.js` | Stamps a new motion's send-readiness workflow from the proven template |
| `gate-integrity-fanout.js` | Fan-out + adversarial-verify upgrade of `gate-integrity-auditor`: one agent per live motion table checks customer-exclusion on REAL rows, any leak found gets independently re-verified before it's reported. Read-only, never edits a gate/row, never spends beyond a live-row read. First live run (2026-07-27) confirmed real leaks in Stars and WFM-Adjacency; see `gate-integrity-report-2026-07-27.md` in memory. Recommended to replace `gate-integrity-auditor`'s Monday 7:20 scheduled slot |

---

## 4. Cloud routines (server-side, cross-session)

| Routine | Schedule | What it does | Note |
|---|---|---|---|
| Mem0 catch-up (`trig_01Ho4bZLRiE15M4xkyga5QWu`) | Daily 6:00 CT | Detects 48h of Mem0 silence and Slacks Dallas | Predates the single-brief rule and DMs directly; candidate to fold into the rundown |

---

## How the pieces connect

```
7:00  signal-engine (if loaded) ──┐
7:15  war room ────────────────────┤
7:00 Thu  credit check ────────────┼──> logs/ ──> 7:50 daily rundown ──> ONE Slack DM
6:00 Fri  friday readout ──────────┤              (reads every log,
7:30  control tower (if loaded) ───┘               computes deltas,
                                                    seeds proposal ledger)

on-demand: clay-operator · credit-strategist · gtm-copy-reviewer ·
           signal-researcher · agent-architect  (+ workflows above)
```

The daily rundown is the hub. Everything upstream writes a log; the rundown is the only thing that speaks.

## Addendum 2026-08-20: Clay read path re-pointed to the CLI (headless access fix)

The Clay MCP plugin tools `mcp__plugin_clay_clay__table` / `__read` / `__surfaces_*` that `gate-integrity-auditor`, `table-hygiene`, `credit-strategist`, and `pipeline-receipts-tracker` listed in their `tools:` line no longer exist (plugin 2.6.0 ships skills plus the `clay` CLI 0.5.0, no MCP tools). That is why gate-integrity and table-hygiene failed headless Aug 17-20. All four agent defs (both copies, `~/.claude/agents/` and `~/coordinator/.claude/agents/`) now read Clay through the CLI only: `clay tables rows list/get`, `clay tables columns get/list`, `clay tables get`, `clay audiences records ...`, `clay credits`, with the binary resolved as `command -v clay || newest ~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay` because launchd PATH is not guaranteed. Row JSON is parsed with `automation/lib/clay_rows2tsv.py` (`json.loads(strict=False)`) because some tables carry raw control characters that break `jq`. Verified interactively 2026-08-20: 524 WFM L3 rows read in 17 s, 143 Stars Contacts rows read, 0 credits (action-execution balance only).

`gate-integrity-auditor` gained check 7: the customer-exclusion UNION (SF Audiences segment `audseg_0tk324emMVGAwsna7g4` Customer or Partner + install-base table `t_0ti4jj1hfZyEWcfirfU` + `tam-outbound-engine/config/customer_denylist.json` + motion L1 `customer_flag=TRUE`) is checked against every live send table's own customer flag, with a new GATE INERT verdict class for rows the union says are customers but the table's own flag says are not, even while HOLD. Salesforce Account Type alone is not sufficient (Elevance Health and TD Bank absent from the synced set; Cigna, Assurant, Farmers, McKesson, Citi, British Gas tagged Prospect).

`pipeline-receipts-tracker` may read Salesforce deals via `clay audiences records --entity-type deals` as a CANDIDATE surfaced-pipeline source only; counted receipts still come only from `credit_pipeline_receipts.md` and `impact/outcomes.csv`.

Guardrail unchanged on all four: read-only, never `clay update`, never touch the plugin install, never spend.

## partner-briefs-loop (scheduled, hourly :20 weekdays)
Watches #gtm-partner-briefs for account-name requests from the partner team (Frank Ciccone first), runs the briefing engine per request (gate from local SF/pre-pipeline/denylist files, signal-researcher fan-out, Clay free path 0 credits, build_briefs.py, partner-safe deploy only), replies in thread with links. DRY RUN until "live": true in automation/config/partner_briefs.json. Wrapper: automation/run_partner_briefs.sh. Log: automation/logs/partner-briefs-<date>.md (rundown source). Inherits governing rules 1-5: never DMs Dallas, logs with evt anchors, no sends, no credit spend beyond the free path, internal pages never deployed. Added Sep 1 2026.
