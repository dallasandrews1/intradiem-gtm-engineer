---
name: intradiem-interactive-enablement
description: Converts a static sales enablement deck (PPTX in SharePoint, or its exported text) into one interactive HTML page on the Intradiem GTM Engineering page system, with present mode for calls, click-to-reveal discovery questions and objection talk tracks, and any ROI worked example rebuilt as a live calculator. Content is transcribed from the deck only; nothing is added or strengthened. Trigger on: convert this deck to a page, make the sales kit interactive, interactive enablement, deck to HTML, replace the PPT, sales enablement page for [product]. Load when a product enablement deck needs to become the page sellers use instead of slides.
---

# intradiem-interactive-enablement

You turn a Product enablement deck into the working page sellers open on a call. The page carries exactly what the deck says, in the deck's numbers, on the house page system, with the parts that were static in slides made usable: questions reveal their listen-fors, objections reveal their talk tracks, the ROI example recomputes, and Present mode runs the narrative full-screen.

## Source discipline (hard rule)
- Read the deck itself (SharePoint via the Microsoft 365 connector `sharepoint_search` then `read_resource`; a PPTX comes back as slide text). Never build from memory of a product.
- Transcribe, do not improve. Every figure, range, claim, customer note, price band and date on the page must exist in the deck. Where the deck is blank or says "to be confirmed" (beta dates "xx/xx/xxxx", ACV "confirm with Sales leadership"), the page says the same, plainly.
- When a worked example is rebuilt as a calculator, reproduce the deck's numbers with the deck's inputs first, then state any interpretation you had to make (for example how a "2%" line is defined) in a caution callout. If the arithmetic cannot reproduce the deck, say so on the page and do not silently pick a formula.
- Deck figures are internal enablement material. Customer-facing use of any number still goes through the Value Repository (`intradiem-verified-metrics`). Put that sentence on the page.
- Name the source on the page: deck title, owning team, date modified in SharePoint.

## Page system
Use the shared templates in `motions/ai_champion_product/_tpl/` (GTM Engineer repo): `base.css` (palette, hero, cards, statband, tables, steps, present mode, HUD), `fonts_head.html` (embedded Roboto and Roboto Mono, so the page works as an Artifact where Google Fonts is blocked), `logo_symbol.html`, `present.js`. Author a `<name>.src.html` with `<!--FONTS-->`, `<!--LOGO-->`, `<!--PRESENT-->` placeholders and run `python3 build_pages.py --check` in that folder. The check fails on em dashes and leftover placeholders.

Page shape (one page, sections numbered only because the deck's narrative is a sequence):
1. Hero: subject headline, one line, three or four counting numbers from the deck, meta (for whom, source, built by, use).
2. In one screen: the pitch in four bullets.
3. The pitch: steps, why we win as "X vs Y" rows, who buys, impact numbers in a statband.
4. Discovery: areas as cards, questions as tabbed lists with click-to-reveal listen-fors.
5. ROI: inputs left, outputs on a forest panel right, reset to the deck example, caution callout on interpretation.
6. Beta and commercial: cards plus a table.
7. Objections: accordion, verbatim talk tracks.
8. Targets, deployment impacts, prerequisites, out of scope, open dependencies.
9. Open with Product: currency of the deck, next decks in line, where the page lives.
10. Present mode: 8 to 10 slides that follow the deck's narrative, each with one idea.

## House style
No em dashes. No "look how impressive" copy, no explainer asides, every line earns its place. Plain labels in the seller's words. Internal pages carry "Internal. Confidential and proprietary." in the footer when the deck does.

## Verification before handover
- `python3 build_pages.py --check` passes.
- One headless render of the top of the page, downscaled (`sips -Z 900`), checked for overlap and font fallback; one render of Present mode (`#present-1` hash) if the slide layout changed.
- Click every tab, accordion and the calculator reset in the render or by reading the JS; the calculator's default output must equal the deck's total.
- Handover states what the deck left unconfirmed and what Product needs to check before sellers use the page.

## Worked example
`motions/ai_champion_product/BOO_Sales_Kit.src.html` from "Back Office Optimizer Early Stage Enablement.pptx" (Product, SharePoint productmanagement/GTM/Sales Enablement, Jun 2 2026).
