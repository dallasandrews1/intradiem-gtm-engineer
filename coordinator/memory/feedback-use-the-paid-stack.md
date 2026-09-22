---
name: feedback-use-the-paid-stack
description: Build signals and enrichment in Clay or lemlist, the tools Intradiem pays for. Never reach for Apollo or another vendor just because a tool happens to be available in the session
metadata:
  type: feedback
---

Sep 22 2026. An executive-hire signal was built on Apollo people search because the MCP tool was in the session. Dallas: "the signal needs to be built in Clay or Lemlist stop relying on Apollo when we pay for lemlist and clay."

**Why:** Intradiem pays for Clay and lemlist. A signal built on Apollo cannot feed a Clay table or a lemlist campaign natively, it puts a dependency on a tool nobody owns the workflow for, and it splits the enrichment layer. The standing doctrine already says Clay enriches and lemlist executes, see [[enrichment-doctrine-clay-not-lemlist]]. Tool availability in a session is not a reason to use a tool.

**How to apply:** for anything that finds, enriches, scores or resolves a person or company, the answer is Clay. Run `clay workflows list` first, per the standing rule, because something close usually exists already. On Sep 22 that check found `wf_0tlqmjdJhZeKuj6gYzs` "LinkedIn profile check (URL in, dated roles out)", which is a start-date read and therefore most of an executive-hire signal, built the day before. Clay's own functions cover a lot: Company Domain, Find People at Company, Enrich Person, Person Job Title. Apollo may still be read for a quick sanity check, never as the thing a motion depends on.

Related: [[enrichment-doctrine-clay-not-lemlist]], [[signal-scoring-model-sep22]], [[clay-spend-posture-aggressive]].
