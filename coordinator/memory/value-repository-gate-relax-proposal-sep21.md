---
name: value-repository-gate-relax-proposal-sep21
description: ADOPTED Sep 21 2026, three claim lanes (Intradiem outcomes strict; public prospect facts self-serve with source, as-of date and send-time re-check; modeled estimates 1:1 and labeled)
metadata:
  type: project
---

Sep 21 2026: Dallas raised that the verified-claims rules may be too strict for where the data and outreach are. Proposal given to him, awaiting his call: keep one truth standard, split by claim type and speed. Lane 1, Intradiem and customer outcome claims: unchanged, Repository plus marketing clearance (Humana and Virgin Media named; JPMC, AT&T, Liberty Mutual never). Lane 2, public facts about the prospect (CMS measure stars, the Jun 17 2026 HPMS memo, filings): self-serve with a primary source, an as-of date and a freshness re-check at send time, no approval step. Lane 3, our modeled estimates (forgone QBP, addressable_pct): 1:1 only with the estimate label, never a headline number.

**Why:** the same day's session showed three confident claims were wrong or stale (which measures still pay, a 3.5 rating for plans CMS had re-rated to 4.0 or higher, a fatigue story with no sends behind it). The failure was freshness, not strictness, so the fix is a faster public-data lane with a date check, not a looser gate on outcome claims.

**How to apply:** until Dallas adopts or edits this, the existing rule in CLAUDE.md stands; do not bypass the gate. If adopted, update CLAUDE.md house style, the intradiem-verified-metrics skill and VERIFICATION_AUDIT.md together. Related: [[clover-ruling-stars-measure-thesis-sep21]].

**Sep 21 2026, later:** Dallas said adopt it, with "show me the diff before saving". Edits are STAGED, not saved: diffs in `october-flywheel/proposed_lanes_diff_sep21/` covering coordinator/CLAUDE.md (3 identical copies: repo coordinator/, ~/coordinator/, ~/.claude/), the verified-metrics SKILL.md (5 identical copies; the claude.ai-synced copy differs and is managed elsewhere), VERIFICATION_AUDIT.md (dated addendum, history untouched) and the Value Repository (lanes section, the "does not ship" sentence scoped to Lane 1, Clover time-stamp on the UHC $190M row, CMS math row re-sourced to the Jul 22 2026 re-issue, new row for the Jun 17 2026 HPMS memo). Apply only on his go.

**Customer-knowledge thread (same day):** Dallas asked whether to ask colleagues about the six payer customers or research first. Advice given: research first (Customer Value Registry, account-health evidence files, Salesforce, Slack, Otter), then ask the AMs the one question systems cannot answer; anything found is CV-INTERNAL, usable blinded per [[feedback-social-proof-ships-sep18]].

**ADOPTED and applied Sep 21 2026** on Dallas's go. Byte-verified against the staged versions: three CLAUDE.md copies (repo coordinator/, ~/coordinator/, ~/.claude/), five verified-metrics SKILL.md copies, VERIFICATION_AUDIT.md (dated addendum) and the Value Repository. The "How to apply" line above about the old rule standing is superseded: the three-lane rule is now the rule. Not updated: the claude.ai-synced copy of the skill under ~/.claude/skills/synced/ (managed at the source, already differed). Still failing the new send-time re-check until corrected: live Stars copy, the E1 prompt and every lead's qbp_avg, see [[clover-ruling-stars-measure-thesis-sep21]].
