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

**Sep 15 accuracy check, keep re-running this before any presentation:** lemlist showed
only 4 campaigns RUNNING, all Jack's UK/Netherlands. Nate's five North America campaigns
held 1,315 leads and had sent nothing since 1 Sep. Both the video ("seven campaigns
sending across North America and the UK") and the results slide ("8 campaigns sending,
live in North America and the UK") were wrong. Account maps had also moved 18 to 25.
Never carry a campaign or roster count from a previous build into a deck or a script;
pull it live and make the deck compute it, as `count_maps()` already does.

**Scene-layout lesson (Sep 15):** never size SVG label text by estimating characters
times a per-character width. Roboto is proportional and the estimate was wrong in both
directions, twice. Measure in the browser with `getComputedTextLength()` (or
`getBoundingClientRect` for HTML scenes) against the enclosing rect. The flow scene
shipped for a week with the feedback wire running through the "Read and adjust" pill as
a strikethrough, the engine footer breaking out of its box, and every source box trailing
a wire stub into empty space for ten seconds because the stubs were hardcoded `class="on"`
instead of waiting for the spine's keyframe.

**Campaign-count rule (Sep 15):** do not put a "campaigns sending" count on a
leadership-facing results slide. Lifetime across the four running lemlist campaigns
(Jack's UK/NL) was 79 leads, 87 messages, zero replies and zero meetings; Nate's five NA
campaigns hold 1,315 leads and are paused ON PURPOSE until launch, which is a deliberate
staging decision and should never be framed as a stall. A campaign count invites "how is
it going," and at ten weeks the send data cannot answer that. Show what the engine
produced instead: leads loaded, researched and gated. Also noted: NL Planners is bouncing
at 11.1%, which is the exact failure mode [[enrichment-doctrine-clay-not-lemlist]] and
[[lemlist-trial-enrichment-credits-exhausted]] warn about.
