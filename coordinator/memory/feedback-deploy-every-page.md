---
name: feedback-deploy-every-page
description: "Dallas's Sep 11 2026 rule: every room, page, or build gets deployed to a live link (Cloudflare Pages, one folder per project under ~/Desktop/Intradiem Deliverables/deploy-*) so he can share it; a Desktop HTML file alone is not delivered"
metadata:
  type: feedback
---

Sep 11 2026, while the Cleveland Clinic Save Room was being merged and loaded: "any rooms or pages or builds etc that you do needs to be deployed so i can share links."

**Why:** he shares work by link with AMs, Success, Naveen and leadership; a file on his Desktop cannot be forwarded and reads as unfinished.

**How to apply:** for every HTML deliverable, in the same turn it is built: copy it into `~/Desktop/Intradiem Deliverables/deploy-<project>/` (index.html, plus `_headers` with X-Robots-Tag noindex and the branded 404.html copied from deploy-backoffice-maps), create the project once with `npx wrangler@latest pages project create <name> --production-branch main --force` (wrangler 4.131+ otherwise delegates Pages to Workers and fails with 'Missing entry-point'; --force is needed only on create, never on deploy), then `CLOUDFLARE_ACCOUNT_ID=37eeacfb7a4767c44ee8f40243b62c96 npx wrangler@latest pages deploy . --project-name=<name> --branch=main --commit-dirty=true`, curl both URLs, and put the live link in chat next to the Desktop path. Sub-pages go in subfolders (`/cleveland-clinic/`). Redeploy the same folder after every rebuild. First use: save-rooms.pages.dev (plan page at /, Cleveland Clinic at /cleveland-clinic/). Related: [[feedback-deliver-html-not-md]], [[feedback-links-land-on-the-thing]].
