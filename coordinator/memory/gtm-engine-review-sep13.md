---
name: gtm-engine-review-sep13
description: "Sep 13 2026 full-stack review + pre-mortem; verdict = strong build, broken throughput loop (0 replies, 215 leads parked at LinkedIn manual steps, 99 open rep tasks, 1,707 loaded never launched); campaign-scorecard built and chained hourly; page at gtm-engine-review.pages.dev"
metadata: 
  node_type: memory
  type: project
  originSessionId: 672b2bcd-96b8-498b-960c-cb37f82b365a
  modified: 2026-09-14T02:07:35.306Z
---

**What was reviewed (Sep 13 2026, Dallas's ask):** every engine, agent, job, skill, motion and page, against "will this succeed at full steam".

**Live read that decided the verdict (lemlist export, 39 mapped campaigns, 0 credits):** zero leads in any replied state anywhere; 151 leads at `linkedinVisitDone` and 64 at `emailsSent`, all waiting on a manual LinkedIn task; 99 open rep tasks (98 Nathan) flat for 9+ days; 1,893 leads `scanned/review` (loaded, never launched: DWO 803, WFM Present 362, Genesys 296, BO Net-New 130, BO FS 79); 4 of the 8 Sep 4 campaigns paused. Email step 1 delivered ~147 emails with open/click tracking OFF, so the 40% open gate in OKR O4 KR3 cannot be measured. Only the first email ever reaches a lead; every sequence's step 2 is a LinkedIn task nobody works.

**Engines:** TAM 60/60 on sourced accounts; signal engine 14/14 but still on the 6-row sample `accounts.csv` (signals.json dated Jun 13, never swapped); impact `outcomes.csv` empty; conductor DRY_RUN with 4 people-gated blockers (a 5th, `tam_contract`, was a regression from the Sep 11 `build_plays` tuple return, fixed in the worktree); `engine_state.json` seeded, control tower says "0 sends by design" while campaigns send. Brain live on Render, snapshot staged only (`deploy=false`, stale at 36h), Slack app awaiting admin approval.

**Swarm:** 26 launchd jobs, 24 wrappers call Claude; hourly relay is a 15 to 23 minute Claude session with 23 FAILs in two weeks, mostly to say "no new events"; agent-architect has minted 60+ proposals, ~0 adopted (decision-followthrough-audit proposed 20 times); registry drift (heatlist, cohortcutter undocumented for 12 days, now added); worktree 141 commits unmerged; fix sheets unrun 3+ weeks (WFM L3 rebind, deliverability re-point, ledger backfill).

**Measurement:** receipts ledger 56 days stale, no reply-to-ledger path existed, no per-campaign funnel, Salesforce Lead Source still Sierra's ticket (OKR KR1 date Sep 12 passed), council feed 0 rows, Day-75 tripwire Sep 19 at 0 of 15.

**Pre-mortem top failure:** the engine produced volume the rep never worked and leadership judged the row on meetings at the Oct 1 council. Uncontrollable: Nate's daily task throughput. One action: Monday, decide with Nate between a daily LinkedIn task quota and skipping the LinkedIn steps on the 8 live campaigns so email steps flow; check by Wednesday that open tasks fell under 20.

**Built:** `automation/campaign_scorecard.py` (13/13 tests), chained hourly after lemlist_pulse in the relay wrapper, rundown source 18, registry row; writes the council CSV (OKR O1 KR2) and `receipts_candidates.csv`. First read flagged Stars Resurrection STALLED 44d, BO Insurance 11d.

**How to apply:** before describing any campaign as "live", read `logs/campaign-scorecard-<date>.md`; "live" means leads advancing, not status=running. See [[campaigns-started-sep4]], [[nate-campaign-structure-review-sep4]], [[feedback-calls-first-net-new]].
