---
name: complete-prompt-not-findreplace
description: "For any edit to an existing Clay column/agent prompt, give Dallas the complete copy-paste prompt with changes baked in, never find-and-replace instructions."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T06:45:42.293Z
---

Jul 20 2026: When a Clay column's (or agent's) prompt needs editing, hand Dallas the FULL prompt text with the changes already merged in, so he selects-all and pastes. Do NOT give "find this line and replace it" / "add X before Y" instructions.

**Why:** find-and-replace anchors often don't map to what he sees (e.g. the live MessageGen column splits Prompt and System Prompt fields, so a "Write the email now" anchor from the combined workflow version doesn't exist in the live System Prompt). Hunting for a line to edit is friction and error-prone.

**How to apply:** produce the complete, final prompt (reproduce the original faithfully + merge the change), give it in one code block or a file to copy. Note WHICH field it goes in (Prompt vs System Prompt). Pairs with [[row-actions-use-filters-not-names]] and [[do-it-now-while-in-the-same-place]]. Note: the live MessageGen Email 1 column = the big rules live in the "System Prompt" field; the token block lives in the separate "Prompt" field.
