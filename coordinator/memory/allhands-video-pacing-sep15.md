---
name: allhands-video-pacing-sep15
description: All-hands demo scenes are timed from reading load, not by hand; 7-minute cap, time comes out of footage not scenes
metadata:
  type: project
---

The all-hands AI demo (`motions/all_hands_sep14/`) was re-timed on Sep 15 2026 because
the scene and card holds were faster than the room could read or Dallas could narrate
over. Naveen had already flagged it on Sep 9: "make sure the video flows slow or fast
enough for you to match with script," and he wants it presented live, not pre-recorded.

Hold time in `scenes/build_scenes.py` is now DERIVED from the words each keyframe puts
on screen (`SETTLE + load/READ`, `PACE` env var scales the whole film), not typed in by
hand. Add a row to a scene and it re-times itself. `final_cut/retime_cues.py` pins every
narration line to something in the picture, one line per scene reveal.

**Why:** hand-set holds gave a 21-word bullet 2.0s (~630 wpm of reading demand) while a
chip got the same 2.0s. The old cue sheet also had one sentence covering a four-row
build, so the scenes had dead air while the text flew past.

**How to apply:** hard cap is 7:00 for this video. When scenes need more room, take the
time back out of slack in the FOOTAGE, off the HEAD of each clip so every shot still
ends on the frame it was cut to end on. Never buy runtime back by speeding the
explanation slides. Target 125-155 wpm per line; `retime_cues.py` flags anything faster.
Related: [[deliverable-strength-framing]], [[naveen-facing-comms-rules]].
