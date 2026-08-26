---
name: clay-builds-strategy-duplicate-ledger-jul17
description: "FEEDBACK: a Cowork thread scoped to the Clay Builds and Strategy folder created a second Clay_Credit_Ledger.md there instead of finding and appending to the canonical one in Intradiem GTM Engineer"
metadata:
  node_type: memory
  type: feedback
  originSessionId: catchup-jul17-2026
---

On 2026-07-17 a Cowork thread doing WFM-Adjacency Phase 1 planning work (build sheet + MessageGen variants) was scoped to `/Users/dallasandrews/Claude/Projects/Clay Builds and Strategy/` — a folder that turned out to be a sibling of `Intradiem GTM Engineer`, not nested inside it. That thread needed a credit ledger, didn't check whether one already existed elsewhere, and initialized a brand-new `Clay_Credit_Ledger.md` from scratch (fresh 72k-pool header, its own genesis row) rather than locating and appending to the real one. Two source-of-truth files then existed simultaneously for a few hours before catching it.

**Why this happened:** the project working directory for that thread didn't include `Intradiem GTM Engineer`, so a same-folder search wouldn't have surfaced the canonical ledger. Nothing prompted a check outside the immediate working directory before creating a governance file.

**How to apply:** before creating any ledger, registry, or other single-source-of-truth file (credit ledger, build-state registry, contact registry) in ANY project folder, search the broader `~/Claude/Projects/` tree first — Dallas runs several sibling project folders (`Intradiem GTM Engineer`, `Clay Builds and Strategy`, others) that all touch the same Clay workspace and the same 5,000/month credit governor. A file named exactly like an existing governance file appearing in a new folder is a strong signal to search before writing, not after. Resolution and canonical path: [[clay-credit-ledger-state-jul16]].
