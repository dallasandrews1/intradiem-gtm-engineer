# Intradiem GTM Engineer: 6-12 Month Grand Strategy

A strategy built on two things: what is publicly true about Intradiem today, and the
premortem's core finding that the system is done but the win is political. This is not
an execution roadmap. It is a stakeholder map, a sequencing logic, and a learning
agenda. The execution details get filled in by what you learn inside.

## The Intradiem reality (what we know now)

- **Growth-equity backed, scaling toward an exit.** JMI Equity is the notable backer. The company closed record 2025 results, 114%+ net retention, record net-new bookings, and roughly 350,000 agents on platform. A company in this posture has one board-level priority: efficient growth. That is exactly the value a GTM Engineer creates, and it is your tailwind.
- **A new CRO rebuilding GTM.** John Norton became CRO in August 2024. A new revenue chief in his first year is building a motion, not defending one, which is why a green GTM function exists for you to own. He is your natural executive sponsor.
- **The platform was just modernized.** The 2025 next-generation platform is what Busbee and Naveen referenced. It newly exposes event-level data, the raw material for the install-base signal engine. That data is the dependency, not the capability.
- **Regulated ICP.** Healthcare, insurance, and financial services. This makes the claims-and-compliance risk from the premortem real, not theoretical. ROI numbers and peer references aimed at health plans are legally sensitive.
- **The moat is unchanged.** Intradiem acts in idle time between scheduled activities, the gap WFM (Verint, NICE, Calabrio) never addresses. Never position those as competitors; they are the layer you sit on top of.
- One caveat: public revenue figures for a private company like this are unreliable (one source lists ~$10.7M, which is implausibly low against 350K seats and record bookings). Do not anchor on a number. Anchor on the direction: backed, scaling, growth-pressured.

## The core strategic insight

Your two motions have **opposite dependency profiles**, and that dictates the sequence.

- **Net-new outbound** runs entirely on external data (firmographics, tech stack, job postings, news) that you control on day one. No internal access required.
- **Install-base expansion**, the motion that extends their 114% NRR strength, runs on internal product-usage data owned by other orgs and gated by enterprise data governance.

So lead with net-new as the visible wedge, and run the install-base motion as a parallel access-and-relationship campaign. Do not stake your first 90 days of credibility on data you do not yet control. This single choice is what makes the premortem's highest-probability failure survivable.

## Stakeholder and dependency map (the real strategy)

| Dependency | Likely owner | Measured on | What they fear | Your move |
|---|---|---|---|---|
| Product-usage data | CTO (Kevin Wilson) / data eng, with Busbee + Naveen on product | Platform, roadmap, uptime | Customer usage data leaving governed systems | Co-design with Busbee/Naveen (already allies); frame the brain as internal, behind their controls |
| Salesforce export + writes | CRO (John Norton) + RevOps | Forecast accuracy, CRM hygiene | A rogue system corrupting the CRM | Make RevOps a co-owner; read-only first, writes only after schema sign-off |
| Slack app install | IT / workspace admin | Security, governance | Shadow IT | Lead with the Claude plugin (no IT dependency); bring the Slack admin in early as a partner |
| Clay / Apollo procurement | Procurement + InfoSec + CFO (William DiPaula) | Vendor risk, spend | New-vendor exposure, cost | Open the procurement track week one; use trial access for the pilot in the interim |
| Claim / proof verification | Marketing (VP Anise) + Legal/Compliance + value engineering | Brand, legal exposure | A false claim to a regulated buyer | Get verified proof points and an approval workflow before any self-serve send |
| Executive air cover | CRO (John Norton), with Busbee | The number, GTM build | Betting on the wrong hire | Orient your roadmap to the CRO's metric; make your wins his wins |

This table is the strategy. Everything below is sequencing.

## The 6-12 month arc

**Days 0-30, listen and map.** Do not deploy anything broadly. Meet every owner in the table and fill it in with real names, real timelines, and the real approval paths. Validate the signals against what a CSM or AE already knows. Recruit one co-owner who will advocate for the system when you are not in the room. Ship the net-new wedge to a one or two rep pilot using external data only.

**Days 30-60, prove the wedge.** Get one rep to book one meeting off a strike plan. Secure verified proof points and a claim-approval path from marketing and legal, which neutralizes the biggest risk. Put the install-base data-access request into governance review. Plugin live for the pilot.

**Days 60-90, first systematic win and the exec story.** Net-new producing real pipeline. The impact scorecard shows opportunity surfaced plus early realized results; present it to the CRO in his language. Begin install-base signals on whatever real data has cleared review. Slack app for the team if admin has approved.

**Months 4-6, scale.** Net-new running across the team. The install-base expansion motion live on real data, extending the 114% NRR strength. Notifier live with governed sends. Measurement feeding the CRO's reporting.

**Months 6-12, platform not project.** Both motions systematized. The brain is the company's GTM intelligence layer, owned by you. Salesforce surface ships as v2. You are the indispensable owner of the growth-engineering layer precisely as the company scales toward its exit, which is the best possible position to be in when that exit happens.

## Learning agenda (the connector pieces you find inside)

These are the questions whose answers set your pace and direction. Answer them in your first weeks.

- What does the modernized platform actually expose at the event level, and who controls access? (Busbee, Naveen, CTO)
- What is the CRO's number-one GTM gap, net-new pipeline or expansion systematization? Sequence to his answer, not your assumption.
- What is the real claim-approval process for customer-facing numbers, and who owns it?
- What is already in the stack (Salesforce, Gainsight, Outreach or Salesloft, any Clay or Apollo)? Build on it; never duplicate it.
- Who is the internal skeptic and who is the internal champion among the system owners?
- How fast does procurement actually move? That single fact resizes your whole timeline.

## The one thing that determines success

Reframe your first 30 days from execution to co-ownership. You already won the build. Walk in recruiting co-owners, the CRO, RevOps, data engineering, marketing and legal, rather than presenting a finished system. The technology is done. The win is political, and it is won by making the owners of your dependencies feel like authors of the outcome, not obstacles to it.
