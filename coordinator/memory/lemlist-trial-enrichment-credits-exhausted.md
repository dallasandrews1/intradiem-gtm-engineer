---
name: lemlist-trial-enrichment-credits-exhausted
description: "lemlist free-trial enrichment credits ran out Aug 6 2026 and fail SILENTLY (empty results, not an error); enrich contacts in Clay instead"
metadata: 
  node_type: memory
  type: project
  originSessionId: d3b88697-23fb-4296-865e-5eaecdcf9851
  modified: 2026-08-06T19:54:07.760Z
---

As of Aug 6 2026 the lemlist free trial's enrichment credits are exhausted. The dangerous part is the failure mode: `add_leads_to_campaign` with findEmail/findPhone returned **empty fields with no error** for the whole Hartford batch. Only an explicit `bulk_enrich_data` retry surfaced the real cause, `MISSING_FUNDS` on every item.

**Why:** an empty enrichment return is indistinguishable from "this person genuinely has no data on file." A wave loaded on that assumption ships with no phones and no emails and nobody notices until sends silently skip.

**How to apply:** never trust a lemlist enrichment return without counting populated fields afterward. Enrich in Clay instead, which has ~72.5K credits: routine `Enrich Person and Find Contact Details` (`function:t_0thx4ojyQd6uNhDf44G`), input is `{"items":[{"id":"...","inputs":{"Social Profile URL":"<linkedin url>"}}]}` via `clay routines runs start ... --input <file>`, 12.8 credits per contact, returns both Work Email and Mobile Phone. Then write results back onto the lemlist leads with `update_lead`.

Clay also beat lemlist on accuracy in the same run: lemlist matched Patrick Savage to `patrick.savage@csn.edu` (wrong person, different company) while Clay returned the correct `@citizensbank.com` address, and Clay resolved two surname mismatches (`stacy.stanton@`, `tayton.guio@`) that a firstname.lastname pattern guess would have got wrong. Treat lemlist enrichment output as needing a sanity check on the domain, not just on presence.

Related: [[blitz-citizens-hartford-aug6]]
