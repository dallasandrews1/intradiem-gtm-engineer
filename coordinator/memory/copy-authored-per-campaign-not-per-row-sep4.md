---
name: copy-authored-per-campaign-not-per-row-sep4
description: "Sep 4 2026 decision: outreach copy is authored per campaign in Claude Code with lemlist variables, not generated per row in Clay; Clay's job is the variable factory (verified email, Why Now, Persona Key, platforms), not prose"
metadata:
  type: project
---

Dallas's call, Sep 4 2026: per-campaign authored copy with lemlist variables has been effortless through Claude Code, so the Clay prose columns (`MessageGen Email`, `Msg1Subject`, `Msg1Body`, and the workflow-generated `WF Msg1-5 Subject/Body`) are not worth maintaining. They host messaging almost nobody sees.

**The evidence supports it.** On the Stars table `send_ready` is `critic_email_valid=="PASS" && msg1_critic=="PASS" && voice_status=="PASS"`, and `voice_status` reads FAIL on essentially every row, so `send_ready` sits at HOLD across the table. The per-row copy path is the thing holding the gate closed. Meanwhile the authored path shipped 803 DWO leads and 332 back-office leads.

**Clay is not redundant, its job is narrower than prose.** The `Sync Leads` action already pushes exactly the variable set lemlist needs: `email_final`, `First Name`, `Full Name`, `Persona Key`, `Why Now (2026-cycle)`, `Contact Center Platform, Latest`, `Technologiesfound`, plus `customer_exclude` and `send_ready`. That is the division of labor: Clay finds, verifies and computes the per-lead facts; the copy is authored once per campaign and per persona, and interpolates them.

**How to apply:** stop investing in the prose columns and the two copy audits. `send_ready` should gate on what protects the company (verified email plus customer exclusion), not on audits of drafts nobody sends. The `motion-stamp` skill still assembles a 5-touch MessageGen prompt set as its default, so change that before the next motion inherits the retired model. For the all-hands demo, show Clay filling the variables and let the lemlist act carry the message. Related: [[messagegen-stale-vs-sep3-doctrine]], [[allhands-ai-session-package-aug31]].
