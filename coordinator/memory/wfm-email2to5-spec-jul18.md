---
name: wfm-email2to5-spec-jul18
description: WFM-Adjacency Email 2-5 stage prompts spec'd as deltas over the shared Email 1 block; build sheet written Jul 18.
metadata:
  type: project
  date: 2026-07-18
---

Live L3 state (`t_0tic8arWbZp8bSx87Ad`, read-only via clay MCP `table` tool 2026-07-18): 524 rows, 62 columns, ONE outreach column `P2P Outreach Email` (AI, claude-sonnet-5, subject + 70-110w body = MessageGen Email 1). Full gate chain live: persona_key (fn) → 12-provider email waterfall → Work Email/Validate/Status → P2P Outreach Email → Final Audit Verdict (AI claims critic) → fn_draft_critic → Email Voice Audit → Voice Rewrite (Final) → Final Draft Body → Final Voice Audit → **Send Ready** (formula: "READY" only if Final Audit Verdict AND Final Voice Audit both pass, else "HOLD"). The 6 send-ready contacts are the ones who survived the title/role filter out of 524 (yield is by design, not a gate misfire). Clay CLI reads are Enterprise-gated (auth_forbidden); use the plugin `table`/`read` MCP tools instead.

Dallas wants a personalized 5-touch sequence (in the WFM definition of done) ready for Monday. Architecture (confirmed right): each touch = its own MessageGen column, single-responsibility; sequencer schedules/threads but never writes; replies are a separate human-gated objection-handler flow, never a Clay column. The shared house-style block (the live Email 1 prompt: core position, number gate, proof beat, persona routing, banned words, plain-spoken rules) is ~90% and pasted verbatim into every stage; only a short STAGE HEADER changes per touch (escalation soft→stronger→direct-with-deliverable→confident-close; brand window opens Day 6+; sign-off first-name D1-5 → full-name D6+; open on a new facet of the one idea, never "following up").

**Deliverable:** `WFM_Email2to5_Stage_Prompt_Build_Sheet.md` (project root) — 4 stage headers + gold-standard examples + audit-chain reuse + Clay UI build steps (Duplicate P2P Outreach Email, rename, RE-PASTE prompt because Duplicate blanks it, pass blanks as literal `(none)`). Constraint: AI columns are UI-only, the API cannot create them, so Dallas builds the columns and pastes; Claude specs. v1 spec — run each through intradiem-copy-sharpener before going live. Sending still gated on deliverability refresh (UNKNOWN) + mailbox warmup. See [[wfm-adjacency-and-belfield-continuation]].
