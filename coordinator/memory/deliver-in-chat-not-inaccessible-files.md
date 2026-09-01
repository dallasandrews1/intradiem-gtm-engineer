---
name: deliver-in-chat-not-inaccessible-files
description: FEEDBACK (Jul 22) — deliver actionable content IN CHAT; stop routing things Dallas must use to folders he can't access (Desktop TCC, scratchpad)
metadata:
  type: feedback
---

FEEDBACK (2026-07-22, said with visible annoyance): "stop creating documents that are meant for me to actually open up now in folders I can't access on my computer."

**Why:** Dallas repeatedly got copy-paste prompts, examples, and deliverables written to files (project subfolders, the Desktop `Intradiem Deliverables` TCC folder, the scratchpad) when what he needed was the content in hand. Being made to open a file to get pasteable content, or handed a link to a folder he can't reach, wastes his time mid-task.

**How to apply:**
- Anything Dallas will ACT ON directly (copy-paste Clay prompts, example emails, Slack-ready briefs) goes IN CHAT, as ready-to-copy blocks, by default. Do not make him open a file for it.
- Durable engineering SPECS (canonical prompt files, change maps, runbooks) can still be repo files IN HIS WORKSPACE (he can open those in VS Code), but surface the actionable slice in chat too.
- CLARIFIED Jul 22 (Dallas corrected an over-read): the two rules cover DIFFERENT things and do NOT conflict.
  * Pasteable/actionable CONTENT (Clay prompts, example emails, Slack briefs) → IN CHAT. Don't make him open a file for it. This is what the annoyance was about (plus the scratchpad/temp dirs, which ARE junk to him).
  * FINISHED branded deliverable PDFs → STILL go to `~/Desktop/Intradiem Deliverables/` per [[exec-update-pdf-standard-format]] and [[findings-become-exec-deliverables]]. That standing rule is NOT retired. The Desktop folder is his canonical deliverables home. Copy the final PDF there on EVERY finished deliverable, plus any editable companion (e.g. a .docx for reviewer markup). Editable HTML source + PDF also live in the project `exec-updates/`.
- So: build the branded HTML/PDF as the deliverable, copy it to the Desktop folder, AND surface the key content in chat. Not either/or.
- ACCESS UPDATE (2026-07-22): Dallas granted Full Disk Access, so `~/Desktop/Intradiem Deliverables/` is now WRITABLE by plain Bash `cp` (no `dangerouslyDisableSandbox` needed; earlier "Operation not permitted" is resolved). The exact folder is `/Users/dallasandrews/Desktop/Intradiem Deliverables` (note the space). DEFAULT to copying every finished deliverable there yourself, do NOT wait for Dallas to ask, he had to remind me twice this session because I skipped it.
