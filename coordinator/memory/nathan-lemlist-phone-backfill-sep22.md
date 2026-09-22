---
name: nathan-lemlist-phone-backfill-sep22
description: "Sep 22 2026 phone backfill on Nathan's 7 lemlist campaigns (204 leads); ZoomInfo files checked first, then Clay; lemlist has no phone-on-entry standard"
metadata:
  node_type: memory
  type: project
  originSessionId: 7fcc8343-d604-4d8d-9244-d83189a75ab4
  modified: 2026-09-22T23:12:59.624Z
---

Dallas believed lemlist adds phones whenever a lead enters a campaign. It does not; nothing in lemlist does that (its own enrichment has been out of credits since Aug 6 and fails silently). Before the backfill only 45 of 204 leads had a phone, and most of those were HQ switchboards (MetLife 2125782211, Humana 5025801000, Cigna 8602266000).

Order Dallas asked for: check the ZoomInfo lists first (`~/Desktop/Intradiem Deliverables/ZoomInfo/`, matched by email, then LinkedIn, then name), then Clay for the rest.
- ZoomInfo: 37 leads matched, 28 phones written (foreign mobiles on US contacts skipped: Remington P., Dan Quinn).
- Clay `Enrich Person and Find Contact Details` on 162 leads with LinkedIn URLs: 159 mobiles, 148 written, 1,463 credits (~9 each). Josiah Mooney held (now at Brightstar Care, not Molina).
- A replaced number is kept in the lead variable `phone_alt`. Trap: 11 leads already had a `phone_alt`, and it was overwritten without being read first. Next time, pull lead variables before any upsert.
- The CLI `routines runs get` returns 20 results per page by default; page with `--limit 100 --cursor`.

Salesforce copy of all 176 numbers: `~/Desktop/Intradiem Deliverables/Nathan lemlist phones Sep22.csv`. Salesforce-linked leads can revert in lemlist, see [[lemlist-salesforce-sync-overwrites-lead-fixes]].

**Why:** Nathan's call steps had almost nothing real to dial.
**How to apply:** any new wave loaded into lemlist needs the ZoomInfo-then-Clay phone pass at load. Related: [[enrichment-doctrine-clay-not-lemlist]], [[lemlist-nathan-invite-steps-manual-sep22]]
