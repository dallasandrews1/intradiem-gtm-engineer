# WFM-Adjacency Clone — New-Thread Build Kickoff
Generated 2026-07-17. Paste this whole file into a fresh Cowork thread to run the WFM-Adjacency build with full context.

## What this build is
Stamp **WFM-Adjacency** (`wfm_adjacency`, strike-seq Registry slot 4 / Competitive) as the **first clone off the New-Logo golden**. This build is the proof that the clone loop works end-to-end; every new-logo motion after it is duplicate-and-re-point.

## Read first (canonical, in this order)
- `Clay_Build_State_Registry.md` — **the state source of truth. Registry wins over every plan doc.** Never infer a Clay asset exists from a plan doc or memory; read this, then verify live. Last sweep (Jul 17): CM motion + 7 functions + CM workflow = BUILT; golden + WFM workbook/Claygent/workflow = PLANNED.
- `Clay_Golden_Standard.md` — the engine standard. Read **§1.5 (build labor map: agent vs. human)** and **§16 (universe + wave standard)**.
- `New_Motion_Build_Runbook.md` — governs. If it disagrees with anything here, it wins.
- `Golden_Scaffold_Promotion_RunSheet_CostMandate_v1.md` — the one-time golden promotion (Clay UI).
- `WFM_Adjacency_Clone_Pack_v1.md` — the stamp spec: PART A re-point sheet + PART B workflow build prompt. **NOTE: its PRE-REQ 0 and PRE-REQ 2 are STALE — both are already done (see Current state).**
- `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` — the authored L4 prompt (§2 pastes into MessageGen node, §4 into the critic column).
- Scaffold mechanism: `Clay_Motion_Scaffold_SOP_v1.md` + `Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`.

## Current state (verified 2026-07-17 — do NOT redo these)
- ✅ **fn_persona_key wfm branch** — published live. Routes "Director of Workforce Management" → `wfm`, COO → `coo_finance`. (Clone Pack PRE-REQ 0 is stale; it's resolved.)
- ✅ **WFM MessageGen prompt** — authored: `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` (v1.0, v2.2.3 contract, cloned from Cost-Mandate). (Clone Pack PRE-REQ 2 is stale; it exists.)
- ✅ **fn_send_ready** — confirmed clean live.
- ✅ **Cost-Mandate donor workflow** `wf_0tiane7qgXQ6PH9UdBA` — complete + running end-to-end (proves the donor's logic).
- ⬜ **`__GOLDEN New-Logo Scaffold`** — **PLANNED, not built** per the Build-State Registry (Jul 17 sweep); the WFM workbook and workflow are PLANNED too. So expect STEP 1 to run the full promotion. Still verify live before creating (registry + eyes-on, never a plan doc alone).

## Do, in order — tiered by who can own it (per §1.5 labor map)

**STEP 1 — [Human · Clay UI] Confirm or create the golden.**
Open live Clay. Does `__GOLDEN New-Logo Scaffold` exist and pass its First-Duplicate Verification?
- If **NO** → execute `Golden_Scaffold_Promotion_RunSheet_CostMandate_v1.md` end-to-end: STEP 0 eyes-on donor check → STEP 1 create the workbook → STEP 2 Duplicate L1–L3 in dependency order → STEP 3 neutralize into a reusable golden → STEP 4 First-Duplicate Verification. Structure only; nothing sends, launches, or flips a gate.
- If **YES** → go to STEP 2.

**STEP 2 — [Human · Clay UI] Stamp WFM-Adjacency** (Clone Pack PART A).
`Duplicate table` the golden's L1–L3 into a new **`WFM-Adjacency Motion`** workbook, then re-point ONLY these 5 motion-specific things:
1. `source_motion` → `wfm_adjacency` (set at creation, read-only after).
2. Universe → **fresh signal-first stamp** (recommended over the Cost-Mandate overlay for this first clone — it proves the loop): technographic search (Verint / NICE / Calabrio / Genesys / Amazon Connect) + RTA/intraday job postings.
3. Persona routing (targeting) → entry `wfm` → routed up to `cc_ops`, `coo_finance`. Do NOT narrow the node-2 gate rubric; that stays the full 6-key set.
4. L4 MessageGen node → paste §2 of `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md`; paste §4 critic into the Draft Audit column.
5. Number rule → unchanged from Cost-Mandate.
Then re-point Lookups to the shared reference + L5–L8 tables (**the #1 silent breakage**), run the abbreviated First-Duplicate Verification, confirm **sender webhook OFF**.

**STEP 3 — [Local Claude Code · workspace 1180800] Build the workflow** (Clone Pack PART B).
Clay CLI OAuth (`clay login`) can't complete in a cloud session — **run local.** Paste Clone Pack PART B verbatim: builds **"WFM-Adjacency Send-Readiness (Alpha)"**, the 9-node fail-closed graph, structural reference = `CostMandate_Workflow_Alpha_Blueprint_v1.md`. No send/sync/launch node — the contract ends at `send_ready`.

**STEP 4 — [Verify] Test fixtures before any real row.**
- KNOWN-GOOD: a `wfm` contact at a net-new Verint/NICE/Calabrio account, qualitative (no disclosed figure). Assert → reaches node 9 with `send_ready=HOLD`.
- KNOWN-BAD: a fabricated competitor result, or a number with a blank `signal_source_url`. Assert → EXITs at node 8 with `msg1_critic=FAIL`. **If it passes, STOP** — the critic needs tightening, do not proceed.

**STEP 5 — [Gated] After green.**
Run on a 10-row hardened slice (all end `send_ready=HOLD`; drafts read send-ready to a real WFM/Ops buyer). Credit estimate + ledger row before any technographic enrichment (~150–300 credits first wave; sample 10 rows first per `clay-credit-steward`). The real signal-first universe wave is a **separate credit GO** — do not source it without explicit approval.

## Standing guardrails
Dry-run law (sender OFF, no send node anywhere). Files-first, config-over-code. Verified-claims gate: the only allowed Intradiem proof is the Humana verified set (occupancy +4% / AHT −45s / 2 hrs per agent per month), **HEALTHCARE rows only** — every other vertical runs qualitative (the biggest live limit vs. Cost-Mandate). DO-NOT-SEND: any competitor's named result, any WFM-replaced framing, idle-% stats, Intradiem NRR/ROI, any non-Humana customer outcome. Source once / process in waves. Human before send. The moment a wave launches, schedule its next-wave check.
