---
name: nate-call-list-job-sep24
description: "Sep 24 2026: Nate's morning call list job (com.dallasandrews.gtm.calllist) LOADED and live; scores lemlist intent signals from the activities API because the native lead score has no API field; posts one message to #gtm-outbound-nathan only when someone qualifies"
metadata:
  node_type: memory
  type: project
  originSessionId: 4951fe64-3990-4080-92b0-6b4bac78b953
  modified: 2026-09-24T22:14:46.929Z
---

Built Sep 24 2026 on Dallas's ask: Nate was not calling the high-intent people in the running lemlist campaigns. Job: `automation/call_list.py` (deterministic) + `run_call_list.sh` + `config/call_list.json` + `tests/test_call_list.py` (29/29). Loaded as `com.dallasandrews.gtm.calllist`, fires 6:12 and 7:12 Mac time, gate = weekday, 07:00-08:45 America/New_York, once a day. `live: true` from day one on Dallas's words ("do that every morning for him"). First real post expected Fri Sep 25 about 7:12am ET.

**Data facts learned.** lemlist's "Lead score" (Settings > AI lead scoring) is UI-only: no field in the lead export, the lead record, or the MCP schema. The signals it is built from are all in `GET /api/activities?type=<t>&limit=100&offset=N` (not plan-gated, needs a User-Agent header): emailsOpened (has `bot`), emailsClicked, linkedinInviteAccepted, linkedinOpened, replies, interested marks, and the dialer calls (`aircallCreated` / `aircallEnded`; Nathan's first dialer call ever was Jessica Capacete, Hartford, Sep 24 14:46Z). Activities carry every lead custom variable, so the hook line (vm_hook on Stars Finance/Quality/Blitz, opener_line on Net-New, enterprise_line on BO customer lanes, measure_read as the fallback; Resurrection got its own spoken vm_hook on Sep 24, so every Stars lane now reads as a spoken line) comes for free. Phone coverage on Nate's ten running campaigns is 316 of 329 after the Sep 22 backfill.

**Scoring (config, not code).** accept 40, click 35, LinkedIn read 20, open 15 (cap 45), reply or interested 100; decay 1.0 to 3 days, 0.75 to 5, 0.5 to 7; threshold 40, so one accepted connect qualifies for three days and single opens never do. Drops: not-interested, meeting booked, unsubscribed or paused, held_leads from action_brief.json, a dialer call after the latest signal, a "<First> DONE / SKIP" reply under the post, and WENT COLD after three listings with no call (log only, rundown raises it). No number = log only for Dallas's backfill, never posted.

**Shape.** Header with the count, then per person: name, title, company, lane, number, "Why now" (real events with ET times), "Angle" (their own hook line), "Day N on this list" when carried. Footer teaches DONE / SKIP. Nobody at threshold = nothing posts anywhere. Claude is a courier only: reads the prior thread for DONE/SKIP, runs compose, posts the staged block verbatim, records the ts.

**Why:** the relay already alerts each accept hourly, but nobody turned those into a dated dial list with the reason and the number in one place.
**How to apply:** tune weights or threshold in `config/call_list.json`; never edit call_list.py for a scoring change. Rundown reads `logs/call-list-<date>.md`. To add Jack later, the script needs a second config keyed by rep (rep, timezone, route). Related: [[nathan-lemlist-phone-backfill-sep22]], [[bo-lemlist-empty-branches-sep22]], [[feedback-never-send-as-dallas]] (a rep-channel job post is not Dallas's voice; the relay set that precedent Aug 15).
