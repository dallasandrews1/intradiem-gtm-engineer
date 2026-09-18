---
name: keegan-execution-kit-sep18
description: "Sep 18 2026: the execution layer on top of the Keegan account package (one-pager shelf, sequence blueprint, what-to-send-when selector, Vanguard lemlist draft); staged not deployed; builders, the pair method, and the defects found"
metadata:
  type: project
---

**Trigger (Sep 18 2026):** Dallas asked what could ship alongside the planning portfolio to help the sales org execute it, then said build items 1 to 3 plus the Vanguard draft. "Planning portfolio" = the Sep 17 package in [[keegan-three-account-package-sep17]].

**Built, all STAGED, nothing deployed, 0 credits:**
1. **One-pager shelf, 22 pages** (Citizens 7, The Hartford 8, Vanguard 7) on the locked partner-followup-onepager template, every page one Letter page. Persona pages (contact center or service, workforce, operations, claims, transformation, finance) plus finding pages (Citizens fraud and disputes, Hartford contact center redesign, Vanguard Workplace return, first year in seat on all three). `motions/keegan/accounts/shelf.py` + `build_shelf.py` -> `deploy-save-rooms/<slug>/keegan/one-pagers/<id>/`, PDFs in Desktop `Keegan Execution Kit - Sep 18`.
2. **Sequence blueprint per account** (`build_kit.py` -> `.../keegan/sequence/`): all 122 mapped people get exactly one status (in sequence, wave two, Keegan's door, wave three, wave four, held), the touch ladder names angle + asset per touch, no message bodies, no contact details. Caps: 12 per wave, 2 per manager per wave.
3. **What-to-send-when selector** injected into each room by an optional import in `build_rooms.py` (room diff = header links line + the new section only). Function + moment + "in seat under a year" -> one page. "Not now" returns send nothing plus the account's next dated moment.
4. **Vanguard lemlist draft** `cam_fZe5WbdMsERQpLwxe`, duplicated from the Hartford blitz, paused, 0 leads. Copy of record `motions/keegan/blitz_vanguard_copy_sep18.py/.json`, build record `Blitz_Vanguard_Build_Sep18.md`, wave-one variables CSV staged, not loaded.

**The pair method (reuse for the next AE):** each account gets a small library of PAIRS, one sourced finding about the account's operation plus the one thing Intradiem does about it. A page picks three pairs and adds its own subhead and gap, so the template's one-to-one mirror rule holds by construction and each fact is sourced and reviewed once. `base1..base3` reuse the approved account-level bullets verbatim by exec'ing the head of `build_onepagers.py`.

**Lessons:**
- The live blitz copy is NOT the Aug 6 no-proof copy. Since the Sep 3 doctrine it carries the blinded RBC "$6.1M a year" line and the Humana line. Read the live sequence before cloning; do not brief from the Aug 6 build doc.
- `duplicate_campaign` copies sequence + schedules, never leads, and lands paused. It is the right clone path.
- A background agent stalled mid-duplicate; the duplicate had succeeded. After any agent failure, read lemlist state before retrying or a second copy gets made.
- `update_sequence_step` echoes the full step list (about 1.5K tokens per call). Push bulk step edits from a JSON copy file through a worker and verify with one re-read.
- The Hartford's account rule (platform never named) killed the "alongside Amazon Connect" one-pager idea; it became "contact center redesign" with no platform named.
- The blitz copy also predates the **Sep 4 pressure standard** (doctrine addendum, line 150 on): exit talk and no-voicemail calls are banned in every net-new sequence. Cloned copy inherits those violations; the Vanguard draft was fixed, the live Citizens and Hartford copy was not. Read the WHOLE doctrine file, not the first 90 lines, before writing sequence copy.
- gtm-copy-reviewer reported the research files and Value Repository as missing when they exist (wrong search root) and failed everything on it. Give it absolute paths and tell it to stop and report if a named source is not found, never to fail the copy on absence.
- Open conflict: Value Repository DO-NOT-SEND blocks blinded peer outcomes, the Sep 4 structure review passed the blinded RBC $6.1M line, and it is live. Dallas to settle.
- Colleague-facing pages carry no defect ledger ([[deliverable-strength-framing]]); defects went to `automation/logs/keegan-execution-kit-2026-09-18.md` and to Dallas in chat.

**Defects and open points found (Dallas's hand):** Mike Bartolazo is loaded in the Citizens blitz as `mbartolazo@adt.com` (validated address `michael.bartolazo@citizensbank.com`), missed by the Sep 17 sweep; Weaver/voya.com still open. Both blitz campaigns read PAUSED on Sep 18 with 0 opens, 0 replies. Plan conflicts: Forte is in the wave two load and on the held route; Aldi and Brooks are in wave two and are Keegan's Oct 5 door; Vanguard has no outbound lane but the draft carries Nathan's sender. Vanguard email one's two CEO-letter numbers need a dated source.

Related: [[keegan-three-account-package-sep17]], [[feedback-no-draft-copy-to-ams]], [[enrichment-doctrine-clay-not-lemlist]], [[feedback-match-the-delivery-alex-loved]].
