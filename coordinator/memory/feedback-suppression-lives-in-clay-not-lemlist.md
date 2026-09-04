---
name: feedback-suppression-lives-in-clay-not-lemlist
description: Sep 4 2026 - Salesforce mirror lists whose only job is dedupe or suppression do not belong in lemlist Contacts; suppression runs in Clay Audiences, lemlist holds only rows a rep could sequence
metadata:
  type: feedback
---

Dallas asked on Sep 4 2026 whether the `(SF)` contact lists belong in lemlist if their only purpose is preventing duplicates. Agreed answer: no.

**Why:** dedupe and customer exclusion already run in Clay Audiences (SF-synced, customer flag, denylist, install-base) before any push. lemlist's native dedupe only prevents a second record for the same email or URL. A stale SF mirror tagged with a live motion is a rep-facing trap (gap-fill test Sep 3: 14 of 16 SF addresses invalid, 2 of 20 resolved to the wrong person).

**How to apply:** push to lemlist only people a rep could sequence after live verification. Retire the sf_stale rows on DWO Executives, Prospects (SF) `clt_FKm6KuNcgeghas73o` and re-verify or remove the two Dir+ (SF) mirrors; contact deletion is Dallas's hand. A lemlist-side safety net, if wanted, is the unsubscribe list (accepts domains), never a contact list. See [[feedback-netnew-pool-is-clay-sourced]].
