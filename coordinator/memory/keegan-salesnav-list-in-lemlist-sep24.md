---
name: keegan-salesnav-list-in-lemlist-sep24
description: Keegan's 264-lead Sales Navigator list is fully in lemlist ("Keegan's Search", clt_fQpabfLBHJX9Ghpwc) and fully read as of Sep 24 2026; 73 on the alumni page (120 total), 4 names unresolved; roster written back to lemlist Sep 24 (URL 200, email 131, phone 182 of 264); 6 duplicate pairs merged Sep 25, list whole at 264 with no shared identifiers
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

Same evening, credits spent (Dallas's call): 114 name-only rows resolved through Clay search by name plus title (110 of 114), then three
Enrich Person and Find Contact Details runs read all 170 unread people (1,238.6 credits). Roster: Keegan_SalesNav_List_Verified_Sep24.csv
(170 rows with lemlist contact id, 119 work emails, 162 mobiles). Final 264: 73 on the page (proven overlap), 109 read with a customer spell
that predates Intradiem, 72 gate-cut Sep 23, 6 no customer in history, 4 unresolved common names (Eric Johnson, Amit Anand, John Hogan,
Scott Davidson). Alumni page 65 to 120 and the Keegan index counter deployed (backoffice-maps d7447df3, 6a149bb9).

**Why:** the lemlist People Database replica of Keegan's search missed two thirds of his real list; his list is the only ground truth for his
definition, and any "N of 264" story must come from list membership, never from the criteria match. Clay search by full_name plus current
title resolves a name-only row to a LinkedIn URL for free, so a names-only paste is recoverable without a re-export.
Write-back done Sep 24 evening: 166 contacts updated by id with fillEmptyOnly (stored values never replaced), list now reads URL 200 / email 131 /
phone 182 of 264; 6 rows conflicted because the email or URL already sits on an older contact (Volz, Hyde, Griffin, Fiorella, Brooks, David M.),
phone landed on each. Charles T Brooks's older record still reads Kemper while Clay reads Bamboo Insurance.
Sep 25: the six pairs merged into the older records (list memberships moved to the survivors, so the list stays at 264; 8 rows now sit in a campaign).
**How to apply:** the list is load-ready on identifiers; what remains is the 4 unresolved names from Keegan's own list, and Charles Brooks's campaign owner should hear that Clay reads him at Bamboo Insurance while the record says Kemper. The Keegan index builder writes account_maps/keegan_index.html only; copy it into
deploy-backoffice-maps/keegan/ by hand before deploying maps. Related: [[keegan-door-context-sep23]],
[[clay-enrich-person-contact-details-routine]], [[lemlist-salesforce-create-on-sync-off-sep23]].
