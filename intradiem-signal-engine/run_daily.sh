#!/bin/bash
# Intradiem signal engine: daily run.
# Scores every account, regenerates the dashboard data, and writes the notifier
# dry-run to a dated digest. Safe to run by hand any time:  bash run_daily.sh
#
# To go live with notifications later, change the notifier line near the bottom
# from a dry run to:  "$PY" notifier.py --send --channel slack
set -euo pipefail

# --- paths (edit if you move things) ---
ENGINE="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/intradiem-signal-engine"
DEPLOY_HTML="/Users/dallasandrews/Desktop/outputs/intradiem-deploy/index.html"
PY="/Users/dallasandrews/.venvs/intradiem/bin/python"

cd "$ENGINE"
mkdir -p logs
STAMP="$(date +%Y-%m-%d)"
DIGEST="logs/digest_${STAMP}.txt"

echo "[$(date)] Intradiem daily run starting"

# 1. Score every account and write the data file.
"$PY" signal_processor.py --output data/signals.json

# 2. Inject fresh data into the deployed dashboard, and place signals.json beside
#    it so the hosted page can fetch the freshest run. Skipped if the deploy file
#    is missing, so a moved folder does not break the run.
if [ -f "$DEPLOY_HTML" ]; then
  "$PY" build_dashboard.py --html "$DEPLOY_HTML"
  cp data/signals.json "$(dirname "$DEPLOY_HTML")/signals.json"
  echo "Dashboard refreshed: $DEPLOY_HTML"
else
  echo "Deploy file not found, skipped dashboard refresh: $DEPLOY_HTML"
fi

# 3. Notifier dry-run into a dated digest (prints what it would send, sends nothing).
"$PY" notifier.py > "$DIGEST" 2>&1
echo "Digest written: $ENGINE/$DIGEST"

# 4. TAM outbound engine: score net-new accounts, refresh the Strike List data
#    beside the page, and write each seller's strike-list digest (dry run).
TAM="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/tam-outbound-engine"
if [ -d "$TAM" ]; then
  ( cd "$TAM"
    mkdir -p logs
    "$PY" account_engine.py --output data/tam_plays.json
    if [ -f "$DEPLOY_HTML" ]; then
      cp data/tam_plays.json "$(dirname "$DEPLOY_HTML")/tam_plays.json"
      echo "Strike List data refreshed beside the page"
    fi
    "$PY" tam_notifier.py > "logs/strike_digest_${STAMP}.txt" 2>&1
    echo "Strike digest: $TAM/logs/strike_digest_${STAMP}.txt"
  )
fi

# 5. Impact scorecard: aggregate both engines, refresh the Impact tab data.
IMPACT="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/impact"
if [ -d "$IMPACT" ]; then
  ( cd "$IMPACT"
    "$PY" impact_engine.py --output impact.json >/dev/null
    if [ -f "$DEPLOY_HTML" ]; then
      cp impact.json "$(dirname "$DEPLOY_HTML")/impact.json"
      echo "Impact scorecard refreshed beside the page"
    fi
  )
fi

# Short summary to the log.
OWNERS="$(grep -c '^To: ' "$DIGEST" || true)"
echo "[$(date)] Daily run complete. $OWNERS owner(s) would be notified (expansion). See the digests above."
