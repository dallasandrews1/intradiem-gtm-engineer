---
name: html-exec-standard
description: The polish bar and template for all exec/customer-facing HTML decks and deliverables
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7d5853bb-4ded-4829-8888-bccc2997f338
  modified: 2026-07-31T13:40:04.682Z
---

Every HTML deck, one-pager, or visual deliverable Dallas ships must hit the **Norton briefing standard**, not just the brand palette. Palette-only branding was rejected Jul 29 2026 as not exec-ready.

**Reference template (copy its system):** `norton-briefing/Norton_Engine_Briefing.html`. It has: the real **Intradiem logo** (inline SVG, 4-color diamond mark + wordmark; also at `strike-room-kit/logo.svg`), a slide engine (full-screen `.slide` absolute/inset, `.active` toggle, arrow-key + click nav, progress bar, HUD counter, brand watermark bottom-left, `on-dark`/`on-title` body classes), and polish patterns: card box-shadows `0 12px 34px rgba(20,40,25,.07)`, stat bands (forest bg, lime accents), flow diagrams with arrows, ledger tables, dark closer slides, Playfair Display headings + DM Sans body + JetBrains Mono eyebrows, `clamp()` responsive type.

**Logo must appear** on the title and as a per-slide watermark. Define it once as an SVG `<symbol id="ilogo">` and `<use>` it. "No logo anywhere" was the specific failure that triggered this rule.

**PDF export:** Chrome headless landscape, `@media print` forcing each `.slide` to `position:relative;height:7.5in;page-break-after:always;overflow:hidden` (10 slides -> 10 pages). Command: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=out.pdf "file://..."`. NOTE: the `file` shell command misreports Chrome PDF page counts; verify via the page-tree `/Count`, not `file`.

**Aspirational bar Dallas named:** the interactive demo at intradiem-interactive-demo.azurewebsites.net (separate product demos, booth-view mode, talking points). RESOLVED Jul 29 2026 — Dallas exported it: `~/Downloads/Intradiem Interactive Demo — A Day in the Life.html` (5.3MB). Its ACTUAL system is **product-UI, not the editorial kit**: font **Roboto** (not Playfair/DM Sans), green `#2DB56E` (+600 `#228752`, 300 `#7BD3A0`), deep forest `#014637` for dark surfaces, action orange `#F58220` (the one spark), text `#202020`/`#5A5A5A`/`#9A9A9A`, white `#FFFFFF` + sidebar `#F5F4F2` + zebra `#FAFAFA`, border `#E0E0E0`, persona-chip blue `#0F4C99`, radius 8px.

**When a deliverable is meant to be presented ALONGSIDE the demo, skin it to the demo's product-UI system above, not the editorial Playfair kit.** Building the US outbound deck in the editorial kit was rejected ("try again") Jul 29 2026; re-skinned to the demo system and confirmed. The US_Outbound_Strategy_Deck.html + US_Outbound_Strategy_Master.html (Desktop deliverables + us-nate-motion/) now follow the demo system. Keep the inline logo `<symbol id="ilogo">` (its mark colors already match the demo). Do NOT revert these to Playfair. See [[intradiem-official-brand]] and [[us-outbound-motion-nate]].

**HARD OVERRIDE, Jul 30 2026 (supersedes the old two-mode rule):** EVERYTHING Dallas produces now ships in the official Intradiem brand. There is no "internal" blurple/creme mode anymore, not even for internal operating docs or daily briefs. Do not build in dallas-brand and do not offer it. The Nate/Jack motion plan-of-action docs and daily briefs are all Intradiem-branded. The **default implementation is the demo product-UI system** (Roboto + Roboto Mono, forest #014637, green #2DB56E / #228752 / #7BD3A0, orange #F58220 as the single spark, ink #202020/#5A5A5A/#9A9A9A, surfaces #FFFFFF/#F5F4F2/#FAFAFA, border #E0E0E0, persona-blue #0F4C99, 8px radius). The canonical copy-from reference for this system is `us-nate-motion/US_Outbound_Strategy_Master.html` (head/style lines 1-136 hold the full palette + the inline `<symbol id="ilogo">` 4-color diamond mark: #FDBF40 / #F58220 / #A5CE3A / #2CB56E, forest wordmark via `.wm` fill). The Playfair/DM Sans Norton editorial kit is the alternate Intradiem system for pure exec/print pieces; when in doubt for motion/GTM work, use the demo product-UI system.
