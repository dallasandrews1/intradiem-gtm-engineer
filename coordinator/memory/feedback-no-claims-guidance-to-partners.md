---
name: feedback-no-claims-guidance-to-partners
description: Partner-facing deliverables never carry a "what we can say" claims section; partner reps are the sellers and set their own words
metadata:
  type: feedback
---

Sep 5 2026: Dallas cut the "What Intradiem can say / What we can put in writing" section from the partner-safe account briefs (motions/partner_channel/build_briefs.py, `say` now internal-only).

**Why:** the verified-claims tiers are an internal reference. Handing a partner rep a list of approved and off-limits lines reads as telling them how to sell, and they are the sellers, not Dallas. The section also rendered blank in the page screenshot, which is a separate reveal-animation artifact (see below).

Deployed the same day: the partner-safe pages are live at https://gtm-partner-pilot.pages.dev/briefs/ (ally, maximus, compare), rebuilt from build_briefs.py and copied into `~/Desktop/Intradiem Deliverables/deploy-partner-pilot/briefs/`. The live pages had a hand edit the builder did not know about (the "Likely role" column stripped from the partner people table); that is now encoded in build_briefs.py so a rebuild cannot regress it. Same reasoning as the claims block: the committee-role read is our working guess, not a fact to hand a partner rep.

**How to apply:** verified-claims and tier guidance, and the committee-role read, stay on internal versions only. Anything that goes out to a channel partner, an AM, or another seller gives them the account facts and leaves the words to them. Related: [[feedback-no-tasks-for-ams]].

Render note: `.rv` in motions/ai_champion_product/_tpl/base.css starts at `opacity:0` and only becomes visible when the IntersectionObserver adds `.in`, so any full-page headless screenshot shows reveal sections as blank. Blank in a render is not proof the content is missing.
