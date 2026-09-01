---
name: clay-free-sourcing-path
description: Clay CLI advanced search + MCP find-and-enrich-list-of-contacts source contacts with LinkedIn URLs at ZERO credit cost (verified Aug 17 2026)
metadata: 
  node_type: memory
  type: project
  originSessionId: 57bf8bee-44ae-4199-a724-bf8f3354a483
  modified: 2026-08-18T01:07:44.374Z
---

Verified Aug 17 2026 during the VodafoneThree ops-layer build for Jack: a full sourcing pass (556 search results pulled, 91 LinkedIn URLs resolved) consumed 0.0 Clay credits. Balance stayed at 72,137.1 throughout.

**Why:** Both surfaces bill against `actionExecutionBalance` (effectively unlimited: ~10^12), not the credit balance.
- `clay search query-mode create/run` (CLI advanced search): returns clay_profile_id, name, matched_experiences (company/title/dates), location. No LinkedIn URL. No credit cost.
- `find-and-enrich-list-of-contacts` (MCP, max 20 contacts/call, name + company domain): returns LinkedIn URL, fresh current title/company, profile_id matching the search ids. No credit cost, IF no dataPoints are requested.

**How to apply:** For any list-building ask (Jack-style "build me a table"), chain: broad advanced search → classify in-model (free, replaces Claygent step one) → URL-bridge via find-and-enrich-list-of-contacts → hooks via signal-researcher web agents (free). Credits only needed for email/phone waterfalls ("Enrich Person and Find Contact Details", 12.8/run) or Claygent research columns. The fresh titles returned by the MCP tool also catch stale-index people who left (5 of 112 caught on the VT build).

Managed routine "Enrich Person" (0.5/run) requires a LinkedIn URL or email input; it cannot start from a bare clay_profile_id.

Related: [[clay-credit-steward-discipline]], [[jack-vodafonethree-ops-layer]]

**Freshness caveat (Aug 25 2026):** the free path's employment data lags. Michael Waterman (Cleveland Clinic) came back 'current' from both the search index and find-and-enrich-list-of-contacts, but Sales Navigator showed him retired. Treat the free path as sourcing, not verification; anything going onto an AM-facing map or into a sequence needs a live check (Sales Nav badge/profile at add time, or a paid enrichment with an explicit go). Also: directors sourced by title keyword arrive without their VP layer; run a second 'layer fill' search per (account, function) so charts don't show Sr Directors reporting straight to a COO.

**Aug 25 addendum:** Amanda King (Cox) came back from find-and-enrich-list-of-contacts as current with a 2025 start date; Sales Nav showed she left ~2 years ago. The bridge is not a freshness check either. Anything AM-facing needs a live source (Sales Nav badge/profile at add time, or a paid live enrichment with an explicit go).

**Aug 25, root cause of the Goldman misses:** Nolan, Sellitti, Rider (and earlier Waterman-type misses) came from the Jul 26 CSV pull path (`Back_Office_*_Jul26.csv` -> roster CANDIDATE rows) which carried month-old titles and URLs straight onto maps without ever going through find-and-enrich-list-of-contacts. Rule: every row that reaches an AM-facing map passes the bridge on the day it is placed, regardless of source; re-bridge anything older than two weeks before reuse.

**Dual-profile rule (Aug 25, Natalie Schneidereit):** when find-and-enrich-list-of-contacts returns two or more profiles for one name at the same company, choose by most recent latest_experience_start_date (the live profile), never by 'title matches what we already had' (that locks in the stale record). Flag all multi-profile resolutions for a Sales Nav check.
