---
name: lemlist-relay-unsubscribe-field-fix-sep25
description: "lemlist get_campaigns_stats MCP tool - unsubscribed count lives at messageMetrics.perChannel.others.unsubscribed, not leadMetrics.unsubscribed (which is always 0)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f58b15a-21be-4aaa-958f-27489b2f3cc1
  modified: 2026-09-25T09:13:22.727Z
---

Fixed 2026-09-25 09:12 UTC run of the hourly lemlist-to-Slack relay job (automation/config/lemlist_channels.json, automation/logs/lemlist-relay-*.md): the campaign-stats snapshot (automation/logs/.lemlist-relay-stats.json) was computing each campaign's `unsubscribed` count from `leadMetrics.unsubscribed` in the `get_campaigns_stats` MCP response. That field always returns 0. The real cumulative unsubscribe counter is at `messageMetrics.perChannel.others.unsubscribed`.

**Why:** discovered while diffing this run's fresh pull against the prior snapshot — every campaign's unsubscribed count silently dropped to 0, which is impossible for a monotonic lifetime counter. Traced to the wrong JSON path. Re-pulled with the corrected path and it matched the prior baseline exactly (3 campaigns carrying 1 unsubscribe each), so no unsubscribe deltas were actually missed by earlier runs — but earlier runs' "0 unsubscribe deltas" log claims should be read as unverified on that one metric specifically (bounced, meetingBooked, linkedinInvitationAccepted, and sendFailed were always correctly mapped and unaffected).

**How to apply:** any future code or agent prompt touching lemlist `get_campaigns_stats` for unsubscribe counts must read `messageMetrics.perChannel.others.unsubscribed`, never `leadMetrics.unsubscribed`. The corrected mapping is now baked into `.lemlist-relay-stats.json` going forward (snapshot written 2026-09-25T09:12:42Z). If the lemlist-relay task prompt/instructions are ever rewritten, carry this field path forward explicitly rather than re-deriving it.
