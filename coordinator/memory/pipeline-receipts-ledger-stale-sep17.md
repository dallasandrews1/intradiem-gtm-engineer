---
name: pipeline-receipts-ledger-stale-sep17
description: Sep 17 2026 pipeline-receipts-tracker run found the receipts ledger 60 days stale and 93% of weekly credit burn unattributed to any motion
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f5843e3-e2cd-421b-b33b-59e49e037fb8
  modified: 2026-09-17T12:22:55.939Z
---

Sep 17 2026 unattended pipeline-receipts-tracker run (log: `automation/logs/pipeline-receipts-2026-09-17.md`):

- Live Clay balance 61,599.4. Consumed against the ~72K one-time proof budget (plus confirmed Jul 31 top-up of 11,836): 22,236.6 credits (~30.9% of the 72K anchor, ~26.5% of the 83,836 total available).
- `automation/logs/credit_pipeline_receipts.md` (the receipts ledger) has not been touched since Jul 19 — 60 days stale as of this run.
- Strictly from that ledger: 23 sends → 1 qualified prospect-authored reply (Latonya Augustine/CCMAPD, referral to Nancy Guzman still open), 1 auto-reply (Kim Bachmeier/Medica OOO) not counted → 0 booked meetings → $0 realized pipeline (`impact/outcomes.csv` still header-only).
- Biggest flag: 802.3 of the week's 864.4-credit burn (93%) has no motion-level attribution anywhere in the credit ledger or memory — the largest unattributed fraction of any pass to date. At least 6 live-sending/committee-build motions (BO customer lane, Stars, Blitz, DWO Executives, WFM/Genesys Present, UPT displacement) have no bucket in the receipts ledger to catch a reply if one lands there.

**Why:** the receipts ledger is what justifies the ~72K proof spend for the renewal case (credits-in vs. qualified-replies-out). A stale ledger plus unattributed burn means the renewal story can't currently be defended with real numbers, and a reply landing in one of the 6 unbucketed motions would go uncounted.

**How to apply:** before presenting any renewal-case/proof-spend narrative to Naveen or leadership, check whether `credit_pipeline_receipts.md` has been updated since Jul 19 — if not, flag it as stale rather than presenting the 1-reply/0-meeting figure as current. When touching the receipts ledger schema, add buckets for the 6 unattributed motions listed above so future replies get caught. See [[feedback-warn-before-large-credit-spend]].
