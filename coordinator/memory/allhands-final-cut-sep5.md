---
name: allhands-final-cut-sep5
description: Sep 5 2026 all-hands demo picture locked at 4:24 with narration script and booth page built; voice pass is the only thing left
metadata:
  type: project
---

Picture is locked at **4:24** as `~/Desktop/Intradiem_AllHands_Demo_Sep5.mp4`, built from the eight v2 screen recordings in `~/Downloads` (one `Claude - 5 September 2026.mp4` for Act 1, seven `Google Chrome - 5 September 2026*.mp4`).

**The only open blocker is Dallas's voice.** Seven takes have no audio stream; the eighth measures -91 dB (muted mic). Everything else is removed as friction:

- `final_cut/build_final_cut.py` — the assembler. Sources, trims, speeds, geometry in one table at the top.
- `final_cut/cues.json` — 17 narration lines written to the locked timecodes, 534 words, 2.02 w/s overall, no beat above 2.6.
- `final_cut/Narration_Booth.html` (Desktop: `AllHands Narration Booth.html`) — plays the cut, shows the line in large type with seconds remaining and the pace that line needs. Space plays, R restarts, arrows step cues.
- `final_cut/add_narration.py` — takes any voice file, high-passes at 80 Hz, loudnorm to -16 LUFS, muxes onto the picture without re-encoding video. `--offset` shifts the voice.

Act balance after easing: Act 1 34.6s (scroll eased to 0.75), Act 2 128.3s, Act 3 27.0s (the lemlist window is pixel-frozen 2.7-15.9s so the middle was eased to 0.6 with nothing moving to slow), Coda 48.2s.

Two content windows stay out of the cut permanently: the strike-plan take carries `{{sender}}` and `[number]` continuously 0:20-1:08, and the lemlist take carries `[draft, Nate reads]` from 0:20 plus a withdraw-invitation warning from 0:48.5. Also caught late: the ICP committee page scrolls into beta terms and early-adopter pricing at 48.5s of that take, so that window hard-stops at 48.0.

**QA method worth reusing on any screen-recorded deliverable.** A Swift/Vision OCR binary reads text off every frame, then a fixed trap-string list is grepped across the whole finished file. 529 frames at 2fps, 23 strings, zero hits. It caught the beta-pricing scroll that eye-scrubbing and the earlier review both missed. See [[feedback-thorough-at-all-costs]] and [[feedback-deliver-html-not-md]].

Pages: `Final_Cut_Review_Sep5.html` and `Narration_Script_Sep5.html` in `motions/all_hands_sep14/`, both staged on the Desktop. Superseded v1 rough cut still sits on the Desktop as `AllHands_Demo_RoughCut_Sep5.mp4`.
