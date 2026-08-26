---
name: sequencer-prep-jul10
description: "Jul 10 2026 decision NOT to flip sequencer sends on despite Nate's enthusiasm; gated path adopted instead. Nate's mailbox warmup walkthrough + Dallas's runbook built."
metadata: 
  node_type: memory
  type: project
  originSessionId: cowork-jul10-2026
---

Jul 10 2026: decision made NOT to flip sends on despite Nate's enthusiasm. Gated path adopted instead. Two new docs built in the project folder:

- **Nate_Mailbox_Warmup_Walkthrough.md**: Outlook OAuth + warmup steps, verified against Clay sequencer docs Jul 10. Nate's only task, ~10 min. If OAuth errors, a Microsoft admin must trust the Clay Sequencer app; Dallas chases that.
- **greenlight-pack/10_Sequencer_Prep_Runbook_Jul10.md**: Dallas's order of operations: purge the 10 pre-gate draft leads, provisional customer_exclude wire, approval pass per SOP, run the resynced sync ONCE.

**Key safety fact:** leads in an UNLAUNCHED Clay campaign cannot send, so the sequencer can be fully loaded for Nate to read in the Leads tab while the mailbox warms. Launch stays off until warmup is green (2-3 weeks) and the walkthrough meeting happens.

**Why:** Nate's enthusiasm to move fast created pressure to launch before deliverability infra (mailbox warmup) was ready. Sending cold from an unwarmed mailbox risks poisoning the whole domain's deliverability, the exact P1 failure mode flagged in the original Q3 premortem (see [[intradiem-q3-mandates]]).

**How to apply:** Do not treat "loaded and ready to view" as "ready to send." The gate is warmup-green + walkthrough meeting, not Nate's readiness or excitement. Ties to [[clay-tables-not-live-yet]] (gated-not-live discipline) and [[naveen-jul8-meeting]] (approval SOP origin).
