---
name: wave1-spoken-variable-sweep-aug2
description: Aug 2 2026 spoken-register sweep of wave-1 Lemlist variables (stars + airlines) against the say-it-out-loud bar; 8 loaded Finance leads patched in Lemlist to match the doc
metadata:
  type: project
---

Dallas asked for everything aligned with the spoken-voice bar (Aug 2 2026), extending [[reply-drafts-never-curt-aug2]] beyond the brief into the staged campaign variables the briefs render from.

What happened: swept the spoken-register variables (`vm_hook`, `voice_script`) in both wave-1 stage docs, 22 replacements in `motions/star_ratings/Lemlist_Variable_Stage_Jul31.md` (all 17 contacts) and 13 in `motions/uk_airlines/UK_Airlines_Wave1_Variable_Stage_Aug1.md`. Email-register variables (`opener_line`, `contract_line`) were left alone; they passed the Jul 31 critic cycles and are written for email, not speech. Named defects fixed: "why the movable points this cycle are operational" (many stars vm_hooks), "what it prices at 520 pounds a seat" (Suzanne Roddie), coined-phrase hooks ("the tomorrow problem", "the second ledger it created"), writerly flourishes in voice scripts ("the compensation clock does its quiet work", "staffed like admin, remembered like the flight", "trained, not hoped for", "turned schedule slack into a priced asset"), and "reached out" in three voice scripts.

Load state at sweep time: stars Finance (cam_2gy9hmEvMjYEuPZ8A) had 8 leads loaded (Goldberg, Marrone, Rains, Thornton, Qin, Miyasato, Yang, Lynch); all 8 PATCHed via the Lemlist API with the new vm_hook + voice_script, verified by re-export. Stars Quality and both Jack campaigns had zero leads loaded, so the docs are the source of truth there and future loads inherit the fixes.

Also learned and encoded: the action-brief fixture's autopilot sends must stage REAL campaign templates resolved with real staged variables, never invented leads or invented send copy. A concurrent staging had invented star-position claims about real plans (SCAN, Alignment, CareSource, Priority Health), which breaks the locked-qbp claims gate; replaced with the real E2/E1/breakup templates pulled from the Lemlist sequences. Guard note now lives in the fixture at `autopilot._sends_note`. Related: [[action-brief-format-v2-aug1]].

Follow-on fixes the same day: the sends-thread render exposed a greeting seam in both of Jack's draft campaigns (E1 ran "Hi {{firstName}}, {{opener_line}}" in one sentence while every opener_line starts with a capital, so sends would read "Hi Adrian, Running short haul..."); fixed via update_sequence_step, greeting now its own paragraph (UK Airlines stp_9oni2Xpgq6aXyMWXk, UK Insurance/FS stp_gvvaxLrpqJnEFHbx5, both campaigns draft, zero leads). Convention: opener_line is a full capitalized sentence and the template gives the greeting its own line. Also pinned in the format spec: lead-line separators are `·`, never em dashes (composers slipped twice). Final v2.2 samples in #relay-test carry the drafts and full-copy sends threads genuinely threaded.
