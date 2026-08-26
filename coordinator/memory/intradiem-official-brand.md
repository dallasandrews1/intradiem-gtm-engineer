---
name: intradiem-official-brand
description: "Intradiem OFFICIAL brand (source of truth = Naveen's onboarding link); green+Playfair, NOT the orange/Outfit guess. Two-mode rule with dallas-brand."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08961b83-9830-4e80-9df7-23be56983c25
---

**SUPERSEDED for deliverables (Jul 30 2026):** Dallas designated the Roboto-system kit from his work-machine US Outbound assets (Interactive Demo lineage) as the current standard for ALL Intradiem deliverables; see [[intradiem-brandkit-current-jul30]]. The green/Playfair kit below is retained as history only.

**Source of truth for Intradiem official branding = Naveen's onboarding site** https://onboarding-dallas-intradiem-gtmeng.netlify.app/ . Extracted live from its CSS Jun 25 2026. This SUPERSEDES the orange-primary / Outfit-Inter guess in the project file `intradiem-brand-kit.md` (which inferred orange from an old theme-color and guessed fonts — wrong).

**Fonts (the insider tell):** Playfair Display = headings (serif, weight 700). DM Sans = body. JetBrains Mono = small eyebrow/tag labels + code. NOT Outfit/Inter.

**Palette is GREEN-forward** (≈882 green vs 183 orange uses on the site; orange is a ~17% secondary spark, not primary):
- --forest #16432C · --green #1F7340 · --green-bright #25B56F · --lime #B6D94C · --lime-bright #A4CE3A
- --ink #15231B · --ink-soft #3E4D44 · --dim #7A877E
- --paper #FAFBF7 · --card #FFFFFF · --mist #F0F4ED · --mist-2 #E7EEE3 · --line #E2E7DD · --line-2 #D4DCCE
- --gold #E0A23B (small accent) · --orange #FE5000 / --orange-soft #F47920 (secondary spark only)
- shadow: 0 1px 2px rgba(20,40,25,.04), 0 12px 34px rgba(20,40,25,.07); rail width 248px (left sidebar layout)

**Two-mode brand rule (Dallas's instruction Jun 25 2026):** [[dallas-brand]] (personal blurple/creme, Outfit) = INTERNAL outputs + personal portfolio/thought-leadership only. THIS official Intradiem kit (green/Playfair/DM Sans/JetBrains Mono, from Naveen's link) = anything EXTERNAL, exec-facing, or sent to Naveen/the team. Goal: look like part of the team and brand, never an outsider. When a deliverable is Intradiem-facing, mirror Naveen's exact fonts + green palette, not a generic orange theme.

**Color-application rules (refined Jun 25 2026 from Naveen's live site, confirmed by extraction h2 color = rgb(22,67,44)):**
- **Headings = forest green #16432C** (var --orange-deep) on light backgrounds — section titles AND card titles. NOT near-black. Keep white on dark surfaces (hero h1, footer, dark cards).
- **Section eyebrows / kicker labels = ORANGE spark #FE5000** (the mono "06 · IN MARKET" style). Orange is the eyebrow/kicker color.
- **In-card small labels (e.g., "THE PROBLEM THEY FEEL", group headers) = green**, not orange.
- Body text near-black #15231B. Big stat numbers green or white-on-dark. So: orange kickers, green headings, green accents/numbers, green in-card labels.

**Interaction pattern to match (Naveen's app feel):** left sticky dark-forest sidebar rail (248px, logo card on top, numbered nav with title+subtitle, active = white-overlay bg + lime left bar + lime number, Presenter toggle pinned bottom). Content = paper, flat white tiles (14px radius, 1px green border) that hover-lift. Rich sections use **selectable cards + a sub-tab pill bar that swaps a detail panel** (his Motions: motion cards → tabs Why now / The machine / Personas / Triggers / Cadence / Status → 3-column detail tiles on mist-green bg + a dark-green stat band). Sub-tabs: active = filled dark-green pill, inactive = white pill w/ border. Build interactive drill-downs, not static stacks.

**Reskin done (Jun 29 2026):** All 5 live connector artifacts (command-center, strike-room, golden-list, control-plane, roi-calculator) were re-skinned from the old orange/Outfit guess to THIS official green kit (green palette, Playfair headings, DM Sans body, JetBrains Mono eyebrows/tags, orange demoted to spark). Logic untouched, only style + copy. ALSO reframed command-center's posture: the old "credit war / not ratified / credit is a claim" attribution language flipped to partnership ("co-define what engine-sourced means with Naveen, shared scoreboard not a credit claim"); 15-meeting target marked provisional (~15, "co-shaping with Naveen") per the rough-sketch posture in [[intradiem-q3-mandates]]. mission-control was already correct (provisional-aware) and was the model. Verified: all 5 JS parse clean, green tokens present. Source files in outputs; pushed via update_artifact.

**Extended (Jul 2 2026, Dallas's instruction):** the reference for this kit is now also his own deployed site gtmstrategy.dallasandrews.dev (same tokens, verified from `GTM Engine - deploy/index.html` in the project folder). Two more surfaces moved onto it: (a) the `intradiem-day1-audit-console` artifact (reskinned from orange/Outfit because Genna may see it; #FE5000 survives once, as the active-tab underline) and (b) `Grand_Plan_Master.html` in the project folder (his eyes-only master plan; he explicitly chose Intradiem green over personal blurple for it). So the two-mode rule now reads: personal blurple = non-Intradiem work only; EVERYTHING Intradiem-context, including private planning surfaces, runs the green kit. Later the same day Dallas asked for `dallas-mission-control` too, so it is now also on the green kit (#FE5000 survives once, as the next-gate banner's left border). No exceptions remain: every Intradiem-context surface runs green/Playfair.

**Reskin (Jul 30 2026), then SUPERSEDED the same day:** the three BDR motion deliverables were rebuilt off the old personal blurple/Outfit skin onto this green/Playfair kit around 14:00. Hours later Dallas supplied the current Roboto standard, so at ~19:15 the same three files were rebuilt AGAIN onto that standard and no longer run this kit. See [[intradiem-brandkit-current-jul30]] for where they landed. The semantic border convention survived both rebuilds and is worth reusing: **green left border = the safe/verified thing** (gates, send-as-written copy blocks), **orange left border = caution or improvise** (risk callouts, call bullets), **orange also carries the "you cannot say" column**. Verified by headless Chrome screenshot (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --screenshot`), which works locally on the personal Mac with no playwright install; see [[headless-render-workaround]].

**DONE (Jul 7 2026):** `intradiem-brand-kit.md` rewritten from the orange/Outfit guess to this official green/Playfair + DM Sans + JetBrains system (orange demoted to secondary spark); Start Here asset-map card updated to match. No stale orange brand doc remains. Two sidebar tombstones (`intradiem-gtm-signal-engine`, `morning-intelligence`) still safe for Dallas to manually delete. See [[intradiem-cohesion-layer]], [[check-project-before-hedging]].
