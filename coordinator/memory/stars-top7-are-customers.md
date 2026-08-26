---
name: stars-top7-are-customers
description: "6 of the top 7 Stars Tier A+B parents ($1.94B of $2.51B addressable) are current Intradiem customers, valid for back office not Stars cold"
metadata: 
  node_type: memory
  type: project
  originSessionId: 526d8dd8-98ee-4387-9c92-b5cdef3423c8
  modified: 2026-08-06T21:17:49.947Z
---

In `StarRatings_PersonaPull_RunConfig_TierAB.csv` (32 Tier A+B parents), six of the top seven by 2028 addressable value are current Intradiem customers: **Humana ($1,082.8M), UnitedHealth ($315.9M), CVS/Aetna ($224.5M), Elevance ($142.9M), HCSC ($105.6M), Molina ($69.9M)**. **Centene ($187.0M) is the only clean name in the top seven.**

That puts **$1,941.6M of the $2,511M Tier A+B addressable total on the customer list**, leaving 26 of 32 parents cold-eligible.

**Why:** this is not a defect to fix, it's a routing rule that is easy to get backwards. The Stars motion drops customers to zero, so those six are invalid for Stars cold outbound. The back-office motion inverts that (`customer_flag` is deliberately not an exclusion) and `BackOffice_ICP_v1.md` names them as Tier-1 warm anchors. Same parent orgs, opposite gate treatment.

**How to apply:** source those six under the back-office spec only, never the Stars spec, and land them in a separate destination table. When anyone cites the ~$2.5B Stars addressable figure as the cold-outbound opportunity, correct it: the cold-eligible slice is ~$569M across 26 parents. Related: [[gate-1-denylist-json-misses-90-customers]], [[sixsense-si-credits-expire-aug30]].
