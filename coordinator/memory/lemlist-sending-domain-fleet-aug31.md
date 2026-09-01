---
name: lemlist-sending-domain-fleet-aug31
description: "Aug 31 2026 sending-domain plan — intradiemhq.com only for now (Nate + Jack cold mailboxes, PO budget caps at one domain), tryintradiem.com then getintradiem.com queued for next approval, intradiem.com mains reply-only going forward"
metadata: 
  node_type: memory
  type: project
  originSessionId: 360b8209-1dfa-4ad2-a5c9-5e6806807ef3
  modified: 2026-08-31T22:19:07.671Z
---

Decided Aug 31 2026 (revised same day): Dallas is buying ONE alternate sending domain now — two at $14/yr each would put the total $28 over the submitted lemlist PO, and the PO is not being amended for it. Fleet:

- **intradiem.com** (Nate + Jack existing mailboxes): replies, warm threads, customer/AM comms only. No NEW cold loads; live campaigns (Stars-Resurrection, Fresh Pool, Blitz) finish on these addresses rather than swapping senders mid-sequence.
- **intradiemhq.com** (PURCHASED, mailboxes CREATED Aug 31: nathan.belfield@ + jack.ohagan@): cold volume after 3-4 week lemlist warmup; ~40-100 sends/day warm. Cap at these 2 mailboxes — do NOT add more mailboxes to this domain (domain-level volume/complaint thresholds; same-person address variants on one domain are a bulk-sender tell); the next pair goes on tryintradiem.com when bought.
- **tryintradiem.com**: NOT purchased — first in the queue when the next approval/budget opening comes ($14/yr); ride a bigger ask, never its own ask.
- **getintradiem.com**: NOT purchased — second in the queue, park and age when bought.

Mailbox hosting decision (Aug 31): lemlist's purchase flow offered Outlook at $10/mailbox/mo vs generic SMTP at $5/mailbox/mo; chose Outlook for both (real Microsoft 365 sending infrastructure beats third-party relay reputation, and the target audience is M365 shops behind Proofpoint/Mimecast). Recurring cost for the budget conversation: $20/mo for the two intradiemhq.com mailboxes, doubling to ~$40/mo when tryintradiem.com and its pair are added.

Rules agreed: 2 mailboxes per domain, ~20-50 sends/mailbox/day warm, 301 redirect to intradiem.com + SPF/DKIM/DMARC + per-domain custom tracking domain before any send, warmup starts the day mailboxes are created. Register under Intradiem-controlled registrar, not personal. Rationale: domain reputation is shared, so cold risk stays off intradiem.com (Google/Microsoft ~0.3% complaint threshold is domain-level).

Related: [[lemlist-approval-status]], [[nate-campaigns-linkedin-sweep-aug31]]
