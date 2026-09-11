#!/bin/bash
# publish_gtm_state.sh : regenerate the brain's snapshot and stage its publish.
#
# The brain fetches ONE published gtm_state.json instead of importing the engines, so
# refreshing what sellers see is this script, not a container redeploy. That is the fix for
# the stale-data root cause (see app.py's header).
#
# Default is STAGE, not deploy: it regenerates, validates, writes the deploy folder and
# PRINTS the wrangler command. Publishing is outward-facing and the snapshot carries seller
# emails and generated prospect copy, so the actual push is a deliberate act. Pass --deploy
# to run it.
#
#   ./publish_gtm_state.sh            regenerate + validate + stage
#   ./publish_gtm_state.sh --check    validate only, write nothing
#   ./publish_gtm_state.sh --deploy   stage, then run wrangler
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DEPLOY_DIR="${GTM_STATE_DEPLOY_DIR:-$HOME/Desktop/Intradiem Deliverables/deploy-gtm-brain-state}"
PROJECT="${GTM_STATE_PAGES_PROJECT:-gtm-brain-state}"
CF_ACCOUNT="${CLOUDFLARE_ACCOUNT_ID:-37eeacfb7a4767c44ee8f40243b62c96}"
LOGDIR="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/logs"
LOG="$LOGDIR/brain-snapshot-$(date +%Y-%m-%d).md"

MODE=stage
for a in "$@"; do case "$a" in --check) MODE=check;; --deploy) MODE=deploy;; esac; done

mkdir -p "$LOGDIR" 2>/dev/null
[ -f "$LOG" ] || printf '# brain snapshot %s\n\n' "$(date +%Y-%m-%d)" > "$LOG"
say() { printf '%s\n' "$*" | tee -a "$LOG"; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# 1. regenerate from the live engines
if ! python3 "$HERE/build_gtm_state.py" --output "$TMP/gtm_state.json" > "$TMP/gen.out" 2>&1; then
  say "$(date +%H:%M)  generator FAILED, nothing published: $(tail -3 "$TMP/gen.out" | tr '\n' ' ')"
  exit 1
fi

# 2. validate before anything leaves this machine. A snapshot that would be served redacted
#    is not worth publishing, and an empty universe would silently blank the strike room.
BRAIN_HERE="$HERE" python3 - "$TMP/gtm_state.json" <<'PY' || exit 1
import json, sys, os
sys.path.insert(0, os.environ["BRAIN_HERE"])   # this script's own folder, passed in
import gtm_state
s = json.load(open(sys.argv[1]))
age = gtm_state.age_hours(s.get("generated_at"))
f = gtm_state.freshness(age)
strike = s.get("engines", {}).get("strike", {})
n = len(strike.get("accounts", []))
seed = strike.get("counts", {}).get("seed", 0)
print(f"  generated_at {s.get('generated_at')}  ({f}, {age}h)")
print(f"  strike {n} accounts, {seed} seed, {strike.get('counts',{}).get('customer_excluded',0)} customer-excluded")
if s.get("errors"):
    print(f"  ENGINE ERRORS: {s['errors']}")
fail = []
if f != "fresh":
    fail.append(f"snapshot is not fresh ({f})")
if n == 0:
    fail.append("strike universe is empty; publishing this would blank the strike room")
if "strike" in s.get("errors", {}):
    fail.append("the strike engine failed to build")
if fail:
    print("  REFUSING TO PUBLISH: " + "; ".join(fail))
    sys.exit(1)
if seed == n:
    print("  WARNING: every strike row is seed data. It will publish, but the brain will")
    print("           redact every figure until the `source` column is filled.")
PY

if [ "$MODE" = check ]; then
  say "$(date +%H:%M)  check only, nothing written"
  exit 0
fi

# 3. stage the deploy folder
mkdir -p "$DEPLOY_DIR"
cp "$TMP/gtm_state.json" "$DEPLOY_DIR/gtm_state.json"
# keep it out of search results; this is not access control, see the note below
cat > "$DEPLOY_DIR/_headers" <<'HDR'
/*
  X-Robots-Tag: noindex, nofollow
  Cache-Control: public, max-age=60
HDR
printf 'User-agent: *\nDisallow: /\n' > "$DEPLOY_DIR/robots.txt"
say "$(date +%H:%M)  staged $DEPLOY_DIR/gtm_state.json"

CMD="CLOUDFLARE_ACCOUNT_ID=$CF_ACCOUNT npx wrangler pages deploy . --project-name=$PROJECT --branch=main --commit-dirty=true"

if [ "$MODE" = deploy ]; then
  say "$(date +%H:%M)  deploying to $PROJECT"
  ( cd "$DEPLOY_DIR" && CLOUDFLARE_ACCOUNT_ID="$CF_ACCOUNT" npx wrangler pages deploy . \
      --project-name="$PROJECT" --branch=main --commit-dirty=true ) 2>&1 | tail -6 | tee -a "$LOG"
  say "$(date +%H:%M)  NOTE: the Cloudflare edge serves a mix of old and new for a few minutes."
  say "         Verify with a few requests, not one. Then POST /v1/refresh on the brain to"
  say "         drop its cache instead of waiting out the TTL."
else
  say "$(date +%H:%M)  staged, not deployed. To publish:"
  say "         cd \"$DEPLOY_DIR\" && $CMD"
  say "         then: curl -X POST -H \"X-API-Key: \$KEY\" https://intradiem-gtm-system.onrender.com/v1/refresh"
fi

# A Pages project is PUBLIC. noindex and robots.txt keep it out of search, they do not keep
# anyone out. This snapshot carries seller emails, account scores and generated
# prospect-facing copy. If that matters, publish somewhere authenticated instead and point
# GTM_STATE_URL + GTM_STATE_TOKEN at it; the brain's fetcher already supports a token.
