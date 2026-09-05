---
name: allhands-ai-session-package-aug31
description: "Aug 31 2026: all-hands AI session package built per Naveen's DM spec (10-15 min, Jason Dowden moderates, 7 presenters); deck live at gtm-allhands-ai.pages.dev, 6:30 demo script (Claude Code -> Clay -> lemlist -> Inger maps closer), Q&A prep; demo still needs recording"
metadata: 
  node_type: memory
  type: project
  originSessionId: dd5f30e3-7cf4-4722-ba8d-1e4be25ec6ca
  modified: 2026-08-31T19:32:06.184Z
---

Naveen's Aug 31 DM set the all-hands section (week of Sep 14, Las Vegas): 10-15 minutes, tag-team with Naveen, Jason Dowden moderating 7 people sharing AI work. Format: intro slide, problem, Clay demo, results/time saved, questions.

Package (built Aug 31, folder `motions/all_hands_sep14/`):
- **Deck + run of show**: `AllHands_AI_Session.html`, live at https://gtm-allhands-ai.pages.dev (Cloudflare Pages project `gtm-allhands-ai`, deploy folder `~/Desktop/Intradiem Deliverables/deploy-allhands-ai/`). Operating-map design system, doc view = run of show + demo beats + open items; Present mode = 7 slides (intro, problem, engine map, AI at every step, demo beats, results, questions). Results slide: 4,400 / 12,400 / 700 / 370 hours (at 5 min a contact) + webinar 1,016, 7 sequences, 12 AM maps, 19 agents.
- **Demo**: recorded video, ~6:30, narrated live. Six beats: Claude Code (overnight agents + live strike plan), Clay Audiences segment, Clay rows enriching live (centerpiece, pre-tested rows re-run), webinar workflow, lemlist Stars-Resurrection sequence (delete the two STRAY steps first), closer = replies loop + backoffice-maps.pages.dev (Inger/MAC story per Dallas's ask). Script: `Demo_Recording_Script.md`.
- **Q&A**: `QA_Prep.md`, ten answers (tools, autonomy framing per [[positioning-automation-first-aug17]], accuracy, cross-team with the AM maps as proof, cost, build time, not replacing sellers, security, measurement, what's next). 6sense stays out of every answer.

Open when built: Dallas records the demo (dry-run beat 3 off camera first), Naveen's pass on the run-of-show split, then slides freeze. Related: [[naveen-1on1-aug26-operating-map]], [[gtm-engineering-totals-aug27]], [[present-mode-deck-pattern-aug26]], [[inger-account-maps-build-aug25]].

**Framing addendum (Aug 31, after Dallas's passes):** problem-slide counter settled as 1,800 hours "of manual work. by hand, it never happens"; results counter 370 hours "of sourcing and research given back to sellers". Rules learned: never show the arithmetic basis on a slide (it lives in QA_Prep "if pressed"); all-hands framing is capacity created, never labor or headcount replaced (adoption showcase, don't feed the AI-replaces-jobs fear); no unfinished-work phrasing ("to write") anywhere.

**Final-audit addendum (Aug 31):** ICP buying committees added to the results slide ("adopted by leadership, the targeting standard across every motion") and to demo beat 1 narration after an audit found it missing; it's the most leadership-validated artifact and belongs in any showcase. Dallas's remaining owner items: send Naveen the DM, confirm room AV/who drives the video with Jason Dowden, confirm "Product Strategy" as the stated department on slide 1, delete STRAY steps, dry-run beat 3, record, one full timed rehearsal.

**Recording plan addendum (Sep 1 2026):** Clay beats grounded in live ids in `motions/all_hands_sep14/Clay_Demo_Beats_UISheet_Sep1.md`: beat 2 = Audiences People tab (140,805), open `Sep 2 webinar invite, T2 ... prospect accounts` (25,968 live Sep 1) and remove the Manager, Supervisor, Lead chips from its existing seniority group to land ~17,531 (or flip Account Type to Customer for ~4,246), don't save; beat 3 = `Contacts (Buying Committee)` t_0thtm73HHxyiupTuepK (143 rows) in a saved "All-hands demo" view with audit/Sync Leads columns hidden, five named wave-2 prospect rows re-running Validate Email, LinkedIn posts, MessageGen; beat 4 = live webinar workflow, backfill twin wf_0tk344sg8uVq27RAKd3 if run history looks thin. Recording is Dallas's hands on the work Mac (Cowork Chrome can stage tabs, cannot record video); one mp4 with 3 to 4s hold frames, assembled in iMovie or by Claude via ffmpeg from raw clips.

**Three-act rebuild (Sep 2 2026):** superseded by the plan in [[naveen-call-sep2-demo-three-acts]]: six beats became three acts plus a coda (script v2, Recording_UISheet_Sep2.md, title_cards/), page redeployed with Naveen's set-up section in the run of show, results counters 4,600 / 12,400 / 950 / 370, 7 campaigns sending, 18 maps, 24 agents.

**Demo-view corrections (Sep 4 2026):** in Contacts (Buying Committee), `Email Status` is NOT the validator (it reads the SalesNav staging import, empty on every row); the live chain is `email_final` -> `Validate Email` action -> `Status` (= `valid` on all five demo rows). Sheets patched to show email_final + Validate Email + Status (optional rename to "Email check", safe by column id). New `Contact center platforms` (PredictLeads) column joins the demo view after li_recent_post_hook; the `Contact center platform, latest` formula column stays hidden (MessageGen plumbing).

**Tech-stack provider decision (Sep 4 2026):** demo column stays PredictLeads Find technology stack only (discovery from job posts with dates, exact-match vendor list, 1 cr/row, pre-tested on the five demo rows). Verify-type enrichments (HG Insights 4/result, Clay waterfall ~4/row, BuyerCaddy) answer "does X run Y", not discovery; reserved as a possible motion-level confirmation layer before copy names a vendor (10-row HG test proposed, ~40 cr). BuiltWith/website waterfalls read the marketing site and never see ACD/WFM; Similarweb/Spade/Enigma wrong domain or cost.

**Sep 4 addendum:** HG Insights Verify column (package b7f3454a..., key hg-insights-get-company-tech-stack-v3; bills PER RECORD RETURNED at 4/result, limit defaults to 10 so cap it at 3 + vendor_names filter) and the AI-prompt research column instructions added to Tech_Stack_Column_UISheet_Sep5 (md + html). Both stay OFF the recording and out of the demo view; HG untested pending the 10-account truth test.
