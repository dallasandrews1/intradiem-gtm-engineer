---
name: outlook-read-paths-vscode-sep9
description: Sep 9 2026 - the M365 connector can show as unauthorized mid-session; after a session resume it worked (Sep 10). New Outlook has no AppleScript message access and headless claude -p shares the auth state. Retry the connector first, then ask Dallas to paste
metadata:
  type: project
---

Tried Sep 9 2026 while asked to read a Naveen email: the claude.ai Microsoft 365 connector is unauthorized in VS Code and CLI sessions (only the scheduled pmo-action-extractor job has read it, and today's run logged email 0); New Outlook for Mac returns 0 messages to AppleScript and stores mail in the proprietary HxStore.hxd (4 MB, no plain text); a headless `claude -p` call with the M365 tools returns the same unauthenticated message; Slack and Gmail searches do not carry work email.

**Why:** an hour of probing produced nothing; the fastest path is the paste.

**How to apply:** when the M365 tools are missing, load them with ToolSearch first (they reappeared after the Sep 10 resume and read the whole thread). If still unauthorized, check the pmo register/log for a captured quote, then ask him to paste. Never spend a session on store forensics. Long thread bodies overflow the tool result; slice the saved file with python and cut at the first quoted-message marker. Related: [[naveen-1on1-sep8-asks]].
