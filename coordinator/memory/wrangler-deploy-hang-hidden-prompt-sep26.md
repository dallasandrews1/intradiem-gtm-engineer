---
name: wrangler-deploy-hang-hidden-prompt-sep26
description: Sep 26 2026 - deploy_rep_pages.sh sat for hours because the Cloudflare token had expired and npm asked to install a newer wrangler, both prompts hidden behind grep and 2>/dev/null; fixed by pinning wrangler@4 with --yes and showing whoami first
metadata:
  type: project
---

Dallas, Sep 26 2026: three deploy attempts froze right after the "files that differ from live" list. The stuck process was `npm exec wrangler pages project list` on his tty, started after the OAuth token's expiration_time (~/Library/Preferences/.wrangler/config/default.toml) and while npm wanted to install wrangler@4.141.0. The script piped that step through `grep -q` with `2>/dev/null`, so neither prompt was visible.

**Fix in automation/deploy_rep_pages.sh (backup .bak_sep26):** every wrangler call is `npx --yes wrangler@4 ...`; the project-list output is teed to /tmp/wrangler_list.txt instead of discarded; a `whoami` line runs before the diff step so an expired login shows and refreshes. A stuck run is cleared with ctrl-c (or kill of the npm exec pid) and re-run.

**How to apply:** when a deploy "hangs" after the diff list, check `ps aux | grep wrangler` and the token expiry before anything else; never hide a wrangler call's output behind grep -q. Related: [[wrangler-pages-force-delegation-trap]], [[claude-code-auto-mode-blocks-deploys]], [[canonical-rep-host-intradiem-accounts-sep25]].
