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

**Polar-ready by default (Dallas, 2026-09-13):** since Polar (the AI browser on his personal Mac) executes these sheets, every UI sheet now carries two more blocks and a closing read:
- **STOP-AND-HAND-BACK lines:** listed after the steps and repeated inline at the step. Always before any step that sends or launches, spends credits (any Clay estimate above 0), changes a gate or a sender, deletes anything the sheet did not name by id, or where the screen differs from the sheet (title, id, or an untouched input not matching the recorded value).
- **REPORT-BACK block:** the exact files Polar saves (`report.md` plus named screenshots or exports) and the folder `automation/inbox/polar/<task-slug>/`. The task is registered in `automation/config/polar_tasks.json` with its verifier; `automation/polar_intake.py` logs the files and the `polar-intake` agent performs the verifier read.
- **Verification that closes the task (Claude Code, not Polar):** the CLI or connector read that proves the change on the real row or campaign. A Polar report is a claim until that read lands.
- The paste block is a single fenced block Dallas pastes into a Polar task, written to Polar (numbered, "do not improvise", the save path, "stop, do not message anyone"). Labels not in the vendor's docs are marked to confirm and the sheet says "read the screen".
First instances: `motions/shared/polar_sheets/` (WFM L3 lookup re-bind, Stars - Resurrection stray steps), live at gtm-polar-sheets.pages.dev. See [[polar-browser-strategy-sep13]].
