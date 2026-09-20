---
name: naveen-okr-tool-list-sep20
description: "Sep 20 2026: Naveen's three GTM objectives as entered in the HR OKR tool, the tool's quarter labels, and the OKR set proposed for Dallas to enter under them"
metadata:
  type: project
---

Seen Sep 20 2026 in the HR OKR tool (screenshot from Dallas). Naveen's GTM-tagged objectives, all 0 percent and not yet updated, period ends Sep 30 2026 and the tool labels that period **2Q2026** (so Oct 1 to Dec 31 is most likely 3Q2026 in the tool; Dallas says Q3/Q4 in calendar terms, confirm the label before entering):

- 2Q2026 GTM Queue optimizer: business readiness to completion; sign two beta customers; alternate platform pricing.
- 2Q2026 GTM Engagement hub: market readiness; pricing.
- 2Q2026 GTM Engineering: industry-specific new-logo strategy (back office, front office, combined DWO messaging); 10x messaging throughput; enriched contact database plus strategy for existing-customer back office; partner channel strategy; deliver 15 meetings; procure lemlist and set up the sequencing engine.

Proposed for Dallas (Sep 20, pending his ratification and the Naveen walk): mirror Naveen's six GTM Engineering lines one for one as shipped artifacts or routines per [[feedback-okrs-in-his-control]], a launch-readiness objective that feeds QO/EH/BOO without owning beta signatures or pricing, and a self-serve tools objective for Oct to Dec. Meetings stay reported on the Pipeline Council scorecard, never promised. Builds on motions/shared/OKRs_Dallas_Sep7.html. Related: [[okr-channel-economics-frame-aug5]], [[product-roadmap-allhands-sep18]].

**Update Sep 20 (later):** Dallas pasted the build prompt; motions/shared/OKRs_Dallas_Sep7.html was rewritten in place as the two-period set (2Q2026 close-out 8 KRs, Oct 1 to Dec 31 11 KRs, 5 objectives), uncommitted, not deployed, not sent. Live checks that day: lemlist is paid (Aug 28 email to Luis: subscription, mailboxes, numbers purchased); 17 engine-built campaigns across eight motions, 13 loaded, 1,895 leads (334 in the five BO campaigns); the "GTM Engineering" Lead Source value is still an open ticket with Sierra, so that KR reads "in motion". "Tyler and Jen" in the OKRs = Tyler Vogley (Director of AI Enablement) and Jenn East (Chief of Staff). The page never mentions Greenlight per [[ai-enablement-update-aug7]].

**Deploy attempt Sep 20:** staged copy at motions/shared/deploy-dallas-okrs (Slack-note section stripped, noindex meta + _headers). `npx wrangler pages project create dallas-okrs` FAILED under wrangler 4.135.0: it delegates to the Workers deploy path, auto-answers yes to a prompt, then errors "Missing entry-point"; nothing was created (project list confirmed). Wrangler's own output suggests `--force` to use the classic Pages path; not run, waiting on Dallas's call. Step 2 (deploy) not run.

**Deployed Sep 20:** live at https://dallas-okrs.pages.dev (200, noindex header served, Slack-note section absent from the live copy). Dallas approved `--force` on `pages project create` only; project now sits on classic Pages so later deploys need no flag: `npx wrangler pages deploy motions/shared/deploy-dallas-okrs --project-name=dallas-okrs --branch=main --commit-dirty=true`. Re-stage the deploy folder from the working file before any redeploy. Not yet sent to Naveen; repo changes uncommitted.
