---
name: st-water-bounces-rep-loaded-gap-sep4
description: "Sep 4 2026: 4 of 6 ST Water (Severn Trent) leads bounced because Jack built and loaded the campaign himself in lemlist on Sep 3 outside the Clay verify path; rep-loaded UK campaigns have no verification or integrity gate"
metadata:
  type: project
---

Sep 4 2026, relay run 10:11 CT: 4 new bounces on cam_uAQgRovxEHb438P77 (ST Water, Jack). Campaign created Sep 2 15:56 UTC by Jack's own lemlist user (usr_Bfn76ik549nxaFJYW), six leads added in one import at Sep 3 09:06:03 UTC, sending from jack.ohagan@intradiem.com by Sep 4. No Clay table, no Audiences push, no ZeroBounce record, no lemlist-lead-integrity sweep (the Sep 4 sweep covered only Nate's five BO campaigns). lemlist's own verifyEmail cannot run either (team credits 0, see [[lemlist-enrichment-credits-zero-sep3]]).

Evidence of guessed addresses: Stephanie Cawley loaded as cawley.stephanie@ while Salesforce/Audiences holds stephanie.cawley@severntrent.co.uk (the 98% first.last pattern); Jodie Bowen loaded on severntrent.com, a domain Severn Trent does not use for staff; Deborah Martin-Rerrie a hyphen-collapsed guess with no SF record; Jude Burditt matched the SF address exactly and still bounced (stale or she goes by Judith). Audiences holds 47 Severn Trent people from Salesforce, all on severntrent.co.uk; only Cawley and Burditt of the six are among them.

**Why:** the "verify and enrich every contact" rule is enforced by the Clay bridge (Audiences to lemlist Contacts) and the engine's load scripts. Jack's UK campaigns (Achmea, LV=, UU Water, ST Water, BA x3) are built and loaded by hand in the lemlist UI from his own sourcing (Lusha, Sales Nav), so nothing in the pipeline ever sees those rows before send. The relay only reports bounces after the fact.

**How to apply:** treat any campaign created by a rep's lemlist user as unverified until a Clay pass has run; the fix is a pre-send hook for rep-built campaigns (integrity sweep on every new campaign id the relay discovers, Clay work-email + ZeroBounce on any lead without a Clay record, cross-check against Audiences SF addresses). Related: [[feedback-enrich-in-clay-never-lemlist]], [[lemlist-relay-campaign-map-gap-aug7]], [[jack-vodafonethree-ops-layer]].

**Fix applied Sep 4 (Dallas's go):** campaign paused, not restarted. Free bridge confirmed Bowen and Martin-Rerrie current. Workflow wf_0tk4jo5z7RjGKo3rvR8 on 4 rows cost 3.1 credits (0.78/row): Cawley stephanie.cawley@ valid, Bowen jodie.bowen@severntrent.co.uk valid, Martin-Rerrie deborah.martin-rerrie@ valid/catch_all (kept, flagged), Burditt no email under Jude or Judith, removed via lemlist-lead-remove. Three lead emails updated in place; 5 leads remain. Log: automation/logs/st-water-fix-2026-09-04.md. Pattern for any rep-loaded bounce: free bridge, then the workflow per row, then update_lead on the email field, then the removal helper on failures.
