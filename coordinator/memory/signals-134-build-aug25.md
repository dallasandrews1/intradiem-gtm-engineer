---
name: signals-134-build-aug25
description: "Aug 25 2026 afternoon build (dry run, 0 credits): li_engaged + sf_activity trigger families (tests 33/33), three people-side Clay Person Signal fields, six SF Activity / LI segments, two DRAFT LinkedIn-engagement workflows (A per post, B per engager, split because list mode is off), a 173-person job-change test roster, and the 20-row job-change cost (10 credits ceiling via cpj-enrich-person)"
metadata: 
  node_type: memory
  type: project
  originSessionId: f150be67-fc33-431e-869f-beb93cef11df
  modified: 2026-08-25T11:47:11.358Z
---

Dallas approved signals 1 (job change), 3 (LinkedIn post engagement), 4 (Salesforce activity) on Aug 25 2026 after the "what other signals" review; full state in section 14 of `motions/signal_marketing_loop/Signal_to_Marketing_Loop_Strategy_Aug25.md` (worktree `vs-code-agents-window-usage`) and ids in main-checkout `automation/config/heat_loop.json`.

Ids: people fields Clay Person Signal `audf_0tkbpqqoebvN3zTmzbd`, Date `audf_0tkbpqq7XiDESb6hZA6`, Detail `audf_0tkbpqqozXiHyan2WC4`. Segments: closed_lost_aged companies `audseg_0tkbpsgNm3aaB2ydJaz` (68) / people `audseg_0tkbpsgDgSH7hDchH8T` (170), open_deal_moved `audseg_0tkbpshtP3k2bxRFFmy` (153, HOLD), renewal_120d `audseg_0tkbpshGdT8nbdCovik` (25, customer_am), customer_active_90d helper `audseg_0tkbpu9rwEBwWVYzSao` (84 of 92), LI Engaged `audseg_0tkbpshaAW3mcvvobJ4` (0 until B runs), JC Watch roster `audseg_0tkbpyip5Kkvyok7wdd` (173). Workflows: A `wf_0tkbpqrVPgA4h5NKanZ` (post_url -> engagers, 1.0 credit per post), B `wf_0tkbq0fNEMoG6PTVFfg` (one engager -> lookup -> stamp or net_new exit, 0 credits). Both validate clean, NOT published.

Data facts that shaped it: SF closed-lost in Audiences is half `Unqualified` stage, so filter stage Contain "Closed Lost"; `opportunity_type` is empty on every deal; Clay `NoItems` ColOp over deals returns server_error (quiet customers = customers minus active helper, 8 today); list mode (Repeat) is NOT enabled on the workspace (`item` mappings rejected), so per-item fan-out runs outside the workflow via routine `--bulk`; code-node `outputSchema` on create is a flat `{name:{type,description}}` map with no array type; LinkedIn company posts page is a login wall, humans paste post URLs.

Open before anything runs: the 5 current post URLs into `heat_loop.json`; Dallas's go for the 20-row job-change test (method: `cpj-enrich-person` 0.5 per found profile, 10-credit ceiling, diff `latest_experience.company_domain` vs the account); native Clay job-change signal pricing read from the Signals UI; scorer code for the new segments and A's output; publish order A -> run -> B -> routine -> bulk.

**Why:** the engine scores 8 market families that only the crash-prone war room feeds; these three add automated, mostly free feeds and keep person-level resolution per [[feedback-person-level-intent-not-company]].

**How to apply:** treat everything here as draft until Dallas says go; never publish A or B or run the roster test on your own. Related: [[signal-marketing-loop-strategy-aug25]], [[carter-webinar-lead-engine-aug20]], [[feedback-warn-before-large-credit-spend]], [[mem0-quota-exhausted-aug2026]].
