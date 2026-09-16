# Person-Centered & Humanistic Outcomes

This reference covers two connected layers:
1. **NCQA's emerging Person-Centered Outcome (PCO) measures** — formally entering HEDIS for MY 2027
2. **Humanistic outcomes** — outcomes that matter deeply to patients, providers, and payers but are not (yet) standardized in claims-based measurement frameworks

Both layers are essential for clinical designers, content creators, and health outcomes teams building programs that go beyond gap closure to genuine health improvement.

---

## Part 1: NCQA Person-Centered Outcome (PCO) Measures

### What They Are

PCO measures are a **HEDIS-bound framework** (targeting MY 2027 for D-SNPs and C-SNPs) that formally measures whether care is organized around what matters to the individual — not just clinical indicators.

PCO measures have three required components:
1. **Goal identification** — identify a health goal that matters to the person; document it using goal attainment scaling or a PRO measure
2. **Goal follow-up** — clinician follows up on the goal at subsequent visits; document the conversation even if progress is stalling
3. **Goal achievement** — assess whether the person made progress toward their goal

### Why It Matters Now

- CMS issued a rule in August 2025 requiring D-SNP care plans to include person-centered goals and follow-up — PCO measures operationalize this requirement
- NCQA has tested PCO measures with 30,000+ patients across 17 states; feasibility is confirmed
- NCQA is moving PCO measures through the HEDIS approval process for MY 2027 (D-SNPs and C-SNPs first; Institutional SNPs excluded)
- NCQA is co-developing an HL7 FHIR Implementation Guide for standardized goal documentation — digitization of goal-directed care is actively underway

### How PCO Measures Work in Practice

**Goal-setting best practices** (from NCQA D-SNP testing):
- Focus on what matters to the *person*, not just the condition. A person with diabetes managing toward a family event is more motivated than one focused solely on HbA1c.
- Identify a **specific task or activity** — "walk daily" rather than "get more active"
- Set a **realistic, timebound target** — "walk 10 minutes daily on average over two months"
- Build in **wiggle room** — "on average" reduces all-or-nothing thinking and prevents a missed day from feeling like failure
- Document follow-up **at every visit** — including visits where no progress was made; stalled progress is clinical information

**Goal Attainment Scaling (GAS)**
The primary measurement tool for PCO. GAS rates progress on a 5-point scale:
- -2: Much less than expected
- -1: Somewhat less than expected
- 0: Goal achieved as expected
- +1: Somewhat more than expected
- +2: Much more than expected

GAS is individualized — each person's scale is defined around their own goal — making it inherently person-centered rather than population-normed.

### D-SNP / C-SNP Context

D-SNPs (Dual-Eligible Special Needs Plans) serve members eligible for both Medicare and Medicaid — typically older adults and people with disabilities with complex, high-cost needs. These members are most likely to have goals that clinical measures miss entirely (maintaining independence, staying home, attending family events, managing pain enough to work).

C-SNPs (Chronic Condition Special Needs Plans) serve members with specific serious conditions (e.g., diabetes, heart failure, ESRD). PCO measures complement disease-specific HEDIS measures by adding the patient's own health priorities.

### Connection to Stars and Value-Based Care

PCO measures are not yet in CMS Stars but represent the direction of travel. The EHO4All equity index (2026 Stars) and the broader CMS "Meaningful Measures 2.0" framework both emphasize outcomes that matter to beneficiaries. PCO measures are the most direct operationalization of this priority.

---

## Part 2: Humanistic Outcomes — Unmeasured but Meaningful

These outcomes are not captured in HEDIS, Stars, or CAHPS, but consistently predict engagement, adherence, and long-term health. Clinical designers and content teams should explicitly consider these when designing features, content, and care programs.

### Patient / Member Outcomes

**Health confidence and self-efficacy**
The belief that one can successfully manage their condition. Strong predictor of medication adherence, follow-through on care plans, and long-term behavior change. Not captured in any claims-based measure.
- Relevant instrument: Patient Activation Measure (PAM) — 10-item validated scale; scores 1–4 from "disengaged" to "proactive manager"
- Design implication: Features that build mastery (not just information delivery) directly address self-efficacy

**Felt sense of being heard and known**
CAHPS captures whether providers "communicated well," but not whether the patient felt understood as a full person with a life beyond their diagnosis. This is a driver of trust, follow-through, and willingness to disclose.

**Reduced fear and health anxiety**
A person can have controlled clinical values and still live in significant fear of complications, progression, or death. Health anxiety predicts unnecessary utilization (ED visits, over-testing) and avoidance behaviors.

**Meaningful daily functioning**
Beyond functional status scales (ADLs, IADLs), the question of whether someone can do what makes life worth living — work, parent, participate in community, pursue hobbies. PROs like PROMIS get partway here; PCO goal-setting captures it most directly.

**Financial toxicity**
The harm caused by healthcare costs and cost-related stress — even when coverage is technically adequate. Drives medication non-adherence, skipped visits, and delayed care. Not a standard quality measure anywhere.
- Relevant instrument: COST (Comprehensive Score for Financial Toxicity) — validated 11-item PRO

**Trust in the healthcare system**
Low institutional trust — especially among historically marginalized populations — predicts disengagement before any care gap appears in claims. It is a root-cause outcome that no administrative measure captures.

**Dignity in care**
Was the person treated as a full human, not a diagnosis, risk tier, or compliance problem? Dignity violations cause lasting harm to the care relationship and are entirely invisible to quality measurement systems.

**Psychological safety in care settings**
Particularly relevant for LGBTQ+ members, people with disabilities, people with trauma histories, and racial and ethnic minorities. Whether a person feels safe being honest with their provider affects every downstream clinical outcome.

---

### Provider / Clinician Outcomes

**Diagnostic confidence**
Did the clinician have the information, time, and support to make a well-reasoned decision? Uncertainty-driven care variation is a major quality and cost driver that no quality framework measures.

**Moral distress**
The harm clinicians experience when system constraints prevent them from acting in alignment with their values. A driver of burnout and attrition; an outcome of care system design. Not measured, rarely acknowledged in quality frameworks.

**Time in meaningful care vs. documentation burden**
Proxy for care quality that administrative measures never capture. Clinicians spending 50%+ of their time on EHR documentation is an outcome of the care system — and inversely predicts the relational quality that PCO measures are trying to restore.

**Care team cohesion and psychological safety**
How well the team around a patient functions together — trust, communication, shared understanding of the care plan. Strong predictor of safety and patient outcomes; essentially unmeasured at the plan level.

---

### Payer / Plan Outcomes

**Member trust and perceived value**
A member who believes their plan is genuinely on their side behaves differently — lower disenrollment, higher engagement, better care-seeking behavior. Distinct from CAHPS ratings; more about the felt relationship than service satisfaction.

**Care fragmentation experienced by the member**
How many handoffs, gaps, repeated stories, and disconnected encounters did a member experience? This shows up diffusely in utilization data but is never measured as a member experience in its own right.

**Equity in lived outcomes**
Not just stratified HEDIS reporting, but whether the plan is actively closing gaps in what members experience — including access, dignity, communication quality, and ability to achieve personal health goals. EHO4All in Stars begins to address this financially.

**Engagement depth and meaning**
Not whether a member completed a program touchpoint, but whether the interaction changed anything in their relationship with their health. High touchpoint counts with no behavior change is a program outcome worth measuring.

**Long-term health confidence at population scale**
Whether the plan's programs are producing members who are more capable and confident health managers over time — not just closed gaps in a single measurement year.

---

## Connecting the Two Layers

| Humanistic outcome | PCO bridge | Formal measure (if any) |
|-------------------|-----------|------------------------|
| Self-efficacy / health confidence | Goal attainment (GAS) | PAM (not in HEDIS/Stars) |
| Meaningful functioning | PCO goal identification | PROMIS Physical Function, HOS |
| Feeling heard | PCO goal conversation | CAHPS How Well Doctors Communicate |
| Reduced fear | Goal follow-up documentation | PHQ-9 (anxiety/depression) |
| Dignity | PCO person-centered framing | None |
| Financial toxicity | SDOH screening | AHC HRSN, Z59.4 Z-codes |
| Trust | — | None |

---

## Design Implications

When clinical designers or content teams ask about outcomes beyond HEDIS/Stars, bring this framework into the conversation:

1. **Ask what the person is trying to do in their life** — not just what clinical goal needs to be met. PCO measures are making this a formal quality requirement.
2. **Design for self-efficacy** — content that builds mastery (incremental goal progress, success feedback) outperforms content that delivers information.
3. **Flag financial toxicity** — any medication adherence feature should surface cost concerns and connect to assistance programs; financial toxicity is the most common hidden driver of non-adherence.
4. **Name the unmeasured outcomes** in design artifacts — when a feature addresses trust, dignity, or fear reduction, say so explicitly even if it can't be reported in a HEDIS rate. These outcomes are the mechanism through which measurable outcomes improve.
5. **PCO readiness** — for teams working with D-SNP or C-SNP populations, goal documentation workflows are no longer optional by MY 2027. Features that support structured goal capture (FHIR-aligned, GAS-compatible) have immediate regulatory relevance.
