# Arsenal & Rollout Playbook
**Dallas Andrews · GTM Engineer · Intradiem · internal operator's manual**
*Built Jun 29, 2026. Private. This is the single map of everything you have, why each piece matters, where it sits in the grand plan, and the order to introduce it. Not for external eyes (it names your private tracker and your premortem fears).*

---

## 0. How to read this

Three layers stack here. The **thesis** (what the engine is). The **arsenal** (every asset you've built, grouped by the job it does). The **rollout** (what you introduce, when, and to whom). If you only internalize one thing: you already won the build, so the next 90 days are about sequencing and co-ownership, not construction. Introduce assets as they earn their place, never all at once.

---

## 1. The grand-scale picture

**The thesis Intradiem handed you (Sections 05/07 of the onboarding site):** "Pipeline is no longer a sales activity, it is a system output." The job is to move every row from manual to automated: lists, enrichment, scoring, personalization, central pipelines, experiment loops, signal-based outreach. The thing you build everything on is the **Golden List**: a live, enriched, scored account-intelligence layer that every campaign, sequence, and agent runs off.

**The governing principle (your spine, baked into every tool):** measurement before volume, ICP before sourcing, human before send. You are the owner who designs the motion; the team are the operators who run it. "Done" means the team runs it without you, not "works when Dallas runs it."

**The two-motion sequencing logic (why order matters):** your two motions have opposite dependency profiles. Net-new outbound (Star Ratings into MA payers at the bonus cliff) runs on *external* data you control Day 1. Install-base expansion (200 back-office contacts inside existing customers) runs on *internal* product-usage data owned by other teams and gated by governance. So you lead with net-new as the visible wedge and run install-base as a parallel access-and-relationship campaign. You never stake your first 90 days on data you do not yet control.

**The posture (Naveen's welcome email):** the Q3 numbers are a "rough sketch" to shape together, not commitments to defend. Walk in recruiting co-owners. The win is political, not technical. The technology is done.

---

## 2. The arsenal, by layer

Everything you've built, organized by the job it does. For each: what it is, why it matters, what it serves.

### Layer 1 — Intelligence (the data spine, your two MCPs)

**`intradiem-tam` connector.** Your TAM and strike engine. Returns scored strike accounts (`list_strike_accounts`), the full per-account strike plan with committee and ready sequences (`get_strike_plan`), and seller-scoped views (`accounts_for_seller`).
*Why it matters:* this is the live Golden List's account-scoring and rep-prioritization backbone. The 15-meeting goal sources from here.

**`intradiem-signals` connector.** Your install-base sensor. Monitors customer accounts (`list_monitored_accounts`, `add_monitored_account`), scores expansion / adoption / risk signals (`score_all`, `get_expansion_signals`).
*Why it matters:* this is the install-base half of the engine. The `crm_not_connected` signal is literally the back-office wedge behind the 200-contact goal.

### Layer 2 — The Golden List surfaces (the live account-intelligence layer made visible)

**`golden-list` artifact.** The live strike board. New-logo accounts scored by fit and why-now, plus monitored accounts with firing signals. Click any row for the full strike plan.
*Serves:* Section 05 Golden List + the 15-meeting goal.

**`control-plane` artifact.** The activation and white-space board. Every customer's adoption gaps, expansion openings, and churn risk, each paired with a recommended play and an in-product message, filterable.
*Serves:* Goal 4's control plane + in-product messaging, and the install-base white-space behind the 200 back-office contacts.

### Layer 3 — The orchestration engine (`gtm-cohesion-layer/`, the connective tissue)

This is what turns separate tools into one motion. It is the real engineering depth, and most of it is invisible in a demo.

**`engine_state.json`.** Single source of truth. Every dashboard reads it, which kills drift.
**`conductor.py`.** The 7-stage weekly conductor: spec reread (anti-drift) to rescore to signals to draft to critic gate to human gate to deliverability-gated send. Fail-closed. This is "10x throughput as one weekly push."
**The critic gate (Stage 4b).** An objective screen (deliverability, ICP, in-scope motion, verified-claims, length) that holds bad drafts *before* the human queue. Maker is not checker.
**The guardrails.** WIP-of-one (only one motion scales at a time), throughput-by-operator (alarms if your share of sends exceeds 20%), operator-test (a motion is only "operable" after the team runs it twice without you).
**The preflight gate.** `conductor.py --preflight` physically blocks live operation until the four go-live blockers clear. Those four (attribution ratified, baseline set, deliverability green, security audit current) ARE your Jul-6 checklist.
**`Clay_Build_Pack.md`.** Click-by-click Clay rebuild in about two hours once you have a workspace: tables, enrichment waterfall, fit/intent/grade formulas, signal columns, source-tag writes, webhooks.
**`Attribution_Loop_Spec.md` + `attribution_dashboard.html`.** The reply-sync agent and two-motion funnel. The credit keystone.
**`approval_queue.html`.** The human approve/edit/reject workbench, with draft-acceptance tracking (clean accepts vs rewrites tells you if the engine is actually saving work).
**`deliverability_monitor.html`.** The P1 send-gate (warmup, rotation, spam/blacklist).
*Why this layer matters:* it is the proof you are a GTM *engineer*, not a prospector with good tools. It is also your defense against every premortem failure mode.

### Layer 4 — The activation surfaces (front doors)

**`command-center` artifact (canonical).** The single front door. Acquisition + install-base funnels in one view, plus the merged engine controls (gates, critic, draft acceptance, the shared engine-sourced scoreboard). Open this first in any walkthrough.
**`strike-room` artifact.** Per-account digital sales room. Pick an account and it builds the pitch from the live plan: snapshot, ROI, triggers, committee, copy-ready sequences. The "custom demo per meeting" tool.
**`roi-calculator` artifact.** Idle-labor recovery math with every assumption exposed, so it survives a CFO. Loads a real account for cross-check.
**`dallas-mission-control` artifact (PRIVATE, never show anyone).** Your behind-the-curtain tracker: mandate progress, relationship health, promise ledger, the outside-read sensor, the grooming guardrail. This is your cockpit, not a deliverable.
**`intradiem-day1-audit-console` artifact.** Day-1 Salesforce audit console. Refit it against the real SF schema on Day 1; it runs on guessed objects until then.

### Layer 5 — The skills (your reusable plays)

Intradiem-specific: **`intradiem-verified-metrics`** (citation discipline, the source of truth for any number you quote), **`intradiem-signal-to-play`** (one account signal becomes synchronized marketing + sales + outreach), **`intradiem-roi-business-case`** (CFO economic impact statement from call data), **`intradiem-competitive-intel`** (Verint/NICE/Calabrio displacement, always positioned as the layer you sit on top of, never competitors), **`intradiem-content-engine`** (one asset becomes a full multi-channel content set for marketing).
Meta-skills: **`cognitive-calibration`** (runs before every output), **`strategic-premortem`** (before irreversible moves), **`ai-readiness-assessment`**, **`weekly-portfolio-prioritization`**, **`schedule`**, and your two brand skills (**`dallas-brand`** internal, the official green Intradiem kit external).
*Note:* the `league-*` skills are a transferable pattern library from your last role, not for Intradiem use. Mine them for structure, do not run them as-is.

### Layer 6 — Automation (the cadence that runs without you)

**`daily-signal-scan`** (weekday 7am): ranked briefing of who to work that day. **`weekly-gtm-conductor`** (Mon 8am): preflight + conductor run + Command Center refresh. Both dry-run/seeded until Jul 6.
*Why it matters:* this is the proof the motion runs whether or not you are watching it.

### Layer 7 — The canon (docs that govern the work)

`Q3_Bulletproof_Operating_Plan.md` (the plan, read first), `GTM_Engine_Build_Spec.md` (the Golden List schema), the three cohesion-layer specs/runbooks, `Naveen_Walkthrough_Talk_Track.md` (your Day-1 screen-share script), and this playbook.

---

## 3. How the arsenal maps to your four mandates

| Mandate (provisional, to co-shape) | Assets that serve it | The leading indicator you own |
|---|---|---|
| 15 vetted new-logo meetings | intradiem-tam, golden-list, strike-room, roi-calculator, Star Ratings motion | Qualified replies sourced (upstream of the meeting, which lives in reps' hands) |
| 10x BDR messaging throughput | conductor.py, approval queue, deliverability monitor, daily-signal-scan | Qualified replies per week, gated by a deliverability floor |
| 200+ back-office contacts | intradiem-signals, control-plane, Clay Build Pack | Qualified contacts sourced and source-tagged (yours regardless of product timing) |
| Build + maintain the engine | the entire cohesion layer + the documented motion | The engine running operable by a non-Dallas operator |

The pattern: for every mandate that ultimately lands in someone else's hands (meetings depend on reps, back-office meetings depend on BOO GA), you instrument the leading indicator *you* control and steer Naveen toward grading you on that.

---

## 4. The rollout sequence (what to introduce when, and to whom)

The discipline: introduce alignment first, then one motion, then expansion. Tools are revealed as they earn their place, never dumped.

### Pre-Day-1 (now to Jul 6) — freeze and rehearse
Introduce nothing. Rehearse the Naveen talk track to a memorized 3-point flow. Eyeball the reskinned green artifacts once. Confirm laptop with Chris and first-day logistics. Resist building. Every new tool now anchors you to assumptions Naveen said he wants to shape with you.

### Day 1 — the do-nothing-else move + the optional walkthrough
The single move: open the attribution conversation with Naveen, collaboratively. "Here's how I'd love for us to define what good looks like together." Get agreement that the engine is credited at the qualified-reply / meeting-sourced line, the three Salesforce fields (`gtm_engine_sourced`, `source_motion`, `sourced_date`), and one baseline. Stand up contact-level source tagging before any volume.
The walkthrough (only if the moment invites it, per the talk track): Command Center first, then golden-list, strike-room, roi-calculator, control-plane, daily-signal-scan. Posture: working prototypes to think with, not a plan of record. Confirm data shareability before any screen-share.
*Introduce to Naveen only. Nothing to reps or marketing yet.*

### Week 1 — orient, listen, secure air cover
Get Naveen's real org map and the gap he most wants closed. Co-define success and attribution (the keystone). Define the back-office ICP with Scott Kemme before sourcing anything. Get access (Clay, Salesforce, squad Slack, the CMS list, Nate's sending setup) and read before touching. Refit the day1-audit-console against the real Salesforce schema and confirm the attribution fields exist or flag them as a build.
*Introduce: Command Center to Naveen as the shared scoreboard. Begin the Scott Kemme ICP partnership. Open procurement for Clay/Apollo now (longest pole).*

### Weeks 2 to 4 (the first 30) — build the Golden List, pilot net-new
Stand up Golden List v1 from the spec (back-office market + existing Star Ratings list). Recruit Nate as rep number one for the net-new pilot, his calibration and your infrastructure. Launch outreach small: three variants per segment, tracked, human approval before send. Stand up deliverability infra first. Build the instrumentation dashboard (enriched to sent to open to replies to qualified replies to meetings, split by motion, source-tagged).
*Introduce: strike-room and golden-list to Nate. roi-calculator into the first live meetings. Deliverability monitor and approval queue as the send discipline.*

### Weeks 5 to 6 (30 to 60) — iterate and turn the motion weekly
Kill underperforming variants, scale what converts. Move Star Ratings from one-time send to weekly cadence (this shift *is* the 10x). Define 10x as qualified replies per week gated by a deliverability floor. Build the first follow-up agent. Run back-office contacts into install-base campaigns.
*Introduce: the weekly-gtm-conductor live as the standing team motion. attribution dashboard live. control-plane to whoever owns CSM/expansion + Sierra in marketing.*

### Weeks 7 to 8 (the blueprint moment) — present and expand
Present pipeline and learnings with the dashboard, provable and source-tagged. This is the "the team that pilots it becomes the blueprint for Intradiem globally" moment. Expand the model across the team. Run the operator-test: the motion only counts as done when a non-Dallas operator runs it twice without you.
*Introduce: the documented engine to the broader team. intradiem-content-engine to Sierra/marketing for volume.*

### Days ~57 to 90 — compound and prove the repeat
Reps work replies; you keep volume flowing and enable reply-handling. You do not personally chase meetings. Day-75 tripwire: if you are not near 10 of 15 meetings, escalate and renegotiate, do not discover it at QBR. Package the whole motion as the documented, repeatable engine. That is Goal 4 and the proof-of-work artifact that travels with you.

---

## 5. Sequencing traps (what NOT to do)

- **Do not dump twelve tools on Naveen Day 1.** Lead with listening and the attribution conversation. The walkthrough is six artifacts, framed as prototypes, only if the moment invites it.
- **WIP-of-one.** Only Star Ratings scales first. Back-office stays in backlog until the ICP is defined with Scott Kemme and BOO is sellable. Your own guardrail enforces this; respect it.
- **Never scale volume before deliverability and attribution are green.** This is the failure that poisons your 157 warm contacts. The preflight gate exists to stop you.
- **Confirm data shareability before any external screen-share.** The artifacts pull real-looking account and seller names from the connectors.
- **Mission Control stays private.** Never show Naveen or anyone the behind-the-curtain tracker. It names your relationship reads and your over-promise risks.
- **Do not introduce the install-base motion as your credibility wedge.** It depends on data you do not control yet. Net-new leads.

---

## 6. One thing to verify Day 1 (cast reconciliation)

Your earlier `Grand_Strategy` and `First_Two_Weeks` docs name a stakeholder cast (CRO John Norton as sponsor, Kevin Wilson CTO, Cheryl Eckel PMM, Genna on Sales Ops) that predates your confirmed Q3 reality. The confirmed cast is: **Naveen Thilagan** (your manager and exec sponsor, Director Product Strategy), **Nate Belfield** (Sales, runs current Star Ratings outbound, your closest collaborator and the credit-risk relationship to manage), **Genna** (Sales), **Sierra Jones** (Marketing), **Tom Russell** (Market readiness), **Scott Kemme** (Business, your back-office ICP partner), **Chris Busbee** (Product, controls BOO GA). The dependency *logic* in the older docs (recruit co-owners, net-new wedge first, procurement is the long pole, make owners feel like authors) is still right. The named org chart is not confirmed. Walk in and fill in the real map from Naveen on Day 1; do not cite interview-era names as fact.

---

*If you want a Naveen-facing or team-facing cut of this later, it is a subset of this document with the private cockpit, the premortem fears, and the cast-reconciliation section removed.*
