---
name: clay-canadian-parent-entity-resolution
description: Clay find-and-enrich resolves bmo.com to the US subsidiary; how to source a Canadian-parent enterprise committee
metadata: 
  node_type: memory
  type: feedback
  originSessionId: abc534b8-ad02-4250-b585-65267c44753a
  modified: 2026-07-29T19:48:16.031Z
---

For the BMO strike room (Jul 29 2026), Clay `find-and-enrich-contacts-at-company` on `bmo.com` resolved to **BMO U.S.** (Chicago retail), returning US branch/retail staff, not the Canadian enterprise leadership the forcing function pointed at. Parent-entity LinkedIn slugs both failed: `/company/bmo` resolved to a garbage Austrian entity (surfaced only frontline Canadian CSRs), and `/company/bmofinancialgroup` returned empty.

**Why:** Big Canadian enterprises with a US arm fragment across multiple LinkedIn/company entities, and Clay's resolver keys off the domain to the wrong one. Chasing the parent slug burns credits for near-zero return.

**How to apply:** For a Canadian-parent enterprise committee, do NOT try to source the C-suite anchors through Clay. Take the named enterprise execs from live research (exec-bio URLs) and run them **LinkedIn-led** (no fabricated email). Use Clay only for the reachable operational seats (which resolve fine via the US-entity domain), email-led with a ZeroBounce gate. Dominant BMO email pattern was `firstname.lastname@bmo.com`; watch for lastname-only guesses (e.g. `gallagher@bmo.com`) and ZB-validate them. This will recur on [[TELUS]] (account 3, Canadian parent with TELUS International / US arm). See CostMandate_BMO_StrikeRoom_Sequence_v1 for the worked committee.
