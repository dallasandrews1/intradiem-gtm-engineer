---
name: nate-campaign-structure-review-sep4
description: "Sep 4 2026 review of all 11 Nate lemlist campaigns against the nine-line multichannel standard; findings, proposals staged (nothing applied), page on the Desktop, sources in motions/shared/campaign_structure_review_sep4/"
metadata: 
  node_type: memory
  type: project
  originSessionId: 834b47fa-3282-47e1-b93a-77ef3681b930
  modified: 2026-09-04T17:10:07.424Z
---

Sep 4 2026 evening: every Nate lemlist sequence pulled (both A/B variants, branches, task titles), readiness run on all 11 (all "ready"), 33 previews clean. Page: `~/Desktop/Intradiem Deliverables/Nate_Campaign_Structure_Review_Sep4.html`; generator + raw sequence trees in `motions/shared/campaign_structure_review_sep4/`. Nothing applied; proposals wait on Dallas's go.

Findings that matter beyond this page:
- The lemlist team has NO custom tracking domain (customDomain null). lemlist now blocks sending when open/click tracking is on without one. Tracking is ON on Quality, BO x4, Net-New, DWO; validate_campaign_readiness does NOT catch this. Fix = trackOpens/trackClicks off (update_settings or UI), keep trackReplies.
- BO customer x4: accepted-connect conditional exists with BOTH branch sequences EMPTY; root LinkedIn message and root call fire for every lead. Net-New and DWO have no conditions. DWO LinkedIn message is auto-send.
- Resurrection: "Opened email" branch is dead (trackOpens false), two STRAY steps still live (root voice note stp_6eBfPTm3Y92XNT363, Yes-branch task stp_MPXXucbkXwjkiiJSP); "just tried you" A/B already has winner A picked (locks A/B for that campaign). Hartford has a stray ROOT voice note stp_6s7955iZXipEEB2Xr (auto, no audio).
- Quality/Finance voice-note steps have empty bodies; leads carry voice_script; Citizens/Hartford put {{voice_script}} in the body (the pattern to copy).
- Relay map covers only Stars x3 + Blitz x2 of Nate's 11; BO x4, Net-New, DWO unrouted. action_brief.json has no BO/DWO blocks, live=false since Aug 17 (plan is now Multichannel).
- LinkedIn account limits: 20 invites / 30 messages / 30 visits per day. DWO 803 leads must be paced (15-20/day) or the invite queue drags E2/E3.
- lemwarm via API: active on Nate's MAIN mailbox usm_BuFNcjKBEvKKABRid since Aug 31 (score 81). The intradiemhq.com mailbox (dem_LhnG9Z4ybizDhnfkE) has no usm id visible to this key; lemwarm settings 404 on the dem id. UI check still required before the sender switch.
- get_settings type=sending shows no email accounts for the API key owner, so Nate's daily email limit is unreadable by API.
- Contact-field collision live: steve.hagerman@truist.com carries companyName/parentAccount JPMorgan (Sep 3 DWO push). Titles with notes: Keenan, Librera.
- Blitz "$6.1M large North American bank" = RBC story cited blinded; registry allows blinded citation. Pass, no copy change.
- Citizens has autoReview true (held Foss play at risk).
- eHarmony.com in DWO is tagged Telecom and gets the device-season opener; wellabe/CarParts.com are brand styling.

Standard used (Dallas's nine lines): channels, branching, testing, timing, variables, replies, measurement, deliverability, gates. Deliverability trade-off recorded: click-fired call task waived while tracking stays off; calls fire on accepted connect and the phone branch.

Related: [[lemlist-api-sequence-step-limits-aug31]], [[bo-lemlist-shells-built-sep2]], [[bo-netnew-package-sep2]], [[naveen-call-sep2-demo-three-acts]].

**v2 (Sep 4 evening, Dallas's call): steps over doctrine arc.** Dallas asked for sustained executive pressure (calls, DMs, follow-up DMs, emails), especially on DWO. Page rebuilt on a pressure model: 5 emails in two threads, 3 calls, ALL with voicemail as of Sep 4 late (Call 1 short-version note, Call 2 paired with the same-hour "just tried you" email, Call 3 closing this-year-or-next), 3 LinkedIn DMs for accepted connects, manual voice note, like + second visit for non-connects, invite withdrawal at d20; 16-17 touches over 18 business days; Second Look campaign for non-responders after 20 quiet days. Applies to DWO and Net-New fully; BO customer lanes get the same inside Mary Ann's rule (calls only on a call_cleared lead variable); Stars/Blitz extend to 16 days with a third call, one-question Email 3, closing DM. Facts driving it: DWO leads carry ZERO phones, ZoomInfo 500-list overlap = 4 emails / 0 accounts, DWO is all C-level (no tier column), 84 new-in-role, 166 multi-seat accounts (624 people). Phone sourcing plan in priority order via Clay waterfall, [estimate] 5-8 cr per number, 20-row test then Dallas's go. Nate load at 20 leads/day ~ 25-35 dials, 12-15 DMs, 4-6 voice notes. Eight DWO step drafts on the page (Nate reads). Doctrine's "no phone on C-level" is overridden by Dallas for this motion.

**v3 (Sep 4 evening): DWO tree BUILT by API** on Dallas's go, adapted to a condition Dallas created in the UI mid-build (root accepted-invite condition; Email 1 variant A subject also changed in the UI to "Quick idea to cut agent idle minutes at {{companyName}}", flagged, not touched). 33 steps, three leaves; IDs in motions/dwo_executives/DWO_Exec_Tree_Built_Sep4.json. API lessons: on a DRAFT campaign delete_sequence_step works even with reviewed leads (the Aug 31 refusal was on a paused/launched campaign); email, phone, linkedinSend, like, visit, withdraw steps all add fine inside condition branches (only voice notes refuse); one add returned "Anthropic Proxy: Invalid content" and was NOT created, so re-read the tree before retrying. {{peak}} values that start with "the" break possessive copy ("wellabe's the Q4 peak"): write "at {{companyName}}" constructions instead. Manual voice note in the Accepted branch is still a UI add. Phone test HELD (20 rows = 256 cr at 12.8/row, over the 200 line).
