# Signal-to-Marketing Loop: web intent, Clay, lemlist and LinkedIn ads on one clock

Written Tue Aug 25 2026 for Dallas. Internal working doc, not Naveen- or council-facing. Sources: Pipeline Council recording Aug 24 (Otter DPymH0p56v4Rz_J-2NZxHmC-yYU), Naveen 1:1 Aug 24 (_tGdAhZ5xzAiF5gwO4QyhvpQwU0), 6sense sync Aug 24, BO expansion council Aug 24, live checks of intradiem.com, the Clay workspace, the Clay action catalog, Clay docs, lemlist Signal Agents docs, and the repo.

## 1. What the council actually said that matters to this build

Speakers named where the transcript makes it unambiguous.

- Melissa opened by saying she invited Naveen and Dallas so they'd see "the flow of how we do things, what we're measuring" because "they're going to be reporting on their results at some point." The format is the 23-column dashboard already mapped in `motions/pipeline_council/`.
- Melissa, straight to Dallas after Nate described lemlist warming contacts before calls: "can we also warm these people up before you're calling, do some sort of digital campaign along with the lemlist... when you get that group of people... target them with ads, just that extra touch." Dallas: "wholeheartedly agree... getting this happening at the same time." This doc is that offline conversation.
- John (CRO): it is not a conversion problem, "it's just getting more meetings." DWO "should resonate at the C-suite better than anything we've done," the team lands in middle management and fights up, "we can't let ourselves fall into the excuse that they don't pick up their phone." He asked whether lemlist is sequencing the call-behinds so the follow-up is visible. He also challenged spend: alliances at ~$2K per meeting vs digital and events at ~$22K, similar 80% meeting-to-opp, "why am I not doing all kinds of partner events."
- Nate: 6 meetings in July, all from 10,000 dials (6,000 back office, 4,000 front), 5 of 6 meetings front office, one BO meeting. VPs don't answer the phone; directors and managers do. He is using Claude for BO persona breakdowns by vertical and will share them. Jen and Melissa want Nate and Jack broken out from memoryBlue; Jenna can do it in the data.
- Sierra (Digital): 6 MQLs in July (HubSpot, Instructure, Principal Financial, Indra, Verity Credit Union, Verizon), Alorica opps from Bing natural search, BCBS NC $553K BPO moved to Procure, TIAA CREF NCC pilot closed won. LinkedIn ads CTR 4.15% overall, ~8% on a promoted Jen thought-leadership post ($1,500 spend, ~3,500 clicks). Conversation ads will be sent from a solutions consultant. Front vs back office A/B evened out.
- Frank (Alliances): $3,400 spend, 5 meetings, 5 opps, $1.3M pipeline in July, $96 pipeline per $1 over 18 months. Asked for digital ads against partner sellers and SCs targeting existing pipeline, not pre-pipeline. Tom (inferred): "give them an asset on our website we want to send them to, then we drop a cookie on them, then we get them." Melissa: LinkedIn targeting is "really to the domain and the title or area of business," not to a named person. Frank has been sending the Humana webinar landing page and partners love it.
- Ellen: Carter introduced as 6sense + Clay + Salesforce certified, expected to "contribute in large part to a lot of these metrics." Three webinars in September (DMG on Sep 2, two customer webinars), Genesys Experience next week, six events in one October week, Gartner customer service event in November, BFSI exchange in Miami in October with Keegan and Lizzy. 3XG back-office webinar mid Q4 as the channel launch of Back Office Optimizer.
- Data integrity: 20 minutes on "squishy" alliances vs events spend; outcome is PO-tagged travel so field engagement is isolated. Jen wants 2027 budget recommendations derived from the 18 months of data.

What this means for us: the council wants more meetings at higher titles, is already sold on integrated marketing, has LinkedIn creative that performs, and will judge our row on cost per meeting against Cold's $3,402. Nobody in the room has a mechanism that puts ads and sequences on the same list at the same time. That is the gap.

## 2. Naveen's ask from the 1:1 (same afternoon)

"Bridge the gap between outbound operations and inbound signals." Action item on me: configure Clay to track per-visit, per-company intent on the WordPress site and send the configuration to Carter and Sierra for implementation. Naveen opens the Carter/Sierra conversation on launching outbound off those signals. He also wants a three-week lemlist sprint aligned with marketing messaging as the all-hands outbound offering, no pipeline-number commitment.

## 3. What exists today (verified Aug 25)

| Piece | State |
|---|---|
| intradiem.com | WordPress 7.0.4, Google Tag Manager `GTM-WSDB2RL` on every page, GA4, Pardot forms. A Clay pixel is a GTM Custom HTML tag on All Pages, no developer needed. No Clay, lemlist, or 6sense tag visible in the homepage HTML (a 6sense tag may live inside GTM; ask Sierra). |
| Clay Website Intent | Native. Company-level only (never a person). Pixel from a "Website visitor tracking" table created in the Clay UI. Each session carries pages, time on site, referrer, UTMs, session count, resolved domain. Costs 1 action plus provider data credits per unique IP resolved, cached 30 days; "waterfall" mode is 5 to 10x cheaper than "best match." Credit cap per connection. Pro plan minimum. A "Web intent" workbook was in the Jul 17 registry; it is not in the workspace today (8 workbooks, none web). |
| Clay Ads | Syncs an Audiences segment to LinkedIn Matched Audiences (people and company audiences), 300 matchable records minimum, ~48h LinkedIn processing, resync every 3 days, 1 action per record plus optional enhanced matching (1 to 3 credits per row). Growth or Enterprise plan. Our tier is not confirmed from the CLI; the Aug 21 watch list already had "Clay enterprise upgrade" on it. Fallback that needs no upgrade: cut the segment to CSV at 0 credits, Sierra uploads it as a list-upload Matched Audience. |
| Clay Audiences | Live, Salesforce-synced (140.8K people, 2.3K companies with Account Type, 7.8K deals). Segments and fields are CLI-buildable at 0 credits. Workflows can trigger on a segment or a webhook. Actions in the catalog: `upsert-audiences-record`, `lookup-in-audiences`, `get-audiences-activity`, `lemlist-add-lead-to-campaign-v2`, `slack-send-for-approval-to-channel`, `send-message-to-channel-botname`, Salesforce `create-object`/`update-object`/`lookup-via-soql`, `http-api-v2`, `versium-online-audience-append-v2` (hashed emails for ad platforms). |
| lemlist Signal Agents | "Website visitors" signal exists: lemlist's own pixel, person-level identification for US visitors (name, role, seniority), company-level fallback, 20 credits per signal, 48 to 72h to populate. Zero watch lists exist today. The current tier still returns HTTP 402 on API routes; contracting closes this week. |
| TAM engine | `tam-outbound-engine/config/triggers.json` is the trigger taxonomy (8 families, weights, persona routing, stakes lines) with recency decay (full weight inside 30 days, floor 0.4 past 120). `data/triggers.csv` is `domain, trigger_type, detail, date`. Web intent belongs here as a trigger family, not in a new engine. |
| Routing surfaces | lemlist relay already posts per-rep to `#gtm-outbound-nathan` (C0BM9V6KGSG) and `#gtm-outbound-jack` (C0BN0JT9D6U). Daily rundown at 7:50 is the only Dallas-facing ping. |
| Attribution | Lead Source `GTM Engineering` + Lead Origin value + helper-tab row specified in `Pipeline_Council_Mapping_Aug24.md`; ticket not yet filed. 6sense SI and LinkedIn Sales Navigator lead sources map to Digital. |
| 6sense | Credits expire Aug 28 to 30; Dustin is running SF-filtered enrichment workflows this week; renewal is an open question. 6sense's own intent (buying stage, keyword intent) is the intent source marketing has today. If those fields sit on the SF Account object and ride the Audiences sync, Clay segments can filter on them at 0 credits. Unverified, one question to Sierra. |
| Apollo | Website visitor tracker exists at the team level with no domains configured. Not used; Apollo is not the sequencer. |

## 4. The strategy in one paragraph

One list, one clock, two lanes. Every account that shows intent lands on a single Heat List in Clay Audiences with a score, a reason, and a lane. The score comes from the TAM engine's trigger taxonomy (web intent is a new trigger family riding the same decay), so "signals that move the needle" is a config file, not a debate. Lane A is fast and named: an account we already target, or a live-sequence account that just came back to the site, goes to the rep's Slack channel the same day with a why-now and a staged lemlist push. Lane B is batched and shared: everything ICP-fit but not yet worked accumulates for two weeks, then the cohort is cut once and goes to two places at the same moment, a lemlist campaign and a LinkedIn Matched Audience, under one Salesforce campaign name. Ads go live three business days before email 1 (Melissa's "warm them up"), run the length of the sequence, and the cohort is split test vs holdout so the council gets a number instead of an opinion. Customers never enter either lane; they route to the AM per the BO expansion rules.

## 5. The Heat List

A company-level Audiences segment plus five fields written by one workflow. No new table, no dashboard.

Fields on the company record (CLI-created, 0 credits):
- `Clay Heat Score` (number, 0 to 100, decayed)
- `Clay Heat Reasons` (text, newest first, e.g. `web:product/back-office-optimizer x3 (Aug 24); lemlist:click E2 (Aug 22); trigger:cost_mandate (Aug 11)`)
- `Clay Heat Lane` (select: rep / cohort / hold / customer_am / excluded)
- `Clay Heat Updated` (date)
- `Clay Heat Cohort` (text, the cohort id once cut, e.g. `GTMENG-2026-09-08`)

Inputs, in order of how much I trust them:
1. Web intent sessions from the Clay pixel (pages, repeat sessions, UTM, referrer).
2. lemlist engagement from the relay log (opens are noise; clicks, replies, LinkedIn accepts count).
3. War-room triggers already staged in `automation/logs/staged_signals.csv` and `data/triggers.csv`.
4. Webinar registration routes already stamped by Carter's workflow (`Clay Webinar Route` = bdr_review).
5. 6sense buying stage, only if it turns out to be on the synced Account object.

Scoring lives in `tam-outbound-engine/config/triggers.json` as new families (weights are a starting point, tune after two cohorts):

| Family | Fires when | Weight | Decay |
|---|---|---|---|
| `web_product` | session touched a product or platform page (Back Office Optimizer, Queue Optimizer, DWO/platform, demo request) | 30 | fresh 14d, floor 0.3 at 45d |
| `web_proof` | customer story, ROI, webinar recording or landing page | 20 | same |
| `web_return` | second or later session inside 7 days, per session, capped at 3 | 15 | same |
| `web_from_us` | referrer or UTM is our lemlist link or our LinkedIn ad | 20, and sets the reason tag `engaged-by-us` | same |
| `web_content` | blog or thought leadership only | 8 | same |
| `lemlist_click` / `lemlist_reply` | relay event | 15 / 40 | same |

Ignored on purpose: careers, contact, about, privacy, support/help portal (`WebHelp` is customer traffic), ISP and personal domains, competitors (the webinar workflow's triage node already holds that list), our own domains.

Lane rules, evaluated after the customer-exclusion union (SF Customer or Partner segment UNION install-base table UNION motion denylists; never SF alone):
- `customer_am`: any current customer. Reason and pages go to the AM's clearance sheet in the BO expansion process, never to a cold sequence. A customer reading the Back Office Optimizer page is the best BO expansion signal we will ever get, so it must reach the AM, just not through this loop's cold lanes.
- `rep`: score >= 60 AND the account is named (in a live motion roster, in the Stars Tier A+B universe, an SF Prospect with an owner, or already in a live lemlist sequence). A live-sequence account that comes back to the site is `rep` at any score.
- `cohort`: ICP-fit (TAM engine fit >= 50, or vertical in the six plus 1,000+ employees when we have no fit row) AND score >= 20 AND not `rep`.
- `hold`: everything else. Rolls off at 45 days.
- `excluded`: triage drops.

## 6. Lane A: rep, same day

Trigger: a company flips to `rep`, or an in-sequence company shows a `web_from_us` or `web_product` session.

What happens, automation first, judgment checkpoint inside the flow:
1. Find the right people at the account. Already-known contacts first (Audiences people at that company with `Clay Persona Key` in icp), then the free sourcing path (Clay CLI advanced search, 0 credits) for 3 to 6 Director+ names in the persona the page implies (BO page implies bo_claims/bo_shared/coo_finance; platform page implies cc_ops/wfm/cx).
2. Post to the rep's channel (`#gtm-outbound-nathan` or `-jack`, ownership from SF Owner ID, default Nate for US and Jack for UK): account, what they read and when, the trigger stakes line from `triggers.json`, the 3 to 6 names, and an Approve/Deny (`slack-send-for-approval-to-channel`).
3. Approve pushes the names into the matching lemlist campaign with the signal as a variable (`lemlist-add-lead-to-campaign-v2`), so email 1 can say what they were reading without saying we watched them (house rule: reference the topic, never the visit). Deny writes `hold` with a reason.
4. Aperture widening, per the automation-first positioning: after two cohorts with zero bad approvals, named accounts already in a running sequence skip the button; net-new accounts keep it.

Why a rep would actually use this: it is the one alert that tells Nate which of his 10,000 dials to make first, and it lands in the channel he already reads. Nothing new to open.

## 7. Lane B: cohort, every two weeks, ads and sequence on the same clock

Cohort day is every other Tuesday, aligned to the Naveen cadence, first cut Tue Sep 8 if the pixel is live by Aug 28.

The clock (business days):
- T0 Tue: `cohort-cutter` freezes the segment: every `cohort` company, plus every company already staged for that fortnight's lemlist wave (a wave is a cohort whether or not it came from web intent; this is Melissa's ask applied to all outbound). Expands to people: known ICP contacts at those companies plus the free sourcing path to reach ~6 per account. Enforces 300 matchable people minimum (about 50 accounts); if short, the cut waits a week rather than shipping a list LinkedIn will reject. Assigns holdout: accounts split by hash, half get ads plus sequence, half sequence only. Writes the manifest (`motions/signal_marketing_loop/cohorts/GTMENG-YYYY-MM-DD.md`) and the SF campaign name `GTM Eng - <motion> - <cohort id>`.
- T0 Tue: ads audience ships. Clay Ads sync from the `Heat Cohort - <id> - ads` segment if we are on Growth or Enterprise; otherwise the CSV (email, first, last, company, title, country) goes to Sierra for a list upload. Either way the audience name equals the SF campaign name. Exclusion audience `Current Customers (SF) UNION install base` ships once and resyncs.
- T2 Thu: LinkedIn finishes matching. Sierra turns the campaign on. Creative: the thought-leadership format that already pulls 8% CTR, vertical-cut, landing on the Humana webinar page or the Sep 2 DMG recording, both carrying UTMs `utm_source=linkedin&utm_campaign=<cohort id>`. Conversation ads from the SC, if she keeps that format, use the same audience.
- T5 Tue: lemlist email 1 goes out (staged in draft by the cutter, launched by the rep, no AI voice, per Jason Jones's pilot conditions). Ads have had three business days of warm-up, which is what Melissa asked for.
- T5 to T20: sequence runs. Every cohort company that hits the site fires Lane A with `web_from_us`. That is the closed loop and the part reps will feel first.
- T25: ads stop; audience rolls into a standing retargeting audience (Tom's cookie point) so the spend is never wasted.
- T30: scorecard.

What marketing owns: budget, creative, Campaign Manager, Pardot. What we own: the list, the timing, the sequence, the attribution stamp, the scorecard. Carter is the bridge on both sides and already has Clay access.

## 8. Attribution, decided before the first cohort, not after

- Every person the cutter creates or touches gets Lead Source `GTM Engineering` and Primary Campaign Source `GTM Eng - <motion> - <cohort id>` in Salesforce (Clay `create-object`/`update-object`; read the field mapping back once before the first write, per the Carter rule).
- A meeting booked by Nate or Jack off the sequence or the call-behind is a GTM Engineering meeting on the council's meeting log, whether or not the person also saw an ad. Ads are assist, recorded on the same campaign.
- A person in the cohort who converts through a Pardot form during the cohort window stays Digital (Sierra's row) with the same Primary Campaign Source, so Genna can cut "integrated cohort" across both rows with one filter. Nobody loses credit; the cohort id is the join key.
- The test vs holdout split is the number John asked for without asking: cost per meeting with and without ads, on the same list, same fortnight.

This needs the Lead Source and Lead Origin values to exist before Sep 8. The ticket is already specified in `Pipeline_Council_Mapping_Aug24.md`; it is the first dependency on the critical path.

## 9. Scorecard (per cohort, feeds the rundown, the Friday readout, and the monthly council CSV)

Accounts and people in cohort; test vs holdout; ad impressions, CTR, and spend (Sierra); site sessions from cohort accounts by test arm (pixel plus UTM); lemlist delivered, clicks, replies, positive replies; meetings booked (from `impact/outcomes.csv` and the receipts ledger); opps and ACV created (Audiences deals, candidate rows until confirmed); cost per meeting including the ad spend share vs Cold's $3,402; meeting-to-opp vs 19%. Surfaced and realized never blended.

## 10. What I would not build, and why

- Bombora, Intentsify, or Delivr topic intent through Clay. 6sense already does this, the credits are real, and topic intent has not moved a needle here that anyone can name. Revisit only if 6sense is not renewed.
- Person-level de-anonymization (lemlist's website-visitor agent) on day one. It is compelling (US visitors resolved to a name and seniority) and it is 20 credits a signal, and a healthcare and financial-services vendor identifying anonymous visitors by name is a Jason Jones question before it is a build. Decision, not a default. If approved, it becomes a second input to Lane A only, never to ads.
- A new dashboard. The council has one; our row goes into it. The Heat List is a segment in Clay, visible to Carter and Genna where they already work.
- A new Slack DM. Rep alerts go to the rep channels that exist; Dallas sees the consolidation in the 7:50 rundown.
- Auto-sending on intent with no warm-up. The ads-first clock exists so email 1 never lands cold on a C-suite inbox.
- The Apollo visitor tracker. Dead end; Apollo is not in the sending path.

## 11. Costs and the tests that precede them

- Pixel: unknown unique-IP volume. Set the connection credit cap at 500 for a 14-day read, waterfall mode, then set the monthly cap from the observed rate. This is over the 100-credit line, so it needs an explicit go.
- Sourcing to fill cohorts: 0 credits on the free path; email waterfall only where a person has no verified email, ~13 per row, estimated per cohort in the manifest before the cut.
- Clay Ads enhanced matching: skip; work emails match 60 to 70% on LinkedIn and the 300 floor is the only constraint that matters. Revisit if a cohort keeps landing under 300.
- Ad budget: marketing's, sized by Sierra. Suggested opening: one cohort at the spend of the Jen post ($1,500), because that creative is the proven one.

## 12. Build plan, dependency order

Do nothing on steps 3 onward until the step before it is confirmed.

| # | Step | Who | Blocks |
|---|---|---|---|
| 1 | Create the Website visitor tracking table in Clay (UI), waterfall mode, 500-credit cap, copy the snippet | Dallas, ~5 min | everything |
| 2 | Send the snippet to Carter and Sierra as a GTM Custom HTML tag on All Pages (`GTM-WSDB2RL`), publish; verify the first sessions in the table within 24h | Dallas sends, Sierra publishes | 4, 5, 7 |
| 3 | File the Lead Source `GTM Engineering` and Lead Origin ticket (already specced), ask Genna for the helper-tab row | Sierra files, Naveen backs | 8 |
| 4 | Add the `web_*` and `lemlist_*` trigger families to `triggers.json`, page-class map in config, tests green | Agent | 6 |
| 5 | Create the five Heat fields and the segments (`Heat List`, `Heat Cohort - <id> - ads`, `Heat Cohort - <id> - holdout`) in Audiences, 0 credits | Agent | 6, 7 |
| 6 | Build `heat-list-scorer`: reads intent rows (`clay tables rows list`), relay log, staged war-room signals, webinar routes; scores per config; stamps Audiences through a `Heat Stamp` workflow on a webhook trigger (`upsert-audiences-record`); Lane A posts to the rep channel with Approve/Deny; writes `automation/logs/heat-list-<date>.md` with `evt:` anchors; runs 7:20 and 13:00 weekdays; log-only wrapper, LATE_RETRY, net shim like the other 18 | Agent | 7 |
| 7 | Build `cohort-cutter`: the T0 freeze, 300 check, holdout split, manifest, ads CSV or Clay Ads sync, lemlist draft load (gated), SF campaign stamp; bi-weekly Tue 8:00 plus on demand | Agent | first cohort |
| 8 | Confirm Clay plan tier for Ads; if Growth/Enterprise, Sierra connects Campaign Manager inside Clay (needs her role); if not, CSV path stands | Dallas asks Clay CSM, Sierra connects | ads sync automation |
| 9 | Add the heat log as a rundown source; add cohort scorecard to the Friday readout and the monthly council CSV | Agent | reporting |
| 10 | Two-cohort review, tune weights and thresholds, widen the Lane A aperture | Dallas with Naveen | steady state |

Ordering traps: creating the table generates the snippet, so 1 precedes 2; do not build 6 against a table with no sessions (nothing to score, and the field ids must exist first); LinkedIn needs 48h so the ads audience must ship on T0, never the day before email 1; the Lead Source value must exist before the first cohort's SF writes or the whole cohort lands in Digital or Exclude.

## 13. Decisions for Dallas

1. Go on the 500-credit pixel read (over the 100-credit line).
2. Person-level identification via lemlist: raise with Jason Jones, or park.
3. Cohort day Tuesday on the Naveen cadence, first cut Sep 8.
4. Holdout: 50/50 by account for the first two cohorts, then shrink to 20% once the effect is measured.
5. Which motion runs the first cohort: the all-hands lemlist sprint (Naveen's three-week sprint) is the natural one; the BO expansion motion stays on its own AM-cleared clock and only feeds `customer_am`.

## 14. Signals 1, 3, 4: build state (Aug 25, afternoon; all dry run, 0 credits spent)

Dallas's ask: add `li_engaged` and `sf_activity` to the trigger taxonomy with tests, create the people-side signal fields, draft (not publish) the LinkedIn-engagement workflow, build the Salesforce-activity segment set, and price a 20-row job-change test before running it.

**Engine.** `tam-outbound-engine/config/triggers.json` now carries 19 families. `li_engaged` (weight 12, fresh 14d / stale 45d / floor 0.3, person-level, source `clay_li_engagement`) sits between a content read (8) and a product-page read (30) on purpose. `sf_activity` (weight 14, fresh 30d / stale 90d / floor 0.4, company-level, source `audiences_sf_activity`) carries four subtypes in the trigger detail: `closed_lost_aged`, `open_deal_moved`, `renewal_120d`, `customer_quiet_90d`. Every family now has a `source` and a `stakes` line (two older ones were missing stakes). Tests 33/33.

**Audiences people fields (0 credits).** Clay Person Signal `audf_0tkbpqqoebvN3zTmzbd` (text, family key), Clay Person Signal Date `audf_0tkbpqq7XiDESb6hZA6` (date), Clay Person Signal Detail `audf_0tkbpqqozXiHyan2WC4` (text, "reaction:like | post label"). Person-level signals write here; Heat Stamp keeps writing the company fields.

**Segments (0 credits, counts on Aug 25).**

| Segment | Id | Root | Count | Lane rule |
|---|---|---|---|---|
| SF Activity: closed_lost_aged (6-24m, not customer) | `audseg_0tkbpsgNm3aaB2ydJaz` | companies | 68 | cohort or rep after the exclusion UNION |
| SF Activity: closed_lost_aged contacts | `audseg_0tkbpsgDgSH7hDchH8T` | people | 170 | Lane A candidates |
| SF Activity: open_deal_moved (updated 14d, HOLD) | `audseg_0tkbpshtP3k2bxRFFmy` | companies | 153 | HOLD, the AE owns it |
| SF Activity: renewal_120d (customer, closing in 120d) | `audseg_0tkbpshGdT8nbdCovik` | companies | 25 | customer_am only |
| SF Activity: customer_active_90d (helper) | `audseg_0tkbpu9rwEBwWVYzSao` | companies | 84 of 92 customers | scorer computes quiet = customers minus this (8 today) |
| LI Engaged (li_engaged, last 45d) | `audseg_0tkbpshaAW3mcvvobJ4` | people | 0 until workflow B runs | Lane A after the UNION |
| JC Watch: customer WFM leaders with LinkedIn (test roster) | `audseg_0tkbpyip5Kkvyok7wdd` | people | 173 | source for the 20-row job-change test, nothing runs on it without a go |

Two things the data forced. Salesforce's closed-lost set in this workspace is half `Unqualified` stage (50 of the naive 111 accounts); the segments filter to stage contains "Closed Lost". And Clay's `NoItems` collection filter over deals returned `server_error` twice, so "customer with no deal touch in 90 days" is computed by the scorer from two segments instead of saved as one. `opportunity_type` is empty on every deal, so "renewal" is read as a customer account with an open deal closing inside 120 days.

**LinkedIn engagement workflows (draft, validated, NOT published).** List mode (Repeat) is not enabled on this workspace, so one workflow cannot loop over engagers. Two workflows instead, mirroring the webinar backfill pattern:

- **A** `wf_0tkbpqrVPgA4h5NKanZ`, manual trigger `post_url` (+ `post_label`, `signal_family`): post reactions (up to 50, 0.5 credit) -> post comments (up to 10, 0.5 credit) -> code merge to a deduped person list at `$.engagers`. **1.0 credit per post, so 5 posts = 5 credits.**
- **B** `wf_0tkbq0fNEMoG6PTVFfg`, manual trigger one engager: look up in Audiences by LinkedIn URL (free) -> known? -> stamp the three person fields on the existing record (free) or exit `net_new` with nothing written. Net-new engagers surface in the run log for a human decision; the workflow never creates a person.
- Fan-out: `heat-list-scorer` reads A's output and starts B per engager through a routine with `--bulk`. Wire-up order: publish A, run A on the 5 URLs, read engagers, publish B, create the routine, bulk run. Nothing in that order happens before Dallas's go.
- Open input: the 5 latest company post URLs. linkedin.com/company/intradiem/posts is a login wall from the CLI; the search index only surfaces 2022 to early-2025 posts, so a human pastes the current five into `heat_loop.json -> workflows.li_engagement.post_urls`.

**Signal 1, job-change test: cost before running (not run).** Roster: the 173 customer WFM leaders with a LinkedIn URL (segment above); take the first 20. Three ways to detect a move, priced from the action catalog:

| Method | Per row | 20 rows | What it gives |
|---|---|---|---|
| Enrich person (`cpj-enrich-person`) and compare `latest_experience.company_domain` to the Audiences account | 0.5, charged only when a profile is found | **at most 10 credits** | current employer and title, our own diff logic, same action the webinar flow already uses |
| Lusha "Find person signals" (`companyChange`, `promotion`) | 8 per signal found | 0 to 160 | vendor-detected change events, no diff logic, expensive when it fires |
| Clay's native job-change signal (Audiences activity type `JobChange`, workflow trigger `signalId`) | not visible from the CLI | unknown | continuous monitoring, the right long-run answer; pricing must be read in the Signals UI |

Recommendation: run the 20-row test on method 1 (10 credits ceiling, well under the 100-credit line), measure how many of 20 show a move, then price native monitoring from the UI screen before choosing the standing method.

**Config.** `automation/config/heat_loop.json` (main checkout) registers every id above under `audiences.people_fields`, `audiences.segments`, `workflows.li_engagement`, and a new `sf_activity` block with per-subtype lane hints. Scorer code to read the new segments and A's output is the next build; nothing in this section flips `dry_run`.
