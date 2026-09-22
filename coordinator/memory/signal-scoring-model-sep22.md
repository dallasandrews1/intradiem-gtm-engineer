---
name: signal-scoring-model-sep22
description: Sep 22 2026 account signal scorer built from Genna's model with four fixes, plus a free horizontal executive-hire signal via Apollo search; Apollo people SEARCH costs no lead credits
metadata:
  type: project
---

Built Sep 22 2026 in `october-flywheel/`: `config/signal_scoring.json` (Genna's nine signals, all thresholds in config), `score_accounts.py` (parent grain, re-runnable against a fresh CMS file), `config/exec_signal.json` (horizontal title taxonomy), `signals/exec_hires.csv`. Output `rehearsal_25v26/Account_Signal_Scores.csv`, 182 parents. Tier 1 49, Tier 2 32, Tier 3 22, Low 70, Excluded 9.

**The fix that only appeared on running it:** scoring "does ANY contract at this parent qualify" makes the score measure company size. The seven largest payers all tied at 22 because a parent with 83 contracts always has one that declined, one at 3.5 and one whose peers improved. Fixed by evaluating per-contract signals on the READ CONTRACT (the one `Parent_Measure_Read_2026.csv` names, falling back to the largest sub-4.0 contract by enrollment). Parent facts (enrollment, contract counts, growth) stay parent level. General lesson: a model that aggregates with "any" across a variable-size child set is measuring the size of that set.

**Customer gate caught Humana at score 22**, which would have been the top-scoring account in a cold campaign. Matches normalised names against `greenlight-pack/Active_Customers_SF_Jul10.csv` plus `tam-outbound-engine/config/customer_denylist.json` aliases. Exclusion sets the tier, never competes on score.

**SUPERSEDED, see [[feedback-use-the-paid-stack]]: the exec signal must be rebuilt in Clay.** Kept only as a fact about Apollo. APOLLO PEOPLE SEARCH COSTS NO LEAD CREDITS. Verified against credit stats before and after. `apollo_mixed_people_api_search` with `person_days_in_current_title_range` returns `total_entries` plus obfuscated surnames and titles, and spends nothing; only revealing contact details bills. So an account-level "they hired a relevant leader recently" signal is FREE at any scale, and enrichment stays a per-lead decision made later. Recipe: `q_organization_domains_list=[domain]`, `person_titles=<set>`, `person_seniorities=["director","vp","c_suite"]`, `person_days_in_current_title_range={"min":0,"max":365}`, `person_locations=["United States"]`, `per_page=1`. Apollo lead credits were 27 of 155 with a Sep 26 reset and none were used.

First run, 9 accounts: Centene 16, Cambia 5, Point32Health 2, Devoted 1, Blue Shield of California 1; zero at Medica, Florida Blue, Excellus, Zing.

**The real gate on scaling it is domains, not money.** Only 26 of 182 scored parents have a domain in `StarRatings_PersonaPull_RunConfig_TierAB.csv` or `relaunch_mined_lines_sep22/netnew_parents_ratings_sep22.csv`, and several read VERIFY. Related: [[stars-trigger-cohorts-sep22]], [[feedback-signals-are-horizontal]], [[clay-spend-posture-aggressive]].

**Domains resolved in Clay Sep 22 2026.** Clay's Company Domain function (`t_0thx4oeCWHZgydZRRVv`, via `run_subroutine_direct`) over the 72 sendable Tier 1 and Tier 2 parents with no domain. All 72 now carry one, in `october-flywheel/signals/parent_domains.csv`. Cost was trivial against a 57,644 balance.

**Resolve on the PARENT name, not the plan brand.** Two brand-name queries came back confidently wrong: "Banner Medicare Advantage" returned ssa.gov (the Social Security Administration) and "Shared Health Dual Freedom" returned sfmc-content.com (a Salesforce Marketing Cloud domain). Re-querying the parent name gave bannerhealth.com and bcbst.com. A wrong domain here sends mail to the wrong organisation, so every resolved domain needs a check column.

**A name-overlap check must understand initials.** The first automated verification flagged 15 healthcare domains as suspect that were plain acronym domains: bcbsnc.com, azblue.com, hpsm.org, scfhp.com, mnscha.org, bcbsri.com, bcbsks.com. Roughly a fifth of a payer list.

**Defect found in the universe file, not in Clay:** the most common `marketing_name` under "Blue Cross Blue Shield of Michigan Mutual Insurance" is a Wellmark brand (Wellmark is Iowa and South Dakota), and under "CuraCor Solutions Corp." it is Blue Cross and Blue Shield of North Carolina. Those parent to marketing_name rows in `rehearsal_25v26/StarRatings_Universe_2026.csv` are mismatched and any per-brand read on them is unsafe.
