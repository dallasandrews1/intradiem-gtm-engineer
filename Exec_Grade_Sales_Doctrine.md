# Exec-Grade Sales Doctrine

Canonical reference for how Intradiem sells to executives. Skills cite this; it is the source, not a copy of it.
Assembled 2026-07-22 from three inputs Dallas curated, all tracing to the same lineage (Nate Nasralla / Fluint "Selling With"):
- **Dave Kellogg (kellblog)**: how CEOs and boards actually think and operate.
- **The SCR framework** (McKinsey Situation-Complication-Recommendation): the exec-summary memo structure.
- **The Miro exit criteria**: S1 Problem Statement + S2 1-Page Business Case, co-created and customer-validated.

This doctrine sits alongside Dallas's 10-fact belief set (see `Sales_Ideology_Map.md`). Same spine, more operational detail.

---

## Part 1: How execs think (Kellogg, condensed to the action)

1. **Answer, then stop.** Answer in under 10 seconds, leave one open thread. "Six weeks, one dependency on your data team could stretch it." Let them pull the thread if they care. A 90-second methodology tour reads as static.
2. **Be the simplifier.** Complexity reads as incompetence or evasion. One-page business case, one-sentence "what you do." If you can't describe a deal in under 60 seconds, you don't understand it yet.
3. **Attach to what matters.** A CEO gets 2-3 things right and delegates ~25 others. Your deal attaches to one of the 2-3, or it's on the ignore list, however good the ROI slide. Test it: "If your CEO listed the three things that matter this year, is this on the list?" If no, wrong problem or wrong level.
4. **Plan-relative beats absolute.** Boards read percent-of-plan as "is management in control." Anchor the case to the gap: "This gets you from 91% to 97% of plan" beats "23% efficiency gains." Surface the plan and the gap in discovery.
5. **You can't fix a compound metric.** Budget and OKRs are set on atomic metrics (win rate, cycle time, cost-per-transaction, AHT, backlog), not compound ones (CAC payback, Rule of 40, NRR). Pitch the atomic metric someone in the room owns, then show how it rolls up to the compound number the CFO reports.
6. **Leaky bucket + context.** Every business is pouring water in (new revenue) or plugging leaks (churn/cost). Read which one the prospect's problem is before the first exec call. Never present a number without a comparison point: vs plan, vs last year, vs trend. A stat with no context is noise.
7. **Start with what's needed, not what you have.** Open a blank file, not "open recent." Write the outline audience-backward: who's in the room, what do they need to walk out believing. Only then pull slides that serve it. Recycled decks broadcast "this is about my convenience."
8. **Diagnosis → beliefs → actions.** "Given diagnosis X and beliefs Y, we choose policy Z and actions 1-5." Facts get agreement fast; the real debate is the belief about what happens next if nothing changes. That's where the buying decision lives.
9. **Probabilities, not vibes.** Commit = 90%, forecast = 70%, upside = 30%. "Adding risk" without changing the number is meaningless. "Closes March 31 at 70%, here's the one event that moves it to 90." Track your own hit rate by category; a calibrated forecast is something almost nobody has.
10. **Sell the problem (person, problem) pair.** Call the right person about an important problem they own. One test for every sequence: would the named owner of this named problem recognize their own situation in the first sentence? If the first sentence is about you, no.

## Part 2: The SCR exec-summary structure

A one-page memo. Mirrors how execs work a problem: agree on context, feel the tension, hear one clear thing to do.

**S: Situation (what's changing?)** The facts and priorities everyone already accepts. Open on agreement or the rest falls apart.
- Open with their own commitment (their words back to them, nobody argues a goal they set).
- Anchor on a number they accept (their revenue, their volume, not in dispute).
- Tie to the board-level metric (margin, percent-of-plan): a business issue, not an IT purchase.

**C: Complication (why do something now?)** Why it needs action now and gets worse if left alone. Name the root cause and build enough tension to force a decision. Too little tension and it stalls.
- State it in one sentence. Everything under it is evidence for that line.
- Name the root cause, not the symptom.
- Quantify the cost of waiting. A concrete downside turns "interesting" into "urgent."

**R: Recommendation (what should we do?)** More than "buy my product." Names dates, projects, people, plus proof and what happens after.
- Recommend an approach, not a product (a plan an exec can defend).
- Bring proof from a peer they respect (a comparable buyer turns a claim into a pattern).
- Name the alternatives, then pick (handle the objections before they're raised).

**Adapting the order:**
- **Match awareness level.** If they already know the fire, lead with the problem in S. If you're showing them something not yet visible to leadership, put it in C.
- **Flip to R-S-C for an active buy.** If the buying team is past S and C and actively comparing vendors, lead with the Recommendation. Just know a late entrant is usually shaping how they already see S and C.

## Part 3: The two exit criteria (customer-verifiable)

Both must be co-created WITH and validated BY the customer. They double as light champion tests.

- **S1 Problem Statement.** The customer's current-state problem and the negative consequences it creates. Can the champion clearly articulate the business impact? If not, that's early disqualification signal.
- **S2 1-Page Business Case.** Restates the problem, outlines the recommended approach, identifies the priority business outcomes and metrics it supports, and clarifies the required investment. Anchored plan-relative.

Observed benefits (Miro): tighter qualification / faster disqualification, higher average deal size, stronger multi-product attach (problem-first configures a platform solution, not a single product).

## Part 4: How this maps to the skills
- `intradiem-problem-statement` → S1 (Part 3), draws on Kellogg 3, 4, 10.
- `intradiem-exec-summary` → S2 + SCR (Parts 2, 3), draws on Kellogg 4, 5, 6, 7, 8; pulls numbers from `intradiem-roi-business-case`, proof from `intradiem-verified-metrics`.
- `intradiem-deal-review` → internal, Kellogg 1, 2, 9 + the exit-criteria as qualification.
- `intradiem-roi-business-case` → the quantification engine feeding S2's Complication and Recommendation.
- `intradiem-copy-sharpener` / `intradiem-first-draft-engine` → Kellogg 10 (person, problem recognition test).
