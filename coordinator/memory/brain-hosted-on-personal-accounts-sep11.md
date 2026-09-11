---
name: brain-hosted-on-personal-accounts-sep11
description: "The GTM brain (intradiem-gtm-system.onrender.com) runs on Dallas's PERSONAL Render account and the gtm_state snapshot on his personal Cloudflare account (andrewsdallas3@gmail.com), not Intradiem-owned infrastructure; never describe it as 'our service' in admin or leadership copy"
metadata:
  type: project
---

Confirmed by Dallas Sep 11 2026 while drafting the Slack app install request note: Render is his own account that he set up, not an Intradiem-owned service. The Pages snapshot at gtm-brain-state.pages.dev is likewise on his personal Cloudflare login.

**Why:** an admin approving the Slack app will read "our service" as company infrastructure; the truthful framing is "a service I host on my own Render account". Slack user identity (user ID, email) reaches that service on every Slackbot call via slack_identity_auth and lands in the brain's request log.
**How to apply:** admin-, IT-, or leadership-facing copy says he hosts it on his own account. If ownership becomes a blocker, the move to an Intradiem-owned Render or Cloudflare account is a redeploy (env vars GTM_STATE_URL, GTM_API_KEYS, SLACK_SIGNING_SECRET, plus the manifest URL), not a rebuild. See [[slack-gtm-brain-app-created-sep11]], [[brain-render-deploy-prereqs-sep11]].
