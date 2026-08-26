#!/bin/zsh
# job_guard.sh — shared reliability layer for the scheduled swarm.
# Consolidates four proposals into one place: job-output-integrity (2026-07-22),
# transient-api-failure-auto-retry (2026-07-28), rundown-completion-watchdog (2026-07-28),
# job-hang-watchdog (2026-08-04). See automation/logs/proposal-triage-2026-08-06.md.
#
# Usage inside a run_*.sh wrapper:
#
#   source "$(dirname "$0")/lib/job_guard.sh"
#   guarded_claude "<job-name>" "<expected-output-glob>" "<raw-out-file>" "$PROMPT"
#
# Behaviour:
#   1. Runs the claude -p call once, appending to the raw out file.
#   2. If the run died on a transient API failure AND the expected dated output is
#      still missing, re-runs the SAME prompt exactly once, stamped [RETRY].
#   3. Asserts the expected dated output landed and is non-empty; writes a single
#      PASS/FAIL line to automation/logs/_job_guard_status.log for the heartbeat.
#
# It never changes the prompt, never runs a different action, never messages anyone.
# If the retry also fails it gives up and records FAIL, so the failure stays visible
# rather than looping.

CLAUDE_BIN="${CLAUDE_BIN:-/Users/dallasandrews/.local/bin/claude}"
CLAUDE_MODEL="${CLAUDE_MODEL:-claude-sonnet-5}"
GUARD_STATUS="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/logs/_job_guard_status.log"

# Signatures that mean "the session died mid-flight", not "the job ran and found nothing".
_guard_is_transient_failure() {
  local outfile="$1"
  [[ -f "$outfile" ]] || return 1
  tail -40 "$outfile" 2>/dev/null | grep -qE 'API Error|Connection closed|Connection error|stream disconnected|Traceback \(most recent call last\)'
}

# Did the job actually produce its dated artifact, non-empty?
_guard_output_landed() {
  local glob="$1"
  local newest
  newest="$(ls -t ${~glob} 2>/dev/null | head -1)"
  [[ -n "$newest" && -s "$newest" ]]
}

guarded_claude() {
  local job="$1" expected_glob="$2" outfile="$3" prompt="$4"
  local stamp attempt=1

  "$CLAUDE_BIN" --model "$CLAUDE_MODEL" -p "$prompt" --dangerously-skip-permissions >> "$outfile" 2>&1
  local rc=$?

  if ! _guard_output_landed "$expected_glob"; then
    if _guard_is_transient_failure "$outfile" || [[ $rc -ne 0 ]]; then
      attempt=2
      print -r -- "[RETRY] $(date '+%Y-%m-%d %H:%M:%S') ${job}: first attempt rc=${rc}, no output landed, re-running once." >> "$outfile"
      "$CLAUDE_BIN" --model "$CLAUDE_MODEL" -p "$prompt" --dangerously-skip-permissions >> "$outfile" 2>&1
      rc=$?
    fi
  fi

  stamp="$(date '+%Y-%m-%d %H:%M:%S')"
  if _guard_output_landed "$expected_glob"; then
    print -r -- "[${stamp}] PASS ${job} rc=${rc} attempts=${attempt}" >> "$GUARD_STATUS"
  else
    print -r -- "[${stamp}] FAIL ${job} rc=${rc} attempts=${attempt} no-output-matching:${expected_glob}" >> "$GUARD_STATUS"
  fi
  return $rc
}
