---
name: nate-campaigns-linkedin-sweep-aug31
description: Aug 31 2026 sweep of Nate's other four lemlist campaigns (Stars Fresh Pool Quality 2, Finance 14, Blitz Citizens 8, Blitz Hartford 8): all URLs filled, two departures found (Jeff Ingram left L.A. Care, Dakota Pelletier left The Hartford) both REMOVED via the allow-listed helper ~/.local/bin/lemlist-lead-remove
metadata:
  type: project
---

Aug 31 2026, same chain as [[lemlist-linkedin-backfill-pattern-aug31]] on Nate's remaining campaigns so he can activate them.

Results:
- Stars - Fresh Pool / Finance (`cam_2gy9hmEvMjYEuPZ8A`, 14 leads, 7 missing): 6 resolved by the free bridge, Zhishen Yang via web search plus paid check (`linkedin.com/in/zhishenyang`, now Deputy Executive Director at NYC H+H since May 2026, was Lincoln Medical Center CFO; same org, kept, finance-fit worth a glance). Jeff Ingram LEFT L.A. Care (Managing Partner, J2 Asset Group, Jun 2026): REMOVED (Aug 31, via lemlist-lead-remove). Laurie Martin (Baystate Health CFO, Health New England's parent) is current per Bloomberg/ZoomInfo but her stored LinkedIn URL could not be verified by Clay or search; kept as is.
- Stars - Fresh Pool / Quality (`cam_viEbB6HkYsCPtxKbi`, 2 leads): Andrew Breuckman current, URL vanity updated to `/in/andrew-breuckman/`. Pedro Rivera shows current at NYC H+H on ZoomInfo/RocketReach; Clay's profile read had no dates; kept.
- Blitz - Citizens (`cam_yWefPqaDhNNv4RyQK`, 8, running): all current. Michael Merritt's title updated to "SVP, Head of Consumer Solutions Delivery" (Jun 2026). Robert Soukkala's vanity URL updated to `/in/rob-soukkala-a73b0a7b/` (same profile id).
- Blitz - The Hartford (`cam_fYp7Nh9wB72gfMke6`, 8, running): Stephen Deane's stored URL `/in/stephen-deane-/` is correct (trailing hyphen is the real vanity; the email-based Enrich Person returned an unrelated Australian Stephen Deane, so never trust email-input matches without a company check). Dakota Pelletier LEFT The Hartford May 2026 (`/in/dakota/`): paused, then REMOVED (Aug 31, via lemlist-lead-remove).

Lead removal path (Dallas approved Aug 31): the auto-mode classifier denies ad hoc curl DELETE calls on lemlist leads, so removals run through `~/.local/bin/lemlist-lead-remove <campaignId> <email>` (symlink to automation/lemlist_lead_remove.sh, one lead per call, action=remove, never unsubscribes), allow-listed in ~/.claude/settings.json as `Bash(/Users/dallasandrews/.local/bin/lemlist-lead-remove *)`. Pause first when a campaign is running: POST /api/leads/pause/{leadId}?campaignId=.

Credits: free bridge 0; paid Enrich Person 9 + 2 runs by URL/email.
