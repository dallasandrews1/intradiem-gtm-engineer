---
name: partner-channel-landscape
description: Map the channel partners that bring a set of contact-center or WFM platforms to market in a region, with what each partner resells and whatever market-share data is actually published. Trigger on "map the channel partners for [vendors] in [region]", "who resells [vendor] in [region]", "channel landscape", "partner landscape", "partner map for EMEA / APAC / LATAM", "which partners carry Genesys and Verint", or when the partner team needs to pick which partners to recruit or prioritise. Produces one branded HTML page with an interactive partner list (filter by platform, type, multi-platform), a published-share table, per-platform context, and a where-to-start list.
---

# Partner channel landscape

You map who brings a set of platforms to market in a region: distributors, resellers, systems integrators, managed service providers, carriers, BPO/CX outsourcers, consultancies. The reader is Intradiem's partner channel team deciding which partners to recruit, prioritise, or work through. Intradiem sits between the ACD (Genesys, Five9, Avaya, Cisco, Amazon Connect) and WFM (Verint, NICE, Calabrio, Aspect); it is never a WFM replacement. That is why the map's most valuable rows are partners that carry BOTH an ACD and a WFM platform.

## Inputs
- The platforms (default set if none given: Five9, Cisco contact center, Avaya, Genesys, Alvaria/Aspect, Verint, Amazon Connect).
- The region (EMEA, a country, APAC, LATAM, North America). Ask once if missing; otherwise start.

## Research rules (non-negotiable)
- Vendor directories first, search second. Every platform has an official partner directory and it is the authoritative list: Genesys Partner Finder (genesys.com/partners/partner-finder, Region and Tier fields), Five9 Global Partner Locator (five9.com/partner-locator, region, tier and type per tile), Verint partner directory (verint.com/partners with the Regions filter), Aspect partner directory (aspect.com/company/partners, all pages), AWS Partner Finder (partners.amazonaws.com with the Amazon Connect product filter), Cisco Partner Locator, Avaya partner locator. Read the directory for the region in full before any web search, and cite the directory as the source on every row it produced.
- Then one research pass PER PLATFORM for awards, partner pages and press, then one pass for published share data and multi-vendor distributors. Do not try to cover seven platforms in one search.
- Every partner row carries at least one real source URL and a date. Prefer 2024 to now. Sources that count: vendor partner locators and press releases, partner-of-the-year awards, partner websites, case studies, LinkedIn company pages, analyst reports, filings.
- Grade every partner-to-platform link LOW, MEDIUM or HIGH. A single old press release or a job posting is LOW and says "inferred". Never invent a tier or designation; use the vendor's own words or "listed partner".
- Market share: report only PUBLISHED figures (Gartner, IDC, Frost & Sullivan, Omdia, Cavell, DMG, Metrigy, vendor filings), each with region, value, how it was measured (revenue, seats, installed base) and source. If only a global figure exists, label it GLOBAL. Never estimate a regional share from a global one. Partner-level revenue share by vendor is almost never public; when a partner is the named "largest" or "primary" for a vendor in a country, quote that statement with its source rather than inventing a percentage.
- Do not pad, and do not list a platform vendor as a channel partner of another platform (Avaya reselling Aspect, Five9 hosting Verint, Cisco via Calabrio belong in the platform card, not the map).
- Collapse multi-country entities into one row (NTT DATA Spain, NTT DATA UK and NTT Ireland are one partner with a country list and the best tier).
- Referral agents are their own type so the reader can filter them out.
- Corporate changes matter (splits, take-privates, acquisitions, distributor changes). Say what the platform's current structure is before listing its partners.
- No Intradiem numbers anywhere on the page beyond the approved lines in the project instructions. No em dashes.

## The page, in this order (each block uses the template patterns below)
1. **In one screen**: three or four bullets. Lead with the multi-platform partners (the leverage point), then the honest state of share data, then where to start.
2. **Market share, what is actually published**: the share table, then a short callout on what is NOT published.
3. **The platforms in [region]**: one card per platform: two or three sentences of regional context, the partner program structure, the published share line (or "no public figure").
4. **The map**: every partner as a record, sorted by number of platforms carried, then name. Each record: name, type, HQ country, coverage, one platform tile per platform carried (relationship, one-sentence evidence, sources, confidence), scale signal, share statement, other platforms it also carries outside the set.
5. **Where to start**: three to five numbered moves for the partner team, grounded in the map (which multi-platform partners, which distributors, which country gaps).
6. **How this map was built**: a table with one row per platform: what was read in full (the directory and its filter), what was added (awards, partner pages, filings), and the count of partners on the map. Below it, one bullet per platform whose directory could not be read and what was used instead. State facts, never apologise.

## Output format: a branded HTML page
Deliver one complete file named `<Region>_Channel_Partner_Map.html`, built on `landscape_template.html` shipped with this skill. `example_emea.html` is the approved worked example; study it before writing. Rules:
- Copy the template verbatim, fill `{{TITLE}}` (e.g. "EMEA channel partner map"), `{{ANGLE}}` (lowercase phrase, the point of the map), `{{SUBHEAD}}` (two sentences: what was mapped, how to read it), `{{DATE}}`, `{{BODY}}`. Never edit the CSS, the filter script, the band, or the footer.
- Block patterns for `{{BODY}}` (copy the markup shapes from the example exactly, the filter script depends on the data attributes):
  - Share table: `<div class="tw"><table class="share">` with columns Vendor, Metric, Region, Value, Measured as, Source.
  - Platform cards: `<div class="vgrid">` of `<div class="vc">` with `.vh` (name + `.cnt` partner count), a context `<p>`, and `<p class="prog"><span>Program</span>...</p>` / `<span>Share</span>` lines.
  - Filters: copy the `.filters` block from the example and keep one `.chip` per platform with `data-f="v" data-v="<slug>"`, one per partner type present with `data-f="t"`, and the two `data-f="m"` chips. Keep the `#q` input and `#count` div.
  - Partner records: `<div class="rec" data-h="<lowercase search text>" data-v="<space-separated platform slugs>" data-t="<type slug>" data-m="<platform count>">` containing `.rh` (name bold, `.pill.ty` type, `.pill.hq` country, `.pill.mv` "N platforms" when 2+), `.rm` coverage line, `.vrow` of `.vt.c-high|c-medium|c-low` tiles each with `.vn` platform name, `.rel` relationship, `.ev` evidence, `.sr` sources and confidence, then `.rn` lines with a `<span>` label (Scale, Share signal, Also carries).
  - Platform slugs: five9, cisco, avaya, genesys, alvaria, verint, connect (add new slugs for other platforms, lowercase, one word).
  - Type slugs: distributor, reseller, systems_integrator, msp, carrier, bpo_cx_outsourcer, consultancy, referral.
  - Where to start: `<div class="start">` of `<div class="st"><span class="n">1</span><div><b>title</b><p>body</p></div></div>`.
  - Method table: `<table class="meth">` with columns Platform, Read in full, Plus, EMEA partners on the map, then a plain `<ul>` of notes.
- The page IS the deliverable. Offer a CSV of the partner rows only if asked (partner, HQ, type, coverage, platforms carried, relationship per platform, confidence per platform, sources).

## Voice
Plain language, short lines, contractions. The reader is choosing partners, so every record answers "why would this partner matter to us". No em dashes anywhere.
