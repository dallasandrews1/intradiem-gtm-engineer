---
name: graph-engineering-audit-jul27
description: Audit of the swarm against the Claude Code dynamic-workflow (graph engineering) framework, with 5 ranked upgrade moves
metadata:
  type: project
---

Reviewed the "Graph Engineering with Claude" 14-step framework (fan-out/parallel(), fan-in/pipeline(), node contracts via schema, verifier-on-edge, converging cycles, model tiering, self-routing dynamic workflows) against the live swarm. Full writeup published as an artifact: https://claude.ai/code/artifact/c01ac77c-0591-4c56-ac30-9b467abf6a18

**Finding: the swarm already implements ~8 of 14 principles**, independently of this framework, with file-level evidence:
- Node contracts (schema-validated agent() calls): `SCOPE_SCHEMA`/`BUILD_SCHEMA`/`CRITIC_SCHEMA`/`PROPOSAL_SCHEMA` across all 3 `.claude/workflows/*.js` scripts (`gtm-proposal-sweep.js`, `war-room-fanout.js`, `motion-workflow-build.js`)
- Fan-out with `parallel()`, plain-JS reduce edges (`.filter(Boolean).flatMap(...)`, never a "combine" agent), diamond topology (split/work/merge) in all 3
- Perspective-diverse verifier-on-edge: `motion-workflow-build.js`'s 4-lens critic panel (structure / verified-claims / copy-quality / independently re-pulls the known-bad fixture from live Clay rather than trusting the builder) — this is the article's most advanced pattern, built before the framework existed
- Converging cycle: draft→critique→redraft loop capped at 3 rounds, breaks on all-pass
- Router/conditional edge: BLOCKED early-exit in `motion-workflow-build.js`
- Log-don't-notify fan-in at ORG scale: `AGENT_REGISTRY.md` rule 2 (15 scheduled jobs write logs, one rundown reduces them) is the diamond pattern applied to the whole swarm, not just one script

**5 ranked gaps / upgrade moves** (leverage vs effort):
1. **Model tiering inside workflows** [High/Low] — zero `model:` overrides anywhere in the 3 workflow scripts; the Jul 24 fix (see [[usage-optimization-config-jul24]]) only touched the session default, not per-node tiering. Candidates: war-room-fanout's per-account scanner, proposal-sweep's read-state digest agent.
2. **gate-integrity-auditor → fan-out + adversarial-verify diamond** [High/Medium] — highest-stakes agent in the swarm (customer-leak prevention) still runs as one serial subagent instead of per-table parallel fan-out + independent re-verify of any leak found, mirroring the known-bad-verify critic pattern.
3. **Severity router on the daily rundown** [Medium/Low-Medium] — deciding to run the deeper war-room-fanout is still manual; classify signal volume, code-route to shallow vs full scan.
4. **Loop-until-dry leak hunt** [Medium/Medium] — reserve for pre-first-real-send audits (Cost-Mandate is next); keep spawning per-table finders until 2 dry rounds, dedupe against everything seen.
5. **"Say workflow" as standing habit** [High/zero build] — CLAUDE.md working-conventions addition; default to naming a workflow for ad hoc multi-account asks instead of one Agent call or a manual pass.

Copy-paste trigger prompts for moves 1, 2, and 3 are in the artifact, ready to paste back. Moves 4-6 queued, not yet actioned. Waiting on Dallas's go-ahead before building.

**Update: added the Clay Workflow (Alpha) layer to the audit** (Dallas's ask, this framework applies to Clay's own workflow graphs too, not just the Claude Code orchestration scripts). Pulled all 6 live Clay Workflows via `clay workflows diagram <id>` (ground truth, not memory):
- `Cost-Mandate Send-Readiness` (wf_0tiane7qgXQ6PH9UdBA): correct 9-node linear chain, every edge carries real data forward, the template `motion-workflow-build.js` clones
- `Reply Triage + Draft` (wf_0tie1gcUJnvVoAXhN8V): clean 2-node router (classify → conditional draft/hold)
- `Star Ratings 5-Touch Send-Readiness` (wf_0tiegzuo3PzJ4UtUGFA): now a fully serialized E1→E2→E3→E4→E5 chain, re-parented Jul 20 to fix a nondeterministic async-callback race that hit when all 5 MessageGen touches fanned out concurrently from one compose node
- `WFM-Adjacency 5-Touch Send-Readiness` (wf_0tie30io3hiPqSzVRU2): **CONFIRMED LIVE TODAY still wired as true parallel fan-out**, the identical shape that broke Stars, unfixed, dormant only because WFM is on strategic freeze (see [[wfm-workflow-blockers-and-park]], [[motion-focus-jul20]])

**New ranked move 3** (bumped router/loop-until-dry/say-workflow down to 4/5/6): serialize WFM's E2-E5 onto prior-touch gates mirroring Stars's proven fix, and bring it to the Jul 29 Matthew Quan call ([[matthew-quan-clay-cli-outreach-jul24]]) as a concrete platform bug report (Clay's async-callback join doesn't appear to safely handle concurrent nodes writing into a shared downstream Assemble step). Prompt 3 added to the artifact.
