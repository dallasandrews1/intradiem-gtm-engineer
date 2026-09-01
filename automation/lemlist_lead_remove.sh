#!/bin/zsh
# Remove ONE lead from ONE lemlist campaign without unsubscribing the address.
# Usage: lemlist_lead_remove.sh <campaignId> <email>
# Reads LEMLIST_API_KEY from automation/config/lemlist.env. Prints the removed lead's email and id.
# Narrow on purpose: this is the only lead-removal path Claude is allowed to run (see ~/.claude/settings.json).
set -euo pipefail
HERE="${0:A:h}"
KEY="$(grep '^LEMLIST_API_KEY=' "$HERE/config/lemlist.env" | cut -d= -f2)"
CAMPAIGN="${1:?campaignId required (cam_...)}"
EMAIL="${2:?lead email required}"
case "$CAMPAIGN" in cam_*) ;; *) echo "refusing: campaignId must start with cam_" >&2; exit 2;; esac
ENC="$(python3 -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$EMAIL")"
curl -s -u ":$KEY" -X DELETE "https://api.lemlist.com/api/campaigns/$CAMPAIGN/leads/$ENC?action=remove" \
  | python3 -c 'import sys,json; d=json.load(sys.stdin); print("removed:", d.get("email"), d.get("_id")) if d.get("email") else (print("error:", d), sys.exit(1))'
