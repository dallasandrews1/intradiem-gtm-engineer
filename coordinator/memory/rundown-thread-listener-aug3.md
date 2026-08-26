---
name: rundown-thread-listener-aug3
description: "Rundown DM threads are two-way as of Aug 3 2026: a 10-min launchd listener (com.dallasandrews.gtm.rundownthreads) reads Dallas's replies under the daily rundown DM and acts with coordinator context; CONFIRM loop for credit-spending actions, send gates stay hand-only"
metadata:
  type: project
---

Built Aug 3 2026 so Dallas can reply to his GTM Daily Rundown DM thread and have Claude act on items. Same chassis as the hourly Lemlist relay's thread ingest (proven that the claude.ai Slack MCP reads/posts threads headlessly).

Pieces, all in `~/Claude/Projects/Intradiem GTM Engineer/automation/`:
- `run_rundown_thread_listener.sh`: headless `claude -p` (sonnet), polls every 10 min via `com.dallasandrews.gtm.rundownthreads.plist` (StartInterval 600), quiet hours 22:00-07:00 gated in shell so overnight polls cost nothing. Silence on empty.
- `run_daily_rundown.sh` (edited): after sending the DM it appends {date, channel, ts} to `automation/logs/rundown-dm-pointer.json`, ends the DM with "Reply in this thread...", and reads `rundown-thread-<recent>.md` plus pending confirms next morning.
- State: `automation/config/rundown_thread_state.json` (processed_reply_ts, pending_confirms). Log: `automation/logs/rundown-thread-<date>.md`.

Permission tiers baked into the listener prompt: reads/analysis/drafts run directly; anything spending Clay credits or mutating Clay/Apollo/Lemlist needs an in-thread "CONFIRM <tag>" loop (48h expiry); send-gate flips, wave loads, campaign edits, deletes, and skill/permission edits are NEVER done from the thread even with CONFIRM (reply hands Dallas steps or a copy-paste prompt instead). Replies only ever land in the existing thread, never a new DM (single-morning-brief rule holds).

Install was handed to Dallas per [[classifier-blocks-unattended-automation]] (chmod +x + cp plist + launchctl). Confirm with him it's loaded before assuming live. Heartbeat job list includes rundownthreads. Rejected alternatives: Claude Tag in Slack (no coordinator memory/skills/MCP wiring), Slack Events API + Cloudflare Worker (real-time but needs a custom Slack app; noted as phase 2 if 10-min polling feels slow).
