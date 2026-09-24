---
name: keegan-salesnav-list-in-lemlist-sep24
description: Keegan's 264-lead Sales Navigator list is fully in the lemlist contact list "Keegan's Search" (clt_fQpabfLBHJX9Ghpwc) as of Sep 24 2026; reconciled, 18 on the alumni page, 72 gate-cut, 174 never read; 114 of those are name and title only
metadata:
  type: project
---

Sep 24 2026 (16:53 ET read). Dallas pushed Keegan's saved search (id 1999259452) into lemlist by hand in two passes. The first 95 (Sep 23 and
overnight) came with LinkedIn URLs and companies. The 169 pushed Sep 24 at 21:50 UTC came as name plus title ONLY (no URL, no company, 15
with truncated surnames), the shape of a results-grid paste rather than an extension push. Full read saved at
motions/keegan/alumni/_lemlist_keegans_search_list_sep24_full.json; per-person classes in Keegan_SalesNav_264_Reconciliation_Sep24.csv.

Reconciliation (log automation/logs/keegan-salesnav-264-2026-09-24.md): 18 on the alumni page, 72 in the People Database pull but gate-cut,
174 never in the pull (60 with a URL, staged as Clay Enrich Person items in _clay_enrich_items_keegan_list_sep24.json, about 480 credits;
114 need a URL first). The alumni page's "on Keegan's list" chip now means real list membership (18 of 65, was 59 under the replica match);
deployed Sep 24, backoffice-maps f5d1545d, gate PASS.

**Why:** the lemlist People Database replica of Keegan's search missed two thirds of his real list; his list is the only ground truth for his
definition, and any "N of 264" story must come from list membership, never from the criteria match.
**How to apply:** to grow the page from his list, first get URLs onto the 114 (extension re-push into the same list, or the SalesNav CSV into
automation/inbox/salesnav/), then run the staged Clay items, read_clay_alumni_runs.py, rebuild and deploy maps. Related: [[keegan-door-context-sep23]],
[[clay-enrich-person-contact-details-routine]], [[lemlist-salesforce-create-on-sync-off-sep23]].
