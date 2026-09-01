---
name: pm-kit-greenlight-coldrun-sep1
description: "Sep 1 2026: PM as a builder kit repackaged for Greenlight (motions/ai_champion_product/pm_kit/, no repo, no Claude Code) and proven cold on a second SharePoint PRD (Scheduling Service v1.0, Screen 7 Holiday Calendar): 7 pass, 1 manual after one PM-style fix loop; second worked example in prototypes/holiday_calendar/"
metadata: 
  node_type: memory
  type: project
  originSessionId: 74126cdd-335c-4fbd-8e02-176e2729aae9
  modified: 2026-09-01T16:21:32.183Z
---

Dallas confirmed Sep 1 2026 that Greenlight can produce downloadable single-file HTML artifacts, so Greenlight is the PM surface for the PM as a builder program (not claude.ai Projects, not Claude Code).

Kit in `motions/ai_champion_product/pm_kit/`: `PROJECT_INSTRUCTIONS.md` (self-contained builder instructions with DS tokens, build rules, self-check panel spec with `#sc-summary` and `window.__selfcheck()`, handover format, fix loop), `Prototype_Brief_Template.docx` (nine sections, generated with python-docx), `DS_Tokens.md` (marked "DS v1 per Skills Editor PRD v2.0, replace with design's current sheet"), `README.md` for the PM (set up once, build, when a check fails, the review).

Cold run: a subagent with only the three kit files plus a PRD excerpt, no Bash, no browser, built Screen 7 Holiday Calendar from PRD-Intradiem-Scheduling-Service v1.0 (SharePoint engineering/Aldus Documents/Proof of Concepts/Aldus Modules Proof of Concepts/Intradiem Scheduling System (on top of core)). First run verified headless at 1920/1440/1280: 6 pass, 1 fail (AC-6, checkbox inputs took browser default black), 1 manual. One PM-style fix message ("Check AC-6 fails: ... Fix that and keep everything else the same") produced a one-line CSS fix; re-verified 7 pass, 0 fail, 1 manual at 1920 and 1440. Files copied to `prototypes/holiday_calendar/` (index.html 59 KB, brief, handover, PRD_source.md).

Verification method for prototypes without puppeteer: a wrapper HTML with an iframe, Chrome headless `--allow-file-access-from-files --dump-dom`, calling `iframe.contentWindow.__selfcheck()` (wrap.html pattern, scratchpad only).

Finding for Product: the Scheduling Service PRD names a different design system (Harmoniq Scheduler: Inter, #1B3A5C, #2E75B6, #4CAF50) from the Skills Editor PRD (DS v1). Two PRDs in the same folder, two DSs. The kit's "attached sheet wins" rule handled it, but design needs to say which sheet is current before PMs build.

Instruction gaps the cold run exposed and that were fixed the same day: brief sections enumerated inline, pre-approval ("Build it") handling, shell nav items outside the built screen shown disabled, category encoding within the token set, explicit text colour on inputs, width checks report the width they ran at, DS wins over the 4.5:1 rule with a handover note.

**Why:** the program page's step 2 ("Run pm-prototype, PM in Claude") assumed Dallas's machine; the kit makes step 2 real for a PM with Greenlight only.

**How to apply:** next is one PM and one live feature paired for 45 minutes (Product names them), review held on the prototype, section 8 written; then send the kit to all PMs. The PM_Builder_Program page still describes the old step 2 and should be updated to Greenlight plus the second worked example before it goes to Naveen again. Related: [[product-ai-goals-build-aug31]], [[feedback-links-land-on-the-thing]], [[ai-champion-product-role-aug17]].
