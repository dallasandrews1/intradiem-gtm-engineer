# Stars MessageGen — Voice Fix v1
**Purpose:** stop the choppy, over-dense, AI-sounding sentences at the source. Two changes: a VOICE & CADENCE block added to the MessageGen prompt, and a second critic (Voice Audit) wired into the send gate next to Terra. Authored Jul 16 2026 after Tom's read on the Star Ratings emails.

---

## 1. Root cause (why the current stack missed it)

The live MessageGen prompt (v2.2.3) polices voice only at the **word** level: no em dashes, forced contractions, a banned-word list, uncontracted "I would" flagged. Every line Tom flagged passes all of that. The tells are **cadence**, not vocabulary:

- *"CalOptima OneCare sits at 3.0 stars this cycle, a full star under the 4.0 bonus line, with no cliff-edge contract in the mix, so the climb has to be multi-year."* — four facts stacked in one sentence. That density is the AI signature.
- *"...how you're sequencing the climb?"* — a reached-for metaphor.

The prompt's own "plain, direct, declarative, front-load, pack the contract math into sentence one" instruction actively **produces** the appositive pile-up. And the only gate downstream is Terra, which checks whether the dollar figures match the source row. Terra has zero voice checking, so a numerically perfect but choppy email passes clean.

Fix both ends: tell the writer to write with flow, and add a gate that fails on the lack of it.

---

## 2. Drop-in: add this block to the MessageGen prompt

Paste under COPY RULES, before OUTPUT FORMAT. (Then bump the live column to v2.2.4 and re-sync the mirror file.)

**Source of the standard:** these rules operationalize Intradiem's own brand voice (intradiem.com/brand-guidelines) — "clear, confident, and human by design," avoid jargon and idioms, simple explanations, people-first. Per Jenn East's Jul 16 ask, the brand voice is the authority the copy has to pass, enforced in the engine instead of cleaned up by hand. This also answers Tom's "built by humans" point: the human standard lives in the generator, not just in the rep's edit.

```text
SENTENCE FLOW (read before writing the body — this outranks every rule below except the number and claim rules)

Write the way a sharp person types a one-to-one email, not the way a brief summarizes facts. The biggest tell that a machine wrote this is cramming several facts into one sentence with commas. Avoid that harder than any banned word.

- One fact per sentence in the opener. Lead with the single sharpest fact, then stop. The next fact goes in the next sentence.
- No stacked appositives. Never chain "X, a Y under the Z, with no A, so B." If you have written two commas before the main verb, break the sentence in two.
- Vary the length on purpose. At least one sentence in the email is under six words. Never write three sentences in a row of the same shape and length.
- No metaphors or decorative phrases. Say the literal thing. Specifically banned in prose: "the climb", "sequencing", "cliff-edge" (the data token is fine, the word in a sentence is not), "the ground you move", "spark", "north star". Also cut any sentence that adds flavor but no new fact.
- Plain words over precise-sounding ones. "sits at 3.0 stars this cycle" becomes "is at 3.0 stars right now". "a full star under the 4.0 bonus line" stays only if it is its own short sentence. Say it the way you'd say it out loud.
- Read the draft aloud in your head before returning it. If a sentence needs a breath in the middle, or sounds like a slide in a deck, rewrite it shorter.

REWRITE EXAMPLES — match the AFTER cadence, never the BEFORE.

BEFORE (dense, AI): "CalOptima OneCare sits at 3.0 stars this cycle, a full star under the 4.0 bonus line, with no cliff-edge contract in the mix, so the climb has to be multi-year."
AFTER (natural): "CalOptima OneCare is at 3.0 stars right now. That's a full star under the 4.0 bonus line, and closing it is a multi-year job, not a one-cycle fix."

BEFORE (reached-for close): "Worth 15 minutes on how you're sequencing the climb?"
AFTER: "Worth 15 minutes on how you're planning the next couple of cycles?"

BEFORE (dense): "Shawn, half a star separates Medica's contracts from the 4.0 bonus line, at 3.5 overall across 3 contracts. The clinical side, at 3.6, isn't the blocker."
AFTER: "Shawn, Medica's three contracts sit at 3.5. That's half a star under the 4.0 bonus line. Your clinical stars are already at 3.6, so that isn't the blocker. The gap is on the service side."
```

---

## 3. Drop-in: new critic column — "Voice Audit"

A second GPT critic column, parallel to Terra. It checks **only** cadence, never facts. Add its PASS to the sync run-condition: send only when `msg1_critic Status == "PASS"` **AND** `voice_audit == "PASS"`.

```text
You audit one cold email for voice only. You do not check facts, numbers, or claims. You judge one thing: does this read like a person typed it, or like AI generated it. Return a verdict and one line of reason.

FAIL if any of these is true:
- The first sentence packs two or more facts separated by commas (appositive stacking). Example FAIL opener: "X sits at 3.0 stars this cycle, a full star under the bonus line, with no cliff-edge contract in the mix."
- Any sentence has two or more commas before its main verb.
- The email uses a metaphor or decorative phrase for color: "the climb", "sequencing", "cliff-edge" in prose, "the ground you move", "spark", "north star", or a flourish sentence that adds no new fact.
- Every sentence is about the same length, and none is short (under ~6 words).
- Any sentence cannot be read aloud in one breath without a pause in the middle.
- The copy reads like a brief or a slide, not a one-to-one email.

PASS only if: one idea per sentence up front, varied sentence length with at least one short sentence, plain words, no decorative phrases, and it sounds like a sharp person wrote it in one sitting.

Return exactly: { "verdict": "PASS" or "FAIL", "reason": "one sentence", "worst_line": "the single worst sentence, or empty if PASS" }
```

---

## 4. Rollout (freeze-aware)

- **P1 wave 1 already sent today and cannot be recalled.** Do not regenerate — MessageGen, sync, and Reset stay frozen until the blank snake_case unify-field source repair, per the standing rule. This fix takes effect at the **next wave** (Jul 29 check), not by re-running P1.
- **Unsent touches are fixable now by hand, not by regen.** P1's follow-ups (#2/#3), plus P2 (Finance, launches Mon Jul 20) and 1B (launch on your call) haven't gone. You can hand-edit that copy directly in the campaign to the AFTER cadence — a copy edit is not a MessageGen re-run, so it respects the freeze. Note: the CalOptima email Tom quoted is 1B, which hasn't launched, so his worst example is still fully editable.
- **Port the same two blocks** into the other MessageGen prompts, which have the identical gap: `Clay_MessageGen_SystemPrompt_BackOffice_v1.md` and `Clay_MessageGen_SystemPrompt_CostMandate_v1.md`.
- **After pasting into the live column:** bump to v2.2.4, re-sync `Clay_MessageGen_SystemPrompt_v2.md` to match verbatim, and capture the Voice Audit column text into that file's section 4 the same way.
- **Optional next step:** this belongs in your Clay Functions doctrine as `fn_draft_voice_critic`, so every motion inherits one voice gate instead of each prompt carrying its own copy.
