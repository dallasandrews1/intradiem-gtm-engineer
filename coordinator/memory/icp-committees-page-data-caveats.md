---
name: icp-committees-page-data-caveats
description: "The ICP Buying Committees page has twin install-base and net-new lanes, 94 contacts, with the net-new lane gated against the Salesforce customer export"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6ca2e88b-0881-40b3-8ef1-9f091aa27912
  modified: 2026-08-06T21:23:37.845Z
---

The **ICP Buying Committees** page (https://icp-committees.pages.dev, source
`~/Desktop/Intradiem Deliverables/deploy-icp-committees`, built from
`Intradiem GTM Engineer/committee_hover_cards_Aug6.json`) runs **two structurally identical lanes**
toggled at the top: `nodes` = install base, `nn_nodes` = net new. Same sectors, same four roles,
same influence weights, 47 contacts each. Hovering a node opens a LinkedIn-style card with photo,
live headline, role, influence and profile link.

**Why two lanes:** the install-base-only version proved nothing about net-new capability. A skeptic
could say "of course you can map Humana, they're a customer." The net-new lane is the actual proof
that the GTM system maps a committee at an account never sold to.

**The install-base IB badges are correct, not a bug.** 20 of 21 companies appear in
`greenlight-pack/Active_Customers_SF_Jul10.csv`. The page was built on install-base accounts by
design (`meta.sources`: "Apollo pull against ICP evidence accounts").

Fixed 2026-08-06:
1. **Point32Health** is not a customer, so its node moved to net new.
2. **Four contacts had left their seat** and were replaced with the current holder, not flagged:
   Michele Cleary to Kristina Maxwell-Smith (RBC), Ken Solon to Greg Hafner (Prudential),
   Bridget Reidy to Mike Innocenzo (Exelon), Sylvie Duquette to Scott Thomson (Rogers).
   The on-card "retired" warning was removed because there is nothing left to warn about.

**The customer-exclusion gate matters and nearly failed.** Naive name matching let UnitedHealth
Group through as "net new" because the SF export says "UnitedHealth Group (UHG)". Strict
normalisation (strip parens, suffixes, compare first tokens) caught UHG, Humana, CVS Health,
Elevance, Molina and HCSC sitting inside `GTM_Engine_Accounts_TierAB_88_NetNew.csv`, plus Guardian
Life and Molina in sourcing results. **Always run that gate before adding a net-new account.**

Still open: **"US Bank / Elavon"** matches US Bancorp, but Elavon is a subsidiary, so that node
inherits install-base status from the parent. Dallas's call.

Unused but ready: **76 UK airline committee contacts** (`motions/uk_airlines/`), the cleanest-classified
seat data in the repo. Deliberately not added, since aviation is not one of the six verticals and a
seventh tab on one lane only would undercut the framing.

Related: [[clay-enrich-person-has-no-photos]], [[pages-new-project-522-window]].
