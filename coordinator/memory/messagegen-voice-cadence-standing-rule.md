---
name: messagegen-voice-cadence-standing-rule
description: "FEEDBACK: sounding like AI is a cadence defect (STACKING or CHOPPING), not a vocabulary defect — fix is connective flow, not banned words or shorter sentences; now a dedicated Voice critic on every send gate"
metadata:
  node_type: memory
  type: feedback
  originSessionId: catchup-jul17-2026
---

After Tom flagged Star Ratings emails as reading AI-generated, Dallas traced the real defect to **cadence, not vocabulary** — the existing word-level rules (no em dashes, banned words, forced contractions) all passed, but copy was stacking multiple facts into one comma-separated sentence (STACKING). Voice Fix v1 added a SENTENCE FLOW block and a parallel Voice Audit critic.

**Dallas then caught v1 over-correcting** into the opposite failure: v1's "one fact per sentence, at least one sentence under six words" rule produced staccato, disconnected copy. Voice Fix v2 (his explicit correction) replaced this with the real rule: there are **two** ways to sound like AI — STACKING (too dense, comma-piled) and CHOPPING (too robotic, short flat fragments) — and the fix for both is connective flow (because/so/which means/though), not shorter sentences.

**Why:** word-level rules alone can't catch a structural cadence problem, and overcorrecting toward "short and punchy" creates a different, equally obvious AI tell.

**How to apply:** this is now a standing rule embedded in every motion's MessageGen prompt and enforced by a dedicated `fn_draft_voice_critic` Function returning PASS/FAIL plus a `failure_mode` of STACKED/CHOPPED/NONE, gating every send condition alongside the figure-integrity critic. The two critics judge different things and both must pass — Terra (facts) never checks cadence, Voice (cadence) never checks facts. Ties to [[intradiem-copy-sharpener]], [[no-aiisms-house-style]].
