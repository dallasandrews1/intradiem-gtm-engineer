# Cost-Mandate Workflow — Node 6 Unblock (v1, 2026-07-17)

**Status:** Workflow `wf_0tiane7qgXQ6PH9UdBA` is one node from a valid end-to-end run. Nodes 1–5 now pass a real row cleanly (two bugs fixed this session). **Node 6 (MessageGen agent node) is the only blocker**, and it needs *your hands in the Clay UI* — no API/CLI path can fix it.

---

## The honest framing (these are not two equal options)

- **Manual pin-bind in the Clay UI = the unblock.** It is the *only* thing that gets node 6 → node 8 → a real critic verdict. ~2–5 minutes.
- **Filing a Clay bug report = optional and parallel.** It does NOT unblock you. It just helps Clay fix their `edit_node` API so a *future* agent build doesn't hit this. File it or don't — the workflow gets to green either way, via the UI.

So: do the UI pin-bind regardless. File the bug only if you want the API fixed for next time (I won't file it unless you say go).

## What's actually broken (one sentence)

Clay decides an **agent node's** required inputs by reading the `{{token}}` placeholders out of the prompt *text*, and expects each token to be explicitly bound to a source. The `edit_node` tool silently drops those bindings on save for agent nodes specifically (every code/tool/conditional node in this same workflow accepted them fine — 5 attempts confirmed the pattern). The UI's own input-mapping panel is a different code path and should bind where the API won't.

---

## The 2-minute UI fix

1. Open workflow **`wf_0tiane7qgXQ6PH9UdBA`** ("Cost-Mandate Send-Readiness (Alpha)") in the Clay UI → open **node 6 (MessageGen Email 1)**.
2. Find its **input mapping / variables panel** (where each `{{token}}` in the prompt is listed with a source dropdown). Clay populates this list from the prompt text, so every token the prompt uses will be there — that's your checklist.
3. **Bind every token to its source:**
   - Every contact field token (`first_name`, `job_title`, `company`, `disclosed_figure`, `signal_evidence`, `vertical`, `product_angle`, etc.) → the matching **trigger input** field.
   - `number_allowed` → **node 4's output** (the H1 gate), not the trigger.
   - Leave nothing on the default/unbound state — an unbound token is what makes the node report "missing inputs" and refuse to run.
4. **Save.** Then reopen node 6 and confirm the bindings persisted (the API silently reverted; verify the UI didn't). If any token snapped back to unbound, rebind and save again.

## Verify it's green (re-run the same 2 records)

Run the Acrisure real record and the known-bad record from `CostMandate_Workflow_AcceptanceTest_Prompt_v1.md` through `clay workflows runs test wf_0tiane7qgXQ6PH9UdBA` again, and check:

- **Node 6 executes** (produces `draft_subject` + `draft_body`) — no "missing inputs."
- **Acrisure:** reaches **node 8 with a real `msg1_critic_status`** (PASS, or a reasoned FAIL — reasoning text present, NOT "Some inputs missing"), then **node 9 `send_ready = HOLD`**.
- **Known-bad:** exits at **node 8 with FAIL** (sourceless fabricated number caught). If it passes, stop — tighten `fn_draft_critic` §4.
- No send/sync node ran. Dry-run law intact.

If all four hold, the workflow is **GREEN** and the acceptance test is finally valid — then the golden-scaffold promotion and clone-per-motion steps open up.

---

## Optional: Clay bug report (drafted, not filed)

If you say go, I'll file this via `clay feedback`:

> **Bug: `edit_node` silently drops input pins on agent nodes (Workflows Alpha).**
> Workspace 1180800, workflow `wf_0tiane7qgXQ6PH9UdBA`, node 6 (agent/MessageGen). Setting explicit input bindings (sourceNodeId/sourcePath) via `edit_node` does not persist for **agent** nodes — bindings silently revert to unbound / bare `{"type":"string"}` on save, so the node reports missing inputs and won't run. Reproduced 5 ways: full pins + `required:[]`; pins with `required` omitted; `inputSchema:{}`; delete+recreate with `automapInputs:true`; fresh node with explicit pins + `automapInputs:false`. Code/tool/conditional nodes in the *same* workflow accept pins via `edit_node` normally — the defect is specific to agent nodes. Clay derives an agent node's required inputs from `{{token}}` placeholders in the prompt text, so unbound tokens hard-block the node. Requested fix: honor sourceNodeId/sourcePath pins passed to `edit_node` for agent nodes (or expose the same binding the UI panel writes).
