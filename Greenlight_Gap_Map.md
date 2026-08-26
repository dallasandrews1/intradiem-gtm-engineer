# Greenlight Gap Map: What to Publish First

Purpose: decide where to plug my GTM engines into Greenlight, where to stay out, and what to publish first. Built by mapping the 30 existing Greenlight agents against the engines and skills already running in my workspace.

## The one-line read

Greenlight has 30 agents, but only about 8 touch the GTM outbound motion, and none of them do outbound GTM engineering (signal to coordinated action, net-new strike plans with committee and ROI, install-base expansion signals). That is open white space, it maps directly to Naveen's Q3 mandates, and it sits on engines I already run. The two agents closest to my messaging and research work are both owned by one person (josh.wilkins), so the move is to publish one level higher than his tools, not rebuild them.

## How Greenlight maps to my architecture

A Greenlight agent is a system prompt plus a set of "actions" (tool integrations). My engines are already MCP servers (`intradiem_mcp_server.py`, `tam_mcp_server.py`) sitting behind the hosted brain (`gtm-hosted-platform/brain/app.py`). So a published agent is a thin front end: Greenlight system prompt, my MCP endpoints as its actions, my config and data staying in my control. Same "one brain, many surfaces" pattern as the Slack app and the Claude plugin. Greenlight becomes a third surface, and the only one where colleagues already log in daily.

Same guardrail carries over: the verified-claims gate. Nothing with placeholder ROI (`roi_model.json`, `proof.json`, seeded `engine_state.json`) reaches a shared agent without passing the Value Repository check.

## The 30 agents, classified

### Overlap: I already run a more complete version (do not rebuild head-on)

| Greenlight agent | Owner | My equivalent | Move |
|---|---|---|---|
| VITO Messaging Assistant | josh.wilkins | first-draft-engine + copy-sharpener + strike-plan sequences | Do not clone. Publish signal-to-play (higher order). Offer to feed his agent verified claims + 12-40-30 compliance. |
| Sales Company Analysis bot | josh.wilkins | tam-outbound-engine strike plan (committee + ROI + 4-touch) | Do not clone. My strike plan is a superset (research plus action). Position as the next step after his research bot. |
| 12-40-30 | ehoy | copy-sharpener / first-draft-engine | Align, do not compete. Make my copy engine output 12-40-30-compliant. This is Intradiem's house messaging framework, so I adopt it. |
| Earnings Call Analyzer | ben.goodenough | daily-war-room + StarRatings_Earnings_Signals | Different enough (mine is scoped to the outbound universe and maps to plays). Acknowledge overlap, keep mine outbound-specific. |

### Adjacent: feeds or consumes my engines (collaborate, do not duplicate)

| Greenlight agent | Owner | Relationship |
|---|---|---|
| Salesforce Agent (read-only) | jason.jones | Data source my signal/tam engines already pull. Potential shared backend. |
| Salesforce Revenue Intelligence | jason.dowden | Forecasting/pipeline. Complements my surfaced-vs-realized impact scorecard, does not replace it. |
| Intelligent Rule Companion (ACD/WFM CS analyst) | jose.villalobos | Closest thing to install-base analysis. Worth a conversation before I publish an expansion-signals agent. |
| Customer Call Insights / ConvoIQ | savannah.cupp / jason.dowden | Transcript to insight. Feeds my roi-business-case input, does not compete. |
| Channel Catalyst | frank.ciccone | Channel/partner motion. Different lane. |
| Confluence Assistant | jason.jones | Internal KB. Consume for research. |

### Out of lane: support, implementation, product, enablement, utilities (ignore)

Float Assistant (x2), MikeG_PRD_HelperAgent, CSC Project Resource Planning, Support Case Resolution, Incident Response, Technical Summary, Final Draft Client Update, WebHelp Documentation, WebHelp Style Guide, Instructional Designer, Prompt Engineer, French Canadian Translator, Micro Motivations, Jason's AI news, Roleplay Agent, Salesforce Core CRM (deprecated), Summarize Meeting Transcript, Summarize Customer Meeting Transcript.

One name to note: Summarize Customer Meeting Transcript is owned by skemme (Scott Kemme), the back-office exec tied to Mandate 3. That is a relationship entry point, not a build target.

## The white space (nobody on Greenlight has built this)

The entire outbound GTM engineering layer is missing:

- Account signal to coordinated action (Marketing brief + Sales alert + outreach draft from one trigger)
- Net-new strike plans with buying committee, ROI, and sequence
- Install-base expansion and risk signals
- Competitive displacement briefs (Verint, NICE, Calabrio, in-house)
- Economic-buyer ROI / business case from call metrics
- Back-office ICP sourcing

All of it already runs in my workspace. None of it exists on Greenlight.

## Publish-first ranking

Ordered by strategic resonance, low ownership conflict, and direct tie to a Naveen mandate.

**1. Signal-to-Play Agent** (on `intradiem-signal-to-play` + signal/tam MCPs)
One account signal becomes three synchronized outputs. Highest strategic story: it mirrors Intradiem's own product thesis, real-time signals triggering automated action, so it doubles as a "we run GTM the way our product runs operations" proof point. No equivalent exists. Conflict: none.

**2. Strike Plan Agent** (on `tam-outbound-engine` via the brain)
Net-new account in, full plan out: committee, ROI, 4-touch sequence. Directly serves the throughput mandate. Conflict: adjacent to josh.wilkins' Sales Company Analysis bot, so I position it as the action step after his research, and give him a heads up.

**3. Back-Office ICP Agent** (on `intradiem-backoffice-icp`)
Ties to Mandate 3 (200+ back-office contacts) and to Scott Kemme by name. No equivalent. Conflict: none. Publishing this is visible proof I am executing a named directive.

**4. Economic Impact / ROI Agent** (on `intradiem-roi-business-case`)
Call metrics to a one-page CFO business case. High value to every AE. No equivalent. Conflict: none.

**5. Competitive Displacement Agent** (on `intradiem-competitive-intel`)
Competitor mention to wedge brief. Useful to the whole sales team. No equivalent. Conflict: none.

Hold: anything that clones VITO Messaging or Sales Company Analysis head-on. Instead, route my copy engine to comply with 12-40-30 and offer it as an upgrade to the existing messaging agents.

## The play with Naveen (walk-in version)

1. Here is the Greenlight landscape: 30 agents, roughly 8 in our lane, none doing outbound GTM engineering.
2. Here is the white space, and it happens to be exactly what my engines already do.
3. I want to publish 3 to 5 agents that sit on those engines, starting with signal-to-play and the strike plan, so the work becomes visible and usable org-wide instead of living in my workspace.
4. Two of the closest existing agents are josh.wilkins', so I will loop him in as a collaborator rather than publish over him. Where do you want me to be careful?
5. 12-40-30 is the house framework, so my copy engine will output to it.

## Ownership-conflict flags (so I do not step on anyone day one)

- josh.wilkins: owns the two agents closest to my messaging and research. Loop in first.
- ehoy: owns 12-40-30. Adopt the framework, credit it.
- ben.goodenough: owns Earnings Call Analyzer. Keep mine outbound-scoped, acknowledge overlap.
- jose.villalobos: owns the ACD/WFM CS analyst. Talk before publishing an expansion-signals agent.
- jason.dowden / jason.jones: own the Salesforce and revenue-intelligence agents. These are backends I want to sit on, not compete with.

## Next build step

Wire the top-ranked agent (signal-to-play) as a Greenlight agent: its system prompt plus my hosted-brain endpoints as actions, verified-claims gate intact. That is the first thing to stand up once I have brain hosting and a Greenlight publish slot.
