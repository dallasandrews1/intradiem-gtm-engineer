# 6sense keyword intent as a campaign trigger: design note (Sep 9 2026)

For Carter and Sierra, from Dallas. Answers Naveen's Sep 8 ask: an actionable mechanism where keyword intent in 6sense invokes a GTM Engineering sequence within a day and shapes its timing, plus a clear line on what intent may feed the message and what never does. Dry run only. Nothing in this note stamps a record, posts to Slack, or loads a lead until Dallas says so.

Source of truth for the plumbing: `automation/config/heat_loop.json`, `tam-outbound-engine/config/triggers.json`, `automation/heat_list_scorer.py`. The strategy this extends: `Signal_to_Marketing_Loop_Strategy_Aug25.md` (the Heat List, Lane A, Lane B).

## 1. What is already true (verified Sep 9, 0 credits)

Carter's Salesforce-to-Clay mapping is live and populated. A read of 150 company records in Clay Audiences:

| 6sense field in Audiences (company) | Field id | Populated | Values seen |
|---|---|---|---|
| 6sense 6QA | audf_0tkduziXxDQmcRNqfNB | 150 of 150 | True 22, False 128 |
| 6sense Account Buying Stage | audf_0tkdv0iCtUFDmNN8aH3 | 137 of 150 | Consideration 81, Decision 21, Purchase 14, Awareness 11 |
| 6sense Account Intent Score | audf_0tkdva7d4mepxMtaGdB | 137 of 150 | 0 to 100 |
| 6sense Account Profile Fit | audf_0tkdvb23QqBxj4tXHzh | 137 of 150 | Weak 72, Moderate 40, Strong 25 |
| 6sense Temperature | audf_0tkdvbn6vTKX7gfiS7N | 147 of 150 | Cold 118, Warm 20, Hot 7, Hot (New) 2 |
| 6sense Segments (2) | audf_0tkdvbt5xi8uZgVuErt | 96 of 150 | "6s - Top of Funnel", "6s - Middle of Funnel", "6s - Top of Funnel, TAM UK", "3. Multiple Unique Website Visitors, 6s - Mid..." |
| 6sense Segments | audf_0tkdv84SAkeYjotMpHz | 0 of 150 | empty on every record sampled |

People carry the contact-level set as well: 6sense Lead Grade, Contact Grade, Lead and Contact Intent Score and Profile Fit, plus the account fields mirrored (14 fields, ids audf_0tkdvr… through audf_0tkdvz…).

Two things follow. First, the segment names 6sense already pushes to Salesforce arrive in Clay on the "6sense Segments (2)" field, so a 6sense segment is readable in Clay with no new integration. Second, no individual keyword arrives. The sync carries scores, stage, and segment membership, not the keyword strings, which is exactly what Sierra described on the call: keyword intent is company-level and anonymous. So the unit we can trigger on is a 6sense segment built around a keyword group, not a keyword.

No saved Clay audience uses any of these fields yet. That is the gap this note closes.

## 2. The path, end to end

```
6sense keyword group  ->  6sense segment "6s - KW - <group>"  ->  Salesforce Account (nightly)
   ->  Clay Audiences "6sense Segments (2)" (SF sync)  ->  Clay segment per group (0 credits)
   ->  heat_list_scorer reads the segment as a trigger family (7:20 and 13:00 weekdays)
   ->  score + lane  ->  Lane A rep alert (named accounts)  /  Lane B cohort (ICP, not yet worked)
   ->  lemlist sequence with the keyword GROUP as the angle variable, never the keyword
```

Timing. 6sense scores nightly. Salesforce receives the segment overnight. The Audiences sync from Salesforce runs on Clay's schedule (Carter to confirm the interval; the Aug 20 setup notes say it is continuous, not batch). The scorer runs at 7:20 CT. A company that crosses a keyword threshold on Tuesday is on Wednesday morning's Heat List and in Nate's channel the same morning. That meets the 24-hour bar Naveen set without anything real-time being built.

## 3. Sierra's part: segments in 6sense, one per keyword group

Build the segment, name it on the existing "6s - " convention so it lands in the same field, and confirm the sync. Suggested opening set, chosen to match the sequences that already exist so a hit has somewhere to go on day one:

| 6sense segment name | Keyword group (branded and non-branded) | Sequence it feeds |
|---|---|---|
| 6s - KW - Desktop analytics competitors | Verint DPA, Verint desktop and process analytics, NICE desktop analytics, NICE NEVA, desktop analytics, employee productivity analytics | UPT displacement (Verint attack, NICE attack) |
| 6s - KW - WFM incumbents | Verint WFM, NICE WFM, IEX, Calabrio, Aspect, Alvaria, workforce management software | WFM Present (Nate), Genesys Present |
| 6s - KW - Back-office capacity | back office automation, back office workforce management, SLA management, backlog management, work allocation, claims operations productivity | BO Net-New, BO Expansion by vertical (customer_am lane only) |
| 6s - KW - Intraday | intraday management, real-time adherence, schedule adherence, intraday automation, real-time management contact center | DWO Executives, WFM Present |
| 6s - KW - Category | dynamic workforce orchestration, workforce orchestration, Intradiem | DWO Executives |

Three notes from the call worth carrying into the build. Sierra said the tracked keyword list has been front-office weighted and needs back-office terms; the third row above is that expansion. Sierra also said profile fit should be read with a grain of salt while the ICP shifts to back office; this design never routes on profile fit (section 5). And Sierra's own suggestion was the mechanism: "push an audience segment, those are already pushing to Salesforce." That is the whole integration.

Two questions for Sierra, both answerable from the 6sense admin screen:
1. Which Salesforce field receives the segment list, and is it the one that lands in Clay as "6sense Segments (2)"? The first "6sense Segments" field is empty on every record sampled and looks retired.
2. Sierra's Sep 8 action item, unchanged: whether the technology-used field can be mapped to Salesforce. It is not in Clay today. It would give the UPT lists a fourth evidence source (the current tiers rest on public case studies, job posts and PredictLeads).

## 4. Carter's part

Nothing new to map. Confirm the Audiences sync interval, confirm the segment field refreshes on the same sync as the scores, and take the Clay invite (resent Sep 9) so the segments in section 6 are visible to you in the Audiences UI. Where the ads side comes in: a 6sense keyword segment is also a valid LinkedIn Matched Audience source for Lane B, which puts ads and sequence on the same list on the same day, the Aug 24 ask from Melissa.

## 5. What feeds the message, and what never does

This is the line Naveen asked for. It is a rule, not a preference, because the message reads as surveillance the moment it crosses it.

**Feeds the message (as the angle, never as evidence):**
- The keyword GROUP picks the angle and the sequence. A desktop-analytics hit routes to the UPT sequence, whose Email 1 already opens on the desktop report the account runs. A back-office hit routes to the back-office one-idea. The reader sees a message about their topic, written as if we had guessed well.
- The keyword group picks the persona lane (`route_personas` on the family), so the right titles are sourced at the account.
- Buying stage sets pace and directness. Decision or Purchase: the account enters Lane A if named, the direct ask arrives in Email 2 rather than Email 4. Consideration: cohort lane, ads three business days ahead of Email 1. Awareness: hold, content only.
- Timing. A hit inside the last 14 days is the reason the account is in this fortnight's cohort instead of next.
- The vertical peak line (open enrollment, Q4 claims, year-end close) is the dated opener when no account-level fact exists. The hit itself is never the opener.

**Never in the message, never in a variable, never in a rep alert as a talking point:**
- The fact of a search ("noticed you were researching", "saw your team looking at").
- Any keyword string, count, geography, or date of search.
- The 6sense score, grade, stage, 6QA, or temperature.
- A competitor name as evidence of their search. Competitor names appear only where the sequence already uses them as the account's known stack (the UPT lists are built on public and rep-confirmed evidence, and stay that way).
- Profile fit, in either direction.

**Customers.** Any current customer (Salesforce Customer or Partner segment, install-base table, denylists) is `customer_am` regardless of score. A customer researching desktop analytics is the best expansion signal the account manager will see this quarter and goes to the AM's clearance sheet with the topic, never to a cold sequence.

## 6. What Dallas builds, in dry run

Nothing here runs live. The scorer already defaults to `dry_run: true` and logs every would-be alert and stamp to `automation/logs/heat-list-<date>.md`; the flags `live_stamp` and `live_lane_a` stay false.

1. **Five Clay segments, company level, 0 credits**, one per keyword group: filter on "6sense Segments (2)" containing the segment name, minus the cold-outbound exclusion union. Ids recorded in `heat_loop.json` under a new `sixsense` block, same pattern as the `sf_activity` block.
2. **Trigger families** added to `tam-outbound-engine/config/triggers.json` (staged copy in `staged/sixsense_families.json` alongside this note). Weights sit below `web_product` (30) on purpose: a third-party inference should never outrank a visit to our own site. A single keyword hit lands a named account in the cohort lane; a keyword hit plus one independent signal (a war-room trigger, a lemlist click, a Decision stage) crosses the rep line. One inference alone never alerts a rep.

| Family | Fires on | Weight | Decay | Routes to |
|---|---|---|---|---|
| sixsense_kw_competitor | 6s - KW - Desktop analytics competitors | 28 | fresh 14d, floor 0.3 at 45d | cc_ops, wfm, bo_claims, bo_shared |
| sixsense_kw_backoffice | 6s - KW - Back-office capacity | 26 | same | bo_claims, bo_shared, coo_finance |
| sixsense_kw_wfm | 6s - KW - WFM incumbents | 22 | same | wfm, cc_ops |
| sixsense_kw_intraday | 6s - KW - Intraday | 22 | same | wfm, cc_ops, coo_finance |
| sixsense_kw_category | 6s - KW - Category | 20 | same | coo_finance, cc_ops |
| sixsense_stage_decision | Buying Stage in Decision or Purchase | 15 | fresh 30d, floor 0.4 at 120d | (modifier, no persona) |
| sixsense_6qa | 6QA true | 10 | same | (modifier, no persona) |

3. **One new source in the scorer**, `events_from_sixsense`, reading the five segments plus stage and 6QA from the company record, emitting events in the same shape as `sf_activity`. In-sequence rule: an account already in a live lemlist campaign that takes a competitor or back-office keyword hit is treated like a return visit and alerts the rep at any score, because Nate should call that account first today.
4. **Angle variable.** Lane A's staged lemlist push carries `signal_family` (the group), never the segment name or score. The sequence's Email 1 chooses its opener from the family and the account's own dated fact, per the dated-signal rule in the UPT and DWO sequences.
5. **Two dry-run cohorts** (Sep 22 and Oct 6 on the existing bi-weekly clock) read with Dallas before anything flips. The log shows, per account: which segment fired, the score contribution, the lane, and the message variable that would have been set. Sizing comes from the segments once Sierra builds them; the sample suggests roughly one in seven accounts carries 6QA and one in twenty is Hot, so the competitor and back-office groups should be small enough to read by hand.

## 7. What this gives the council

A GTM Engineering sequence that fires within a day of marketing's own intent signal, on the same list the ads run against, with a holdout. Cost per meeting with and without the intent trigger, same fortnight, same creative. It also answers John's "are we tracking the right keywords" from the other side: the keyword groups that produce replies are the ones worth keeping.

## 8. Open items

| Item | Owner | Blocks |
|---|---|---|
| Build the five 6sense segments on the "6s - KW -" convention | Sierra | Everything below |
| Confirm the Salesforce field that lands in "6sense Segments (2)" and retire the empty one | Sierra with Carter | Clay segment filters |
| Confirm Audiences sync interval from Salesforce | Carter | The 24-hour claim |
| Technology-used field mapping (Sep 8 action item) | Sierra | UPT list evidence, not this trigger |
| Clay segments, families, scorer source, two dry-run reads | Dallas | Go-live decision |
| Flip `live_lane_a` | Dallas's explicit call, after two clean dry runs | |

Nothing above spends a Clay credit. Audiences reads are the workspace's own synced data.
