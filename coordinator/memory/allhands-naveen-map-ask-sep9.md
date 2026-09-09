---
name: allhands-naveen-map-ask-sep9
description: "Sep 9 2026: Naveen's three video notes (operating-map system view as motion graphics with ZoomInfo, drop 'Nine campaigns, one engine', strong AI focus for the AI Champions audience) built into v3 the same day: flow scene after the title card, AI named on screen and in the read, 4:57"
metadata:
  type: project
---

Sep 9 2026 11:09 to 11:23 CDT, Naveen DM, three notes on the all-hands video (otherwise approved to send to Sierra):
1. Screenshot of gtm-operating-map.pages.dev Present slide 1 ("Nine campaigns, one engine.", statband, sources-to-outcomes diagram). Asked if it could be a useful addition, "render through some form of motion graphics explaining the flow of data from these systems into the sequencer", ZoomInfo included, drop "Nine campaigns, one engine", only if not much rework.
2. "This demo/segment is all about how we use AI through the AI champions network. I'd recommend a strong focus on AI while you walk through this."
3. Same DM: Sierra's back-office messaging doc landed, Dallas already updating the lemlist BO messaging from it; Naveen introduces Jean Ann and Mike Regan at the all-hands; Naveen talking to Tom about LinkedIn Ads Sep 9.

**Built Sep 9 (v3, ~4:57, no re-recording):**
- `scenes/flow.html`: "Every source, one AI engine." Six sources (Salesforce, CMS Star Ratings, account maps, intent, market signals, ZoomInfo lists) draw in one at a time, then the AI engine box (chip "AI runs it"), then Sequences (AI-written, rep-owned) and AM clearance (chip "Human checkpoint"), Meetings, Salesforce, the two-week loop, then a dot travels the whole path. Placed after the title card, before the six-step system scene. Trimmed versus the map: no "ZoomInfo, proposed", no LinkedIn ads lane (not running; Naveen is asking Tom), no statband, no council or VITO labels.
- Pulse phase = new `PULSE` mode in `scenes/build_scenes.py`: frames at 12 fps from `?k=11&p=0..1`, minterpolate to 30 fps. Reusable for any scene that needs one moving element.
- `system.html` chips now read "AI runs it" and "Human checkpoint".
- Narration: 25 cues, AI named on every line where it does the work ("the AI reads the public record", "drafted by the AI", "One AI engine"). `final_cut/sync_narration.py` regenerates the booth and the script page from cues.json.
- Output `~/Desktop/Intradiem_AllHands_Demo_v3_Sep9.mp4` (silent; Dallas records the voice in the booth, then `add_narration.py`). The v2 on the Desktop was never narrated (mean volume -91 dB), so the insert cost nothing on the voice side.

**Rule kept:** everything on screen exists and runs today. The full map with the proposed lanes is Naveen's live closing slide, not the recording.

Related: [[allhands-naveen-edits-sep7]], [[allhands-demo-v3-narrated-sep4]], [[operating-map-sep3-refresh]], [[feedback-6sense-replacement-lobby]].
