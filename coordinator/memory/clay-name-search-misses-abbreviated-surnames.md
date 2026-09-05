---
name: clay-name-search-misses-abbreviated-surnames
description: A Clay name-based people search returning nothing is NOT evidence a contact left; anyone who abbreviates their surname on LinkedIn is invisible to it. Confirm with the URL-keyed Enrich Person routine.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3fbe2bea-a6b2-440e-8a40-06dcd40494a7
  modified: 2026-09-05T20:48:13.719Z
---

Found 5 Sep 2026 verifying the Centene buying committee. Corey Taliaferro returned nothing from
three separate free Clay searches: `find-and-enrich-list-of-contacts` at centene.com,
`find-and-enrich-contacts-at-company` with a `names: ["Taliaferro"]` filter at centene.com, and the
full 20-contact roster at carolinacompletehealth.com. Clay's coverage of both companies is good, so
absence looked like a departure.

He had not left. His LinkedIn display name is **"Corey J. T."**, not "Corey Taliaferro". Every
name-based path matches on the displayed name, so an abbreviated surname makes a person invisible
to all of them.

**The rule: a name-based miss is never evidence of a departure.** Confirm with the URL-keyed
routine before concluding anything:

```
clay routines runs start "function:t_0thx4ohpCNT3KNijyVo" \
  --input '{"items":[{"id":"p0","inputs":{"Professional Profile URL":"<linkedin url>"}}]}'
clay routines runs get <runId> --wait 60
```

0.5 credit per person. The reliable field is `current_experience`: populated with `is_current: true`
means still employed (it returned title, company, summary, locality and a 2023-03-01 start date for
Taliaferro); empty means left or retired. Same routine `verify_live.py` uses in the back-office map
pipeline, verified Aug 31 2026 against two known-stale people.

Also learned the same day: paid data points in the Clay MCP surface (Email, Summarize Work History,
Find Thought Leadership) only enrich contacts a search already returned. They cannot find someone
the find step missed, so spending credits on a failing company-scoped search is wasted. The
URL-keyed routine is the paid path that actually resolves a missing person.

Third-party aggregators are worse than Clay here and cost credibility: on the same five contacts,
RocketReach reported a stale title for Jesse Lewis and web results falsely suggested Matthew Tran
had moved to Aetna (a current-customer exclusion). Clay showed both were wrong. Check Clay before
raising a departure or exclusion-gate flag. Related: [[tam-seed-data-never-swapped-sep5]],
[[clay-free-sourcing-path]].
