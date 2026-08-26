# Clay Sculptor Operating SOP — "Copilot, Not Architect" v1
**Owner: Dallas Andrews. Companion to `Clay_Motion_Scaffold_SOP_v1.md`, `Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`, `New_Motion_Build_Runbook.md`, `Clay_Golden_Standard.md`. Open this the moment you're tempted to say "let Sculptor build it."**

## Why this exists
Sculptor is Clay's **native in-app AI copilot** — the one thing that can build a Clay table without a human clicking through Chrome and without hitting the "no create-table API" wall. That makes it tempting to hand it the whole engine. Don't. Your engine's value is in the parts Sculptor is explicitly weakest at: run conditions, message drafting, fail-closed gates, verified-claims discipline, and deterministic repeatability across motions. This SOP draws the line so Sculptor accelerates you on the two fronts it's genuinely good at and stays out of the layers that carry your risk.

The one-line rule: **Sculptor drafts and analyzes; your system decides and sends.** Everything it produces is a draft that must pass the gates you already built.

## What Sculptor actually is (verified, and its limits)
Verified Jul 17 2026 against `university.clay.com/docs/sculptor` and `clay.com/sculptor`.

**Two modes:**
- **Builder Mode** — turns plain-English intent into tables/columns step by step. Full support for **AI Columns** (read, recommend, configure, edit, preview) and **Formulas** (read, recommend, configure, edit). **Partial** on enrichments (read + recommend; configuration "coming soon"). Table edits run in **Sandbox mode with approval-before-publish**.
- **Analyst Mode** — queries an entire table in plain English: patterns, outliers, health checks, pipeline snapshot. Exports to Notion/PDF. **Read-only** — it does not modify the table.

**Stated limits (this is the important half):** no run conditions, no message drafting, no filters/sorting, no Signals-table support, limited cross-table operations, cannot configure sources yet (CPJ/Google Maps/CSV limited), no direct CRM integration, and it **won't build a complete workflow from a single request**. Non-deterministic by nature — same prompt, different structure.

**What this UPDATES:** `Clay_Motion_Scaffold_SOP_v1.md` says "Clay has no create-table API → an agent physically cannot build tables → browser automation is the only path." That remains true for **external** agents (MCP, CLI, agent-plugin — verified). It is **not** true for Clay's own in-app AI: Sculptor can build tables, with your approval. So "browser is the only path" is softened for net-new/exploratory building. It does **not** change the cloning story — see the decision rule.

## The decision rule (when Sculptor vs when not)
Three build surfaces, three right tools. Pick by what you're actually doing, not by what's newest.

| You're doing this | Use | Not this | Why |
|---|---|---|---|
| **Cloning an existing motion** (stamp motion N) | `Duplicate table` from `__GOLDEN` | Sculptor | Deterministic + seconds. Sculptor re-generates structure probabilistically and forces full re-verification every stamp. Determinism beats regeneration. |
| **First draft of a genuinely NEW table / AI column / formula** you have no golden for | **Sculptor Builder** → then verify | Hand-building in Chrome | Faster first pass; Sandbox+approval fits dry-run law. Then run First-Duplicate Verification — treat output as a draft. |
| **The 9-node fail-closed send-readiness Workflow** | Workflows-Alpha via **local** Claude Code/CLI | Sculptor | Sculptor can't do run conditions, message drafting, or a complete workflow. This layer is programmatic, testable, snapshotable. |
| **Understanding / QA'ing what's in a live table** | **Sculptor Analyst** | manual UI scan | Read-only, instant, exactly the verify/tune half of your job. See question bank. |
| **MessageGen or critic/send-ready copy** | Your per-motion MessageGen + gates | Sculptor | Verified-claims-disciplined, per-motion (never functionalized). Sculptor has no voice gate and no claims repo. |

**Guiding heuristic:** if the artifact is something you'll *clone repeatedly* or *must be identical every time*, Sculptor is the wrong tool — it's non-deterministic. If it's a *one-off draft* or a *read*, Sculptor earns its place.

## Front 1 — Analyst Mode over live tables (the immediate, low-risk win)
This is where Sculptor pays off today, because it's read-only and answers questions you currently resolve by eyeballing the UI. Starter question bank, keyed to your real open items:

**Persona routing integrity (unblocks the Cost-Mandate dead-gate):**
- "How many rows in Contacts have `persona_key` = `review`? List them with title and company." — this is the manual scan the scaffold work flagged before flipping the `fn_tokens_ready` gate. Answer it here in one question.
- "How many rows resolved to `out_of_icp` vs each valid persona key (`coo_finance`, `cc_ops`, `bo_claims`, `bo_shared`, `wfm`, `cx`)? Show the distribution."
- "Which rows have a title containing 'customer care' or 'member services' but did NOT resolve to `cc_ops`?" — catches the branch-order bug pattern you already hit once.

**Send-readiness snapshot (pre-launch health check):**
- "How many rows are `send_ready` = HOLD vs PASS, and for the HOLDs, what's the most common blocking reason?"
- "Which rows have a drafted message but failed the critic — group by failure reason."
- "How many rows have `source_motion` blank or set to a value other than the current motion key?"

**Universe / data-quality checks:**
- "What's the email-verification coverage — how many rows have a valid verified email vs missing/unverified?"
- "Flag likely duplicate contacts against the install-base (same person, two rows)."
- "Show outliers in agent/FTE count that would break the ROI number rule for this motion."

Run these before every wave launch as a standing health check. Export the pre-launch snapshot to PDF and drop it in the readout — it doubles as evidence for Naveen that the engine self-QAs.

## Front 2 — Builder Mode for NEW structures only (draft, then gate)
Use Builder Mode when you're inventing structure you don't have a golden for: a brand-new motion's L0–L4 before it earns promotion to `__GOLDEN`, a novel AI column, or a formula you'd otherwise hand-write. Workflow:

1. Describe the intent in plain English. Let Sculptor draft in **Sandbox**.
2. **Do not publish on its say-so.** Review every column against the contract.
3. Run the **First-Duplicate Verification** checklist from `Clay_Motion_Scaffold_SOP_v1.md` — Sculptor output is non-deterministic, so it gets the same scrutiny as a fresh duplicate: no stray Claygent binding, no orphan campaign column with Auto-run ON, run-conditions present, "Required to run" OFF on optional inputs, Lookups resolve, sender OFF.
4. Only after it passes does it become a candidate. If the new motion proves out, promote its clean L0–L4 to `__GOLDEN` (per `Golden_Scaffold_Promotion_Checklist_v1.md`) — and from then on you **clone it, you don't re-Sculpt it.** Sculptor builds the first of a kind; Duplicate-table builds the next thousand.

## Guardrails — the lines Sculptor never crosses
- **No autonomous publish.** Sandbox + your approval on every table edit. This is Sculptor's default and it aligns with dry-run-by-default — keep it that way.
- **No message drafting.** MessageGen stays yours, per-motion, through the voice gate and verified-claims repo. Sculptor has neither.
- **No gate authoring.** Send-readiness logic, critic, run-conditions = Workflows-Alpha, built and tested locally.
- **No verified-number generation.** Sculptor doesn't know the Intradiem Value Repository. Anything it surfaces that reads like an Intradiem stat is `[UNVERIFIED]` until checked against the repo.
- **Nothing it produces sends.** Same law as the rest of the stack: structure and analysis only; loading, enriching, drafting, and launching stay gated, waved, and human-approved.

## The law this preserves
Sculptor changes *who drafts*, never *who decides*. It removes some Chrome toil and answers read questions fast; it does not touch the fail-closed spine, the verified-claims discipline, or the human send gate. Source once, process in waves. Measurement before volume. Draft with the copilot; decide with the system.
