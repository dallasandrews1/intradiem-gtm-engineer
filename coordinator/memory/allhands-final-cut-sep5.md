---
name: allhands-final-cut-sep5
description: Sep 5 2026 all-hands demo v2 cut assembled at 4:18 (Desktop), zero traps in frame, narration still unrecorded
metadata:
  type: project
---

The eight v2 screen recordings (Sep 5 2026, all in ~/Downloads: one `Claude - 5 September 2026.mp4` for Act 1, seven `Google Chrome - 5 September 2026*.mp4`) are assembled into `~/Desktop/Intradiem_AllHands_Demo_Sep5.mp4`, 4:18, 1920x1080.

Three facts that govern the next pass:

1. **No take has narration.** Seven have no audio stream; the Cowork take's track is digital silence at -91 dB (muted mic). The cut is a picture lock with a silent track attached. The voice pass is the only thing blocking the send to Jason (due Tue Sep 8).
2. **Act 3 is 19.5s against the script's 45s.** The lemlist take carries `[draft, Nate reads]` in the call bodies from 0:20 and a lemlist withdraw-invitation warning from 0:48.5. Only the opening window is clean.
3. **Act 1 has no per-person copy scroll.** `{{sender}}` and `[number]` sit in the voicemail bodies continuously from 0:20 to 1:08 of that take; no clean window over 1.5s exists inside it. Act 3 carries the rendered-copy proof instead.

Everything else the Sep 5 footage review flagged is fixed in v2: no Loom pill, no 6sense sidebar thread, no exclusion line, no error cells, no `Not verified` badges or FIND PHONE buttons, no launch button, Opus 5 High consistent, no composed fit score.

Rebuild with `motions/all_hands_sep14/final_cut/build_final_cut.py` — sources, trims, speeds and geometry are one table at the top; replace a take in Downloads and change two numbers. Cards are HTML in `title_cards/` (nine now: open, three act, three outcome, coda, end) rendered via headless Chrome.

QA method worth reusing: a Swift/Vision OCR binary reads text off every frame, then a fixed trap-string list is grepped across the whole finished file. 259 frames, 17 strings, zero hits. Far cheaper and more reliable than scrubbing renders. See [[feedback-deliver-html-not-md]].
