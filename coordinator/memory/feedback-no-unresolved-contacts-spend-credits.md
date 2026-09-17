---
name: feedback-no-unresolved-contacts-spend-credits
description: "Sep 17 2026: on seller-facing maps and rooms no contact may stay unresolved, not found or dual; spend Clay credits (Enrich Person 0.5 cr, contact details 12.4 cr) to settle every name before delivery"
metadata:
  type: feedback
---

Sep 17 2026, mid-build of Keegan's three-account package, after the free Clay MCP live check left 55 names not_found and 8 dual: "none of these contacts should be unresolved or not findable... use whatever credits in Clay required to do this thorough and correctly."

**Why:** the free find-and-enrich check is company-scoped, so a leaver comes back as not_found instead of left, and it cannot see a second LinkedIn company page (Citizens Financial Group, Inc. versus Citizens). A not_found pile reads as unfinished work, and these packages go to AEs and the SVP of Sales.

**How to apply:** after the free bridge, run the paid Enrich Person routine (function:t_0thx4ohpCNT3KNijyVo, 0.5 cr, accepts LinkedIn URL or Email) on every map card, every not_found name that Salesforce holds a URL or email for, and both profiles of every dual; find URLs for the rest by web search, then enrich those too. Every name ends as current (live title), left (now where), or no profile exists. Script: motions/back_office_expansion/keegan_resolve.py. Do not ask before spending at this scale; see [[clay-spend-posture-aggressive]]. Related: [[keegan-three-account-package-sep17]].
