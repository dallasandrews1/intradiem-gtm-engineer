---
name: lemlist-trial-gameplan-jul31
description: Jul 31 Lemlist 14-day trial architecture - Dallas orchestrates from his account, Nate is the sender identity via team invite (his mailbox + LinkedIn), Stars-only scope (resurrection + fresh-pool Quality/Finance lanes), API-key build path, day-14 receipts feed the Naveen-to-Chris paid case at QBR week
metadata:
  type: project
---

Lemlist trial started Jul 31 2026 (ends ~Aug 13-14, QBR is week of Aug 10). Fulfills Naveen commitment #6 from [[naveen-jul31-call-commitments]] (small live campaign on trial, then Naveen takes the paid case to Chris; position as an AI tool for budget; Matt alignment Mon Aug 3; Jason Dowden in approval path, IT already cleared per Dallas).

**Architecture (Dallas's explicit stance: he orchestrates, never does seller activities):**
- One workspace = Dallas's account. Nate invited as a TEAM MEMBER (trial allows unlimited seats); Nate connects HIS mailbox (OAuth) and HIS LinkedIn (Chrome extension). All sends carry Nate's identity. Nate's own untouched free-trial eligibility = backup runway.
- Dallas pastes an API key; Claude builds campaigns, sequence steps (email/LinkedIn/call task), schedules, and lead loads programmatically (verified: Lemlist API supports create-campaign, step creation, lead add; developer.lemlist.com).
- Trial facts verified Jul 31: full multichannel + LinkedIn extension, 50 emails/day, 200 credits, unlimited team invites, NO lemwarm during trial (paid only), falls to Freemium after 14 days, no auto-charge.

**Scope decision: Stars-only, 3 campaigns** (Naveen's iteration-2 directive = multichannel close-the-loop):
1. Stars Resurrection: already-emailed cohort minus repliers, LinkedIn visit + connect, call task (Connor's ~50 ZoomInfo cells), "just tried you" email referencing Nate's earlier note (no true Gmail threading, copy references it), breakup.
2. Stars Fresh Pool / Quality lane and 3. Finance lane: untouched addressable send-kit contacts, adapted from the Jul 13 Wave 1 5-touch persona sequences. Zero Intradiem stats in default copy (claims discipline holds).

**Gates that survive the tool switch:** hand-verify every loaded contact against the 101-account customer file BEFORE load (Clay gate leak from [[gate-integrity-fanout-first-run-jul27]] means no automated gate is trusted); campaigns built PAUSED, only Dallas starts them; LinkedIn steps manual-approve only; click tracking OFF for trial (shared tracking domain hurts deliverability; custom CNAME is the paid-rollout step); Lemlist daily cap ~20-25 so Nate's mailbox warmth budget is shared with native sends.

**Mechanic to confirm in-app (not assumed):** campaign sender assignment to a teammate's connected mailbox (per-seat vs workspace-level). Verify in the Sender setting once Nate's mailbox is connected; fallback = create campaigns under Nate's seat/key.

**Proof plan:** lemlist_pulse API fetch script logs activity into the rundown (single-morning-brief rule, no independent DMs); receipts = sends/replies/meetings + cost per meeting vs native path; day-14 readout lands QBR week for the Chris paid case. Demo-able workspace target: Mon Aug 3 (Matt + Jack meeting).
