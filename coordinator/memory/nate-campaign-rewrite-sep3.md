---
name: nate-campaign-rewrite-sep3
description: "Sep 3 2026 - Nate's four running lemlist campaigns PAUSED and every email, LinkedIn message and call script rewritten under the Sep 3 doctrine and applied in lemlist; restart is Dallas's call after Nate reads the page; one UI fix open on Resurrection variant B"
metadata: 
  node_type: memory
  type: project
  originSessionId: 864a99bb-87d2-49b7-8d95-dcb3da162f63
  modified: 2026-09-03T17:00:30.586Z
---

Sep 3 2026, Dallas: "we need to pause and improve all of the messaging for Nate's campaigns in lemlist, especially the Stars ratings focused campaigns. they sound like choppy unnatural ai and the emails themselves don't make sense... they don't deliver the why are you reaching out to me, why does it matter to me, who are you, why should I care standards that actually get replies."

**Paused (Sep 3, before any edit):** Stars - Resurrection (cam_sh3JCJoxtEHyjGrsw, 43 leads), Stars - Fresh Pool / Finance (cam_2gy9hmEvMjYEuPZ8A, 13), Blitz - The Hartford (cam_fYp7Nh9wB72gfMke6, 7), Blitz - Citizens (cam_yWefPqaDhNNv4RyQK, 8). Stars - Fresh Pool / Quality (cam_viEbB6HkYsCPtxKbi) was already a draft and was rewritten too.

**What was wrong:** Email 1 never said who Intradiem is or what it does (brand-light rule), leaned on clever lines ("eating my words", "the seam I work", "the cliff is being priced in"), every email ended on the same "Worth 15 min in the next few weeks?" template, and the per-lead opener_line variables read as writerly AI.

**What the rewrite does:** every Email 1 opens on the plan's own CMS number ({{plan_name}} near {{qbp_avg}}, humility clause) or the account's public signal, says what Intradiem does by sentence three (sits on top of the WFM and phone system they already run, holds adherence and handle time steady while calls are scored), carries one verified proof (Humana AHT down 45 seconds, 7X five years in, 2 hours capacity per agent per month; RBC cited blinded as "a large North American bank, $6.1M a year"), and ends on one no-calendar question. Email 2 is the timing angle, Email 3 a short breakup naming the re-entry condition. Call scripts keep the four-beat opener and add the product sentence. Templates use plan_name and qbp_avg directly instead of opener_line and contract_line; vm_hook and voice_script variables still used in phone and voice steps.

**Files:** source of truth `motions/star_ratings/nate_rewrite_sep3.py` (regenerates the review doc and the JSON of step updates); review page `Nate_Copy_Rewrite_Sep3.md/.html` (Desktop copy in Intradiem Deliverables); pre-rewrite backup of every step `Lemlist_Sequences_Backup_PreRewrite_Sep3.json`.

**Applied in lemlist Sep 3:** all steps in all five campaigns, both A/B variants on the four Email 1s. **Open:** lemlist refused the variant B edit on Resurrection "just tried you" (stp_afdYJbTbPXLZkvxkC) with SEQUENCE_AB_CAMPAIGN_RUNNING despite the pause; variant B still carries the old body. UI fix: pick variant A as winner or paste the new B text. Restart (set_campaign_state start) is Dallas's call after Nate reads the page. Related: [[messaging-doctrine-sep3]], [[feedback-bdrs-are-the-experts]], [[naveen-product-materials-index-sep3]].
