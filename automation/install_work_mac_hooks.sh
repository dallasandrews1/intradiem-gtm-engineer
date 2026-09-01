#!/bin/bash
# install_work_mac_hooks.sh : one-time setup on the work Mac (IntradiemDA). Merges the two sync hooks
# into ~/.claude/settings.json (SessionStart -> sync_work_mac.sh start, SessionEnd -> sync_work_mac.sh end),
# keeping every other setting and any existing hooks. Safe to run twice: it never adds a duplicate.
# Backs up settings.json first, validates the result with python3's json parser, prints what it did.
#   bash install_work_mac_hooks.sh            # edits ~/.claude/settings.json
#   bash install_work_mac_hooks.sh <file>     # edits another settings file (used for testing)
set -uo pipefail
SETTINGS="${1:-$HOME/.claude/settings.json}"
SCRIPT="$HOME/Claude/Projects/Intradiem GTM Engineer/automation/sync_work_mac.sh"
[ -f "$SCRIPT" ] || { echo "sync_work_mac.sh not found at $SCRIPT; pull the repo first"; exit 1; }
chmod +x "$SCRIPT" 2>/dev/null || true
mkdir -p "$(dirname "$SETTINGS")"
[ -f "$SETTINGS" ] || echo '{}' > "$SETTINGS"
BAK="$SETTINGS.bak-hooks-$(date +%Y%m%d-%H%M%S)"; cp "$SETTINGS" "$BAK"
python3 - "$SETTINGS" <<'PY'
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
try:
    s = json.loads(p.read_text() or "{}")
except json.JSONDecodeError as e:
    print(f"settings.json is not valid JSON ({e}); nothing changed"); sys.exit(1)
hooks = s.setdefault("hooks", {})
start_cmd = '"$HOME/Claude/Projects/Intradiem GTM Engineer/automation/sync_work_mac.sh" start >/dev/null 2>&1 || true'
end_cmd   = '"$HOME/Claude/Projects/Intradiem GTM Engineer/automation/sync_work_mac.sh" end >/dev/null 2>&1 || true'
want = {
    "SessionStart": {"type": "command", "command": start_cmd, "timeout": 120, "statusMessage": "Syncing from GitHub"},
    "SessionEnd":   {"type": "command", "command": end_cmd,   "timeout": 180, "async": True, "statusMessage": "Publishing to GitHub"},
}
added = []
for event, hook in want.items():
    groups = hooks.setdefault(event, [])
    present = any("sync_work_mac.sh" in h.get("command", "") for g in groups for h in g.get("hooks", []))
    if not present:
        groups.append({"hooks": [hook]}); added.append(event)
p.write_text(json.dumps(s, indent=2) + "\n")
json.loads(p.read_text())  # re-parse: proves the file is valid
print("added: " + (", ".join(added) if added else "nothing (both hooks were already there)"))
PY
rc=$?
if [ $rc -ne 0 ]; then cp "$BAK" "$SETTINGS"; echo "restored backup $BAK"; exit 1; fi
echo "settings: $SETTINGS  (backup: $BAK)"
echo "hooks now:"; python3 -c "import json,sys;s=json.load(open(sys.argv[1]));[print('  '+e+': '+h['command']) for e in ('SessionStart','SessionEnd') for g in s.get('hooks',{}).get(e,[]) for h in g['hooks'] if 'sync_work_mac' in h.get('command','')]" "$SETTINGS"
echo "Done. Hooks load on the next Claude Code session (or type /hooks in an open one)."
