# Cost-Mandate Send-Readiness Workflow (Clay Workflows Alpha) — Blueprint v1

**Date:** 2026-07-17
**Pilot motion:** Cost-Mandate (hardened, non-launched, proved the fail-closed pattern). Not Stars.
**Workspace:** 1180800
**What this is:** the node graph for a Clay Workflow (Alpha) that runs a contact through the full send-readiness pipeline by *calling your 7 published Functions in order*, with every gate fail-closed, and ends at `send_ready = HOLD`. It does NOT send, sync, or launch. Launch stays a separate human action, exactly as today.

Why a Workflow and not more table columns: Workflows Alpha escapes the 50,000-row table cap, supports code nodes (the H1 date-window check), and can be built/edited by an agent in Claude Code instead of click-by-click in the grid. It orchestrates logic; your Functions still do the work and still bill exactly as they do now. No credit savings, same win as Functions: one auditable pipeline, fix-once.

---

## 0. Pre-requisites to confirm before building (2 min)

Your 7 Functions exist. Live check in workspace 1180800 (Jul 17) found two required edits before building. Both are Clay UI edits (Functions are not CLI-writable). Make them first; the workflow inherits whatever these Functions hold.

1. **`fn_send_ready`** (t_0tiahe2mzsH9CCaC4Sx) — `draft_clean` is already AND-ed in (confirmed live). It is MISSING an `Email Status` input. Add a function input `Email Status` (string) and set the formula to:
   `{{Function inputs}}?.["Msg 1 Critic Status"] == "PASS" && {{Function inputs}}?.["Human Approved"] && !{{Function inputs}}?.["Bdr Claimed"] && !{{Function inputs}}?.["Customer Exclude"] && {{Function inputs}}?.["Draft Clean"] && {{Function inputs}}?.["Email Status"] == "valid" ? "READY" : "HOLD"`
2. **`fn_persona_key`** (t_0tiahksb4jmyFfMSQYd) — live formula returns only `bo_claims` / `bo_shared` / `coo_finance` / `review` (fallback). Two gaps: it never returns `cc_ops` (so the motion's primary persona, e.g. "VP Customer Care Operations", falls through), and it never returns `out_of_icp`. REQUIRED: add a `cc_ops` branch before the fallback, matching customer-facing ops titles (customer care operations, contact center operations, customer experience operations, VP Customer Care, head of customer operations), scoped distinct from the company-wide COO/VP-Operations titles `coo_finance` owns. The `review`→`out_of_icp` rename is OPTIONAL and only if nothing else consumes `review`; node 2's gate is set-membership so it does not depend on the fallback value.

---

## 1. Workflow identity

- **Name:** `Cost-Mandate Send-Readiness (Alpha)`
- **Input:** one contact record (the workflow runs per-row; batch the wave through it). Fields:
  `first_name, last_name, company, company_domain, job_title, customer_flag, disclosed_figure, disclosed_figure_source, signal_source_url, signal_source_date, signal_evidence, top_signal, product_angle, vertical, source_motion` (must equal `cost_mandate`), `human_approved` (default FALSE), `bdr_claimed` (default FALSE).
- **Output:** structured record carrying every field below plus the final `send_ready` verdict and the reason trail. Downstream (campaign load) reads this; the workflow never writes to a campaign itself.

---

## 2. The node graph (in order, fail-closed)

Each node maps to a published Function by name, or is a small code/formula node the workflow owns. Any gate that fails exits the row early with a status and reason; a failed row never reaches MessageGen or `send_ready=READY`. That is the design, not a limitation.

| # | Node | Type | Calls | Inputs → Outputs | Gate behavior (fail-closed) |
|---|------|------|-------|-------------------|------------------------------|
| 1 | **Eligibility kill switch** | Function | `fn_eligible` | company_domain, customer_flag → `eligible`, `exclusion_reason` | If `eligible==false`: EXIT `status=EXCLUDED`, carry `exclusion_reason`. Customers + install-base + AmEx die here. |
| 2 | **Persona routing** | Function | `fn_persona_key` | job_title → `persona_key` | EXIT `status=HOLD_persona` if `persona_key` is NOT one of {coo_finance, cc_ops, bo_claims, bo_shared, wfm, cx}. Set-membership (not `==out_of_icp`) so it is robust to the live fallback value (`review`) and any non-ICP title. |
| 3 | **Email verify** | Function | `fn_email_verified` | first_name, last_name, company_domain → `email_final`, `email_status` | If `email_status!="valid"`: EXIT `status=HOLD_no_email` (H4 deliverability). |
| 4 | **H1 source gate** | Code node | *workflow-owned* | signal_source_url, signal_source_date → `number_allowed` (bool) | `number_allowed = url is non-empty AND date within 90 days of run date`. Never exits; sets the flag MessageGen obeys. |
| 5 | **Tokens ready** | Function | `fn_tokens_ready` | first_name, job_title, company, persona_key, email_status, source_motion → `tokens_ready` | If `tokens_ready==false`: EXIT `status=HOLD_incomplete`. MessageGen structurally cannot fire on a thin row. |
| 6 | **MessageGen Email 1** | AI node (per-motion, NOT a Function) | Cost-Mandate §2 prompt | all contact fields + `number_allowed` → `draft_subject`, `draft_body` | If `number_allowed==false`: prompt takes the qualitative no-number path (recover idle capacity already on payroll, no new headcount). Never invents a number. |
| 7 | **Malformed guard** | Function | `fn_draft_clean` | draft_body → `draft_clean` | If `draft_clean==false`: EXIT `status=HOLD_malformed` (catches Sonnet double-encode). |
| 8 | **Figure-integrity critic** | Function | `fn_draft_critic` | draft_subject, draft_body, disclosed_figure, disclosed_figure_source, signal_source_url, signal_source_date, signal_evidence, top_signal, product_angle, vertical → `msg1_critic_status`, `critic_reason` | Number gate keys on a populated `signal_source_url`, NOT on Claygent prose. FAIL any number whose row has blank url. |
| 9 | **Send-ready gate** | Function | `fn_send_ready` | msg1_critic_status, human_approved, bdr_claimed, customer_exclude, draft_clean, email_status → `send_ready` | `human_approved` defaults FALSE, so every real row ends `send_ready=HOLD`. A rep flips approval later, outside this workflow. |

**End state for a healthy row:** `eligible=true`, valid email, `tokens_ready=true`, clean draft, `msg1_critic_status=PASS`, `send_ready=HOLD`. HOLD is correct. Nothing is ready to send until a human approves.

**No node 10.** There is deliberately no send/sync/launch node. The workflow's contract ends at `send_ready`. This preserves the dry-run law: nothing leaves Clay from inside the workflow.

---

## 3. Baked-in H2 critic test (anti-rubber-stamp)

Save these two fixtures as the workflow's test inputs. Any edit to the workflow or to `fn_draft_critic` must still pass (a) and fail (b) before you trust a real PASS.

- **(a) KNOWN-GOOD:** a real cited figure, clean copy, `signal_source_url` populated, `signal_source_date` within 90 days. Expect: node 8 `PASS`, and node 9 `send_ready=HOLD` (because `human_approved=false`, which is the correct healthy end state).
- **(b) KNOWN-BAD:** a fabricated number with an attribution phrase (e.g. "the 5,000 roles you cut last quarter") and a BLANK `signal_source_url`. Expect: node 8 `FAIL`, row exits at the critic.

Run both through the CLI test harness (section 5) after every build or edit. A workflow that passes (b) is theater; tighten `fn_draft_critic` §4 until it discriminates, then re-test.

---

## 4. Design principles this graph enforces (do not remove when editing)

- **Fail-closed.** Every gate exits the row on failure; nothing degrades into a send.
- **Human gate.** `human_approved` defaults FALSE; `send_ready` can only read READY after a human sets it true downstream.
- **Verified-claims.** Numbers require a real `signal_source_url` within 90 days (H1), enforced at MessageGen (node 6) and again at the critic (node 8). No source, no number, qualitative path.
- **Deliverability gate.** Only ZeroBounce-valid emails proceed (node 3, H4).
- **Per-motion copy stays per-motion.** Node 6 is the Cost-Mandate MessageGen prompt inline, never a shared Function (Golden Standard §6). Re-point it per motion when you clone this workflow.

---

## 5. Build it — exact steps for your local Claude Code / Cursor (Clay agent-plugin authenticated)

This runs where the Clay CLI is OAuth-signed into workspace 1180800. Paste the prompt in section 6 into that agent. The commands it will run:

```bash
# 1. create the empty workflow (returns an id like wf_...)
clay workflows create --name "Cost-Mandate Send-Readiness (Alpha)"

# 2. the agent reads the created workflow, then adds nodes 1-9 per this blueprint,
#    mapping each Function node to the published fn_* by name.

# 3. test with the two H2 fixtures (replace wf_ID)
echo '{"first_name":"Test","last_name":"Good","company":"Acme","company_domain":"acme.com","job_title":"CFO","customer_flag":false,"disclosed_figure":"1,400","signal_source_url":"https://<real-primary-source>","signal_source_date":"2026-06-20","product_angle":"","vertical":"retail","source_motion":"cost_mandate","human_approved":false,"bdr_claimed":false}' | clay workflows runs test wf_ID --input -

echo '{"first_name":"Test","last_name":"Bad","company":"Acme","company_domain":"acme.com","job_title":"CFO","customer_flag":false,"disclosed_figure":"5,000 roles you cut last quarter","signal_source_url":"","signal_source_date":"","product_angle":"","vertical":"retail","source_motion":"cost_mandate","human_approved":false,"bdr_claimed":false}' | clay workflows runs test wf_ID --input -
```

Expected: fixture (a) reaches node 9 with `send_ready=HOLD`; fixture (b) exits at node 8 with `msg1_critic_status=FAIL`. If (b) passes, stop and tighten the critic.

**Schema note (honest):** Clay hasn't published the exact node-definition syntax for Workflows Alpha. That's fine — the intended flow is that the agent runs `clay workflows create`, reads the resulting workflow graph, and edits nodes against the live schema it sees. This blueprint gives the agent the logical graph (order, function mapping, gates, exits); the agent fills the exact node syntax from what it reads. Do not hand-author the JSON blind.

---

## 6. Copy-paste prompt for your local Claude Code (Clay plugin installed)

> You have the Clay agent-plugin installed and authenticated to workspace 1180800. Build a Clay Workflow (Alpha) named "Cost-Mandate Send-Readiness (Alpha)" from the attached blueprint (CostMandate_Workflow_Alpha_Blueprint_v1.md).
>
> Steps: (1) Run `clay workflows create --name "Cost-Mandate Send-Readiness (Alpha)"`. (2) Read the created workflow graph to learn the node schema. (3) Add nodes 1 through 9 in the exact order in section 2, mapping each Function node to the published Function by name (fn_eligible, fn_persona_key, fn_email_verified, fn_tokens_ready, fn_draft_clean, fn_draft_critic, fn_send_ready). Node 4 is a code node computing `number_allowed` (signal_source_url non-empty AND signal_source_date within 90 days of today). Node 6 is an inline AI node using the Cost-Mandate MessageGen §2 prompt from Clay_MessageGen_SystemPrompt_CostMandate_v1.md, and it must receive `number_allowed` and take the qualitative no-number path when it is false. (4) Wire every gate fail-closed exactly as the "Gate behavior" column says: a failed gate exits the row with the given status and reason and never proceeds. (5) Add NO send, sync, or launch node — the workflow ends at send_ready. (6) Save the two H2 test fixtures from section 3 as the workflow's test inputs and run `clay workflows runs test` on both. Assert fixture (a) reaches send_ready=HOLD and fixture (b) exits at the critic with FAIL. If (b) passes, stop and report — do not proceed. (7) Report the workflow id and the two test results. Do not run it on real rows or load any campaign; dry-run law holds.

---

## 7. After it's green

- Run the workflow on the current 5 hardened rows as a slice; confirm all end `send_ready=HOLD` and the drafts read send-ready to a real COO.
- Clone-and-repoint for the next motion by swapping node 6 (MessageGen prompt) and node 4's number rule; every Function node carries over unchanged. That clone-per-motion pattern is the payoff of building on Functions.
- The real 150–200 signal-first universe wave is a SEPARATE credit GO. Do not source it without explicit approval.
