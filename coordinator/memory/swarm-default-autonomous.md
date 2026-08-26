---
name: swarm-default-autonomous
description: DESIGN PRINCIPLE (Jul 19) - new swarm agents default to scheduled/autonomous, never on-demand-only; the goal is a swarm that assists Dallas without him remembering to launch anything
metadata:
  type: feedback
---

DESIGN PRINCIPLE (Dallas, Jul 19 2026): "the point is to have a swarm, ultimately, that removes the need for me to remember to launch any of them in order for them to be assisting me."

**Why:** an on-demand agent Dallas has to invoke is a tool, not a swarm member. The swarm's value is zero-recall operation: it works FOR him and WITH him without a prompt.

**How to apply:**
- Default every new agent to a SCHEDULED launchd job that fires on its own, does its work, writes a dated log to `automation/logs/`, and never DMs (single-morning-brief rule). The daily rundown consolidates.
- On-demand invocation stays available too, but scheduled is the default, not the afterthought.
- Retrofit: the on-demand Tier 1 agents (gate-integrity-auditor before-a-wave, pipeline-receipts-tracker before-readout) should get scheduled weekly backstops in the next scheduling pass, keeping their event-triggered use too.
- Respect the four registry rules: nobody but Dallas, single morning brief, read-only by default, log-don't-notify. See [[agent-registry-and-architect]], [[tier1-swarm-agents-built]].
