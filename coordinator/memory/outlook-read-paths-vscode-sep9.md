---
name: outlook-read-paths-vscode-sep9
description: Sep 9 2026 - no path reads Dallas's Outlook mail from a VS Code / CLI session (M365 connector unauthorized, New Outlook has no AppleScript message access, headless claude -p hits the same auth wall); ask Dallas to paste the email
metadata:
  type: project
---

Tried Sep 9 2026 while asked to read a Naveen email: the claude.ai Microsoft 365 connector is unauthorized in VS Code and CLI sessions (only the scheduled pmo-action-extractor job has read it, and today's run logged email 0); New Outlook for Mac returns 0 messages to AppleScript and stores mail in the proprietary HxStore.hxd (4 MB, no plain text); a headless `claude -p` call with the M365 tools returns the same unauthenticated message; Slack and Gmail searches do not carry work email.

**Why:** an hour of probing produced nothing; the fastest path is the paste.

**How to apply:** when Dallas asks to read an Outlook email, check the pmo register/log for a captured quote, then ask him to paste the body (or authorize Microsoft 365 in claude.ai connector settings). Do not spend the session on store forensics again. Related: [[naveen-1on1-sep8-asks]].
