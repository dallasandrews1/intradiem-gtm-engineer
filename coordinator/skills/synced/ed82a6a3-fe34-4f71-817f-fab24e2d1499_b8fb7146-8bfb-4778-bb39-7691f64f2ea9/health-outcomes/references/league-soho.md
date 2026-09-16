# League Spectrum of Health Outcomes (SoHO)

This is League's proprietary framework for measuring and communicating health outcomes across programs, features, and platform experiences. Load this file whenever a question involves League's own programs, question bank, Pulse Checks, observation codes, or how League measures member health outcomes internally.

**Source**: Confluence — Spectrum of Health Outcomes (SoHO), SoHO Question Bank, How We Use Behavioral Science, KPIs and Success Metrics

---

## What SoHO Is

SoHO is League's internal framework for connecting what members do on the platform to meaningful health outcomes. It solves a specific problem: the link between member engagement and health status change is not direct. SoHO creates a structured way to:

- **Design** programs with intentional outcome targets
- **Evaluate** whether programs are performing at the right level
- **Collect** data at the appropriate outcome level via Pulse Checks
- **Communicate** health outcomes to payers, clients, and partners
- **Iterate** based on which upstream outcomes predict downstream ones

SoHO is used prospectively (design), retrospectively (evaluation), for data collection infrastructure, for product strategy, and for growth and marketing.

---

## The SoHO Spectrum — Nine Levels

The spectrum runs from engagement → immediate → intermediary → measurable health outcomes. Outcomes become harder to attribute to League as they move downstream, but carry more clinical and financial weight.

| Level | Category | What it captures | Indicator type | Example |
|-------|----------|-----------------|---------------|---------|
| 1 | Engagement and satisfaction | Program enrollment/completion, user satisfaction, CSAT | Engagement | % MAU enrolled; % rating program helpful |
| 2 | Immediate outcomes | Improved member understanding or awareness of a health topic | Leading — Moderate | Knowledge gain: "more or a lot more" vs. before |
| 3 | Intervention opportunities | Insights into obstacles, priorities, interest in addressing a health concern | Leading — Moderate | Barrier identification; readiness to act |
| 4 | Connection to other program/pathway | Member enrolls in another program or purchases a relevant product | Directional | Cross-program enrollment rate |
| 5 | Behavior change progress | Member shows progress on intentions, goal setting, planning, action | Leading — Strong | Self-efficacy score; behavioral intention score |
| 6 | Action completed | Member books an appointment, screening arranged, action taken as a result | Lagging — Direct action | "As a result of this program, did you [action]?" — Yes |
| 7 | Self-reported outcomes | Improvements to validated outcome measures | Lagging — Self-reported | PHQ-2 score change; confidence managing blood sugar |
| 8 | Biometric / verified outcomes | Improvements from connected devices, lab sources, EMR/Rx data | Lagging — Loop-closing | HbA1c lab result; BP reading from PC Health Station; PBM fill data |
| 9 | Outcome / habit maintenance | Durable changes maintained over months or years; ROI demonstrated | Lagging — Long-term | 6-month behavior retention; PMPM cost reduction |

> **Key framing**: League can most directly influence levels 1–6. Levels 7–9 require data integration pathways (lab feeds, PBM, EHR/EMR) and are harder to attribute to League alone. The further downstream, the more clinically meaningful — and the more infrastructure is required.

---

## How SoHO Maps to Indicator Types and HEDIS/Stars

| SoHO level | Skill indicator type | HEDIS / Stars connection |
|-----------|---------------------|------------------------|
| 1 — Engagement | Engagement | No direct quality measure |
| 2 — Knowledge gain | Leading — Moderate | No direct HEDIS measure; health literacy mechanism |
| 3 — Intervention opportunity | Leading — Moderate | SDOH screening (SNS-E); AHC HRSN |
| 4 — Connection to program | Directional | Indirect — increases probability of gap closure |
| 5 — Behavior change progress | Leading — Strong | Self-efficacy → CDC-H, CBP, MAD, MAH; Intention → MAD, IET-I |
| 6 — Action completed | Lagging — Direct action | CDC-E, CDC-K, FUH-7, IET-I — supplemental data eligible |
| 7 — Self-reported outcomes | Lagging — Self-reported / Loop-closing | PHQ-2 → DSF; BP self-report → CBP analog; HbA1c → CDC-H analog |
| 8 — Biometric / verified | Lagging — Loop-closing | CBP (BP Station); CDC-H (HbA1c lab); MAD/MAH (PBM PDC) |
| 9 — Habit maintenance | Lagging — Long-term | PCR readmissions; Stars PMPM; HOS physical/mental function |

---

## League's Behavioral Science Foundation

Two models underpin SoHO levels 2–6 — these are the "why it works" behind League's questions.

### Health Action Process Approach (HAPA)
Programs are matched to the member's stage of change. SoHO question placement maps to HAPA stage.

| Stage | Description | What League targets | SoHO questions used |
|-------|-------------|---------------------|-------------------|
| Pre-intender | Not engaging, does not intend to | Risk/benefit communication; outcome expectancies; knowledge confidence | knowledge_confidence_start; outcome_expectancies_end |
| Intender | Not engaging, intends to | Action and coping planning; barrier self-efficacy; behavioral intention | task_self_efficacy_start; intentions_end; barrier_self_efficacy_end |
| Actor | Currently engaging | Monitoring; relapse prevention; habit formation | task_self_efficacy_end; program_action_end; habit_formation_end |

### Self-Determination Theory (SDT)
Drives intrinsic engagement (SoHO level 1 and upstream of levels 2–5):
- **Competence** — programs build mastery and skill
- **Relatedness** — person-first language, vignettes, normalization
- **Autonomy** — self-selected programs, member-paced completion

---

## SoHO Question Bank — Full Standardized Set

These are League's standardized Pulse Check questions with observation codes and LOINC mappings. Use exact wording and codes when advising content or product teams.

### Confidence scale (shared across multiple questions)
1 = Not at all confident · 2 = A little confident · 3 = Somewhat confident · 4 = Quite confident · 5 = Very confident · 99 = Prefer not to say
LOINC codes: LA30024-6 · LA30026-1 · LA30027-9 · LA30028-7 · LA30029-5 · LA30122-8
Reporting convention: "Quite + Very confident" combined = positive response rate

### Yes/No/Not sure scale (shared)
1 = Yes · 0 = No · 2 = I'm not sure · 99 = Prefer not to say
LOINC codes: LA33-6 · LA32-8 · LA14072-5 · LA30122-8

---

### START questions — capture at program enrollment

| Question | Code | SoHO level | Indicator type | Pre/post pair |
|----------|------|-----------|---------------|--------------|
| "Based on what you know today, how confident are you in your knowledge about [program goal]?" | `knowledge_confidence_[program]_start` | 2 | Leading — Moderate | → `knowledge_confidence_[program]_end` |
| "How confident are you in your current ability to [insert program goal/desired action]?" | `task_self_efficacy_[program]_start` | 5 | Leading — Strong | → `task_self_efficacy_[program]_end` |

Both use the confidence scale above.

---

### END questions — capture at program completion

**Program goal achievement** *(primary outcome question — include in every program)*
"Overall, I feel this program has put me on the right path to [insert primary outcome of interest]."
Code: `program_goal_[program]_end`
Scale: Yes/No/Not sure
SoHO level: 5–6 | Type: Lagging — Moderate
HEDIS: PCO Goal Attainment analog (MY2027 D-SNP/C-SNP)
Note: Needs FHIR documentation layer to become fully PCO-eligible

**Knowledge — binary**
"This program gave me new information to help me [insert program goal/desired action]."
Code: `knowledge_[program]_end`
Scale: Yes/No/Not sure
SoHO level: 2 | Type: Leading — Moderate

**Knowledge — comparative**
"Compared to before you completed this program, rate your current level of understanding of [insert program goal/desired action]."
Code: `knowledge2_[program]_end`
Scale: 1 A lot more · 2 More · 3 About the same · 4 Less · 5 A lot less · 6 Not sure · 99 Prefer not to say
League codes (not LOINC): lot_more · more · about_same · less · lot_less
SoHO level: 2 | KPI: % "more or a lot more" vs. before

**Knowledge confidence (post)**
"After completing this program, how confident are you in your knowledge about [program goal]?"
Code: `knowledge_confidence_[program]_end`
Scale: confidence scale
SoHO level: 2 | Pre/post pair with `_start`

**Task self-efficacy (post)**
"After completing this program, how confident are you in your ability to [insert program goal/desired action]?"
Code: `task_self_efficacy_[program]_end`
Scale: confidence scale
SoHO level: 5 | Type: Leading — Strong
HEDIS: CDC-H, CBP, MAD, MAH (condition-dependent)
Pre/post pair with `_start`

**Barrier self-efficacy (post)**
"After completing this program, how confident are you that you'll be able to overcome hurdles that might make it harder to act on your plan?"
Code: `barrier_self_efficacy_[program]_end`
Scale: confidence scale
SoHO level: 5 | Type: Leading — Strong
Behavioral basis: Coping planning (HAPA Actor stage)

**Outcome expectancies (post)**
"After completing this program, I have a better understanding of how [insert program goal] can benefit my health."
Code: `outcome_expectancies_[program]_end`
Scale: Yes/No/Not sure
SoHO level: 2–3 | Type: Leading — Moderate
Behavioral basis: Social Cognitive Theory — motivational mediator

**Behavioral intention (post) — 7-point Likert** *(use for HEDIS/Stars reporting)*
"After completing this program, I intend to [insert program goal/desired action]."
Code: `intentions_[program]_end`
Scale: 1 Strongly disagree · 2 Disagree · 3 Slightly disagree · 4 Neutral · 5 Slightly agree · 6 Agree · 7 Strongly agree · 99 Prefer not to say
LOINC: LA15236-5 · LA15773-7 · LA15234-0 · LA14786-0 · LA15235-7 · LA15774-5 · LA15237-3 · LA30122-8
SoHO level: 5 | Type: Leading — Strong
HEDIS: MAD, MAH, CDC-T/E/K, FUH-7, IET-I
Reporting: "Agree or above" = slightly agree + agree + strongly agree

**Behavioral intention (post) — 5-point scale** *(do not mix with 7-point in same analysis)*
"After completing this program, I intend to [insert program goal/desired action]."
Code: `intentions2_[program]_end`
Scale: 1 Not at all · 2 A little bit · 3 Somewhat · 4 Quite a bit · 5 Very much · 6 Prefer not to say

**Goal-setting confidence (post)**
"After completing this program, how confident are you in your ability to set a [insert behavior] goal?"
Code: `goal_setting_confidence_[program]_end`
Scale: confidence scale
SoHO level: 5 | PCO-adjacent — maps to NCQA PCO goal identification component

**Action completed (post)** *(highest-value lagging indicator without clinical integration)*
"As a result of this program, did you [insert program goal/desired action]?"
Code: `program_action_[program]_end`
Scale: 3 Yes, I did (action-completed) · 2 Not yet, but I plan to (action-planned) · 1 No, and I don't plan to (no-action-no-plan) · 99 Prefer not to say (LA30122-8)
SoHO level: 6 | Type: Lagging — Direct action
HEDIS: CDC-E, CDC-K, BCS scheduling — supplemental data eligible with plan data agreement

**Sleep quality** *(fully LOINC-coded PRO)*
"In the past 7 days, my sleep quality was:"
Code: `61987-4` (LOINC)
Scale: 5 Very poor (LA9615-1) · 4 Poor (LA8969-3) · 3 Fair (LA8968-5) · 2 Good (LA8967-7) · 1 Very good (LA13913-1) · 99 Prefer not to say (LA30122-8)
SoHO level: 7 | Type: Lagging — Self-reported PRO
Note: Highest data standardization of any SoHO question — FHIR/ECDS pathway ready

**Habit formation (post)** *(challenge programs)*
"Did this challenge help you start a [insert challenge habit]?"
Code: `habit_formation_[challenge]_end`
Scale: Yes/No/Not sure
SoHO level: 5–6 | Behavior change / action

---

## Observation Code Conventions

Format: `[question_type]_[program_name]_[placement]`

Placement values:
- `_start` — program enrollment / first activity
- `_end` — program completion
- `_m1`, `_m2`, `_m3` — mid-program milestone placements

**Pre/post delta rules:**
- Same question type required at both `_start` and `_end`
- Member ID linkage required for matched cohort analysis
- Without member ID linkage: delta is directional only, not a proven individual-level change

**For product teams:** LOINC-coded questions are the highest data quality — interoperable with EHR systems and eligible for ECDS/hybrid reporting pathways. Prioritize LOINC codes when building data infrastructure.

---

## SoHO KPIs — What the Health Journey Team Officially Tracks

| Funnel | Metric | SoHO level |
|--------|--------|-----------|
| Top | % MAU viewed health program library | 1 |
| Top | % MAU viewed a health program | 1 |
| Middle | % MAU enrolled in a health program | 1 |
| Middle | % MAU who viewed a Pulse Check | 1/2 |
| Bottom | % MAU completed a health program | 1 |
| Bottom | % users rating "more or a lot more" knowledge | 2 |
| Bottom | % members rating program helpful or very helpful (CSAT) | 1 |

---

## SoHO Gaps and Honest Caveats

These are limitations the SoHO framework itself acknowledges in Confluence — always reflect these in the Honest Caveat section of any outcome record:

- Remote, long-term outcomes (sustained LDL change, 12-month BP control) are hard for League to ascertain without clinical data integration
- Outcomes change at different speeds — mood changes fast, HbA1c changes slowly
- Many hidden variables influence health independently of League programs
- Behavioral changes (self-efficacy, intention) may be perceived as too "distant" from clinical outcomes by some payer audiences — always pair with whatever downstream data is available
- Upstream outcomes can be tracked but won't necessarily lead to downstream outcomes — the logic model hypothesis should be stated as a hypothesis, not a proven mechanism, unless validated with actual longitudinal data
