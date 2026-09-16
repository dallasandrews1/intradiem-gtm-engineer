# Output Templates

This file defines the output modes for the health-outcomes skill. Always determine which mode applies before responding. Never process, analyze, or reproduce real League program data — see compliance note below.

---

## Compliance Note — Read First

**This skill does not process real data.** League program data — including aggregated percentages, sample sizes, pre/post scores, or any figures pulled from Looker or internal trackers — must not be entered into this skill. This applies even to de-identified aggregate statistics.

What this skill does instead:
- Produces blank, pre-formatted outcome record templates ready to be filled in offline
- Provides hypothetical worked examples to show what good looks like
- Gives fill-in guidance so anyone can complete a record correctly in a League-controlled environment (Google Docs, Confluence, the tracker)
- Answers knowledge questions about measures, conditions, content architecture, and product data models

If someone pastes real data into the skill, respond with:
> "I can't process real program data due to compliance requirements — but I can give you a pre-formatted template and a worked hypothetical example so you can complete this record in Google Docs or Confluence. Want me to generate that now?"

---

## Mode Detection — Do This First

Read the message and ask: what job is this person trying to do?

| Signal in the message | Mode |
|----------------------|------|
| "give me a template", "outcome record", "how do I fill this in", "what format" | Mode 1 — Template + hypothetical |
| "payer", "health plan", "client", "RFP", "Stars", "value story" | Mode 2A — Payer / client knowledge |
| "content", "create", "program", "lesson", "what should we ask", "what to measure" | Mode 2B — Content team / measurement architecture |
| "product", "feature", "build", "data event", "track", "what are we measuring" | Mode 2C — Product team / indicator map |
| Real data pasted (%, n, scores) | Compliance redirect → offer Mode 1 template |

When the signal is ambiguous, ask one clarifying question: "Are you looking for a template to fill in, or do you want to know what to measure and why?"

---

## Mode Announcement — Required at the Top of Every Response

Before producing any output, always open with a one-line mode announcement in this exact format:

> **[Mode name]** — [plain-language description of what this response will give them and why]. If this isn't what you were looking for, just tell me and I'll switch.

Use these announcements verbatim for each mode:

**Mode 1:**
> **Outcome record template** — I'm generating a blank structured template plus a hypothetical worked example. Fill in the template with your real data in Google Docs or Confluence — real program data shouldn't be entered into this chat.

**Mode 2A:**
> **Payer & client value story** — I'm pulling the measure stack, Stars weights, and value framing for this condition or program. This is organized for health plan partners, RFPs, and client presentations.

**Mode 2B:**
> **Content measurement architecture** — I'm mapping what to measure and what content to create at each stage of the program. This is organized by program stage, not by measure — designed for content designers and program builders.

**Mode 2C:**
> **Product indicator map** — I'm mapping each interaction to its signal type, data event, and pathway to a quality measure. This is in markdown so you can paste it directly into Jira, Confluence, or Notion.

**Compliance redirect:**
> **Heads up** — I can't analyze real program data in this chat due to compliance requirements. I can generate a blank outcome record template and a hypothetical example that shows what a completed record looks like — you fill it in with your real numbers offline. Want me to do that?

**Hybrid / ambiguous:**
> **[Mode name]** — I'm giving you [X] because your question looked like [signal]. If you actually needed [alternative mode], just say so and I'll regenerate.

The announcement should feel conversational and helpful — not bureaucratic. It's a one-line orientation, not a disclaimer.

---

## Mode 1 — Outcome Record Template + Hypothetical Example

Use when someone needs a structured outcome record to complete offline with their own data.

Produce two things in this order:
1. A **blank template** with every field, its plain-language definition, and a fill-in prompt
2. A **hypothetical worked example** using clearly fictional but realistic numbers, showing what a completed record looks like

Always state clearly at the top: *"Fill this template in Google Docs, Confluence, or your outcomes tracker — do not paste real program data into this chat."*

---

### Part 1 — Blank Template

Produce every field in this exact order. Under each field label write: the plain-language definition in italics, then the fill-in prompt in brackets.

---

**OUTCOME RECORD TEMPLATE**
*Fill in offline — Google Docs / Confluence / Outcomes Tracker*
*Based on League Health Outcomes Framework — [Month Year]*

---

**Metric**
*What this is: The short name for what was measured — one phrase that describes the signal.*
[Enter the metric name — e.g. "Self-efficacy for managing blood sugar"]

**Survey question**
*What this is: The exact words members were asked. Small differences in wording produce different results — record it precisely.*
[Paste the exact question wording]

Response options:
*What this is: All the answer choices members could select.*
[List every response option]

How the result was calculated:
*What this is: Which options were combined to produce the reported percentage — e.g. "Quite confident + Very confident combined"*
[Describe how the reported % was derived]

---

**Pre-program result**
*What this is: The score before the program started — your baseline. Without this, you can't show change.*
Result: [X%]
n = [How many members answered this question at program start]
When captured: [Start of program / enrollment / baseline check-in]
Total enrolled in program: [N — the full denominator]
Response rate: [X% — n divided by total enrolled]
*What response rate means: The share of eligible members who actually answered. Below 20% = low confidence. Above 30% = solid for in-app surveys.*

**Post-program result**
*What this is: The score after the program ended — what you're comparing against the baseline.*
Result: [X%]
n = [How many members answered this question at program end]
When captured: [Program completion / exit survey]
Response rate: [X% — n divided by total enrolled]

**Change (delta)**
*What this is: The difference between pre and post — how much the metric moved.*
Delta: [+/- Xpp]
*What pp means: Percentage points — the direct arithmetic difference between two percentages. If 27% felt confident before and 44% after, the delta is +17pp.*
Matched cohort:
*What this means: Were the pre and post respondents the same individual members (matched) or different people at each point (unmatched)? Matched = stronger evidence.*
[Yes — same members tracked / No — different respondents / Unknown — member ID linkage not confirmed]

---

**Sample size breakdown**
*What this is: The three numbers that make your n meaningful — total enrolled, answered pre, answered post.*
Total members in program: [N]
Answered pre: [n] — [X%] response rate
Answered post: [n] — [X%] response rate
*Note: If pre and post response rates differ by more than 10 points, flag this in the methodology note.*

---

**HEDIS / Stars measure**
*What this is: The official quality measure this outcome connects to. This is what health plans report to NCQA and CMS — connecting your metric to a measure gives it clinical and financial weight.*
Measure name: [Full name (abbreviation) — Framework]
*Plain-language explanation: [What does this measure track, in one sentence anyone can understand?]*

**Stars weight**
*What this is: How heavily this measure counts toward a health plan's quality rating. Higher weight = more financial impact for the plan.*
[Triple-weight (3×) / Double-weight (2×) / Standard (1×) / Not in Stars]
[Any 2026/2027 notes — e.g. "Returns to triple-weight MY2027"]
*What Stars weight means: Health plans are rated 1–5 stars by Medicare. Plans with 4+ stars receive quality bonus payments. A triple-weight measure counts three times toward that rating.*

**Outcomes framework**
*What this is: The scientific theory that explains why this type of metric predicts clinical outcomes — the "why it works" behind the question.*
Framework: [e.g. Bandura Self-Efficacy Theory / TTM Stage 4 / PCO Goal Attainment / PROMIS]
*Plain-language explanation: [One sentence on the behavioral science basis]*
Time horizon to clinical impact: [e.g. 3–6 months / 30–90 days / end of program]

**Indicator type**
*What this is: Does this metric predict future health outcomes (leading), measure something that already happened (lagging), show movement without closing a clinical loop (directional), or generate a clinically actionable signal the care system can act on (loop-closing)?*
[Leading — Strong / Leading — Moderate / Lagging — Direct action / Lagging — Self-reported / Directional / Loop-closing]
*Why this matters: Loop-closing indicators are the most valuable — they're the moments when member engagement translates into something the health system can act on. Leading indicators predict outcomes but don't prove them.*

---

**Data strength**
*What this is: An honest rating of how much confidence to place in this finding, based on sample size, methodology, and design.*
Rating: [High / Medium-High / Medium / Low-Medium / Low]
[●●●● / ●●●○ / ●●○○ / ●○○○]
Reason: [One sentence explaining why this rating — e.g. "Pre/post available but not a matched cohort"]
What would make this stronger: [Specific next step — e.g. "Link pre and post by member ID"]

**Methodology note**
*What this is: A precise description of how the data was collected and combined. Be specific — name any normalization, language versions, question format differences, or exclusions. This is what protects you if someone questions the finding.*
[Describe exactly how the data was collected, combined, and cleaned]

**Data gap / action needed**
*What this is: The specific next step to strengthen this record, enable external use, or connect to clinical data.*
[Name the exact action needed — not just the category]

**Approval status**
*What this is: Whether this record has been reviewed and cleared for external use. Nothing leaves League without an approved status.*
[APPROVED FOR EXTERNAL USE — approved by: [name], [date]
/ PENDING — waiting for: [specific reviewer]
/ INTERNAL ONLY — reason: [specific reason]
/ DO NOT USE EXTERNALLY — reason: [specific reason, e.g. n too small]]

---

### Narrative template

Complete this section after filling in the structured fields above.

**So what**
*Write 2–4 sentences. What does this finding actually mean for members and for the program? Connect the metric to the clinical outcome it predicts. Write it so someone who has never heard of HEDIS can understand it.*
[Your so what here]

**Honest caveat**
*Write 1–3 sentences. Name the specific limitation of this data and what it means for how it should be used. Never leave this blank — if the data is strong, say why.*
[Your honest caveat here]

**How to use this**

| Audience | How to frame it |
|----------|----------------|
| Payer / health plan | [Frame using measure rates, Stars weight, QBP impact] |
| Clinical team | [Frame using clinical evidence, patient activation, risk] |
| Leadership | [Frame using retention, revenue, competitive differentiation] |
| Product / engineering | [Frame using data events, structured fields, integration] |

---

### Part 2 — Hypothetical Worked Example

Immediately after the blank template, produce a fully completed example using clearly fictional but realistic numbers. Label it prominently.

---

**HYPOTHETICAL EXAMPLE — fictional data for illustration only**
*These numbers are not real League data. Use this as a reference for how to complete the template above.*

**Metric**
Self-efficacy for managing blood sugar
*What this is: The short name for what was measured.*

**Survey question**
"How confident are you that you can manage your blood sugar on a daily basis?"
Response options: Not at all confident · Slightly confident · Moderately confident · Quite confident · Very confident
How the result was calculated: "Quite confident" + "Very confident" combined into a single reported percentage

**Pre-program result**
Result: 27%
n = 148 members answered at program start
When captured: Program enrollment check-in
Total enrolled: 412 members
Response rate: 36%

**Post-program result**
Result: 44%
n = 155 members answered at program completion
Response rate: 38%

**Change (delta)**
Delta: +17pp
Matched cohort: Unknown — member ID linkage not confirmed. Pre and post groups are similar in size but may not be the same individuals. Delta is directional, not a proven individual-level change.

**Sample size breakdown**
Total enrolled: 412
Answered pre: 148 (36% response rate)
Answered post: 155 (38% response rate)
Note: Response rates are consistent — this is a good sign. Difference of 2pp between pre and post response rates is within acceptable range.

**HEDIS / Stars measure**
CDC-H — Comprehensive Diabetes Care: HbA1c Control (<8%) — HEDIS / Stars
Plain-language explanation: This measure tracks how many members with diabetes have their blood sugar under control. HbA1c is a blood test showing average blood sugar over 3 months. One of the most widely reported diabetes quality measures in the US.

**Stars weight**
Double-weight (2×) — Stars MY2026
Plain-language: Health plans are rated 1–5 stars by Medicare. A double-weight measure counts twice toward that score. Plans with 4+ stars receive quality bonus payments worth tens of millions of dollars annually.

**Outcomes framework**
Bandura Self-Efficacy Theory
Plain-language explanation: A person's belief in their own ability to manage their condition is the strongest predictor of whether they actually will — more predictive than knowledge or stated intentions alone.
Time horizon to clinical impact: 3–6 months

**Indicator type**
Leading — Strong
Why: Robust peer-reviewed evidence links self-efficacy to HbA1c control. This predicts the clinical outcome but does not measure it directly.

**Data strength**
Medium-High ●●●○
Reason: Pre/post comparison available with consistent sample sizes, but not a matched cohort — the same individuals are not confirmed across both time points.
What would make this stronger: Link pre and post responses by member ID to confirm the +17pp reflects the same members improving.

**Methodology note**
"Quite confident" and "Very confident" responses normalized across English and French question versions. French version used equivalent confidence scale mapped to 5-point English scale. Pre and post groups have similar but not confirmed identical membership.

**Data gap / action needed**
Link pre and post responses by member ID in Looker to create a matched cohort analysis. This would confirm the +17pp change reflects individual-level improvement and elevate data strength to High.

**Approval status**
INTERNAL ONLY — pre/post matched cohort not yet confirmed. Pending member ID linkage before external use.

---

**So what**
Before the program, fewer than 1 in 3 members felt confident managing their blood sugar. After completing it, nearly 1 in 2 did — a 17 percentage point increase. Self-efficacy is the most validated behavioral predictor of HbA1c control we have. When members leave feeling this way, research shows they are more likely to fill prescriptions, keep appointments, and make dietary changes — the exact behaviors that close the CDC-H gap.

**Honest caveat**
The pre and post groups are similar in size but may not be the same people. Until responses are linked by member ID, the +17pp is a strong directional signal, not a proven individual-level change. Label it as directional in any materials until the matched cohort analysis is complete.

**How to use this**

| Audience | How to frame it |
|----------|----------------|
| Payer / health plan | Behavioral precursor to CDC-H — a double-weight Stars measure. The +17pp pre/post shift shows the program moves members toward the confidence state that predicts HbA1c control. Pair with adherence or lab data for strongest story. |
| Clinical team | Members leaving at 44% confidence are in the activation range that predicts 3–6 month adherence. Members who started below 30% are your highest follow-up priority. |
| Leadership | The program moved members from 27% to 44% confident — a measurable shift in the behavioral state that precedes lower-cost, better-outcome care. This is what activated membership looks like at scale. |
| Product / engineering | Add member ID linkage to pre/post capture. Same question wording, structured field, captured at program entry and exit. This converts a directional finding into a matched cohort result. |

---

## Mode 2A — Payer / Client Knowledge Response

Use when the person wants to explain League's value to a health plan, build a value story, or respond to an RFP. No data required or expected.

Structure:
1. Identify the condition or program area
2. Measure stack — Tier 1 (must), Tier 2 (should), Tier 3 (consider)
3. Value translation — one framing per audience
4. Any 2026/2027 Stars or HEDIS changes relevant to this condition
5. → Template invite

Close with:
> "Want a blank outcome record template to document your program's results against these measures? I'll generate one you can fill in offline."

---

## Mode 2B — Content Team / Measurement Architecture

Use when someone is building a program or lesson and needs to know what to measure at each stage and what content to create.

Structure — organize by program stage, not by measure domain:

For each stage (Entry / Early / Mid / Exit):
- **Question to ask** — exact recommended wording
- **Signal generated** — what type (leading / lagging / directional / loop-closing) and what it tells you
- **HEDIS / Stars connection** — which measure it links to, if any
- **Content this enables** — what lesson, module, or intervention this signal should drive

Always include:
- Loop-closing moments called out explicitly — these are the highest-value interactions
- A note on question wording consistency — same words at entry and exit or delta is invalid
- → Template invite

---

## Mode 2C — Product Team / Indicator Map

Use when someone wants to understand what a feature or interaction actually measures and what its pathway to clinical meaning is.

Structure — organize by interaction / data event:

For each interaction:
- **Data event** — what structured data is generated (field, format, code)
- **Indicator type** — Leading / Lagging / Directional / Loop-closing (with definition)
- **What it generates** — what the signal means clinically or behaviorally
- **Pathway to measure** — which HEDIS / Stars measure it connects to, if any
- **What's required** — data infrastructure, integrations, or agreements needed for it to count

Output format: markdown — paste-ready for Jira, Confluence, or Notion.

Always include:
- Loop-closing events identified and their data requirements spelled out
- Explicit "does not generate a clinical data point" label for directional interactions
- → Template invite

---

## Standard Template Invite — append to all Mode 2 responses

> **Want a blank outcome record template?**
> I'll generate a pre-formatted template with every field, plain-language definitions, and a hypothetical worked example — ready to fill in with your real data in Google Docs or Confluence. Just say "give me the template" and I'll build it for whichever condition or metric you're working on.
