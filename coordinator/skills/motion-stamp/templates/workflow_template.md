# Workflow Template (parameterized from the proven WFM graph)

Source of truth: `wf_0tic9xaFeq2rKvMnKuD` (WFM-Adjacency Send-Readiness Alpha, 24 nodes, validated clean, proven end-to-end to HOLD). This template captures its topology and marks the ONLY per-motion injection points, so `motion-stamp` step 4 can rebuild it for a new motion via `clay workflows create` + `edit_node`.

## The whole per-motion surface is tiny
Everything below is REUSED unchanged except three injection points. The 7 Functions are workspace-shared (referenced by tableId, never duplicated); the gates, exits, and terminal are generic code; the Voice Audit is motion-invariant.

### Injection points (the only things a stamp changes)
1. **MessageGen agent prompt** (node 6). Replace with the assembled stage prompt = [voice_core] + [filled motion_slots] + [stage_ladder header]. For the E1-only engine this is one node; for the full 5-touch see the expansion below.
2. **`source_motion` literal check** inside the MessageGen prompt: `"<MOTION_KEY>"` (e.g. `wfm_adjacency`).
3. **Persona in_icp gate set** (node 2g): which `fn_persona_key` return values count as in-ICP for this motion (WFM = wfm, cc_ops, coo_finance). `fn_persona_key` itself is shared; only the gate's accept-set is motion config.

### Optional tokens (surface, default to WFM values)
- H1 source-gate freshness window (node 4): 90 days, a numeric constant, expose as a token if a motion needs a different staleness bar.
- Node 8b `Record` key `"Cost Signal Research (AI)"`: a carryover column-name artifact from an earlier motion. VERIFY it matches what the shared `fn_draft_critic` formula actually reads before stamping; likely should be a generic signal key, not a Cost-Mandate-era name.

## Invariant skeleton (reuse verbatim)
```
Trigger (manual; supplies row fields)
  -> 1. Eligibility kill switch        [tool: fn_eligible  t_0tial9rYKzWKU2y9MTC]
  -> 1g gate: eligible? --false--> EXIT: EXCLUDED
  -> 2. Persona routing                [tool: fn_persona_key  t_0tiahksb4jmyFfMSQYd]
  -> 2g gate: persona in <MOTION in_icp set>? --no--> EXIT: HOLD_persona
  -> 2b. Compose full_name             [code, generic]
  -> 3. Email verify                   [tool: fn_email_verified  t_0tiajxdwq8Z4zM6hwXw]
  -> 3g gate: Status==valid? --no--> EXIT: HOLD_no_email
  -> 4. H1 source gate                 [code; sets number_allowed = URL present AND date within <window>d]
  -> 5. Tokens ready                   [tool: fn_tokens_ready  t_0tiako9CBV2yiGnA5r7]
  -> 5g gate: tokens_ready? --no--> EXIT: HOLD_incomplete
  -> 6. MessageGen  <<INJECTION 1 + 2>>  [agent, claude-sonnet-5, inline prompt]
       -> Voice Audit                  [agent, MOTION-INVARIANT, cadence STACKED/CHOPPED critic]
       -> 7. Malformed guard           [tool: fn_draft_clean  t_0tial35xhuRurytCduv]
  -> 7g gate: draft_clean? --no--> EXIT: HOLD_malformed
  -> 8b. Compose Record for critic     [code; see node-8b token caveat]
  -> 8. Figure-integrity critic        [tool: fn_draft_critic  t_0tiabaamPvDuEyTxSaF]
  -> 9. Send-ready gate                [tool: fn_send_ready  t_0tiahe2mzsH9CCaC4Sx]
  (Voice Audit) + (9. Send-ready) -> 10. Voice-gated send-ready  [code; final = READY iff send_ready==READY AND voice==PASS, else HOLD]
```
No send node. Five dead-end HOLD/EXCLUDED exits plus the final HOLD/READY status node. Nothing writes to a CRM or fires a send. Never add a send node.

## 5-touch expansion (decision required before building)
The proven graph generates EMAIL 1 only (one MessageGen node). For the 5-touch, the send-generation options are:
- **(A) One graph, five MessageGen sub-chains.** Duplicate the node-6-through-critic sub-chain five times (E1-E5), each with its stage prompt, all reusing the same shared functions and voice audit, converging on a per-stage HOLD/READY. All 5 drafts generated up front at qualification, staged for the sequencer to thread. Fully CLI-reproducible. Heaviest graph.
- **(B) E1 in the workflow, E2-E5 elsewhere.** Keep this graph as the E1 send-readiness engine; generate E2-E5 as separate stage columns/workflow. Smaller graph, but splits the generation surface.
- **(C) One parameterized stage-runner.** A single MessageGen node whose stage header is a trigger input; run the graph five times (once per stage). Smallest template, but each stage is a separate run.
RECOMMENDATION: **(A)** for the self-serve goal — one stamp yields the whole 5-touch, all gated, all reproducible. Confirm with Dallas before building.

## Build sequence (motion-stamp step 4 executes)
1. `clay workflows create` from this skeleton (or clone `wf_0tic9xaFeq2rKvMnKuD` if Clay supports workflow clone).
2. `edit_node` node 6 (and E2-E5 nodes under option A): inject the assembled stage prompt; set the `source_motion` literal; blanks as literal `(none)`, never `""`.
3. `edit_node` node 2g: set the persona in_icp accept-set for the motion.
4. **Re-verify tool-node input bindings after create** — the CLI drops explicit tool-node bindings at CREATE time; re-apply via UPDATE (known bug from the WFM build).
5. `validate_workflow`, then run ONE real row to HOLD before declaring BUILT.

## Open decisions surfaced by the graph read (2026-07-18)
- Voice Audit is named per-motion but its prompt is fully motion-invariant. Decide: clone per motion (current) vs one shared Voice Audit Claygent across motions.
- Node 8b's `"Cost Signal Research (AI)"` key looks like a Cost-Mandate carryover; verify against `fn_draft_critic`'s formula before reuse.
- 5-touch expansion option A/B/C (recommend A).
