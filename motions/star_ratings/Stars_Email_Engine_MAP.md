# Stars Email Engine — The Map (single source of truth)
Last updated: 2026-07-20

This explains the whole email-writing machine in one place so it's a cohesive thing, not a pile of parts.

## The four Clay building blocks (and how they connect)
1. **Claygent** = a reusable AI agent (a saved prompt + model). Does nothing alone. Gets *used by* a workflow node or a table AI column. (Tools=None is correct for writing/judging agents.)
2. **Table AI column** = an AI action that runs per row on the Contacts table. Either an inline prompt or a Claygent.
3. **Workflow** (Terracotta, `wf_0tiegzuo3PzJ4UtUGFA`) = a node graph. Agent nodes use Claygents. This is the multi-touch (E1-E5) engine.
4. **Sequencer campaign** = sends the emails. It pulls the finished email TEXT from table columns. It never touches Claygents or the workflow directly.

Data flows: **Claygent/column/workflow generate email text INTO the table → the campaign pulls that text and sends it.**

## The winning method (proven Jul 20): TWO-PASS
One AI pass can't nail facts AND human voice at once. So split it:
- **Pass 1 - MessageGen** (claude-sonnet-5): writes the draft, owns the FACTS. Passes the figure/claim critic.
- **Pass 2 - Voice Fix** (GPT-5.6): rewrites ONLY the cadence, breaks stacking, avoids chopping (CONNECT the pieces), kills false-contrast and decorative flourishes, preserves every number. Owns the VOICE.
- Then the audits (Draft Audit = facts, Voice Audit = cadence) read the **Voice Fix** output, and the send gate requires both PASS.

## Engine A — Email 1 (LIVE, powers wave 2). Lives as TABLE COLUMNS on `t_0thtm73HHxyiupTuepK`.
Flow: `MessageGen Email 1 (v2.2)` -> `Voice Fix` -> `VoiceFix Subject`/`VoiceFix Body` (extractors) -> `Draft Audit` + `Voice Audit` (read VoiceFix) -> `send_ready` (READY only if email valid + critic PASS + voice PASS) -> the wave-2 campaign pulls VoiceFix Subject/Body.
Status: DONE and verified. Wave 2 ships on this.

## Engine B — Emails 1-5 (autonomization). Lives in the WORKFLOW `wf_0tiegzuo3PzJ4UtUGFA`.
Purpose: generate + gate all 5 touches per contact in one run, so E2-5 aren't hand-written.
Flow per touch (En): `MessageGen En` -> `Voice Fix En` (NEW, being added Jul 20) -> `Figure-integrity critic En` + `Voice Audit En` (read Voice Fix En) -> send-ready gate En.
Status: IN PROGRESS. MessageGen E1-E5 nodes already carry the latest writing rules (clinical guardrail, false-contrast ban, anti-stack). The Voice Fix pass is being added node-by-node so the workflow matches Engine A's quality.

## Why two engines, and the unification
Engine A got Email 1 out fast for the wave-2 deadline. Engine B (the workflow) is how E2-5 scale without hand-building columns. The unification = port the Voice Fix pass into the workflow (Engine B) so every touch generates at Engine A's quality, then wire the workflow's output back into the Contacts table so the sequence pulls all 5. Once Engine B is complete, it can replace Engine A for Email 1 too, one engine, five touches, fully autonomous.

## What each wave needs
- **Wave 2 (now):** Email 1 only, from Engine A. Launch on that.
- **Wave 3+ / full 5-touch:** Engine B complete (Voice Fix on all 5 + writeback to the table).
