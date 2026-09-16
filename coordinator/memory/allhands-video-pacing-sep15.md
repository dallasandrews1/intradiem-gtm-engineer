---
name: allhands-video-pacing-sep15
description: Slides carry headlines and the voice carries the sentence; scene holds = longer of read-time and say-time, 7-minute cap
metadata:
  type: project
---

The all-hands AI demo (`motions/all_hands_sep14/`) was re-timed and rewritten on Sep 15
2026. Naveen flagged it on Sep 9: "make sure the video flows slow or fast enough for you
to match with script," and he wants it presented live, not pre-recorded.

Two separate problems were being solved with one lever. **Reading load** is what makes a
room feel behind, and that is fixed by shorter on-screen copy, not more seconds.
**Talk time** is what Dallas needs to narrate, and that is fixed by seconds. Adding time
alone left paragraphs on screen that he then had to read off the slide.

So: on-screen copy is now a headline of roughly eight words, a fragment not a sentence,
and the narration carries the full thought. In `scenes/build_scenes.py` each keyframe is
`(words newly on screen, the line said over it)` and its hold is the LONGER of reading it
and saying it, so the picture cannot get ahead of the script. `final_cut/retime_cues.py`
imports those same lines, so a line and the picture it runs over cannot drift apart.

**How to apply:** hard cap is 7:00. When scenes need more room, take it out of slack in
the FOOTAGE, off the HEAD of each clip so every shot still ends on the frame it was cut
to end on. Never buy runtime back by speeding the explanation slides. If a scene still
feels long, cut words from the slide before cutting seconds. `retime_cues.py` flags any
line needing over 156 wpm. `PACE` env var scales the whole film.
Related: [[deliverable-strength-framing]], [[naveen-facing-comms-rules]].
