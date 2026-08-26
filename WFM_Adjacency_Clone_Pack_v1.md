# WFM-Adjacency — Clone Pack v1 (first stamp off the New-Logo golden)
**Companion to `Clay_Motion_Scaffold_SOP_v1.md`, `Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`, `Motion_Roadmap_Next3_2026-07-15.md`. This is everything you need to stamp WFM-Adjacency from `__GOLDEN New-Logo Scaffold` once the golden exists.**

Generated 2026-07-17. Motion key: `wfm_adjacency`. Populates strike-seq Registry slot 4 (Competitive).

---

## ⛔ PRE-REQ 0 — Fix `fn_persona_key` first (confirmed blocker, live-verified)
Ran `fn_persona_key` from here (2026-07-17, Clay MCP) against WFM-Adjacency's primary titles. **All routed to `out_of_icp`:**

| Job Title | Returned | Should be |
|---|---|---|
| Director of Workforce Management | `out_of_icp` ❌ | `wfm` |
| Manager, Real-Time Analytics & Intraday | `out_of_icp` ❌ | `wfm` |
| VP Capacity Planning | `out_of_icp` ❌ | `wfm` |
| Chief Operating Officer | `coo_finance` ✓ | `coo_finance` |

WFM-Adjacency's ENTRY persona is `wfm`. With no `wfm` branch, node 2 (persona routing) exits every primary contact as `HOLD_persona` and the motion drafts nobody. **This must be fixed before the clone routes anyone.**

**Fix (Clay UI only — Functions are not CLI/MCP-writable):** open `fn_persona_key`, add a `wfm` branch that maps these title patterns → `wfm`: Workforce Management, WFM, Capacity Planning, Intraday, Real-Time Analyst/Analytics, RTA, Resource Planning, Forecasting & Scheduling. Then re-run the 4 titles above and confirm the three WFM titles now return `wfm` and COO still returns `coo_finance`. (Same class of fix as the earlier `cc_ops` branch add.)

---

## PRE-REQ 1 — `fn_send_ready` — already confirmed clean
Verified live 2026-07-17: it ANDs Msg1 Critic Status, Human Approved, Bdr Claimed, Customer Exclude, Draft Clean, Email Status. No action.

## PRE-REQ 2 — MessageGen prompt must be authored (content dependency)
There is no `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` yet. The clone's node 6 needs it. Author it from the v2.2.3 contract (adapt `Clay_MessageGen_SystemPrompt_CostMandate_v1.md`) with:
- **Core angle:** idle-time execution layer *on top of* WFM — never rip-and-replace. WFM plans the day; it does nothing in the idle gaps between scheduled activities and stops at the contact center while the back office runs uncovered.
- **Allowed proof (VERIFIED only):** Humana occupancy +4%, AHT −45s, 2 hrs capacity/agent/month; idle-time-gap positioning.
- **DO-NOT-SEND:** any competitor's named results; any claim that frames WFM as replaced; idle-% stats; Intradiem NRR/ROI; any non-Humana customer outcome.
- Brand-light, block-on-empty numbers, v2.2.3 contract.

(This is a standalone writing job that should run through the first-draft-engine → copy-sharpener → verified-metrics gate. Flag to build next; the workflow prompt below references it by filename.)

---

## PART A — Scaffold re-point sheet (the 5 motion-specific things)
After `Duplicate table`-ing the golden's L1–L3 into a new **`WFM-Adjacency Motion`** workbook, re-point ONLY these:

1. **`source_motion` tag** → `wfm_adjacency` (set at creation, read-only after).
2. **Universe source** → signal-first: Clay technographic search (Verint / NICE / Calabrio / Genesys / Amazon Connect) + RTA/intraday job postings. Overlaps Cost-Mandate accounts.
   - *Decision to make:* stamp a fresh `WFM-Adjacency Motion` workbook (clean, structure-law-compliant, proves the clone pattern) **[recommended]**, OR run as a signal-overlay segment on the Cost-Mandate table (roadmap's credit-saving option since contacts overlap). Recommend the fresh stamp this first time — the whole point of this exercise is to prove the clone loop end-to-end; save the overlay optimization for later.
3. **Persona routing (motion targeting)** → entry `wfm`, routed up to `cc_ops`, `coo_finance`. (This is the motion-label targeting layer. The node-2 gate `{{PERSONA_KEYS}}` below stays the FULL rubric — do not narrow it.)
4. **MessageGen prompt (L4 node)** → paste `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` (PRE-REQ 2) once authored.
5. **Number rule** → identical to Cost-Mandate (see `{{NUMBER_RULE}}` below) — so node 4 carries over unchanged.

Then: re-point Lookups to the shared reference + L5–L8 tables (the #1 silent breakage), run the abbreviated First-Duplicate Verification, confirm sender webhook OFF.

---

## PART B — Filled workflow build prompt (paste into LOCAL Claude Code)
The 5 blanks, filled for WFM-Adjacency:

| Placeholder | Value |
|---|---|
| `{{MOTION_NAME}}` | WFM-Adjacency |
| `{{MOTION_KEY}}` | `wfm_adjacency` |
| `{{PERSONA_KEYS}}` | `coo_finance, cc_ops, bo_claims, bo_shared, wfm, cx` (FULL canonical rubric — constant across motions; exits only truly out-of-ICP titles) |
| `{{MSGGEN_FILE}}` | `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` |
| `{{NUMBER_RULE}}` | `number_allowed = TRUE only if a prospect-disclosed figure has signal_source_url non-empty AND signal_source_date within 90 days of today. Intradiem proof numbers are permitted ONLY from the Value Repository VERIFIED set (Humana occupancy/AHT/2-hrs-per-agent). NEVER a competitor's named result.` |

**Run location (not optional):** the Clay CLI authenticates via `clay login` (browser OAuth), which a cloud session can't complete. Run this in your **LOCAL Claude Code** with the Clay agent-plugin signed into workspace **1180800**.

---

### THE PROMPT — paste verbatim into local Claude Code

> You have the Clay agent-plugin installed and authenticated to workspace 1180800. Build a Clay Workflow (Alpha) named **"WFM-Adjacency Send-Readiness (Alpha)"**. Use the Cost-Mandate blueprint (`CostMandate_Workflow_Alpha_Blueprint_v1.md`) as the structural reference — same 9-node fail-closed graph, this motion's specifics swapped in.
>
> Steps:
> 1. Run `clay workflows create --name "WFM-Adjacency Send-Readiness (Alpha)"`.
> 2. **Read the created workflow graph first** to learn the live node schema. Clay has not published the Workflows-Alpha node syntax, so do not hand-author JSON blind — edit nodes against the schema you actually see.
> 3. Add nodes 1–9 in this exact order, mapping each Function node to the published Function by name:
>    1. **Eligibility kill switch** → `fn_eligible` (company_domain, customer_flag). If `eligible==false`: EXIT `status=EXCLUDED` carrying `exclusion_reason`.
>    2. **Persona routing** → `fn_persona_key` (job_title). EXIT `status=HOLD_persona` unless `persona_key` ∈ {`coo_finance, cc_ops, bo_claims, bo_shared, wfm, cx`} — the full 6-key rubric, so it exits only truly out-of-ICP titles and is robust to the live fallback value (`review`). Use set-membership, not equality on a fallback value. Do NOT narrow this to the motion's target personas; that targeting happens in node 6 and in sourcing. NOTE: this depends on `fn_persona_key` having a live `wfm` branch — confirm it returns `wfm` for "Director of Workforce Management" before trusting node 2.
>    3. **Email verify** → `fn_email_verified` (first_name, last_name, company_domain). If `email_status != "valid"`: EXIT `status=HOLD_no_email`.
>    4. **Number-source gate** → CODE node (workflow-owned). Compute `number_allowed = TRUE only if a prospect-disclosed figure has signal_source_url non-empty AND signal_source_date within 90 days of today; Intradiem proof numbers permitted ONLY from the Value Repository VERIFIED set (Humana occupancy/AHT/2-hrs-per-agent); NEVER a competitor's named result.` Never exits; sets the flag MessageGen obeys. (Reuse the Cost-Mandate node-4 pure-integer Julian-day date math — zero stdlib imports — so it doesn't hit the deployed-runtime `ModuleNotFoundError: datetime`.)
>    5. **Tokens ready** → `fn_tokens_ready` (first_name, job_title, company, persona_key, email_status, source_motion). If `tokens_ready==false`: EXIT `status=HOLD_incomplete`.
>    6. **MessageGen Email 1** → INLINE AI node (per-motion, NOT a Function). Use the §2 prompt from `Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md`. It must receive `number_allowed` and take the qualitative no-number path when it is false. Never invents a number. Core angle: idle-time layer on top of WFM, never rip-and-replace.
>    7. **Malformed guard** → `fn_draft_clean` (draft_body). If `draft_clean==false`: EXIT `status=HOLD_malformed`.
>    8. **Figure-integrity critic** → `fn_draft_critic` (draft + disclosed_figure + source fields). Number gate keys on a populated source url, NOT on prose. FAIL any number whose row has a blank source url, any competitor-named result, and any WFM-replaced framing.
>    9. **Send-ready gate** → `fn_send_ready`. `human_approved` defaults FALSE, so every real row ends `send_ready=HOLD`.
> 4. Wire every gate **fail-closed**: a failed gate exits the row with its status/reason and never proceeds. A failed row never reaches MessageGen or `send_ready=READY`.
> 5. Add **NO** send, sync, or launch node. The workflow's contract ends at `send_ready`. Nothing leaves Clay from inside the workflow (dry-run law).
> 6. Save two test fixtures as the workflow's test inputs and run `clay workflows runs test` on both:
>    - **(a) KNOWN-GOOD:** a `wfm` contact (e.g. Director of Workforce Management) at a net-new account running Verint/NICE/Calabrio, clean copy, qualitative (no disclosed figure needed). Assert it reaches node 9 with `send_ready=HOLD`.
>    - **(b) KNOWN-BAD:** a fabricated competitor result or a number with a BLANK source url. Assert it EXITS at node 8 with `msg1_critic_status=FAIL`.
>    If (b) passes, **stop and report** — do not proceed; the critic needs tightening.
> 7. Report the workflow id and both test results. Do **not** run it on real rows or load any campaign.

---

## After it's green
- Run on WFM-Adjacency's hardened 10-row slice; confirm all rows end `send_ready=HOLD` and drafts read send-ready to a real WFM/Ops buyer.
- Credit estimate + ledger row before any paid enrichment (technographic is the new cost — sample 10 rows first per credit-steward). First-wave est. ~150–300 credits.
- The real signal-first universe wave is a **separate credit GO** — do not source it without explicit approval.
- **Then Install-Base** needs the *other* golden (donor = Back Office, inverted kill switch) — a separate promotion, not this one.
