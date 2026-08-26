---
name: intradiem-roi-business-case
description: CFO / Economic-Buyer Economic Impact Statement builder for Intradiem. Triggers once an Economic Buyer (CFO, VP Finance, COO, VP/SVP Operations or Customer Care) is identified. Extracts operational and financial data from call transcripts across contact-center AND back-office workforces (agent and back-office FTE counts, AHT or cost-per-transaction, shrinkage/idle time, backlog, attrition, training load, vendor/WFM spend, budgets) and generates a 1-page business case with Current State, Projected Impact, Cost of Inaction, and Implementation Timeline. Trigger on "build the business case for [account]", "ROI for [account]", "economic impact statement", "CFO case", or after any call where workforce cost metrics are discussed. Built for the GTM Engineer to convert operational discovery into financial justification.
---

# Intradiem ROI / Business Case Engine

## Scope reminder (read first)
Intradiem sells **Dynamic Workforce Orchestration** for large, structured workforces —
**contact centers AND back offices** (claims, lending/underwriting, billing, field
dispatch, fulfillment, care teams) — across **Healthcare, Financial Services,
Insurance, Retail, Telecom, Utilities.** Build the case around the workforce and
vertical in front of you, not a generic "call center." The value mechanic is
recovering productive capacity from idle/downtime in real time and redirecting it to
backlogs, training, and SLA protection — in both the front and back office.

## When this skill applies
- Trigger on identification of an Economic Buyer (CFO, VP Finance, COO, VP/SVP
  Operations or Customer Care)
- Run after any call where workforce cost metrics are discussed
- Run when a prospect shares budget constraints or efficiency targets
- Run before any business-case presentation or formal proposal

## Background
Intradiem sells guaranteed, measurable results — so the business case is the deal.
This skill converts operational discovery (idle time, backlog, handle time/throughput,
training load, attrition) into the financial language the Economic Buyer rewards:
recovered capacity, cost relief, protected SLAs, margin. It bridges the operational
floor — front office or back — and the finance org.

## Pipeline

### 1. Extract economic data from transcripts/notes
Pull every quantified metric mentioned. Use the set that fits the workforce:
- Total FTEs — contact-center agents and/or back-office processors (and locations / BPO mix)
- Front office: AHT, contact volume, service-level / occupancy targets
- Back office: cases/transactions per day, backlog size, cost-per-transaction, SLA/turnaround targets
- Shrinkage or idle/downtime rate (paid time not on value work)
- Attrition / turnover rate and cost-to-hire/onboard
- Training load (hours, and whether staff are pulled off queues/cases to do it)
- Fully-loaded FTE cost
- Current WFM / automation / QA vendor spend
- Any stated efficiency, compliance, or cost-reduction target
Flag missing data as **"Ask on Next Call."**

### 2. Identify the pain-driven ROI lever
Pick the largest operational cost as the primary lever:
- Idle/downtime not reallocated to backlog or training (front or back office)
- Capacity / overtime / seasonal hiring
- Backlog or turnaround-time penalties (back office)
- Attrition and onboarding ramp cost; burnout-driven quality loss
- Vendor redundancy (multiple tools doing one job)

### 3. Pull Intradiem impact ranges (verified only)
Route **every** impact number through `intradiem-verified-metrics` (e.g., capacity
recovered per FTE, idle-time reallocated, handle-time/throughput improvement, overtime
reduction, attrition improvement, training delivered without pulling staff off
queues). Match the proof point to the prospect's vertical where possible. Never invent
a number. Respect 1:1 vs. 1:many approval tiers. Where a verified range isn't
available, leave the slot as `[VERIFY]`.

### 4. Build the four sections
Apply the verified ranges to the prospect's baseline to produce account-specific math.
Frame Cost of Inaction as a **monthly** bleed to create urgency.

## Output

Save as: `[Account]_Business_Case.md`

```
# [Account Name] Economic Impact Statement
Date: [Date]
Vertical: [Healthcare / Financial Services / Insurance / Retail / Telecom / Utilities]
Workforce in scope: [Contact center / Back office / Both]
Economic Buyer: [Name, Title]

## Current State
- FTEs in scope: [X]   (Locations / BPO mix: [X])
- Throughput: [AHT + volume  OR  cases/transactions per day + backlog]
- Shrinkage / idle rate: [X%]
- Attrition: [X%]   Cost-to-hire/onboard: [$X]
- Training load: [X hrs]   (Staff pulled off queues/cases: [Y/N])
- Fully-loaded FTE cost: [$X]
- Current WFM / automation vendor stack: [List]   Annual spend: [$X]

## Projected Impact (12-Month Horizon)
- Capacity recovered: [VERIFY range] x [FTEs] = [recovered hours / FTE-equivalents]
- Idle-time → backlog/training reallocation: [$X annual]
- Overtime / seasonal hiring avoided: [$X]
- Attrition improvement: [VERIFY %] = [$X onboarding cost avoided]
- Total annual impact: [$X to $Y]

## Cost of Inaction
- Monthly cost of recoverable-but-lost capacity: [$X]
- Monthly overtime / contractor premium / backlog penalty: [$X]
- Total monthly bleed: [$X]

## Implementation Timeline
- Technical scoping: 2 weeks
- Integration & configuration (WFM / CCaaS / back-office systems): 4-6 weeks
- Procurement & legal: 3-4 weeks
- InfoSec review: 2-3 weeks
- Executive sign-off: 1-2 weeks
- Go-live: [Estimated date]
- Total: 12-18 weeks from kickoff

## Data Gaps & Next Steps
- [Gap] - Ask: [Specific question]
- [Gap] - Ask: [Specific question]
```

## Constraints
- Build around the actual workforce and vertical — never default to "call center."
- Use only numbers extracted from the prospect, plus verified Intradiem ranges.
- Every impact stat verified or flagged `[VERIFY]`.
- Apply Intradiem brand voice. Tone: financial, precise, no hype.
- Named output — save as a file, never chat-only.
- Show the math. A claim without arithmetic behind it doesn't ship.
