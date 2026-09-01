---
name: signal-marketing-loop-strategy-aug25
description: "Aug 25 2026 strategy + BUILT (dry run) same day: one Heat List in Clay Audiences scored by the TAM engine trigger taxonomy (web intent as new trigger families), Lane A same-day rep alerts with Approve/Deny, Lane B bi-weekly cohorts cut once to lemlist AND LinkedIn Matched Audiences (ads T0, email T+5) with a holdout; doc in motions/signal_marketing_loop/"
metadata:
  type: project
---

Written Aug 25 2026 after the Aug 24 Pipeline Council and Naveen 1:1 (Naveen action item: configure Clay web intent on the WordPress site, send snippet to Carter/Sierra). Doc: `motions/signal_marketing_loop/Signal_to_Marketing_Loop_Strategy_Aug25.md` (worktree vs-code-agents-window-usage).

Verified facts the design rests on:
- intradiem.com is WordPress 7.0.4 with GTM `GTM-WSDB2RL` on every page and Pardot forms; a Clay pixel is a GTM Custom HTML tag, no developer. No Clay/lemlist/6sense tag visible in homepage HTML.
- Clay Website Intent: company-level only, table created in the UI generates the snippet, 1 action + data credits per unique IP (30-day cache), waterfall mode 5 to 10x cheaper, per-connection credit cap, Pro plan minimum. The Jul 17 "Web intent" workbook no longer exists.
- Clay Ads: Audiences segment to LinkedIn Matched Audiences (people and company), 300 matchable minimum, ~48h processing, 3-day resync, 1 action/record; Growth or Enterprise plan (our tier unconfirmed). Fallback: CSV to Sierra for list upload.
- lemlist Signal Agents "Website visitors": lemlist pixel, person-level ID for US visitors, 20 credits/signal, 48 to 72h; zero watch lists exist; API still 402 until the contract lands.
- Action catalog has upsert-audiences-record, lookup-in-audiences, lemlist-add-lead-to-campaign-v2, slack-send-for-approval-to-channel, Salesforce create/update/soql, http-api-v2. Rep channels exist (#gtm-outbound-nathan C0BM9V6KGSG, #gtm-outbound-jack C0BN0JT9D6U).

Design decisions: scoring in `triggers.json` (web_product 30, web_proof 20, web_return 15 x3 cap, web_from_us 20, web_content 8, lemlist_click 15, lemlist_reply 40; fresh 14d, floor 45d), lanes rep / cohort / hold / customer_am / excluded after the customer-exclusion UNION; customers route to the AM clearance sheet never to cold; cohort day every other Tuesday (first Sep 8), ads at T0, LinkedIn live T+2, email 1 at T+5, ads off T+25 into retargeting; 50/50 account holdout for two cohorts; one SF campaign name per cohort as the join key; Lead Source GTM Engineering must exist before the first SF write.

Explicitly not built: Bombora/Intentsify via Clay (6sense covers it), person-level de-anon by default (Jason Jones question), new dashboard, new DM, auto-send without ad warm-up, Apollo tracker.

Agents to build: `heat-list-scorer` (7:20 and 13:00 weekdays, log-only, rep-channel alerts with Approve/Deny) and `cohort-cutter` (bi-weekly Tue 8:00); rundown reads the heat log. Open decisions: 500-credit pixel read (over the 100-credit line), lemlist person-level ID, Clay plan tier.

**Build state, Aug 25 2026 (all DRY RUN, 0 credits):** Audiences company fields Clay Heat Score/Reasons/Lane/Updated/Cohort (`audf_0tkbgjwfqXfbz3tVvFE`, `audf_0tkbgjw5yKPSuiQ6kxP`, `audf_0tkbgjx4SbZbS8yNu4j`, `audf_0tkbgjxAYwK64ZxUtjd`, `audf_0tkbgjxozeptXEZDecr`); segments Heat List `audseg_0tkbglis6qhvceQSZzJ`, Lane A queue `audseg_0tkbgljnEDPCFGqwHka`, Cohort pool `audseg_0tkbgljqW8NToVQnDSN`, customer_am `audseg_0tkbglj2HPXwazijzsm`; draft workflows Heat Stamp `wf_0tkbgk0UytzkPQWmakX` (webhook -> upsert company) and Heat Lane A `wf_0tkbgk02Xub84UtnRXS` (webhook -> Slack Approve/Deny -> approved? -> lemlist add lead), both validate clean, NOT published. Engine: 9 new trigger families with per-trigger recency in `triggers.json`, `web_intent.json` page map on real intradiem.com paths, tests 26/26 (branch `agents/vs-code-agents-window-usage`). Jobs in the MAIN checkout `automation/` (untracked dir): `heat_list_scorer.py`, `cohort_cutter.py`, `config/heat_loop.json`, wrappers and plists written, plists NOT loaded; wrappers set `HEAT_ROOT` to the worktree until merge. First dry run: 335 companies scored (rep 1 Centene, cohort 4, customer_am 19 incl. HCSC/Humana/CVS/Molina, hold 310); web intent source skipped (no table yet). Rundown skill inputs 10 and 11 added. CLI gotchas: edges are set via `nodes update` with `incomingEdges` (a rule edge goes on the TARGET node as `{sourceNode, ruleId, ruleName}`); `graph validate` exists; Audiences `fields create` accepts number/date.

Still Dallas's hands: Clay Settings -> Website tracking -> Add connection (waterfall, 500 cap) -> snippet to Carter/Sierra (GTM `GTM-WSDB2RL`) -> workbook Create -> Website visitor tracking -> table id into `heat_loop.json`; lemlist campaign ids into the config once campaigns exist; Lead Source ticket; merge the branch then `launchctl bootstrap` the two plists. Sheet: `motions/signal_marketing_loop/Clay_Web_Intent_Setup_UISheet_Aug25.md`.

**Why:** Melissa asked for ads on the lemlist list on the record, Naveen asked for the inbound/outbound bridge, John wants more C-suite meetings; the loop answers all three without a new engine.

**How to apply:** follow the build order in section 12 of the doc; nothing on step 3+ until the pixel has sessions. Related: [[pipeline-council-aug24-meeting-takeaways]], [[pipeline-council-context-aug24]], [[bo-expansion-council-aug24]], [[feedback-warn-before-large-credit-spend]], [[positioning-automation-first-aug17]].

**Aug 27 decision:** the 50/50 account holdout is dropped. Dallas: "what does that even mean, half held out? and why would we even do that." At LinkedIn's 300-matchable floor a cohort is ~50 accounts, 25 per arm, too small to read; the comparison is the sequences that run without ads (Stars, Blitz, UK) vs the intent cohorts that run with ads. Removed from the operating map; `cohort_cutter.py` holdout assignment should be switched off before the first cut.
