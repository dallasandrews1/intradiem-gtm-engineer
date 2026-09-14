#!/bin/zsh
# Swarm heartbeat: confirms each scheduled job actually fired and its log landed. Pure bash, no LLM.
# Launched by com.dallasandrews.gtm.swarmheartbeat at 7:45 weekdays, just before the daily rundown (7:50),
# so the rundown can lead with swarm health. Writes a log the rundown reads; never DMs anyone.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation"

TODAY="$(date +%Y-%m-%d)"
NOW="$(date +%H:%M)"
UID_="$(id -u)"
OUT="logs/swarm-health-${TODAY}.md"

{
  echo "# Swarm health ${TODAY} ${NOW}"
  echo ""
  echo "## Loaded jobs (runs = lifetime fire count)"
  for j in warroom meetingcapture tablehygiene agentarchitect gateintegrity pipelinereceipts creditcheck fridayreadout deliverabilitywatch competitorwatch starsrefreshwatch swarmheartbeat rundownthreads alumniwatch lemlistrelay contextbus; do
    lbl="com.dallasandrews.gtm.${j}"
    runs="$(launchctl print gui/${UID_}/${lbl} 2>/dev/null | awk -F'= ' '/[[:space:]]runs =/{gsub(/ /,"",$2); print $2; exit}')"
    if [ -z "$runs" ]; then
      echo "- ${lbl}: NOT LOADED"
    else
      echo "- ${lbl}: runs=${runs}"
    fi
  done
  echo ""
  echo "## Today's expected upstream logs (checked at ${NOW}, before the rundown)"
  for f in "war-room-${TODAY}.md" "agent-architect-${TODAY}.md" "meeting-capture-${TODAY}.md"; do
    if [ -f "logs/${f}" ]; then echo "- OK: ${f}"; else echo "- MISSING: ${f}"; fi
  done
  echo ""
  echo ""
  echo "## Job exit status + hang check"
  for j in warroom meetingcapture tablehygiene agentarchitect gateintegrity pipelinereceipts creditcheck fridayreadout deliverabilitywatch competitorwatch starsrefreshwatch rundownthreads alumniwatch lemlistrelay contextbus; do
    lbl="com.dallasandrews.gtm.${j}"
    pr="$(launchctl print gui/${UID_}/${lbl} 2>/dev/null)"
    [ -z "$pr" ] && continue
    code="$(printf '%s' "$pr" | awk -F'= ' '/last exit code =/{gsub(/ /,"",$2); print $2; exit}')"
    st="$(printf '%s' "$pr" | awk -F'= ' '/^[[:space:]]*state =/{gsub(/^ +| +$/,"",$2); print $2; exit}')"
    case "$code" in
      0|"(neverexited)"|"(never exited)"|"") : ;;
      *) echo "- FAIL: ${lbl} last exit code = ${code}" ;;
    esac
    case "$pr" in *"penalty box"*) echo "- THROTTLED: ${lbl} in launchd penalty box (will not fire until reset)";; esac
    [ "$st" = "running" ] && echo "- STILL RUNNING: ${lbl} at ${NOW}"
  done

  echo ""
  echo "## Output integrity (job_guard)"
  if [ -f logs/_job_guard_status.log ]; then
    grep "^\[${TODAY}" logs/_job_guard_status.log | grep "FAIL" | sed 's/^/- /' || echo "- no guard FAILs recorded today"
  else
    echo "- guard status log not yet written (job_guard.sh not wired into wrappers yet)"
  fi

  # Three-way reconciliation, widened 2026-08-07.
  # This check used to walk ONE direction only: loaded -> AGENT_REGISTRY.md. So it reported
  # "no drift" on 2026-08-06 while three jobs were actually out of sync: alumniwatch was
  # loaded and running with no plist versioned in the repo, and actionbrief and controltower
  # were versioned in the repo but never loaded. A job that is running but not in source
  # control cannot be reviewed or restored; a job that is in source control but not running
  # is silently doing nothing. Both are invisible to a one-way check.
  echo ""
  echo "## Swarm drift (repo plists vs LaunchAgents vs launchd vs registry)"
  REG="/Users/dallasandrews/coordinator/AGENT_REGISTRY.md"
  REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
  LA_DIR="${HOME}/Library/LaunchAgents"
  drift=0

  # Must be space-safe: the repo path contains spaces ("Intradiem GTM Engineer"), so any
  # pipeline through xargs/word-splitting invents bogus labels ("GTM", "Intradiem").
  labels_in() {
    local d="$1" f b
    for f in "$d"/com.dallasandrews.gtm.*.plist; do
      [ -e "$f" ] || continue
      b="${f##*/}"
      printf '%s\n' "${b%.plist}"
    done
  }
  REPO_LBLS="$(labels_in "$REPO_DIR")"
  LA_LBLS="$(labels_in "$LA_DIR")"
  LOADED_LBLS="$(launchctl list | awk '/com\.dallasandrews\.gtm\./{print $3}')"
  ALL_LBLS="$(printf '%s\n%s\n%s\n' "$REPO_LBLS" "$LA_LBLS" "$LOADED_LBLS" | sed '/^$/d' | sort -u)"

  # ${(f)...} splits on newlines: zsh does NOT word-split a bare $ALL_LBLS, so the old
  # loop ran ONCE with every label glued into one string, diffed a nonexistent multiline
  # filename, and printed a single false OUT-OF-SYNC naming every job (seen 8/14).
  for lbl in ${(f)ALL_LBLS}; do
    short="${lbl##*.}"
    in_repo=0; in_la=0; in_loaded=0
    printf '%s\n' "$REPO_LBLS"   | grep -qx "$lbl" && in_repo=1
    printf '%s\n' "$LA_LBLS"     | grep -qx "$lbl" && in_la=1
    printf '%s\n' "$LOADED_LBLS" | grep -qx "$lbl" && in_loaded=1

    if [ "$in_loaded" -eq 1 ] && [ "$in_repo" -eq 0 ]; then
      echo "- UNVERSIONED: ${lbl} is loaded and running but has no plist in the repo. It cannot be reviewed or restored."
      drift=1
    fi
    staged=0
    [ -f "${REPO_DIR}/config/staged_jobs.txt" ] && grep -v '^#' "${REPO_DIR}/config/staged_jobs.txt" | grep -qx "$lbl" && staged=1
    if [ "$staged" -eq 1 ] && [ "$in_loaded" -eq 0 ]; then
      echo "- STAGED (by design, config/staged_jobs.txt): ${lbl} is not loaded; load on Dallas's word."
    fi
    if [ "$in_repo" -eq 1 ] && [ "$in_loaded" -eq 0 ] && [ "$staged" -eq 0 ]; then
      echo "- DORMANT: ${lbl} is versioned in the repo but is NOT loaded. It is doing nothing."
      drift=1
    fi
    if [ "$in_la" -eq 1 ] && [ "$in_loaded" -eq 0 ] && [ "$staged" -eq 0 ]; then
      echo "- INSTALLED BUT NOT LOADED: ${lbl} plist is in LaunchAgents but launchd is not running it."
      drift=1
    fi
    if [ "$in_repo" -eq 1 ] && [ "$in_la" -eq 1 ] && ! diff -q "${REPO_DIR}/${lbl}.plist" "${LA_DIR}/${lbl}.plist" >/dev/null 2>&1; then
      echo "- OUT OF SYNC: ${lbl} repo plist and the installed LaunchAgents plist differ. The running schedule is not the reviewed one."
      drift=1
    fi
    if [ "$in_loaded" -eq 1 ] && [ -f "$REG" ] && ! grep -q "gtm\.${short}" "$REG"; then
      echo "- UNDOCUMENTED: ${lbl} loaded but absent from AGENT_REGISTRY.md"
      drift=1
    fi
  done

  [ ! -f "$REG" ] && echo "- registry not found at ${REG} (documentation check skipped)"
  if [ "$drift" -eq 0 ]; then
    n_repo=$(printf '%s\n' "$REPO_LBLS" | sed '/^$/d' | wc -l | tr -d ' ')
    n_loaded=$(printf '%s\n' "$LOADED_LBLS" | sed '/^$/d' | wc -l | tr -d ' ')
    echo "- no drift: ${n_loaded} loaded, ${n_repo} versioned, all four views agree"
  fi

  echo ""
  echo "_Heartbeat runs at 7:45; the rundown (7:50) and any Thu/Fri/weekly jobs are not expected in this check._"
} > "${OUT}"
