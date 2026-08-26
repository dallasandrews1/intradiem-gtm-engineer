# BOO Launch — War-Room Signal Additions (v0)

Most of the taxonomy already shipped with the back-office fork; this file records what the daily war room adds at launch and what is genuinely new.

## Already live (engine + config, scored under `active_motion = back_office`)

`bo_cost_mandate` (20/T1) · `sla_penalty_backlog` (20/T1) · `bo_hiring_cluster` (15/T2) · `bpo_transition` (15/T2) · `claims_backlog_news` (10/T2) · `transaction_volume_surge` (10/T2). The war room's morning sweep should treat a Tier-1 back-office fire on an owner-cleared account as a same-day play (signal-to-play skill), exactly like a Stars Priority-1.

## New at launch (add to the daily sweep checklist)

1. **Cost-per-transaction language in filings/earnings** — a named unit-cost metric in an operations context is the strongest coo_finance door-opener; log as `bo_cost_mandate` with the quote captured verbatim for the copy skills.
2. **BPO contract news involving OUR install base** — a Tier-1 account signing/exiting a BPO deal is both a `bpo_transition` fire and an AE/CSM heads-up; route both, same day.
3. **Regulator/DOI/CMS remediation orders** on claims processing at any Tier-1 parent — fires `sla_penalty_backlog`, and the account's AE owns the first move (owner etiquette before outreach).
4. **Back-office hiring clusters** at Tier-1 parents (≥3 relevant reqs, keyword-filtered count) — already wired; launch adds a weekly delta pass on the 56 Tier-1 parents.

## Routing

Every fired signal maps to a play: T1 fire on cleared account → sequence entry + Slack alert to the owner; T1 fire on UNCLEARED account → owner ping first (the signal is the reason to get clearance, not a bypass); T2 fire → priority bump only. Suppressed (`fo_risk_flag`) accounts never fire into outreach regardless of signal.
