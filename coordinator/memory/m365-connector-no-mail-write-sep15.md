---
name: m365-connector-no-mail-write-sep15
description: "Sep 15 2026: the Microsoft 365 connector holds Mail.Read scopes only (no Mail.ReadWrite), so outlook_create_draft / reply drafts fail 403 until an Entra admin grants consent; save Outlook drafts as paste-ready files instead"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1cc96141-e5aa-4bc9-8ae4-2f2c4b818224
  modified: 2026-09-15T14:32:45.327Z
---

Verified Sep 15 2026 on `outlook_create_reply_all_draft`: FORBIDDEN, missing scope Mail.ReadWrite. Granted: Calendars.Read, Mail.Read, Mail.Read.Shared, MailboxItem.Read, Files.Read.All, Sites.Read.All, Chat/Channel read, OnlineMeeting transcript read, User.Read. Tenant 25f5c5af-fa76-4991-8f3b-76ea58be8146, app api://07c030f6-5743-41b7-ba00-0a6e85f37c17.

**How to apply:** any "draft it in Outlook" ask lands as a paste-ready file in the motion folder until IT grants Mail.ReadWrite (Entra admin center, Enterprise applications, the app, Permissions, Grant admin consent). The owner-digest agent's `outlook_draft` route is affected the same way; check it before trusting a "draft created" log line. Related: [[outlook-read-paths-vscode-sep9]].
