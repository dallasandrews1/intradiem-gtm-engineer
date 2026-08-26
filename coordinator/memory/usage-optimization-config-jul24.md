---
name: usage-optimization-config-jul24
description: Jul 24 2026 config changes to stop burning the weekly Claude Max limit — root causes from the usage panel and the fixes applied
metadata:
  type: project
---

Jul 24 2026: Dallas hit 65% of his weekly Claude Max (7-day) limit in ~2 days (resets Wed). The usage panel's "what's contributing" (local sessions on this machine, does NOT include Cowork/claude.ai) named the real causes — it was NOT mainly Cowork browser-driving:
- **60% of usage was at >150k context** — marathon sessions re-bill the whole context every message. Fix is behavioral: `/clear` (or X-out + new session, equivalent) when switching TASKS; `/compact` to keep the same task but shrink. Never run one giant session across multiple tasks. This is the single biggest lever.
- **26% from the Clay MCP** (plugin:clay:clay) — its tool results stay in context all session. Do NOT disable the plugin: the Clay-reading scheduled jobs (gate-integrity, credit-strategist, table-hygiene, pipeline-receipts) use those tools and would break. Mitigated by short sessions + those jobs now on Sonnet.
- **11% from cognitive-calibration** — fires inline on every message, large. FIXED Jul 24: scoped "When This Skill Applies" + frontmatter description in both mirrors (`~/.claude/skills/cognitive-calibration/SKILL.md` and `~/coordinator/.claude/skills/cognitive-calibration/SKILL.md`) to fire only on strategy/copy/analysis/judgment work, with an explicit non-firing list (file edits, exports, list ops, simple lookups) and a carve-back for browser/live-tool reads that become reported claims. Note: the two mirrors had already drifted independently (global had a Jul 14 Gate 2B browser-ops addition coordinator's Jul 9 copy lacked) — edited each in place rather than merging that unrelated drift; worth reconciling separately if it matters.
- **~16% from scheduled skills on the premium model** (gtm-daily-rundown 8, naveen-weekly-readout 5, war-room 3, plus others).

**Changes applied to ~/.claude/settings.json + the 12 automation wrappers (backups in scratchpad/cfgbackup):**
1. All 12 `run_*.sh` wrappers in `Intradiem GTM Engineer/automation/` now call `claude --model claude-sonnet-5 -p` (were inheriting the premium default at xhigh). run_control_tower.sh + run_swarm_heartbeat.sh untouched (no claude call).
2. `effortLevel`: **xhigh → high** (global; biggest single multiplier; drop to medium for more savings on routine work).
3. Default `model`: **claude-fable-5[1m] → claude-sonnet-5** (Dallas's call, picked the recommendation). Takes effect on NEW sessions.

**Standing model rule going forward:** Sonnet 5 is the daily driver for everything (Clay, copy, lists, execution, strategy chat — it handles complex fine; rigor comes from the skills). `/model opus` ONLY when wrong-is-expensive AND judgment-heavy: exec/Naveen deliverable, a committed decision (roadmap/premortem/pricing), first-impression senior-buyer copy. `/model claude-fable-5[1m]` ONLY for genuinely huge-context work (feeding a big transcript/doc). See [[high-stakes-no-errors-posture]], [[clay-find-people-imports-are-free]].
