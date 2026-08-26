---
name: apollo-credit-ceiling-and-ghost-avatars
description: Apollo plan is 155 lead credits/month and photo enrichment burns one per person; static.licdn.com URLs mean no real photo
metadata: 
  node_type: memory
  type: reference
  originSessionId: 70497397-25f3-4c4f-af31-d8a2961a3267
  modified: 2026-08-07T02:56:01.385Z
---

Apollo's plan on this account is **155 lead credits per calendar cycle** (cycle observed 26 Jul - 26 Aug 2026). Every `apollo_people_match` / `apollo_people_bulk_match` enrichment costs one credit per person, whether or not the field you wanted comes back. Hit zero on 6 Aug 2026 pulling profile photos for the ICP committee site; 3 credits left, reset 26 Aug.

Two things that cost credits for nothing if you don't know them:

1. **Ghost avatars.** When Apollo returns `photo_url` starting `https://static.licdn.com/aero-v1/...`, that is LinkedIn's default grey silhouette, not a person. Treat it as "no photo" and fall back to initials. On a 62-person pull only 22 had a real `media.licdn.com` image, so budget roughly a third hit rate for photos.
2. **LinkedIn CDN URLs expire.** Some `media.licdn.com` links 403/400 the moment you curl them, even with browser headers. Always download immediately in the same run, never hotlink, and expect a few to be dead on arrival with no way to re-fetch except spending another credit.

Also: `apollo_people_bulk_match` takes up to 10 per call and returns matches **positionally**, including a `null` for a non-match, so map results by input index, not by the returned `linkedin_url` (some matches omit that field entirely). One bulk call for 10 costs the same 10 credits as 10 single calls but is far cheaper in context.

Check the balance with `apollo_usage_stats_credit_usage_stats` before starting any enrichment sweep. See [[enrichment-doctrine-clay-not-lemlist]] for which tool should be doing enrichment in the first place.
