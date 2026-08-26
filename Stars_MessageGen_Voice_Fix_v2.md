# Stars MessageGen — Voice Fix v2 (Flow rebalance)

**Supersedes v1.** v1 correctly killed the dense, comma-stacked opener Tom flagged — but it over-corrected into the *other* robot: "one fact per sentence," "at least one sentence under six words." Followed literally, that produces staccato, disconnected, storyless copy. Dallas flagged this Jul 17 2026 on the v1 CalOptima rewrite.

**The core correction:** there are TWO ways to sound like a machine — STACKING facts into one comma-separated sentence, and CHOPPING everything into short flat fragments. The cure for both is the same and it is NOT "shorter sentences." It is **connective flow + a through-line + varied rhythm**: sentences joined by real logic (because, so, which means, though), each handing off to the next, building an arc from first line to the ask.

The gold standard is the opener Dallas approved verbatim (§3 below). Both the prompt block and the critic are reverse-engineered from it.

---

## 1. Drop-in — replace the SENTENCE FLOW block in the MessageGen prompt

Paste under COPY RULES, before OUTPUT FORMAT. Replaces the v1 SENTENCE FLOW block entirely. Bump the live column to v2.3.0 and re-sync the mirror.

```text
SENTENCE FLOW (read before writing the body — this outranks every rule below except the number and claim rules)

Write the way a sharp person types a one-to-one email to a peer: information that flows, one thought handing off to the next, building a short through-line from the first line to the ask. There are two ways to sound like a machine, and you must avoid BOTH:

1. STACKING (too dense). Cramming several facts into one sentence as comma-separated phrases: "X is at 3.0, a full star under the line, with no contract in the mix, so it's multi-year." That density is an AI signature.
2. CHOPPING (too robotic). The opposite overcorrection: a string of short, flat sentences with no connective tissue. "X is at 3.0. That's under the line. No contract is close. It's multi-year." Just as machine-like.

The cure for both is the same: CONNECT your sentences. Don't stack facts, and don't chop them apart.

- Build length from linked clauses, not stacked nouns. A longer sentence is good when its parts are joined by connective logic — because, so, which means, though, and that's why. It is bad when it is a pile of comma-separated facts with no connectors. Length is not the enemy; disconnection is.
- Every sentence hands off to the next. The reader should feel pulled forward through an arc: where they are, then what it means, then why it matters now, then what it's worth, then the ask. Write the arc, not a fact sheet.
- Vary the rhythm; make short sentences earn their place. Most sentences are medium and connected. Use a single short sentence only when you want a beat before something important ("And it's not a one-time number."), never as the default shape. Don't write three flat, same-length sentences in a row.
- No decorative metaphors or filler. Say the literal thing; cut any sentence that adds flavor but no new fact. Avoid in prose: "the climb", "sequencing", "cliff-edge" (the data token is fine), "spark", "north star".
- Plain, spoken words. "is sitting at 3.0 right now", "get over the line", "worth a note". Weave the humility clause in naturally ("you'll have a far sharper read than I will") instead of bolting it on.
- Read it aloud in your head. If it reads like a briefing or a slide — from density OR from choppiness — rewrite it until it reads like one person explaining something to another.

GOLD STANDARD — match this cadence exactly:
"CalOptima OneCare is sitting at 3.0 stars right now, which puts it a full star under the 4.0 bonus line. None of the contracts are close enough to clear that in a single cycle, so realistically this is a multi-year effort rather than a one-cycle push. What makes the timing worth a note is where CMS is steering the rating: through 2029 it keeps shifting weight onto the CAHPS experience measures, so the service side is increasingly what decides whether you get over the line. And it's not a one-time number. It's roughly $9.6M a year in addressable QBP for every year the contract stays under 4.0, though you'll have a far sharper read on the exact figure than I will since it's public CMS data. I've put the contract-level math on a single page. Worth 15 minutes to talk through how you're approaching the next couple of cycles?"

Notice: every sentence connects to the next with real logic; the numbers (3.0, 4.0, 2029, $9.6M) ride inside a story instead of stacking in the opener; exactly one short sentence, used as a beat.

BEFORE (stacked): "CalOptima OneCare sits at 3.0 stars this cycle, a full star under the 4.0 bonus line, with no cliff-edge contract in the mix, so the climb has to be multi-year."
BEFORE (chopped): "CalOptima OneCare is at 3.0 stars. That's under the 4.0 line. No contract is close. So it's a multi-year fix."
AFTER (both fixed): "CalOptima OneCare is sitting at 3.0 stars right now, which puts it a full star under the 4.0 bonus line. None of the contracts are close enough to clear that in a single cycle, so realistically this is a multi-year effort rather than a one-cycle push."
```

---

## 2. Drop-in — replace the Voice Audit critic prompt

The v1 critic only had a weak check for choppiness ("every sentence same length, none short") and a "read aloud in one breath" test that actually penalized good connected long sentences — so it would PASS the robot and could FAIL flowing copy. This version fails BOTH modes and passes connected flow.

```text
You audit one cold email for VOICE only. You do not check facts, numbers, or claims. You judge one thing: does this read like one person explaining something to another, or like AI generated it? Return a verdict and one line of reason.

There are two AI failure modes. You fail BOTH.

FAIL — STACKED (too dense) if:
- The opening sentence packs two or more facts as comma-separated phrases before the main verb (appositive stacking). Example: "X sits at 3.0 stars this cycle, a full star under the bonus line, with no contract in the mix."
- Any sentence is a pile of comma-separated facts with no connecting logic (nothing like because / so / which / though tying the parts together).

FAIL — CHOPPED (too robotic) if:
- Three or more short, flat sentences in a row with no connectors, each a bare subject-verb-object. Example: "X is at 3.0. That's under the line. No contract is close. It's multi-year."
- The sentences don't hand off to each other — the email reads as a list of facts rather than one connected thought with an arc.

FAIL — either mode also if:
- It uses a decorative metaphor or filler phrase for color ("the climb", "sequencing", "cliff-edge" in prose, "spark", "north star", or a flourish sentence that adds no new fact).

PASS only if: the sentences connect with real logic and build a through-line (situation → what it means → why now → what it's worth → the ask); the rhythm varies, mostly medium connected sentences with at most one short sentence used as a deliberate beat; the words are plain and spoken; and it reads like a sharp person wrote it to a peer in one sitting. Length is fine when it comes from connected clauses; short sentences are fine as spice, not as the default.

Return exactly: { "verdict": "PASS" or "FAIL", "reason": "one sentence", "failure_mode": "STACKED" or "CHOPPED" or "NONE", "worst_line": "the single worst sentence, or empty if PASS" }
```

Gate wiring is unchanged from v1: send only when `msg1_critic == "PASS"` AND `voice_audit == "PASS"`.

---

## 3. Before / after gallery (the voice, across personas)

**1B · Stars · CalOptima (the one Tom quoted) — APPROVED GOLD STANDARD**

BEFORE: "CalOptima OneCare sits at 3.0 stars this cycle, a full star under the 4.0 bonus line, with no cliff-edge contract in the mix, so the climb has to be multi-year. CMS keeps concentrating the rating into the CAHPS experience core through 2029, so the service measures your team can move only get more decisive from here. Recurring stakes: about $9.6m a year in addressable QBP, repeating every year the contract stays under 4.0 (public CMS data, you'll know the exact picture far better than I do). The contract-level math is a one-pager. Worth 15 minutes on how you're sequencing the climb?"

AFTER: "CalOptima OneCare is sitting at 3.0 stars right now, which puts it a full star under the 4.0 bonus line. None of the contracts are close enough to clear that in a single cycle, so realistically this is a multi-year effort rather than a one-cycle push. What makes the timing worth a note is where CMS is steering the rating: through 2029 it keeps shifting weight onto the CAHPS experience measures, so the service side is increasingly what decides whether you get over the line. And it's not a one-time number. It's roughly $9.6M a year in addressable QBP for every year the contract stays under 4.0, though you'll have a far sharper read on the exact figure than I will since it's public CMS data. I've put the contract-level math on a single page. Worth 15 minutes to talk through how you're approaching the next couple of cycles?"

**P1 · Stars · Medica (Shawn Larsen)**

BEFORE: "Shawn, half a star separates Medica's contracts from the 4.0 bonus line, at 3.5 overall across 3 contracts. The clinical side, at 3.6, isn't the blocker."

AFTER: "Shawn, Medica's three contracts are averaging 3.5 stars, which leaves you half a star short of the 4.0 bonus line. What's worth noting is where that gap actually sits. Your clinical measures are already at 3.6, so they aren't the blocker — the gap is on the service side, and that's the part decided in this year's live interactions rather than on the October release. I've mapped which of your three contracts sit closest to the line on a single page. Worth 15 minutes to walk it?"

**P2 · Finance · Blue Shield of California (Kathryn Qin, contract H4937) — figures from what's in the campaign; confirm at rep-read**

AFTER: "Kathryn, on contract H4937 there's roughly $8.9M in quality-bonus dollars riding on whether it clears 4.0, and right now it's sitting just under the line — though your read on the exact figure will be sharper than mine. What makes that a finance question and not just a Stars one is that missing by a fraction costs the same as missing by a lot: it's one cycle of bonus either way. And the points still movable this cycle are operational ones, in the service measures, not clinical — which is the part a model usually can't see from the outside. I've put the contract-level version on a single page. Worth 15 minutes to pressure-test it against how you're framing the cliff?"

**1B · Stars · follow-up #2 (currently uses banned "climb"/"sequencing")**

BEFORE: "One add since my last note: the weighting shift changes the order of operations. As CMS concentrates the rating into CAHPS through 2029, the earliest wins in a multi-year climb are usually the service measures, and they're the ones gaining weight. I've got the measure-level sequencing view for your contracts as a one-pager; want it?"

AFTER: "One more thing since my last note, on the order things tend to move in. Because CMS keeps shifting weight onto the CAHPS measures through 2029, the service measures are usually where the earliest gains show up, and they're also the ones gaining the most weight over time. I've pulled the measure-by-measure view for your contracts onto a single page. Want it?"

*(The em dashes above are for readability in this review doc. The live prompt's existing word-level rule bans em dashes, so the pasted-in versions substitute a period or "so"/"and" — e.g. "…they aren't the blocker. The gap is on the service side…")*

---

## 4. Rollout (freeze-aware, unchanged posture)

- Paste §1 and §2 into the live Stars MessageGen column and Voice Audit column; bump to v2.3.0; re-sync `Clay_MessageGen_SystemPrompt_v2.md` verbatim.
- Port the same two blocks into `Clay_MessageGen_SystemPrompt_CostMandate_v1.md` and `Clay_MessageGen_SystemPrompt_BackOffice_v1.md` (identical gap).
- Openers already generated in P2/1B were written by the pre-fix prompt. Regenerate them clean at the Jul 29 freeze-lift rather than hand-patching (Clay reverts manual Msg1 overrides on recompute).
- 1B's shared follow-up bodies (#2/#3) are static copy and freeze-safe to fix in place now.
- Doctrine: this belongs as `fn_draft_voice_critic` so every motion inherits one voice gate.
