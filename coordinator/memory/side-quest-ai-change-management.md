---
name: side-quest-ai-change-management
description: "Board-visible side quest, AI-powered change management program piloted on internal Greenlight usage, $10K/person bonus, due Dec 31 2026"
metadata: 
  node_type: memory
  type: project
  originSessionId: beb4c19e-5686-4930-ba34-aa727395eb20
  modified: 2026-08-05T20:03:44.895Z
---

Dallas joined as third member of the AI Change Management side quest (recruited Aug 4 2026 via call; JD suggested his name).

**Team:** Joey Fogle (SM project lead; started Dec 2025, ex-sports/marketing background, Tampa, Eastern time, no Claude license), Catherine Anderson (VP Legal, holds change management certifications), Dallas. Joey is holding the current charter back until it's realigned on scope and measurables; Dallas builds from scratch, charter edits wait for Joey's revised draft.

**Stakeholders:** Derek Eck (VP Customer Experience, sponsor), Jen East (primary stakeholder, determines bonus payout against the submitted success criteria), Jen Lee (originator; project has board visibility from the senior leadership offsite), Jason (Manager AI Enablement, Greenlight owner, key partner), JD = Jason Dowden. A new director under Jason starts mid-Aug 2026 and will have a voice; Jason confirmed the project continues as planned.

**Scope:** Build an AI-powered change management program (framework + data-triggered intervention playbooks + light software: dashboards, reporting, message delivery). Prove it internally using Greenlight usage data as the proving ground, with the external/productized view as the final output. Explicitly NOT a change to the Intradiem product or V11. Long-term: standalone service/product customers could use for any AI tool, even non-Intradiem.

**Constraints:**
- No ProSci/ADKAR language (copyright risk if productized); Catherine gates legal language.
- Success criteria in the side-quest form must be deliverable-based and vague on metrics per Derek: whatever is written is what Jen East pays out against. Adoption-lift targets vs baseline were scrapped (no proven baseline exists for a brand-new framework).
- Not a formal pilot/control-group design; internal proving ground.
- Jason's hosting rule applies: anything hosted for the team must run standalone, no Claude calls at runtime.
- Deadline Dec 31 2026. $10K/person spot bonus. Form was due ~Jul 1, so team is about a month behind; speed is the defense against the new-director reframe risk.

**Status Aug 4 2026:** Dallas messaged Jason on-call for Greenlight backend user-level usage reporting/access; Jason confirmed internal employee reporting exists (daily/weekly, user-level scorecards, integrating with Claude and Zuar). Joey is revising the project charter (Catherine's Claude first pass) and scheduling a 3-way meeting this week, then likely a Jen East meeting before form submission. Matt Graves (SM boss) precedent: Claude-built adoption reports now connected to Zuar.

**Phase 0 built Aug 4 2026** in `~/Desktop/Intradiem Deliverables/AI Change Management Side Quest/`:
1. `01_Momentum_Framework_v0.html`: clean-room framework, working name **Momentum (Dynamic Adoption Orchestration)**. Three layers (Signal/Decision/Action), five-stage Momentum Loop (Baseline, Signal, Intervene, Reinforce, Compound), five behavior-inferred adoption postures (Dormant, Skimming, Building, Fluent, Multiplier), seven-measure vocabulary. Clean-room statement + Catherine review checklist included; naming needs her trademark screen.
2. `02_Intervention_Playbooks_v0.html`: 7 trigger families (T1 cold start, T2 dormancy, T3 decay, T4 shallow use, T5 launch moment, T6 momentum win, T7 non-response) x 3 altitudes (user/manager/exec), 14 plays with draft copy, 7 design principles (never shame, caps/cooldowns, managers coached not surveilled, exec aggregate-only), slow escalation ladder.
3. `03_Adoption_Dashboard_Demo.html`: standalone dashboard + client-side trigger engine on seeded synthetic Greenlight-shaped data (56 users, 6 teams, 12 weeks, week-10 launch event, Customer Success as the deliberately declining team so PB-M1 fires). Config-over-code rules block. No runtime AI per Jason's hosting rule. Render-verified.
4. `04_JenEast_Meeting_Guide.html`: ask-first-show-last meeting plan, question blocks with listen-fors, three live reframes (lift numbers, services play, tool-specific), four exit criteria.
5. `05_Greenlight_Data_Spec.html`: tiered field spec mapped to triggers, 8-12 week history ask, four delivery options (one-off CSV = immediate unblock), Slack-ready ask for Jason.

Success-criteria strategy locked: deliverable-based (the five artifacts by Dec 31), never adoption-lift metrics. Strategic frame: "we manage AI adoption the way Intradiem manages workforces."

**Aug 5 2026 — Greenlight data reality + premortem risk-fix wave.** Dallas confirmed Greenlight telemetry is very very limited / mostly doesn't exist yet (contradicts Jason's earlier "reporting exists"). Ran a full strategic premortem (dated Sep 30 failure). Top 3 failure modes: (1) no data → pilot/dashboard artifacts go hollow; (2) Dallas mistaking his build velocity for project velocity while the real clock runs on Joey's bandwidth (Joey no Claude license, ramping onto own accounts, already underwater) and Catherine's legal queue — July slip repeats; (3) automated nudges to colleagues = surveillance optics on a board-visible project, no permission ever secured (undefended risk). Pre-fix confidence 45%.

**Keystone fix: pilot v1 = opt-in volunteer cohort (20-30 people, 3-5 teams, 6-8 wks).** Opt-in kills the surveillance risk AND guarantees a controllable data substrate (a cohort you own can always be manually instrumented). Built 4 new deliverables + updated 04:
- `06_Pilot_Design_and_Data_Ladder.html`: reframe (pilot proves the LOOP not the pipeline); opt-in cohort scope; 4-tier data fallback ladder (A full Greenlight → B coarse Greenlight → C another AI tool's admin usage e.g. Claude → D manually instrument the cohort = guaranteed floor); 4 non-negotiable gates (permission, legal, opt-in, logging-before-sends).
- `07_Success_Criteria_and_Form_Draft.html`: the payout contract. Five artifacts defined data-agnostically; pilot = "best available internal AI-usage data" NEVER "Greenlight telemetry"; full drafted form answers for Joey to review not author; "what the form must NOT commit to" (no lift number, no Greenlight-specific pilot, no hosted production system).
- `08_Permission_and_Consent_Brief.html`: one-page ask to Derek+Jen (cc Catherine/Jason) for written yes to run opt-in pilot; 6 safeguards; this is Gate 1, no send without it.
- `09_Team_Operating_Plan.html`: Joey's single read. 8-step dependency-ordered critical path, ownership table, copy-paste kit (3-way invite+agenda, Jen East mtg request, cohort recruitment note), tripwire (3-way not booked by end of week = July repeating) + escalation (Dallas → Derek if a stakeholder step stalls, agreed in the 3-way).
- `04` updated: Jen East meeting now also carries the data-agnostic scope blessing + the permission ask (one meeting closes both big uncontrollables).

Post-fix confidence: ~80% (high), contingent on the 4 human moves actually happening. Residual risk = execution/Joey bandwidth (not buildable away); hedge = escalation to Derek + Dallas owning the short critical path. Single biggest lever = get Jen East to bless the data-agnostic pilot definition in the vision meeting.

Related: [[deliverables-save-location]], [[html-exec-standard]]
