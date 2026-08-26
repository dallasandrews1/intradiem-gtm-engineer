---
name: cold-call-contract-aug2
description: "Research-grounded cold call contract (Aug 2 2026): shared Cold_Call_Playbook_Aug2.md, banned availability-opener family, four-beat opener skeleton, busy/brush-off branches, airlines quick-handles v1.4, format spec v2.3, fixture v5"
metadata:
  type: project
---

Aug 2 2026: Dallas asked for a full review of the Daily Action Brief cold call scripts against 2025-2026 call research. Findings and fixes, now live in the composer chain:

**Defects found in the v2.2 renders:** Nate's opener used "Did I catch you at an OK moment?" and Jack's "Did I catch you with 30 seconds?", both in the availability yes/no family that large call studies (Gong Labs + 2025 dial-level data) put ~40% BELOW baseline; the high-performing shape (~11% vs ~2% baseline) states the reason first, then asks for ~30 seconds with the prospect explicitly in control. Engage segments ran monologue-into-meeting-ask with no check question (booked calls have real back-and-forth and run ~2x longer). Jack had ZERO objection handles on live calls (the airlines playbook had no quick-handles section). No busy or brush-off branches existed for either rep.

**The fix, four layers (config over code):**
1. NEW `motions/shared/Cold_Call_Playbook_Aug2.md`: canonical call direction, wired into every brief's `playbook_sources` in action_brief.json. Four-beat opener skeleton (name+pause, who, reason-from-lead-hook, 30-second contract; UK vs US register), BANNED opener family (any availability yes/no before the reason), engage-ends-on-check-question, ask names the payoff + honest-exit clause, lock-the-slot-on-a-yes, universal branches (busy, brush-off, send-me-an-email, what's-this-about), delivery cues, voicemail-as-email-amplifier. Research stats live there marked research-sourced, never prospect-facing.
2. `automation/config/action_brief_format.md` bumped to v2.3: call segment list gained If they're busy / If they brush you off, opener rule, per-Calls-block delivery line.
3. `automation/run_daily_action_brief.sh` step 3 updated to match (unattended composer follows the same contract).
4. `action_brief_fixture.json` v5: all three dial scripts rebuilt to the contract; Jack's calls now carry pushback from the airlines v1.4 quick-handles.

Also: `UK_Airlines_Wave1_Variable_Stage_Aug1.md` is now v1.4 with a motion quick-handles section (claims provider, planning/WFM tools, ops-not-me, call-after-summer), verified figures only.

**Premortem hardening (same day):** BRANCH CAP (max seven labeled blocks, max two pushback blocks per call, relevance rule never a wording trim), OPENER FACT CHECK on live runs (every opener fact must trace to a lead variable or playbook source, one OPENER-CHECK log line per composed dial script; fixture-staged scripts skip it), brush-off HARD STOP (release line ends the call, the answer is logged intel, never a second pitch). All three live in the playbook, spec v2.3, and runner prompt.

**Render verified (Aug 2):** RUN 3 in automation/logs/action-brief-2026-08-02.md is the authoritative v5 render: all three dial scripts carry the four-beat openers, busy/brush-off branches, Jack's first pushback blocks, zero banned openers, branch cap self-checked at 7/7/7 blocks. Composer also fixed the recurring em-dash separator defect on title-bearing lead lines. Brief titles in action_brief.json and the spec's dry-run thread marker now use `·`/colon instead of em dashes (they were the last em-dash sources in renders).

**Standing rule:** composed openers assemble from the skeleton plus the lead's real variables, never new facts; premortem watch-item is the unattended composer drifting facts into openers on the first live (non-fixture) run, so eyeball the first live brief's OPENER-CHECK lines. Related: [[action-brief-format-v2-aug1]], [[wave1-spoken-variable-sweep-aug2]].
