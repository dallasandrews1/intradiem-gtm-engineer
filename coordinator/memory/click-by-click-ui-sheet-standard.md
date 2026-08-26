---
name: click-by-click-ui-sheet-standard
description: Standing deliverable format — when a task needs Dallas's own hands in his Clay account, produce a click-by-click UI sheet.
metadata:
  type: feedback
---

**Standing preference (Dallas, 2026-07-19):** whenever a task requires Dallas to go to his Intradiem Clay account and build/do something himself (anything NOT agent-buildable: Functions, AI columns, table structure, running a workflow on a real row, attaching a workflow to a table), the STANDARD deliverable is a **click-by-click UI sheet**.

**Why:** the agent-buildable/UI-only split means some steps must be his hands; a precise sheet makes those fast and unambiguous.

**How to apply:**
- Ground every step in the EXACT table/field/workflow IDs (not vague names).
- VERIFY Clay's current UI before writing steps (house rule); never fabricate button labels; flag any label to confirm.
- Include: the target IDs, the click path, exactly what to change/paste, and a verification/regression step.
- If the paste content is a live send-gating asset (e.g. a shared Function prompt), author the exact paste-ready text carefully against the live structure rather than handing a half-formed block; the sheet can give the navigation while the paste text is produced separately.
- Save the sheet as a durable file (e.g. `UI_Sheet_<task>.md`).

**NEVER hand Dallas raw Clay-formula code to paste into the visual AI-prompt editor (Dallas, 2026-07-19, learned the hard way):** the visual "Prompt" editor does NOT interpret pasted `Clay.formatForAIPrompt({{...}})` / `+ "\n..." +` code — it inserts it as LITERAL TEXT and breaks the concatenation (caused a malformed published fn_draft_critic prompt). For chip references, give ONLY: the plain label text to TYPE (e.g. `source_motion: `) + the picker steps to insert the chip (`/` → click Record → click the sub-key). The raw `Clay.formatForAIPrompt(...)` form is the underlying representation for READING/verifying, never for Dallas to paste. Also: every Record-sub-key chip DISPLAYS "Record" (the parent name), you can't tell sub-keys apart by label, so verify the binding by reading it, not by the chip label.

**Chip-marking (Dallas, 2026-07-19):** in ANY Clay AI-prompt Dallas pastes, explicitly MARK every `{{}}` reference that must be inserted via the `/` picker (binds by column ID) vs plain text that's typed. A `{{}}` typed as text does NOT bind (known Clay gotcha). State clearly which blocks have zero chips (paste verbatim) and, for each chip, the exact 3-part build: type-literal → `/`-pick the column → type-literal. Example done in `UI_Sheet_fn_draft_critic_fix.md` (system prompt = 0 chips; the one added User-Prompt line = 1 chip, `{{Function inputs}}` via `/`).

**Complement (Dallas, 2026-07-19):** for AGENT-buildable tasks/handoffs (things Claude executes), provide a ready copy-paste prompt block INLINE in the chat that Dallas pastes back to trigger/confirm — do NOT make him open a document or compose the request. UI-only tasks → saved sheet; agent-buildable tasks → in-chat copy-paste prompt. Both in both CLAUDE.md.

Also added to both CLAUDE.md working conventions. First instances: `UI_Sheet_fn_draft_critic_fix.md` (the Function fix) and the pending workflow-run sheet (after Claude wires the Stars trigger to L3). See [[star-ratings-upgrade-backlog]].
