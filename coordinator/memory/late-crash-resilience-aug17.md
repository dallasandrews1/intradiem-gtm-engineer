---
name: late-crash-resilience-aug17
description: "Aug 17 2026, Monday's six-job failure wave root-caused as connection-closed late in long runs; fixed with incremental-logging contract plus opt-in LATE_RETRY in the 12 log-only wrappers"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e01e1f9-ff0d-4498-81cb-ef1f4061c140
  modified: 2026-08-17T15:35:17.470Z
---

Monday 2026-08-17's failure wave (war-room and gate-integrity dead 75+ min in, four more jobs failed, no logs written) was NOT the [[swarm-blackout-fixed-guarded-shim-aug15]] wake-time class: these were "API Error: Connection closed mid-response" crashes near the END of long runs, so the shim's early-death-only retry correctly did not fire.

Fix shipped same day: (1) `automation/lib/log_resilience.txt`, a prompt contract appended to all 12 log-only wrappers via `$(cat ...)` inside the -p argument: create the dated log FIRST with a "RUN IN PROGRESS" marker, append sections as completed, and if a partial log exists RESUME it rather than restarting; (2) `claude_net.sh` gained a late-death retry gated on `LATE_RETRY=1`, exported only by those same 12 wrappers. Posting jobs (rundown, relay, action brief, thread listener, context bus) intentionally have neither, so a post can never double-fire. Also shipped the thread listener's weekend skip (ledger 08-09 item).

**Why:** two distinct silent-blackout classes existed; the second one wiped 75-minute runs at the finish line.

**How to apply:** a log stuck at "RUN IN PROGRESS" means a partial run; downstream readers must not treat it as clean. Any NEW log-only wrapper gets both LATE_RETRY=1 and the resilience cat-append; any posting wrapper gets neither. Guard-status log lines now include LATE-RETRY entries when the resume path fires.
