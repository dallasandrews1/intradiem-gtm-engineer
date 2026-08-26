---
name: action-brief-format-v2-aug1
description: "Daily Action Brief format v2 line (v2 Aug 1, v2.1 spoken voice, v2.2 full-copy autopilot sends thread + activity-block ordering) — per-type layouts, real threading, playbook-sourced handles"
metadata: 
  node_type: memory
  type: project
  originSessionId: d841a1b4-7037-46aa-b545-c990d8c42973
  modified: 2026-08-02T01:56:36.993Z
---

Dallas reviewed the Aug 1 2026 Action Brief samples in #relay-test and flagged three defects, fixed the same day as format v2:

1. **Strike-room layout never reached the brief.** Calls rendered as one mashed paragraph with the objection handle folded into the opener. v2 contract: call scripts render as labeled segments, each its own code block — Opener / If they engage / The ask / If pushback - "<objection>" / No answer - voicemail — mirroring the strike-room sequence docs and the cold-call-playbook structure (opener, 30-second expansion, CTA, objection handles). Segmentation lays copy out, never shortens it.
2. **False threading claim.** The sample said "Draft reply is threaded under this brief" but nothing was threaded. v2: fresh reply drafts post as REAL threaded messages (compose threads first, post main brief, capture ts, post threads with thread_ts); the brief never claims a mechanic this run didn't perform. Relay-owned drafts still reference the relay alert, never re-thread.
3. **Per-type formatting.** Emails render as emails inside code blocks (greeting line, blank lines between paragraphs, sign-off line, Subject: only on new sends). Voicemails/voice notes/DMs stay single blocks.

Objection handles come only VERBATIM from per-brief `playbook_sources` now listed in automation/config/action_brief.json (stars → StarRatings_Wave1_Persona_Sequences_Jul13.md quick-handles; airlines → UK_Airlines_Wave1_Variable_Stage_Aug1.md; insurance_fs → UK_Insurance_FS_Motion_Spec_v1.md). Never invent a handle in the brief.

Files: automation/config/action_brief_format.md (v2 contract), action_brief.json (playbook_sources), action_brief_fixture.json (calls now carry segmented `script` objects), run_daily_action_brief.sh (steps 2/3/5 rewritten). Dry-run renders show threads under "↳ THREAD" markers. Related: [[banned-phrases-comparing-notes-jul31]].

**v2.1 (Aug 2 2026, same day):** SPOKEN VOICE section added at the top of the spec, outranking every layout rule: all rendered copy must pass "would a real person say this out loud"; warm-never-curt on declines ("fair to ask, I would too" shape); objection handles render in spoken form with claims/facts/mechanism unchanged; two reference drafts (Marc/Aer Lingus, Thornton/Clover) set the register. Fixture rewritten to v3 spoken copy; runner guardrail (c) added.

**v2.4 (Aug 2 2026, night): for-dummies rep instructions.** Dallas: zero resistance, "for dummies" simple. Footer rewritten to plain actions with a REAL example name from today's brief ("Pedro DONE / SKIP / HOLD"), each word defined inline, all plumbing words (relay, hourly reads, logs) banned from rep-facing copy. Reply entry now says "Send it from your inbox... then reply <Name> DONE here", never "approve it" (no approve button exists; reps must know drafts never send themselves). Overflow pointer standardized to "The rest of today (...) is in this thread." Connect line reads "Approve these connects in Lemlist (they send blank, no note)". NEW PINNED EXPLAINER section: canonical 60-second how-it-works pinned once per rep channel at launch so the daily footer stays two lines; sample posted to #relay-test Aug 2. DONE/SKIP/HOLD reply format unchanged, so brief-thread-ingest parsing is untouched. v2.3 (same day, earlier): research-grounded call contract per [[cold-call-contract-aug2]].

**v2.2 (Aug 2 2026, later same day), two changes from Dallas's feedback:**

1. **Full-copy autopilot sends thread.** Dallas: omitting the automated email copy from the brief is confusing; for continuity and formality the brief must show EVERYTHING going out under the rep's name that day. Autopilot section is now two parts: the counts summary stays in the main message, and every automated email firing today renders in full in a threaded message (ALWAYS threaded, never main-message, last in thread order). New AUTOPILOT SENDS spec section: group by campaign step, distinct per-lead copy (MessageGen variants) renders each email in full, a shared template renders once with {{variables}} visible above the recipient list. Copy only from the Lemlist sequence API or fixture staging; if today's recipients aren't derivable, render step copy + count + "recipient schedule is in Lemlist", never fabricate recipients or copy. Visits/likes/follows stay counts. Fixture v4 stages both paths (Nathan 4 distinct variants, Jack 1 template × 8 recipients); runner gained step 4 (later steps renumbered 6/7).
2. **Activity-block ordering made explicit.** Dallas asked whether the day's order should couple by activity so reps block their work; that was already the design (section order mirrors Lemlist queue order) but only as a fixed list. Spec now states the intent: sections ARE activity blocks, rep runs top-to-bottom as time blocks (inbox → one dialing block → LinkedIn admin batch → recording), no layout/overflow decision may interleave activities or scatter one activity across the brief; per-lane split of an oversized brief multiplies the blocks and stays last resort.
