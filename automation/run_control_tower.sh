#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

# launchd starts with a bare PATH (no node, npx, clay). Sep 15 2026: the 7:30 deploy had failed every run with
# "npx: command not found" while exiting 0. Put every place those binaries live on the PATH before anything runs.
for d in /opt/homebrew/bin /usr/local/bin "$HOME/.local/bin" "$HOME/.clay/bin" "$HOME"/.nvm/versions/node/*/bin "$HOME/.volta/bin" "$HOME"/.claude/plugins/cache/clay-plugins/clay/*/bin; do
  [ -d "$d" ] && case ":$PATH:" in *":$d:"*) ;; *) PATH="$d:$PATH";; esac
done
export PATH
command -v npx >/dev/null || echo "WARNING: npx not on PATH, deploy will fail"
command -v clay >/dev/null || echo "WARNING: clay CLI not on PATH, live Clay pulls will carry"

python3 build_control_tower.py

# Stage the deploy folder every run (index + state + headers), push only when the config says so.
# Added 2026-09-15 with the animated tower: the deployed link is only useful if it is never stale.
DEPLOY_DIR="$ROOT_DIR/control-tower/deploy"
mkdir -p "$DEPLOY_DIR"
cp "$ROOT_DIR/Control_Tower.html" "$DEPLOY_DIR/index.html"
cp "$ROOT_DIR/control_tower_state.json" "$DEPLOY_DIR/control_tower_state.json"
echo "Control tower snapshot refreshed at $(date -u +%Y-%m-%dT%H:%M:%SZ), staged in control-tower/deploy/"

CFG="$ROOT_DIR/automation/config/control_tower_publish.json"
if [[ -f "$CFG" ]] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$CFG')).get('deploy') else 1)" 2>/dev/null; then
  PROJECT=$(python3 -c "import json; print(json.load(open('$CFG'))['project'])")
  ACCOUNT=$(python3 -c "import json; print(json.load(open('$CFG'))['account_id'])")
  URL=$(python3 -c "import json; c=json.load(open('$CFG')); print(c.get('url') or 'https://'+c['project']+'.pages.dev')")
  if CLOUDFLARE_ACCOUNT_ID="$ACCOUNT" npx --yes wrangler@4 pages deploy "$DEPLOY_DIR" --project-name="$PROJECT" --commit-dirty=true --branch=main >/tmp/control_tower_deploy.log 2>&1; then
    echo "Deployed to $URL at $(date -u +%H:%M:%SZ)"
  else
    echo "DEPLOY FAILED (snapshot still refreshed locally): $(tail -1 /tmp/control_tower_deploy.log)"
    exit 3
  fi
fi
