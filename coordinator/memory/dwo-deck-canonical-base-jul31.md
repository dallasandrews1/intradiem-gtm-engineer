---
name: dwo-deck-canonical-base-jul31
description: Naveen's Interactive-6 is the canonical DWO deck base, the BrandFix fork is retired, and the rebranded deck lives at DWO_Deck_RachelBrand_v1.html
metadata:
  type: project
---

Jul 31 2026. Two DWO deck files existed and they had diverged.

**Canonical base: `~/Downloads/Dynamic-Workforce-Orchestration-Interactive-6.html`** (Naveen's, 782,762 bytes, live at dwostoryqbr.netlify.app). It is what Rachel and Melissa actually reviewed and it holds the newest slide-5 interaction.

**Retired: `Naveen_QBR_Deck_BrandFix.html`** (780,975 bytes). It was branched off an earlier cut and applied the Jul 30 Roboto kit. Three reasons it is a dead end: it silently dropped 36 lines of slide-5 JavaScript (the pinnable loss-isolation interaction plus `role=button`, `aria-pressed`, `aria-label`, keyboard Enter/Space/Escape, `:focus-visible`), downgrading it to plain `:hover` and losing keyboard access entirely; its colour pass was incomplete, leaving 8 hardcoded old-orange and 11 old-lime rgba values behind; and its palette was wrong anyway against Rachel's rules.

**Live deliverable: `~/Desktop/Intradiem Deliverables/DWO_Deck_RachelBrand_v1.html`.** Built on Naveen's v6 with the slide-5 interaction intact, then linted clean against [[intradiem-brand-kit-machine-jul31]].

Two lessons worth keeping. Always confirm which file is canonical before a brand pass; the prettier filename was the older, lossier fork. And when screenshotting this deck, the file contains **two** `</body>` tags because the presenter-view shell is a JavaScript string, so any injected harness must target the LAST one or it silently lands inside a JS string and renders nothing. See [[context-discipline-jul31]] for the render-reading rules.
