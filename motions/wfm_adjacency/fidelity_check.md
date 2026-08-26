# Fidelity Check — motion-stamp library vs live WFM Email 1
Date: 2026-07-18 · Purpose: prove that [voice_core] + [stage_ladder E1] + [WFM motion_slots] reproduces the live `P2P Outreach Email` prompt with nothing dropped.

## Section-by-section map of the live Email 1 prompt

| Live Email 1 section | Covered by | Notes |
|---|---|---|
| "peer-to-peer composer... input one enriched contact... output ONE email" | stage_ladder E1 + slots WHO YOU ARE | E1 framing + persona voice |
| WHO YOU ARE (GTM engineer, floor fluency) | slots WHO YOU ARE | verbatim |
| THE CORE POSITION (additive, on top of WFM) | slots CORE POSITION | verbatim |
| Source Motion Check | slots SOURCE_MOTION_CHECK | verbatim |
| Subject ≤8 words; body 70-110 problem→reframe→ask; peer tone | voice_core OUTPUT + MESSAGE ARCHITECTURE | invariant |
| Top Signal Rule (sourced+dated-90d number gate; unsourced/benchmark = fail) | voice_core NUMBER GATE | invariant |
| No-number path = operational MOMENT | voice_core NUMBER GATE + slots SIGNAL SEMANTICS | principle invariant, the WFM moments live in slots |
| Never characterize their WFM platform as failing; no ROI/competitor/customer number; platform named at most once | slots MOTION-SPECIFIC BANS | motion-specific |
| Drop weak hedges | voice_core PLAIN SPOKEN | invariant |
| MESSAGE ARCHITECTURE (Tenbit++ arc) | voice_core MESSAGE ARCHITECTURE | invariant |
| PROOF BEAT (verified-repo named; industry-level qualitative; never invent) | voice_core PROOF BEAT | invariant |
| PERSONA ROUTING (wfm/cc_ops/coo_finance) | slots PERSONA ROUTING | motion-specific |
| COPY RULES (no em dashes, banned words, one idea, front-load) | voice_core COPY RULES | invariant |
| OPENER (don't narrate their world back; break stacked openers) | voice_core OPENER | **GAP FOUND + PATCHED 2026-07-18** — invariant principle added to voice_core; WFM BEFORE/AFTER examples stay in the gold standard |
| SENTENCE FLOW (stacking/chopping cure) | voice_core SENTENCE FLOW | invariant |
| PLAIN SPOKEN | voice_core PLAIN SPOKEN | invariant |
| GOLD STANDARD (Noemi example) | slots GOLD STANDARD | motion-specific |
| TOKEN USE (first name; company not welded to generic scenario) | voice_core TOKEN USE | invariant |
| OUTPUT (JSON subject+body, no signature) | voice_core OUTPUT | invariant |

## Result
**PASS.** Every section of the live Email 1 prompt maps to either voice_core (invariant) or WFM motion_slots (motion-specific). One gap (the OPENER principle) was found and patched into voice_core; nothing else was missing. The split is clean: voice_core holds what every motion shares; slots hold the WFM wedge, personas, signal moments, bans, and gold standard.

## What this proves
Assembling [voice_core] + [stage_ladder] + [a filled motion_slots] reproduces a known-good motion prompt. A NEW motion is now: fill motion_slots, assemble E1-E5, copy-sharpen. The workflow template (next step) can be cut from the WFM graph with confidence that the prompt layer is faithful.

## Note on E2-E5
The sharpened WFM Email 2-5 (WFM_Email2to5_Stage_Prompt_Build_Sheet.md) already match stage_ladder E2-E5 + these WFM slots. No gap found there.
