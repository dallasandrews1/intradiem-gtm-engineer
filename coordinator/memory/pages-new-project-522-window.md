---
name: pages-new-project-522-window
description: "A brand-new Cloudflare Pages project serves 522 / SSL handshake errors for several minutes after the first deploy; this is propagation, not a failed deploy"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6ca2e88b-0881-40b3-8ef1-9f091aa27912
  modified: 2026-08-06T20:38:38.665Z
---

When a NEW Cloudflare Pages project is created and deployed for the first time, both
`<project>.pages.dev` and the per-deployment `<hash>.<project>.pages.dev` hostname can return
`error code: 522` (and curl `sslv3 alert handshake failure`) for roughly 5-10 minutes while the
edge provisions the hostname and its certificate. The deploy itself already succeeded.

**Why:** the upload and deployment complete instantly, but the new pages.dev subdomain's edge
routing and cert lag behind. A 522 here reads like a broken deploy and tempts a redeploy, which
does nothing but mint a second deployment.

**How to apply:** do not redeploy and do not debug the files. Confirm the deploy succeeded with
`wrangler pages deployment list --project-name=<name>`, sanity-check an EXISTING pages.dev project
(if it returns 200, the account and edge are fine and it's just the new hostname), then poll until
it serves. Deploys to projects that already exist do not have this window.

Verified 2026-08-06 on the `icp-committees` deploy. Related: [[deliverables-folder-convention]].
