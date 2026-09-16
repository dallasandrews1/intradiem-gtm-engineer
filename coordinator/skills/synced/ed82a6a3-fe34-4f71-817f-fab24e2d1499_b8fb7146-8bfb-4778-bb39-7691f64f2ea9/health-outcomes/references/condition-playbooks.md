# Condition Playbooks

Pre-built outcome stacks for the five highest-priority conditions. Each playbook covers the full outcome picture: HEDIS measures, Stars weight, PROs, SDOH factors, humanistic outcomes, and value translation hooks.

Load this file when the question starts with a condition or population rather than a measure.

---

## How to Use a Playbook

1. Identify the condition and population (commercial, Medicaid, Medicare/MA)
2. Pull the relevant measures from the stack — not all measures apply to all product lines
3. Layer in PRO and humanistic outcomes to complete the picture
4. Use the value translation hooks to frame for the right audience

---

## Playbook 1: Diabetes

### Condition Overview
Most measured condition in HEDIS and Stars. Affects ~15% of Medicare Advantage members. High comorbidity burden (hypertension, CKD, depression, obesity). Significant SDOH interaction (food insecurity, financial toxicity of medications and supplies).

### Measure Stack

| Measure | Framework | Product line | Stars weight |
|---------|-----------|-------------|-------------|
| Comprehensive Diabetes Care — HbA1c Testing (CDC-T) | HEDIS | Commercial, Medicaid, Medicare | — |
| Comprehensive Diabetes Care — HbA1c Control <8% (CDC-H) | HEDIS / Stars | All | Double |
| Comprehensive Diabetes Care — HbA1c Poor Control >9% (CDC-P) | HEDIS / Stars | All | Double (*lower = better*) |
| Comprehensive Diabetes Care — Eye Exam (CDC-E) | HEDIS / Stars | All | Standard |
| Comprehensive Diabetes Care — Kidney Health Evaluation (CDC-K) | HEDIS / Stars | All | Standard |
| Blood Pressure Control for Patients with Diabetes (BPD-E) | HEDIS MY2026 | All | — (new) |
| Controlling High Blood Pressure (CBP) | HEDIS / Stars | All | Double |
| Statin Use in Persons with Diabetes (SPD) | HEDIS / Stars | Medicare | Triple |
| Medication Adherence — Diabetes (MAD) | Stars | Medicare | Triple (2027) |
| Depression Screening and Follow-Up (DSF) | HEDIS | All | — |

### PRO Instruments
- **PHQ-9**: Screen for depression comorbidity (highly prevalent in diabetes)
- **PROMIS Physical Function**: Functional impact of neuropathy, fatigue
- **PROMIS Pain Interference**: Relevant for diabetic neuropathy
- **DDS (Diabetes Distress Scale)**: Specific to diabetes-related emotional burden — not in HEDIS but highly predictive of self-management

### SDOH Factors
- **Food insecurity** (Z59.4): Direct impact on glycemic control; relevant to AHC HRSN screening
- **Financial toxicity**: Insulin cost is a top driver of non-adherence; GLP-1 cost is a current crisis point
- **Transportation**: Missed eye and nephrology appointments
- **Health literacy**: Carbohydrate counting, glucose monitoring, sick day management

### Humanistic Outcomes
- Fear of complications (blindness, amputation, dialysis) — often unaddressed, drives avoidance
- Grief and identity disruption at diagnosis
- Self-efficacy around glucose management — strongest predictor of HbA1c control
- Dietary restriction impact on social participation and cultural identity

### Value Translation Hooks
- **Payer**: CDC composite + SPD + MAD = three Stars measures in one condition; MAD returns to triple-weight in 2027
- **Clinical**: HbA1c control reduces microvascular complications by 35–40%; every 1% HbA1c reduction = ~20% reduction in diabetes-related complications
- **Leadership**: Diabetes is the highest-cost chronic condition in most MA books; gap closure programs with demonstrated HbA1c improvement are tier-1 evidence for plan RFPs
- **Product**: HbA1c result + date + value = CDC numerator event; needs to be structured, not free-text

---

## Playbook 2: Hypertension

### Condition Overview
Most prevalent chronic condition in Medicare populations (~70% of MA members). Largest single contributor to cardiovascular events, stroke, and CKD. Strong SDOH drivers (stress, diet, access). Often asymptomatic — member engagement is the primary challenge.

### Measure Stack

| Measure | Framework | Product line | Stars weight |
|---------|-----------|-------------|-------------|
| Controlling High Blood Pressure <140/90 (CBP) | HEDIS / Stars | Commercial, Medicaid, Medicare | Double |
| Blood Pressure Control for Patients with Diabetes (BPD-E) | HEDIS MY2026 | All | — (new, ECDS) |
| Medication Adherence — Hypertension/RAS (MAH) | Stars | Medicare | Triple (2027) |
| Statin Therapy for Cardiovascular Disease (SPC) | HEDIS / Stars | Medicare | Double |

### PRO Instruments
- **PROMIS Fatigue**: Side effects of antihypertensives affect adherence
- **VR-12 / HOS**: Physical component — relevant for cardiovascular functional status
- **PHQ-9**: Depression is a common driver of medication non-adherence

### SDOH Factors
- **Food insecurity / diet**: Sodium, DASH diet adherence
- **Stress and neighborhood safety**: Chronic stress is a direct physiological driver of hypertension
- **Financial toxicity**: Even generic antihypertensives can be a barrier at scale
- **Employment and work conditions**: Shift work, physical labor, limited PTO for appointments

### Humanistic Outcomes
- Asymptomatic condition = low perceived urgency; engagement challenge is motivational, not informational
- Medication side effects (fatigue, sexual dysfunction) rarely disclosed but major adherence driver
- Agency and control — members who understand their BP numbers and trends feel more capable

### Value Translation Hooks
- **Payer**: CBP is double-weighted; MAH is triple-weight returning 2027; together they're the highest-leverage measure pair in cardiovascular care
- **Clinical**: 10 mmHg systolic reduction = ~20% reduction in major cardiovascular events; BP control is one of the most evidence-dense interventions in medicine
- **Leadership**: Hypertension is the entry point to most cardiovascular cost — preventing one MI saves $50,000–$100,000+; this is the clearest PMPM story in chronic care
- **Product**: BP reading + date = CBP numerator event (if <140/90); home BP monitoring data needs clinical reconciliation pathway to count in hybrid reporting

---

## Playbook 3: Behavioral Health (Depression + SUD)

### Condition Overview
Most rapidly growing cost and quality priority in health plans. Depression affects ~20% of MA members; SUD affects ~10%. Strong comorbidity with every chronic disease. Significant stigma and access barriers. Behavioral health measures are among the most poorly performed in HEDIS.

### Measure Stack

| Measure | Framework | Product line | Stars weight |
|---------|-----------|-------------|-------------|
| Depression Screening and Follow-Up (DSF) | HEDIS | All | — |
| Antidepressant Medication Management — Acute (AMM-A) | HEDIS | Commercial, Medicaid | — |
| Antidepressant Medication Management — Continuation (AMM-C) | HEDIS | Commercial, Medicaid | — |
| Follow-Up After Hospitalization for Mental Illness — 7-day (FUH-7) | HEDIS / Stars | All | Double (Stars) |
| Follow-Up After Hospitalization for Mental Illness — 30-day (FUH-30) | HEDIS | All | — |
| Follow-Up After ED Visit for Mental Illness (FUM) | HEDIS | All | — |
| Initiation of SUD Treatment (IET-I) | HEDIS / Stars | All | Double (Stars) |
| Engagement of SUD Treatment (IET-E) | HEDIS / Stars | All | Double (Stars) |
| Follow-Up After ED Visit for Alcohol/Drug Abuse (FUA) | HEDIS | All | — |
| Diabetes Screening for People with Schizophrenia/Bipolar (SSD) | HEDIS | All | — |

### PRO Instruments
- **PHQ-9**: Gold standard depression screener; score ≥10 triggers DSF follow-up numerator
- **GAD-7**: Anxiety; often comorbid with depression
- **AUDIT-C**: 3-item alcohol use screener; brief and validated
- **DAST-10**: Drug Abuse Screening Test
- **PROMIS Depression / Anxiety**: PROMIS versions for population-level tracking

### SDOH Factors
- **Social isolation**: Strongest SDOH predictor of depression severity
- **Housing instability**: Z59 codes; acute driver of mental health crises
- **Trauma history / ACEs**: Adverse childhood experiences — root cause for much SUD and depression
- **Employment**: Job loss, financial stress, workplace trauma

### Humanistic Outcomes
- Stigma — the felt shame of a mental health diagnosis; shapes disclosure, help-seeking, and medication acceptance
- Hope and recovery identity — "I can get better" is a clinical outcome not captured anywhere
- Relationship repair — depression and SUD devastate relationships; restoration is a patient-defined outcome
- Safety and absence of suicidal ideation — the most critical unstated outcome in BH

### Value Translation Hooks
- **Payer**: FUH-7 and IET are double-weighted in Stars; behavioral health is the #1 driver of avoidable ED and inpatient cost; 7-day follow-up post-discharge is the single highest-leverage intervention available
- **Clinical**: 60–80% of people with depression who initiate and continue treatment for 6 months achieve remission; the AMM continuation rate is a direct proxy for treatment completion
- **Leadership**: Employers and Medicaid plans rank behavioral health access as a top RFP criterion; demonstrating PHQ-9 follow-through and IET rates is a tier-1 differentiator
- **Product**: PHQ-9 ≥10 must trigger a 30-day follow-up tracking flag; IET initiation = first treatment contact within 14 days of diagnosis; system must distinguish initiation from engagement (2+ additional contacts in 34 days)

---

## Playbook 4: Heart Failure

### Condition Overview
Highest 30-day readmission rate of any condition (~25%). Primary driver of HRRP hospital penalties. Predominantly Medicare population. Rapid decompensation requires early symptom detection — a primary use case for digital health monitoring. Complex medication regimen (ACE/ARB, beta-blocker, diuretic, SGLT2i).

### Measure Stack

| Measure | Framework | Product line | Stars weight |
|---------|-----------|-------------|-------------|
| Plan All-Cause Readmissions (PCR) | Stars | Medicare | Standard |
| Follow-Up After Hospitalization for Mental Illness (FUH) | HEDIS / Stars | All | Double — BH comorbidity |
| Controlling High Blood Pressure (CBP) | HEDIS / Stars | All | Double |
| Statin Therapy for Cardiovascular Disease (SPC) | HEDIS / Stars | Medicare | Double |
| Medication Adherence — Hypertension/RAS (MAH) | Stars | Medicare | Triple (2027) — ACE/ARB |
| Care for Older Adults (COA) — Medication Review | Stars | Medicare | Standard |

### PRO Instruments
- **KCCQ (Kansas City Cardiomyopathy Questionnaire)**: Gold standard HF-specific PRO; 23 items; measures physical limitation, symptoms, quality of life, social limitation
- **PROMIS Fatigue**: Fatigue is the #1 symptom burden in HF
- **PHQ-9**: Depression affects 40% of HF patients and doubles readmission risk
- **VR-12 / HOS**: Physical and mental component scores; relevant for Medicare HF population

### SDOH Factors
- **Housing instability**: Inadequate heating/cooling dramatically worsens HF; Z59 codes
- **Food insecurity**: Dietary sodium is a direct trigger for decompensation
- **Social isolation**: No support person to recognize early symptoms or call for help
- **Transportation**: Missed follow-up appointments are primary readmission driver

### Humanistic Outcomes
- Fear of death — HF is experienced as a life-limiting diagnosis; prognosis conversations are often avoided
- Loss of identity and independence — activity limitations affect dignity and self-concept
- Caregiver burden — family members carry enormous unacknowledged load
- Advance care planning preferences — what the person wants if they decompensate

### Value Translation Hooks
- **Payer**: Every prevented readmission = ~$15,000–25,000 in avoided cost; PCR is a Stars measure; 7-day post-discharge follow-up is the highest-evidence intervention for readmission prevention
- **Clinical**: Daily weight monitoring catches fluid retention 2–4 days before hospitalization; remote monitoring + protocol-driven response is the clinical standard; SGLT2i uptake is now a quality gap
- **Leadership**: HF is the prototypical case for digital health ROI — remote monitoring has the strongest evidence base of any chronic condition digital intervention; this is the clearest story to tell health system and ACO partners
- **Product**: Daily weight event + trend analysis = early warning signal; needs threshold logic (>2 lbs/day or >5 lbs/week = outreach trigger); 7-day post-discharge contact must be documentable as a claims event or hybrid supplement

---

## Playbook 5: COPD / Respiratory

### Condition Overview
Third leading cause of death in the US. High readmission burden. Strong smoking history — tobacco cessation is both a clinical and HEDIS opportunity (new TSC-E measure in MY2026). Significant functional limitation; quality of life impact is often the patient's primary concern, not spirometry values.

### Measure Stack

| Measure | Framework | Product line | Stars weight |
|---------|-----------|-------------|-------------|
| Pharmacotherapy Management of COPD Exacerbation (PCE) | HEDIS | Commercial, Medicaid, Medicare | — |
| Use of Spirometry Testing in COPD (SPR) | HEDIS | Commercial, Medicaid | — |
| Tobacco Use Screening and Cessation Intervention (TSC-E) | HEDIS MY2026 | All (age 12+) | — (new) |
| Plan All-Cause Readmissions (PCR) | Stars | Medicare | Standard |
| Medication Adherence — various | Stars | Medicare | Triple/Single |
| Adult Immunization Status (AIS-E) — flu + pneumococcal | HEDIS / Stars | All | Standard |

### PRO Instruments
- **CAT (COPD Assessment Test)**: 8-item COPD-specific quality of life measure; score 0–40
- **mMRC Dyspnea Scale**: Simple 5-point breathlessness rating; widely used clinically
- **PROMIS Fatigue / Physical Function**: Functional limitation tracking
- **PHQ-9**: Depression highly comorbid with COPD; often undiagnosed

### SDOH Factors
- **Housing quality**: Mold, dust, indoor air quality — direct disease triggers; Z59 codes
- **Neighborhood environment**: Air quality, occupational exposures
- **Financial toxicity**: Inhalers are among the most expensive generic medications; cost is top adherence barrier
- **Social isolation**: Breathlessness limits mobility and social participation

### Humanistic Outcomes
- Breathlessness as lived experience — the visceral fear of not being able to breathe shapes every life decision
- Grief over lost activities and identity (outdoor work, sports, travel)
- Guilt and shame around smoking history — affects engagement and disclosure
- Self-efficacy around exacerbation recognition — "I know when I'm getting worse and what to do" is a life-saving outcome

### Value Translation Hooks
- **Payer**: TSC-E is new in MY2026 — early performance on a first-year measure is easier to differentiate; exacerbation prevention directly reduces inpatient cost (~$10,000–15,000/hospitalization)
- **Clinical**: Inhaler technique errors affect 70–90% of patients and directly cause exacerbations; digital coaching on technique is a clinical intervention, not just content
- **Leadership**: COPD + tobacco cessation is a strong story for Medicaid plans (high smoking prevalence) and employer plans; TSC-E being new means there's a window to lead on performance
- **Product**: Exacerbation event = PCE numerator trigger (systemic corticosteroid or antibiotic within 14 days of acute event); inhaler adherence tracking needs PDC logic similar to cardiovascular medications
