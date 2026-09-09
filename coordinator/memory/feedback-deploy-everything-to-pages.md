---
name: feedback-deploy-everything-to-pages
description: "Sep 9 2026: every built page goes live on Cloudflare Pages by default so the people it is for can open a link; do not hold a deploy back out of hosting caution, Dallas decides exposure"
metadata:
  type: feedback
---

Dallas, Sep 9 2026, when I suggested sending the side-quest pages as files and hosting later: "shouldn't all things we build be deployed to pages so they can all access them easily and view/use them". Yes. Default is a noindex Pages project per deliverable (pattern: `deploy-<name>/` folder on the Desktop with index.html, `_headers` noindex, branded 404), link first in any Slack draft.

**Why:** a link lands on the thing ([[feedback-links-land-on-the-thing]]); attached HTML files make colleagues download and open, and cross-file links break. Hosting caution about an internal tool name on a noindex page is Dallas's call to make, not a reason to withhold.

**How to apply:** build, verify, deploy, then hand over the URL. Raise an exposure concern in one line alongside the link if there is one; never in place of it. Related: [[html-deliverable-standard]], [[wrangler-pages-create-force-sep9]].
