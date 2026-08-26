---
name: uk-current-customers-aug3
description: UK current-customer list arrived Aug 3 2026; 7 accounts; AXA (UK) excluded from UK FS motion; DNC scope confirmation with Jack still open
metadata: 
  node_type: memory
  type: project
  originSessionId: 3266a9ed-3e5c-4186-843d-97753e59046e
  modified: 2026-08-03T12:57:52.541Z
---

The UK current-customer list arrived Aug 3 2026 and is saved at `~/Claude/Projects/Intradiem GTM Engineer/motions/UK_Current_Customers_Aug3.csv`. Seven accounts: American Express GBT, AXA (UK), British Gas, Capita, CENTRICA PLC, Virgin Media O2 (UK), VitalityHealth. CSM for six of seven is Scott McHaffie; owner mostly Matt Rumins.

Applied to the UK motions the same day:

- AXA (UK) is a current customer (since 2018-07-02, Genesys Cloud, ~5,000 agents). Removed from the UK FS target list; its 8 committee contacts in `UK_FS_Committee_Contacts_v1.csv` are marked `EXCLUDED - current customer`. AXA row in the graded universe top-15 annotated.
- The "two largest UK insurers" Jack cited as customers are AXA (UK) and VitalityHealth ([[jack-uk-motion-strategy-call]]). Same day, the UK facts were saved into the Value Repository as BLINDED entries: section "UK install base — blinded facts (Salesforce export, Aug 3 2026)" in `04-value-repository/Intradiem_Value_Repository.md`, tier 1:1 blinded only, existence/tenure/stack facts with no outcomes attached. Also added as a quick-reference line in all four `intradiem-verified-metrics` SKILL.md copies and as a DO-NOT-SEND row blocking named UK customer use. Jack's "two of the LARGEST UK insurers" superlative stays [UNVERIFIED]; copy says "well-known" or "major". Naming any UK customer still requires reference approval recorded in the repo section.
- Aviva, Admiral, Direct Line are NOT customers and stay in the FS universe as targets.
- Amex GBT corroborates the earlier American Express Services Europe exclusion (Matt Graves, Jul 21 call).
- No customer names matched the UK Airlines universe or committee CSV.

Still open before any UK load: (1) confirm with Jack that the DNC scope is customers only (no open opps or partner accounts to add); (2) the exclusion check re-runs on real rows at load time including legal-name variants and subsidiaries, per the gate-integrity discipline. This CSV lives file-side; when the UK workbook gets a customer_exclude column, match on patterns (axa, amex/american express, british gas, centrica, capita, virgin media/o2, vitality), not exact names.
