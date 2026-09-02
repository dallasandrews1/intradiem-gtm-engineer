# Channel landscape (Frank's Sep 2 2026 ask)

Frank's DM, Sep 2 2026 09:58 CT: "map out all of the channel partners bringing Five9, Cisco, Avaya, Genesys, Alvaria, Verint, and Amazon Connect to market in EMEA. Need a detailed breakdown of who they resell and market share if possible."

## What runs

| Step | What | Where |
|---|---|---|
| 1 | Research fan-out: one signal-researcher pass per platform (strongest model) plus one pass for published share data and multi-vendor distributors. Each returns a Vendor context paragraph, a PARTNERS JSON array, a SHARE JSON object and a Gaps list. | `research/emea/<slug>.md`, `research/emea/share_multi.md` |
| 2 | Hand-written page copy and normalisation rules: vendor cards, in-one-screen, where-to-start, confidence, gaps, name aliases, drop lists. | `data/emea_meta.json` |
| 3 | `merge_landscape.py emea` normalises partner names across passes (aliases + suffix stripping), merges per-platform links, applies `drop` and `drop_links`, and writes the page data. | `data/emea.json` |
| 4 | `build_landscape.py emea` writes the page and the CSV on the brief template family, and refreshes the skill template so Frank's copy never drifts. | `EMEA_Channel_Partner_Map.html`, `EMEA_Channel_Partners.csv`, `../frank_selfserve/skills/partner-channel-landscape/landscape_template.html` |

Rebuild after any research or copy change:

```
python3 merge_landscape.py emea && python3 build_landscape.py emea
```

## Rules baked in

- A partner row exists only when at least one platform link survives. Platform vendors themselves (Avaya as Verint's OEM route, Five9 hosting Verint, Cisco via Calabrio, 8x8, Odigo, Salesforce) are described in the vendor context, never listed as channel partners.
- LOW links that the researcher flagged as "no contact center sale or delivery evidence" are removed through `drop_links` (Atea, Bechtle, Computacenter, Swisscom on Cisco; Westcon and TD SYNNEX on Five9 and Connect; Vodafone on Avaya). Award-sourced LOW links stay, marked orange.
- Market share is shown only as published, with the region on every row. Partner-level share is never computed; where a partner or vendor claims "largest" or "#1", the quote and its source are shown.
- No Intradiem figures on the page. No 3xG data anywhere in this folder, so the page is safe to deploy.

## Deploy

Public copy lives at https://gtm-partner-pilot.pages.dev/emea-partners/ (folder `emea-partners/index.html` in `~/Desktop/Intradiem Deliverables/deploy-partner-pilot/`, same wrangler command as the pilot page).

## Extending

- Another region: add `research/<region>/` passes, write `data/<region>_meta.json`, run both scripts with the region argument.
- Frank can run the same shape himself in the shared project with the `partner-channel-landscape` skill; this engine copy is for the deployed, versioned page.
- Fastest wins on coverage: a browser pass over the Aspect partner directory (pages 2 to 4), the Verint directory with the EMEA filter, and the Five9 and AWS partner finders filtered to EMEA.
