---
name: allhands-marketing-pptx-sep10
description: "Sep 10 2026: marketing (Chelsea, Rachel) wants the exact AI-Champions-Demo PPT with the demo video embedded, due early afternoon; built from their template via motions/all_hands_sep14/build_pptx.py to Desktop/Intradiem Deliverables/All-hands demo (Sep 10)/; video stays silent, Dallas narrates live"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d47b7e1-bf43-4f06-b24b-3190c48f0ec2
  modified: 2026-09-10T14:36:12.088Z
---

Naveen DM Sep 10 2026 08:41 to 09:13 CDT: Chelsea and Rachel (marketing) need the slides for the all-hands AI Champions segment, "the exact ppt to be used", "video uploaded in the PPT", format intros / problem / demo / results, "absolutely need this doc by early afternoon". Naveen first proposed Dallas take the whole section as AI Champion, then paused pending Jen's / marketing's approval; he sets the stage either way. Jack O'Hagan also has his own segment.

Template `~/Downloads/AI-Champions-Demo (1).pptx`: 6 slides (AI Intro single, AI Intro two presenters, "What problem you were trying to solve with AI" comparison layout, Demo Video media placeholder full-slide, Results with an off-canvas icon library, Questions/Thank you). Theme Tahoma, accent1 2CB56E, accent2 F58220, accent5 014637. Recording guide link lives on SharePoint (Marketing site), not read (Graph 500).

Built: `motions/all_hands_sep14/build_pptx.py` (python-pptx 1.0.2, takes the scratch dir with the unzipped template as arg 1) writes `~/Desktop/Intradiem Deliverables/All-hands demo (Sep 10)/AI-Champions-Demo_GTM-Engineering.pptx` (49.6 MB, video 43 MB inside). Slide 1 two presenters (Naveen sets the stage, Dallas AI Champion), slide 2 Dallas-only HIDDEN alternate, slide 3 problem (three problems left, what we set out to do right, 1,800 hours line), slide 4 the v3 video full-bleed with poster frame, slide 5 results (370 hours forest hero, 4,600 / 12.4K / 950, then 8 campaigns sending, 23 account maps, 24 agents, ICP buying committees, orange time-saved bar), slide 6 questions. Speaker notes carry Naveen's set-up, Dallas's talk tracks, the 25 narration cues with timecodes, the if-pressed bases, and the Q&A one-liners.

Live counts used Sep 10: lemlist running = 8 (Nate: BO Expansion Insurance, Hartford, Citizens, Stars Resurrection; Jack: NL Planners, UU Water, Debbie Rolechange, THE Achmea contact); maps = Inger 12 + Nate 6 + JW 4 + Centene/Rachel 1; agents = 24 launchd plists.

Open: headshots (no photo on disk or via Slack/M365 tools; the two circular picture placeholders are empty, marketing or Dallas drops them in); which intro slide stays depends on Jen/marketing's call.

**Copy pass (Sep 10, Dallas's ask: no fluff, no AI-sounding lines):** title cut to "GTM Engineering: using AI to widen the net" (Naveen's phrase had AI twice); Dallas's title plain "GTM Engineer"; bios one or two plain sentences; no "judgment checkpoints", "gated", "orchestrated", "capacity created" on a slide, say "a person deciding at the points that matter", "checked", "time given back"; "About 1,800 hours" carries the estimate; "adopted by leadership" dropped from the committee card.

**How to apply:** rerun the script after any count change; never put the hour arithmetic on a slide; the video is silent on purpose (Naveen Sep 9 "Please do it live"). Related: [[allhands-naveen-map-ask-sep9]], [[allhands-final-cut-sep5]], [[feedback-no-showy-deliverable-copy]].
