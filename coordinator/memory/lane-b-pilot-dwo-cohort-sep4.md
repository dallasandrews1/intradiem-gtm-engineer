---
name: lane-b-pilot-dwo-cohort-sep4
description: Sep 4 2026, Lane B pilot rides on DWO wave 1 as cohort GTMENG-DWO1-2026-09 (test 337 people/144 accounts ads+sequence, holdout 363/141), same sha1-by-domain split as cohort_cutter; the heat-list cohort cutter itself is WAITING on an empty pool
metadata:
  type: project
---
Lane B (lemlist + LinkedIn Matched Audience on one clock with a holdout) is piloted on the DWO wave 1 load instead of the heat list: `automation/cohort_cutter.py --dry-run --force` on Sep 4 returned WAITING (cohort pool segment 0 companies, scorer dry). The DWO loader stamps `cohortId=GTMENG-DWO1-2026-09` and `cohortArm` (sha1(domain) parity, holdout_share 0.5, identical rule to the cutter) on every lead; ads CSV (test arm, LinkedIn list-upload columns) at motions/dwo_executives/GTMENG-DWO1-2026-09_ads_linkedin.csv; Salesforce campaign name `GTM Eng - DWO Executives - Wave 1`.

**Why:** Melissa asked on record for ads on the same list as the sequence and the council row needs its own cost-per-meeting number; a real 700-person wave gives the 300-matchable floor the heat list cannot yet.

**How to apply:** ads live T-3 business days before Email 1, off day 25; the ads CSV goes to Melissa/Sierra only once the launch date is set. Report test and holdout side by side on the council row. See [[dwo-shell-load-plan-sep4]].
