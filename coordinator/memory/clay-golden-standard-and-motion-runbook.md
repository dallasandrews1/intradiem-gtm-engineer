---
name: clay-golden-standard-and-motion-runbook
description: "STANDING PROCESS LAW ratified Jul 15 2026: the permanent rules for building any Clay GTM motion — one workbook per motion, repo is spec-only, files-first, 8-layer L0-L8 architecture reused, wave discipline, credit governance"
metadata:
  node_type: memory
  type: feedback
  originSessionId: catchup-jul17-2026
---

`Clay_Golden_Standard.md` + `New_Motion_Build_Runbook.md`, ratified Jul 15 2026, is the permanent standard for every future motion (Cost-Mandate, then WFM-Adjacency, then Install-Base). Core rules, all load-bearing:

- **One motion = one Clay workbook** (Back Office was the precedent). Shared assets (Verified Metrics, Product-Angle Map, ICP Rubric, customer exclusion) join by Lookup or seeded copy, never table adjacency.
- **The repo engine is config + reference scorer + tests ONLY, never a parallel build.** Clay is the live source of truth. Violating this has a real documented cost: the MessageGen prompt drifted a full version behind live (repo trailed v2.2.1 while Clay ran v2.2.3), flagged in the standard itself as a known drift to reconcile. Ties to [[built-means-in-the-live-tool]].
- **Files first, Clay once:** draft every formula/prompt/critic as a file, transcribe once, verify live.
- **8-layer architecture (L0-L8):** a new motion builds L0-L4 (sources, accounts, signals, contacts, messaging) and reuses L5-L8 (Send Queue, Sync, Reply/Attribution, Worklist) via `source_motion` tags — never rebuilt per motion.
- **Persona-key normalization (ratified same day):** canonical rubric keys are `coo_finance, cc_ops, wfm, cx, bo_claims, bo_shared`. The old `finance` key was standardized to `coo_finance` (tests 25/25 green).
- **Gate discipline, fail-closed, non-negotiable:** Send Queue is the single egress; `send_ready = critic PASS AND human_approved AND NOT claimed`; dry-run is the default state; nothing sends without an explicit in-session instruction.
- **Wave discipline:** source the full universe once at kickoff; gate expensive layers (enrichment, MessageGen, campaign load, sync) in waves of 30-50 contacts; no new wave until the prior wave's replies are read.
- **Credit governance:** every enrichment run needs a pre-estimate, named motion, expected yield, and ledger row before firing; 60% burn triggers a mid-burn review.

**Hard-won gotchas worth remembering as standing traps:** sync clicks miss silently (always re-verify `Sent At`); full MessageGen re-rolls reintroduce figure errors (fix per-lead, never re-roll); never click "Create Claygent" (binds an unwanted agent template); never click "Create Clay email campaign" while exploring (creates a stray campaign that can push real leads into a draft — this exact failure already happened once, see [[clay-build-audit-jul12]]); optional enrichment inputs must have "Required to run" OFF or they hard-fail and wipe drafts.

**Why:** this codifies lessons paid for in real credits and real near-misses (the stray campaign leak, the MessageGen drift) into a rule every future motion build must follow, rather than relearning them per motion.

**How to apply:** treat this as the checklist before starting ANY new motion build. Ties to [[clay-motion-factory-scaffold-system]], [[verify-tool-capabilities-before-instructing]].
