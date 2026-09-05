---
name: allhands-demo-footage-review-sep5
description: Sep 5 2026 all-hands demo footage review, 6 clips shot, 2 screens missing, 11 defects, rough cut assembled at 4:07 by build_rough_cut.sh
metadata:
  type: project
---

Sep 5 2026, six Loom clips in ~/Downloads reviewed frame by frame against
`motions/all_hands_sep14/Demo_Recording_Script.md`. Total footage 8:02 against a 4:50 target.

Coverage: Act 1 both halves (Cowork ask + finished AmeriHealth Caritas plan), Act 2 screens 3/4/5
(Clay enrichment, back-office maps, ICP committee ring), Act 3 lemlist. NOT shot: Act 2 screen 2
(Clay Audiences 312 count) and the Coda partner brief.

Geometry facts that matter for any recut: the four browser takes are identical, 1920x958 live
content at y=60, so they cut with no adjustment. The two Cowork takes are 1718x1078 and
1668x1044@y34, a 25px shift at the Act 1 straight cut. Every source is variable frame rate,
which is why a plain iMovie import behaves unpredictably.

Top defects: Loom control pill burned into all four browser clips (x15-75, y325-470, covers content
on maps and lemlist); Act 3 shot from the live pool `DWO Executives - Live Pool (Nate)` (803 leads,
Launch button in frame) instead of the 11-lead draft `All hands demo - recording`; error cells kept
in the enrichment clip; 6sense thread visible in the Cowork sidebar; the new-logo exclusion list
visible in the finished plan; unrendered `[{sender}]` / `[draft, Nate reads]` placeholders on screen.

Claims gate is clean: the Humana figures on screen (since 2020, 2 hours per agent per month,
AHT down 45s, occupancy up 4%) are all VERIFIED 1:1 and 1:many in the Value Repository. The
unverified one to watch for is "15 to 20 minutes per agent per day" (status CONFIRM).

Build: `motions/all_hands_sep14/rough_cut/build_rough_cut.sh` normalises everything to
1920x1080/30fps CFR/silent AAC, trims to slot, and concatenates with the four title cards plus two
brown gap slates. Output `~/Desktop/AllHands_Demo_RoughCut_Sep5.mp4`, 4:07. Re-run it after new
takes land. Review page: `motions/all_hands_sep14/Demo_Footage_Review_Sep5.html` (copy on Desktop).
Requires ffmpeg (installed via brew Sep 5; the Homebrew build has no drawtext, so text slates are
rendered from HTML through headless Chrome). Related: [[allhands-ai-session-package-aug31]],
[[naveen-call-sep2-demo-three-acts]], [[feedback-deliver-html-not-md]].
