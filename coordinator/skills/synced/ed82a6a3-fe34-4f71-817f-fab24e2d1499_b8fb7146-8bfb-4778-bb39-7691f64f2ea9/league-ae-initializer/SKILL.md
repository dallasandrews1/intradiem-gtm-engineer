---
name: league-ae-initializer
version: 1.0.0
description: AE system initialization and Canon lock. Indexes AE_Deal_Accelerator_Canon.md, BDR_Architect_Canon.md, and League_Payer_Value_Prop.pdf to establish session-wide constraints. Boot sequence for all downstream AE skills.
---

## When this skill applies

- Run at the start of every AE session
- Run before executing any other League skills
- Run when onboarding a new AE to Dallas Andrews' playbook
- Run when shifting accounts or resetting the operating model

## Background

The AE Initializer is the foundational boot sequence. It indexes all canon documents, locks the session-wide constraints, and ensures every subsequent skill operates under the same disciplined framework. Without this initialization, individual skills may drift from the unified operating model.

## Workflow Steps

1. **Index Canon Documents**
   - Load AE_Deal_Accelerator_Canon.md
   - Load BDR_Architect_Canon.md
   - Load League_Payer_Value_Prop.pdf
   - Confirm all three documents are accessible in the session

2. **Lock Canon Constraints**
   - Extract all constraints from canon documents
   - Apply the following shared constraints to the session:
     - **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
     - **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
     - **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
     - **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
     - **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
     - **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
     - **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

3. **Confirm Buying Committee Tier Structure**
   - Verify 4-tier buying committee mapping is locked:
     - **Tier 1 (Champion Layer)**: Initial contact, usually mid-level operator or digital health director
     - **Tier 2 (Economic Buyer Layer)**: CFO, VP Finance, VP Operations. Controls budget, approval authority.
     - **Tier 3 (Technical/Legal Layer)**: CTO, VP IT, General Counsel, InfoSec. Controls feasibility and risk gates.
     - **Tier 4 (Executive Sponsor)**: Chief Medical Officer, Chief Member Experience Officer. Rarely engaged until paper process; validates clinical/member impact.

4. **Load Value Proposition Context**
   - Extract League's core value drivers from Payer Value Prop PDF:
     - Primary driver: Operational Relief (cost reduction, staffing efficiency, member experience improvement)
     - Secondary driver: Compliance and risk mitigation
     - Tertiary driver: Data and analytics (not lead with)
   - Lock this into session memory for all outreach

5. **Validate Persona Rules**
   - Confirm persona-to-messaging alignment:
     - **CFO/VP Finance**: Metrics-driven. Lead with ROI, payback period, cost avoidance.
     - **VP Operations**: Process-driven. Lead with workflow improvement, FTE elimination, operational timeline.
     - **VP Digital Health/Member Experience**: Engagement-driven. Lead with NPS, retention, engagement uplift.
     - **CTO/VP IT**: Technical risk-driven. Lead with integration complexity, data security, scalability.
     - **General Counsel**: Risk-driven. Lead with contract negotiation, indemnification, compliance.

6. **Set Session Output Directory**
   - Create session workspace: `/Accounts/` directory structure
   - Each account gets its own folder: `/Accounts/[Account Name]/`
   - All outputs saved there with consistent naming convention

7. **Confirm AE Identity & Tier-1 Account List**
   - Confirm AE name (Dallas Andrews)
   - Load list of Tier-1 accounts assigned to this AE
   - Store account list in session memory for multi-account orchestration

## Canon Constraints

All downstream skills inherit these rules:

- **Tenbit++ Framework**: Observation → Insight → Value → Next Step
- **Pincer Rule**: VPs and Directors receive Operational Relief messaging, never Brand Vision
- **Brand-Light Execution**: No League mentions Days 1-5. Frame as category solution.
- **FORBIDDEN WORDS**: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `Session_Init_[Date].md`

Format:

```
# AE Session Initialization
Date: [Date]
AE: Dallas Andrews

## Canon Documents Loaded
- AE_Deal_Accelerator_Canon.md: [Confirmed/Failed]
- BDR_Architect_Canon.md: [Confirmed/Failed]
- League_Payer_Value_Prop.pdf: [Confirmed/Failed]

## Session Constraints Locked
- Tenbit++ Framework: Active
- Pincer Rule: Active
- Brand-Light Execution: Active
- FORBIDDEN WORDS: [List locked]
- Strict Punctuation: Active
- Named Outputs: Active
- MEDDPICC Discipline: Active

## Buying Committee Tier Structure Confirmed
- Tier 1 Champion Layer: [Description]
- Tier 2 Economic Buyer Layer: [Description]
- Tier 3 Technical/Legal Layer: [Description]
- Tier 4 Executive Sponsor Layer: [Description]

## Persona Rules Locked
- CFO/VP Finance: Metrics-driven, ROI/payback focus
- VP Operations: Process-driven, FTE/timeline focus
- VP Digital Health/Member Experience: Engagement-driven, NPS/retention focus
- CTO/VP IT: Technical risk-driven, integration/security focus
- General Counsel: Risk-driven, contract/compliance focus

## Value Proposition Context Loaded
- Primary Driver: Operational Relief
- Secondary Driver: Compliance and Risk Mitigation
- Tertiary Driver: Data and Analytics

## Tier-1 Accounts Assigned
[List all accounts]

## Session Ready
All systems locked. Ready to execute downstream skills.
```

## Examples

### Compliant Session Init
"Session initialized. All canon documents loaded. Tenbit++ Framework, Pincer Rule, and FORBIDDEN WORDS list locked. Buying committee structure confirmed (4 tiers). Persona rules active. Value prop context loaded: Operational Relief as primary driver. Tier-1 accounts loaded (7 accounts). Session workspace created at /Accounts/. Ready to execute league-full-pipeline, league-deal-desk, and competitive intelligence workflows."

### Non-Compliant Initialization Attempt
Attempting to run league-full-pipeline without initializing first will result in constraint drift and messaging inconsistency. Always run league-ae-initializer first.
