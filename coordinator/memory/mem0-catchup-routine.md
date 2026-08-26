---
name: mem0-catchup-routine
description: "Daily cloud routine 'intradiem-mem0-catchup' (trig_01Ho4bZLRiE15M4xkyga5QWu) checks Mem0 daily at 6am CT for 48h of silence and Slacks Dallas if sync has gone quiet"
metadata:
  node_type: memory
  type: reference
  originSessionId: 070cc632-174f-4c32-b9d7-50f80b21e0e6
---

Created Jul 17 2026 as the automated backstop for [[mem0-sync-gap-jul17]]. Runs daily at 6am America/Chicago (`0 11 * * *` UTC) as a Claude Code cloud routine (id `trig_01Ho4bZLRiE15M4xkyga5QWu`, https://claude.ai/code/routines/trig_01Ho4bZLRiE15M4xkyga5QWu).

**What it does:** queries Mem0 (user_id=dallasandrews, app_id=coordinator) for any memory created in the last 48 hours. If there's at least one, it exits quietly. If there are zero, it sends Dallas a Slack message flagging the silence and suggesting a manual catch-up.

**What it deliberately does NOT do:** it cannot read local files (no GitHub remote exists for either the coordinator or Intradiem GTM Engineer project, so a cloud routine can't clone them) and does not attempt to auto-distill or write memories itself — it only detects and alerts. A real catch-up still requires a session with local file access (like this one) to read what actually changed and write the memory files.

**How to apply:** if the Slack alert fires, don't dismiss it — it means Mem0 has been quiet for 2 days, which is exactly the failure mode that let a full week of work go uncaptured. Run a manual catch-up (read recent project files, distill, sync) rather than assuming it's a false alarm.
