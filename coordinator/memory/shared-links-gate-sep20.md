---
name: shared-links-gate-sep20
description: "Sep 20 2026: every pages.dev link Dallas has sent is registered (43 holder entries, 65 URLs) and check_shared_links.py is the hard gate before and after every Pages deploy; its first run caught two links Nate holds that had been 404 for two weeks"
metadata:
  type: project
---

**What exists:** `automation/config/shared_links_manifest.json` (who holds which link, when, source; append only, never remove) and `automation/check_shared_links.py` (cache-busted GET on every URL; exit 1 unless 200 or a redirect ending on a 200 for the same rep, account and page type). Companion `automation/pages_live_diff.py` does the staged-versus-live file check (`--expect`) and the post-deploy byte verification with one re-sample (`--verify`).

**Sweep, Sep 20 2026:** Slack (42 messages, all DMs and channels), Outlook sent mail, Teams (zero). Both Needle Movers emails re-read against the registry (16 and 5 links, 21 distinct; an earlier "22" was a miscount). No direct send to Rachel DiBello, J.W., Jen Lee or Jenn East outside those emails. Naveen holds the most. One link travels without Dallas sending it: gtm-operating-map.pages.dev, circulated by Sierra to a marketing group.

**Why it matters (the first run proved it):** `backoffice-maps.pages.dev/centene/` and `/nate/front-office/`, sent to Nathan Sep 4, had been 404 since about Sep 6. A `--force` Pages deploy replaces the whole site with the folder's contents, and the deploy folder never held those two pages, so the next deploy silently dropped them. Nobody noticed for two weeks.

**How to apply:**
- Run the gate before AND after every deploy, rebuild, rename or migration. A fail blocks the deploy.
- The deploy folder is the site. Anything live that is not in the folder disappears on the next deploy; before deploying, `pages_live_diff.py` shows what differs, but it cannot see a live page the folder lacks. The registry gate is what catches that.
- Add every newly sent link to the registry the moment it is sent.

**State at close, Sep 20 2026:** 44 holder entries, 97 URLs (32 are the new intradiem-accounts equivalents under a "Nobody yet" holder), gate 97 of 97 after all three deploys. `automation/check_holder_versions.py "<name>"` answers the sharper question for one person: are their links intact AND serving the newest staged bytes, fetched plain as well as cache-busted. Dallas asked exactly this about Jen Lee's email; run it after any deploy that touches a page leadership holds.

**Sep 20 2026, record sheets deploy:** 45 holder entries, 109 URLs, gate 109 of 109. Trap: `pages_live_diff.py --verify` with no file list checks nothing and exits 0; the whole-site proof is `--expect` with an empty list.

Related: [[rep-index-pages-sep20]], [[wrangler-pages-force-delegation-trap]], [[feedback-seller-pages-no-fluff]].
