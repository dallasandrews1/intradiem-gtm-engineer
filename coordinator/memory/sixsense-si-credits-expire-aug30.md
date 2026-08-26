---
name: sixsense-si-credits-expire-aug30
description: "183,318 6sense SI credits expire Aug 30 2026; 1 credit = 1 person incl. email + phone; sourcing specs written Aug 6"
metadata: 
  node_type: memory
  type: project
  originSessionId: 526d8dd8-98ee-4387-9c92-b5cdef3423c8
  modified: 2026-08-06T21:17:31.905Z
---

Intradiem has all three 6sense products (Sales Intelligence, Data Workflows, ABM). Balances as of Aug 6 2026: **SI 183,318 / Data Workflows 15,225 / ABM 15,471, all expiring Sun Aug 30 2026** (last working day Fri Aug 28). Credits do not roll over.

**Economics that make this matter:** 1 credit unlocks 1 person including email(s) AND phone(s) together. Unlock is free when no data exists, but CSV export charges 1 credit regardless (so always filter `Has Direct Dial = True` first). Unlocked records re-enrich free for 12 months, through Aug 2027.

**No Enrichment API credits** (only Company Identification API), so `POST api.6sense.com/v2/enrichment/people` is unavailable. Do not buy API credits while this pool expires. Path is SI Discovery UI → CSV (25K/export ceiling) → Clay in waves.

Sourcing specs live at `Intradiem GTM Engineer/SixSense_SI_Sourcing_Sprint_Specs_Aug6.md`.

**The finding that reframes it:** every motion with a defined universe is far too small to absorb the pool. Stars (32 parents) + Back Office (101 accounts) + Install Base together are ~4-5K contacts, ~3% of the balance. The cap rules (`3 per persona`, Tier-1-only) were Clay-scarcity artifacts. The two motions that could absorb volume, WFM-Adjacency and Cost-Mandate, have no account universe at all. WFM-Adjacency was explicitly blocked on "separate credit GO" and SI Discovery's Technology Used + Job Postings filters are exactly its spec, so it became the priority spec. Realistic total spend ~31,700; ~152,000 will expire unused and that is the correct outcome.

See [[gate-1-denylist-json-misses-90-customers]] and [[stars-top7-are-customers]] for the two gate findings this surfaced.
