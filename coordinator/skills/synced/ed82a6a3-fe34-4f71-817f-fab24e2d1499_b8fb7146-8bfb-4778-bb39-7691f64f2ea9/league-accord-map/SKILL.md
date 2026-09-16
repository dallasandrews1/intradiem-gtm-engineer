---
name: league-accord-map
version: 1.0.0
description: Accord MAP Architect. Triggers when prospect confirms go-live date or hard deadline. Reverse-engineers timeline from go-live using enterprise payer procurement benchmarks. Generates Accord workspace format with Give/Gets per phase.
---

## When this skill applies

- Trigger immediately when prospect states a go-live date or hard deadline
- Trigger after Technical Evaluation phase when timeline commitment is made
- Trigger before moving to Procurement/Legal gates
- Trigger when creating formal Mutual Action Plan with prospect

## Background

The Accord MAP Architect works backward from the go-live date to create a realistic, phase-gated timeline. It factors in procurement cycles (3-4 weeks), legal review (3-4 weeks), InfoSec (2-3 weeks), technical scoping (2 weeks), and executive sign-off (1-2 weeks). The output is an Accord-style workspace with phase gates, Give/Gets per phase, and clear accountability. This prevents timeline slippage and keeps the deal moving.

## Workflow Steps

1. **Extract Go-Live Date**
   - From prospect conversation (email, call transcript, RFP response), identify the hard go-live date
   - Confirm this is a "must-have" date (board commitment, member communication deadline, regulatory requirement) vs. "target" date
   - Note who committed to the date (CEO, CFO, VP Ops, project sponsor)
   - If no explicit date, ask: "What's driving your timeline? When do you need to be live?"

2. **Reverse-Engineer Timeline from Benchmarks**
   - Starting from go-live date, work backward through enterprise payer procurement cycles
   - Use these BENCHMARKS for enterprise health plans (250K+ members):
     - **Go-Live**: Day 0 (start using platform with members)
     - **Final Implementation**: Week -2 (final testing, training, go-live readiness)
     - **Testing & Refinement**: Week -4 (UAT, issue resolution, performance validation)
     - **Data Integration & Configuration**: Week -6 (data flow validation, system setup, member communication start)
     - **Technical Scoping Complete**: Week -8 (API design finalized, architecture validated, third-party confirmations)
     - **InfoSec Complete**: Week -10 (security audit passed, pen testing complete, attestations signed)
     - **Legal/Procurement Complete**: Week -14 (MSA signed, SOW signed, budget approved, vendor agreement finalized)
     - **Executive Sign-Off**: Week -16 (CFO/CEO approval to move forward, budget allocation)
     - **Discovery/Validation Complete**: Week -18 (requirements gathered, fit assessment confirmed)

3. **Map Realistic Phase Gates**
   - Create 5-6 major phases from kickoff to go-live:
     - **Phase 1: Executive Approval & Discovery** (Week 0-2 from kickoff)
       - Give: MSA + SOW draft, technical requirements, discovery call
       - Get: Signed MSA, SOW, project sponsor name, executive approval, budget allocation
     - **Phase 2: Technical Scoping & InfoSec Initiation** (Week 2-4)
       - Give: Technical architecture doc, data integration plan, InfoSec questionnaire response
       - Get: Your CTO confirms integration approach, InfoSec questionnaire started, API access sandbox provided
     - **Phase 3: InfoSec & Legal Review** (Week 4-8)
       - Give: SOC 2 attestation, HIPAA BAA, security certifications, legal review support
       - Get: Legal approval, InfoSec clearance, signed MSA (final), signed SOW
     - **Phase 4: Data Integration & Configuration** (Week 8-14)
       - Give: API integration, data mapping, system configuration, UAT plan
       - Get: Data validation, UAT environment ready, internal stakeholder training scheduled
     - **Phase 5: Testing & Go-Live Readiness** (Week 14-18)
       - Give: UAT support, issue resolution, performance validation, go-live playbook
       - Get: UAT sign-off, member communication launched, go-live date confirmed
     - **Phase 6: Go-Live & Post-Launch** (Week 18+)
       - Give: 24/7 launch support, daily stand-ups, performance monitoring
       - Get: Go-live execution, member adoption tracking, success metrics baseline

4. **Identify the Longest Gate**
   - Most commonly: Procurement/Legal (3-4 weeks total) is the bottleneck
   - Second most common: InfoSec (2-3 weeks) or internal approvals
   - Note which gate will be longest and flag as "critical path"
   - Example: "For your timeline to hold, legal and procurement must move in parallel with technical scoping. If legal review takes 4 weeks sequentially, you'll miss the March go-live."

5. **Create Give/Gets per Phase**
   - "Give" = what League provides in this phase
   - "Get" = what prospect must provide/confirm to move to next phase
   - Make Gets specific and achievable
   - Examples of Gets:
     - Phase 1: Signed MSA, Project sponsor identified, Budget approved
     - Phase 2: CTO confirms integration approach, API sandbox access provided, InfoSec questionnaire started
     - Phase 3: Legal sign-off, InfoSec clearance, signed MSA (final)
     - Phase 4: Data validation complete, UAT environment ready, internal training scheduled
     - Phase 5: UAT sign-off, member communications drafted and approved, go-live date confirmed

6. **Flag Risks & Dependencies**
   - Identify any phase that depends on external vendor (e.g., Epic integration depends on Epic's availability)
   - Flag any gate that prospect has never done before (new legal team, first cloud vendor)
   - Identify any parallel streams that must align (legal + technical + marketing member comms)
   - Example risk: "If you're integrating Epic claims, Epic's integration team must confirm they can complete their scoping by Week 4. That's your critical path."

7. **Create Accord Workspace Format**
   - Use table format that mimics Accord software (if prospect uses Accord)
   - Include: Phase, Timeline, Give, Get, Owner (League), Stakeholder (Prospect), Status, Risk Flag
   - Make it easy for prospect to copy into their project management tool

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_Mutual_Action_Plan.md`

Format:

```
# [Account Name] Mutual Action Plan (MAP)
Created: [Date]
Go-Live Target: [Date]
Total Timeline: [Weeks] weeks from kickoff
Reverse-Engineered From: [Go-live date]

## Executive Summary
Timeline to [Go-Live Date]: [X weeks from today]
Critical Path Gate: [Phase that takes longest]
Key Assumption: [Any assumption that could break timeline, e.g., "Epic integration scope is confirmed by Week 2"]
Sponsor: [Executive name and title]

## Phase-By-Phase Breakdown

### Phase 1: Executive Approval & Discovery (Weeks 0-2)
**Go-Live Reference Point**: Week -18 from go-live

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| MSA/SOW | Draft agreements | Signed MSA, SOW | Dallas / Prospect Legal | [Date] | Pending |
| Discovery Call | Facilitation, requirements doc | Business requirements, use cases | Dallas / Prospect PM | [Date] | Pending |
| Project Sponsor | Recommendation, alignment | Named sponsor (CFO/CEO level) | Dallas / Prospect Exec | [Date] | Pending |
| Budget Approval | Financial impact template | Budget approved, allocation confirmed | Dallas / Prospect Finance | [Date] | Pending |

**Gate to Phase 2**: All Gets completed. Moving to Technical Scoping.

---

### Phase 2: Technical Scoping & InfoSec Initiation (Weeks 2-4)
**Go-Live Reference Point**: Week -14 from go-live

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| Technical Architecture | Detailed design doc, data flow | Reviewed and approved by CTO | Dallas / Prospect CTO | [Date] | Pending |
| Data Integration Plan | API spec, SFTP config, refresh cycles | Validated by your technical team | Dallas / Prospect IT | [Date] | Pending |
| InfoSec Questionnaire Response | Comprehensive security docs | Questionnaire reviewed, follow-ups scheduled | Dallas / Prospect InfoSec | [Date] | Pending |
| API Sandbox Access | Sandbox environment provided | Sandbox testing begins, API validation | Dallas / Prospect Tech | [Date] | Pending |

**Gate to Phase 3**: CTO approval of technical approach. InfoSec process started.

---

### Phase 3: Legal/InfoSec Review & Procurement (Weeks 4-8)
**Go-Live Reference Point**: Week -10 from go-live

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| SOC 2 Attestation | SOC 2 Type II cert, penetration test results | Reviewed and approved by InfoSec | Dallas / Prospect InfoSec | [Date] | Pending |
| HIPAA BAA | Business associate agreement draft | Reviewed and signed by Legal | Dallas / Prospect Legal | [Date] | Pending |
| Contract Negotiation | MSA with standard terms | Negotiation complete, final agreement signed | Dallas / Prospect Legal | [Date] | Pending |
| Procurement Approval | Budget impact doc, vendor onboarding | Procurement sign-off, budget allocated | Dallas / Prospect Procurement | [Date] | Pending |

**Gate to Phase 4**: All legal agreements signed. InfoSec clearance obtained.

---

### Phase 4: Data Integration & Configuration (Weeks 8-14)
**Go-Live Reference Point**: Week -6 from go-live

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| Data Mapping | Complete mapping doc, transformation rules | Data validation, mapping approval | Dallas / Prospect Data Team | [Date] | Pending |
| System Configuration | Environment setup, member communication templates | Configuration review, approval | Dallas / Prospect Product PM | [Date] | Pending |
| Integration Testing | API testing, data flow validation | Test execution, sign-off | Dallas / Prospect QA | [Date] | Pending |
| UAT Plan | Test scenarios, expected outcomes | Resources assigned for UAT, timeline confirmed | Dallas / Prospect Project Lead | [Date] | Pending |

**Gate to Phase 5**: Data integration validated, UAT environment ready.

---

### Phase 5: Testing & Go-Live Readiness (Weeks 14-18)
**Go-Live Reference Point**: Week -2 from go-live

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| UAT Execution Support | Test execution support, issue tracking | UAT completion, issue resolution | Dallas / Prospect QA | [Date] | Pending |
| Performance Validation | Load testing, scaling validation | Confirmation system handles expected load | Dallas / Prospect Tech | [Date] | Pending |
| Go-Live Playbook | Runbook, rollback plan, escalation contacts | Review and approval | Dallas / Prospect Ops | [Date] | Pending |
| Member Communications | Email/SMS templates, FAQs | Final member communication approved | Dallas / Prospect Comms | [Date] | Pending |

**Gate to Phase 6**: UAT complete, go-live date confirmed.

---

### Phase 6: Go-Live & Launch (Weeks 18+)
**Go-Live Reference Point**: Week 0 (Go-Live)

| Item | League Provides (Give) | Prospect Delivers (Get) | Owner | Due Date | Status |
|------|----------------------|-------------------------|-------|----------|--------|
| Go-Live Support | 24/7 support, daily stand-ups, performance monitoring | Go-live execution, member activation launch | Dallas / Prospect Ops | [Go-Live Date] | Pending |
| Day 1-5 Monitoring | Real-time monitoring, issue resolution | Production data monitoring, issue escalation | Dallas / Prospect Ops | [Go-Live Date] | Pending |
| Success Metrics Baseline | Baseline metric collection, reporting dashboard | Member adoption tracking, performance validation | Dallas / Prospect Analytics | [1 week post] | Pending |

**Success Criteria**: System live, members activated, zero critical issues.

---

## Critical Path Analysis

**Longest Gate**: [Phase name, typically Legal/Procurement]
**Duration**: [X weeks]
**Bottleneck**: [What/who is causing delay]
**Mitigation**: [How to compress timeline]

**Example**: "Legal review is your critical path at 4 weeks. Mitigation: Start legal review in parallel with technical scoping (Week 2) instead of after technical sign-off. This compresses your overall timeline by 2 weeks."

## Risk Flags

1. **Risk**: [Risk 1]
   **Likelihood**: High/Medium/Low
   **Impact**: [If this happens, go-live slips X weeks]
   **Mitigation**: [How to prevent]

2. **Risk**: Epic integration scope not confirmed by Week 2
   **Likelihood**: Medium
   **Impact**: Technical scoping slips 2 weeks, overall timeline slips 1 week
   **Mitigation**: Dallas to contact Epic integration team directly in Week 1 to confirm scope and availability

3. **Risk**: Procurement cycle longer than 4 weeks (if new vendor type for this account)
   **Likelihood**: Medium
   **Impact**: Overall timeline slips 1-2 weeks
   **Mitigation**: Start procurement process in parallel with legal (Week 2) instead of after legal completion

## Success Metrics Post-Launch

- **Metric 1**: [Member adoption rate by Day 5]
- **Metric 2**: [System uptime by Week 2]
- **Metric 3**: [Engagement metric baseline by Week 4]
- **Metric 4**: [Support ticket volume and resolution time]

## Sign-Off

**For [Account Name]**:
- Sponsor: [Name, Title, Signature]
- Project Lead: [Name, Title, Signature]
- Date: [Date]

**For League**:
- Dallas Andrews, Enterprise Sales AE
- Date: [Date]
```

## Examples

### Compliant MAP (April Go-Live)
**Go-Live Date**: April 15, 2026
**Today**: January 15, 2026 (13 weeks away)
**Reverse Engineering**:
- Week -18 (Jan 15): Kickoff / Executive approval
- Week -14 (Feb 12): Technical scoping complete
- Week -10 (Mar 12): Legal/InfoSec complete
- Week -6 (Apr 2): Data integration complete
- Week -2 (Apr 9): UAT complete
- Week 0 (Apr 15): Go-Live

**Critical Path**: Legal review takes 4 weeks (Feb 12 - Mar 12). InfoSec takes 2 weeks (Feb 12 - Feb 26). Parallel execution saves 2 weeks.

**Risk Flag**: If Legal review starts after technical scoping, timeline compresses to 10 weeks, missing April 15. Mitigation: Start legal review on Feb 12 (same day as technical scoping kickoff).

### Non-Compliant MAP
"We'll aim to go live soon. Let's figure out timing as we go. It should be fast because our solution is innovative and best-in-class."
Issue: No reverse-engineered timeline, no phase gates, no realistic procurement cycles, uses FORBIDDEN WORDS, no Give/Gets, no risk mitigation.

### Compliant Risk Flag
**Risk**: Your CTO is new (6 months in role). May request extensive architecture review and validation.
**Likelihood**: Medium-High
**Impact**: Technical scoping takes 3 weeks instead of 2. Overall timeline slips 1 week.
**Mitigation**: Schedule technical deep-dive with CTO in Week 1 to establish credibility and confidence in our architecture. Provide third-party technical references if needed.

### Non-Compliant Risk Flag
"We might have delays if your team is slow."
Issue: Vague, blame-shifting, no specific risk, no mitigation plan.
