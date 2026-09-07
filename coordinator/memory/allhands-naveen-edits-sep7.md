---
name: allhands-naveen-edits-sep7
description: Naveen's Sep 7 2026 edits to the all-hands demo and how each was built without re-recording
metadata:
  type: project
---

Naveen's five notes on the demo (Slack DM, Sep 7 01:20 CDT), all built by Sep 7 evening into `~/Desktop/Intradiem_AllHands_Demo_v2_Sep7.mp4`, 4:38:

1. **Retitle** to "AI in action - GTM engineering: Using AI to widen the net". His wording verbatim on the opening card.
2. **System motion slide after the opener** showing the engine executing the three acts, with how AI works in it. Built as `scenes/system.html`: six steps (Signal, Find, Research, Write, Run, Reply) build one at a time, then green "runs itself" chips and orange "checkpoint" chips, then the three acts drawn as lanes over the same rail. Act 1 spans all six, Act 2 spans Find-Research, Act 3 spans Run-Reply.
3. **A short motion graphic before each act**: problem / how it's done / how AI solves. Built as `scenes/act1|act2|act3.html`, three revealed rows each. These REPLACE the old act title cards rather than adding to them.
4. **Ally brief to slides.** Built partly: two slides (`coda1`, `coda2`) framing the real page, which still runs 14s between them. Reasoning given to Naveen: the brief being a live page Frank opens himself is the point of the coda; all-slides would make it look purpose-made for the video.
5. **Send the script.** `Demo_Handoff_Naveen_Sep7.html` carries the three act paragraphs (his ask, so he can build his own graphics on the same claim) plus the full 23-line timecoded read.

He also said "not suggesting we re-record this" and "if it's too much work we can ditch it". Nothing was re-shot; every new segment is built HTML.

**Scene animation pattern worth reusing.** Each scene page reads `?k=<index>` and draws its own state, so `scenes/build_scenes.py` renders keyframes with headless Chrome and cross-dissolves them into an mp4. Deterministic, fast, no frame-by-frame render, and a copy change is a text edit. See [[allhands-final-cut-sep5]] for the assembler and QA sweep.

Still open: the voice pass (narration re-cut to 23 lines, 551 words, 1.98 w/s; booth page updated). Tuesday Sep 8 Dallas and Naveen align on tone-setting so the intro and the read land as one piece.
