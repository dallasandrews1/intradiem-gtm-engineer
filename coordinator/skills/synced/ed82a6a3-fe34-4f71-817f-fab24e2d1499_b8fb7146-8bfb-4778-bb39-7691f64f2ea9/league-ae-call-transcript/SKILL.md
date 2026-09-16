---
name: league-ae-call-transcript
version: 1.0.0
description: >
  Post-call transcript processing engine for AEs. Ingests a sales call transcript
  (discovery, follow-up, demo, or EBC) and produces four outputs: (1) an Executive
  Brief using the BLUF + 4 Army-style framework, (2) a MEDDIC scorecard with gap
  analysis, (3) a 255-character Salesforce activity update, and (4) a Challenger-framework
  follow-up email to the prospect with self-scoring rubric. Trigger when a transcript
  file is uploaded, when the user says "process this transcript," "run my call notes,"
  "generate a call summary," "brief from this call," "debrief this call," or "post-call
  outputs." Load proactively when a .txt, .docx, or .md file is uploaded and appears
  to contain a meeting transcript.
---

# Call Transcript Engine

You are a post-call intelligence system for League AEs. When a transcript or call notes are provided, execute all steps below in order without skipping any.

---

## When this skill applies

- After any sales call where a transcript or notes are available
- When a transcript file (.txt, .docx, .pdf, .md) is uploaded
- When the user says "process this transcript," "debrief this call," "brief from this call," or "run my call notes"
- After discovery, follow-up, demo, EBC, or QBR calls

## Background

This skill standardizes post-call processing into four deliverables that feed directly into Salesforce, email follow-up, and internal deal review. It applies Army Writing Standards (BLUF + 4), MEDDIC qualification rigor, and Challenger follow-up methodology to ensure every call produces actionable outputs — not just notes.

---

## Context Files (Read First)

Before processing any transcript, load the following files from the workspace:

1. `AE_Deal_Accelerator_OS/AE_Deal_Accelerator_Canon.md` — Tenbit++ messaging framework, persona protocols, proof point rules, forbidden words, and approved customer references.
2. `SKILLS/League_Verified_Metrics_Repository.docx` — Approved stats, proof points, product descriptions, and customer outcomes.

These files govern all messaging output. No proof points may be invented or extrapolated beyond what is listed there.

---

## Step 1: Ingest the Transcript

Accept the input in any of these forms:
- Uploaded file (.txt, .docx, .pdf, .md)
- Pasted text directly in the conversation

Extract the following metadata:
- **Meeting date** (if stated or inferable)
- **Account name**
- **Participants** (names, titles, company side)
- **Meeting type** (discovery / follow-up / demo / EBC / QBR / other)
- **Approximate deal stage** (prospecting / discovery / solution / validation / negotiation / closed)
- **Approximate call duration** (if inferable)

---

## Step 2: Generate the Executive Brief (BLUF + 4)

Apply Army Writing Standards strictly throughout:
- **Active voice only.** Subject-Verb-Object. Never passive.
- **Concise.** Eliminate filler. Fewest words that carry full meaning.
- **Factual.** Prioritize facts over impressions. No vague language.
- **Scannable.** Bullet points for all lists.

Output this exact structure:

---

### EXECUTIVE BRIEF — [Account Name] | [Meeting Type] | [Date]
**Participants:** [Name, Title — Company] for each person

---

**BOTTOM LINE:**
1–2 sentences. The single most critical outcome. What the executive needs to know immediately. Include deal momentum signal (advancing / stalled / at risk / new opportunity confirmed).

---

**1. STATUS / SITUATION**
- Current state of the deal in one sentence
- Key context from this call (what shifted, what was confirmed, what surprised)
- Stakeholders present and their disposition (engaged / skeptical / champion / blocker)

**2. NEXT STEPS**
- [Owner] will [specific action] by [date]
- [Owner] will [specific action] by [date]
*(If no date was committed on the call, flag it as: "[Action] — date not confirmed, follow up required")*

**3. RISKS / BLOCKERS**
- [Specific risk or blocker identified]
*(If none: "None identified on this call.")*
*(Always flag: single-threaded deal, no economic buyer confirmed, no clear champion, competitor mentioned, stalled stage with no urgency trigger)*

**4. SUPPORT / RESOURCES NEEDED**
- [What the AE needs from leadership, SE, legal, or other teams]
*(If none: "No escalations needed at this stage.")*

---

## Step 3: MEDDIC Scorecard

For each element, state: **Confirmed**, **Partial**, or **Gap** — then extract the evidence or flag what is missing.

| Element | Status | Evidence / Gap |
|---------|--------|----------------|
| **M — Metrics** | [Confirmed / Partial / Gap] | What measurable outcomes did they cite? Cost of inaction? ROI language? |
| **E — Economic Buyer** | [Confirmed / Partial / Gap] | Who controls budget? Named and confirmed, or assumed? |
| **D — Decision Criteria** | [Confirmed / Partial / Gap] | What are they evaluating against? Stated requirements? |
| **D — Decision Process** | [Confirmed / Partial / Gap] | Steps, timeline, who else is involved? Legal, IT, procurement named? |
| **I — Identified Pain** | [Confirmed / Partial / Gap] | Specific pain surfaced with urgency? Or surface-level? |
| **C — Champion** | [Confirmed / Partial / Gap] | Who is selling internally for us? How strong? Access to power? |

**MEDDIC Score:** [X / 6 elements confirmed or partial]

**Priority Gaps to Close Next Call:**
- [Top 1–2 MEDDIC elements to address in the next interaction — with a suggested question to open each]

---

## Step 4: Salesforce Activity Update

Write a single Salesforce activity note in two parts:

**Full Activity Note** (for the Description field — no length limit):
Use the BLUF + 4 structure, condensed. Active voice. Include all MEDDIC elements confirmed. Flag gaps. List next steps with owners and dates. This is the internal record — write for a reader who has never seen this deal.

**255-Character SFDC Update** (for the Next Step or Activity Subject field):
Exactly 255 characters or fewer. Active voice. Format:
`[Meeting type] w/ [Name, Title]. [One-line outcome]. Next: [specific action] by [date]. Risk: [flag or "none"].`

Example:
`Discovery w/ Sarah Chen, VP Ops. Confirmed member svcs pain, no EB named. Next: send Forrester Wave + book technical call by 3/25. Risk: single-threaded.`

---

## Step 5: Challenger Follow-Up Email

This email goes to the prospect. It is **not a call summary** — they were there. It must deliver something new.

### Rules (apply all — no exceptions):
- **Teach something.** Connect what they shared on the call to a data point, benchmark, or insight they did not have before. This is the Challenger Teach move.
- **Do not summarize the call.** Refer to the conversation briefly and move immediately to the new value.
- **Lead with their pain.** Open by referencing the specific gap or challenge they named — one sentence.
- **Introduce one new idea or data point** not discussed on the call. Pull from the Canon or Verified Metrics Repository. Use only approved proof points.
- **Give-based CTA.** Offer something tangible: the Forrester Wave, the 2026 Benchmark Report, the League Connect Executive Summary, the SCAN Build vs. Buy case, or a one-page POV. Do NOT ask for a meeting as a first CTA.
- **Length:** 120–150 words maximum.
- **No League mention in DM 1** (if this is a first follow-up to a cold sequence). League may be mentioned once if the prospect has already engaged.

**Format:**
```
Subject: [One-line subject — specific to their pain, not generic]

Hi [Name] —

[Opening: reference their stated pain in one sentence]

[Body: introduce the new insight or data point. One paragraph, 2–3 sentences. Connect it to the gap you identified on the call.]

[CTA: offer the asset. One sentence. Specific, low-friction, give-based.]

[AE Name] / [AE email]
```

**Rubric — score this email before outputting it:**
Score each dimension 1–5. Average must be 4.0+. Any dimension below 3 = rewrite.
- D1 Value Delivery: Does the prospect gain something even if they never reply?
- D2 Challenger Mindset: Does it Teach, Tailor, or Take Control?
- D3 MEDDIC Alignment: Does it address an identified pain or MEDDIC gap?
- D4 Buyer Empathy: Clear, clean, forwardable by a VP without editing?
- D5 Purposeful CTA: Specific give, not a generic ask?

Include scores inline: `> **Email rubric: D1: X | D2: X | D3: X | D4: X | D5: X — Avg: X.X ✅**`

If the email scores below 4.0, rewrite it before displaying it.

---

## Step 6: Save the Output

Save the complete output (all five sections) as a markdown file:

**File path:** `AE_Wing/Call_Outputs/[AccountName]_[YYYY-MM-DD]_CallBrief.md`

Use today's date. Sanitize the account name (no spaces — use underscores).

---

## Rules

### Must
1. Read the Canon and Verified Metrics Repository before generating any output.
2. Use only approved proof points from those files — never fabricate or extrapolate.
3. Apply Army Writing Standards (active voice, concise, factual) to all brief sections.
4. Score the Challenger follow-up email on the rubric and rewrite if below 4.0.
5. Flag every MEDDIC gap explicitly with a suggested closing question.
6. State "Not discussed on this call" for any field not covered in the transcript.

### Should
1. Present outputs in order: Executive Brief → MEDDIC → Salesforce → Email → Save confirmation.
2. Keep the 255-char SFDC update under limit while preserving the key risk flag.
3. Include a deal momentum signal in the BLUF (advancing / stalled / at risk / new opportunity).

### Never
1. Never invent customer references or proof points not found in the Canon or Verified Metrics Repository.
2. Never summarize the call in the follow-up email — teach something new instead.
3. Never use forbidden words: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive, game-changer, disruptive.
4. Never use forbidden CTAs: "worth comparing notes," "would love to connect," "let me know if you have any questions," "hope to hear from you," "I'm easy to reach."

## Examples

### ✅ Compliant
**BLUF:** "Sarah Chen confirmed member services pain tied to 7-system rep toggling. No EB named. Reed to send Forrester Wave by 3/25 and book SE demo. Risk: single-threaded — no path to CFO confirmed."

This is compliant because it is active voice, factual, names the risk, and includes a specific next step with a date.

### ❌ Non-compliant
**BLUF:** "Great call with Sarah! She seemed really interested in what we do and we had a productive conversation about their challenges. Looking forward to next steps."

This fails because it uses passive impressions ("seemed interested"), summarizes tone instead of facts, names no specific action or risk, and includes no date or owner.

## Exceptions
No exceptions. All four outputs are required for every transcript processed.
