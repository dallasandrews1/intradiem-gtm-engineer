# Value Translation Layer

The same health outcome means different things to different audiences. This reference helps translate a single clinical event or program outcome into the language that resonates with each stakeholder group.

Use this whenever someone asks: "How do I explain the value of X to [audience]?"

---

## The Four Audience Frames

| Audience | Primary question | Language that lands | What they're accountable for |
|----------|-----------------|--------------------|-----------------------------|
| **Payer / Health Plan** | Does this move our Stars or close HEDIS gaps? | Measure rates, QBP dollars, PMPM cost, gap closure %, Stars weight | Quality bonus payments, accreditation, member retention |
| **Clinical / Provider** | Is this good care? Does it help my patients? | Clinical evidence, outcomes, care protocols, patient activation | Patient health, clinical guidelines, liability |
| **Internal Leadership** | Does this grow the business and differentiate us? | Engagement rates, retention, revenue impact, competitive positioning | Growth, margin, product-market fit |
| **Product / Engineering** | What does this system need to do, and how do we measure it? | Data events, API triggers, measurable user actions, instrumentation | Feature delivery, data quality, system reliability |

---

## Translation Templates by Outcome Type

### Template 1: Member Completes a Health Check-In / Assessment

**What happened**: A member with diabetes answers a set of questions about their recent HbA1c, blood pressure, and medication use.

| Audience | How to frame it |
|----------|----------------|
| Payer | "This interaction captures data that supports hybrid reporting for CDC and CBP measures. If the member's HbA1c is documented as controlled (<8%), it can contribute to the numerator of the Comprehensive Diabetes Care measure — a double-weighted Stars measure. Each closed gap has actuarial value: plans typically attribute $X PMPM in Stars QBP uplift per percentage point of gap closure." |
| Clinical | "The check-in surfaces a structured clinical snapshot outside of an office visit. It enables earlier identification of uncontrolled values, prompts timely outreach, and supports shared decision-making at the next visit. It also activates the patient as an informed participant in their own care." |
| Leadership | "Members who complete regular health check-ins have [X]% higher 90-day retention. This interaction is a direct signal of activated membership and a differentiator in plan RFPs where care management engagement is a scored criterion." |
| Product | "The check-in creates a structured data event: condition tag + response values + timestamp. Numerator-eligible responses should trigger a care gap closure flag in the member record and an outreach suppression signal if the gap is closed. Requires EHR/claims reconciliation to count in hybrid reporting." |

---

### Template 2: Member Picks Up a Medication Refill (Adherence Event)

**What happened**: A member fills their statin prescription on time, maintaining their PDC above 0.80.

| Audience | How to frame it |
|----------|----------------|
| Payer | "This fill event contributes to the Medication Adherence for Cholesterol (MAC) measure — currently single-weighted in MY2026, returning to triple-weight in MY2027. Each percentage point improvement in MAC adherence rates is among the highest-ROI Stars interventions available. Plans with strong adherence programs have demonstrated $200–400 PMPM reduction in cardiovascular event costs." |
| Clinical | "Consistent statin use at therapeutic PDC reduces major cardiovascular events by 25–35% in high-risk populations. This fill represents a patient successfully executing their care plan — the clinical goal isn't the fill itself but the serum LDL reduction and event prevention it enables." |
| Leadership | "Medication adherence is the single highest-weight domain returning to Stars in 2027. Our ability to influence fills through reminders, cost transparency, and barrier removal is a direct revenue driver — and a defensible clinical differentiator in plan partnerships." |
| Product | "A fill event = a PDC increment. The system needs to track: fill date, days supply, expected next fill window, and gap days. Outreach logic should trigger 7–10 days before the expected refill gap. Data source is typically PBM feed; reconciliation latency affects outreach timing." |

---

### Template 3: Member Engages With Mental Health Content / Screening

**What happened**: A member completes a PHQ-9 through the app and scores 12 (moderate depression).

| Audience | How to frame it |
|----------|----------------|
| Payer | "PHQ-9 completion supports the Depression Screening and Follow-Up (DSF) HEDIS measure. A score of ≥10 triggers the follow-up numerator — the member needs a follow-up contact or care plan within 30 days to close the gap. This is increasingly a Stars-adjacent measure and directly relevant to behavioral health network adequacy requirements." |
| Clinical | "A PHQ-9 score of 12 indicates moderate depression requiring clinical follow-up. The evidence-based response is: confirm diagnosis, assess safety, initiate treatment (therapy referral, medication evaluation, or both), and schedule follow-up within 4 weeks. The app has identified a member who may not have otherwise disclosed." |
| Leadership | "Depression is the #1 driver of productivity loss and comorbidity cost in working-age populations. Identifying and connecting members to care at this stage — before a crisis — is the highest-value intervention in behavioral health. This is a strong story for employer plan sponsors and Medicaid managed care RFPs." |
| Product | "PHQ-9 score ≥10 should trigger: (1) immediate in-app response with safety check language, (2) care navigation outreach within 24 hours, (3) DSF follow-up tracking flag in the member record with a 30-day window. Score and date must be documentable in a structured field for hybrid reporting eligibility." |

---

### Template 4: Member Sets and Tracks a Personal Health Goal (PCO)

**What happened**: A D-SNP member sets a goal to walk 10 minutes daily and checks in on progress weekly through the app.

| Audience | How to frame it |
|----------|----------------|
| Payer | "This interaction directly operationalizes the NCQA Person-Centered Outcome (PCO) measures entering HEDIS MY2027 for D-SNPs. CMS's August 2025 rule requires person-centered goals in D-SNP care plans. Goal documentation + follow-up in the app creates the structured data needed for PCO measure reporting. Early implementation is a competitive advantage for plan accreditation." |
| Clinical | "Goal-directed care activates self-efficacy — the strongest predictor of long-term behavior change. A walking goal for a D-SNP member addresses functional status (HOS physical health domain), potential weight and glucose management, and social isolation reduction. It also creates a conversational anchor for the care team at every subsequent touchpoint." |
| Leadership | "D-SNP members are the highest-cost, highest-complexity population in Medicare Advantage. Features that activate this population — and that are required by CMS rule — are a direct differentiator in D-SNP contract bids. PCO capability signals clinical sophistication to health plan partners evaluating vendors." |
| Product | "Goal events need: goal text, goal category (functional, social, clinical), GAS baseline score, follow-up timestamps, and achievement score. NCQA's FHIR Implementation Guide (releasing spring 2026) defines the interoperability standard. Build goal data model to be FHIR-compatible from the start to avoid rework when digital PCO reporting is required." |

---

## Outcome Stacking: Showing Cumulative Value

When presenting to leadership or payers, outcomes can be "stacked" across dimensions to show the full value of a single interaction:

**Example: A diabetes member completes a check-in, then refills their statin, then sets a walking goal.**

```
Clinical value:     HbA1c monitoring → early detection of poor control
                    Statin adherence → cardiovascular event prevention
                    Walking goal → functional status improvement (HOS)

Regulatory value:   CDC measure numerator (HbA1c documented)
                    MAC measure PDC contribution (statin fill)
                    PCO measure components (goal + follow-up) — MY2027

Financial value:    Stars QBP uplift on CDC, MAC (triple-weight 2027)
                    Avoided cardiovascular event cost (~$25,000–$40,000/event)
                    D-SNP contract differentiation

Humanistic value:   Member feels seen and supported
                    Self-efficacy built through goal progress
                    Reduced fear of complications
```

Use this stacking approach in executive presentations and payer business reviews. It shows that a single well-designed member interaction creates value across every dimension simultaneously.

---

## Anti-Patterns to Avoid

**For payers**: Don't lead with patient experience language ("members feel better") — lead with measure rates and financial impact, then layer in experience as reinforcement.

**For clinicians**: Don't lead with Stars or QBP language — it signals misaligned priorities. Lead with clinical evidence and patient outcomes; measures are a reporting mechanism, not the goal.

**For leadership**: Don't get lost in measure acronyms. Translate to: retention impact, revenue tied to quality bonuses, RFP differentiation, and risk reduction.

**For product/engineering**: Don't present outcomes without data requirements. Every claimed outcome needs a defined data event, a collection mechanism, and a reconciliation pathway.
