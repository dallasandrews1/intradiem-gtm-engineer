---
name: feedback-check-memory-before-describing-pipeline
description: "Sep 5 2026: before describing how any live motion works (what generates copy, what loads where), read the standing memory first; Claude told Dallas the Clay MessageGen columns fed the lemlist campaigns when the Aug 6 memory says the per-lead variables are Claude-side"
metadata:
  type: feedback
---

Sep 5 2026, all-hands narration prep. Asked whether the engine takes the Clay enrichment columns, writes per-person messaging, and loads it into lemlist as custom variables, Claude said yes and described the Clay MessageGen path as the source. Dallas corrected it: the live campaigns' per-lead variables were generated Claude-side (the skills), critic-gated, and loaded via the bridge; no Clay column produced them. The memory [[lemlist-variable-generation-is-claude-side]] (Aug 6) already said exactly that.

**Why:** the narration Dallas gives leadership has to survive any follow-up; a confident description of the wrong path is worse than no description.

**How to apply:** when asked how a motion works end to end, grep memory and the registry for the surface in question before answering, and separate what is BUILT (Clay MessageGen + critic + sync, July) from what the LIVE campaigns actually used (Claude-side variables). Say "the engine" for the whole system and never claim a specific column is the source unless the sync path is verified live. Related: [[tech-stack-verified-read-sep5]], [[feedback-thorough-at-all-costs]].
