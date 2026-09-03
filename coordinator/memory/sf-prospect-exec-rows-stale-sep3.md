---
name: sf-prospect-exec-rows-stale-sep3
description: Sep 3 2026 test: Salesforce prospect executive rows are stale beyond repair (14 of 16 emails invalid, 2 of 20 resolve to a profile and both wrong); source senior prospect pools LIVE from Clay search (free, current) and pay only for emails on confirmed-current people
metadata:
  type: feedback
---

Sep 3 2026, DWO executives pool (3,144 SF prospect rows pushed to lemlist). Gap-fill tests: ZeroBounce validate-email on 16 SF addresses returned 14 invalid; Enrich Person by email on 20 rows resolved 2 profiles, both wrong for the motion (name collision, retiree); the free find-and-enrich bridge on 24 rows hit 3, two of them wrong people. Clay's live advanced search for current C-suite / EVP / SVP operating titles at the same accounts returned 77 clean current executives for 25 accounts at 0 credits.

**Why:** the SF prospect layer was loaded from ZoomInfo and 6sense years ago; names, titles and mailboxes have rolled over. Validating or enriching a stale row spends credits to confirm it is dead.

**How to apply:** for any senior prospect pool, source live first (`clay search query-mode`, seniority C-suite/VP/Head, job_title is_similar_to the target titles, company.domain in the account list, location_country United States), bridge URLs free, then run Work Email (1.6/row measured) only on confirmed-current people, waved. Use SF rows only as a match key to keep SF IDs. Clay caps direct `workflows actions test` at 25 a day; bulk always goes through a routine. Never use "President" or "Managing Director" as Contain terms in an Audiences filter. Related: [[lemlist-us-lists-sep3]], [[clay-free-sourcing-path]], [[jpmorgan-email-waterfall-stop-sep3]].
