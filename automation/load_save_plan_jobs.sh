#!/bin/zsh
# Loads the two save-plan jobs (account-health-watch Mon 7:10, owner-digest Mon 7:30) into launchd.
# Guard: refuses to load until the worktree is merged, i.e. until the scripts exist in the MAIN repo path the plists point at.
set -euo pipefail
MAIN="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
for f in automation/account_health_score.py automation/run_account_health_watch.sh automation/owner_digest.py automation/run_owner_digest.sh automation/config/account_health.json automation/config/owner_digest.json; do
  [ -f "$MAIN/$f" ] || { echo "HOLD: $MAIN/$f missing, merge the worktree first"; exit 1; }
done
for label in com.dallasandrews.gtm.accounthealth com.dallasandrews.gtm.ownerdigest; do
  cp "$MAIN/automation/$label.plist" ~/Library/LaunchAgents/"$label".plist
  launchctl bootout "gui/$(id -u)/$label" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/"$label".plist
  launchctl print "gui/$(id -u)/$label" | grep -E "state|program" | head -2
done
echo "loaded both; first fire Monday 7:10 and 7:30"
