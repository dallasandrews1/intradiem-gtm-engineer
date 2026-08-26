---
name: wfm-messagegen-canonical
description: "Canonical location for the WFM-Adjacency Wave 1 MessageGen persona variants file, and the stale-close bug found and fixed on 2026-07-17."
metadata: 
  node_type: memory
  type: project
  originSessionId: bc54fe22-1c3e-4602-b3dc-6518811893f7
---

Canonical file: `~/Claude/Projects/Intradiem GTM Engineer/WFM_Adjacency_QuickWin_MessageGen_Variants_2.md` (Variant A = Operational Champion, Variant B = Economic Buyer, Wave 1 quick-win cold email 1).

**Why:** A Cowork session claimed to have de-rhymed Variant A's and B's CTA closes so a champion and economic buyer at the same account wouldn't see matching messages. The fix landed in the body template and the summary table but not in Variant B's "Rendered example" block, which still showed Variant A's exact connector/CTA ("Might be worth walking through..." / "Worth 15 minutes..."). The file also existed as four stray, non-canonical copies (`~/Downloads` no-suffix, `_1`, `_2`, and `~/Claude/Projects/Clay Builds and Strategy/`) rather than in the main working repo — see [[surface-split-rule]].

**How to apply:** Before generating a Clay MessageGen batch or Wave 1 send from this file, pull from the canonical repo path above, not from Downloads. All four stray copies now carry a `SUPERSEDED` redirect notice pointing here; treat any edit to them as not-yet-real until ported to the canonical file. Sender is still an open input (`{{sender_first_name}}`, default Nathan Belfield) — confirm before send per the file's own deployment notes.
