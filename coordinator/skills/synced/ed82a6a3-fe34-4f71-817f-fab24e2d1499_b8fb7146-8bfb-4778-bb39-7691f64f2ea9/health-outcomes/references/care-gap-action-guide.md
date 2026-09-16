# Care Gap Action Guide

This guide answers the question: **"A member did Y — does that close a care gap?"**

It translates specific member actions, app interactions, and content engagements into their quality measure implications — what counts, what doesn't, what's needed for it to count, and what to do when it's ambiguous.

---

## How Care Gaps Work (Quick Primer)

A care gap exists when a member is **in the denominator** of a measure (eligible) but **not yet in the numerator** (hasn't completed the qualifying event). Closing a gap means generating a numerator-eligible event — documented in claims, medical records, or (increasingly) ECDS/EHR data.

**Three things must be true for a gap to close:**
1. The event happened (the right service was rendered or the right value was documented)
2. It was documented in an acceptable data source
3. It met the measure's timing, provider, and coding requirements

A member doing the right thing doesn't close a gap if it isn't documented correctly. This is the most common failure mode.

---

## Action-to-Gap Translation Table

### Preventive Care

| Member action | Measure potentially closed | What's required for it to count | Common failure modes |
|--------------|--------------------------|--------------------------------|---------------------|
| Gets a mammogram | BCS-E (Breast Cancer Screening) | Mammogram claim with eligible CPT code; member 40–74; within measurement year | Screening at non-covered facility; result not in structured data for ECDS |
| Gets a colonoscopy or FIT test | COL (Colorectal Cancer Screening) | Appropriate CPT/LOINC code; member 45–75; result documented | FIT test result not returned to clinician; colonoscopy done outside measurement window |
| Gets flu shot | Flu Vaccine (Stars) | Claim or immunization registry record; date within measurement period (Aug 1–Mar 31) | Self-reported by member but not in registry; administered at pharmacy not linked to health record |
| Gets documented BMI + counseling | ABA (Adult BMI Assessment) | BMI value + counseling note in medical record; admin or hybrid | BMI documented but counseling not coded; telehealth visit without structured documentation |
| Completes cervical cancer screening | CCS (Cervical Cancer Screening) | Pap smear CPT; member 21–64; within required look-back window (3 years for Pap; 5 years for Pap+HPV) | Screening done but lab result not linked to member record |

---

### Diabetes Care

| Member action | Measure potentially closed | What's required for it to count | Common failure modes |
|--------------|--------------------------|--------------------------------|---------------------|
| Gets HbA1c lab drawn | CDC-T (HbA1c Testing) | Lab claim with LOINC code; within measurement year | Lab ordered but not completed; result in EHR but not in claims |
| HbA1c result documented as <8% | CDC-H (HbA1c Control) | Numeric result value <8 in structured data; ECDS or hybrid | Value in free-text note; result from prior year used |
| HbA1c result documented as >9% | CDC-P (Poor Control) | Numeric result >9; *this is an inverse measure — lower rate = better* | Same as above; important to note this counts against the plan |
| Gets dilated eye exam | CDC-E (Eye Exam) | Retinal exam CPT by eligible provider (optometrist, ophthalmologist); within measurement year OR prior year for 2-year look-back | Eye exam by non-eligible provider; telehealth retinal exam coding varies by payer |
| Gets urine microalbumin or eGFR | CDC-K (Kidney Health Evaluation) | Either uACR or eGFR lab within measurement year | Only one test done when the measure requires either — check measure spec for current requirements |
| Fills statin prescription | SPD (Statin Use in Persons with Diabetes) | Active statin fill during measurement year; PDC ≥ not required — any fill counts | Gap in fill; statin discontinued by provider; formulary change |
| Fills diabetes medication on time | MAD (Medication Adherence — Diabetes) | PDC ≥ 0.80 across measurement year | Hospitalization days (MY2026 change: IP/SNF days no longer excluded from PDC) |

---

### Cardiovascular / Hypertension

| Member action | Measure potentially closed | What's required for it to count | Common failure modes |
|--------------|--------------------------|--------------------------------|---------------------|
| BP reading documented as <140/90 | CBP (Controlling High Blood Pressure) | Most recent BP reading in measurement year <140/90; hybrid or ECDS | BP taken in office but not coded; home BP reading not clinically documented |
| Fills antihypertensive (RAS antagonist) on time | MAH (Medication Adherence — Hypertension) | PDC ≥ 0.80; RAS antagonist class (ACE inhibitor or ARB) | Wrong drug class (not RAS); PDC calculated across full year including hospitalization gaps (MY2026) |
| Fills statin on time | MAC (Medication Adherence — Cholesterol) | PDC ≥ 0.80 for statin | Same PDC considerations as MAH |
| Statin prescribed for CVD patient | SPC (Statin Therapy — Cardiovascular Disease) | Active statin prescription AND fill during measurement year | Prescribed but not filled; statin contraindicated — check exclusion criteria |

---

### Behavioral Health

| Member action | Measure potentially closed | What's required for it to count | Common failure modes |
|--------------|--------------------------|--------------------------------|---------------------|
| Completes PHQ-9 screening | DSF (Depression Screening and Follow-Up) — screening numerator | PHQ-9 or equivalent administered; documented with LOINC code and score | PHQ-2 only (insufficient); score not recorded in structured field |
| PHQ-9 ≥10 + follow-up contact within 30 days | DSF — follow-up numerator | Follow-up must be a qualifying contact (office visit, telehealth, care management) within 30 days of positive screen | Follow-up is a phone check-in not documented as a clinical encounter; 31+ days |
| Fills antidepressant within 14 days of new diagnosis | AMM-A (Acute Phase) | New antidepressant prescription filled within 14 days of depression diagnosis; 84-day continuous fill | Prescription given but not filled; fill gap >84 days |
| Continues antidepressant for 180 days | AMM-C (Continuation Phase) | Continuous antidepressant fills for 180 days after acute phase; PDC logic | Medication changed; fill gap; member self-discontinues |
| 7-day follow-up after psych hospitalization | FUH-7 | Outpatient mental health visit within 7 days of discharge | Visit on day 8; visit with non-behavioral health provider without BH diagnosis code; no-show not documented |
| Initiates SUD treatment within 14 days of diagnosis | IET-I | First SUD treatment service within 14 days of new SUD diagnosis | Treatment delayed >14 days; peer support only (may not qualify depending on measure spec year) |
| 2+ additional SUD treatment contacts in 34 days | IET-E | Two additional qualifying treatment contacts within 34 days of initiation | Only 1 follow-up contact; contacts not coded as qualifying service type |

---

### Post-Discharge and Transitions

| Member action | Measure potentially closed | What's required | Common failure modes |
|--------------|--------------------------|----------------|---------------------|
| Outpatient visit within 7 days of psych discharge | FUH-7 | Face-to-face or telehealth BH visit; qualifying provider; within 7 calendar days | Day 8 visit; ER visit doesn't count; visit without BH diagnosis code |
| PCP or specialist visit within 30 days of any discharge | PCR (Readmissions — indirect) | No direct numerator event; PCR measures whether readmission occurred; the visit prevents the readmission | Gap closure here is prevention, not documentation |

---

## The "Does It Count?" Decision Framework

When a team member asks whether a specific interaction closes a gap, walk through these questions in order:

```
1. Is the member eligible?
   → Are they in the denominator? (age, enrollment, diagnosis, product line)
   → Are there any exclusions that apply?

2. Did the right event happen?
   → Was it the correct service type / test / medication?
   → Was it performed by an eligible provider?
   → Did it happen within the correct measurement window?

3. Was it documented in an acceptable data source?
   → Claims: correct CPT/HCPCS/NDC/LOINC code?
   → Hybrid: is there a medical record to support it?
   → ECDS: is the value in a structured field in the EHR?

4. Is the result value correct (for outcome measures)?
   → HbA1c: is the numeric value documented?
   → BP: is the exact reading documented?
   → PDC: has enough time passed and have fills been consistent?

5. Will it be captured in the plan's data?
   → Claims lag: 60–90 days typical; late-year events may not process in time
   → Supplemental data: does the plan accept supplemental data feeds?
   → Hybrid outreach: will the plan request records, and will the record support the numerator?
```

---

## App Interactions and Their Gap Closure Potential

| App interaction | Gap closure potential | Pathway | Limitation |
|----------------|----------------------|---------|-----------|
| Member self-reports HbA1c value | Medium | Supplemental data / hybrid if plan accepts | Value must be reconciled against lab claim; self-report alone usually insufficient |
| Member logs medication fill | Low-medium | Supports outreach for adherence; not a direct numerator event | PBM data is the authoritative source for PDC |
| Member completes PHQ-9 in app | Medium-high | ECDS-eligible if app is connected to EHR; or supports hybrid with structured score + date | Requires data integration pathway to clinical record |
| Member schedules appointment through app | Low (indirect) | Increases probability of numerator event occurring | Scheduling ≠ attending ≠ documented |
| Member views educational content | Low (indirect) | May increase likelihood of care-seeking behavior | No direct measure impact; value is behavioral activation |
| Member uploads lab result photo | Low | Not acceptable for claims or ECDS; could support hybrid review if extracted and verified | Requires clinical review to convert to usable data |
| Member completes health assessment | Medium | If structured data is captured (not free text) and there's a data integration pathway | Platform must generate structured output, not narrative |
| Member sets and tracks PCO goal (MY2027) | High (D-SNP/C-SNP) | Direct PCO measure component if FHIR-compliant documentation | Only applies to SNP populations in MY2027+ |

---

## Supplemental Data: The Critical Infrastructure Question

Many app interactions could contribute to gap closure — but only if the plan has a **supplemental data agreement** that accepts digital data, and only if the app generates data in an acceptable format.

Questions to ask for any new data integration:
- Does the plan accept supplemental data for this measure?
- What format is required (X12, HL7 FHIR, flat file)?
- What is the submission deadline before measure lock?
- Is there an audit trail that supports hybrid record review?
- Who is the plan contact for supplemental data submissions?

Without this infrastructure, app interactions remain in the "indirect / behavioral" category — valuable but not directly reportable.
