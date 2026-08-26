---
name: intradiem-strike-sequence
description: "Motion-agnostic account engine for Intradiem outbound. Turns an account into a full buying-committee outreach sequence staggered across business days with send-ready copy per contact. Default cadence is a five-touch multi-channel core (Centene Star Ratings is the built-in reference example); an extended arc is available for must-win contacts. Two modes: SEQUENCE (default, builds from existing engine/Clay research) and FULL (pulls from the TAM engine, signal engine, and Clay Contacts, then sequences). Runs any motion via a registry: Star Ratings cliff-edge is populated; back-office, install-base expansion/risk, competitive displacement, and cost-mandate are stubbed. Enforces two gates: verified-claims and current-customer exclusion. Trigger on: run the sequence, 10-day plan, execution roadmap, outreach plan, daily cadence, strike sequence, full pipeline, run the full engine for [account], build the sequence for [account], launch [account]. Load when an account is ready for outbound."
---

## When this skill applies

- Any request for an outreach sequence, execution roadmap, or daily cadence for an Intradiem account
- Any request to "run the full engine" or "run the pipeline" on a new account
- When an account has a buying committee identified (in Clay or from the engines) and is ready for outbound
- When a single account signal needs to become a coordinated committee play
- Runs for ANY motion. If the motion is not named, detect it from context or ask. Do not default to Star Ratings just because it is the most built-out module.

This skill consolidates what were two separate League skills (full-pipeline and holistic-roadmap) into one engine with a depth toggle. The sequence is the core job. The research orchestration is a mode on top of it, not a separate skill.

## Two run modes

Detect the mode from the request. When ambiguous, default to SEQUENCE and say so.

### SEQUENCE mode (default)
The account and its committee already exist, pulled by the TAM engine, the signal engine, or the Clay Contacts table. This mode goes straight to building the staggered committee sequence with full copy. This is the fast path and the one used most often.

Inputs it expects to already exist: a list of real, validated committee contacts (name, title, tier, email/LinkedIn, verification status), the account's why-now, and the motion.

### FULL mode
The account is new or research is stale. This mode orchestrates the front half first, then hands off to the same sequence builder.

1. Pull the account's strike plan from the TAM engine (`get_strike_plan(domain)` via the intradiem-tam MCP, or read `account_plays.json`). This carries fit score, triggers, personas, and the ROI model output. Treat all dollar/ROI figures from the engine as placeholder assumptions, never as verified numbers (see Verified-claims gate).
2. If the account is an existing customer, pull expansion/risk signals from the signal engine (`get_expansion_signals(domain)` via intradiem-signals). New-logo accounts skip this.
3. Pull the real committee contacts from the Clay Contacts (Buying Committee) table. If the committee is thin (fewer than 6), expand it with a persona pull before sequencing. **Clay-read caveat:** the connected Clay MCP cannot read the built tables when Audiences is disabled for the workspace (`query-objects` and `ask-question-about-accounts` return "Clay Audiences is not enabled for this workspace"). When that happens, do not invent the data. Ask for an export/paste of the rows, or have an admin enable Audiences. Never fabricate a contact, a star level, or a contract count from an unreadable table.
4. Confirm the motion and load its pack from the Motion Registry below.
5. Run both universal gates (verified-claims, customer-exclusion).
6. Hand off to the sequence builder (the same logic SEQUENCE mode runs).
7. Package the outputs (sequence file, committee summary, optional PDF handoff).

Do NOT re-derive research the engines already produce. Read from them. The engines are the source of truth for scoring and committee; this skill is the source of truth for sequence and copy.

## Mandatory skill chain

Fires in this order. Do not skip, do not reorder.

1. **cognitive-calibration** — Fires first, silently. Mode is Build for the sequence structure, then Execution for the copy.
2. **intradiem-verified-metrics** — Load before any claim is written. It gates every stat and proof point against the Value Repository.
3. **intradiem-first-draft-engine** — Before writing ANY copy. Every email, LinkedIn message, and voicemail goes through the prospect-first thinking sequence individually, per contact. No batch-writing.
4. **intradiem-copy-sharpener** — After drafting, to bring every message to send-ready C-suite quality.
5. **intradiem-competitive-intel** — Whenever a competitor is named in the account context (Verint, NICE, Calabrio, Assembled, Playvox, in-house RPA/scripts). Produces the wedge and reframe the copy then uses.

Motion-specific skills load alongside the registry entry (for example intradiem-backoffice-icp for the back-office motion).

## Two universal gates (run on EVERY sequence, every motion)

These are Intradiem company rules, not motion rules. They run regardless of which module is loaded.

### Gate A: Verified-claims gate
Only figures confirmed in the Intradiem Value Repository (`04-value-repository/Intradiem_Value_Repository.md`, surfaced by intradiem-verified-metrics) may appear as Intradiem-verified in prospect copy. Concretely:
- Any ROI, lift, NRR, idle-time, or performance number that is not in the Repository does not ship. No exceptions, no "I remember that number."
- Engine-generated ROI and any `roi_model.json` / `proof.json` / `engine_state.json` figures are placeholder assumptions. Never let them read as Intradiem-confirmed.
- Public math (CMS Star levels, forgone-QBP estimates, cliff counts, a prospect's own operational data, a prospect's own public disclosures) is allowed when labeled as an estimate from public data, with the humility clause that the prospect knows their exact picture better than we do.
- Third-party peer figures (a competitor's or peer's public filing) are allowed as third-party magnitude, attributed and dated, never restated as an Intradiem result. Screen them first for whether the figure actually supports the thesis (see the retired $190M proof under Motion 1 for a cautionary case).
- Mark anything unconfirmed `[UNVERIFIED]` rather than smoothing it into the copy.

### Gate B: Current-customer exclusion gate
The new-logo motions exclude existing customers. Before sequencing, screen every account and contact against the current-customer list. If the flagged customer file or Salesforce read is available, use it as source of truth. As of Jul 2026 the verbal exclusion list for new-logo Star Ratings is: UnitedHealthcare, Humana, CVS/Aetna, Kaiser, Elevance, Molina, Scan Health. Confirmed non-customers include Centene, HCSC, Medica, and the rest of the universe. Existing customers are not dropped from the system; they move to the install-base expansion motion and the account-manager lane, not new-logo outbound.

## Motion Registry

Each motion supplies the concreteness that keeps copy sharp: its why-now triggers, product angle, persona pains, and approved proof source. Pick the motion, load its pack. If a pack is a stub, that is the gap to fill before running, not something to improvise around. A vague motion produces deletable copy.

### MOTION 1 — Star Ratings cliff-edge (POPULATED)
- **Buyers:** payer operations, customer care, member experience, and Medicare operations leaders. See committee tiers below.
- **Why-now triggers:** contracts sitting at 3.5, a half star under the 4.0 bonus line (the fast money); the CMS October ratings release resetting the cliff; the next measurement window open across the current year; forgone Quality Bonus Payments concentrated in the sub-4.0 book.
- **Product angle:** Queue Optimizer (real-time contact-center orchestration) primary; Back Office Optimizer for operations-integration and processing seats.
- **Persona pains:** service levels and admin/experience measures slipping under load; back-office turnaround during peak weeks; the half star decided by execution, not by a scorecard fix after the fact.
- **Approved proof (via Value Repository):** the account's own forgone-QBP exposure, labeled an estimate from public CMS data with the humility clause; the account's own public Stars trajectory as their record (for example Centene's move from ~1% to ~18-20% of members in 4-star plans, 2025 to 2026); the largest single sub-4.0 block named accurately from the public CMS release; and the closing measurement window (the next rating is being set across the current year) as the urgency. No Intradiem outcome claims, none verified yet.
- **Retired proof point — do not reintroduce:** the UnitedHealthcare $190M court figure was removed as a default in Jul 2026 after review. The case is one UnitedHealthcare WON by arguing the measure was applied unfairly (a single disputed secret-shopper call), so to a Medicare-quality leader it reads as evidence the measure is arbitrary and litigable, not that operational execution moves the rating, and the copy had to disclose the measure retires for 2028, undercutting its own proof. If a peer-magnitude figure is ever wanted, source one where the payer's own operational execution drove the dollars, and clear it through verified-metrics first.
- **Star-level precision:** a half star means 3.5, one half step under the 4.0 line. A 3.0 contract is a FULL star under; name it as the largest block or the biggest prize, never as "half a star." Do not conflate a single measure's star (for example Customer Service at 3.0) with the overall-rating gap to 4.0. The 3.5 contracts are the fast money; the 3.0-and-below blocks are the bigger prize and the bigger climb.
- **Count-safe rule:** never assert an unverified hard contract count in prospect copy ("seven contracts"). Keep it count-safe ("a cluster of near-line contracts," "the contracts sitting at 3.5") unless the exact count is confirmed against the live CMS Star Ratings file or a Clay export. The public web tools do not return a contract-by-contract count; the authoritative source is the CMS 2026 Star Ratings data file or the Clay table.
- **Exclusions:** the current-customer list in Gate B.
- **Source files:** the tiered CMS universe file, the Clay Contacts (Buying Committee) table, the Value Repository.

### MOTION 2 — Back-office expansion / BOO launch (STUB — populate before running)
- **Buyers:** claims operations, shared services, document processing, payment operations leaders.
- **Why-now triggers:** backlog growth, cost-takeout mandates, BPO/vendor changes, processing SLA pressure.
- **Product angle:** Back Office Optimizer.
- **Proof:** TBD from the Value Repository as BOO material lands. Do NOT ship a back-office outcome number until it is in the Repository.
- **Load alongside:** intradiem-backoffice-icp (ICP straw-man, persona pain maps, qualification and dedup rules). Gated on the Scott Kemme ICP conversation.

### MOTION 3 — Install-base expansion & risk (STUB — existing-customer lane)
- **Buyers:** existing-customer economic buyers and champions, worked through the account-manager lane (Mary Ann, Rachel), not new-logo outbound.
- **Why-now triggers:** from the signal engine. Expansion: seat utilization, coaching coverage, rule-engine active, CRM not connected. Risk: automation volume drop, champion job change.
- **Product angle:** Queue Optimizer expansion, Back Office Optimizer, the DWO platform.
- **Note:** this is the one motion where existing customers are IN scope. Gate B routes here rather than excluding.
- **Source:** signal-engine outputs (`get_expansion_signals`).

### MOTION 4 — Competitive displacement (STUB)
- **Trigger:** a competitor named in the account context (Verint, NICE, Calabrio, Assembled, Playvox, in-house RPA or scripts, or status quo).
- **Product angle:** the DWO platform, positioned against the named incumbent.
- **Load alongside:** intradiem-competitive-intel for the wedge, reframe, and trap-setting talking points the copy then uses.

### MOTION 5 — Cost-mandate / efficiency (STUB)
- **Why-now triggers:** layoffs, cost-takeout, margin pressure, hiring freeze, capacity-without-headcount mandates.
- **Product angle:** Queue Optimizer plus Back Office Optimizer, framed as capacity gained from existing headcount.
- **Guardrail:** do NOT use any idle-time percentage or unverified efficiency stat (blocked in the Value Repository). Frame from the prospect's stated pressure, not a manufactured idle number.

**Scope reminder for all motions:** Intradiem sells Dynamic Workforce Orchestration across contact centers AND back offices, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities). Never frame it as just a call-center tool.

## Intradiem buying committee tiers

Adapt the committee to Intradiem's operations buyers. Every identified member across the tiers gets full touchpoints. Target 6-12 contacts; never fewer than one clear owner per tier that exists at the account.

- **Tier 1 — Champion / floor owner:** VP or Director of Contact Center Operations, WFM leaders, CX Operations. They feel the pain daily and own the floor. Outreach focus: operational relief when volume spikes, execution holding under load.
- **Tier 2 — Economic buyer:** CFO, VP Finance, COO, SVP Operations, VP Customer Care. Controls budget. Outreach focus: cost of the status quo, capacity without headcount, the dollars tied to the outcome (from public or prospect data, never an unverified Intradiem number).
- **Tier 3 — Technical / enablement:** CIO, VP IT, WFM/CCaaS platform owners, automation or RevOps leads. Validates feasibility and integration. Outreach focus: fit alongside existing WFM/ACD/CCaaS, the gap between forecast and floor, real-time signal-to-action.
- **Tier 4 — Executive sponsor:** COO, Chief Customer Officer, Chief Operations Officer, and for payers the Stars or Quality executive. Final organizational validation. Outreach focus: the enterprise outcome and the size of the exposure.
- **Tier 5 — Operational / pain layer:** Sr Directors and Directors of Operations, Member/Customer Service, Claims Ops, Medicare Ops, back-office processing. They live the pain and their validation accelerates the committee. Outreach focus: the specific daily friction they own.

**Contract-specific vs company-level messaging:** default to a company-level narrative for enterprise seats. Go contract-specific only where a leader clearly owns a specific contract or book (for example a Sr Director of Medicare Operations on a named sub-4.0 contract). Do not claim to know who owns which contract when you do not. Keep the "you know your book better than I do" humility on that one contract-specific seat, not on every contact (see Copy standards).

## Cadence: the validated core and the extended arc

The default and validated standard is a **five-touch, multi-channel cadence across about nine business days** from each contact's entry day. This is the structure the Centene Star Ratings reference sequence was built and stress-tested on across two premortem rounds. Use it unless the account warrants heavier pursuit.

### Five-touch core (per contact, from their entry day)
- **Touch 1 (Day 1):** Email 1 — the why-now plus one persona-specific hook, one CTA that names the payoff.
- **Touch 2 (Day 2):** LinkedIn connection request — carries the opener; leads the sequence if the email is still validating in Clay.
- **Touch 3 (Day 4):** Voicemail + a LinkedIn message the same day — different channels, same day; the LinkedIn note is the text TL;DL of the voicemail.
- **Touch 4 (Day 6):** Email 2 — a genuinely new second angle (the closing measurement window for Stars), never a recycled Day 1.
- **Touch 5 (Day 9):** Breakup email — the highest-open touch; end on a sharp parting idea, never a shrug.

### Extended arc (optional, must-win contacts only)
For a top-priority contact, extend into the fuller escalation ladder before the breakup: add phone call #1 (full script), phone call #2 (shorter), and a pattern-interrupt touch (different channel or format), then a hail-mary email with the sharpest distilled thesis. The order is sacred: soft → moderate → direct → persistent → nuclear. A contact who enters late runs past calendar Day 9; the calendar extends, the order never inverts to fit a window. Never place a nuclear step before a direct or persistent step to hit a date.

### Staggered committee entry
Stagger so a consistent why-now narrative surfaces inside the account within a week without looking like a blast.
- **Day 1:** the highest-probability contacts and the Tier 5 operators who feel the trigger daily.
- **Days 2-3:** remaining technical/enablement and operational contacts. Entering after Day 1 avoids the coordinated-spray look.
- **Days 3-5:** Tier 4 executive sponsors, after champion-layer contacts have had time to mention the outreach internally.
- Any contact whose email is still validating in Clay leads with the LinkedIn connect so the thread does not go cold, and the queued email fires on validation.

### Deliverability guardrail
Multiple similar-topic emails into one corporate domain in a week can trip spam filtering or IT pattern-flags, which caps read rate before copy quality matters. Lean on the staggered entry, vary subject lines across contacts (never the same subject to five people), stagger send hours within a day, and let the LinkedIn touch carry the opener when an email is at deliverability risk. Deliverability is the one lever largely outside your control; plan around it rather than assuming clean inbox placement.

## Copy standards (Intradiem house style)

Every message must pass these before it ships. Hardcoded.

- **Verified claims only.** Gate A applies to every sentence. Public/prospect math is labeled an estimate with the humility clause. No unverified Intradiem outcome, ever.
- **No em dashes.** Periods and commas only.
- **No AI-isms and no filler.** Cut leverage, synergy, seamless, robust, transform, empower, best-in-class, cutting-edge, comprehensive, innovative, paradigm, catalyst. No self-narration, no "I help organizations," no "companies like yours," no "compare notes / trade notes / pick your brain / touch base," no "I would value / I'd value ___ minutes" (seller-want CTA). Contractions always; natural CTA patterns per the first-draft-engine ("Thought it might be worth finding time to ___. Have 15 minutes ___?").
- **Prospect is the hero.** The meeting is their idea. Feel, do not tell. Describe a situation the prospect self-selects into rather than accusing them of a problem.
- **DWO framing.** Contact center and back office, never just a call center.
- **Brand-light early.** Keep the sender in the background; the copy carries weight from the prospect's own math and their own public record, not from a pitch.
- **CTA names the payoff, per persona.** One clear ask per message, soft early and confident late. Never a generic ask repeated across the committee ("twenty minutes to compare notes" to five people is a fail even though "compare notes" is already banned). Each CTA states what THIS contact gets from the call in their language: where a plan their size loses the half star, what holding the next half point costs versus returns, where the integration-to-staffing lag is widest, which measures are most exposed, which specific contracts still move. Vary the ask across contacts and across a contact's own touches.
- **One specific, verifiable hook per contact (research inventory).** Before writing each contact, name the single detail that proves you know their world: their plan (Carolina Complete Health), their public trajectory, their exact seat's measures, their named book. Write from that detail, not the account-level narrative. Smart-generic gets a polite ignore; account-specific earns a reply.
- **Humility dosage.** The "you know your book better than I do" clause appears at most once across the committee, on the contract-specific seat where it is warranted. Everywhere else, invite their number without self-deprecating. Five humility clauses to five senior people leak status and are a template fingerprint.
- **Breakups earn their open.** Touch 5 is the highest-open touch. End on a sharp parting idea (for Stars, "the cheapest half star they will ever buy back"), never a passive "glad to help whenever."
- **{{sender}} token.** For reusable sequences, use `{{sender}}` in every signature and in each voicemail intro ("this is {{sender}} with Intradiem"), so the sequence ports across reps without a rewrite.
- **Every voice note has a text TL;DL** (2-3 sentences), delivered as the same-day LinkedIn message.
- **Word counts:** cold email 80-120, follow-up 100-150, LinkedIn message 40-80, voicemail 45-70.

## Prospect response simulation (do not skip)

After all copy is drafted, read each message AS the specific contact, on a Tuesday, between meetings, and ask only: would I reply to this? Not "is this good copy." If the answer is "maybe" or "it's fine," that is a no. Diagnose why (one-way value, over-explaining to an expert, teaching a stranger, vague or interchangeable CTA, obvious pitch setup, template sameness, status-leaking humility) and rewrite through the first-draft-engine, not with a one-line patch. Run this with equal rigor on the last contact as the first; the batch-generation trap is that rigor decays as volume grows, and the later contacts are often the ones who tip the committee.

## Quality gate

Before saving, check the whole document:
1. Every committee contact has the full five-touch arc (or the extended arc, if used) in correct escalation order.
2. Both universal gates pass: no unverified claim (Gate A), no current-customer in a new-logo sequence (Gate B).
3. No em dashes, no forbidden words, no self-narration anywhere.
4. No two contacts open the same way and no two share a CTA (template-creep guard). The humility clause appears at most once across the committee.
5. Every voicemail has a same-day LinkedIn TL;DL. Word counts within spec.
6. Touch 4 introduces a genuinely new angle, not recycled Touch 1 material. Touch 5 ends on a sharp parting idea.
7. Star-level precision holds (3.5 = half star; 3.0 = full star, named as the largest block). No unverified hard contract count.
8. Every contact block starts with `### N. Full Name -- Title`. Every touch has a `**Touch N (Day X) --**` header.
9. `{{sender}}` used for the sender name if the sequence is meant to be reusable; otherwise the real rep name is filled. No other placeholders. Send-ready.

## Reference example: Centene Star Ratings (the 10/10 standard)

This is the built, twice-premortemed sequence that defines the quality bar. The full five-contact file lives as `StarRatings_Centene_StrikeRoom_Sequence_FINAL.md` in the account folder. Two contacts are embedded here as the canonical example: Corey Taliaferro (company-level, Tier A) and Jesse Lewis (the one contract-specific seat). Match this energy, length, specificity, and CTA discipline on every sequence.

**Account snapshot (abbreviated):** Centene, confirmed non-customer, overwhelmingly sub-4.0 Medicare book under the Wellcare brand (portfolio average ~3.39, ~a fifth of members in 4-star-or-better plans). Public trajectory: ~1% to ~18-20% of members in 4-star plans, 2025 to 2026, a turnaround the CEO put on record. Fast money is the contracts at 3.5; largest single block is Wellcare by Fidelis Care, ~69k members at 3.0 overall (full star under, the biggest prize). Forgone QBP across the sub-4.0 book ~$76M (estimate from public CMS data). Count of 3.5 contracts stays count-safe until confirmed from the CMS file or Clay.

### Company-level example — Corey Taliaferro, VP Health Plan Operations (Carolina Complete Health), Tier A

**Touch 1 (Day 1) — Email** Subject: the half star lives on the floor

Corey, running Carolina Complete Health's operations, you already know the half star between a near-line contract and the 4.0 bonus is not won in the scorecard. It is won on the floor, in the weeks volume runs hardest and service either holds or slips right when the measures are watching. Across Centene's sub-4.0 book that gap models to roughly $76M in forgone Quality Bonus Payments from public CMS data, and the fastest of it is the contracts already sitting at 3.5.

Intradiem runs workforce orchestration across the contact center and the back office, acting on real-time conditions so quality does not dip under load. I can show you where a plan your size typically loses that half star before the next measurement window closes. Worth twenty minutes?

{{sender}}

**Touch 2 (Day 2) — LinkedIn connection request** Corey, I work the operations side of health plan Stars, the gap between what the scorecard measures and what happens on the floor when volume spikes. Given you run Carolina Complete Health's ops, would value connecting.

**Touch 3 (Day 4) — Voicemail** Corey, this is {{sender}} with Intradiem. I sent you a note on the half star between Centene's near-line contracts and the 4.0 bonus, and why most of it is decided on the operations floor during peak weeks. I can show you where a plan your size usually loses it before the next window closes. I am at [number], or reply to the email. Thanks Corey.

**Touch 3 (Day 4) — LinkedIn message** Corey, left you a voicemail too. Short version: the fastest Star money for Centene is the contracts already at 3.5, and whether they clear is an execution question during peak weeks. I can show you where that gap opens for a plan your size. Twenty minutes?

**Touch 4 (Day 6) — Email** Subject: the window is more than half gone

Corey, the reason this is a now question and not an October one: the measurement that sets the next rating is running across this year and is already more than half spent. Every peak week without the operational piece in place locks more of the next cliff in before the ratings ever publish. The contracts at 3.5 are the ones where that still swings your way if execution holds.

That is what Intradiem is built to hold steady under load. Twenty minutes and I will walk the specific points in a peak week where that half star is usually won or lost.

{{sender}}

**Touch 5 (Day 9) — Email** Subject: leaving it here

Corey, I will stop here. One parting thought: the contracts at 3.5 are the cheapest half star Centene will ever buy back, and the window to move them is the peak weeks between now and the next measurement close, not the October release. When that lands on your desk, the workforce-execution angle is where I would start. Glad to help whenever it is useful.

{{sender}}

### Contract-specific example — Jesse Lewis, Sr Director Medicare Operations, Tier 5 (the one seat cleared to name the Wellcare cliff)

**Touch 1 (Day 1) — Email** Subject: the Wellcare contracts closest to 4.0

Jesse, since you own Medicare operations I will be specific. By our estimate from public CMS data, the Wellcare book carries roughly $76M in forgone Quality Bonus Payments across its sub-4.0 contracts. The fastest to recover is the set sitting right at 3.5, a half star from the bonus; the largest single block is Wellcare by Fidelis Care, around 69,000 members at 3.0 overall, a bigger climb but the biggest prize. You will know the exact picture better than I will.

On the contracts closest to the line, the gap is largely execution: whether service and back-office turnaround hold during peak weeks. Intradiem orchestrates the contact center and back office off real-time conditions so they do. Twenty minutes on the specific Wellcare contracts nearest the line and which measures still move them?

{{sender}}

**Touch 2 (Day 2) — LinkedIn connection request** Jesse, reached out on the Wellcare contracts closest to the 4.0 line. Would value connecting here too.

**Touch 3 (Day 4) — Voicemail** Jesse, this is {{sender}} with Intradiem. I sent a note on the Wellcare contracts closest to the 4.0 line, the 3.5 set that is the fastest bonus money, plus Fidelis as the largest block, and how much of it comes down to execution holding during peak weeks. Twenty minutes on the ones nearest the line? I am at [number]. Thanks Jesse.

**Touch 3 (Day 4) — LinkedIn message** Jesse, left you a voicemail too. Short version: the half star on the Wellcare contracts nearest 4.0 is an execution question, and closing that gap in real time is what Intradiem does. Twenty minutes on the ones nearest the line?

**Touch 4 (Day 6) — Email** Subject: the next rating is being set now

Jesse, one point on timing for the Medicare book specifically. The measurement that sets the next rating is running across this year, so the Wellcare contracts nearest 4.0 are being decided right now, in the peak weeks between now and year end, not on the October release. Every week execution holds is a week toward clearing the line; every week it slips is priced into the next cliff.

Intradiem makes that execution consistent under load. Twenty minutes and I will walk the Medicare-operations view on the contracts nearest the line.

{{sender}}

**Touch 5 (Day 9) — Email** Subject: leaving it here

Jesse, I will stop for now. One parting thought: the 3.5 contracts are the cheapest half star on the Wellcare book to buy back, and Fidelis is the biggest single prize behind them, both decided in the peak weeks happening now. When protecting them becomes a priority, the workforce-execution angle is where I would start. Glad to help whenever the timing is right.

{{sender}}

### Why this set is the bar
- **Every CTA names a different payoff** (where a plan your size loses it; the specific Wellcare contracts and which measures move them). None is an interchangeable "compare notes."
- **One specific hook per contact.** Corey's opener uses that he runs Carolina Complete Health; Jesse's uses the named Fidelis block and the 3.5-vs-3.0 distinction.
- **Humility used once.** Only Jesse, the contract owner, gets "you will know the exact picture better than I will." Corey does not defer.
- **Touch 4 is a new angle** (the closing measurement window), not a restated Touch 1.
- **Breakups end on a sharp idea** ("the cheapest half star they will ever buy back"), not a shrug.
- **No unverified Intradiem number, no $190M peer figure, star-level precision holds, count stays safe.**

## Output

Save a single .md file to the account folder: `[Account]_Strike_Sequence.md` (or `[Account]_StrikeRoom_Sequence_FINAL.md` for a finalized, reusable version).

```markdown
# [Account] Strike Sequence — [Motion]
Motion: [motion] · Mode: [Sequence/Full] · Built: [date] · Status: send-ready draft, human approval gate not yet cleared

## Account snapshot
[Why-now, the exposure or trigger with sources, public trajectory, customer status]

## Buying committee (real contacts)
| # | Name | Title | Tier | Email status | Angle |

## What reps can and cannot say
[The verified-claims guardrail in rep-facing form: say / do not say]

## Cadence and committee choreography
[The five-touch core + staggered entry + deliverability note]

## Sequences
### 1. Full Name -- Title
**Touch 1 (Day 1) -- Email** ...
**Touch 5 (Day 9) -- Email** ...

## Objection quick-handles
## Claims basis
```

Use `{{sender}}` for the sender name when the sequence is meant to be reusable across reps. FULL mode also produces a committee summary table and, on request, a branded PDF handoff (via the pdf skill and the CURRENT Intradiem brand kit, Roboto system: forest `#014637`, green `#2DB56E`, `#F58220` as the action accent only, official inline SVG logo; see the `## Brand` section of CLAUDE.md. Never the personal blurple/creme palette on Intradiem work, and never the retired `#FE5000` kit).

## What this skill does NOT do

- It does not invent research the engines already produce. In FULL mode it reads from the TAM engine, signal engine, and Clay; it does not re-score accounts, and it does not fabricate data a disabled Clay table will not return.
- It does not send anything. Every output is a send-ready draft that stops at the human approval gate. Nothing goes to a prospect from this skill.
- It does not ship an unverified Intradiem number, or a peer figure that undercuts the thesis, to clear a gap. If the proof is not in the Value Repository, or does not actually support the argument, the claim does not appear.
- It does not assert a hard contract count or a star level it has not verified. Count-safe until confirmed.
- It does not default to Star Ratings. The motion is chosen per run; Stars is simply the first fully-built module and the source of the reference example.
