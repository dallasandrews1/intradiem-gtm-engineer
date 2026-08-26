---
name: swarm-blackout-fixed-guarded-shim-aug15
description: "Aug 12-15 swarm blackout root-caused (ENOTFOUND at launchd fire time, network not up after wake) and fixed Aug 15 2026 via automation/lib/claude_net.sh shim wired into all 18 run_*.sh wrappers"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e01e1f9-ff0d-4498-81cb-ef1f4061c140
  modified: 2026-08-16T03:23:50.978Z
---

The Aug 12-15 2026 swarm blackout (every claude-based launchd job exiting 1, rundown silent since Aug 11, see [[rundown-job-outage-since-aug11]]) was root-caused on 2026-08-15: `API Error: Unable to connect to API (ENOTFOUND)` at fire time. launchd fires the early-morning jobs when the Mac wakes, before Wi-Fi/DNS is back up, so the bare `claude -p` call dies instantly and a naive immediate retry loses the same race.

Fixed same day: `automation/lib/claude_net.sh` is a drop-in shim now called instead of the bare claude binary by all 18 `run_*.sh` wrappers. It waits up to 10 min for DNS on api.anthropic.com, retries once only on early death (nonzero exit in under 5 min, so a job that already posted a DM can never fire twice), and writes PASS/FAIL lines to `automation/logs/_job_guard_status.log`. This shipped the proposal ledger's #1 open item (guarded_claude rollout, specced 08-11). Smoke-tested PASS; first live proof is the catch-up war-room run launched that evening.

**Why:** the swarm's reliability was the gating factor on everything else; five separate outage days (Aug 10, Aug 12-15) traced to this one failure class.

**How to apply:** if a job still blackouts after this, check `_job_guard_status.log` first: a FAIL line means the shim ran and the failure is real (new class, investigate); no line at all means launchd never fired the wrapper (schedule/load problem, check `launchctl list`). Any NEW run_*.sh wrapper must call the shim path, never the bare claude binary. The swarm-health "repo plist vs installed plist drift" check reported false positives on 08-14 (warroom plists diff clean); treat its drift section as suspect until its comparison is fixed.
