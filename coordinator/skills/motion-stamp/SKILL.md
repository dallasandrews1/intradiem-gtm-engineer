---
name: motion-stamp
description: "Stamp a new Intradiem outbound motion fast (minutes, not a week of hand-tinkering) on the workflow-first path. Assembles the 5-touch MessageGen prompt set from the canonical library (voice_core + stage_ladder + filled motion_slots), builds the send-readiness workflow via the Clay CLI from the proven template, and returns the short UI checklist for the must-stay-manual steps. Trigger on: stamp a new motion, spin up a motion, new motion factory, add a motion, motion-stamp, self-serve motion. Load when someone wants to launch a new outbound motion without waiting on Dallas."
---

## The goal
A new motion should be self-serve. Someone launching one fills the motion slots and runs the stamp; they do not wait a week for Dallas to hand-build columns. This skill is the front door to Dallas's motion factory (extends clay-motion-factory-scaffold-system; the Clay_Golden_Standard governs, this executes).

## The hard constraint (state it, don't fight it)
Clay AI columns, table structure, and Functions are UI-only. No API/trigger auto-adds a MessageGen column to a table. What IS agent-buildable: WORKFLOW logic (`clay workflows create` + `edit_node`) and enrichment/data. So generation and gating live in the WORKFLOW (reproducible by CLI), the table stays a thin data layer built by golden Duplicate, and the 7 Functions are workspace-shared (reused, never rebuilt).

## Inputs
1. A filled `templates/motion_slots.md` for the new motion (core position, one idea, personas, signal semantics, bans, brand convention A/B, sender).
2. `templates/voice_core.md` (motion-invariant, verbatim).
3. `templates/stage_ladder.md` (motion-invariant escalation).
4. The proven workflow template (the WFM-Adjacency Send-Readiness graph `wf_0tic9xaFeq2rKvMnKuD` is the current reference; generalize it into a token-parameterized template on first stamp).

## Steps
1. **Registry + credit check first.** Run `clay workflows list` and check the Clay_Build_State_Registry before building anything; prefer extending an existing asset. Estimate credits (clay-credit-steward) before any enrichment.
2. **Assemble the 5 stage prompts.** For each of E1-E5: concatenate [stage header from stage_ladder] + [filled motion slots] + [voice_core]. Swap MOTION_KEY and the Source Motion check. Write them to the motion's build folder as text (version-controlled), so re-paste is copy, not author.
3. **Copy-sharpen.** Run intradiem-copy-sharpener on E1-E5 before anything goes live. Honor motion-specific brand convention (WFM = B; do not let the generic brand-light Days 1-5 rule override a motion that sets B). Verified-claims gate is a hard stop.
4. **Build the workflow via CLI.** Create the send-readiness workflow from the template (`clay workflows create`), then `edit_node` to inject each stage's assembled prompt into its MessageGen agent node and repoint tokens. Re-verify tool-node bindings after creation (the CLI drops explicit input bindings on tool nodes at CREATE time; re-apply via UPDATE). Pass genuinely blank fields as the literal `(none)`, never `""` (agent nodes treat `""` as missing). The graph ends at HOLD; no send node, ever.
5. **Validate.** Run `validate_workflow`; then run ONE real row end to end and confirm it reaches send_ready=HOLD with clean drafts. Never claim BUILT until it runs live.
6. **UI checklist (the must-stay-manual minutes).** Hand back: Duplicate the golden table (structure only), re-point L1/L3 lookups, set Source Motion, and (only if the motion keeps any table AI columns) re-paste their prompts because Duplicate blanks them. Everything else came from the CLI.

## Guardrails (non-negotiable)
- Config over code; dry-run by default; the graph ends at HOLD; never add a send node or flip a send gate.
- Verified-claims gate on every generated line; no invented customer, outcome, or number; industry-level proof only until the verified_proof feed lands.
- Do not run two agent sessions editing the same table/workflow at once (has caused fix reverts).
- Registry is present-tense ground truth; if a plan doc disagrees, the registry wins; stop and reconcile.

## Output
A motion build folder containing: the filled motion_slots, the 5 assembled + sharpened stage prompts, the workflow id once built, and the UI stamp checklist. Plus a one-line registry update proposal (not applied) for Dallas.

## First-run note
The workflow template does not exist as a parameterized artifact yet; the proven WFM graph is the reference. Generalizing it into a token-swappable stamp template is a live Clay operation (read the WFM workflow, extract the node graph, replace motion-specific prompt text with slots). Do that deliberately with Dallas against Clay, not unprompted against his live graph.
## Retired 2026-09-05: Clay-side messaging
Dallas's decision: Clay does not write messaging. Step 4 (MessageGen prompt injection into workflow agent nodes) is retired. A stamped motion builds sources, scoring, signals, the contacts segment, enrichment (email, posts, platforms, persona key) and the gates; copy is written Claude-side per contact by intradiem-first-draft-engine and intradiem-copy-sharpener and loaded to lemlist by the bridge. Do not assemble or paste MessageGen prompts. Reference: motions/shared/Clay_MessageGen_Retirement_Sep5.md.
