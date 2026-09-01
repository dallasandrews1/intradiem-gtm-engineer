---
name: context-bus-ingest-verified-aug6
description: "Context-bus work-Mac ingest path verified working Aug 6 2026 (first real drop landed cleanly); coordinator/CLAUDE.md on the work Mac was stale vs the corrected single-brand rule at ingest time"
metadata:
  type: project
---

Aug 6 2026: the cross-laptop context-bus (built same day on the personal Mac) had its first real drop ingested on the work/enterprise Mac. The previously-untested ingest path (`bin/ingest.sh`) worked: INBOX.md, 9 session digests, and 43 memory files landed in ~/coordinator/memory/ and ~/context-bus/incoming/. So the ingest side is now exercised, not just written.

Actions taken on the work Mac at ingest (Aug 6):
- Synced for parity (bus -> work Mac): AGENT_REGISTRY.md (superset, adds governing rule 5 chain-the-logs), automation/LOG_CONVENTION.md (was missing, referenced by the new rules), 4 skills (gtm-daily-rundown, intradiem-daily-war-room, intradiem-verified-metrics, naveen-weekly-readout) to BOTH ~/coordinator/.claude/skills and ~/.claude/skills, and 2 agents (alumni-champion-watch NEW here, competitor-displacement-watch) to both agent dirs.
- CLAUDE.md was GRAFTED, not blind-copied: the bus CLAUDE.md still carried the RETIRED two-mode brand rule (dallas-brand blurple for internal), which the global ~/.claude/CLAUDE.md supersedes with the single-mode correction. Took the two new bus rules (context-discipline, causal-chain) and set coordinator/CLAUDE.md brand line to single-mode to match the authority. [[rachel-brand-standard-jul31]] is current HTML authority.
- DRIFT AT SOURCE: the PERSONAL Mac's coordinator CLAUDE.md still says two-mode brand. Dallas should fix it there or the next drop re-introduces it.
- Deliberately SKIPPED all .plist files and the automation runtime (.py/.sh). This is the SNAPSHOT machine ([[two-machine-setup]]); nothing gets `launchctl load`ed here or it doubles the morning DM.

STILL OPEN / carry-forward:
- WFM Clay customer-exclusion leak: as of the last log (Aug 3) still OPEN, 5 Elevance (current customer) contacts at READY. The fix is Clay-UI-only and needs Dallas's hands, BUT `Gate_Fix_UISheet_Aug3.md` is NOT on the work Mac and was NOT in the drop (exists only on personal Mac). Since Clay Enterprise auth lives on the work Mac, the sheet must be regenerated here against live WFM table IDs before Dallas can act. See [[gate-fixes-aug3-state]].
- Sustain vocal app deploy still unresolved, Aug 10/11 date; personal Mac / GitHub dallasandrews1/sustain, not on this machine.
