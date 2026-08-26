#!/bin/zsh
# Headless access fix, staged 2026-08-20. Default is DRY-RUN (prints diffs). Pass --apply to install.
# Installs the four re-pointed agent defs into BOTH copies, drops the rows parser into automation/lib,
# and appends the registry addendum. Nothing here touches Clay, launchd, or any wrapper.
set -uo pipefail
ST="$(cd "$(dirname "$0")" && pwd)"
REPO="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
A1="$HOME/.claude/agents"; A2="$HOME/coordinator/.claude/agents"; REG="$HOME/coordinator/AGENT_REGISTRY.md"
AGENTS=(gate-integrity-auditor table-hygiene credit-strategist pipeline-receipts-tracker)
MODE="${1:---dry-run}"
for a in $AGENTS; do
  for dst in "$A1" "$A2"; do
    echo "=== $a -> $dst ==="
    if [ "$MODE" = "--apply" ]; then
      tag="copy1"; [ "$dst" = "$A2" ] && tag="copy2"
      cp "$dst/$a.md" "$ST/backup_${tag}_$a.md.bak" 2>/dev/null || true
      cp "$ST/$a.md" "$dst/$a.md" && echo "installed"
    else
      diff -u "$dst/$a.md" "$ST/$a.md" | head -400 || true
    fi
  done
done
echo "=== clay_rows2tsv.py -> $REPO/automation/lib ==="
if [ "$MODE" = "--apply" ]; then cp "$ST/clay_rows2tsv.py" "$REPO/automation/lib/clay_rows2tsv.py" && chmod +x "$REPO/automation/lib/clay_rows2tsv.py" && echo "installed"; else echo "(would copy)"; fi
echo "=== registry addendum -> $REG ==="
if [ "$MODE" = "--apply" ]; then
  if grep -q "Addendum 2026-08-20: Clay read path re-pointed" "$REG"; then echo "already appended"; else cat "$ST/registry_patch.md" >> "$REG" && echo "appended"; fi
else cat "$ST/registry_patch.md"; fi
if [ "$MODE" = "--apply" ]; then
  echo "=== verify: no MCP clay tool refs remain in the four defs (both copies) ==="
  grep -l "mcp__plugin_clay_clay" "$A1"/{gate-integrity-auditor,table-hygiene,credit-strategist,pipeline-receipts-tracker}.md "$A2"/{gate-integrity-auditor,table-hygiene,credit-strategist,pipeline-receipts-tracker}.md 2>/dev/null && echo "STILL REFERENCED (unexpected)" || echo "clean"
  echo "=== verify: both copies identical ==="
  for a in $AGENTS; do diff -q "$A1/$a.md" "$A2/$a.md" && echo "$a: in sync"; done
  echo "APPLIED $(date '+%Y-%m-%d %H:%M')" >> "$ST/APPLIED.marker"
fi
