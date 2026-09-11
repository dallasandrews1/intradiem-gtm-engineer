# Channel landscape (Frank's Sep 2 2026 ask)

Frank's DM, Sep 2 2026 09:58 CT: "map out all of the channel partners bringing Five9, Cisco, Avaya, Genesys, Alvaria, Verint, and Amazon Connect to market in EMEA. Need a detailed breakdown of who they resell and market share if possible."

## What runs

| Step | What | Where |
|---|---|---|
| 1a | Vendor directories read in full with headless Chrome / the directories' own data endpoints: Five9 locator (puppeteer, 190 pages), Genesys Partner Finder (Zift locator API, 595 records), Verint directory (FacetWP refresh endpoint, EMEA + Channel), Aspect directory (Webflow pagination), AWS Partner Finder (puppeteer, Amazon Connect product filter). Scripts live in the scratchpad pattern described below; outputs are the `*_directory.md` files in the same PARTNERS schema. | `research/emea/<slug>_directory.md`, `research/emea/five9_locator.json`, `research/emea/genesys_finder.json` |
| 1b | Research fan-out: one signal-researcher pass per platform (strongest model) plus one pass for published share data and multi-vendor distributors. Each returns a Vendor context paragraph, a PARTNERS JSON array, a SHARE JSON object and a Gaps list. | `research/emea/<slug>.md`, `research/emea/share_multi.md` |
| 2 | Hand-written page copy and normalisation rules: vendor cards, in-one-screen, where-to-start, confidence, gaps, name aliases, drop lists. | `data/emea_meta.json` |
| 3 | `merge_landscape.py emea` normalises partner names across passes (aliases + suffix stripping), merges per-platform links, applies `drop` and `drop_links`, and writes the page data. | `data/emea.json` |
| 4 | `build_landscape.py emea` writes the page and the CSV on the brief template family, and refreshes the skill template so Frank's copy never drifts. | `EMEA_Channel_Partner_Map.html`, `EMEA_Channel_Partners.csv`, `../frank_selfserve/skills/partner-channel-landscape/landscape_template.html` |

Rebuild after any research or copy change:

```
python3 merge_landscape.py emea && python3 build_landscape.py emea
```

## Rules baked in

- A partner row exists only when at least one platform link survives. Platform vendors themselves (Avaya as Verint's OEM route, Five9 hosting Verint, Cisco via Calabrio, 8x8, Odigo, Salesforce) are described in the vendor context, never listed as channel partners.
- Every LOW link is removed after the merge, so every tile on the page is either confirmed in the vendor's own directory or on the partner's page (HIGH) or single-sourced (MEDIUM). A directory hit on a research row lifts it to HIGH and adds the directory as a source.
- ISVs and platform vendors that appear in a directory (Genesys lists PolyAI and Sycurio; Verint lists Cisco and Zoom) are dropped through `drop`; multi-country entities are collapsed to one row inside the directory builders.
- Market share is shown only as published, with the region on every row. Partner-level share is never computed; where a partner or vendor claims "largest" or "#1", the quote and its source are shown.
- No Intradiem figures on the page. No 3xG data anywhere in this folder, so the page is safe to deploy.

## Deploy

Public copy lives at https://gtm-partner-pilot.pages.dev/emea-partners/ (folder `emea-partners/index.html` in `~/Desktop/Intradiem Deliverables/deploy-partner-pilot/`, same wrangler command as the pilot page).

## Extending

- Another region: add `research/<region>/` passes, write `data/<region>_meta.json`, run both scripts with the region argument.
- Frank can run the same shape himself in the shared project with the `partner-channel-landscape` skill; this engine copy is for the deployed, versioned page.
- Directory pull recipes (all worked Sep 2 2026): Five9 locator is Salesforce Lightning Out in shadow DOM, drive it with puppeteer-core and pierce shadow roots, click Next 190 times; Genesys uses Zift (`rest.ziftmarcom.com/locator/partners?size=100&page=N` with header `X-ZIFT-PARTNER-LOCATOR: 8a99836c82cdb3970182d1169fef4b2c`, the locatorId from `dynamic.ziftsolutions.com/.../Partner_Locator/.../0`); Verint is FacetWP (`POST /wp-json/facetwp/v1/refresh` with `partner_regions: ["emea"]`, `partner_type: ["channel-partner"]`, paged 1..n); Aspect is Webflow (`?7f3d30a2_page=N`, curl); AWS Partner Finder needs a headed puppeteer session, the Amazon Connect product facets in the URL, and the `li[data-testid="pagination-right-arrow"] button` control.
- Cisco has no filterable public directory; Avaya's locator was offline on Sep 2 2026. Re-check both on the next refresh.
