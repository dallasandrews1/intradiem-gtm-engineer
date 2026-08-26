---
name: intradiem-30-60-90-plan
description: "Dallas's first-90-days plan at Intradiem (GTM Engineer) and the premortem fixes baked into it"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2918217f-55ac-4e42-8263-98f47c3d8610
---

Dallas's 30/60/90 plan for Intradiem (start Jul 6, 2026, reports to Naveen Thilagan). Deliverables in project folder, all blurple/creme personal brand: `Dallas_Andrews_30-60-90_Intradiem.pdf` (7-page designed leave-behind), `Dallas_Andrews_30-60-90_OnePager.pdf` (single-page, for attaching to a pre-start note to Naveen), `Dallas_Andrews_30-60-90_Intradiem.docx` (editable). Built from HTML via WeasyPrint (plan.html, onepager.html) + docx-js (build_docx.js) in the outputs scratchpad; fonts Lato (brand-approved). Pages are fixed-height .page divs, so adding content can overflow to blank pages, re-check pdfinfo page count after edits (target 7).

**Anchor:** flagship = turn Intradiem's one working motion (the intimate ~60-80 person invite-only customer-panel event) into an instrumented C-suite meeting engine. Arc: Days 1-30 learn + ship one external-data strike list; 31-60 build the engine; 61-90 stage first event + pipeline in motion. AI-native build system woven in via results, NOT front-loaded as a tool count (matches Busbee's judgment-over-activity read).

**Premortem (strategic-premortem skill, Jun 15) surfaced 3 blind spots, now FIXED across all 3 files:**
1. Pre-decided flagship / event ownership. Fix: plan reframed as a HYPOTHESIS to pressure-test with Naveen, not a plan of record; event language changed from "my flagship / productize the event" to "partner with whoever owns the event"; day-1 gate to find the owner and bring them in before touching it; "not annex the event" guardrail.
2. 90-day clock can't produce a measured/closed event result (events plan 3-4 mo out; enterprise sales cycle is long). Fix: day-90 promise changed from "measured first result + locked quarterly cadence" to "first event STAGED + pipeline IN MOTION + cadence appetite tested"; explicit line that closed revenue follows the sales cycle, not the 90-day clock.
3. Broken funnel downstream of the strike list (no sequencing tool, CRM/AE capacity). Fix: day-1 capacity gate (ask Nathan "if I hand you 20 C-suite targets tomorrow, what happens to them?"); build only behind a funnel that can absorb output.

**Uncontrollable risk named:** the event's value may BE its rarity (customer execs may not attend >1-2x/yr). So the plan bets on conversion + instrumentation of the existing cadence first, and tests appetite before promising any added frequency. Do not assume quarterly.

**Premortem verdict's single action item:** in first 1:1 with Naveen, ask (1) who owns the event and (2) what he wants the first 90 days to produce, and let answers reshape the flagship before it becomes a plan of record. Confidence: Moderate, tips to High if Dallas holds the flagship loosely.

See [[intradiem-interview-status]].
