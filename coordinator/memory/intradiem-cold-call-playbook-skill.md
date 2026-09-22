---
name: intradiem-cold-call-playbook-skill
description: Intradiem cold call playbook skill built Sep 22 2026 as the method layer over the repo canon; the Aug 2 playbook stays authoritative for call structure because the brief composer reads it directly
metadata:
  type: project
---

Sep 22 2026. Built `~/.claude/skills/intradiem-cold-call-playbook/SKILL.md`. Until then the only cold-call skill was `league-cold-call-playbook`, written for a different company and sitting in `~/.claude/skills/synced/<uuid>/`, where local edits get overwritten. That one is left untouched.

**Why the split matters:** `motions/shared/Cold_Call_Playbook_Aug2.md` stays canonical for call STRUCTURE because the unattended Daily Action Brief composer reads that file directly through `playbook_sources` in `automation/config/action_brief.json`. The skill carries an explicit drift rule: on opener skeleton, branch handles, branch cap or OPENER FACT CHECK the canon wins and the skill is corrected. Structure changes go in the canon so the composer inherits them; judgement lives in the skill.

**How to apply:** load it after `intradiem-first-draft-engine` and before `intradiem-copy-sharpener` for any spoken output (dial scripts, openers, objection handles, voicemails, voice notes, Daily Action Brief call blocks). Both of those skills now point at it. It carries the Nathan/Jack registers, spoken persona one-liners, Intradiem's real objections, the three claim lanes applied to live calls, and the Star Ratings measure rules with the October 2026 expiry. Related: [[stars-messaging-authored-in-claude-code]], [[cold-call-contract-aug2]].
