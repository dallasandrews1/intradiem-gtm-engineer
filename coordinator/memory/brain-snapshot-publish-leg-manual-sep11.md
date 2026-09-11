---
name: brain-snapshot-publish-leg-manual-sep11
description: "Sep 11 2026 verified: the brain refetches gtm-brain-state.pages.dev every 5 min (live loop on the brain side) but NOTHING on the personal Mac auto-publishes the snapshot; sync_publish stages only, both Sep 11 publishes were by hand, so the brain goes stale at 36h unless --deploy is wired into the nightly"
metadata:
  type: project
---

Checked Sep 11 2026 evening when Dallas asked whether a "live loop" from an earlier thread made the nightly publish unnecessary.

- Brain side: `_read_snapshot()` in `gtm-hosted-platform/brain/app.py` fetches `GTM_STATE_URL` on a 300 s TTL, redacts past 36 h, refuses past 168 h. That is the loop that removed the redeploy-to-refresh problem.
- Mac side: `automation/sync_publish.sh` step 4b runs `publish_gtm_state.sh` with NO `--deploy` (comment says stage only, outward-facing). Log `automation/logs/brain-snapshot-2026-09-11.md` shows ~15 stage-only entries and two manual deploys (16:05Z, 20:12Z).
- No launchd plist, process, or worktree commit runs `wrangler pages deploy` for gtm-brain-state. Unverified: the work Mac and Cloudflare itself (no cron seen from here).

**Why:** the two halves look like one loop from the outside; the publish leg is the gap that makes Slackbot answers read withheld by Sunday.
**How to apply:** if Dallas confirms no loop elsewhere, add `--deploy` to step 4b of sync_publish (log result, staging as fallback), and POST /v1/refresh is optional since the TTL is 5 min. See [[brain-render-deploy-prereqs-sep11]], [[slack-gtm-brain-app-created-sep11]].
