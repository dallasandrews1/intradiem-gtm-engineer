---
name: feedback-restyle-check-every-slide-family
description: "Sep 24 2026: after restyling the ChangeOS pages from all-dark to the deck's cream-and-forest rhythm, page-level styles kept white text and lime headers, so overview slides 3 and 4 were unreadable on cream; Dallas caught it. Page styles are light-first with .dark overrides, and a restyle renders one slide of EACH family before deploy."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d937e8e6-de04-4cb7-b28c-971c069eef89
  modified: 2026-09-24T16:00:31.540Z
---

Dallas, Sep 24 2026: "we need to fix the color choices on the presentation especially 3 and 4 because I can't read half the page." Cause: the overview's own `<style>` block (phase cards, the component table, the quote) was written for the all-dark first build (`color:#fff`, `var(--lime)`, `var(--mist)`); when the shared CSS moved to the deck's cream-paper slides those rules stayed, and two tokens (`--mist`, `--mist-2`) no longer existed at all. The render check before deploy looked at the title and one screen slide, both fine, and never at a light content slide with page-level styles.

**Why:** a restyle that changes slide backgrounds changes the contrast contract for every page-level rule; the shared file being right proves nothing about the page files.

**How to apply:** write page-level styles light-first with `.dark` overrides (never bare `#fff` or accent colors outside a `.dark` scope); after any background or token change, grep every page for `var(--` names missing from the shared CSS and for hard-coded whites, then render one slide from each family (dark cover, light content, light screen) before deploying. Related: [[changeos-pilot-prototype-sep24]], [[feedback-render-before-calling-it-live]].
