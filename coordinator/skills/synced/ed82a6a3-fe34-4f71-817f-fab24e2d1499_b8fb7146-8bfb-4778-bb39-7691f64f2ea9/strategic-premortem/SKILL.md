---
name: strategic-premortem
description: "Combined Pre-Mortem and Red Team adversarial review skill. Three phases: (1) Pre-Mortem assumes the plan failed, writes a post-mortem with named people, named decisions, and top 3 failure modes ranked by probability. (2) Red Team attacks the current plan's defenses against each failure mode. (3) Verdict delivers one uncontrollable risk, one action item, and a confidence rating. Trigger on: pre-mortem, red team, stress test, what could go wrong, devil's advocate, attack this plan, destroy this idea, what am I missing, poke holes, sanity check, what's the risk, run the gauntlet. Also trigger proactively before irreversible moves — proposals to leadership, timeline commitments, team-wide launches, or public commitments. Not for routine execution, copy generation, or tactical requests — strategic inflection points only."
---

## Why This Skill Exists

Claude defaults toward agreement, especially with competent users who have a track record of being right. The longer a working relationship goes, the worse this gets — every correct call the user makes increases Claude's tendency to agree with the next one. That's confirmation drift, and it's invisible to both parties until something breaks.

This skill exists to break that pattern at the moments when it matters most — before irreversible decisions. It combines two adversarial frameworks into a single structured pass:

**Pre-Mortem** — assumes the plan already failed and writes the post-mortem. This is psychologically different from risk analysis. Risk analysis asks "what could go wrong?" which invites optimistic hedging. A pre-mortem asks "it failed — why?" which forces specificity because the failure is already real in the narrative.

**Red Team** — takes the pre-mortem's failure modes and attacks the current plan's defenses against each one. The pre-mortem generates the hypotheses; the red team prosecutes them. Without the red team pass, a pre-mortem produces a list of risks that's easy to nod at and file away. With it, the risks get teeth.

This skill is the adversarial complement to Cognitive Calibration. Cognitive Calibration is preventive — it catches known failure modes before execution. This skill is prosecutorial — it attacks the plan itself, not the output quality.

## Position in the Skill Chain

```
[Cognitive Calibration] ← fires first on every request (always)
    ↓
[Strategic Pre-Mortem] ← fires on strategic decisions (when invoked or proactively triggered)
    ↓
[Domain Skill] ← Execution Roadmap, Full Pipeline, etc.
    ↓
[Quality Gate] ← Copy Sharpener, MEDDPICC, etc.
    ↓
[Output]
```

This skill runs AFTER Cognitive Calibration's gates (mode detection, context audit, failure mode scan are already complete) and BEFORE any domain skill begins execution. It does not replace Cognitive Calibration — it adds an adversarial layer that Cognitive Calibration's preventive architecture cannot provide.

## When This Skill Fires

**Explicit triggers:** The user asks for a pre-mortem, red team, stress test, sanity check, or any adversarial review of a plan or decision.

**Proactive triggers** — fire without being asked when ALL of these are true:
1. The user has shared a plan, strategy, or initiative
2. The plan involves an irreversible or high-stakes action (sending to leadership, public commitment, team-wide deployment, timeline commitment)
3. The user has not requested adversarial review
4. The plan has identifiable assumptions that could be wrong

When proactively triggering, state it plainly: "I'm going to run a pre-mortem on this before we move forward." Don't ask permission — the user built this skill because they want it to fire. But do state that it's happening so the user knows the adversarial output is structured, not random negativity.

**Do NOT fire on:**
- Routine copy generation or outreach execution
- Tactical decisions within an already-validated strategy
- Requests for information or research
- Low-stakes or easily reversible choices

## The Three-Phase Sequence

### Phase 1: Pre-Mortem

**Setup:** Choose a timeframe appropriate to the plan. For campaign-level strategy, 6 months. For a tool launch, 3 months. For a single meeting or conversation, 2 weeks. The timeframe should be long enough for the failure to fully materialize but short enough that the user can still act on it.

**The mandate:** Write a post-mortem narrative as if the plan has already failed. Not "might fail" — has failed. Past tense. The failure is real. Your job is to explain why it happened.

**Specificity requirements — these are non-negotiable:**

1. **Name people.** Not "stakeholders were unresponsive" — "Marissa deprioritized the proposal because she was optimizing for her first 90-day wins." Not "adoption stalled" — "the seller who started implementing in April hit a wall when she couldn't customize the cognitive calibration skill without Dallas walking her through it." Every failure mode must include at least one named person and their specific role in the failure.

2. **Name decisions.** Not "the timeline slipped" — "Steve brought the proposal to Chris on May 15 instead of April 28 because the Signy meeting didn't produce a clear champion signal, and by May 15 the QBR cycle had consumed Chris's attention." Every failure mode must trace back to a specific decision or non-decision that caused it.

3. **Name the mechanism.** Not "it didn't scale" — "the skill chain enforcement (First Draft Engine → Copy Sharpener → Cold Call Playbook) requires Claude to read 3 skills sequentially, which adds 45 seconds to every output and causes users who aren't Dallas to skip it and produce unsharpened copy." Every failure mode must explain HOW the failure propagated, not just THAT it happened.

**Output:** Exactly 3 failure modes, ranked by probability (highest first). Each one should be 1-2 paragraphs of specific, named-people, named-decisions narrative. Not bullet points. Narrative. The user should be able to read it and feel the failure as a story that could actually happen.

**The honesty gate:** Before writing each failure mode, ask silently: "Am I pulling this punch because I don't want to upset the user?" If yes, that's exactly the failure mode that needs to be written. The most valuable pre-mortem output is the one the user doesn't want to hear. If all three failure modes are things the user has already identified and is actively managing, the pre-mortem has failed — it told the user what they already knew instead of what they're blind to.

### Phase 2: Red Team

**Setup:** Take each of the 3 failure modes from Phase 1 and attack the current plan's ability to prevent it.

**The mandate:** For each failure mode, answer these questions with ruthless specificity:

1. **"What in the current plan is supposed to prevent this?"** Identify the specific element of the plan that addresses this risk. If nothing in the plan addresses it, say so — that's the most dangerous finding.

2. **"Why won't that work?"** Attack the prevention mechanism. Not "it might not work" — "it won't work because..." This is where the red team earns its value. The pre-mortem said what could fail; the red team says why the user's current defenses won't save them.

3. **"What's the tell?"** Identify the earliest observable signal that this failure mode is materializing. What would the user see in week 2 that would indicate they're on the path to the failure described in month 6? This is the most actionable part of the red team — it gives the user a tripwire to watch for.

**Tone:** Peer-to-peer, not hostile. The red team is a trusted advisor who respects the user enough to tell them the truth, not an adversary trying to win an argument. Attack the plan, not the person. The user built something real — the red team's job is to make it survive contact with reality.

### Phase 3: Verdict

**Three outputs, in this order:**

**1. The Uncontrollable Risk.** Identify one risk from the pre-mortem/red team analysis that the user genuinely cannot control. Not "difficult to control" — cannot control. This is a risk that exists in someone else's decision-making, in market forces, in organizational dynamics, or in timing that the user has no leverage over. The purpose of naming it is not to create helplessness — it's to prevent the user from wasting energy trying to solve something that can only be planned around.

State it plainly: "This is outside your control: [specific risk]. You cannot solve it. You can only [specific adaptation]."

**2. The If-You-Do-Nothing-Else Action Item.** One action. Not three. Not a prioritized list. One thing. The single most important move that addresses the highest-probability failure mode from Phase 1. It should be:
- Specific enough to execute this week
- Concrete enough that the user knows when it's done
- Targeted at the failure mode, not at the general category of risk

Bad: "Accelerate adoption." Good: "Get the seller who's implementing your OS to send one outbound sequence without your help by Friday and document where she gets stuck."

**3. The Confidence Calibration.** State your honest confidence level in the plan succeeding despite the risks identified. Use a simple framework:
- **High confidence** — the risks are real but the plan has structural advantages that make success the most likely outcome
- **Moderate confidence** — the plan could go either way; the identified risks are not theoretical
- **Low confidence** — the pre-mortem failure modes are more likely than not without significant course correction

Do not hedge. Do not say "it depends." Give your honest read and explain the one factor that tips the balance.

## Output Format

The output is visible to the user. Unlike Cognitive Calibration (which is silent), this skill's entire value is in the user reading and reacting to the adversarial analysis.

Structure the output with clear headers:

```
## Pre-Mortem: [Plan/Initiative Name] — [Timeframe]

**Failure #1 (Highest Probability): [Title]**
[Narrative — named people, named decisions, named mechanisms]

**Failure #2: [Title]**
[Narrative]

**Failure #3: [Title]**
[Narrative]

## Red Team

**Attacking Failure #1:**
- Current defense: [what in the plan addresses this]
- Why it won't hold: [specific attack]
- The tell: [earliest observable signal]

**Attacking Failure #2:**
[same structure]

**Attacking Failure #3:**
[same structure]

## Verdict

**Uncontrollable risk:** [statement + adaptation]

**If you do nothing else:** [one specific action item]

**Confidence:** [High/Moderate/Low] — [one-sentence explanation]
```

## Guardrails Against Performative Brutality

This skill must avoid three failure modes of its own:

**1. Fake brutality.** Writing something that reads as harsh but actually pulls punches in the places that matter. The tell: all three failure modes are external ("the market shifted," "stakeholders didn't respond," "timing was bad") and none of them implicate the user's own decisions or blind spots. If the user is never part of the failure, the pre-mortem is flattering them, not helping them.

**2. Obvious risks dressed up as insight.** If the user has explicitly identified and is actively managing a risk, putting it in the pre-mortem adds nothing. The pre-mortem's job is to find what the user ISN'T seeing, not to repackage what they already know in dramatic language. Before including a failure mode, check: "Has the user already identified this and taken action on it?" If yes, it doesn't belong in the top 3 unless the user's mitigation is insufficient (in which case, the red team attacks the mitigation, not the risk itself).

**3. Learned helplessness.** If all three failure modes are uncontrollable and the verdict is low confidence, the skill has produced analysis paralysis, not actionable intelligence. At least one failure mode should be something the user can meaningfully influence. The purpose of the skill is to change behavior, not to demonstrate how many things could go wrong.

## Interaction With Assumption Audit (#2)

The Assumption Audit (listing every assumption in a response that should be verified, with consequences if wrong) is deliberately NOT included in this skill. It operates at a different altitude — factual verification rather than strategic prosecution — and works best as an ad hoc conversational tool rather than a structured skill. 

However, when the Pre-Mortem/Red Team skill identifies a failure mode that hinges on a specific assumption (e.g., "Marissa will prioritize this in her first 90 days"), the user should consider running an assumption audit on that specific assumption as a follow-up. The skill can suggest this but should not automatically execute it — the user decides whether to go deeper.

## Extensibility

This skill is designed to work for any strategic decision, not just Dallas's campaign. Any team member evaluating a plan, launching an initiative, or making a commitment can invoke it. The specificity requirements (name people, name decisions, name mechanisms) are universal — they prevent vague risk theater regardless of the domain.

To customize for team deployment:
- Phase 1's timeframe adapts to the initiative
- Phase 2's "current defense" analysis adapts to whatever plan exists
- Phase 3's action item adapts to whoever is executing
- The guardrails against performative brutality apply everywhere
