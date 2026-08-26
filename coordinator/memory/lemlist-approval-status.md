---
name: lemlist-approval-status
description: "Lemlist approval state as of Aug 17 2026 - PO in motion, one open item (deletion confirmation to Luis), Dallas leads the ask"
metadata: 
  node_type: memory
  type: project
  originSessionId: 20dbbad1-901b-4730-bfde-5a4ee84513fc
  modified: 2026-08-17T17:59:08.666Z
---

Lemlist Multichannel approval (3 seats: Nate, Jack, Dallas; ~$3.1K/yr, $3.5K budgeted) as of Aug 17 2026:

- Dallas LEADS the lemlist ask. Jack Ohagan just happened to have the prior vendor contact; don't frame Dallas as "working with Jack."
- Lemlist contact: Luis Olivera, luis@lemlist.com.
- Security: Enrique Colville approved and added lemlist to the approved list (Aug 12). Jason Jones (AI security) said "everything looks good" (Aug 13) with ONE open condition: written confirmation that account data can be fully deleted on request at cancellation (his misread: 30-day figure is backup retention, not post-cancel deletion; live data is kept until deletion is requested, which lemlist never explicitly confirmed).
- Dallas is emailing Luis directly for that written confirmation, then forwards it to the approval thread to close Jason's condition.
- PO: Chris Busbee wrapping the PO Aug 17 (per Naveen's Slack DM). Naveen wants Dallas and Jack live in lemlist the week of Aug 17.
- Jason Jones's standing pilot conditions: dedicated sending mailboxes on a separate subdomain, OAuth scoped to those mailboxes only, human sign-off on sends, AI voice left OUT of the initial pilot.
- Mailbox plan: purchase dedicated mailboxes/domain directly through lemlist (their standard model). No Randy/IT coordination and no M365/Entra OAuth grant needed - nothing touches the corporate tenant, which satisfies Jason's admin-access concern by design. Only timing variable is inbox warmup, managed by lemlist.
- Outlook connector is read-only on Dallas's mailbox (no draft creation); email drafts get delivered inline in chat.
