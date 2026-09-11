# Open items as of Fri Sep 4 2026 (end of day)

Standing mandates
- Pipeline Council: our row is judged on cost per meeting vs Cold's $3,402 and 19% meeting-to-opp; report in the council's columns; every sourced contact stamped Lead Source `GTM Engineering` (ticket with Sierra, Lead Origin value still open); monthly meeting CSV in the Cold outreach data schema; Melissa's on-record ask: LinkedIn ads on the same list as the lemlist sequence.
- John (CRO): more meetings, DWO lands at the C-suite, VITO per account (AE confirms), a one-page brief in his ten rows for every campaign idea; bi-weekly GTM campaign alignment Thu 11:00 CT (next Sep 17, Oct 1).
- Naveen: 15 meetings through new channels is his OKR bucket; Dallas's OKRs written the week of Sep 7 as shipped artifacts and disciplines, never outcomes owned by others; all-hands demo video due Tue Sep 8; back office ~300 sequenced by the all-hands week of Sep 14.
- Mary Ann: AM clears every customer-lane name before Nate calls behind an email; no one under the current sponsor's line.

Live state
- lemlist: BO customer lanes loaded and paused (HC 67, FS 79, Ins 33, BPO 20) from Nate's main mailbox, exclusion gate PASS, waiting on Nate's clearance read. BO Net-New 130 loaded, paused, all fixes applied, waits for the warm intradiemhq.com mailbox (target Sep 21, earliest Sep 18; confirm lemwarm is active). DWO Executives - Live Pool (Nate) cam_SiD4KmWcRuhiF6uhL staged as a draft, five touches, zero leads. Stars x3 and Blitz x2 paused pending Nate. Three empty (SF) list shells to delete in the UI.
- Clay / pool: DWO live universe 4,363 at 564 accounts (96% not in SF); wave 1 done (1,061 on list, 758 verified emails, 978 LinkedIn URLs); 172 rows in two stuck routine runs (~275 credits to re-run); wave 2 = 2,669 EVP/SVP/Head, ~4,300 credits at 1.6/row, not started. Balance ~65K credits. Warn line 200 credits per run, 10-20 row test above it.
- Signals 1/3/4 (job change, LinkedIn engagement, SF activity) built as drafts, not published; heat loop and Lane B (lemlist + LinkedIn Matched Audiences on one clock) designed, not running.
- Partner pilot (Haresh/Frank) live at gtm-partner-pilot.pages.dev; 5-10 account pilot on the $101M pre-pipeline.
- Inger's 12 back-office maps built in Sales Nav; clearance is the next step. Nate's six net-new maps done.
- Product AI Champion: three goals marked done, PMO extractor next quarter; Greenlight agent pack staged.

Next moves in order
1. Nate clears customer lanes, start them one by one (readiness check first). Send the Slack note.
2. Confirm lemwarm on nathan.belfield@intradiemhq.com; net-new starts on the warm mailbox.
3. DWO: title filter, load the 758 verified into the shell with `opener` / `workTeams` / `peak` filled (new-in-role rule first), Nate reads copy, no launch. Then wave 2 sizing after first replies.
4. Enrichment backlog: every pool contact with an email AND a LinkedIn URL (free bridge for URLs, Work Email + ZeroBounce 1.6/row only on confirmed-current people; Enrich Person 0.5 on misses).
5. Lead Source `GTM Engineering` stamping on every contact created; council CSV feed.
6. Lane B pilot: one cohort to lemlist and LinkedIn Matched Audiences on the same clock, with a holdout, for the council's cost-per-meeting row.
7. Sep 17 alignment meeting: DWO executives brief in John's ten rows; Stars adjustments.
8. OKRs draft to Naveen (motions/shared/OKRs_Dallas_Draft_Sep2.md) week of Sep 7.

## Sep 4 evening pass (dry run, 0 credits spent)

Delivered (all on the Desktop under Intradiem Deliverables, sources in the repo)
- DWO shell load plan: `motions/dwo_executives/load_dwo_shell.py` (dry run; --go loads, never launches). 700 loadable of 1,135 at 285 accounts; 76 new-in-role (rule A); angles core 450 / customer 160 / transformation 90 with 182 family swaps; 32 provider-unit COOs flagged for Nate; 4 stay in BO Net-New (Elwood, D. Clark, S. Smith, Malee); mm@fidelity.com disputed; 52 title-filter holds (chief of staff, deputy, associate, chief nursing, chief medical added). Nate read page: `DWO_Executives_Nate_Read_Sep4.html`. Email 1 needs the angle-variable edit (angleIdea / angleProof / angleAsk) BEFORE the load; copy-paste prompt on the page.
- Lane B pilot rides on DWO wave 1: cohort GTMENG-DWO1-2026-09, sha1-by-domain split (same rule as cohort_cutter), test 337 people / 144 accounts (ads + sequence), holdout 363 / 141; ads CSV `GTMENG-DWO1-2026-09_ads_linkedin.csv`; SF campaign `GTM Eng - DWO Executives - Wave 1`. cohort_cutter dry run itself is WAITING (heat pool empty, scorer dry).
- Enrichment backlog page + CSV (`motions/enrichment/`): 673 gaps across pools. Email-only 85 (free bridge), URL-only 588 (DWO 289 incl. 177 rows never returned by the two stuck runs, WFM 206 parked). Run C (re-run 177, ~283 credits) is over the 200 line: 15-row test then Dallas's go, or cancel.
- Council feed: `automation/council_meeting_feed.py --month YYYY-MM` writes the meeting CSV in Genna's schema (0 rows for Aug and Sep today). Stamp plans: `automation/lead_source_stamp_plan.py` wrote 11 CSVs (1,141 rows) in `motions/pipeline_council/stamp_plans/` (Lead Source, Lead Origin, Primary Campaign Source per lemlist campaign, cohort arm). No Salesforce write exists; Sierra's ticket is the gate.
- Sep 17 brief: `DWO_Exec_Brief_Sep17.html` (John's ten rows, wave 2 sizing 164 EVP / 621 SVP / 1,884 Head, Stars adjustments: VITO thread per parent + own SF campaign).
- OKRs: `OKRs_Dallas_Sep7.html` from the Sep 2 draft, with the Slack note to Naveen.

Checks
- Warm mailbox nathan.belfield@intradiemhq.com: active in lemlist, 4 days old, DNS 100/100 (MX, SPF, DMARC quarantine, no blacklists). lemwarm status is not readable by API: confirm in the lemlist UI before the sender switch.
- DWO campaign sender is still the intradiem.com main mailbox; switch only when lemwarm clears (Sep 21 to 28).
- Stuck runs still in_progress: run_0tktg67B6g9g3PcGcmh 98/100, run_0tktgpqEnKpc4jMdnjN 71/72.
- Clay balance 64,997.

Nate's DM review (09:51 to 10:03 CT, separate thread, notes in motions/back_office_expansion/Nate_Review_Notes_Sep4.md): Insurance, Healthcare Payer and BPO cleared on copy and contacts; Financial Services still "thinking through", do not start FS; Maximus added to BPO (5 loaded, Baylinson held, BPO now 25, 6.5 credits); Nate owes good-reply examples for the messaging models; Frank's partner brief also covers Maximus (heads-up before BPO starts).

Next moves (order)
1. Nate reads the DWO page; Dallas gives the go: Email 1 variable edit, then load 700, then integrity sweep.
2. Run A (free bridge on 85 email-only rows) on Dallas's word; run C test (15 rows) before any re-run decision.
3. Lemwarm confirmed in UI, sender switch, readiness check, ads CSV to Melissa/Sierra with the launch date.
4. BO: the 332 loaded already clear the 300 line; next pool = free Clay pull on Inger's nine remaining accounts (layer gaps in `_layer_gaps.json`), 0 credits, after clearance starts.
5. Wave 2 sizing after first DWO replies (EVP+SVP first, ~1,260 credits, Dallas's go).

## Sep 4 late morning, executed on Dallas's go
- DWO shell LOADED: Email 1 A/B now per-lead angle variables; 690 leads in cam_SiD4KmWcRuhiF6uhL (699 loaded, 9 removed after the free bridge found movers and noise, 1 duplicate), test 336 / holdout 354, 64 without a LinkedIn URL flagged as current-role unconfirmed; three previews clean; campaign DRAFT, sender still the main mailbox, nothing sent.
- Run A (free bridge, 85 rows): 15 found, 70 miss. Run C test: 15 rows, 11 valid, 45.6 credits (3.04/row, over the 30 ceiling); full re-run of the remaining 162 would be ~490, held for Dallas.
- Next: Nate reads the page (three calls + the 64 unconfirmed); Enrich Person by email on the 64 (~32 credits max) or hold them; lemwarm confirmed in UI, sender switch, readiness check; ads CSV to Melissa/Sierra with the launch date.

## Sep 4 afternoon, spend delegated to Claude
- Enrich Person on the 64 no-URL leads (20 cr): 35 confirmed, 5 movers removed, 24 no profile (kept). Stuck 162 rows re-run: Work Email by URL 110 of 125 found (139 cr, 1.07-1.42/row), workflow on 17 no-URL rows 14 valid (17 cr), Apollo on 20 bank rows 10 verified (17 Apollo cr). Total 176 Clay + 17 Apollo.
- Loader --go added 119: DWO campaign now 804 leads at 346 accounts, test 399 / holdout 405, 36 with no URL, DRAFT, sender still the main mailbox, nothing sent. 36 provider-unit COOs flagged. Angles re-aligned on 5 leads after the load.
- Rule learned: Work Email routine by LinkedIn URL beats the name-and-domain workflow on cost and hit rate; banks still go to Apollo.
- Still Dallas's hands: lemwarm confirmation in the lemlist UI, sender switch, Nate's read, ads CSV to Melissa/Sierra with a launch date.

## Sep 4, copy check and Nate page
- DWO copy re-checked against the Sep 3 doctrine: Email 1 trim was REVERTED on Dallas's call (copy stands as written, median 128 words); Email 2's "In 2025" dropped from the VTO line (source has no year). All Humana figures re-verified 1:many. Opt-out not required (US prospect lane). Nate has NOT reviewed DWO copy yet; his DM review was the four BO customer campaigns.
- Shareable Nate page live at https://dwo-exec-read.pages.dev (project dwo-exec-read). The Desktop DWO_Executives_Nate_Read_Sep4.html stays Dallas-only (credits, prompts, removals). Vega (audit COO) removed; campaign 803 leads.

## Sep 4 evening, DWO pressure tree BUILT (Dallas's go, adapted to a UI edit)
- cam_SiD4KmWcRuhiF6uhL rebuilt by API in draft: root E1 (locked) + visit d0 + has-URL split; URL side: connect (A/B note vs blank), Call 1 no VM (EA route), E2 thread; no-URL side: calls and emails only; then the accepted-connect split (the condition created in the UI, set to within 2): Yes = DM1, Call 2 VM + same-hour "just tried you", Email 3 new thread (peak), DM2, Call 3, Email 4, DM3, breakup; Else = like, Call 2 VM + JTY, Email 3, visit, Call 3, Email 4, breakup, withdraw invite. 33 steps, three leaves. IDs in motions/dwo_executives/DWO_Exec_Tree_Built_Sep4.json. Readiness: ready. New step bodies marked [draft, Nate reads].
- Found during the build: Email 1 variant A subject changed in the UI to "Quick idea to cut agent idle minutes at {{companyName}}" (variant B still "idle minutes at {{companyName}}"). Not the agent. Needs Dallas's call: it makes the A/B a subject-plus-close test and "Quick idea" sits next to a banned opener.
- Dallas's hands: manual Voice message step in the Accepted branch after DM 1 (API refuses it there); sender switch after lemwarm; phone sourcing above the 20-row test (12.8 cr/row managed routine = 256 for 20, over the 200 line; 15 rows = 192).
- Also done: eHarmony lead fixed (name, opener, workTeams, peak, angleAsk); cohort manifest GTMENG-DWO1-2026-09.md with pacing and read dates; phone priority CSV + 20-row test file in motions/dwo_executives/phones/. Zero credits spent, nothing sent, sender unchanged.
- Rule: calls and voicemails are the spine of every net-new sequence from now on (memory feedback-calls-first-net-new).
- Sep 4 late: all three DWO calls now leave a voicemail (Call 1 the short-version-in-your-email note, Call 2 the overtime voicemail paired with the just-tried-you email, Call 3 the closing this-year-or-next question), EA route kept on every call. Five phone steps updated by API, previewed first.
- Sep 4 late, timing fix: delays were compounding (relative, not absolute); Call 1 and Email 2 on the URL path set to +1, Email 3 new-thread steps to +2. Arc is now the 18-business-day design (breakup d18, withdraw d20).
- Sep 4 late, Dallas's rule applied to the DWO drafts: no admitting you don't know the org, no apologies, no exit talk except the one breakup. Rewritten by API (11 steps): "just tried you" (x3), DM 2, Email 4 (x3), DM 3, Call 3 (x3). Multi-thread close added: Email 4 carries {{colleagueLine}} ("X owns the transformation side of this at AES, so I've sent the same note there" / same-family: "X has the same note from me, since the overtime line at AOL runs through both your teams"), DM 3 and Call 3 carry {{colleagueFirst}}, all inside Liquid if-blocks so single-seat leads see nothing. Colleague map: motions/dwo_executives/DWO_Colleague_Map_Sep4.csv (624 leads, 166 accounts, 249 same-family pairs). Push script motions/dwo_executives/push_colleague_vars.py (REST, POST then PATCH on /api/leads/{id}/variables; needs a User-Agent header or the API returns 403). Launch rule: all seats at an account enter the same day.
- Sep 4 late: colleagueFirst and colleagueLine written on all 624 multi-seat DWO leads (0 missing, 0 failed; log automation/logs/dwo_colleague_push_sep4.log). Single-seat leads (179) carry neither by design.
- Sep 4 late: Email 1 variant A subject ("Quick idea to cut agent idle minutes at {{companyName}}") is Dallas's decision, taken on the lemlist agent's suggestion. Closed. The A/B is a package test (subject + close together); recorded in the cohort manifest.
- Sep 4 late (Dallas, UI): lemwarm is active on all mailboxes, including nathan.belfield@intradiemhq.com and jack.ohagan@intradiemhq.com. The API only exposes the main mailbox (usm_BuFNcjKBEvKKABRid, active since Aug 31, score 81). Sender switch still waits for the warm-up window: earliest Sep 21 if the intradiemhq.com warm-up started Aug 31, about Sep 25 if it started today. Week one on the new mailbox stays at 10 to 15 emails a day.
- Sep 4 late, platform fixes APPLIED: tracking off (opens, clicks) on Quality, BO x4, Net-New, DWO; onReplied = stop + create task on BO x5 and DWO; relay campaign_channel_map now carries all 11 Nate campaigns (13 total with Jack's two); action_brief.json has backoffice and dwo blocks for nathan (live still false). Resurrection dead "opened" branch swapped to hasEmailAddress (everyone gets the "one more" email). Quality and Finance voice-note bodies now {{voice_script}}. Citizens autoReview is not exposed by the settings API: UI toggle. Pending your confirm (irreversible skips): Hartford root voice note stp_6s7955iZXipEEB2Xr (7 leads), Resurrection root voice note stp_6eBfPTm3Y92XNT363 (43 leads); the Yes-branch stray was already skipped.
- Leadership go to resume (Slack group DM with Chris Busbee and Naveen, Sep 4 15:14 to 15:41 CT): "this is resolved and we can switch back on our campaigns" (Naveen), "Yes please resume campaigns" (Chris). Sends from the main domain, 20 to 30 a day, first new domain still warming. The Sep 3 pause was precautionary after an unrelated Salesforce email-limit error.

## Sep 4 late, CAMPAIGNS STARTED (Dallas's go, after Chris and Naveen's resume in the group DM)
- Skipped for all leads (irreversible): Hartford root voice note stp_6s7955iZXipEEB2Xr, Resurrection root voice note stp_6eBfPTm3Y92XNT363.
- Launched (first send, leads reviewed, auto-review off): BO Insurance 33, BO Healthcare Payer 67, BO BPO 25, Stars Quality 29.
- Resumed (were running before the Sep 3 precautionary pause): Stars Finance, Stars Resurrection, Blitz Citizens, Blitz Hartford.
- Sender on all eight: nathan.belfield@intradiem.com (main), 20 to 30 emails a day shared across the eight, per Dallas in the Chris/Naveen DM.
- Still held: BO Financial Services (Nate's notes), BO Net-New and DWO (warm intradiemhq.com mailbox, sender switch earliest Sep 21 to 25). DWO stays draft.
- Nate: reads scripts as the tasks reach him (Dallas, Sep 4 late). Daily brief still live=false; relay live=true with all 11 campaigns mapped.
- Nate's UI items: Citizens auto-review off (settings), the DWO manual voice note after DM 1.
