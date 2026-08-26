---
name: stars-5touch-concurrency-fix-jul20
description: "The Stars 5-Touch workflow's parallel AI fan-out caused a nondeterministic async-callback race; fix is touch serialization. WFM-Adjacency 5-Touch has the identical bug."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T03:49:17.446Z
---

Jul 20 2026: The Star Ratings 5-Touch Send-Readiness workflow (`wf_0tiegzuo3PzJ4UtUGFA`, workspace 1180800) failed reliably under a nondeterministic concurrency race. Root cause: node `5a. Compose MessageGen E1 inputs` (`wfn_0tiehcioJrFRnJc9Riq`) fanned out in PARALLEL to all five MessageGen agents (E1-E5), so 5 async AI actions (and downstream, 5 critics + 5 voice audits, up to ~10 concurrent) fired at once and the platform mangled the AI-action callbacks ("Invalid returnData shape in AI action task callback"). Two headless `clay workflows runs test --input` runs failed on COMPLETELY DIFFERENT node sets (run 1 killed MessageGens; run 2 killed critics/voice audits), proving a real timing race, not a test-mode artifact. This is the same defect Dallas observed on real runs ("all 5 concurrent fn_draft_critic nodes failed", "send data back not sending").

Fix (workflow-scoped, zero blast radius to shared functions): SERIALIZE the touches. Repoint MessageGen E2/E3/E4/E5 incoming edges from `5a` to the prior touch's HOLD terminal (HOLD_E1→E2, etc.), and because `{{variable}}` filling only works node-to-immediate-successor, convert each of those 4 MessageGen nodes to `automapInputs: false` with all 10 tokens PINNED to `5a` via `sourceNodeId`+`sourcePath`. Node IDs: E2 `wfn_0tiehwcEeQthi2Yt2yy`←HOLD_E1 `wfn_0tiehh5YoPiNrbjsA8R`; E3 `wfn_0tiei0jyJuTqKPtrjzT`←HOLD_E2 `wfn_0tiehyfGUX3XFgu8Tsn`; E4 `wfn_0tiei41w6ds8kKjs74S`←HOLD_E3 `wfn_0tiei244AkQdRr2vRT8`; E5 `wfn_0tiei7eTKfUdXe76BVJ`←HOLD_E4 `wfn_0tiei5m7TUKiExtEneb`. Rollback snapshot: `wfs_0tigdp5Q2E6xGub84JG`.

OPEN BLAST-RADIUS ITEM: WFM-Adjacency 5-Touch (`wf_0tie30io3hiPqSzVRU2`) has the IDENTICAL parallel fan-out and the identical race. It needs the same serialization before it is trusted. See [[fn-draft-critic-shared-function]].

The shared functions themselves (fn_draft_critic `t_0tiabaamPvDuEyTxSaF`, fn_send_ready `t_0tiahe2mzsH9CCaC4Sx`) were NOT edited; their send-data-back has no per-call completion guard, which is the deeper latent fragility, but serialization removes the concurrency that triggers it.
