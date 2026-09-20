---
name: keegan-package-refresh-sep20
description: "Sep 20 2026: review of the package Keegan was sent Sep 18 and the refresh that brings the execution kit and the Product roadmap into his index, rooms and self-serve libraries; deployed Sep 20; Keegan asked for a walkthrough with Nate on his weekly call"
metadata:
  type: project
---

**Context:** Keegan was sent the four-piece package in Slack on Sep 18 2026 at 04:23 CT (index + maps, room, brief, one-pager per account). He replied the same morning asking Dallas to join his weekly call with Nate the following week and walk them through it; Dallas said yes. The execution kit, proof tiles, sales kit refresh and EH kit all landed AFTER that message, so the index he holds showed none of it.

**Built Sep 20 2026, DEPLOYED Sep 20 2026 on Dallas's go (save-rooms dcd2e6ea, backoffice-maps 5fae863a; 4 of 4 cache-busted samples byte-identical on all four pages; 0 credits):**
- `motions/keegan/accounts/roadmap_fit.py`: BOO, QO, EH mapped to each account's routes, availability, kit links. Every "why" restates a room fact; route ids asserted against plans.py. Injected by `build_rooms.py` as an optional `#roadmap` section (same opt-in pattern as the selector). Room diff vs live is additive only. No dated moves added to plans.py.
- `build_keegan_index.py`: Execution kit row per card (sequence, what to send when + page count from shelf_manifest.json, roadmap fit), 25 one-pagers stat, sales kits strip. Note the manifest's `pages` list already counts the account one-pager (8, 9, 8).
- `selfserve/export_library.py`: a roadmap fit block per library, call prep only, "why" text left out because it carries CRM reads. check PASS. Project still not uploaded.

**Useful fact for net-new AEs:** the BOO beta is open to a new logo purchasing two or more Contact Center Automation solutions (BOO kit, beta terms), so a prospect account can reach the Q4 2026 beta.

**Blitz state, real read Sep 20 2026:** all 15 manual LinkedIn invite tasks are STILL pending in Nathan's queue (Citizens 8, Hartford 7), 0 invites sent, nothing has fired since Aug 7. The lemlist-pulse job's "0 open tasks" for these campaigns is false. Open tracking is not configured (custom tracking domain waiting on IT), so 0 opens means nothing on these campaigns. The Citizens LEAD rows still read adt.com (Bartolazo), voya.com (Weaver), stale titles and Foss's switchboard number with no LinkedIn URL, although the Sep 18 log recorded them fixed and re-read. RESOLVED Sep 20: re-corrected and proven by re-read; the reversion was the Salesforce sync, see [[lemlist-salesforce-sync-overwrites-lead-fixes]]; Blitz - Citizens left paused. Order trap: correct the lead rows BEFORE Nathan clears the invites, or the next emails go to the wrong companies. Log: `automation/logs/keegan-package-refresh-2026-09-20.md`.

Related: [[keegan-three-account-package-sep17]], [[keegan-execution-kit-sep18]], [[sales-kits-roadmap-refresh-sep18]], [[ae-selfserve-project-sep18]].
