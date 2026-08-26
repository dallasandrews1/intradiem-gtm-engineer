---
name: clay-input-rule-refined
description: Refined Clay --input rule — free for any build/test/smoke; only the final pre-send-wave gate check needs real rows.
metadata:
  type: feedback
---

**Refined rule (Dallas, 2026-07-19) — supersedes the earlier "never hand-crafted --input" and the interim "structural-smoke-test-only" versions:**

Clay `--input` is fine ANYTIME it's helpful: building, testing, debugging, exploring, or a labeled structural smoke test (use real values). Loosened because the restrictive version blocked genuinely useful smoke tests.

The ONE guardrail kept: the FINAL gate-semantics validation right before a real send wave runs on REAL rows (UI or audience-segment), never synthetic `--input`. Never present an `--input` run as proof a real wave will qualify/gate correctly.

**Why the one guardrail (concrete):** gate functions depend on real null-vs-empty column semantics. Live example in Dallas's own build: `customer_exclude` is stored as text `"TRUE"` but the workflow treats it as a boolean, so a synthetic run could "prove" current customers (humana/uhc/cvs/molina/elevance/hcsc) are excluded while a REAL row passing text `"TRUE"` slips a current customer into a cold campaign. In a prove-it-or-lose-it budget, one cold email to a current customer is a bad look. That's the asymmetric risk the final real-row check protects against.

In both CLAUDE.md working conventions. The smoke tests this session (WFM + Stars) are exactly the now-allowed use. See [[credit-budget-correction-jul18]].
