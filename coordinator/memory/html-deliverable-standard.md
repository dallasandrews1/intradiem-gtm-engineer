---
name: html-deliverable-standard
description: The bar for seller/leadership HTML pages is the Naveen operating-plan design system; flat pages get rejected
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 57bf8bee-44ae-4199-a724-bf8f3354a483
  modified: 2026-08-18T15:14:33.256Z
---

Aug 18 2026: Dallas rejected the first VodafoneThree Entry Layer page as "not up to the same standards as the html we created and sent to Naveen."

**Why:** These pages represent the GTM Engineering function to sellers and leadership. The established system reads as one product family with the DWO deck and the Interactive Demo; a flatter page reads as lower effort even when the content is identical.

**How to apply:** Build every seller/leadership page on the system in `GTM_Outbound_Motion_Operating_Plan_v1.html` (the Jul 31 Naveen page). Components: forest #014637 hero with the inline Intradiem logo `<symbol id="ilogo">`, radial green glow (`radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)`), 900-weight headline with a green-300 `.spark` word, mono meta grid (Prepared for / By / Date / Companion); white 1120px `.sheet` on #F5F4F2; `.tldr` panel first; `.tag` pills; forest `.statband` for numbers; `.phase` numbered squares for sequences; `.callout` (orange, caution) and `.gate` (green, verified) boxes; zebra tables with mono green TH; mono uppercase `.foot`; print styles. For Artifact publishes, embed Roboto (wght 100-900 variable) and Roboto Mono as woff2 data URIs from fonts.gstatic.com latin subsets (~94KB total); the Google Fonts `<link>` is CSP-blocked in artifacts and silently falls back. Reusable template: `motions/jack/named_accounts/vodafonethree_ops_layer/VodafoneThree_EntryLayer_Brief.html`.

Related: [[feedback-deliverables-carry-the-why]], [[jack-vodafonethree-ops-layer]]

**Addendum (Aug 27):** pages built around wide org trees (the back-office maps site) run full width: `.sheet{max-width:none}`, `.wrap{max-width:none;padding:0 40px}`, white body, cards 172px. Dallas: "make it the entire width of the page so everything isn't boxed in and making us scroll left and right." The 1120px sheet stays the default for text pages.
