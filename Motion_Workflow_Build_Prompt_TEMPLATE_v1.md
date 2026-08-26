# Motion Send-Readiness Workflow — Local Claude Code Build Prompt (TEMPLATE) v1
**Companion to `Clay_Motion_Scaffold_SOP_v1.md` and `CostMandate_Workflow_Alpha_Blueprint_v1.md`. Generalized from the Cost-Mandate blueprint so any motion is a fill-in-5-blanks paste.**

## What this is / isn't
This builds the **logic layer** — a Clay Workflow (Alpha) that runs a contact through the full send-readiness pipeline by calling your 7 published Functions in order, fail-closed, ending at `send_ready = HOLD`. It does **not** create tables (Clay has no create-table API — that's the Scaffold SOP's `Duplicate table` job) and it does **not** send, sync, or launch. Table structure comes from the duplicated scaffold; this stamps the brain on top.

## Where to run it (the OAuth constraint — not optional)
The Clay CLI authenticates via `clay login`, which opens a browser OAuth flow. A cloud Cowork session cannot complete that, so this **must run in your LOCAL Claude Code (or Cursor)** with the Clay agent-plugin installed and signed into workspace **1180800**. One-time setup, paste into your local agent: `Set up the Clay plugin by following the steps in https://github.com/clay-run/agent-plugins`.

## Before you paste: fill these 5 blanks (from the runbook decisions)
| Placeholder | What it is | Cost-Mandate example |
|---|---|---|
| `{{MOTION_NAME}}` | Human name of the motion | Cost-Mandate |
| `{{MOTION_KEY}}` | `source_motion` tag | `cost_mandate` |
| `{{PERSONA_KEYS}}` | Node-2 ICP gate — the FULL canonical rubric, **constant across motions** (not the motion's target subset). Exits only genuinely out-of-ICP titles. Per-motion persona *targeting* lives in node 6/sourcing, not here. | `coo_finance, cc_ops, bo_claims, bo_shared, wfm, cx` |
| `{{MSGGEN_FILE}}` | The motion's MessageGen prompt file | `Clay_MessageGen_SystemPrompt_CostMandate_v1.md` |
| `{{NUMBER_RULE}}` | The H1 number-window rule for node 4 | signal_source_url non-empty AND signal_source_date within 90 days of today |

## Two pre-reqs to confirm live first (Functions are UI-only, not CLI-writable)
The workflow inherits whatever your Functions hold, so fix these in the Clay UI before building:
1. `fn_send_ready` — confirm it AND-s in `draft_clean` AND `email_status == "valid"` alongside critic PASS + human_approved + NOT bdr_claimed + NOT customer_exclude.
2. `fn_persona_key` — confirm it can return every key in `{{PERSONA_KEYS}}` (the Cost-Mandate gap was a missing `cc_ops` branch). If a persona in your list has no branch, the motion's primary contacts fall through.

---

## THE PROMPT (fill the 5 blanks, then paste into local Claude Code)

> You have the Clay agent-plugin installed and authenticated to workspace 1180800. Build a Clay Workflow (Alpha) named **"{{MOTION_NAME}} Send-Readiness (Alpha)"**. Use the Cost-Mandate blueprint (`CostMandate_Workflow_Alpha_Blueprint_v1.md`) as the structural reference — same 9-node fail-closed graph, this motion's specifics swapped in.
>
> Steps:
> 1. Run `clay workflows create --name "{{MOTION_NAME}} Send-Readiness (Alpha)"`.
> 2. **Read the created workflow graph first** to learn the live node schema. Clay has not published the Workflows-Alpha node syntax, so do not hand-author JSON blind — edit nodes against the schema you actually see.
> 3. Add nodes 1–9 in this exact order, mapping each Function node to the published Function by name:
>    1. **Eligibility kill switch** → `fn_eligible` (company_domain, customer_flag). If `eligible==false`: EXIT `status=EXCLUDED` carrying `exclusion_reason`.
>    2. **Persona routing** → `fn_persona_key` (job_title). EXIT `status=HOLD_persona` unless `persona_key` ∈ {`{{PERSONA_KEYS}}`} — the full 6-key rubric, so it exits only truly out-of-ICP titles and is robust to the live fallback value (`review`). Use set-membership, not equality on a fallback value. Do NOT narrow this to the motion's target personas; that targeting happens in node 6 and in sourcing.
>    3. **Email verify** → `fn_email_verified` (first_name, last_name, company_domain). If `email_status != "valid"`: EXIT `status=HOLD_no_email`.
>    4. **Number-source gate** → CODE node (workflow-owned). Compute `number_allowed` = `{{NUMBER_RULE}}`. Never exits; sets the flag MessageGen obeys.
>    5. **Tokens ready** → `fn_tokens_ready` (first_name, job_title, company, persona_key, email_status, source_motion). If `tokens_ready==false`: EXIT `status=HOLD_incomplete`.
>    6. **MessageGen Email 1** → INLINE AI node (per-motion, NOT a Function). Use the §2 prompt from `{{MSGGEN_FILE}}`. It must receive `number_allowed` and take the qualitative no-number path when it is false. Never invents a number.
>    7. **Malformed guard** → `fn_draft_clean` (draft_body). If `draft_clean==false`: EXIT `status=HOLD_malformed`.
>    8. **Figure-integrity critic** → `fn_draft_critic` (draft + disclosed_figure + source fields). Number gate keys on a populated source url, NOT on prose. FAIL any number whose row has a blank source url.
>    9. **Send-ready gate** → `fn_send_ready`. `human_approved` defaults FALSE, so every real row ends `send_ready=HOLD`.
> 4. Wire every gate **fail-closed**: a failed gate exits the row with its status/reason and never proceeds. A failed row never reaches MessageGen or `send_ready=READY`.
> 5. Add **NO** send, sync, or launch node. The workflow's contract ends at `send_ready`. Nothing leaves Clay from inside the workflow (dry-run law).
> 6. Save two test fixtures as the workflow's test inputs and run `clay workflows runs test` on both:
>    - **(a) KNOWN-GOOD:** a real cited figure, clean copy, source url populated, source date within the window. Assert it reaches node 9 with `send_ready=HOLD`.
>    - **(b) KNOWN-BAD:** a fabricated number with an attribution phrase and a BLANK source url. Assert it EXITS at node 8 with `msg1_critic_status=FAIL`.
>    If (b) passes, **stop and report** — do not proceed; the critic needs tightening.
> 7. Report the workflow id and both test results. Do **not** run it on real rows or load any campaign.

---

## After it's green
- Run the workflow on the motion's current hardened slice; confirm all rows end `send_ready=HOLD` and drafts read send-ready to a real buyer in that persona.
- **Clone-per-motion payoff:** the next motion swaps only node 6 (`{{MSGGEN_FILE}}`) and node 4 (`{{NUMBER_RULE}}`). Every Function node carries over unchanged. That's the whole point of building on the 7 Functions.
- The real signal-first universe wave is a **separate credit GO**. Do not source it without explicit approval.

## The pairing (how A + B answer "consistently and accurately per motion")
1. Decide the motion + answer the runbook's two decisions.
2. **Scaffold SOP:** `Duplicate table` the L0–L4 golden scaffold into a new `<Motion> Motion` workbook, re-point the 5 motion-specific bits. (structure — seconds, deterministic, no agent)
3. **This prompt:** fill 5 blanks, paste into local Claude Code, get a tested send-readiness Workflow. (logic — agent-built, one auditable pipeline)
4. Runbook gates: 10-row slice → credit ledger → Draft + critic PASS + approval → nothing sends.
