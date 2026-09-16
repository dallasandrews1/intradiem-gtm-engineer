# Population Health Reference

---

## What Is Population Health?

Population health focuses on **health outcomes of groups of individuals** — not just individual patients — and the distribution of those outcomes within the group. It encompasses:
- Prevalence and incidence of conditions
- Preventive care and screening rates
- Chronic disease management at scale
- Utilization patterns (ED, inpatient, ambulatory)
- Health disparities across demographic subgroups

---

## Key Population Health Metrics

### Prevalence & Burden
| Metric | Definition | Source |
|--------|-----------|--------|
| Condition prevalence | % of population with a diagnosed condition | Claims, EHR, registry |
| Disease burden | Morbidity, disability-adjusted life years (DALYs) | CDC, CMS |
| Comorbidity index | Charlson or Elixhauser comorbidity scores | Claims |
| Risk stratification tier | Low / moderate / high / complex risk | Predictive models |

### Preventive Care Rates
| Metric | Benchmark source |
|--------|----------------|
| Mammography screening rate | HEDIS BCS; Healthy People 2030 |
| Colorectal cancer screening rate | HEDIS COL; USPSTF target: 68.3% |
| Annual flu vaccination rate | Stars / HEDIS; CDC Healthy People |
| Adult immunization rate | HEDIS AIS |
| Cervical cancer screening rate | HEDIS CCS |
| Annual wellness visit rate | Stars; Medicare AWV |

### Chronic Disease Control
| Condition | Key metric | Target |
|-----------|-----------|--------|
| Diabetes | HbA1c <8% (controlled) | HEDIS CDC-H |
| Diabetes | HbA1c >9% (poor control) | Lower = better |
| Hypertension | BP <140/90 | HEDIS CBP |
| Asthma | Medication ratio ≥0.5 | HEDIS AMR |
| COPD | Exacerbation hospitalization rate | HEDIS PCE |
| Heart failure | 30-day readmission rate | CMS HRRP |

### Behavioral Health
| Metric | Definition |
|--------|-----------|
| Depression screening rate | % screened with PHQ |
| SUD treatment initiation rate | HEDIS IET — Initiation phase |
| SUD treatment engagement rate | HEDIS IET — Engagement phase |
| 7-day follow-up after psych hospitalization | HEDIS/Stars FUH |
| Antidepressant adherence | HEDIS AMM (Acute/Continuation phases) |

### Utilization Metrics
| Metric | Unit | Benchmark |
|--------|------|-----------|
| ED visits | Per 1,000 member months | HEDIS AMB |
| Inpatient admissions | Per 1,000 members/year | HEDIS IPU |
| 30-day readmission rate | % of index admissions | PCR — Stars |
| Avoidable admissions | AHRQ Prevention Quality Indicators (PQIs) | See PQI table below |
| Primary care visit rate | Per member per year | HEDIS CAP, AAP |
| Specialist visit rate | Per member per year | Internal benchmarks |

---

## AHRQ Prevention Quality Indicators (PQIs)

PQIs measure **ambulatory care-sensitive conditions** — hospitalizations that could have been prevented with good outpatient care. High PQI rates signal gaps in primary care access or chronic disease management.

| PQI # | Condition |
|-------|-----------|
| PQI 01 | Diabetes short-term complications |
| PQI 03 | Diabetes long-term complications |
| PQI 05 | COPD / asthma in older adults |
| PQI 07 | Hypertension |
| PQI 08 | Heart failure |
| PQI 11 | Bacterial pneumonia |
| PQI 12 | Urinary tract infection |
| PQI 14 | Uncontrolled diabetes (no complications) |
| PQI 15 | Asthma in younger adults |
| PQI 16 | Rate of lower extremity amputations — diabetes |

> **Design implication**: Programs targeting diabetes, heart failure, and COPD can track PQI rates as outcome evidence of clinical impact, especially relevant for value-based contract reporting.

---

## Healthy People 2030 Targets

Healthy People 2030 provides nationally benchmarked targets for population health metrics. Key examples:

| Objective | Target |
|-----------|--------|
| Reduce adult hypertension | <44.7% of adults |
| Reduce adult obesity | <36% of adults |
| Increase colorectal cancer screening | 74.4% |
| Reduce diabetes-related ED visits | Target set at national baseline improvement |
| Reduce opioid overdose deaths | Reduce rate by 10% |
| Increase depression screening in adults | Increase from baseline |
| Reduce tobacco use in adults | <8% |

---

## Risk Stratification Frameworks

Most population health programs stratify members into risk tiers to prioritize interventions:

| Tier | Characteristics | Typical intervention |
|------|----------------|---------------------|
| Low risk | Healthy, engaged, low utilization | Preventive content, wellness nudges |
| Rising risk | 1–2 chronic conditions, some care gaps | Care gap outreach, condition management |
| High risk | Multiple chronic conditions, ED utilizers | Care management, nurse coaching |
| Complex / catastrophic | Polychronic, high cost, complex needs | Intensive case management, social work |

Common risk models used in population health:
- **HCC (Hierarchical Condition Categories)**: CMS model; drives Medicare risk adjustment
- **ACG (Adjusted Clinical Groups)**: Johns Hopkins; used in commercial and Medicaid
- **CDPS (Chronic Illness and Disability Payment System)**: Medicaid-focused
- **Proprietary models**: Many plans use vendor or internally developed predictive models

---

## Population Health Outcome Reporting

When designing outcomes frameworks or reporting dashboards for population health programs, standard metrics include:

**Clinical outcomes**
- Condition control rates (HbA1c, BP, LDL)
- Screening and gap closure rates
- Readmission and ED visit rates

**Engagement outcomes**
- Program enrollment rate
- Active participation rate (sessions completed, assessments submitted)
- 90-day retention rate

**Experience outcomes**
- Member satisfaction (custom survey or CAHPS)
- Net Promoter Score (NPS) — not a clinical standard, but common in health tech
- PRO change scores (PHQ-9 change, PROMIS change)

**Economic outcomes**
- Cost per member per month (PMPM) trend
- Medical cost ratio (MCR) improvement
- Return on investment (ROI) — claims-based cost analysis vs. matched controls

> Always pair **engagement metrics** with **clinical outcomes** — high engagement with no health improvement is a signal of program design failure.
