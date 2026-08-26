---
name: icp-committees-site
description: "The icp-committees.pages.dev buying-committee site Naveen uses for the QBR ICP slide, how it's built and how to redeploy it"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3a9e0889-cfac-42f3-88da-22ed3810bfe5
  modified: 2026-08-07T01:29:24.717Z
---

`~/Desktop/Intradiem Deliverables/deploy-icp-committees/` is a single-file Cloudflare Pages site (project `icp-committees`, account `37eeacfb7a4767c44ee8f40243b62c96`) that Naveen asked for on 6 Aug 2026 as material for the QBR "Who we sell to, sector by sector" slide. He called it "killer" and "perfectly executed", then asked for a third product the same night.

All content lives in one `const PAYLOAD={...}` JSON blob near the bottom of `index.html`. Adding a product means adding a key to `labels` and `data`; the product pills, industry tabs, node map and hover cards all render off it. Node radius comes from the influence weight, colour from the role string.

Three products as of 6 Aug 2026: Queue Optimizer (5 tabs), Back Office Optimizer (6 tabs), Engagement Hub (5 tabs). Engagement Hub's committee is Naveen's own spec, given verbatim in DM: IT gatekeeper, classic front-office WFM director buyer, HR champion, supervisor user, and "don't worry about the user" so the supervisor is on the map as an unnamed persona node at weight 30. Its buyer and gatekeeper seats reuse the QO people (same front office); only the HR champion seat was new Apollo sourcing.

Redeploy: `npx wrangler pages deploy . --project-name=icp-committees` from that folder. Same URL every time.

Related: [[naveen-facing-comms-rules]], [[deliverables-folder-convention]]
