# Q3 GTM Engineer — Bulletproof Operating Plan
**Dallas Andrews · starts July 6, 2026 · reports to Naveen Thilagan**
Backbone: the onboarding site's **Section 05 (GTM Engineering)** — Intradiem's own definition of the role and what "great" looks like. Section 08 = what you're measured on. Premortem fixes layered as protection on the risky steps.

---

## PART 0 — POSTURE (how to walk in) — per Naveen's 6/23 welcome email
Naveen's framing changes how you carry all of this, not what you build:
- **The Q3 numbers are a "rough sketch."** His words: "don't read too much into the specifics yet — we'll shape them together once you're in and have a sense of the lay of the land." So 15 / 10× / 200 are **provisional targets to co-shape, not commitments to defend.** Treat every specific number below as a placeholder.
- **He's a collaborative, supportive sponsor**, not a turf you're protecting. "We'll shape them together." "I'm here to help all the way." Posture accordingly.
- **Reframe the attribution move.** Getting measurement defined early is still the #1 priority — but bring it as *"here's how I'd love for us to define what good looks like together,"* not as defending against a credit war. Same substance, partnership delivery. With a manager handing you partnership, a defensive posture is the one thing that could misread the room.
- **Bring the pre-start assets as contributions, not a finished plan.** The engine architecture (Golden List, enrichment, signals, instrumentation, pilot motion) is the durable value and is robust to whatever targets land. Walk in with strong thinking *to shape the specifics with him*, not a rigid plan to execute at him.
- **No pre-access:** Clay + accounts set up when you join; laptop coordinated via Chris. Pre-start work = design/spec/content only (already built).

---

## PART A — WHAT YOU'RE MEASURED ON (Section 08 — provisional, to co-shape)
Your four owned directives:
1. **15 vetted new-logo meetings** — senior tech officers in WFM/Ops; sourced via the Star Ratings motion (MA payers at the bonus cliff) + the back-office motion via Clay.
2. **10× BDR messaging throughput** — one push → a motion that runs every week.
3. **200+ back-office contacts** — inside existing customers' back offices, sourced via Clay, sold into the install base.
4. **Build + maintain the modern growth engine** — standing OKR.

### Scope — your directives vs. the company's product goals (don't conflate)
**Yours (GTM-eng outputs):** the four above. **Not yours (product/company goals, owned by others):** Back Office Optimizer GA (Sept; Chris Busbee), Queue Optimizer beta, Engagement Hub, the Market/Business/Product readiness streams (Tom Russell / Scott Kemme / Chris Busbee), the CMS 4208 window. Those are inputs and dependencies. **A product slip changes the value/timing of what you source — never your ability to hit your number.**

---

## PART B — WHAT "GREAT" LOOKS LIKE (Section 05 + 07) — the real spec
This is how Intradiem defines the role and success. Build to *this*, and the four numbers in Part A fall out as byproducts.

**Their definition of GTM Engineering:** "Pipeline is no longer a sales activity, it is a system output." The job is "automating the frontline sales and marketing work so reps spend time selling, not researching." You move every row from left to right: manual list → automated enrichment · rep research → AI-scored lists · one-off emails → personalization at scale · disconnected tools → central pipelines · slow iteration → experiment loops · limited personalization → signals-based outreach.

**The thing to build — the Golden List (the foundation).** "A live account intelligence layer. Not a static spreadsheet. Dynamic, enriched, scored, graded, updates as the market moves. Every campaign, every sequence, every agent runs off the Golden List." Six components: **account scoring · contact enrichment · intent signals · outreach sequences · rep prioritization · pipeline reporting.**

**The three capabilities the engine must express:**
- **AI Enrich** — waterfall enrichment across 75+ data sources (firmographic, technographic, intent).
- **Personalize** — context-aware AI messaging at scale. "No more copy-paste templates."
- **Automate** — agents running around the clock for prospecting, research, list-building, follow-up.

**The modern motion (Section 07):** replace decks with interactive tools, Excel with live calculators, static collateral with a control plane + always-on channel. The onboarding site itself is the proof standard — they want you producing artifacts like that.

**The bar for "great":**
- Proof class they chose: **Intercom — ~$1M pipeline in 30 days** (Clay-sourced → enriched → CRM-integrated → scaled from tests to full deployment). **Rippling — 2× cold email YoY, 60% open, 10% reply, 100K+ emails/mo** via signal-triggered multi-channel sequences, team-wide experimentation, *no engineering resources*.
- The standard: **"the team that pilots it becomes the blueprint for Intradiem globally."** Great = building the motion the rest of the org copies, not just hitting 15 meetings.
- The guardrail (how *not* to do it): **"AI does the enrichment. People keep the judgment. Outbound engineered rather than sprayed. Human approval before anything leaves the building."**

### The cast
Naveen Thilagan (mgr / Product Strategy, exec sponsor) · Nate Belfield (Sales, runs current Star Ratings outbound — credit risk + closest collaborator) · Genna (Sales) · Sierra Jones (Marketing) · Tom Russell (Market) · Scott Kemme (Business — your back-office ICP partner) · Chris Busbee (Product — controls BOO GA).

---

## PART C — THE GOVERNING PRINCIPLE
**Measurement before volume. ICP before sourcing.** Their pilot launches small and instrumented (three variants, tracked) *then* scales what converts. The scale step is the dangerous one — so the instrumentation, deliverability infra, and attribution rails exist to protect Weeks 5–8, where "present learnings / become the blueprint" has to be *provable*, not anecdotal.

---

## PART D — THE PLAN: their 8-week pilot as the spine
Their Section 05 pilot is the backbone. Mapped onto Jul 6 → end of Q3, with the Star Ratings motion (Section 06) running in parallel and the premortem fixes layered in. ✦ = premortem-fix protection.

### Pre-start (now → Jul 6) — get ahead of the ball
Built before day one, no system access required: the **GTM Engine Build Spec** (Golden List schema, enrichment waterfall, signal library, attribution schema), a **back-office ICP hypothesis** to pressure-test with Scott Kemme, and a **message-variant starter pack** (3 variants/segment). Walk in day one with the architecture done.

### Weeks 1–2 — Train & build (Days 1–14)
- Get trained on Clay; get access to Clay, Salesforce, squad Slack, the CMS-derived list, Nate's sending setup. Read before touching.
- Stand up the **Golden List v1** from the spec — start with the back-office market and the existing Star Ratings list.
- ✦ **Co-define success with Naveen** (collaborative, per his email — he wants to shape specifics together): agree how each goal is counted, that the engine is credited at the qualified-reply/meeting-sourced line, and which leading indicators you own. Frame as "let's define what good looks like," not defense. This is the if-you-do-nothing-else move.
- ✦ Define the **back-office ICP with Scott Kemme** before sourcing — confirm/replace the pre-start hypothesis.
- ✦ Stand up **contact-level source tagging** in Clay/Salesforce before any volume scales.
- Get the real BOO GA confidence from Chris Busbee.
- Refit the day-1 audit console against the real Salesforce schema; confirm the attribution fields (`gtm_engine_sourced`, `source_motion`, `sourced_date`) exist or flag them as a build. (Don't rebuild pre-access — it runs on guessed objects until SF connects.)

### Weeks 3–4 — Enrich & launch
- Run the **waterfall enrichment** across the 75+ sources; layer Tier 1/2 signals as live Clay triggers.
- Launch first outreach **small**: three message variants per segment, tracked. Human approval before anything sends.
- ✦ Stand up **deliverability infra first** (domain/inbox warmup, rotation, spam/blacklist monitoring) — small instrumented sends only; do not scale yet.
- ✦ Build the **instrumentation dashboard**: enriched → sent → deliverability/open → replies → qualified replies → meetings, split by motion, source-tagged.

### Weeks 5–6 — Iterate
- Kill underperforming variants; scale what converts.
- Move Star Ratings from one-time send → **weekly cadence** (this shift *is* "10× throughput").
- ✦ Define **10× as qualified replies/week, gated by a deliverability floor** (open ≥ baseline, spam < threshold) — so scaling can't become spray-and-burn.
- Build the **first follow-up AI agent** (Automate capability).
- Run back-office contacts into targeted campaigns inside the install base.

### Weeks 7–8 — Review & expand
- Present pipeline + learnings with the dashboard (provable, source-tagged).
- ✦ Mid-quarter recut with Naveen: your **200 contacts is yours regardless of product timing — hit it.** Only back-office *meetings* depend on BOO being sellable; if GA slips, renegotiate the meeting expectation, not the contacts or the engine build.
- Expand the model across the team — **this is the "blueprint for Intradiem globally" moment.** Document it as a repeatable motion.

### Days ~57–90 — Compound & prove the repeat
- Reps work replies; you keep volume flowing + enable reply-handling. You don't personally chase meetings.
- ✦ **Day-75 tripwire:** if you're not near ~10 of 15 meetings, escalate and renegotiate — don't discover it at QBR.
- Package the whole motion (list, signals, instrumentation, cadence, agents) as the documented, repeatable engine = Goal 4 and the proof-of-work artifact that travels with you.

---

## PART E — PREMORTEM FIXES (baked into Part D)
| Failure mode | Defense |
|---|---|
| Credit/attribution war — meetings book but reps absorb credit | Wk1–2 written attribution at the qualified-reply line; source-tagged instrumentation before volume |
| 10× as vanity metric burns deliverability (poisons the 157 warm contacts) | Wk3–4 deliverability infra as P1; 10× redefined as qualified replies/week with a deliverability floor |
| Back-office contacts sourced against a non-existent ICP | Wk1–2 ICP with Scott Kemme; 200 *qualified* contacts, paced so they don't decay before sellable |

## PART F — VERDICT
- **Uncontrollable:** Goal #1 lives in reps' reply-handling — people you don't manage. Plan around it: instrument upstream so you're credited for *qualified replies sourced*, and steer Naveen toward a leading indicator you own.
- **If you do nothing else:** Wk 1, co-define the measurement model with Naveen (engine credited at the qualified-reply/meeting-sourced line) + stand up contact-level source tagging before scaling volume. Collaborative framing, not defensive.
- **Confidence: Moderate–High.** Infra in place, exec sponsor, clear goals. Tips on winning the Week-1 instrumentation + attribution fight before volume shows up.

## PART G — WEEKLY CADENCE
- **Mon:** refresh signal triggers; pull last week's dashboard by motion.
- **Wed:** throughput + deliverability check; adjust sequences.
- **Fri:** numbers vs. all 4 goals to Naveen (leading indicators you own up top); flag GA/rep-conversion risk early.
- **Day-75 tripwire:** <10 of 15 → escalate + renegotiate.
