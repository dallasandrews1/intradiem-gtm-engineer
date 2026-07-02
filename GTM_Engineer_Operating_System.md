# The GTM Engineer Operating System
### A portable method for turning Salesforce + Slack into a self-running deal-intelligence machine

*Extracted from real builds shipped at League. The League specifics (Momentum, payer accounts, named channels) are kept only as proof points — the method below is what transfers. It assumes the two tools Intradiem is confirmed to run: **Salesforce + Slack**.*

---

## The thesis (what a GTM Engineer actually does)

Every B2B GTM org has the same shape: **Salesforce is the database, Slack is where reps actually live, and there's a layer of point tools (call recording, sequencers, MAPs) in between.** What's almost always missing is the *middleware* — the thing that reads what happened, structures it, routes it to the right people, and writes it back to the CRM without a human retyping anything.

A GTM Engineer finds that missing layer, proves the gap is real, and closes it — fast, with the tools already in the building before asking for new budget.

The system runs on one architectural conviction:

> **Salesforce is the system of record. Slack is the interface. AI is the middleware that reads from one and writes to the other — so a rep has near-zero reason to open Salesforce during their day.**

---

## The Operating Loop

This is the repeatable sequence I run at any new org. It's the "way of work" — every project, every account, every automation goes through these moves in order.

### 1 — Diagnose before you build
Walk in and audit what already exists before writing a line of code. Most failures aren't engineering failures; they're "we built on top of broken data/permissions" failures. The audit covers three layers: the **connection layer** (is Salesforce↔Slack actually wired up and user-mapped?), the **object layer** (do the fields the AI needs to write to even exist?), and the **data layer** (are contacts deduped, emails correct, contact roles populated?). *(Full checklist below.)*

### 2 — Find the missing middleware
Name the manual gap out loud. The recurring pattern: a tool posts intelligence into Slack, humans read it, then *manually* retype it into Salesforce — or skip it, so the CRM rots. The diagnostic is simple: *Does your call tool post to Slack? Are SF activity logs current? Do managers read Slack instead of Salesforce for deal intel?* Three "yes/no/no" answers and the bridge is missing — that's the build.

### 3 — Lock the foundation (the knowledge layer)
Before any tooling, write down how the org's data is to be interpreted: which record types count, which field is the source-of-truth for revenue, the real stage list, the owner list, the hygiene risks. This becomes a persistent **Foundational Rules** file that every AI session loads, so every tool produces consistent, trustworthy output instead of each one inventing its own definition of "correct." *(This is the Salesforce Foundational Template — fill it before building on top.)*

### 4 — Architect in four functional layers
Decompose every "intelligence" build into the same four layers, then map each to a tool that exists or a thin piece you build:

| Layer | Job | Build with what's already there |
|---|---|---|
| **1. Capture** | Get a speaker-attributed transcript / signal into a place you can read | Existing call recorder, or any tool that outputs a transcript |
| **2. Intelligence** | Transcript + CRM context → structured output | Claude API + a stage-aware prompt |
| **3. Distribution** | Route the structured output to the right Slack channel(s) | Slack API / webhook |
| **4. CRM write-back** | Push the structured fields into Salesforce | SF REST API, or a lightweight Slack→SF tool |

The layering is the portable part: it doesn't matter what the vendor is, you're always building or buying these four boxes.

### 5 — Engineer the intelligence (the prompt is the product)
The "magic" layer is a well-engineered prompt, not a model. Two rules make it work:
- **Context-enriched, not one-pass.** Feed the LLM the transcript *plus* the Salesforce object context (stage, ARR, account, existing next steps) — that's what produces source attribution and stage awareness instead of generic summary.
- **Stage-aware schema.** A different extraction prompt per pipeline stage, each returning a *defined JSON schema* — not free text. A late-stage call gets a prompt focused on legal/PO/signatures; an early call gets pain + stakeholders. Short and actionable beats a wall of text.

### 6 — Close the loop (write-back is where others quit)
Most DIY builds stop at "posted to Slack." Don't. The differentiator is the write-back: an Activity record on the Opportunity, the next-steps field, contact-intelligence fields, and the qualification/MEDDIC fields. Either fully automatic, or a two-click Slack button → confirm → write. This is what turns Slack into a *headless front end for Salesforce.*

### 7 — Govern, enforce, and roll out
A system that works on Day 1 and rots by Day 90 is a failure. Bake in the durability: validation rules so reps can't advance a stage without minimum field completion; dedupe rules so matching stays clean; monitoring that alerts on OAuth/token failures instead of silently dropping data. Then roll out in the right order — **calendar/connection setup first** (the single most-skipped, most-fatal step), clean the data *before* launch, and treat the first 30 days as tuning.

---

## The Day-1 Diagnostic Kit (the questions I walk in with)

These map the gap in the first conversations — before touching anything.

**Stack & gap:**
- What call recording / conversation tool are you using, and does it connect to Salesforce or just Slack?
- How do reps update Salesforce after a call — manual, or automated?
- Do managers read Slack or Salesforce for deal intel? *(If Slack, the write-back gap is live.)*
- Is there any Slack→SF automation running today?

**Foundation readiness:**
- What fields are reps *required* to fill? *(That's what write-back must map to.)*
- Do you have a qualification framework (MEDDIC/MEDDPICC) with actual SF fields behind it?
- Do you have deal-room channels in Slack, and a naming convention?
- Who owns the Salesforce config and who owns the Slack config? *(Your partners.)*

**Hygiene & access:**
- Is Salesforce↔Slack user-mapped by email/SAML, and is mapping clean?
- Is API access enabled on the integration user? *(Not all SF licenses include it — confirm before writing code.)*
- Any security boundaries to respect (e.g. data-crossing policies, PHI/PII)?

---

## Day-1 → Week-1 application at a Salesforce + Slack org

What I'd actually do in the first week, using only the confirmed stack (Slack + Salesforce). Tool-specific names get filled in once I have access.

**Day 1 — Access + audit.** Get Salesforce read access and run the discovery queries (record types, stage list, owner list, currency/revenue field, custom-field inventory). Confirm the Salesforce↔Slack native connector is live and *my own* user is mapped correctly. Map the tool stack in writing and name the middleware gap publicly — a short, specific written artifact, not a verbal claim.

**Days 2–3 — Foundation.** Fill in the Salesforce Foundational Rules file for this org so every later build shares one definition of "correct." Audit the object layer: do `Next_Steps`, call-date, and qualification fields exist? Are Contact Roles enabled? Run a contact email + duplicate audit on open-pipeline accounts.

**Days 4–5 — First proof.** Stand up the smallest end-to-end slice that demonstrates the loop: capture → Claude intelligence (stage-aware prompt) → structured Slack post → Salesforce activity write-back — even if scoped to my own calls first. A live "call happened → Slack post → SF logged itself" demo is worth more than any deck.

**Throughout — partner, don't lone-wolf.** Identify the RevOps/Salesforce admin and the Slack admin early; nothing routes or writes without them. Frame every build as closing a gap *they* already feel.

---

## Operating principles (the beliefs underneath the method)

- **The gap is almost always the write-back, not the capture.** Capturing intelligence is easy and already happening; getting it *back into the system of record automatically* is the unsolved part.
- **Ship the path of least resistance first.** A Slack webhook ships in hours; a fully-approved CRM integration takes weeks. Get value flowing, then close the loop.
- **The prompt is the product.** Stage-aware, context-enriched, schema-enforced. That's the leverage.
- **Consistency comes from a shared knowledge layer**, not from each tool's individual config. One Foundational Rules file beats five tools each guessing.
- **Design for failure.** OAuth tokens expire, users get unmapped, data drifts. Monitoring and validation rules are the difference between a demo and a system.
- **Adoption is an ordering problem.** Connections first, clean data before launch, 30 days of tuning. Skip the order and the best architecture sits idle.

---

## Proof artifacts (real outputs behind this method)

These are the concrete builds this operating system produced at League — kept as evidence the method is lived, not theoretical. Detail lives in the companion files transferred alongside this one:

- **`momentum-architecture-and-diy-guide.md`** — full reverse-engineering of a production call-intelligence stack and a layer-by-layer plan to replicate it with Claude API + Slack API + SF REST API at near-zero new cost.
- **`call-recording-slack-bridge-pattern.md`** — the portable recording→Slack→CRM bridge: channel architecture, exact message schema, the MEDDIC scoring taxonomy, and where the manual gap sits. Includes real production post examples across master, opportunity, and account-management channels.
- **`day1-prerequisites-sf-slack-setup.md`** — the full Day-1 audit: Salesforce↔Slack native connector setup, the object/field layer the AI writes to, contact-data hygiene fixes, the security/permissions blockers to expect, and the complete pre-build checklist.
- **`SALESFORCE_FOUNDATIONAL_TEMPLATE.pdf`** — the reusable knowledge-layer template: record-type filters, currency/revenue source-of-truth, stage definitions, and the discovery queries to run against a new org before building anything.

---

*Extracted June 2026 from builds shipped at League. Method is tool-agnostic and anchored on Salesforce + Slack. Load this file as the operating reference for any GTM-engineering build at a Salesforce + Slack org.*
