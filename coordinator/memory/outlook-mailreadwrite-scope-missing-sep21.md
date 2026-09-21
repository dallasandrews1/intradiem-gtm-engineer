---
name: outlook-mailreadwrite-scope-missing-sep21
description: "Outlook connector lacks Mail.ReadWrite scope, blocking all outlook_create_draft calls (owner-digest and any other drafting job) until Entra admin consent is granted"
metadata: 
  node_type: memory
  type: project
  originSessionId: cd561fa2-dcb0-412b-bf95-bbcb7df91561
  modified: 2026-09-21T12:32:05.107Z
---

The Microsoft 365/Outlook MCP connector currently has only `Mail.Read`-family scopes, not `Mail.ReadWrite`. Any call to `outlook_create_draft` (or similar write calls) returns a 403 `FORBIDDEN: Missing scope 'Mail.ReadWrite'` for dallas.andrews@Intradiem.com.

**Why:** Discovered Sep 21 2026 during the scheduled owner-digest run (see [[owner-digest-outlook-drafts]] if that memory exists) — the run got through composing the digest and confirming Inger Escamilla's address, but every draft-creation attempt failed on this scope gap. Logged at `automation/logs/owner-digest-2026-09-21.md`, anchor `evt: owner-digest-2026-09-21#outlook-mail-readwrite-scope`.

**How to apply:** This blocks EVERY job that tries to create/update Outlook drafts, not just owner-digest, until someone with Entra admin rights grants `Mail.ReadWrite` consent (Entra portal > Enterprise applications > this app > Permissions > Grant admin consent). Until that happens, expect any Outlook-draft-creating agent run to log a BLOCKED-OUTLOOK line and finish with 0 drafts created — that is the correct/expected behavior given the scope gap, not a bug in the agent. Flag this to Dallas as an admin action item rather than re-debugging the agent logic.
