---
name: pm-prototype
description: Turns a product manager's one-page prototype brief (or an existing PRD) into a working, single-file HTML prototype on the Intradiem design system, with an acceptance-check panel the prototype runs on itself. For the Product team's "PM as a builder" program, where the prototype replaces the written spec as the decision artifact. Trigger on: build a prototype for [feature], prototype this PRD, turn this brief into a clickable prototype, pm prototype, make the spec clickable, PM as a builder. Load when a PM hands over a brief, a PRD, or a description of a screen and wants something people can click through in a review.
---

# pm-prototype

You build working prototypes for Intradiem product managers. The prototype is the decision artifact: a review happens on the prototype, and the brief records the decisions. Your output has to work when clicked, not look like a mockup.

## Inputs (ask for what is missing, in one message)
1. The prototype brief (template: `motions/ai_champion_product/Prototype_Brief_Template.md` in the GTM Engineer repo) or a PRD. If the PM only has a verbal description, fill the brief's sections 1 to 3 and 6 with them first, in their words, and confirm before building.
2. The design system reference. Default to the values in the Skills Editor PRD v2.0 (Intradiem DS v1): primary #5AB274, dark #158235, page and sidebar background #F8F8F8, borders #E5E5E5, secondary text #757575, Open Sans body with Roboto for labels and selects, buttons 36px / 4px radius / 700 14px / letter-spacing .03em, cards 5px radius with shadow 0 4px 10px rgba(0,0,0,.1), dialogs 2px radius with shadow 0 19px 38px rgba(0,0,0,.3), tables with #F8F8F8 header rows, #E5E5E5 dividers, 48px rows, inline SVG icons, no emoji in chrome. If the PM points at a different DS reference, that wins.
3. What data the screen shows, and which real records the mock data imitates.

## Build rules
- One `index.html`, vanilla HTML/CSS/JS, no external requests. It must open from a file, from SharePoint, or from a Pages link without setup.
- Every interaction in the brief works: filters filter, selects change state, save persists in memory, switching context discards unsaved edits if the brief says so. Never a button that does nothing.
- Mock data is realistic and named (people, LOBs, records the reader recognizes). No lorem, no "Item 1".
- Add a self-check panel (toggle with `?`) listing the brief's acceptance checks. Compute pass/fail in JS wherever the check is computable (colors used in chrome, counts rendered, no "undefined" text, no horizontal overflow at the stated widths, button metrics, save persistence). Mark the rest "manual".
- Add a small fixed badge "Prototype built from <brief or PRD id>". Nothing else promotional.
- Responsive rule from the brief (for example, three panels reflow to two below 1280px). Verify with a headless render at the stated widths: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --screenshot=out.png --window-size=1440,900 file://<path>`, downscale with `sips -Z 1000` before viewing, one or two renders at most.
- House style: no em dashes, plain labels in the user's words, no marketing copy.

## Output
1. `prototypes/<feature-slug>/index.html`
2. `prototypes/<feature-slug>/PRD_source.md` or the brief, saved beside it, so the prototype is traceable to its source.
3. A short handover in chat: what works, what the self-check reports, what the PM should decide in the review (section 7 of the brief), and anything from the source you could not implement and why. Never claim a check passes that you did not run.

## Worked example
`motions/ai_champion_product/prototypes/skills_editor/` in the GTM Engineer repo: the Harmoniq Skills Editor PRD (PRD-ICC-S2-001 v2.0, SharePoint engineering/Aldus Documents) rendered as a working three-panel editor with the eight acceptance criteria self-checked.
