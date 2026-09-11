#!/bin/bash
# Drains the "CC Platforms: needs read" segment through the PredictLeads tech-stack
# workflow, 10 companies per batch (the CLI's hard cap). 1 credit per company.
#
# Three guards, each earned on the Sep 5 run:
#  1. kicks retry through Clay's transient server_errors instead of aborting
#  2. a batch must SETTLE before the next kick. Kicking on the first flicker of
#     movement re-sends rows still in flight (~10% duplicate reads on run 1).
#  3. Clay's dispatch slows under load: batches ran 22s early and 6min late. So a
#     quiet batch is NOT fatal. Only three consecutive zero-progress batches stop
#     the loop, which is also how it exits on rows PredictLeads rejects outright
#     ("This domain is invalid" fails before the write node, so they never drain).
set -u
WF=wf_0tkv9u0BKvNYsV4NsQx
SEG=audseg_0tkv9vq4SZBjZdJuiYi
LOG="$(cd "$(dirname "$0")" && pwd)/data/cc_platform_backfill_sep5.log"
MAX_BATCHES=${MAX_BATCHES:-250}
BATCH=10
POLL=30
MAX_WAIT_POLLS=26        # ~13 min per batch before we move on
STABLE_NEEDED=3
DEAD_BATCHES=3           # consecutive no-progress batches before giving up
KICK_RETRIES=6

count() { clay audiences records search-count --entity-type companies --audience-id $SEG 2>/dev/null \
          | python3 -c "import json,sys;print(json.load(sys.stdin).get('count','ERR'))" 2>/dev/null; }

kick() {
  local try=0 res backoff=10
  while [ $try -lt $KICK_RETRIES ]; do
    res=$(clay workflows runs test $WF --audience-segment $SEG --limit $BATCH 2>&1)
    if echo "$res" | grep -q '"ok": *true'; then return 0; fi
    try=$((try+1))
    echo "$(date '+%F %T')  retry  kick $try/$KICK_RETRIES: $(echo "$res" | tr -d '\n' | cut -c1-160)" | tee -a "$LOG"
    sleep $backoff; backoff=$((backoff*2))
  done
  return 1
}

START=$(count)
echo "$(date '+%F %T')  START  queue=$START  max_batches=$MAX_BATCHES" | tee -a "$LOG"
DEAD=0

for b in $(seq 1 $MAX_BATCHES); do
  BEFORE=$(count)
  case "$BEFORE" in ''|*[!0-9]*) echo "$(date '+%F %T')  ABORT  count unreadable ($BEFORE)" | tee -a "$LOG"; exit 1;; esac
  if [ "$BEFORE" -eq 0 ]; then
    echo "$(date '+%F %T')  DONE   queue empty after $((b-1)) batches" | tee -a "$LOG"; break
  fi

  if ! kick; then
    echo "$(date '+%F %T')  ABORT  batch $b: kick failed $KICK_RETRIES times, queue=$BEFORE" | tee -a "$LOG"; exit 1
  fi

  WAITED=0; STABLE=0; LAST=$BEFORE
  while [ $WAITED -lt $MAX_WAIT_POLLS ]; do
    sleep $POLL; WAITED=$((WAITED+1))
    NOW=$(count)
    case "$NOW" in ''|*[!0-9]*) NOW=$LAST;; esac
    if [ "$NOW" -eq "$LAST" ]; then STABLE=$((STABLE+1)); else STABLE=0; LAST=$NOW; fi
    [ $((BEFORE-NOW)) -ge $BATCH ] && break
    { [ $STABLE -ge $STABLE_NEEDED ] && [ "$NOW" -lt "$BEFORE" ]; } && break
  done

  READ=$((BEFORE-LAST))
  echo "$(date '+%F %T')  batch $b  $BEFORE -> $LAST  (read $READ, waited $((WAITED*POLL))s)" | tee -a "$LOG"

  if [ "$READ" -le 0 ]; then
    DEAD=$((DEAD+1))
    if [ $DEAD -ge $DEAD_BATCHES ]; then
      echo "$(date '+%F %T')  STOP   $DEAD batches with no progress, queue=$LAST. Likely rows PredictLeads rejects; inspect failed runs." | tee -a "$LOG"; exit 2
    fi
  else
    DEAD=0
  fi
done

END=$(count)
echo "$(date '+%F %T')  END    queue=$END  drained_this_run=$((START-END))" | tee -a "$LOG"
