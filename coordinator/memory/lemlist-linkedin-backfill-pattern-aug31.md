---
name: lemlist-linkedin-backfill-pattern-aug31
description: "Aug 31 2026 - lemlist \"Stars - Resurrection (Nate)\" (cam_sh3JCJoxtEHyjGrsw) got LinkedIn URLs on all leads and four contacts removed, three departed plus one who moved to a non-plan vendor (47 -> 43); repeatable chain is lemlist export -> Clay free bridge -> paid Enrich Person only on misses -> PATCH/DELETE by email; URL-input Enrich Person ~0.8 cr/run, email-input runs coincided with a 15-credit drop (unmeasured)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 53dbdbfd-fd14-436f-89c5-44386129457c
  modified: 2026-08-31T14:37:09.805Z
---

Aug 31 2026: Dallas asked for LinkedIn URLs on every lead in lemlist "Stars - Resurrection (Nate)" (id `cam_sh3JCJoxtEHyjGrsw`, draft, 47 leads, 23 missing), then to remove leads no longer at their company. End state: 43 leads, every one with a LinkedIn URL. Removed: Giancarla Addison (Clover, role ended 2026-05), Peter Kuipers (Clover CFO, ended 2026-04), Marvin Martin (Solis, ended 2026-08), Candace Lowman (moved Apr 2026 from ATRIO to Allymar Health Solutions, a BPaaS/BPO vendor for MA plans, JV of CPF and Accenture; Star Ratings attach to plans, not vendors). Dallas's rule for Stars campaigns: a lead who moves to a company where Star Ratings no longer apply is removed, same as a departure. Sudha R. (MetroPlusHealth, Head of CX Strategy) placed as a labeled best guess for `sarodes@nychhc.org`.

**Pattern (reuse for any lemlist campaign):**
1. Export: `GET /api/campaigns/{id}/export/leads?state=all&format=json` with `-u ":$LEMLIST_API_KEY"` (key in `automation/config/lemlist.env`). Leads missing a URL simply lack the `linkedinUrl` key.
2. Free bridge first: `find-and-enrich-list-of-contacts` (Clay MCP, 20 per call, name + domain, no dataPoints) resolved 20 of 23 at 0 credits, and doubles as a cheap employer sweep on leads that already have URLs. Retry misses with the nickname on the email (Melissa -> Mel), the operating-company domain instead of the holdings domain, and the plan subsidiary's domain (nychhc.org -> metroplus.org).
3. Paid fallback only on the residue: managed routine "Enrich Person" (`t_0thx4ohpCNT3KNijyVo`) via `run_subroutine_direct`, input `{"Email": ...}` or `{"Professional Profile URL": ...}`. Read with `get-task-context` (5+ profiles overflow the tool result; parse the saved file with python). `current_experience` empty plus `latest_experience.end_date` set = departed. This is the definitive freshness check the free bridge is not.
4. Write back: `PATCH /api/campaigns/{campaignId}/leads/{leadId}` body `{"linkedinUrl": ...}`. Remove: `DELETE /api/campaigns/{campaignId}/leads/{email}?action=remove` (path must be the EMAIL, by lead id returns "An email is required to unsub a lead"; without `action=remove` lemlist unsubscribes the address instead of just dropping it). `GET /api/leads/{leadId}` by _id returns empty; look up by email.

**Credit observation:** the five URL-input Enrich Person runs cost 4.0 credits total (67,620.7 -> 67,616.7, about 0.8 per run, consistent with the 0.5 in [[clay-free-sourcing-path]] plus rounding). The earlier 15-credit drop (67,635.7 -> 67,620.7) landed during the three EMAIL-input runs; either email-input waterfalls cost more than URL input or a scheduled job spent concurrently. Prefer URL input when a URL exists; budget email-input runs at up to 5 each until measured cleanly.

**Why:** Free bridge covers most of the list; paid enrichment is only worth it on the residue and as the departure check, and the whole job stayed far under the 100-credit go gate in [[feedback-warn-before-large-credit-spend]].

**How to apply:** Same chain for "add LinkedIn URLs to campaign X" or "clean campaign X of departed leads". For motion-specific campaigns (Stars, back office), a company change is a removal unless the new company is still in the motion's buyer set, and BPO/vendor moves are out. Related: [[feedback-guess-and-label-sales-validates]], [[lemlist-activities-plan-gate-aug14]].
