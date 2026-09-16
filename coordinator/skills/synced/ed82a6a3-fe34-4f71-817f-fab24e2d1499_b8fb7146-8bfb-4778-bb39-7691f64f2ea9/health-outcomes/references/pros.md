# PRO Reference — Patient-Reported Outcomes

---

## What Are PROs?

A **Patient-Reported Outcome (PRO)** is any report of a patient's health status that comes directly from the patient, without interpretation by a clinician. PROs capture:
- Symptoms (pain, fatigue, nausea)
- Functional status (ability to perform daily activities)
- Health-related quality of life (HRQoL)
- Mental/emotional health
- Treatment satisfaction and adherence

**Why PROs matter**: Clinical measures (labs, vitals, imaging) don't fully capture how a patient is experiencing their condition. PROs provide a patient-centered view of whether interventions are working.

---

## Key PRO Instruments

### PROMIS (Patient-Reported Outcomes Measurement Information System)
**Source**: NIH-funded; managed by Northwestern University's PROMIS Health Organization
**Format**: Computer Adaptive Testing (CAT) or short fixed forms
**Domains**:
- Physical Function
- Pain Interference / Pain Intensity
- Fatigue
- Sleep Disturbance
- Anxiety
- Depression
- Ability to Participate in Social Roles

**Scoring**: T-score with mean = 50, SD = 10 (referenced to US general population)
- Score of 60 in Depression = 1 SD worse than average
- Score of 40 in Physical Function = 1 SD worse than average

> **PROMIS is the gold standard for PROs** in clinical research, value-based care programs, and CMS innovation models. Recommend PROMIS when designing digital symptom tracking or member check-in features.

---

### PHQ (Patient Health Questionnaire) — Depression & Anxiety

**PHQ-9**: 9-item depression screener. Most widely used in primary care.
- Score 0–4: Minimal depression
- Score 5–9: Mild
- Score 10–14: Moderate
- Score 15–19: Moderately severe
- Score 20–27: Severe

**PHQ-2**: 2-item ultra-brief screener (first two items of PHQ-9). Used for initial screening.

**GAD-7**: 7-item Generalized Anxiety Disorder scale. Companion to PHQ-9.
- Score ≥10 = moderate anxiety (threshold for further evaluation)

> **Clinical note**: PHQ-9 is used in HEDIS Depression Screening (DSF) and is the most common instrument in Stars-relevant behavioral health interventions.

---

### VR-12 / VR-36 (Veterans RAND)
**Used in**: CMS Medicare Health Outcomes Survey (HOS) — directly in Stars
**Domains**: Physical Component Summary (PCS) and Mental Component Summary (MCS)
**How Stars uses it**: Compares member scores at baseline and 2-year follow-up to assess whether physical and mental health improved or declined

Stars measures:
- **Improving or Maintaining Physical Health (MHP)**
- **Improving or Maintaining Mental Health (MHM)**

> Features targeting fall prevention, chronic pain, functional independence, or behavioral health in Medicare populations directly affect HOS-based Stars measures.

---

### SF-36 / SF-12
- Legacy instruments; largely replaced by PROMIS and VR-12 in plan contexts
- Still used in clinical trials and some chronic disease management programs
- SF-12 gives Physical Component Score (PCS) and Mental Component Score (MCS)

---

### KOOS / HOOS (Knee/Hip Osteoarthritis Outcome Scores)
Used in orthopedic care and CMS Comprehensive Joint Replacement (CJR) model:
- Pain
- Symptoms
- Function in daily living
- Function in sport/recreation
- Quality of life

---

### Pain-Specific Instruments
- **NRS (Numeric Rating Scale)**: 0–10 pain intensity; simplest, most common
- **BPI (Brief Pain Inventory)**: Severity + interference subscales
- **PEG (Pain, Enjoyment, General Activity)**: 3-item version of BPI; used in opioid risk monitoring

---

### Functional Status
- **KATZ ADL**: Activities of Daily Living — bathing, dressing, toileting, transferring, continence, feeding
- **Lawton IADL**: Instrumental ADLs — shopping, cooking, housekeeping, laundry, transportation, medications, finances
- **Barthel Index**: Used in rehab and post-acute settings

---

## PROs in Regulatory Contexts

### FDA PRO Guidance
FDA requires PRO instruments for patient-reported endpoints in clinical trials and labeling claims. Instruments must be validated for the specific condition and population.

### CMS Value-Based Programs
CMS uses PROs in:
- **Comprehensive Joint Replacement (CJR)**: KOOS/HOOS pre/post surgery
- **Bundled Payments for Care Improvement (BPCI-Advanced)**: Functional outcomes
- **Medicare HOS**: VR-12 for Stars

### PCORI (Patient-Centered Outcomes Research Institute)
Funds comparative effectiveness research using PROs. PCORI prioritizes outcomes that matter to patients — not just clinical biomarkers.

---

## Designing PRO-Informed Features

When clinical design teams ask about incorporating PROs:

1. **Select validated instruments** — don't create custom symptom scales without validation
2. **Match the instrument to the population**: PROMIS for general adults; PHQ-9 for depression; VR-12 for Medicare/HOS
3. **Define a MCID (Minimal Clinically Important Difference)** — the threshold for a score change to be meaningful. Without MCID, you can't interpret whether change is real.
   - PHQ-9 MCID: ~5 points
   - PROMIS Physical Function MCID: ~4–6 T-score points
4. **Plan for action**: A PRO without a defined care pathway response is a data collection exercise, not a clinical intervention
5. **Frequency matters**: Weekly for acute/active symptoms; monthly for chronic condition monitoring; annually for HOS-type functional assessments
