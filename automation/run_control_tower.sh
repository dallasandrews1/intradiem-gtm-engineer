#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

python3 build_control_tower.py
python3 build_control_tower_page.py "$@"

if [[ -f "Control_Tower.html" ]]; then
  echo "Control tower snapshot refreshed at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi
