---
name: league-full-pipeline
description: "Master 7-phase autonomous account orchestrator. Runs complete research and outreach pipeline sequentially from Init through PDF generation. Trigger when starting a new Tier-1 account, running a full account pipeline, or launching an account from scratch. Includes 5-tier buying committee mapping and persona rules. Load proactively for any new account assignment."
---

## When this skill applies

- Run at the beginning of any new Tier-1 account assignment
- Run as the foundational orchestration for full-account acceleration
- Run in Phase 1 immediately after account selection
- Run sequentially through all 7 phases (do not skip phases)

## Background

The Full Pipeline skill is the master orchestrator. It runs Dallas through a complete 7-phase account launch sequence, from system initialization through omnichannel swipe file generation. Every phase outputs specific deliverables that feed into the next phase. Phase 1 locks in constraints. Phase 2 diagnoses the forcing function and maps the 5-tier buying committee. Phase 3 builds multi-threading matrices with persona-specific research. Phase 4 audits the digital front door (app reviews). Phase 5 creates the 10-day execution roadmap. Phase 6 generates send-ready copy for every touchpoint. Phase 7 packages everything into League-branded PDFs. All outputs are saved to /Accounts/[Account Name]/ with consistent naming.

## Buying Committee Structure (5-Tier Model)

### Tier 1: Champion Layer (Initial Contact)
- **Typical Role**: VP Digital Health, Director of Member Experience, Senior Manager of Engagement
- **Characteristics**: Mid-to-senior level operator, owns member-facing initiatives, evaluates solutions for operational capability
- **Primary Motivation**: Reduce operational friction, improve member NPS, demonstrate innovation to leadership
- **Engagement Style**: Peer-to-peer, consultative, values efficiency and transparency
- **Decision Authority**: Recommends solution internally, influences peers, does NOT have final budget approval
- **Key Metrics**: Cares about engagement rate, NPS, member feedback, operational complexity, time-to-launch

### Tier 2: Economic Buyer Layer (Budget Authority)
- **Typical Roles**: CFO, VP Finance, VP Operations, Chief Financial Officer
- **Characteristics**: Executive level, controls budget allocation, thinks ROI and payback
- **Primary Motivation**: Cost reduction, margin expansion, financial risk mitigation
- **Engagement Style**: Metrics-driven, data-centric, prefers executive summary format
- **Decision Authority**: Approves vendor spend, allocates budget, final financial sign-off
- **Key Metrics**: ROI, payback period, cost avoidance, annual spend, implementation cost, NPV

### Tier 3: Technical/Legal Layer (Risk & Feasibility Gates)
- **Typical Roles**: CTO, VP IT, VP Infrastructure, General Counsel, Chief Security Officer, Compliance Officer
- **Characteristics**: Risk-averse, technically detailed, concerned with integration complexity and security
- **Primary Motivation**: Reduce technical risk, maintain security posture, avoid rework and integration issues
- **Engagement Style**: Technical specification, proof-of-concept, documentation, third-party validation
- **Decision Authority**: Validates feasibility, approves integration approach, controls legal and InfoSec gates
- **Key Metrics**: Integration complexity, API availability, data security, compliance certifications, SLA guarantees, time to implement

### Tier 4: Executive Sponsor (Clinical/Member Impact Validation)
- **Typical Roles**: Chief Medical Officer, Chief Member Experience Officer, Chief Clinical Officer
- **Characteristics**: Senior executive, rarely engaged until late stages, validates clinical impact and member safety
- **Primary Motivation**: Member outcomes, clinical safety, regulatory compliance, organizational mission alignment
- **Engagement Style**: Evidence-based, clinical data, outcomes focused
- **Decision Authority**: Final organizational validation, CEO/Board reporting
- **Key Metrics**: Clinical outcomes, member safety, member satisfaction, regulatory compliance, evidence base

### Tier 5: Operational/Pain Layer
- **Typical Roles**: Directors, VPs, and mid-level leaders whose teams absorb consequences of the forcing function daily (Dir. of Member Services, Clinical Operations Manager, Contact Center Director, Dir. of Quality/HEDIS, Care Management leads)
- **Characteristics**: Hands-on operational leader, closest to the daily pain, credible internal voice for change
- **Primary Motivation**: Operational relief, workflow efficiency, staff burden reduction
- **Engagement Style**: Tactical, problem-solving, values practical solutions over strategic vision
- **Decision Authority**: Validates pain internally, influences Champions and EBs through ground-truth evidence
- **Key Metrics**: Call volume, staffing ratios, processing time, error rates, member complaints, operational capacity

## Persona Rules (Applied to Each Tier)

### Tier 2 Persona: CFO/VP Finance
- **Lead With**: ROI, payback period, cost avoidance, vendor cost reduction
- **Frame As**: Financial relief, margin expansion, operational cost reduction
- **Avoid**: Clinical outcomes (that's CMO's interest), technical architecture (that's CTO's interest)
- **Example Language**: "Your current member services cost is $2.1M annually. A 20% reduction is $420K annual savings. Payback period is under 12 months. That's margin relief."
- **Tenbit++ Application**: Observation (current state cost) → Insight (engagement drives cost) → Value ($420K savings) → Next Step (15-min business case review)

### Tier 2 Persona: VP Operations
- **Lead With**: Workflow efficiency, FTE reduction, implementation speed, operational burden
- **Frame As**: Operational relief, staff efficiency, process simplification
- **Avoid**: Member experience design (that's member experience director), financial details (that's CFO)
- **Example Language**: "Your member services team spends 60% of time on basic navigation and benefits questions. Automation and self-service reduce that to 20%. That's 6-8 FTE reduction potential. Implementation is 4-6 weeks with zero disruption to call center."
- **Tenbit++ Application**: Observation (current operational burden) → Insight (automation solves this) → Value (FTE reduction + speed) → Next Step (workflow audit)

### Tier 1 Persona: VP Digital Health / Director Member Experience
- **Lead With**: Member engagement uplift, NPS improvement, digital experience modernization
- **Frame As**: Digital transformation, engagement catalyst, member retention driver
- **Avoid**: Cost reduction (save that for CFO), technical architecture (save for CTO)
- **Example Language**: "Your app is at 3.2 stars. Member feedback shows benefit navigation is the top friction point. Solving that typically drives 2-3 point engagement uplift and 0.5-1 point NPS improvement. We can measure impact within 90 days."
- **Tenbit++ Application**: Observation (app ratings + member feedback) → Insight (navigation is the barrier) → Value (engagement + NPS uplift) → Next Step (15-min audit review)

### Tier 3 Persona: CTO / VP IT
- **Lead With**: Integration simplicity, API availability, zero custom development, data security
- **Frame As**: Technical partnership, risk mitigation, architecture fit
- **Avoid**: Member experience benefits (irrelevant), financial impact (irrelevant)
- **Example Language**: "We integrate with HealthEdge through standard EDI feeds and SFTP. Zero custom development. Real-time webhooks for urgent signals. We handle HIPAA compliance and SOC 2 attestation. Integration timeline: 2-3 weeks with your HealthEdge team."
- **Tenbit++ Application**: Observation (integration risk concern) → Insight (our approach reduces risk) → Value (2-3 week timeline, no custom work) → Next Step (technical deep-dive with your team)

### Tier 3 Persona: General Counsel
- **Lead With**: Contract negotiation, indemnification, compliance, liability
- **Frame As**: Risk management, compliance certainty, legal partnership
- **Avoid**: Clinical outcomes, member experience, financial benefits
- **Example Language**: "Standard MSA or your template. HIPAA business associate agreement. State-specific privacy compliance. Indemnification covers data breach and services failure. We work with your legal team on contract timeline — typically 4 weeks for negotiation."
- **Tenbit++ Application**: Observation (legal risk and timeline) → Insight (standard process) → Value (clear timeline and framework) → Next Step (legal review kickoff)

### Tier 4 Persona: Chief Medical Officer / Chief Member Experience Officer
- **Lead With**: Member outcomes, clinical safety, evidence base, member satisfaction
- **Frame As**: Clinical value, member-centric innovation, outcome improvement
- **Avoid**: Cost reduction, technical details, implementation speed
- **Example Language**: "Engagement is clinically proven to improve medication adherence, reduce preventable ER visits, and improve chronic disease outcomes. We track member safety metrics throughout implementation. Clinical outcomes are measurable within 90 days."
- **Tenbit++ Application**: Observation (engagement-to-outcomes gap) → Insight (member activation drives outcomes) → Value (clinical improvement + member safety) → Next Step (outcomes validation)

### Tier 5 Persona: Director/Manager Operations
- **Lead With**: Operational pain relief, workflow simplification, staffing burden, specific friction points
- **Frame As**: Day-to-day relief, practical improvement, ground-level fix
- **Avoid**: Strategic vision (that's executive sponsor), financial modeling (that's CFO), technical architecture (that's CTO)
- **Example Language**: "Your team processes 4,000 calls per week on benefits navigation alone. Self-service deflection typically cuts that by 30-40% in the first quarter. That's your staffing math changing."
- **Tenbit++ Application**: Observation (current operational burden) → Insight (root cause of the burden) → Value (specific relief metric) → Next Step (15-min walkthrough of how a similar team solved this)

## Workflow: 7 Phases (Sequential)

### Phase 1: System Initialization
Run league-ae-initializer to:
- Load AE_Deal_Accelerator_Canon.md, BDR_Architect_Canon.md, League_Payer_Value_Prop.pdf
- Lock session-wide Canon constraints
- Confirm 5-tier buying committee structure (as documented above)
- Confirm persona rules (as documented above)
- Create session workspace at /Accounts/[Account Name]/

**Output**: Session_Init_[Date].md

---

### Phase 2: Autonomous Research + Forcing Function Diagnosis + Buying Committee Mapping

#### Step 1: Public Company Research
- Pull most recent 10-K SEC filing (if publicly traded)
- Search company news and press releases (last 12 months)
- Review latest earnings call transcript
- Identify organizational structure, key executives (CEO, CFO, CIO, CMO if publicly disclosed)
- Extract quantified metrics: member count, member engagement rate, member services cost, current vendors
- Note any recent M&A, leadership changes, regulatory events, strategic initiatives

#### Step 2: Diagnose Forcing Function
- From research, identify the PRIMARY operational pain driving this account
- Forcing function is typically: cost reduction, engagement gap, regulatory pressure, technology modernization, market consolidation, member experience improvement
- Document with evidence (quote from earnings call, news article, regulatory filing)
- This becomes the primary sales angle

#### Step 3: Map 5-Tier Buying Committee
Research each tier and identify likely roles and personas:

**Tier 1 Champion Mapping**:
- Likely role: VP Digital Health, Director of Member Experience, Senior Manager of Engagement, VP Marketing (if member engagement focused)
- Search LinkedIn for current title holders at target account
- Note: If no clear member experience executive, Champion may be Chief Medical Officer or VP Operations who owns digital initiatives

**Tier 2 Economic Buyer Mapping**:
- Likely roles: CFO, VP Finance, VP Operations, Controller
- Search public filings for CFO name and reporting structure
- Note: VP Operations often has operational budget authority; confirm if they're the Economic Buyer or if they report to CFO

**Tier 3 Technical/Legal Mapping**:
- Technical: CTO or VP IT (find on LinkedIn)
- Legal: General Counsel (find on LinkedIn, sometimes in SEC filings)
- Security: Chief Information Security Officer or VP InfoSec (if large enough to have dedicated role)

**Tier 4 Executive Sponsor Mapping**:
- Likely roles: Chief Medical Officer, Chief Member Experience Officer, Chief Clinical Officer
- Note: May not exist in smaller organizations; in that case, CMO or Chief Medical Director fills role
- At Medicare Advantage plans: Medical Director often owns member outcomes

**Tier 5 Operational/Pain Layer Mapping**:
- Likely roles: Directors and Managers who feel the forcing function daily (Member Services, Contact Center, Quality, Care Management)
- Search LinkedIn for mid-level operational leaders at the target account
- Note: These people validate pain internally. Their engagement accelerates C-suite decisions. Never skip them.

**Output**: Buying_Committee_Map_[Account].md with names, titles, LinkedIn URLs (if found), likely personas, motivation summary

#### Step 4: Identify Competitive Posture & Vendor Stack
- Search for any mentions of current engagement platform or vendor (Castlight, Accolade, Wellframe, etc.)
- Identify any announced competitive evaluations or RFPs
- Note any Epic, QNXT, HealthEdge deployments (technical integration points)
- Note any cloud migrations (Azure, AWS, GCP)

**Output**: Account_Competitive_Posture.md

#### Step 5: Create Account Strike Packet
Run league-ae-briefing to create:
- Primary Forcing Function (clinical, evidence-backed)
- Playbook Hypothesis (TSA Exit, Microsoft Pivot, Wrapper Moat, Labor Substitution, Care Redesign)
- Hidden Fear (unstated anxiety of buying committee)
- Internal Enemy (stakeholder who will resist)
- Strategic Intervention (how Dallas unlocks the deal)
- Deal Playbook with Phase timing
- Wildcard Risks

**Output**: [Account]_Strike_Packet.md

#### Phase 2 Output Files (Save to /Accounts/[Account Name]/):
- Session_Init_[Date].md
- Buying_Committee_Map_[Account].md
- Account_Competitive_Posture.md
- [Account]_Strike_Packet.md

---

### Phase 3: Multi-Threading Matrix & Persona Research

#### Step 1: Build Multi-Threading Matrix
Create a matrix with:
- Column 1: Tier (1, 2, 3, 4, 5)
- Column 2: Role (VP Digital Health, CFO, CTO, CMO, etc.)
- Column 3: Persona Rules (How to message this person)
- Column 4: Primary Motivation (Cost, efficiency, engagement, risk, outcomes)
- Column 5: Key Metrics (ROI, FTE reduction, NPS, integration timeline, member safety)
- Column 6: LinkedIn Search String (To find this person at target account)
- Column 7: Outreach Angle #1 (Opening email/call narrative)
- Column 8: Outreach Angle #2 (If first approach fails)
- Column 9: Outreach Angle #3 (If Angles 1 & 2 don't land)

#### Step 2: Deep Persona Research
For each persona identified (CFO, VP Digital Health, CTO, CMO, etc.):
- Search LinkedIn for 3-5 examples of this role at similar-size accounts
- Review their public profiles (certifications, background, stated interests)
- Search for articles they've published or spoken at conferences
- Identify key language they use (operational efficiency, member centricity, clinical outcomes, etc.)
- Document how Dallas should speak to this persona

#### Step 3: Create Persona-Specific Outreach Angles
For each Tier and Persona, create 3 different opening angles:

**Angle 1 (Forcing Function Lead)**: Lead with the primary operational pain
- Example for CFO: "I saw your earnings guidance. Engagement and retention are your biggest cost drivers in 2026. Let me share how other plans in your category are addressing that."

**Angle 2 (Competitive/Benchmark Lead)**: Lead with benchmark data or competitive intel
- Example for VP Digital Health: "Your app is at 3.2 stars. Competitors in your category are at 3.8. Worth a 15-min call to see what's driving the gap?"

**Angle 3 (Executive Commitment Lead)**: Lead with new strategic commitment or signal
- Example for CTO: "Saw your Azure adoption roadmap. Real-time member analytics on Fabric requires a consumer-facing activation layer. Let's align on architecture."

**Output**: Multi_Threading_Matrix_[Account].md with all personas, angles, and research notes

---

### Phase 4: Digital Front Door Audit

Run league-app-audit to:
- Pull iOS and Android app ratings (1-star, 2-star review analysis)
- Identify top 3 complaint categories (benefit navigation, login issues, claims visibility, etc.)
- Calculate impact metrics (NPS, call center deflation, churn risk)
- Draft 3-touch LinkedIn sequence for VP Digital Health

**Output**: [Account]_App_Audit.md with executive summary and outreach sequence

---

### Phase 5: 10-Day Execution Roadmap

Run league-holistic-roadmap to:
- Synthesize Strike Packet, Multi-Threading Matrix, and App Audit
- Map all 5-tier buying committee members into the outreach sequence with full 10-day coverage per contact
- Create day-by-day tactical plan for 10 business days
- For all cold call, voice note, and voicemail touchpoints in the roadmap, invoke league-cold-call-playbook to generate gold-standard scripts with persona-calibrated openers, objection handles, and memorizable variants
- Week 1: Foundation (personalized emails, LinkedIn connection requests, voice notes to all committee members across all 5 tiers)
- Week 2: Pincer (technical gap audit email to CTO, economic impact email to CFO, operational pain emails to Tier 5, hail mary call to Champion)
- Assign specific tasks per day with "Why" rationale

**Output**: [Account]_Holistic_10_Day_Roadmap.md

---

### Phase 6: Omnichannel Swipe File

**IMPORTANT: Before writing ANY outreach copy in this phase, invoke league-first-draft-engine.** That skill governs the thinking process for how copy is drafted: prospect-first cognition, single-idea construction, voice-matched writing, and the Prospect Test. Every email, InMail, and DM in this phase must be produced through the First Draft Engine's five-gate sequence FIRST, then verified with the Copy Sharpener. Do not start with rules and build sentences against a checklist. Start with one idea per prospect, write the whole message as a flowing thought, pass the Prospect Test, then check for rule violations.

Create send-ready copy for every touchpoint:

#### Cold Email Sequence (5-email sequence over 15 days)
- Email 1: Forcing function lead (80-120 words)
- Email 2: Follow-up with specific insight (100-150 words)
- Email 3: Competitive benchmark or app audit reference (100-150 words)
- Email 4: Social proof or case study angle (120-150 words)
- Email 5: Meeting request with 2-3 times (80-120 words)

#### LinkedIn InMail Sequence (3 touches)
- InMail 1: App audit or forcing function observation (2-3 sentences)
- InMail 2: Benchmark or competitive insight (2-3 sentences)
- InMail 3: Meeting CTA (2-3 sentences)

#### Voice Note / Voicemail Scripts (under 45 seconds for voice notes, under 25 seconds for voicemail)
- Opening hook (5-10 seconds)
- Specific observation (10-15 seconds)
- Value prop (5-10 seconds)
- CTA (5 seconds)
- **TL;DL (Too Long; Didn't Listen)**: Every voice note MUST also include a written TL;DL summary (2-3 sentences) sent alongside the audio. Captures core insight and CTA in text form. Sending both is getting significantly more replies than voice note alone.

#### Voicemail Scripts (under 25 seconds, ~50-60 words)
- Name, one sentence of context, callback reason. That's it.

#### Vidyard Scripts (under 3 minutes)
- Screen share of their actual app reviews or public data, walk through 2-3 specific friction points, reference one peer outcome, soft CTA.
- Tone: Like showing a colleague something interesting. Not a sales demo.

#### Cold Call Script

**Invoke league-cold-call-playbook for all phone-based scripts.** That skill generates the complete cold call playbook including: universal 45-second script, memorizable 20-second script, all four persona-calibrated versions (CEO, CTO, CXO, VP/Ops), objection handles, voice note scripts, and voicemail scripts. Do not generate cold call scripts from the structural parameters below — use the playbook's gold-standard patterns.

The playbook will produce a `[Account]_Cold_Call_Playbook.md` file with all variants and a quality gate verification checklist.

Structural reference (for context, but use playbook for actual scripts):
- Opening (8-10 sec): Name + one credible sentence. Example: "Hi [Name], Dallas Andrews. I work with digital strategy teams at the big plans on front door architecture."
- Hook (15-20 sec): One specific, data-backed observation about THEIR business. Reference their app ratings, earnings data, member count, or a specific initiative.
- Bridge (10-15 sec): Connect to a result someone else achieved. "One plan your size solved this by..." Vague enough for curiosity, specific enough for credibility.
- CTA (5-10 sec): Assumptive. "I think it'd be worth 10 minutes" or "If that resonates, let's find 15 minutes this week."
- NEVER start with "I know you're busy." NEVER use yes/no CTAs. NEVER use generic value props.
- Tone: Conversational, peer-level, mixed sentence lengths. Sounds like explaining something interesting at a dinner party.

#### Persona-Specific Angles (minimum 3 versions per account)
- CFO version: Leads with ROI, payback, cost avoidance. Metrics-driven, concise.
- VP Digital Health version: Leads with engagement, NPS, digital experience. Consultative, partnership tone.
- CTO version: Leads with integration, architecture, data security. Technical specification, third-party validation.
- COO version: Leads with operational efficiency, vendor consolidation, scaling challenges. Process-driven.
- CMO/CDO version: Leads with member satisfaction, competitive positioning, digital front door. Strategic tone.

#### Apply Copy Sharpener Rules (MANDATORY, NON-OPTIONAL)
This is not a suggestion. Every piece of outreach copy MUST pass through these rules before being included in any output:
- Tenbit++ framework (Observation → Insight → Value → Next Step)
- Brand-Light execution (no League mention Days 1-5)
- No FORBIDDEN WORDS
- Strict punctuation (periods and commas only in paragraphs)
- Persona-specific tone matching
- CTA escalation (Days 1-2 soft, Days 3-5 moderate, Days 6-8 direct, Days 9-10 confident close)
- Natural human tone: mixed sentence lengths, varied openers, no canned phrases ("compare notes," "pick your brain," "touch base")
- Account-specific references in every script. No generic copy reused across accounts.
- Every cold call, voice note, voicemail, and Vidyard script must sound like a real human speaking naturally, not reading a script
- Every voice note must include an accompanying TL;DL (too long; didn't listen) text summary (2-3 sentences)

**Output**: Omnichannel_Swipe_File_[Account].md with all 5 emails, 3 InMails, voice scripts, call script, and persona variants

---

### Phase 7: League-Branded PDF Generation

Generate polished PDFs for champion handoff:

#### Document 1: Account Executive Brief (1 page)
- Formatted as PDF ready for internal Slack/email
- Includes: Primary Forcing Function, Hidden Fear, Strategic Intervention, Next Milestone
- Executive summary of the strike packet
- Dallas's recommended 10-day plan

#### Document 2: Multi-Threading Persona Matrix (1 page)
- Formatted as PDF
- All Tier 1-4 stakeholders, their motivations, and outreach angles
- Ready to share with champion as "here's how we'll align your team"

#### Document 3: Economic Impact Summary (1 page, if Economic Buyer identified)
- Run league-cfo-business-case and format as PDF
- Current State metrics, Projected Impact, Cost of Inaction, Implementation Timeline
- Ready to send to CFO

#### Document 4: Digital Front Door Audit (1 page, if applicable)
- Format App Audit as PDF with 3-bullet summary and member complaint quotes
- Visual (chart or table) of app rating trends
- Ready to share with VP Digital Health

#### Document 5: 10-Day Execution Plan (1 page)
- Formatted as Gantt or calendar view
- Tasks, owners, due dates, Why rationale
- Ready to share with champion and internal sales team

All PDFs are branded (League logo, Dallas Andrews name, date) and saved to /Accounts/[Account Name]/PDFs/

---

## Canon Constraints (Session-Wide)

All outputs across all 7 phases follow these rules:

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name anywhere in Days 1-5 outreach — not in subject lines, email bodies, LinkedIn notes, voice scripts, or email signatures. Sign as "Dallas Andrews" only. Frame solution as category. League can appear starting Day 6, but sparingly.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.
- **Cold Call Playbook Integration**: All cold call, voice note, and voicemail scripts MUST be generated using league-cold-call-playbook. Phone-based scripts generated without the playbook will not meet the gold-standard quality bar.
- **Copy Quality Gate**: Before saving Phase 6 output, re-read every piece of outreach copy and verify: (1) no forbidden words or canned phrases anywhere in copy, (2) word counts within spec for each format, (3) CTAs match the escalation schedule for the sequence position, (4) no League mentions in Days 1-5 including signatures, (5) no two scripts open the same way, (6) every voice note has an accompanying TL;DL text summary. If anything fails, rewrite inline before saving.
- **Day 1 Email Gold Standard**: All first cold emails follow the Rick Hopfer HMSA three-beat CTA structure: proof point sentence → "Might be helpful/valuable to walk you through..." sentence → "Worth 15 min in the next few weeks?" as separate line → bare "Dallas" sign-off. Body prose flows naturally with merged sentences. Time anchors calibrated by seniority ("next few weeks" for VPs/C-suite, "this week or next" for directors).

## Output Structure

All outputs saved to: `/Accounts/[Account Name]/`

```
/Accounts/[Account Name]/
├── Session_Init_[Date].md
├── Buying_Committee_Map_[Account].md
├── Account_Competitive_Posture.md
├── [Account]_Strike_Packet.md
├── Multi_Threading_Matrix_[Account].md
├── [Account]_App_Audit.md
├── [Account]_10_Day_Roadmap.md
├── Omnichannel_Swipe_File_[Account].md
├── PDFs/
│   ├── [Account]_AE_Brief.pdf
│   ├── [Account]_Persona_Matrix.pdf
│   ├── [Account]_Economic_Impact.pdf
│   ├── [Account]_App_Audit.pdf
│   └── [Account]_10_Day_Plan.pdf
└── Deal_Tracking/
    ├── MEDDPICC_Updates.md
    ├── Call_Transcripts/ [folder for transcripts]
    └── Email_Log.md [log of all sent communications]
```

## Execution Summary

To run the full pipeline on a new account:

1. **Phase 1**: Run league-ae-initializer (5 min) → Save Session_Init
2. **Phase 2**: Run league-full-pipeline Phase 2 (30 min) → Save 4 research documents + Strike Packet
3. **Phase 3**: Build Multi-Threading Matrix (30 min) → Save Persona Matrix
4. **Phase 4**: Run league-app-audit (20 min) → Save App Audit
5. **Phase 5**: Run league-holistic-roadmap (20 min) → Save 10-Day Plan
6. **Phase 6**: Run league-first-draft-engine to draft ALL email/LinkedIn copy through the five-gate thinking sequence → Run league-copy-sharpener to verify drafts pass quality standards → Run league-cold-call-playbook for ALL phone-based scripts (15 min) → Apply Mandatory Copy Quality Standards → Save Swipe File + Cold Call Playbook. Copy must pass quality gate before proceeding to Phase 7.
7. **Phase 7**: Generate PDFs (15 min) → Save 5 branded PDFs

**Total time**: ~2 hours to go from new account to ready-to-execute

**Output**: 13 markdown documents + 5 branded PDFs, all saved to /Accounts/[Account Name]/, ready for Dallas to execute

## Example Account Execution

**Account**: Centene Corp
**Tier-1 Focus**: Medicaid + Medicare Advantage

**Phase 1 Output**: Session initialized, Canon locked, workspace created at /Accounts/Centene/

**Phase 2 Outputs**:
- Forcing Function: Medicaid rate cuts + TSA expansion. Need member engagement to reduce cost in Medicaid while acquiring high-margin Medicare members.
- Buying Committee: Sarah Martinez (SVP Digital Health - Champion), John Chen (CFO - Econ Buyer), Lisa Patel (CTO - Tech Gate), Dr. Michael Wong (Chief Medical Director - Sponsor)

**Phase 3 Output**: Multi-Threading Matrix with 4 personas, 3 angles each, motivation summary

**Phase 4 Output**: Centene's app is 3.4 stars. Complaints cluster around benefit clarity and login. NPS gap vs. UnitedHealth is 0.8 points.

**Phase 5 Output**: 10-day plan: Day 1-2 = research + multi-thread LinkedIn outreach to all 4 personas. Day 3-4 = app audit email to Sarah Martinez, CFO context email to John Chen. Day 5-6 = cold call to Sarah + CFO intro from Sarah. Day 7-10 = Discovery call + economic impact + technical deep-dive scheduling.

**Phase 6 Output**: 5 cold emails (CFO version, Digital Health version, CTO version), 3 LinkedIn InMails, voice scripts, call script, all brand-light and Tenbit++ compliant

**Phase 7 Output**: 5 branded PDFs ready for champion sharing and internal alignment

**Next**: Dallas executes Phase 5 (10-day roadmap) immediately. Measures success by booking Discovery call by Day 12.
