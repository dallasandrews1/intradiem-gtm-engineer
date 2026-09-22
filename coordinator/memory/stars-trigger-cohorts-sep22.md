---
name: stars-trigger-cohorts-sep22
description: Sep 22 2026 Stars trigger-cohort proposal built on Genna's nine-signal scoring model; page staged not deployed, audit found 4 of 9 signals computable today and killed two cohort claims
metadata:
  type: project
---

Sep 22 2026. After the GTME cadence call, Genna Barrett-Moeller posted a nine-signal trigger and scoring model to the group (strong 3 / moderate 2 / supporting 1, +2 combination bonus, Tier 1 at 8+, ICP fit kept separate from trigger strength). Dallas directed that the proposal be built on hers rather than the four-cohort sketch taken from the call transcript. Built in `motions/star_ratings/trigger_cohorts_sep22/`: the markdown source, the page rendered through `motions/shared/build_md_page.py`, the Slack post in Dallas's voice, and `stage.sh`. Staged to `~/Desktop/Intradiem Deliverables/deploy-stars-trigger-cohorts/`, NOT deployed, no Cloudflare project exists yet.

**Three arithmetic defects found in the scoring model, all raised as Genna's call:** nothing catches a 7, and new exec plus declining rating scores exactly 7 (2+3+2), so the likeliest pair in the model falls between Tier 1 and Tier 2; the combination bonus is described as "two strong signals" in her summary but four of her six examples pair a moderate with a strong; and five supporting signals stack to a 5, which is Tier 2, with no real trigger in it. Proposed fixes: Tier 2 becomes 5 to 7, the bonus fires on any named combination, supporting signals cannot lift an account past Tier 3 alone.

**Data audit (read-only subagent) verdict on the nine signals.** Computable today: rating declined YoY (120 of 800 contracts), rating 3.0 to 3.5 (264 of 800), multiple contracts below 4 per parent (26 parents), specific measure deterioration (12,240 contract x measure rows, 460 of 800 contracts with a service measure down). Partly: MA enrollment sits on only 297 of 800 contracts because the join covered the sub-4.0 set only; public statements cover 20 of 93 parents with just 7 having an earnings-call source. Needs sourcing: new-exec hires (signal engine slot specced but data is mock), enrollment growth (one June 2026 snapshot, no prior vintage), local peer comparison.

**Two claims the audit killed before ship, worth not re-making.** (1) There is NO state, county, region or market field anywhere in the CMS Star Ratings tables, so "plans they share counties with" is not computable; only a national peer comparison is. (2) Roughly 8 of the 93 universe parents are publicly traded, about 22 percent of Tier A and B, so an earnings-call cohort reaches almost none of the universe; the rest are Blues, mutuals, county authorities and nonprofit systems whose equivalent surface is a press release, rate filing or state filing.

**The free unlock to remember:** the CMS county-level monthly enrollment file is a free public download, and joining it on contract id repairs the enrollment coverage gap, creates the growth series, and enables a real county-overlap peer comparison. Three of nine signals go from approximate to real for no spend. The only paid item is the executive title sweep across 93 parents.

**Position taken in the proposal:** the trigger decides why we write today, the measure-level read is the payload in every cohort, because the overall rating is public and fails the uniqueness test alone. Pre-release wave needs no new build, the 72 leads already loaded were selected on a contract under 4.0 with a durable-measure gap, which is two cohorts already assembled. Also flagged: customer exclusion is a third axis beside trigger strength and ICP fit, because scoring surfaces the largest and most exposed plans first and those are likeliest to be customers.

NOT done: the back office half of Dallas's action item. Related: [[naveen-gtm-physics-stars-relaunch-sep21]], [[stars-recut-staged-sep21]], [[clover-ruling-stars-measure-thesis-sep21]].
