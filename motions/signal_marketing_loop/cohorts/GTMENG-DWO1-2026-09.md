# Cohort GTMENG-DWO1-2026-09 (DWO Executives, wave 1)

Salesforce campaign: `GTM Eng - DWO Executives - Wave 1`
Motion: DWO Executives (Nate), lemlist cam_SiD4KmWcRuhiF6uhL (draft)
Cut: Sep 4 2026 by load_dwo_shell.py, sha1-by-domain split. 803 leads at 346 accounts: test 399 (ads + sequence) / holdout 405 (sequence only). Ads CSV: motions/dwo_executives/GTMENG-DWO1-2026-09_ads_linkedin.csv.

## Pacing rule (Sep 4 2026)
- 15 to 20 new leads a day, never more. Ceilings: LinkedIn automation on the account (20 invites, 30 messages, 30 visits a day), the intradiemhq.com mailbox in warm-up (10 to 15 emails a day week one, 20 to 30 week two), Nate's dial and DM time (about 25 to 35 dials, 12 to 15 DMs, 4 to 6 voice notes a day at steady state).
- Test and holdout arms interleaved by day (alternate arms, or half and half each day) so both arms age at the same rate and the ads window covers the test arm evenly.
- Phones sourced a week ahead of the launch pace (motions/dwo_executives/phones/DWO_Phone_Priority_Sep4.csv), in priority order: new in role (84), multi-seat accounts (552), single seat (168).
- Wave 1 enters over eight to eleven weeks at this pace.

## Read dates (business days from the first send; earliest first send Sep 21 2026)
- Email 1 A/B read: first send + 14 business days (earliest Fri Oct 9 2026). Read on reply rate by variant, not opens (tracking off). Do not pick a winner before this date; the pick is permanent.
  - The test as set Sep 4 (Dallas's decision, on the lemlist agent's suggestion): variant A = subject "Quick idea to cut agent idle minutes at {{companyName}}" + benchmark-question close; variant B = subject "idle minutes at {{companyName}}" + offer-note close. Two variables move together, so the read says which package wins, not which element; treat it as a package test and write it up that way.
- Connect note A/B (note vs blank): same date, read on acceptance rate.
- Scorecard T30: first send + 30 business days (earliest Mon Nov 2 2026). Council row: cost per meeting against $3,402 and 19 percent meeting-to-opp, meetings from automation/council_meeting_feed.py, split by arm.
- Ads stop at T25 (earliest Mon Oct 26 2026); audience rolls to the standing retargeting audience.

## Status
Draft, sender still the intradiem.com main mailbox, nothing sent. First send waits on lemwarm clearing the intradiemhq.com mailbox (Sep 21 to 28) and Dallas's explicit go.

## Launch rule added Sep 4 late: account-complete days
Every seat at an account enters on the same day (the 166 multi-seat accounts, 624 people). The Email 4, DM 3 and Call 3 steps tell the executive that a named colleague has the same note; that has to be true by day 3. Colleague map: motions/dwo_executives/DWO_Colleague_Map_Sep4.csv (variables colleagueFirst, colleagueLine; single-seat leads carry neither and the Liquid block hides the line).
