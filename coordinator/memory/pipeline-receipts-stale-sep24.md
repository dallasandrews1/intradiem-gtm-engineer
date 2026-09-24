---
name: pipeline-receipts-stale-sep24
description: "Sep 24 2026 pipeline-receipts-tracker run - credit_pipeline_receipts.md unchanged since Jul 19, 67 days stale, seventh straight flag"
metadata: 
  node_type: memory
  type: project
  originSessionId: 90571299-1126-4070-8b8d-debb62bc0169
  modified: 2026-09-24T12:22:59.501Z
---

Sep 24 2026 unattended pipeline-receipts-tracker run (log: `automation/logs/pipeline-receipts-2026-09-24.md`). Renewal-case receipts picture:

- Credits in: 31,918.6 consumed to date (~44.3% of the ~72K anchor, ~38.1% of ~83,836 total incl. Jul 31 top-up). Live balance 51,917.40 (reused from same-day credit-check, not re-pulled).
- Qualified pipeline out per `automation/logs/credit_pipeline_receipts.md` (the only counted source): 23 sends, 1 qualified reply, 1 uncounted auto-reply, 0 meetings, $0 realized. This ledger has not moved since Jul 19 - 67 days stale, 7th consecutive pass flagging it.
- At least 11 live-sending/contact-built motions have opened since the ledger was last touched with no bucket to log a reply/meeting into it (two new this window: Frank Ciccone's 3xG Back Office QuickStart pair, Keegan former-customer alumni).
- Unattributed weekly burn: 5,731.8 of 9,682.0 credits (59%) this window has no motion-level home; ~3,554.6-credit gap inside the canonical ledger's own Sep 22-23 sequence.
- `clay_credit_ledger.csv` (CSV mirror) is 13 days / ~10,484.3 credits behind the canonical markdown ledger.
- No new prospect meetings Sep 18-24 per meeting-capture logs.

**Why:** this feeds the renewal-case proof-spend story (credits-in vs qualified-replies-out) for the Friday readout. The receipts ledger going stale means that story can't currently be told with real numbers - the engine is spending across 11+ motions but only one narrow hand-maintained file counts outcomes, and it stopped being updated in mid-July.

**How to apply:** before building or citing the credits-in/replies-out receipts story (Friday readout, renewal case, `[[naveen-weekly-readout]]`), check whether `credit_pipeline_receipts.md` has been updated past Jul 19 2026. If still stale, flag it rather than presenting the Jul 19 numbers as current, and note the 59% unattributed-burn gap as the reason the story is incomplete. Do not silently blend the small receipts-ledger reply count with the larger live-motion volume - they answer different questions (surfaced motion activity vs. logged qualified outcomes).
