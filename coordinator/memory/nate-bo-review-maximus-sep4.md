---
name: nate-bo-review-maximus-sep4
description: Sep 4 2026: Nathan reviewed the four BO customer campaigns (Insurance great, Healthcare good, BPO thumbs up, Financial still thinking); asked for MAXIMUS in the BPO campaign, five loaded same day (6.5 credits), Baylinson held; Maximus is also Frank's 3xG partner-pilot account
metadata:
  type: project
---

Sep 4 2026 (Slack DM 09:51-10:03 CT). Dallas asked Nathan to scan contacts and copy in the four paused customer-lane campaigns. Verdicts: Insurance "great, would not change, hits the mark"; Healthcare "good"; BPO thumbs up; Financial Services "thinking through", no verdict yet (do not start FS until he weighs in). No contact-level objections. He will send replies and emails that landed well as messaging context.

His one ask: add MAXIMUS to BO Expansion - BPO (cam_Fy287YF9X5fjPYBSo), "they use Verint for their back office and don't like it." Executed same day with the new reusable `motions/back_office_expansion/add_account_cohort.py <cohort> [--go]` (cohort CSV in `cohorts/`, SF check 0 cr, Enrich Person 0.5, Work Email workflow, load with the vertical's neutral enterprise_line). Five loaded (Howard, French, Hillman, Fitzwater, Biernacki, all valid at maximus.com), Baylinson held on freshness, campaign 20 -> 25, still paused. 6.5 credits actual against a 9.3-12.6 estimate. Notes: `motions/back_office_expansion/Nate_Review_Notes_Sep4.md`.

Maximus facts: not a customer or partner (SF segment Sep 1), clear to work; about 1,510 Verint Operations Visualizer seats per the 3xG sheet (internal only); Frank's partner brief on it exists (motions/partner_channel/briefs/data/maximus.json), so direct and partner motions on the same account should know about each other.

**How to apply:** the next "add <account> to <campaign>" ask from a rep = write `cohorts/<name>.csv`, dry-run, `--go`, then rebuild the seed CSVs and seed the bo_customer list. Related: [[bo-netnew-package-sep2]], [[partner-pilot-haresh-frank-aug31]], [[feedback-warn-before-large-credit-spend]].
