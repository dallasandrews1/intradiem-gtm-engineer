---
name: lemlist-enrichment-credits-zero-sep3
description: "Sep 3 2026: lemlist team enrichment credits read 0 remaining (GET /api/team/credits), so verifyEmail, findEmail and findPhone on add_leads silently do nothing; verify through Clay (ZeroBounce) instead until the plan adds credits"
metadata:
  type: project
---

Sep 3 2026, while loading seven greylisted addresses into Stars - Fresh Pool / Quality with verifyEmail on: the add succeeded, but `GET /api/team/credits` returned credits 0 (freemium, subscription, gifted, paid all 0). lemlist reserves credits on submit and charges on result, so with a zero balance the verification never ran and nothing in the API says so; the lead record has no verification field.

**Why it matters:** any "verified through lemlist" claim is false until the balance is above zero. The Aug 2 findPhone run used trial credits that are now gone.

**How to apply:** check `GET /api/team/credits` before enabling any paid option on add_leads_to_campaign; when it reads 0, verify emails on the Clay side (workflow wf_0tk4jo5z7RjGKo3rvR8 or the ZeroBounce action, ~0.1 per address on top of the waterfall) and load plain. Dallas's ruling the same day: do not buy lemlist credits for this, lemlist never enriches, see [[feedback-enrich-in-clay-never-lemlist]]. Related: [[quality-fresh-pull-sep3]].
