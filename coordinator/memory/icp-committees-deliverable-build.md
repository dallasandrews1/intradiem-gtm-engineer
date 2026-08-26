---
name: icp-committees-deliverable-build
description: "How the ICP Buying Committees deliverables are built, and the retail_variant trap that hides nodes from any key-name traversal"
metadata: 
  node_type: memory
  type: project
  originSessionId: 70497397-25f3-4c4f-af31-d8a2961a3267
  modified: 2026-08-07T04:14:45.277Z
---

The ICP Buying Committees site lives at `~/Desktop/Intradiem Deliverables/deploy-icp-committees/` and deploys to https://icp-committees.pages.dev (Cloudflare Pages project `icp-committees`, account 37eeacfb7a4767c44ee8f40243b62c96). All content is one `const PAYLOAD={...}` JSON blob on a single line near the bottom of index.html.

**The trap that cost the most on 6 Aug 2026: `retail_variant`.** Under `qo/bpo_shared_services` there is a nested `retail_variant` object with its own `nodes` and `nn_nodes` (6 people: Home Depot, Lowe's, Best Buy). Any traversal written as "for k of ['nodes','nn_nodes','bench']" silently skips them. That bug caused an orphan-image sweep to delete 4 images that were genuinely in use, shipping broken images live, and made the first standalone builds inline 139 of 144 photos. **Always walk the payload recursively** (treat any object with both `name` and `linkedin` as a person, and any string value starting `img/` as an image reference) rather than iterating a fixed key list. Recursive counts are 210 person entries, 166 unique by LinkedIn URL.

Builders live in the session scratchpad pattern, not in the repo: one script inlines every image as a base64 data URI and writes the full page plus one file per product, another wraps the whole thing in a Shadow DOM for the paste-anywhere embed block. Two things the per-product build must do or the file renders blank: filter both `labels` and `data` to the single product, **and rewrite the boot line** `let prod='qo', sec=S.labels.qo.order[0],` to that product, because the app hardcodes `qo` at startup. Hide the switcher with `#prodrow{display:none}`.

Keep profile images downscaled to 256px. Reverse Contact returns up to 750x750, which took the folder to 7.6 MB and would have made a standalone file ~10 MB; at 256px it is 2 MB and the full standalone is 3.2 MB.

Always render each generated file headlessly and assert the DOM actually populated (tabs, `data-n` nodes, a card) before calling it done. A syntax check passes on a file that renders completely blank. See [[cloudflare-pages-edge-propagation]] for verifying the deploy and [[photo-enrichment-reverse-contact-via-clay]] for refilling photos.
