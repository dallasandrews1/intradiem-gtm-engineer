---
name: audiences-strike-universe-refresh-sep5
description: Sep 5 2026 dry run - the TAM strike universe can go from 7 hand-maintained rows to 1,560 real accounts at ZERO Clay credits; agent_count is the only blocker and needs a decision.
metadata:
  type: project
---

`tam-outbound-engine/data/tam_accounts.csv` had been 7 hand-maintained rows since the engine's
first commit, and the hosted brain served those 7 rows. Dry run Sep 5 2026 via
`tam-outbound-engine/refresh_from_audiences.py` (dry run by default; nothing promoted).

**Verified free.** A full 2,287-record company pull from Clay Audiences left the balance
unchanged at 62,657.5 on both sides. Audiences reads are the workspace's own synced data.
Fields available at no cost: domain, org_name, industry, employee_count, sfdc_owner_id,
Account Type, and the Sep 5 PredictLeads ACD/WFM read.

**Result: 1,560 candidate cold accounts.** Excluded 304 blank account type (unknown fails
closed), 234 under 1,000 employees, 98 Customer, 48 no domain, 41 Partner, 2 Churned.
765 of 1,560 (49%) already carry a tech read from the Sep 5 drain, so that half is paid for.

**The blocker, undecided on purpose.** `agent_count` has no free source, and `is_seed` treats a
non-positive agent count as unsourced, so all 1,560 rows land SEED and the brain withholds their
figures. Deriving it from employee count is free, but the seven existing rows imply ratios from
16.4% (Centene) to 42.9% (AmeriHealth), a 2.6x spread. ROI is `agents x $2,380`, so a uniform
band carries that 2.6x error into every dollar figure. Counting SF-known contacts in Audiences
gives buying-committee coverage, NOT agent population; do not conflate the two.

Industry mapping lives in `config/audiences_industry_map.json`. It surfaced a scoring gap:
`icp_weights.industry_points` scores only 5 labels, so Retail (235), Utilities (194) and
Telco/Cable (99) all land on "Other" at 8 points and can never reach Tier 1 on industry, even
though they are 3 of Intradiem's 6 verticals. Flagged, not decided.
Related: [[brain-snapshot-rewrite-sep5]], [[feedback-warn-before-large-credit-spend]].
