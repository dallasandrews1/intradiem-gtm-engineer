# BUILD PROMPT — "GTM Engine: Ready to Run" showcase site
### Paste this whole file into Claude Design (Claude.ai project / artifact). Attach the other five files in this folder as project knowledge so every fact is grounded.

---

## ROLE
You are a senior product designer + front-end engineer. Build a **single, self-contained HTML page** (one file: inline CSS + inline JS, no external build, no frameworks required — vanilla is fine; a single CDN font link is allowed). It must work opened straight from disk and when shared as a link.

## WHO THIS IS FOR & THE JOB IT DOES
This is **Dallas Andrews's** showcase of the GTM engine he built and has ready to run on **Day 1 (July 6, 2026)** as Intradiem's new **GTM Engineer**, reporting to Naveen Thilagan. It is the mirror-image companion to the onboarding site Naveen built to pre-onboard Dallas — same caliber, same dark-editorial Intradiem feel — but where Naveen's site said *"here's the role and where you come in,"* this one says *"here's the engine I've prepared, and how it delivers the quarter."*

It must serve **two readers at once**:
- **The presenter path** — Dallas walks Naveen / GTM leadership through it live. Section order is a narrative he can talk over.
- **The skim path** — someone opens the link cold, with no presenter, and still gets the whole story. Every expandable element must make sense unguided. Include a short "read me first" orientation and self-explaining captions.

## NON-NEGOTIABLE POSTURE (this governs tone everywhere)
Per Naveen's welcome email, the Q3 numbers are a *"rough sketch we'll shape together."* So the site's voice is **partnership, not conquest.** This is *"here's strong thinking I've prepared to accelerate us — let's shape the specifics together,"* never *"look what I built instead of learning your system."* Confident about the engineering, humble about the targets. The frame that lands with Naveen: **"I don't automate the judgment — I automate everything around it and put a hard human gate where the judgment lives."**

## METRIC INTEGRITY — THE HARD RULE (read `03_VERIFIED_METRICS_and_integrity_rules.md`)
This is the most important rule in the build. Mislabeling a number is the one thing that can damage Dallas.
- **VERIFIED facts** (from `03_...md`) may be stated plainly as fact (e.g., Intercom ~$1M pipeline in 30 days; Rippling 2× / 60% open / 10% reply / 100K+ emails/mo; 157 Director+ contacts; 38 non-customer plans < 4.0; 5,000 Clay credits; 40+ data sources).
- **SEEDED / dry-run numbers** from Dallas's engine (e.g., any "$ surfaced," variant reply-rates, funnel counts) must be visibly labeled **"illustrative — dry-run / seeded, goes live Jul 6."** Never let a seeded number look like real pipeline. Put a small persistent legend chip near any such figure.
- **PROJECTIONS / targets** (15 meetings, 10×, 200 contacts) must be labeled **"Q3 target — provisional, to co-shape."**
- Do not invent any statistic. If a number isn't in the attached files, don't use it.

---

## INFORMATION ARCHITECTURE (single page, sticky tab nav 00–09)
Mirror Naveen's numbered, card-based structure. Content for each section is in `01_CONTENT_sections.md` — use it verbatim-ish; tighten, don't embellish.

- **00 · Start here** — hero + orientation. Dark ink hero, Intradiem orange spark. One line: *"The engine, built before day one. Ready to run, built to co-shape."* A 3-bullet "how to read this" (presenter vs skim), and a legend explaining the VERIFIED / DRY-RUN / TARGET chips.
- **01 · The thesis** — "Pipeline is a system output." The left→right transformation table (manual list → automated enrichment, etc.). What Dallas built to make it real.
- **02 · The Golden List** — the foundation. The six components as a hub-and-spoke (account scoring · contact enrichment · intent signals · outreach sequences · rep prioritization · pipeline reporting) + the three capabilities (AI Enrich / Personalize / Automate). Expandable cards.
- **03 · The engine (cohesion layer)** — the centerpiece. The 7-stage weekly conductor as a horizontal flow with gates highlighted. The **maker → objective critic → human** three-layer story. The control tower as the single front door.
- **04 · Guardrails as the product** — measurement before volume · ICP before sourcing · human before send. The three premortem tripwires (WIP-of-one, throughput-by-operator, operator-test). The go-live preflight gate (12 assertions, 4 known blockers = the Day-1 checklist). This section is what separates "engineered" from "sprayed."
- **05 · Proof** — verified proof class (Intercom, Rippling) presented as "the bar I'm building to," not as Dallas's own results. Clear attribution.
- **06 · The four Q3 goals** — 15 / 10× / 200 / build-and-maintain, each as a card that expands to "how the engine delivers it" + the premortem risk + the leading indicator Dallas owns. All targets labeled provisional.
- **07 · Motions in play** — Star Ratings (the one scaling motion, at the CMS 4208 cliff) + Back Office (staged behind ICP + BOO GA). Show why only one motion scales at a time (WIP-of-one).
- **08 · Modernizing (the live tools)** — the dashboards/artifacts as "decks replaced by tools": command center, golden list, control plane, ROI calculator, mission control. Note these are live front-ends; the engine windows run on a seeded snapshot until go-live.
- **09 · Everything that's ready** — the full inventory index (from `05_INVENTORY_whats_ready.md`): engines, dashboards, skills library, scheduled automations, the Day-1 / Week-1 order of operations. The "nothing left to build, here's the proof" close.
- **Footer / close** — partnership line: *"All of this is a contribution to shape together — the durable value is the engine, robust to whatever targets land."*

## INTERACTION & LAYOUT
- **Sticky left or top tab rail** numbered 00–09 (like Naveen's), with the active section highlighted; smooth-scroll. On mobile it collapses to a hamburger / horizontal scroller.
- **Expandable cards** ("Enter →" / click-to-open) for depth-on-click, exactly like Naveen's site. Default collapsed so the skim path isn't overwhelmed; opened state reveals detail.
- **Banners / pills** for status and integrity chips (VERIFIED · DRY-RUN · TARGET · LIVE Jul 6).
- **A "presenter mode" toggle** (optional but strongly preferred): a switch that expands all cards and adds a subtle on-screen talk-track caption per section so Dallas can present without notes; off by default for the clean skim view.
- Subtle scroll-reveal animations; nothing gimmicky. Respect `prefers-reduced-motion`.
- Fully responsive (desktop presentation + mobile share). Keyboard-accessible; aria labels on toggles; AA contrast.

## DESIGN SYSTEM (full tokens in `02_BRAND_intradiem.md`)
- **Arc:** dark **ink** hero that commands → warm **paper** interior that breathes → orange as the spark only on the highlight / key number / CTA (~10% of surface, never wallpaper).
- Colors: `--ink:#14181F` `--ink-2:#2A323C` `--paper:#FAF8F6` `--white:#FFFFFF` `--text:#1B1F26` `--orange:#FE5000` (primary spark) `--orange-deep:#D8400A` `--orange-tint:#FFE9DF` `--line:#EFEBE6` `--gray:#5A5F66`. Status only (never orange): green `#2f8f4e` amber `#b5751a` red `#c0392b`.
- Type: headings/numbers **Outfit** (700–800), body **Inter** (400/600). One Google Fonts link is fine.
- Feel (Dallas's brand soul): whimsical-but-serious — inventive yet engineered, warm yet authoritative, airy, scannable, rememberable, executive-ready. If it looks templated, it's wrong.
- Do NOT use League blurple/purple anywhere — this is Intradiem; orange = "one of us."

## OUTPUT
- One `index.html`, fully self-contained. No backend. No localStorage/sessionStorage. All data hard-coded from the attached files.
- Make every section editable-by-hand later (clean structure, commented sections).
- At the very top of the file, a comment block: what's verified vs seeded, and where to swap real numbers in after Jul 6.

## ACCEPTANCE CHECK (do this before returning)
1. Open the skim path mentally: with zero presenter, does each section explain itself? 
2. Is every number correctly chipped VERIFIED / DRY-RUN / TARGET? Any unlabeled stat is a defect.
3. Does the tone read as partnership, never as a parallel-system flex?
4. Does it match Naveen's caliber (dark editorial, numbered sections, expandable cards) without copying his copy?
5. Single file, responsive, accessible, reduced-motion safe.
