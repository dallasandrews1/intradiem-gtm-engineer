---
name: clay-motion-selfserve-path
description: How to make a new Clay motion fast (minutes not a week) despite Clay's UI-only walls; motion-stamp direction.
metadata:
  type: project
  date: 2026-07-18
---

Goal (Dallas, 2026-07-18): a new motion should be self-serve, so someone launching one doesn't wait a week for Dallas to hand-tinker.

**Hard wall (state honestly):** Clay CANNOT auto-inject an AI/MessageGen column into a table on creation. No trigger, template, or API does this. AI columns, table structure, and Functions are all UI-only constructs (same wall as chip-binding). "New table auto-grows MessageGen columns" is not achievable.

**What IS agent-buildable:** Workflow logic via the Clay CLI (`clay workflows create` + `edit_node`) — proven by the 22-node WFM workflow. AI agent NODES inside a workflow are scriptable even though AI COLUMNS are not. Enrichment/data ops too. Functions are workspace-SHARED, so new motions reuse the 7 functions, never rebuild them.

**The three levers to hit the goal:**
1. Columns travel by golden **Duplicate**, not injection. Build the full column set once into the golden; every motion is a UI-Duplicate. Stamp = duplicate, re-point L1/L3 lookups, set Source Motion, re-paste AI prompts (Duplicate blanks them, the recurring tax).
2. Move generation+gating into the **workflow** (CLI-reproducible) so a stamp script rebuilds it per motion from a template; the table drops to a thin data layer. This is the real self-serve path.
3. Canonical **prompt library** as version-controlled text files (WFM_Email2to5_Stage_Prompt_Build_Sheet.md is the first entry) so re-paste is copy, not author. The week was spent authoring/binding prompts, not clicking.

**Proposed build:** a `motion-stamp` skill — input a motion name + ICP, it generates the motion-specific prompt set from the library, builds the send-readiness workflow via CLI from the proven template, and returns the short UI checklist for the must-stay-manual steps. Extends the existing [[clay-motion-factory-scaffold-system]]; does not replace it. Honest floor: a couple of UI minutes per motion (structure is UI-only), but a checklist, not tinkering.

**DECISION RESOLVED (Dallas, 2026-07-18): WORKFLOW path.** Generation + gating standardize on the CLI-buildable workflow; table stays a thin data layer.

**BUILT 2026-07-18:** the `motion-stamp` skill (`~/.claude/skills/motion-stamp/`, mirrored to coordinator) with a canonical prompt library split motion-invariant vs motion-specific:
- `templates/voice_core.md` — motion-invariant voice/format/number-gate/proof/output block (extracted from the proven WFM Email 1 prompt), pasted verbatim into every motion.
- `templates/stage_ladder.md` — motion-invariant 5-touch escalation (E1 cold → E2 soft new-facet → E3 value/proof → E4 direct-with-deliverable → E5 confident close), cadence, thread/brand/sign-off rules.
- `templates/motion_slots.md` — the per-motion fill-in (core position, one idea, personas, signal semantics, bans, brand convention A/B, sender, E1 gold standard).
- `SKILL.md` — orchestration: registry+credit check → assemble 5 stage prompts → copy-sharpen → build workflow via `clay workflows create`+`edit_node` (re-verify tool-node bindings, blanks as `(none)`, ends at HOLD) → validate on one live row → UI checklist for the must-stay-manual minutes (duplicate golden, re-point lookups).

**Prompt layer PROVEN against WFM (2026-07-18):** filled `motions/wfm_adjacency/motion_slots.md` + assembled = reproduces the live Email 1. One gap found (the OPENER discipline) and patched into voice_core. Fidelity map: `motions/wfm_adjacency/fidelity_check.md`. PASS.

**Workflow template AUTHORED (2026-07-18):** `templates/workflow_template.md`. Read the proven WFM graph `wf_0tic9xaFeq2rKvMnKuD` via clay-operator (read-only, 24 nodes). KEY FINDING: the ONLY per-motion surface is node 6 (MessageGen inline prompt) + the `source_motion` literal + node 2g's persona in_icp accept-set. The 7 functions are workspace-shared (by tableId), gates/exits/terminal are generic, Voice Audit is motion-invariant. Template marks those 3 injection points; everything else reused.

**DECISIONS LOCKED (Dallas delegated "whatever you recommend", 2026-07-18):**
1. 5-touch expansion = **A** (one graph, 5 MessageGen sub-chains, all gated, generated up front, staged for the sequencer to thread).
2. Voice Audit = **shared** Claygent across motions (prompt is motion-invariant). Caveat: if Clay can't reference one shared Voice Audit agent across separate workflows, fall back to clone-per-motion; the content is identical either way.
3. Node 8b `"Cost Signal Research (AI)"` key = **verification in flight** (clay-operator reading fn_draft_critic t_0tiabaamPvDuEyTxSaF vs node 8b). If it's a stale Cost-Mandate key, it's a live bug on the WFM critic gating the 6 send-ready contacts, fix before trusting send-ready.

**FACTORY STATUS: proving live.** Prompt layer proven, workflow template authored, decisions locked.

**FIRST FACTORY BUILD, LIVE (2026-07-18):** WFM 5-touch (option A) being built live in Clay = `wf_0tie30io3hiPqSzVRU2` "WFM-Adjacency 5-Touch Send-Readiness (Alpha)", workspace 1180800. **STAGE 1 DONE + validate clean:** qualification chain (eligible→persona[in_icp wfm/cc_ops/coo_finance]→email→H1→tokens + gates + 5 HOLD/EXIT exits) + Email-1 sub-chain (MessageGen E1 [live prompt verbatim] → draft_clean → compose Record → critic → send_ready → Voice Audit E1 → HOLD_E1_send_ready), 25 nodes, 7 shared functions reused by tableId, NO send node. Learned: there is NO `clay workflows` clone command, so a 5-touch = rebuild proven graph + 4 more sub-chains node-by-node.
**WFM 5-TOUCH COMPLETE (2026-07-18):** all 5 stages built live, **57 nodes, validate clean, no send node, every path ends at HOLD.** Qualification runs once; all 5 MessageGen agents fan out from node 6a; each stage = MessageGen Ei → malformed guard → (shared HOLD_malformed exit) → compose Record → critic → send_ready → Voice Audit Ei → HOLD_E<i>_send_ready. E2-E5 = E1 body with only stage header + sharpened gold standard swapped, rest byte-identical. Claude audited Stage 1 topology/safety/fidelity before continuing. **OWED: one live test row end-to-end before any real wave** (structure audited, runtime not yet run).
This PROVES the factory pattern end-to-end in Clay. A new motion (incl. the Stars upgrade) is now a STAMP of this skeleton with the motion's own prompts + slots, not from scratch. Shared across motions: the 7 functions, the reply-triage workflow, the (pending) fn_draft_critic motion-aware fix.
Also live: reply-triage workflow `wf_0tie1gcUJnvVoAXhN8V` (built + validated, pending reply_body sync). See [[orchestrator-not-manual-directive]], [[star-ratings-upgrade-backlog]].
