---
name: engine-room-deliverable-aug7
description: "The Clay engine-room site for Naveen (gtm-engine-room.pages.dev) - shows the machine, leads with defects caught not features; companion to the ICP committees site"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a6fa178f-5397-4e80-bd71-df855f3566a2
  modified: 2026-08-07T19:00:50.153Z
---

Built 2026-08-07, revised and redeployed the same day. **Live: https://gtm-engine-room.pages.dev** (Cloudflare Pages project `gtm-engine-room`, account 37eeacfb7a4767c44ee8f40243b62c96).

**Canonical artifact: the live Pages URL.** The Desktop standalone is the editable source and is only true after a sync into `deploy-engine-room/index.html` plus a redeploy. Two sessions once held the same Desktop file open and the later whole-file write silently reverted the earlier session's in-place edits; a passing Edit and a clean JS syntax check are NOT proof a change survived, only a headless render assert against the file on disk is.

**Revision 2 (13:57, after Dallas said the first build "portrays us weak and sloppy").** Structure changed, not substance: magnitude moved ahead of defects, section 02 retitled to the interception outcome ("Twelve defects surfaced. Ten closed. None reached a prospect"), a caught defect leads instead of the leak, "STOP THE LINE" dropped for `OPEN · CONTAINED · CLOSES 11 AUG` with the containment fact moved to the first sentence, and a new section 10 "Close dates" gives every open item an owner and a date. The closing "Where this is genuinely thin" note was cut as the final beat and its substance moved into section 08. See [[deliverable-strength-framing]] for the rule this produced.

- Source: `~/Desktop/Intradiem Deliverables/deploy-engine-room/` (index.html, 404.html, _headers)
- Standalone copy: `~/Desktop/Intradiem Deliverables/Clay Engine Room - Aug 7.html`
- Redeploy: `CLOUDFLARE_ACCOUNT_ID=37eeacfb7a4767c44ee8f40243b62c96 npx wrangler pages deploy . --project-name=gtm-engine-room --commit-dirty=true`

Same build pattern as the ICP committees site: single self-contained HTML, all content in one `const PAYLOAD={...}`, rendered by a small block-renderer (`stat`, `cards`, `filter`, `table`, `note`, `steps`, `prose`). **Zero external assets and zero images** (the Intradiem logo is the official inline `<symbol id="ilogo">` copied verbatim from `dwo-html-deck/`), so there is no image-inlining step and no broken-asset trap. Current brand kit: forest #014637, green-300 #7BD3A0 accents, orange #F58220 as the action accent.

**The editorial choice worth keeping.** Dallas's brief proposed sections for motions, strike rooms, enrichment and campaign strategy. That is a feature list. The structure that shipped leads with **section 02, "what the engine caught"** - nine real defects with what surfaced each, two marked still open - because every one of them is the class of failure that sends cleanly and is therefore invisible to bounce rates, opens and replies. The features become legible as the things that catch those. Cut entirely: campaign strategy as its own section (it lives inside the motions and the copy doctrine), and any Clay explainer.

Honesty rules held throughout: surfaced and realized never blended, the demo-era surfaced figure excluded by name ([[impact-json-is-demo-data]]), the open gate leak stated as open ([[wfm-adjacency-customer-leak-open]]), zero em dashes, head-start framing.

**Verification that mattered:** a JS syntax check passes on a file that renders blank, so every output was rendered headlessly with `Google Chrome --headless --dump-dom` and asserted on real DOM counts (9 sections, 15 cards, 4 tables, header populated) before shipping. Pages propagation checked in batches of 12 until zero mismatches (took 3 rounds), then the downloaded page diffed byte-for-byte against local.
