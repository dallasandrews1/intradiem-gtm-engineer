---
name: lemlist-relay-dual-surface-staleness-sep15
description: "FIXED Sep 15 2026: the lemlist-relay job's MCP and REST surfaces minted different ids for the same event, so seen_activity_ids could not dedup across them; canonical cross-surface ids plus a stale-snapshot protocol are now in the job prompt"
metadata:
  node_type: memory
  type: project
---

The lemlist-to-Slack relay (`automation/run_lemlist_relay.sh`, hourly, live=true) has two independent activity surfaces: MCP (`get_campaigns_stats`, diffed against `automation/logs/.lemlist-relay-stats.json`) and a REST fallback (`/api/activities`) used when the MCP tools do not load that hour. Two defects compounded on 2026-09-15.

**Root cause (the real one):** the surfaces minted DIFFERENT ids for the SAME event. A REST run recorded Babeth Schaart's VodafoneZiggo bounce as `act_RL45H67iyamCAnLLR`; the MCP run had recorded it as `bounce|cam_kDgZw2b6ixJ8AJKrR|lea_KiDAhJdJg97a7fzTq|2026-09-15`. Two namespaces that never collide, so `seen_activity_ids` could not dedup across surfaces.

**Second defect (staleness):** a REST-only run cannot refresh the stats snapshot (REST exposes no equivalent aggregate), so the next MCP run diffed against a baseline one event behind and saw an already-posted bounce as new. Hit twice on Sep 15: Babeth at 10:52Z, Kevin Van Stijn (Nationale-Nederlanden, `lea_bHz2YiWqTjfD98Act`) at 14:14Z.

**What actually leaked:** nothing. No duplicate ever reached #gtm-outbound-jack. But each false positive cost a full forensic sweep (all 72 leads across two pages, plus full Slack channel history) to prove it was a repeat, every hour, on a job that runs 24/7.

**Fix, in the job prompt Sep 15 2026:**
- **Canonical event id** `<type>|<campaignId>|<leadId>|<YYYY-MM-DD>` (type: bounce, unsub, li_accept, meeting, send_fail) that BOTH surfaces can construct. Before posting anything, check the canonical id AND the native `act_*` id; a hit on either means already posted. Replies keep `<conversationId>|<lastMessageDate>`.
- **Write both ids** for every non-reply event, and backfill the missing half whenever a reconciliation matches on one namespace only.
- **Stale-snapshot protocol:** a REST-only run sets `"stale": true` on the snapshot, leaves the counts untouched, and appends what it posted to `"pending_canonical_ids"`. The next MCP run checks that list FIRST and only sweeps campaign leads for a delta the list does not explain. An MCP run writes fresh counts, clears the flag, and empties the list.
- Backfilled `bounce|cam_kDgZw2b6ixJ8AJKrR|lea_bHz2YiWqTjfD98Act|2026-09-15` (Kevin, REST-only until now) so both Sep 15 bounces carry a complete id pair. Snapshot seeded `stale: false`, `pending_canonical_ids: []`. Backups: `automation/run_lemlist_relay.sh.bak_sep15`, `automation/config/lemlist_channels.json.bak_sep15`.

**Log misread to ignore:** the 15:15Z run called both bounce activities `jack.ohagan@intradiemhq.com`, "an internal seed address, not a real lead". That is the SENDER on the activity record. The leads are Babeth Schaart and Kevin Van Stijn, both real, both correctly posted.

**How to apply:** any relay surface added later must construct the canonical id too, or it reintroduces the same split. Verify the fix on the first REST-fallback hour: the snapshot should go stale with a populated `pending_canonical_ids`, and the next MCP run should absorb the delta with a one-line reconciliation and no lead sweep. Related: [[bo-copy-c-autopilot-sep15]], [[gtm-engine-review-sep13]].
