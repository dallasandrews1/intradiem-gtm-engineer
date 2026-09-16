---
name: intradiem-launch-kit
description: "Product-launch GTM kit compiler for Intradiem. Takes a product's readiness status (Market: Tom Russell, Business: Scott Kemme, Product: Chris Busbee) and compiles the full go-to-market execution package: positioning brief draft, enablement one-pager, outreach sequence set, demo script and interactive artifact spec, launch campaign brief for Marketing, war-room signal additions, and the launch instrumentation plan. First run: Back Office Optimizer, September 2026 GA. Then Queue Optimizer beta, Engagement Hub, and the 2027 GA wave. Trigger on: launch kit, GA package, launch plan for [product], BOO launch, QO beta launch, what does GTM need for the [product] launch, or any moment a readiness stream approaches its launch date. Load proactively when a launch date moves or a GA confidence read changes."
---

## When this skill applies

- 6-8 weeks before any product's target GA or beta date (start the compile)
- The week a readiness owner changes a launch date or confidence level (recompile timing)
- When Naveen or a readiness owner asks what GTM has ready for a launch
- Post-launch: week-2 and week-6 retro passes

## Background

Intradiem tracks launches through three readiness streams: Market (Tom Russell), Business (Scott Kemme), Product (Chris Busbee). The streams measure whether a product is ready to launch. Nothing on the map owns the execution package that turns "GA declared" into a coordinated market motion. This skill fills that seam: it consumes what the streams produce and compiles the package, explicitly crediting the streams. It packages; it never claims their ownership.

## Ownership etiquette (hard rules)

- **Tom owns positioning and narrative.** This skill drafts the positioning brief FOR his review and sign-off, framed as "a compiled draft from your market readiness work." Never ship positioning he has not blessed.
- **Chris owns the date.** Pace everything off his stated confidence, never the slide date. A slip changes timing, never readiness. Never promise a GA date to anyone on his behalf.
- **Scott owns business readiness** (pricing posture, packaging, ICP validation). The kit consumes his outputs as inputs.
- **Sierra runs the campaign.** The campaign brief hands her a ready plan she can edit, never a fait accompli.
- **Week-1 discovery step (first run only):** confirm with each owner who owns launch execution today. If someone does, this skill becomes their tool and the compile runs in service of them. Claim the seam only if it is genuinely empty.

## Inputs

1. Product dossier: problem, what it does, where it wins, value, pricing posture (readiness stream materials; the onboarding site dossiers are the seed shape)
2. Readiness status per stream, with dates and the owner's own confidence language
3. ICP and target list (for BOO: the back-office ICP defined with Scott + the 200-contact universe)
4. Verified proof points from the Value Repository ONLY (intradiem-verified-metrics; a new product may have none, in which case the kit uses mechanism claims and beta evidence clearly labeled, never invented outcomes)
5. Competitive landscape (intradiem-competitive-intel wedge briefs for the product's space)

## The kit (outputs, one folder per launch)

Save under `launches/[product]_[target-date]/`:

1. **Positioning brief (DRAFT for Tom):** problem, category frame, one-sentence position, three message pillars, what we never say (product tells, unverified claims), objection map.
2. **Enablement one-pager:** what it is, who buys it, the three discovery questions, qualification criteria, pricing posture, FAQ. Written for a rep's ten minutes before a call.
3. **Sequence set:** persona-mapped outreach for the launch universe, compiled through intradiem-first-draft-engine and intradiem-copy-sharpener (their gates apply in full, including brand-light and verified claims).
4. **Demo script + interactive artifact spec:** the demo narrative plus the spec for the launch's interactive artifact (calculator, walkthrough page) in the green kit, consistent with the demo-engineering layer.
5. **Campaign brief for Marketing:** audience, offer, channels, timing, content set (intradiem-content-engine compiles the assets), success metrics.
6. **War-room signal additions:** which new signals now matter for this product (for BOO: BPO contract news, back-office hiring clusters, cost-per-transaction language in filings) appended to the daily war room taxonomy.
7. **Instrumentation plan:** source tags for the launch motion (its own source_motion value), baseline definitions, what the week-2 and week-6 retros will measure, credit budget for the launch's enrichment (clay-credit-steward pre-check).

## Workflow

1. Confirm inputs and owner confidence. Missing readiness inputs stop the compile for that section; the kit ships with the gap named, never guessed.
2. Compile sections 1-7. Copy-bearing sections route through the copy skills; claim-bearing sections route through the verified-claims gate.
3. Owner review pass: positioning to Tom, business facts to Scott, product claims to Chris, campaign to Sierra. Log sign-offs in the kit folder.
4. Launch week: activate sequences (human approval gate as always), war-room signals live, instrumentation verified BEFORE volume.
5. Retros at week 2 and week 6: what the instrumentation shows, what gets killed, what scales. Append to the kit folder; feed the readout.

## Canon constraints

- Verified claims only; a launch with no Repository proof ships mechanism-and-beta framing, labeled
- Brand-light rules apply to launch outreach same as any motion
- Contact centers AND back offices, six verticals; BOO especially is the back-office white space, never a call-center feature
- Fail-closed: no send without instrumentation live and deliverability green
- No em dashes, no AI-isms, house style everywhere

## First run: Back Office Optimizer (Sept 2026 target)

Pre-work already in place: the back-office ICP (Layer 1 skill, with Scott), the 200-contact sourcing mandate (the launch universe and Mandate 3 are the same work), competitive wedges vs in-house RPA and status quo, and the war room's back-office signal tier. The kit's job in August: compile early so the September date is a switch-flip, and pace public-facing pieces off Chris's real confidence in his own words.
