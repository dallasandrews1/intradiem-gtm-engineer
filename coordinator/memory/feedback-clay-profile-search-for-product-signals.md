---
name: feedback-clay-profile-search-for-product-signals
description: Sep 9 2026 correction from Dallas; when a signal lives on LinkedIn profiles (a product named in a role), run Clay advanced search on headline/about/current-role text first, never call it unreachable because web search cannot see LinkedIn
metadata:
  type: feedback
---

On the UPT displacement sweep I told Dallas LinkedIn profiles were "the one source this sweep could not reach" because web search cannot index them. He pushed back: Clay reaches LinkedIn every day. He was right. Clay advanced search (`clay search query-mode`) matches `headline`, `about` and `experiences.any(description contains ...)` at 0 credits; scoped to a domain list with `clay.filter_to_companies((...))`; batches of about 45 domains (181 in one query times out); `--limit 40` and sequential batches (parallel calls collide). Enrich Person (0.5 cr) returns the full profile text to read the exact sentence. Skills sections are not indexed; job postings are, but returned nothing for these product terms.

**Why:** the profile pass found six product-confirmed accounts in an hour for five credits after ~130 web searches found four. Web search reach is not the ceiling; Clay is.

**How to apply:** for any "who uses product X" or "who has skill X" question, run the Clay profile search before declaring a gap or handing it to a rep's Sales Nav. Web search stays for vendor case studies and press. Related: [[feedback-person-level-intent-not-company]], [[clay-free-sourcing-path]], [[upt-displacement-verint-nice-sep9]].
