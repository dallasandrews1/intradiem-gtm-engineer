---
name: inger-execution-state-rogers-sep20
description: "Sep 20 2026: Mary Ann's all-hands concern (data and ideas, no execution plan) answered on Inger's index with done/slipped state per move, a Rogers save room, and shelf-only accounts removed; staged, not deployed; the PMO export holds no Cleveland Clinic rows so no state shows yet"
metadata:
  type: project
---

**Trigger:** Mary Ann Chandler said in person at all-hands (so not in Otter or Slack) that the account work has great data and ideas but no plan for executing on them. Inger's index had one plan out of twelve accounts and no sign of whether any move happened.

**Built Sep 20 2026, STAGED not deployed:**
- `motions/churn_risk_save_plan/apply_tracker_state.py`: done / slipped per move from the newest real PMO Progress tracker export, plus a hand-recorded `word` block in `data/move_state_<slug>.json` that wins over the tracker ([[feedback-rep-word-is-the-truth]]). No row and no word means no state; a passed date alone never marks a colleague's move slipped. Our own import drafts are never read as a record.
- Cleveland Clinic room and the rep index render the state; slipped moves stay in the next-move block until done.
- Rogers save room: `build_comms_plan_rogers.py`, `build_save_room_rogers.py`, facts in `data/rogers_fact_sheet.md`. Redacted AM-room shape ([[feedback-no-draft-copy-to-ams]]). Five people checked current, 0 credits.
- Guardian Life and McKesson off the index until they have a plan; shelf URLs keep serving.

**Findings worth keeping:**
- The only real PMO export (Sep 10) is 32 ADT rows, zero Cleveland Clinic. `Cleveland_Clinic_PMO_Tracker_Import.csv` is OUR draft, never confirmed loaded. Until a fresh export or Inger's word arrives, zero moves carry a state. See [[account-health-pmo-tracker-path-wrong-sep14]].
- Rogers: term ends Dec 31 2027, no auto-renew, no termination for convenience before then, 8,250 licenses. Projected return 2.1x to 1.3x, YTD 0.7x, AHT still TBD, coaching 0.1%, governance council recommended twice and not standing. NO document names a blocker; Inger's word is the only source. Success manager in documents is Christine Gotleib as of Apr 6 2026, unconfirmed today.
- A room rebuild drops the hero One-pagers link; rerun `link_shelf.py`. `check_plans_site.py` fails on any intended change until `_staged_pre_job6` is refreshed for exactly those files.

**Open:** deploy is Dallas's (`deploy_rep_pages.sh maps`, `rooms`, `plans`); register the Rogers URL in the shared links manifest once sent; get the tracker export or the brainstorm outcome; Inger names the Rogers blocker before the room goes to her.

Related: [[rep-index-pages-sep20]], [[inger-churn-risk-save-plan-sep10]], [[feedback-map-vs-route-comms-plan]].
