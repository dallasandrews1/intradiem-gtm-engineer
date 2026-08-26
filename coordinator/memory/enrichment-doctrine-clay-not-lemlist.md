---
name: enrichment-doctrine-clay-not-lemlist
description: "Standing rule set Aug 6 2026 - Clay enriches, lemlist executes; the dangerous defect is a wrong-but-deliverable email, so the fix is a validation gate not an auto-enricher"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d3b88697-23fb-4296-865e-5eaecdcf9851
  modified: 2026-08-06T20:59:10.886Z
---

Dallas asked whether to build an agent that auto-enriches lemlist contacts via Clay. The answer landed as: **no auto-enricher, build a validation gate instead.** He agreed with the reframe.

**Why:** three things failed on Aug 6, and swapping the enrichment vendor only fixes one. Credits running out is the trivial failure. The dangerous one is that lemlist resolved a Citizens VP to `patrick.savage@csn.edu`, a real deliverable mailbox belonging to a different person at a Nevada college. That never bounces, never shows in a bounce report, and an unattended agent would have written it onto the lead with nobody looking at the domain. Automation makes the worst failure mode more likely, not less. Second: lemlist enrichment fails SILENTLY, returning empty fields with a success response, indistinguishable from "no data exists."

**How to apply:** enrichment happens once per wave, at load, attended, through Clay (`Enrich Person and Find Contact Details`, `function:t_0thx4ojyQd6uNhDf44G`, 12.8 credits). Never schedule it. The three non-optional checks are: count populated fields after every run (never trust the response shape), compare resolved email domain against the account domain, and preview a real loaded lead per email step. Where phone sources disagree, load Clay's mobile as primary and keep the other as a fallback rather than discarding it. Doctrine lives at `Intradiem GTM Engineer/motions/shared/Enrichment_Doctrine_Aug6.md`; the recurring unattended piece is the read-only `lemlist-lead-integrity` agent, which finds defects and never fixes them.

**Generalizable principle worth reusing:** when a tool produces output that is wrong but syntactically valid, the answer is a gate that checks truth, not automation that produces more of it faster. Ask which failure mode automation makes worse before proposing an agent.

Related: [[lemlist-trial-enrichment-credits-exhausted]]
