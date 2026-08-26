#!/bin/zsh
# claude_net.sh — drop-in replacement for the bare claude binary in run_*.sh wrappers.
# Ships the ledger's #1 open proposal (guarded_claude rollout, 2026-08-11) as a shim:
# every wrapper swaps its claude path for this file and gets, with no other change:
#   1. Wait-for-network: polls DNS for api.anthropic.com up to 10 min before launching.
#      (The Aug 10 + Aug 12-15 blackouts were ENOTFOUND at fire time — the Mac's network
#      wasn't up yet when launchd fired. A bare retry loses that race too; waiting wins it.)
#   2. Early-death retry: if the run exits nonzero in under EARLY_DEATH_SECS, it almost
#      certainly died before doing anything (transient API/DNS failure), so re-run once.
#      Long runs that fail are NOT retried — a job that already posted a DM or wrote a
#      log must never fire twice.
#   3. A PASS/FAIL line per attempt to _job_guard_status.log so swarm-health's output
#      integrity section finally has data.
# Never changes the prompt, never messages anyone, never loops more than one retry.

CLAUDE_BIN="${CLAUDE_BIN:-/Users/dallasandrews/.local/bin/claude}"
GUARD_STATUS="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/logs/_job_guard_status.log"
EARLY_DEATH_SECS="${EARLY_DEATH_SECS:-300}"
NET_WAIT_TRIES="${NET_WAIT_TRIES:-40}"   # 40 x 15s = 10 min max wait

# Best-effort name of the wrapper that invoked us, for the status log.
_job_name() {
  local parent
  parent="$(ps -p $PPID -o command= 2>/dev/null | grep -oE 'run_[a-z_]+\.sh' | head -1)"
  print -r -- "${GUARD_JOB:-${parent:-unknown-job}}"
}

_wait_for_network() {
  local i
  for i in {1..$NET_WAIT_TRIES}; do
    if /usr/bin/nslookup -timeout=3 api.anthropic.com >/dev/null 2>&1; then
      return 0
    fi
    sleep 15
  done
  return 1
}

job="$(_job_name)"

if ! _wait_for_network; then
  print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] FAIL ${job} network-never-came-up-after-10min" >> "$GUARD_STATUS"
  # Fall through and attempt anyway — claude's own error lands in the job's out file.
fi

start=$(date +%s)
"$CLAUDE_BIN" "$@"
rc=$?
dur=$(( $(date +%s) - start ))

# Late-death retry is OPT-IN via LATE_RETRY=1, set only by wrappers whose jobs write
# logs and never post (war room, audits, watchers). Jobs that DM or post to channels
# must never late-retry: a run that dies after its post would post twice. Safe jobs
# pair this with the incremental-logging contract (lib/log_resilience.txt), so the
# retry RESUMES a partial log instead of redoing the whole run.
if [[ $rc -ne 0 && ( $dur -lt $EARLY_DEATH_SECS || "${LATE_RETRY:-0}" == "1" ) ]]; then
  if [[ $dur -lt $EARLY_DEATH_SECS ]]; then
    print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] RETRY ${job} rc=${rc} died-early-after-${dur}s, waiting for network and re-running once" >> "$GUARD_STATUS"
  else
    print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] LATE-RETRY ${job} rc=${rc} died-late-after-${dur}s, log-only job, resuming once" >> "$GUARD_STATUS"
  fi
  _wait_for_network
  sleep 20
  start=$(date +%s)
  "$CLAUDE_BIN" "$@"
  rc=$?
  dur=$(( $(date +%s) - start ))
fi

if [[ $rc -eq 0 ]]; then
  print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] PASS ${job} rc=0 dur=${dur}s" >> "$GUARD_STATUS"
else
  print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] FAIL ${job} rc=${rc} dur=${dur}s" >> "$GUARD_STATUS"
fi
exit $rc
