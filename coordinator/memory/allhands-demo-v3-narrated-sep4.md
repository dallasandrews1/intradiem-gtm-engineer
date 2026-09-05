---
name: allhands-demo-v3-narrated-sep4
description: "Sep 4 2026: all-hands demo recording plan rewritten to v3 (eight screens, 5:00, Dallas's narration kept in the cut, one live execution) after Dallas said the v2 muted-plus-live-narration plan felt choppy; four asks staged for Naveen"
metadata:
  type: project
---

Sep 4 2026. Dallas said the planned recording (v2, Sep 2) felt awkward and choppy and he didn't know what to ask Naveen for. Diagnosis: the muted cut narrated live in the room, two live executions on camera, and fourteen screens across eleven tabs in 6:30.

**v3 decisions (files rewritten, HTML regenerated via motions/shared/md_to_page.py):**
- Each act recorded as its own take with Dallas speaking, audio kept, submitted narrated; played with sound at the all-hands, questions after.
- Eight screens: Claude Code strike plan (only live execution, 2x ramp if over 60s); Audiences single count (BO Leaders customers Dir+, ~312, no Prospect-to-Customer flip); Clay enrichment as a pre-recorded clip on the five named rows; backoffice-maps MetLife; icp-committees State Farm; lemlist one lead's sequence; Slack routed reply; Ally partner brief. Coda title card carries webinar routing and PM prototypes.
- 5:00 target, 5:30 cap. One browser window per act, joins behind title cards, script off frame via QuickTime Record Selected Portion.
- Deck AllHands_AI_Session.html patched (run of show Results 8:00 / Questions 10:00, act times 1:05 / 3:35 / 4:35, "Dallas, narrated"); patched copy sits in ~/Desktop/Intradiem Deliverables/deploy-allhands-ai/index.html, redeployed to gtm-allhands-ai.pages.dev Sep 4 (wrangler, deployment 6e30c7f2).
- Desktop package: ~/Desktop/Intradiem Deliverables/All-hands demo (Sep 4)/ (script v3, sheet v3, QA prep, title cards). Also live as subpages of the deck project (Sep 4): /script/, /sheet/, /qa/ on gtm-allhands-ai.pages.dev; deploy folder ~/Desktop/Intradiem Deliverables/deploy-allhands-ai/ holds index.html plus script/ sheet/ qa/ folders.

**Asks for Naveen (Slack draft given Sep 4):** confirm with Jason a narrated video is fine; send his set-up lines; watch the rehearsal take Fri Sep 4; confirm slot length.

**How to apply:** Demo_Recording_Script.md and Recording_UISheet_Sep2.md in motions/all_hands_sep14/ are v3 and supersede the v2 text quoted in [[naveen-call-sep2-demo-three-acts]]. Due Tue Sep 8. Related: [[allhands-ai-session-package-aug31]].

**Sep 4 evening verification pass (live systems, before recording):**
- Act 1 ask `Build the strike plan for AmeriHealth Caritas.` has never been run in Claude Code. The TAM engine's own plan for that domain prints placeholder dollars ($7.1M, $2,380/agent, a "Medicaid plan about your size" line) and `Owner: Jordan Kim` (placeholder seller). Act 1 is now two recordings (the ask + first 15s, then the finished output) joined by a straight cut; no dollar or owner line on tape. Dallas runs the ask off camera first and reports which path fired.
- Slack #gtm-outbound-nathan (C0BM9V6KGSG) and #gtm-outbound-jack (C0BN0JT9D6U) hold only Dallas's own posts (Jul 31 to Sep 1); no lemlist relay post has ever landed. Screen 7 cut; seven screens now.
- "All hands demo" campaign (cam_SxnHzvAr3WsvWPPeY): 11 of Jack's UK leads (Saga, L&G, D&G, Ageas), all variables filled; steps = email, LI visit, LI invite, call branch, email 2, LI message/call branch, breakup. NO voice note step. Demo lead = Kate Taphouse (Saga, lea_iewAHWD8KE9bw6stP); email 2 and LI message carry the "15-20 minutes per agent" figure (CONFIRM in the Value Repo, UK on Jack's authority), scroll past without pausing.
- Live counts Sep 4: segment 312, people 140,993. Partner brief resolves to /briefs/ally (no .html).
- Sep 5: act 1 off-camera run DONE in a Cowork thread with the explicit strike-sequence FULL-mode prompt (skill named, no dollars/owner/UNVERIFIED): fit 82 tier 1, D-SNP expansion trigger, 9-person committee, 5 touches each, Humana figures verified 1:many in the Value Repo, tape-safe. That thread = recording B; recording A (the short ask, fresh thread) is recorded after B. Demo lead block = Scott Mullaney.
