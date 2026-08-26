---
name: lemlist-relay-wiring-jul31
description: Lemlist-to-Slack rep-channel relay - hourly 24/7, silent on empty; as of Aug 1 LIVE in CANARY MODE with both routes pointed at Dallas's private #relay-test (C0BM86CV138), rep channel ids parked in rep_channels_at_launch for the launch swap
metadata:
  type: project
---

**Aug 1 2026 update, CANARY MODE:** Dallas asked to route everything to his test channel first. Config now: `live: true`, both nathan and jack routes point at his private #relay-test (C0BM86CV138), the real rep channel ids are parked in a `rep_channels_at_launch` field, and Jack's new campaign cam_nwKASgttBM6QT8XGq maps to the jack route. Launch handoff = restore the two ids from rep_channels_at_launch and delete that field, one edit. `live: false` stays the kill switch. Silence-on-empty is now PROVEN in production: five-plus quiet hourly cycles logged Aug 1, one log line each, zero Slack posts. Still unproven: message composition and the headless Slack post itself (zero lemlist activity exists until campaigns start); the canary window covers exactly that on launch day.

Jul 31 2026. The two rep channels are live and posted to: #gtm-outbound-nathan (C0BM9V6KGSG) and #gtm-outbound-jack (C0BN0JT9D6U), both private, members are Dallas + the rep + Naveen, and Matt Rumins in Jack's. Kickoff posts sent Jul 31 5:28pm and 5:31pm. Both posts promise the reps that Lemlist activity lands in the channel automatically, so the relay is now a commitment in front of Naveen and Matt.

**Relay state:**
- `com.dallasandrews.gtm.lemlistrelay.plist` installed in ~/Library/LaunchAgents and bootstrapped. Schedule is hourly at :10, every hour, every day (StartCalendarInterval with Minute only). 24/7 by Dallas's call Jul 31, because Jack's UK hours are overnight US.
- Dry run Jul 31 completed clean, exit 0: "no new events". Nothing to compose from, all three Stars campaigns are still Draft with zero Lemlist activity.
- Still `live: false` in automation/config/lemlist_channels.json. That flag is the nobody-but-Dallas posting gate; it needs an explicit ask to flip.
- Jack's channel has no campaign mapped. All three campaign IDs route to nathan, so his channel stays silent until his Europe campaign exists.

**Two rules Dallas set Jul 31:** the job runs hourly 24/7, and it posts NOTHING to a channel on a run with no new events for that channel. No heartbeats, no "all quiet", no standalone task digest. The open-task digest is ride-along only, appended to a channel that is already getting a real event message, because open tasks persist for days and a standalone digest would repeat hourly and train the reps to ignore the channel. Quiet runs are recorded only in automation/logs/.

**API gotcha, verified live Jul 31:** Lemlist `GET /api/tasks` requires a `filters` query param holding a URL-encoded JSON array. A bare call returns `{"error":"Malformed filters"}` on every variant. Use `?filters=%5B%5D` for no filter. The job was silently falling back to an MCP tool to cover for this; the correct call is now in run_lemlist_relay.sh.

**Unproven:** message composition (no activity has ever existed) and whether the headless `claude -p` run can actually post to Slack. The unattended run DID reach a Lemlist MCP connector on its own, which is a good sign for connectors loading headless, but Slack posting specifically has never been attempted. Related: [[lemlist-trial-build-jul31]], [[lemlist-trial-gameplan-jul31]], [[registry-reconciled-jul27]].
