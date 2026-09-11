---
name: tam-seed-data-never-swapped-sep5
description: "RESOLVED 2026-09-11, see tam-universe-swapped-real-accounts-sep11. The TAM engine's account and trigger CSVs are still the Jul 1 2026 interview-build seed, never swapped for real data; caught Sep 5 2026 and guarded with a source column plus a SEED banner"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3fbe2bea-a6b2-440e-8a40-06dcd40494a7
  modified: 2026-09-05T20:14:02.202Z
---

Found 5 Sep 2026. `tam-outbound-engine/data/tam_accounts.csv` (6 rows) and `data/triggers.csv`
(12 rows) have not changed since commit a6839e6 on 1 Jul 2026, the interview-era build, five days
before Dallas started. They are demonstration inputs: round agent counts, templated trigger strings
with no citation, and two invented sellers ("Jordan Kim", "Alex Rivera"). The engine README said so
all along in a section called "The honest line", and documented a day-one swap that never happened,
because the real GTM work went into Clay Audiences, lemlist, the maps and the committee pages
instead. Nothing was fabricated deceptively; the scaffolding was simply never replaced.

How it surfaced: a Cowork strike-plan run for AmeriHealth Caritas web-checked the engine's trigger
and found the opposite was true. The Philadelphia Inquirer (26 May 2026) reported revenue grew 15%
to $28.1B *despite winning no new state contracts*, and Becker's (2 Jul 2024) reported 102
administrative roles cut on falling Medicaid enrolment. The engine's seed trigger said they had
won two new Medicaid state contracts and were hiring WFM analysts.

Guard added the same day, `is_seed()` in `account_engine.py`: both CSVs now carry a `source`
column, provenance is opt-in, and any row with an empty `source` prints `[SEED]` in the ranked list
and a full-width `!! SEED RECORD !!` banner on `--plan`. Mirrors `roi_model.json`'s `_verified:
false` default. 52/52 tests pass. All six rows are currently SEED. `intradiem-strike-sequence` (all
three copies) now refuses to put a seed row's fit score, tier, agent count, ROI or triggers into a
plan and sources the why-now live instead.

Consequence for the all-hands demo: Act 1 switched from AmeriHealth Caritas to **Centene** and drops
the fit score entirely. Centene is the skill's built-in reference example with a real tiered
committee, is already on screen in Act 2's committee ring, is a name the company knows, and is a
confirmed non-customer. AmeriHealth Caritas's only edge was the fit score, which does not exist, and
it has no sourced committee at all (the Sep 5 run reported the TAM engine returns personas not
people and there is no Clay export for it). Any named committee in the retired Sep 5 output was not
sourced from a roster and must not be recorded.

RESOLVED Sep 11 2026: the file was replaced with a 16-account sourced universe, seed rows survive only as tests/fixture_seed/ ([[tam-universe-swapped-real-accounts-sep11]]). Related:
[[allhands-demo-footage-review-sep5]], [[gtm-engineering-totals-aug27]].

## Shared platform read (Sep 5 2026)

`tech_stack_refresh.py` gained `--lookup <domain> [--json] [--force]`: a read-only PredictLeads
platform check that works for ANY domain, in the CSV or not, never writes, reuses a fresh cached
read for 0 credits and otherwise spends 1 Clay credit. It is now the single entry point the
`intradiem-strike-sequence` skill calls, so a strike plan and the Clay Audiences platform column
share one read, one vendor taxonomy (`config/tech_vendors.json`) and one freshness rule
(`verified_max_age_days` 365, stale reads may not name a vendor in copy). Before this, the script
hard-exited on any domain missing from `tam_accounts.csv`, so a skill could never get a read for a
net-new account. Also fixed: `FIELDS` in that script omitted the new `source` column, so a `--write`
would have stripped provenance off every row it touched.

## Centene made real, and the committee check (Sep 5 2026)

Centene added to `tam_accounts.csv` as the first non-seed row: 61,100 employees (SEC filings,
2025-12-31), 28.0M at-risk members (Q2 2025 10-Q); `agent_count` 10,000 is a labelled banded
ESTIMATE, no payer publishes it. Three sourced trigger rows added: cost_mandate 2026-08-17 (CFO
transition, Chris Neczypor from Lincoln Financial, joins Sep 2026, CFO 2027-01-01),
qbp_earnings_pressure 2026-07-28 (Q2 call named Stars cut-point/methodology headwinds plus MA
breakeven-by-2027), quality_identity_gap 2025-10-08 (CMS 2026 release). Centene now scores
**88/100 Tier 1** with a fresh trigger and outranks every seed row. Owner set to Nathan Belfield
(Slack handle @nathan.belfield is CONSTRUCTED, needs confirming).

Committee verification against `StarRatings_Centene_StrikeRoom_Sequence_FINAL.md` (Aug 26 roster),
web-checked Sep 5: Taliaferro and Hoseini and Hedrick confirmed in role (Hedrick is NEW in role,
brief is reducing administrative waste in back-office operations, the strongest angle in the set).
**Jesse Lewis title mismatch**: roster says Sr Director Medicare Operations, RocketReach says
Director Call Center Operations; he is the one seat cleared for contract-specific Wellcare
messaging and that clearance rested on his role. **Matthew Tran unresolved**: LinkedIn still shows
Centene, two searches surface a move to Aetna as Lead Director Aetna Technology Strategy and
Operations. Aetna is on the customer-exclusion list, so a move would make him a Gate B violation.
Hold Tran out until LinkedIn is checked directly. Third-party aggregators are corroboration, not
proof; LinkedIn/Sales Nav settles all five in two minutes.

Incidental find worth a trigger row once its posting date is confirmed: Centene has a live req for
**VP, Contact Center Platforms (Remote-FL)**.

Engine fixes the same day: future-dated triggers scored as maximally fresh (`recency_factor`
returned 1.0 for negative days while the tech read already guarded with `0 <=`); a test pinned
AmeriHealth to rank 1 and broke the moment real data beat seed data, replaced with a sort-contract
assertion; `tech_stack_refresh.py` now resolves the clay binary itself (Cowork and launchd do not
carry the plugin-cache PATH). 53/53 tests pass.

## The Cowork run hit a DIFFERENT engine (Sep 5 2026)

A Cowork run of "build the strike plan for Centene" returned fit 43 Tier 3, no agent count, no
triggers, `data_source: mock`, and copy reading "On ~0 agents that's about $0 a year" under a
subject line about a seven-figure number. The local engine had the same account at 88 Tier 1 with
three sourced triggers. Cause: Cowork took the `intradiem-tam` / `intradiem-gtm` MCP path, which
points at the hosted Render deployment `https://intradiem-gtm-system.onrender.com/mcp` running an
older build with its own stale data. `tam_mcp_server.py` in the repo reads the SAME local CSVs, so
only the remote deployment diverges. The MCP's `add_strike_account` also writes without reading
back (`trigger_added: true` then `triggers: []`), so a row added through it looks saved and is not.

Fixes: the skill now requires the local CLI and explicitly forbids the MCP for this, and says to
refuse the run rather than work around a bad source. `is_seed` now also returns True for a
non-positive `agent_count`, because every ROI figure is `agents * ...` and a zero rendered straight
into prospect copy. `get_data_source()` is now DERIVED from the rows (live / mixed / mock) instead
of read from a hand-maintained `config/meta.json` flag, which had been reporting `mock` for a fully
sourced account. Currently reports `mixed`: 1 real row (Centene), 5 seed. 53/53 tests pass.

Still open: the hosted Render deployment is stale and should be redeployed or retired, otherwise
anyone using the plugin/connector gets mock data with no warning.
