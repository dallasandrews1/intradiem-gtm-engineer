# CONTENT — section by section
### Source copy for the showcase. Tighten freely; do not add facts not present here or in `03_VERIFIED_METRICS`.

---

## 00 · Start here
**Hero headline:** The engine, built before day one.
**Hero subline:** Ready to run, built to co-shape. A GTM acquisition engine — enriched, scored, instrumented, and gated — prepared for July 6, so we start from a system, not a blank page.
**Orientation (how to read this):**
- *Presenting?* Flip on Presenter mode — every card opens with a talk-track.
- *Just browsing?* Read top to bottom; each section stands on its own.
- *Chips:* **VERIFIED** = confirmed fact · **DRY-RUN** = illustrative, seeded, goes live Jul 6 · **TARGET** = Q3 goal, provisional and to shape together.
**Posture line (small, under hero):** This is a contribution to shape with Naveen and the team — the durable value is the engine itself, robust to whatever targets land.

## 01 · The thesis
**Headline:** Pipeline is a system output, not a sales activity.
**Body:** The job is automating the frontline work so reps spend time selling, not researching. Every row moves left → right:
- Manual list → **automated enrichment (Clay AI)**
- Rep research → **AI-scored lists**
- One-off emails → **personalization at scale**
- Disconnected tools → **central pipelines**
- Slow iteration → **experiment loops**
- Limited personalization → **signals-based outreach**
**Close:** I built the system that runs every row of the right column — and the rails that prove it's working.

## 02 · The Golden List (the foundation)
**Headline:** A live account intelligence layer — not a static spreadsheet.
**Body:** Dynamic, enriched, scored, graded; updates as the market moves. Every campaign, every sequence, every agent runs off it.
**Six components (hub-and-spoke):** account scoring · contact enrichment · intent signals · outreach sequences · rep prioritization · pipeline reporting.
**Three capabilities (cards):**
- **AI Enrich** — waterfall enrichment across 40+ data sources (firmographic, technographic, intent). [VERIFIED: 40+ sources feed the current Star Ratings enrichment]
- **Personalize** — context-aware AI messaging at scale. No copy-paste templates.
- **Automate** — agents running around the clock for prospecting, research, list-building, follow-up.
**Ready-now artifact:** a click-by-click **Clay Build Pack** — tables, columns, enrichment waterfalls, fit/intent/grade formulas, signal columns, source-tag writes, webhooks — so the list rebuilds in ~2 hours on Day 1, not designed from scratch.

## 03 · The engine (cohesion layer) — the centerpiece
**Headline:** One weekly motion, seven stages, gated where it matters.
**The conductor (horizontal flow):** 0 Spec-reread → 1 Refresh → 2 Re-score → 3 Scan signals → 4 Draft → **4b Objective critic** → **5 Human approve** → **6 Send (deliverability-gated)** → 7 Instrument → 8 Guardrails.
**The three-layer story (the line that lands with Naveen):** **Maker** (the draft engine) → **objective Checker** (an independent critic that holds bad drafts on deliverability, ICP/persona, in-scope motion, verified-claims, length) → **Human** (Dallas/the rep approves before anything leaves the building). Three layers, not one. *I automate around the judgment, not the judgment itself.*
**Control tower:** the single front door — one screen with headline numbers, the 7-step diagram, and a tile per window. [DRY-RUN: numbers shown are seeded until go-live]
**Single source of truth:** one state file every dashboard reads and the conductor writes — kills dashboard drift.

## 04 · Guardrails as the product
**Headline:** The guardrails are the product.
**Governing principle:** measurement before volume · ICP before sourcing · human before send.
**Three self-policing tripwires (from a pre-mortem):**
- **WIP-of-one** — only one motion scales at a time; anti-sprawl. (Star Ratings is the one; everything else waits in backlog.)
- **Throughput-by-operator** — alarms if Dallas's share of weekly releases exceeds a 20% ceiling. "Done" = the team runs it unaided, not "works when Dallas runs it."
- **Operator-test** — a motion only flips to "operable" after two consecutive batches released by a non-Dallas operator.
**Go-live preflight gate:** `conductor --preflight` runs 12 assertions and refuses to go live until green. Pre-access it correctly reports **NOT READY — 4 known blockers: ratify attribution, set the 1× baseline, deliverability green, security audit current.** Those four ARE the Day-1 checklist. [VERIFIED by running it]
**Deliverability infra** is a P1 send-gate (warmup, rotation, spam/blacklist monitoring) so scaling can't become spray-and-burn and poison the 157 warm contacts.

## 05 · Proof (the bar I'm building to)
**Framing line:** These are the proof class Intradiem chose as the standard — the bar I engineered this to meet. (Not my results — the target shape.)
- **Intercom** — close to **$1M new pipeline in 30 days**: Clay-sourced → enriched → CRM-integrated → scaled from small tests to full deployment. [VERIFIED proof point]
- **Rippling** — **2× cold-email performance YoY, 60% open, 10% reply, 100K+ emails/month** via real-time signal-triggered multi-channel sequences and team-wide experimentation, no engineering resources. [VERIFIED proof point]
**The standard:** the team that pilots it becomes the blueprint for Intradiem globally.

## 06 · The four Q3 goals (all TARGET / provisional)
For each: the goal → how the engine delivers it → the pre-mortem risk → the leading indicator Dallas owns.
1. **15 vetted new-logo meetings** [TARGET] — senior tech officers in WFM/Ops, sourced via the Star Ratings motion (MA payers at the bonus cliff) + the back-office motion via Clay. *Risk:* meetings live in reps' reply-handling (people Dallas doesn't manage). *Owned indicator:* qualified replies sourced, source-tagged.
2. **10× BDR messaging throughput** [TARGET] — one push → a motion that runs every week. *Defined as* qualified replies/week, gated by a deliverability floor — not raw send volume. *Risk:* vanity volume burns domains. 
3. **200+ back-office contacts** [TARGET] — inside existing customers' back offices, sourced via Clay, sold into the install base. *This number is Dallas's regardless of product timing.* *Risk:* sourcing against a non-existent ICP — fixed by defining the ICP with Scott Kemme in Week 1.
4. **Build + maintain the modern growth engine** [standing OKR] — lists, signals, instrumentation, cadence, agents, calculators, control plane. A living system that stays current.
**Where you come in (echo of Naveen's site):** Dallas owns the GTM engineering behind all three numbers — the Clay build, the enrichment + signal library, the list expansion, and the instrumentation that turns numbers into a motion that repeats.

## 07 · Motions in play
- **Star Ratings (the one scaling motion):** at the CMS 4208 cliff. From CMS data, Director+ contacts in Finance, Stars, and Medicare across non-customer plans below 4.0 stars; Clay enriches each record and drafts a contextual message at scale. [VERIFIED current state: 157 Director+ contacts · 38 non-customer plans < 4.0 · 5,000 Clay credits · security review done · Clay rolled out to the outreach team] The 2028 Stars call-center measures are the cleanest, finite attribution window.
- **Back Office (staged):** the manual back-office white space inside existing customers. Held behind ICP definition (Scott Kemme) and Back Office Optimizer GA (Sept, owned by Chris Busbee). Correctly *not scaling yet* — WIP-of-one.
**Signal library (tiered):** Tier 1 act-immediately (CMS releases, Stars language in SEC filings, earnings mentions) · Tier 2 prioritize-this-week (new quality leadership, hiring clusters, contracts just under 4.0) · Tier 3 supporting context.

## 08 · Modernizing (the live tools)
Decks → interactive tools; Excel → live calculators; static collateral → a control plane + always-on channel.
- **Command Center** — the canonical live front door (gates, approvals, deliverability, variant winners, attribution credit). [DRY-RUN snapshot until Jul 6]
- **Golden List board** — accounts scored/graded.
- **Control Plane** — install-base white-space view (the 200 back-office wedge).
- **ROI Calculator** — live economic-impact tool.
- **Mission Control** — the daily personal tracker.
Note: these are live front-ends; the engine windows run on a seeded snapshot until Salesforce/Clay connect on Day 1.

## 09 · Everything that's ready (index)
Pull the full list from `05_INVENTORY_whats_ready.md`. Group as: **Engines · Dashboards/Artifacts · Skills library · Scheduled automations · Day-1/Week-1 order of operations.**
**Close line:** Nothing here needs to be built — it needs to be wired to real data on Day 1. The pre-access work is design, spec, and content; the go-live work is four checklist items.

## FOOTER / CLOSE
**Partnership close:** This is strong thinking prepared to accelerate us — a contribution to shape together, not a plan to execute at you. The engine is the durable value, and it's robust to whatever targets we land on together.
*Dallas Andrews · GTM Engineer · starting July 6, 2026*
