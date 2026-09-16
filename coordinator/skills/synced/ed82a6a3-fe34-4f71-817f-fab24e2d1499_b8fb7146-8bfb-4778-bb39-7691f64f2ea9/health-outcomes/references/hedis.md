# HEDIS Reference

**Steward**: NCQA (National Committee for Quality Assurance)
**Reporting cycle**: Annual (measurement year = prior calendar year)
**Used by**: Commercial, Medicaid, and Medicare health plans for NCQA accreditation and public reporting

---

## Measure Domains

HEDIS organizes measures into 6 domains. Use these to classify clinical content and features.

### 1. Effectiveness of Care
The largest domain — clinical quality and preventive care. Sub-domains:

**Prevention & Screening**
- Adult BMI Assessment (ABA)
- Breast Cancer Screening (BCS-E) — expanded MY 2025 to include ages 40–49 (previously 50+), aligning with USPSTF
- Documented Assessment After Mammogram (DBM-E) — **NEW MY 2025**: BI-RADS result documentation within 14 days
- Follow-Up After Abnormal Mammogram Assessment (FMA-E) — **NEW MY 2025**: timely follow-up after abnormal result
- Cervical Cancer Screening (CCS)
- Colorectal Cancer Screening (COL)
- Chlamydia Screening (CHL) — renamed MY 2025 (was "Chlamydia Screening in Women"); expanded to include transgender members
- Tobacco Use Screening and Cessation Intervention (TSC-E) — **NEW MY 2026** (ECDS); replaces retired survey-based MSC measure; covers ages 12+

**Respiratory Conditions**
- ~~Asthma Medication Ratio (AMR)~~ **RETIRED MY 2026** — replaced by Follow-Up After Acute and Urgent Care Visits for Asthma (AAF-E)
- Use of Spirometry Testing in COPD (SPR)
- Pharmacotherapy Management of COPD Exacerbation (PCE)

**Cardiovascular Conditions**
- Controlling High Blood Pressure (CBP)
- Statin Therapy for Patients with Cardiovascular Disease (SPC)
- Statin Use in Persons with Diabetes (SPD)

**Diabetes**
- Comprehensive Diabetes Care (CDC) — composite including:
  - HbA1c testing
  - HbA1c poor control (>9%) — *lower rate = better*
  - HbA1c control (<8%)
  - Eye exam (Administrative reporting only as of MY 2025; Hybrid method retired)
  - Kidney health evaluation
  - BP control (<140/90)
  - Statin use
- Blood Pressure Control for Patients with Diabetes (BPD-E) — **NEW MY 2026** (ECDS): expands on CBP with pharmacy-based denominator identification; stratified by race/ethnicity

**Musculoskeletal**
- Disease-Modifying Anti-Rheumatic Drug Therapy for RA (ART)
- Osteoporosis Management in Women (OMW)

**Behavioral Health**
- Antidepressant Medication Management (AMM) — Acute and Continuation phases
- Follow-up After Hospitalization for Mental Illness (FUH) — 7-day and 30-day
- Follow-up After ED Visit for Mental Illness (FUM)
- Initiation and Engagement of Alcohol and Other Drug Abuse or Dependence Treatment (IET)
- Follow-up After ED Visit for Alcohol and Other Drug Abuse (FUA)
- Depression Screening and Follow-Up for Adolescents and Adults (DSF)
- Diabetes Screening for People with Schizophrenia or Bipolar Disorder (SSD)

**Musculoskeletal / Pain**
- Use of Opioids at High Dosage (UOD) — *lower rate = better*
- Use of Opioids from Multiple Providers (UOP) — *lower rate = better*

**Children & Adolescents**
- Well-Child Visits (W15, W34, WCV)
- Immunizations for Adolescents (IMA)
- Children's and Adolescents' Access to Primary Care Practitioners (CAP)
- Weight Assessment and Counseling for Nutrition and Physical Activity (WCC)
- Attention-Deficit/Hyperactivity Disorder (ADD)

**Women's Health**
- Prenatal and Postpartum Care (PPC)
- Lead Screening in Children (LSC)

### 2. Access/Availability of Care
- Adults' Access to Preventive/Ambulatory Health Services (AAP)
- Children's and Adolescents' Access to Primary Care Practitioners (CAP)
- Annual Dental Visit (ADV) — Medicaid only
- Initiation of Prenatal Care (IPC)

### 3. Experience of Care
- CAHPS 5.0H survey measures (see cahps.md)
- Child CAHPS
- Cultural Competence measures

### 4. Utilization & Risk-Adjusted Utilization
- Ambulatory Care (AMB): ED visits and outpatient visits per 1,000 member months
- Inpatient Utilization — General Hospital/Acute Care (IPU)
- Mental Health Utilization (MPT)
- Identification of Alcohol and Other Drug Services (IAD)
- Plan All-Cause Readmissions (PCR) — risk-adjusted

### 5. Health Plan Descriptive Information
- Board Certification (BOC)
- Practitioners with Current HEDIS Licensure

**MY 2026 New Measures — Surgical Follow-Up (Risk-Adjusted)**
For members 65+, risk-adjusted ratio of observed-to-expected unplanned acute hospitalizations within 15 days of outpatient surgery:
- Acute Hospitalizations Following Outpatient Orthopedic Surgery (HFO)
- Acute Hospitalizations Following Outpatient General Surgery (HFG)
- Acute Hospitalizations Following Outpatient Colonoscopy (HFC)
- Acute Hospitalizations Following Outpatient Urologic Surgery (HFU)

---

## Digital Transformation of HEDIS (Critical Trend)

NCQA is phasing out **hybrid (medical record review) reporting** entirely by **MY 2029**. Everything is moving to ECDS (electronic clinical data via EHR/registries) and Administrative methods.

Key milestones:
- MY 2025: Eye Exam for Diabetes — Hybrid retired; Administrative only
- MY 2026: Lead Screening in Children (LSC) — Hybrid retired; ECDS only. Specs reformatted to align with FHIR standards.
- MY 2029: All hybrid methods retired; fully digital

**Design implication for clinical and content teams**: As hybrid methods are retired, documentation quality in EHRs becomes the primary source of truth. Features that support structured clinical data capture (vs. free-text notes) will have increasing impact on plan measure performance.

---
Measures using EHR / registry data rather than claims:
- Depression Screening (DSF)
- Prenatal Immunization Status (PRS)
- Weight Assessment and Counseling (WCC)

---

## Measure Anatomy (Standard Template)

| Element | Description |
|---------|-------------|
| Denominator | Eligible population (age, enrollment, diagnosis criteria) |
| Numerator | The qualifying event or service |
| Exclusions | Clinical or administrative reasons to remove from denominator |
| Measurement period | Typically Jan 1 – Dec 31 of measurement year |
| Data source | Administrative (claims), hybrid (claims + medical record), ECDS (EHR) |

---

## Data Collection Methods

- **Administrative**: Claims data only — lowest burden, but can miss chart-documented events
- **Hybrid**: Claims + medical record review — gold standard, higher rate potential
- **ECDS**: EHR structured data — growing method, requires data normalization

---

## HEDIS and Equity

NCQA introduced **HEDIS Equity Measures** and stratified reporting by race/ethnicity. Key equity-relevant measures:
- Prenatal and Postpartum Care (PPC)
- Controlling High Blood Pressure (CBP)
- Comprehensive Diabetes Care (CDC)
- Child Well Visits

When mapping content or interventions for health equity, always check if stratified HEDIS performance data exists for the measure.

---

## Common HEDIS Coding Pitfalls

- Eye exams for diabetes must meet specific timing and provider type requirements
- "Hybrid" measures allow medical record documentation to supplement claims — content teams can help members understand documentation importance
- Exclusions matter: a member with certain diagnoses may be excluded from a denominator even if they receive the service
- Look-back periods vary: some measures look back 2 years (e.g., BMI counseling documentation)
