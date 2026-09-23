---
name: feedback-render-before-calling-it-live
description: "Sep 23 2026: Dallas caught a broken tools-bar layout on a live rep page that I had declared deployed and verified; verification was byte-identity and grep, never a render. Render one downscaled screenshot after any layout change before saying a page is live."
metadata:
  type: feedback
---

**What happened (Sep 23 2026):** the Keegan index shipped with a two-column grid that squeezed the "Warm doors" link into a one-word-per-line sliver and stretched the builder button across the page. I had called it live after a byte-identical live diff and grep checks; Dallas sent a screenshot and asked "would you use this as-is?" The answer was no.

**Why:** byte checks prove the deploy, not the page. A layout change needs one visual read.

**How to apply:** after any CSS or markup change to a rep-facing page, render once with headless Chrome, downscale with sips -Z 900, and look at it before the deploy and before the handoff line says "live". One render per iteration, deleted after the check (context discipline). Related: [[keegan-call-asks-built-sep23]], [[feedback-seller-pages-no-fluff]].
