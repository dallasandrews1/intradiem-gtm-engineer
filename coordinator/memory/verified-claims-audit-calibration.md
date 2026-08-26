---
name: verified-claims-audit-calibration
description: "Calibration gotchas for a verified-claims / voice audit AI column (the Wave 2 Audit gate over assembled emails): three false-positive classes to pre-empt so it doesn't HOLD clean, approved copy."
metadata:
  node_type: memory
  type: reference
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T22:47:12.759Z
---

Jul 20 2026: Building the Stars "Wave 2 Audit" table column (one AI column that figure-audits + voice-audits the 5 assembled emails and returns READY/HOLD to gate the send). A too-literal audit HOLDs approved copy. Three false-positive classes learned the hard way, all now written into the gate prompt (canonical copy lives in `Intradiem GTM Engineer/STARS_WAVE2_HANDOFF_README.md` section 4):

1. **Fail-closed default over-HOLDs.** "Any doubt/borderline = HOLD" plus a long checklist means it always finds something to doubt and HOLDs everything. Fix: default to PASS; only HOLD when it can QUOTE the offending words AND name a rule that's literally written in the prompt; forbid inventing rules; a borderline case is a PASS. Also drop mechanical rules like "3+ commas = stacking" (flags good prose); define stacking as "3+ distinct facts crammed with no connectors."

2. **Product-capability read as a forbidden customer claim; CAHPS read as clinical.** The verified-claims rule ("only the 6 Humana lines are permitted Intradiem customer results") gets over-applied to the PRODUCT PITCH ("teams use Intradiem to move service and CAHPS measures in real time"), which is approved copy, not a customer-result claim. And "CAHPS" gets misread as clinical/HEDIS. Fix: explicitly separate PRODUCT CAPABILITY (always permitted, never a customer claim) from a named-CUSTOMER RESULT/ROI figure (restricted to the whitelist), and state that CAHPS is a customer-EXPERIENCE/service measure Intradiem DOES move, NOT clinical/HEDIS (only blood-pressure/diabetes/med-adherence/named-HEDIS claims are the clinical HOLD).

3. **A whitelisted verbatim line that itself violates a voice rule.** Humana line 4 ("...table stakes now, not a nice-to-have") is an "X, not Y" shape = the false-contrast VOICE rule. The prompt then contradicts itself (Check 1 says use verbatim, Check 2 says that shape is a HOLD) and the model thrashes, dumping its reasoning into the verdict field and flip-flopping HOLD->READY. Fix: EXEMPT the whitelisted proof lines (the 6 Humana + the UHC stakes line) from ALL voice rules; apply voice checks only to the surrounding original copy. Plus force a clean output: "decide silently, output ONLY `READY` or `HOLD: <reason>`, no narration, no self-correction" (a rambling verdict breaks the `startsWith("READY")` gate).

General rule: a verified-claims audit must loosen ONLY where it flags APPROVED copy (the pitch, the whitelisted proof lines, service/CAHPS framing). Never loosen the real catches: per-contract dollar misattribution, altered/off-list customer figures, em dashes, cross-touch proof repetition. The audit column is cheap (~0.5 credits/row) so calibrate it freely; the workflow batch is the expensive part. See [[proof-lines-attribute-to-intradiem]] and [[stars-5touch-engine-live-state-jul20]].
