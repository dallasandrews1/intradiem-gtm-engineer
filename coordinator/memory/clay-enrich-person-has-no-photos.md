---
name: clay-enrich-person-has-no-photos
description: "Clay's managed Enrich Person function returns no profile photo; Apollo does, so profile pictures must come from Apollo"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6ca2e88b-0881-40b3-8ef1-9f091aa27912
  modified: 2026-08-06T20:59:12.629Z
---

Clay's managed **Enrich Person** function (`function:t_0thx4ohpCNT3KNijyVo`, input `Professional Profile URL`)
returns `picture_url_copy` and `picture_url_orig` as **null** — verified 2026-08-06 on two LinkedIn profiles
where Apollo had a real photo for one of them. There is no image URL anywhere in Clay's response. It does
return a good `headline`.

Apollo's `apollo_people_bulk_match` (match by `linkedin_url`, max 10 per call) returns `photo_url` plus
`headline`. On a 40-person sample, 23 had a real photo and 17 returned LinkedIn's default ghost avatar
`https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2` — treat that exact URL as "no photo"
and fall back to initials.

**Why:** Dallas's default is to prefer Clay for its premium capabilities, but for profile pictures
specifically Clay does not carry the field, so preferring it silently yields no photos.

**How to apply:** for profile photos, use Apollo, not Clay. Download the images at build time rather than
hotlinking — `media.licdn.com` URLs are signed and expire (2 of 23 already returned HTML instead of an
image because their `e=` token had lapsed). Two more Apollo gotchas: it masks surnames on some records
("Bridget R"), and it sometimes omits `linkedin_url` entirely, so match results **positionally** against
request order (`missing_records` is 0 when order is preserved) rather than by name or URL.

Related: [[pages-new-project-522-window]].
