---
name: present-mode-deck-pattern-aug26
description: "Aug 26 2026: leadership pages can carry a built-in Present mode (Naveen's queueoptimizer-qbr.netlify.app is the reference: forest slides, staggered data-a reveals, counting numbers, drawn lines, bottom HUD with dots and count, arrow keys and swipe); first use is GTM_Campaign_Brief_Sep3.html; Dallas wants motion with few words"
metadata:
  type: feedback
---

On Aug 26 2026 Dallas asked for a Present mode on the Sep 3 campaign brief page: "Make the presentation dynamic with motion elements etc and keep it simple when it comes to the words and explanations. Naveen's presentation is a great example." Naveen's reference: https://queueoptimizer-qbr.netlify.app/ (DM'd Aug 17): 29 `.slide` sections, dark forest gradient with corner glows, `[data-a]` staggered reveals (opacity + translateY), big tabular-nums counters, SVG stroke-dash draws, bottom HUD (brand, dots, count, arrows), progress bar, arrow keys, space, swipe.

**Why:** the meeting rooms Dallas presents to (John's campaign alignment, Pipeline Council) respond to moving visuals with few words; dense tables read as documents.

**How to apply:** one file, two views. Document view stays the default for pre-reads; a fixed "Present" button (and `#present-N` hash) opens a fixed-position deck built in the same Roboto/forest system, nine slides max, under 40 words each, motion only where it carries meaning (counters, a travelling pulse on a loop, bars growing on a timeline), Esc returns. Pattern lives in `motions/gtm_campaign_alignment/GTM_Campaign_Brief_Sep3.html` (append block after `.sheet`). Gotchas: never style `.dec div` (hits inner divs, use `.dec>div`); animateMotion circles need `opacity=0` plus a `<set>` at begin; check renders at 1280x720 via zoom:.5 iframes, not 640px tiles (mobile breakpoint). Related: [[html-deliverable-standard]], [[feedback-no-showy-deliverable-copy]], [[gtm-campaign-alignment-meeting-sep3]].

**Addendum (Aug 26, evening):** Dallas asked whether the operating map should get "motion elements and more marketing drastic eye-catching color choices"; the call was motion yes where it explains, palette no (every Naveen-facing page this quarter is the same forest/green/orange system, and a weekly reference page that shouts fatigues). Applied to `GTM_Operating_Map_Aug26.html`: the system map lives in the hero on forest and draws itself in order (`.hmap.play` with per-element `--d` delays, a pulse on the loop via animateMotion), IntersectionObserver-staggered `.rv` reveals on every list and table, orange narrowed to the AM sheet, the ads lane, and decision owners (`td.own`), and a four-slide Present mode (map, roster, calendar, threads). Slide maps need `max-height:60vh` or they run under the HUD at 720px.
