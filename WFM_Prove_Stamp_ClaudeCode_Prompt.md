GOAL: Prove the finished `Golden New-Logo Scaffold` by stamping the FIRST motion off it — WFM-Adjacency — end-to-end, ending at send_ready = HOLD on a hardened test slice. Nothing sends. This is the proof the stamp system works; after it, every new-logo motion is the same loop.

You are running in my LOCAL Claude Code (Clay CLI is OAuth-authenticated here; the cloud Cowork session cannot authenticate, which is why this step is local). The project repo is your working directory — read the referenced files directly.

═══════════════════════════════════════════
GROUND TRUTH — verified live in Clay on 2026-07-17 (workspace 1180800). Re-verify before acting; if live disagrees, stop and tell me.
═══════════════════════════════════════════
The golden is BUILT and neutralized. Do NOT rebuild it.
- Workbook `Golden New-Logo Scaffold` = wb_0tib7v5msZ2qYbGc4AC. Tables: L1 Accounts/Universe = t_0tib7x9pjMe9Givg4Dm (firmographic structure, 0 rows, no bound universe source); L3 = t_0tib7yp7mNKKYX4imrW (50 cols, 0 rows, carries the full send-readiness column pipeline).
- L3 `Universe Lookup` correctly resolves to the golden's OWN L1 (not Cost-Mandate's).
- `Source Motion` = `<<motion>>` (neutralized). `MessageGen Email 1` renamed (CM tag dropped).
- All 7 shared Functions live: fn_eligible, fn_persona_key (wfm branch published), fn_email_verified, fn_tokens_ready, fn_draft_clean, fn_draft_critic (t_0tiabaamPvDuEyTxSaF), fn_send_ready.
- Cost-Mandate donor workflow proven live: wf_0tiane7qgXQ6PH9UdBA (9-node, ends HOLD).

⚠️ CRITICAL FINDING that rewrites the stamp process — Clay "Duplicate table" does NOT carry over "Write with AI" column prompts. On the golden, all 3 AI columns (MessageGen = Sonnet, Draft Audit = GPT-4o, Email Voice Audit) came through with EMPTY prompt boxes; only model + structure survived. Therefore EVERY stamp must re-populate ALL THREE AI columns — not just MessageGen + Draft Audit. If Email Voice Audit is left blank, the motion ships with no voice gate (the exact "sounds like AI" failure Tom/CMO flagged) AND no figure-integrity critic. This corrects `WFM_Adjacency_Clone_Pack_v1.md`, which only lists two.

═══════════════════════════════════════════
CAPABILITY BOUNDARY — do not fight these
═══════════════════════════════════════════
- Table/workbook STRUCTURE (duplicate table, add columns): UI-only. No create-table/duplicate on the Clay CLI or MCP as of Jul 17. FIRST thing: run `clay --help` and `clay tables --help` to check if a duplicate/create command shipped since. If yes, use it and note it. If no, the table duplicate is my manual UI action — you generate the exact click-list and verify the result via CLI/MCP after.
- Workflow logic (Alpha graph): YOURS to build via `clay workflows create`.
- AI-column prompts + Functions: UI paste/edit only (I do it; you give exact text + verify).
- Enrichment/data: CLI or Clay MCP.
Tag every step [UI = me] / [CLI = you] / [VERIFY = you].

═══════════════════════════════════════════
READ THESE FIRST (repo root)
═══════════════════════════════════════════
1. WFM_Adjacency_Clone_Pack_v1.md — Part A (5 re-points) + Part B (workflow build prompt). NOTE: its AI-column list is incomplete — see the finding above; treat as 3 AI columns.
2. WFM_Adjacency_Clone_Pack_v1_CORRECTION.md — the all-3-AI-columns correction + save-as-Claygent guidance (authored today).
3. Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md — §2 MessageGen body, §4 Draft-Audit critic.
4. CostMandate_Workflow_Node6_Unblock_v1.md — the agent-node pin gotcha.
5. Clay_Golden_Scaffold_Neutralize_Repoint_Checklist_LIVE_v1.md — the golden's live column map (reference).
6. Clay_Build_State_Registry.md — present-tense ground truth; reconcile against live and UPDATE it when done.

═══════════════════════════════════════════
STEP 1 — Stamp the WFM table  [UI = me, VERIFY = you]
═══════════════════════════════════════════
a. Duplicate the golden's L1 + L3 into a new workbook `WFM-Adjacency Motion` (UI: table title → Duplicate table → Move into new workbook). Confirm 0 rows carried (structure only).
b. Re-point the 5 motion-specific things (Clone Pack Part A):
   1. `Universe Lookup` (L3) → the WFM copy's OWN L1 (NOT the golden's, NOT CM's). ⚠️ This is the recurring silent breakage — verify the referenced workbook id equals the new WFM workbook, not wb_0tib7v5msZ2qYbGc4AC.
   2. `Source Motion` → `wfm_adjacency`.
   3. Universe source on L1 → the WFM universe (WFM/RTA/intraday signal source: Verint/NICE/Calabrio/Genesys/Amazon Connect technographic).
   4. Number rule → WFM H1 gate (prospect's own occupancy/shrinkage/SL/AHT/backlog/headcount only; Humana proof HEALTHCARE rows only; every non-healthcare row qualitative).
   5. persona routing → verify `fn_persona_key` returns `wfm` for a WFM title (already published).
c. Re-populate ALL 3 AI columns (the finding): 
   - `MessageGen Email 1` ← paste Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md §2; rename to `(WFM-Adjacency)`.
   - `Draft Audit` ← paste §4 critic (adds WFM-specific FAILs).
   - `Email Voice Audit` ← re-apply the universal voice-audit prompt/Claygent (do NOT leave blank).
VERIFY: query the WFM L3 via Clay MCP/CLI; confirm columns exist, Universe Lookup target = WFM's own L1, Source Motion = wfm_adjacency.

═══════════════════════════════════════════
STEP 2 — Build the WFM Send-Readiness workflow  [CLI = you]
═══════════════════════════════════════════
From WFM_Adjacency_Clone_Pack_v1.md Part B, fill the 5 blanks and `clay workflows create` a 9-node fail-closed graph calling the 7 fn_*, ending HOLD, NO send node — the CM donor (wf_0tiane7qgXQ6PH9UdBA) is your reference shape. Confirm it validates (no dangling inputRefs).

═══════════════════════════════════════════
STEP 3 — Node-6 agent-pin gotcha  [UI = me]
═══════════════════════════════════════════
The agent node's input pins won't persist via API/CLI (revert on edit). Per CostMandate_Workflow_Node6_Unblock_v1.md, hand me the exact tokens to pin-bind + the required-array to clear in the Clay UI. Budget 15 min; don't retry the CLI more than twice.

═══════════════════════════════════════════
STEP 4 — Acceptance test  [CLI = you]
═══════════════════════════════════════════
Load a hardened 10-row WFM slice and run the pipeline. PASS = every row ends `send_ready = HOLD`. No real sends. Report the per-row gate that held each one.

═══════════════════════════════════════════
RULES OF THE ROAD
═══════════════════════════════════════════
- Dry-run law: nothing sends/launches/flips a gate. Workflow ends HOLD, no send node. Test slices only.
- NEVER restore a Clay snapshot (re-IDs nodes, breaks inputRefs — burned before). Fix-forward on the live graph only.
- Verified-claims: WFM proof is Humana-only + HEALTHCARE-only → non-healthcare rows qualitative; no competitor-named results (Verint/NICE/Calabrio/Genesys/Amazon Connect); no Intradiem ROI/NRR.
- Credits: STEP 4 is the only credit spend — estimate before running; 10 rows only.
- When done: update Clay_Build_State_Registry.md (WFM table + workflow → BUILT) and add a Mem0 memory (user_id=dallasandrews, app_id=coordinator, infer=false) recording the stamp result + whether `clay tables` gained a duplicate/create command.
- For any [UI = me] step: give me the exact click path + exact text to paste, then verify live before continuing. Don't call anything done until the page/CLI confirms it.

START by running `clay --help` / `clay tables --help` (capability check), then reading the 6 files, then walk me through Step 1a.
