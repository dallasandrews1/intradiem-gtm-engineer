---
name: jack-vodafonethree-ops-layer
description: "Jack O'Hagan's VodafoneThree ops-layer build (Aug 17 2026) - spec, scope rules, avoid list, deliverable location"
metadata: 
  node_type: memory
  type: project
  originSessionId: 57bf8bee-44ae-4199-a724-bf8f3354a483
  modified: 2026-08-20T12:20:49.229Z
---

Aug 17 2026, Slack DM: Jack O'Hagan (UK Senior AE) asked for a Clay-built contact table for VodafoneThree, his number 1 account. Senior contacts are held but unresponsive; the play is to reach the operational layer BENEATH them for intelligence and referrals, then re-approach seniors non-cold.

**Scope rules (Jack's own spec):**
- In: VodafoneThree consumer, Three consumer, Vodafone Business (tag separately, ~900 agents). Ignore legacy "Vodafone" consumer entity as a target label.
- Out: VOXI, SMARTY, Talkmobile (self-serve, no planning function).
- Buckets: Planning and WFM / Contact Centre Operations / Frontline Management / Analytics and CI. Classification by written definition, never fixed title match.
- Do NOT capture senior directors/heads (already held). AVOID entirely: Jon Shaw (Consumer Director), Ryan Rubertazzi (Head of Consumer Assisted Sales and Service).
- Tag legacy estate (Three side absorbing into Vodafone side's operating model matters for messaging). Divisions: Care, Specialist care, Sales, Retention, Channel operations.
- Integration phase (duplication assessment, office consolidation) is context explaining resistance, NOT a buying signal.
- ~7k agents total. Genesys Cloud estate. Jack runs Lusha for contact details himself; he does not need email/phone enrichment from Clay.
- Jack cares about hit rate because it strengthens dedicated-UK-Clay-credits over a Lusha license.

**Build (Aug 17):** 556 raw search results, 339 after dedupe vs the held roster (Bonnar/Bourke dropped as already held), 106 classified keepers + 5 bonus CC-tooling/transformation contacts, 91 LinkedIn URLs resolved, 0.0 credits spent (see [[clay-free-sourcing-path]]). 6 stale-index leavers caught, incl. Neil McCormack now WFM Strategy Manager at Webhelp (possible BPO angle if Webhelp runs VodafoneThree work). Deliverable: motions/jack/named_accounts/vodafonethree_ops_layer/ in the main repo.

**Aug 17-18 follow-on, credit-backed (Dallas greenlit):** despite Jack normally running Lusha himself, Dallas ran a deliberate Clay-vs-Lusha hit-rate benchmark on this account — the exact case the "dedicated-UK-Clay-credits over a Lusha license" argument above needs receipts for. Verify pass (96 rows, 48.0 credits) caught 2 leavers (Gareth James -> MBNL, Sam Bantu -> independent) and resolved 8/10 identity conflicts before the expensive step. Contact waterfall (85 verified-current rows, Enrich Person + Find Contact Details, 1,038.8 credits) returned 57 work emails (67%) and 77 mobiles (90%); net clean email rate ~62% after flagging 4 SUSPECT_DOMAIN hits. Total pass ≈1,137.9 credits — the single largest motion burn in the whole ledger's history, more than every other tracked motion's multi-week total combined (per credit-check-2026-08-20.md). Not yet assigned a formal motion-budget line in the canonical ledger's header.
