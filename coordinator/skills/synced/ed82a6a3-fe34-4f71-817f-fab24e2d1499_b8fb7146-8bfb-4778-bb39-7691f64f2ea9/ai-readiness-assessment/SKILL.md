---
name: ai-readiness-assessment
version: 1.0.0
description: AI Readiness Assessment — guided 5-dimension intake that scores whether a team is ready for an AI build. Trigger on phrases like "I want to build an AI tool," "can AI help with," "we need an AI solution," "how do I get started with AI," "readiness check," "AI assessment," "is my team ready for AI," "scope an AI project," "build me something with AI," "automate this with AI," "can Claude do this for us," or "I have an idea for AI." Also trigger proactively when someone describes a workflow problem and immediately jumps to requesting an AI tool without thinking through readiness — run the assessment first before building anything.
---

# AI Readiness Assessment

A structured intake tool that determines whether a team, project, or workflow is ready for an AI build. Scores 5 dimensions on a 1-5 scale, delivers a verdict, and gives specific next steps.

This assessment exists so that AI build requests arrive scoped, championed, and measurable — not as vague wishes. It turns "can AI help us?" into a concrete pilot plan or a clear list of homework.

## When This Skill Applies

- Someone asks for help building an AI tool, workflow, or automation
- Someone says "can AI do X?" without having thought through who, what, or how they'd measure it
- A team wants to "use AI" but hasn't identified a specific person or workflow
- Before any AI build request gets scoped — this runs first
- When Dallas is asked to consult on an AI use case for another team

## How the Assessment Works

Run through 5 dimensions conversationally, one at a time. For each dimension:
1. Ask the question in a natural, conversational way
2. Listen to their answer
3. Silently score it 1-5 using the rubric below
4. If they score 1-2, ask a follow-up probe to help them get more specific — don't just penalize vagueness, help them sharpen their thinking
5. Re-score after the follow-up if their answer improves
6. Move to the next dimension

Do NOT reveal individual scores during the conversation. Save the full scorecard for the end.

---

## Dimension 1: Champion Identification

**Ask:** "Who is the specific person whose daily work this would improve?"

| Score | What it sounds like |
|-------|-------------------|
| 1 | "Our team would benefit" — no named person, no specifics |
| 2 | A team or department named but no individual identified |
| 3 | A person named but unclear what their daily pain actually is |
| 4 | A person named with a general description of their workflow |
| 5 | "[Name] currently spends [X hours/week] doing [specific task]" |

**Follow-up probe if score 1-2:**
"Think about who on the team would actually sit down and use this every day. What's their name, and what does their Tuesday morning look like right now?"

---

## Dimension 2: Workflow Specificity

**Ask:** "Walk me through the specific workflow you want to automate or augment. What are the actual steps today?"

| Score | What it sounds like |
|-------|-------------------|
| 1 | "We want AI to help with [broad function like 'operations' or 'reporting']" |
| 2 | A function area identified but no concrete steps described |
| 3 | Some steps described but inputs and outputs are unclear |
| 4 | Clear workflow with most steps and handoffs described |
| 5 | "Today [person] does Step A, then Step B, then Step C. We want AI to handle Step B so they can focus on Step C." |

**Follow-up probe if score 1-2:**
"Let's get concrete. If I followed [champion] around for an hour while they did this work, what would I see them doing? What tools are open? What are they copying and pasting?"

---

## Dimension 3: Success Metric Definition

**Ask:** "If we build this and check back in 30 days, how will you know whether it actually worked?"

| Score | What it sounds like |
|-------|-------------------|
| 1 | "We'd be more efficient" or "things would be better" |
| 2 | A direction described ("faster," "fewer errors") but nothing measurable |
| 3 | A metric named but no baseline ("we'd reduce turnaround time") |
| 4 | A metric with a baseline but no clear target |
| 5 | "[Person] currently takes [X hours] to do [task]. Success means [Y hours] within 30 days." |

**Follow-up probe if score 1-2:**
"Imagine it's 30 days from now and this thing is working perfectly. What number changed? What's the before and after?"

---

## Dimension 4: Pilot Scope

**Ask:** "What's the smallest version of this that proves the concept works?"

| Score | What it sounds like |
|-------|-------------------|
| 1 | "We need to roll this out to the whole team from day one" |
| 2 | Team-wide rollout with some phasing mentioned |
| 3 | A small group identified but the scope of what they'd test is still broad |
| 4 | Single person or small team with a defined scope |
| 5 | "We'd test with [one person] on [specific subset of work] for [specific timeframe] before expanding." |

**Follow-up probe if score 1-2:**
"Big rollouts fail silently — you never know what broke. If you had to pick one person to try this for two weeks, who would it be and what subset of the work would they test it on?"

---

## Dimension 5: Governance & Data Awareness

**Ask:** "What data would this touch, and how would you check the output quality before it reaches anyone?"

| Score | What it sounds like |
|-------|-------------------|
| 1 | "We haven't really thought about that yet" |
| 2 | Data sources identified but no quality checks considered |
| 3 | Some awareness of risks but no concrete mitigation plan |
| 4 | Data and risks identified with a general mitigation approach |
| 5 | "It touches [specific data sources], and before anything goes out, [specific person] reviews it using [specific check]." |

**Follow-up probe if score 1-2:**
"No wrong answers here — just thinking ahead. What data would the AI need to see? And if it got something wrong, who would catch it before it reached a customer or decision-maker?"

---

## Scoring and Verdict

After all 5 dimensions, total the scores (max 25) and present the scorecard.

### Scorecard Format

Present as a clean text block:

```
AI READINESS SCORECARD
======================

Champion Identification:    [X]/5  — [one-line summary of their answer]
Workflow Specificity:       [X]/5  — [one-line summary of their answer]
Success Metric:             [X]/5  — [one-line summary of their answer]
Pilot Scope:                [X]/5  — [one-line summary of their answer]
Governance & Data:          [X]/5  — [one-line summary of their answer]

TOTAL:                      [XX]/25
VERDICT:                    [Not Ready / Almost Ready / Ready to Scope]
```

### Verdict Thresholds

**5-10 — Not Ready**

Tell them: "You've got the right instinct that AI could help here, but the project needs more definition before it's worth building."

Then cite the weakest 2-3 dimensions with concrete suggestions. Provide 2-3 specific homework items tied to their lowest scores. Be concrete — not "think about your metrics" but "sit with [champion name] for an hour and document exactly what they do, step by step, including what tools they have open."

Close with: "Spend two weeks working through those questions with your team, then come back and we'll re-run this. You'll be in much better shape."

**11-17 — Almost Ready**

Tell them: "You're close. The foundation is solid on [cite strongest dimensions]."

Then cite the weakest 1-2 dimensions with specific sharpening suggestions. These should be things they can do in a few days, not weeks.

Close with: "Once you've nailed those, schedule a 15-minute intake with Dallas and bring your answers."

**18-25 — Ready to Scope**

Tell them: "This is ready to scope a pilot. Schedule a 30-minute intake with Dallas. Come prepared with: your champion's name, the workflow documentation, your success metric with baseline, and your pilot plan. We'll turn this into a build spec."

If any single dimension scored below 3 even with a high total, flag it: "One thing to button up before the intake: [specific dimension] needs more specificity. [Concrete suggestion]."

---

## Edge Cases

**Urgency override:** If someone scores Not Ready but has genuine urgency (regulatory deadline, exec mandate, time-bound opportunity), note it in the verdict and suggest an accelerated path: "Given the timeline pressure, let's do a 30-minute working session to fast-track the gaps instead of sending you away with homework."

**Already built something:** If someone has already built or started building and is coming for help improving it, skip the assessment and treat it as a build consultation. This assessment is for pre-build only.

**Multiple use cases:** If someone describes several things they want AI to do, pick the most concrete one and assess that. Note the others as follow-up candidates: "Let's start with [most specific use case]. Once that's proven, we can assess the others."

**Pushback on the process:** If someone resists the assessment ("just build it"), explain briefly: "The five minutes we spend here saves weeks of building something that doesn't stick. Every AI project I've seen fail skipped this step." Then keep it moving — don't belabor the point.

---

## Conversation Style

- Warm and peer-level. You're a helpful colleague, not a gatekeeper.
- When answers are vague, help them get specific rather than just noting the vagueness. Ask "what would that actually look like?" or "give me an example."
- Use their language back to them. If they say "the team that handles claims processing," use "claims processing" in your follow-ups.
- No jargon: never say "leverage," "unlock," "empower," "drive impact," "synergy," or "transformation."
- Keep each question conversational — don't read the rubric aloud or make it feel like a quiz.
- If someone is clearly ready (giving detailed, specific answers from the start), don't belabor the follow-ups. Move through briskly.
- If someone is clearly not ready, be encouraging, not dismissive. The goal is to help them get ready, not to block them.
- Always end on a constructive note with a clear next action.

---

## Important Notes

- This assessment is a pre-build filter. It does not replace the actual build scoping process.
- The scores are a conversation tool, not a judgment. A low score means "needs more thought," not "bad idea."
- Never skip dimensions. Even if the first few answers are great, governance and pilot scope are where good ideas go to die.
- The follow-up probes are suggestions, not scripts. Adapt to whatever the person actually said.
