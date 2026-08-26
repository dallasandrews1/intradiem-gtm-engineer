---
name: feedback-sf-presence-is-info-not-exclusion
description: "Dallas's Aug 25 2026 rule for the back-office maps: being in Salesforce does NOT remove a person; only people actively involved in the current front-office customer relationship (on the AM's Relationship Map / sponsor line) stay off; SF-known back-office leaders (Michael Campbell type) stay on the map tagged 'in Salesforce'"
metadata:
  type: feedback
---

Aug 25 2026: after I removed 13 Salesforce matches from Inger's back-office maps, Dallas: "don't remove contacts here in these lists if they aren't actively involved in our current customer deals in the front office. We still need to know who these people are if they are explicitly relevant to back office, like michael campbell etc."

**Why:** the map's job is to show who runs the back office at a customer. A Salesforce record (often stale, often from a prior employer or a one-off lead) is context for Inger, not a reason to hide the person. Mary Ann's rule is about the sponsor's reporting line, not about CRM presence.

**How to apply:** exclusion = on the AM's existing Relationship Map or in the sponsor's line, or a contact-center / front-office role. Salesforce presence = a green "in Salesforce" tag on the card (with the SF company where known). Common-name possibles get "confirm CRM badge". `build_map_build_sheets.py` implements this via SF_FLAG; nothing is dropped for SF presence. Related: [[feedback-maps-before-clearance-aug25]], [[inger-account-maps-build-aug25]].
