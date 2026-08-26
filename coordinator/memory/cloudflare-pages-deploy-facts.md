---
name: cloudflare-pages-deploy-facts
description: REFERENCE - Cloudflare Pages behaviors that constrain how Dallas ships HTML deliverables; the big one is that a Direct Upload project can NEVER be converted to Git integration, so the URL decision is one-way unless a custom domain fronts it
metadata:
  type: reference
---

Verified against Cloudflare's own docs 2026-07-30 while deploying the DWO deck ([[dwo-html-deck-build-jul30]]).

**1. Direct Upload cannot become Git-connected. Ever.** Cloudflare docs, verbatim: "If you choose Direct Upload, you cannot switch to Git integration later. You will have to create a new project with Git integration to use automatic deployments." A new project means a new `*.pages.dev` URL, so any link already shared breaks. **Therefore: put a custom domain on any Pages project whose link gets emailed to someone, BEFORE sending it.** The custom domain makes the hosting method a swappable implementation detail. `dallasandrews.dev` is already on Cloudflare (verified `server: cloudflare` on the apex plus gtmstrategy/gtmplan subdomains), so adding a subdomain is a one-click Custom domains step with no DNS work. Precedent for hosting Intradiem exec material on that domain exists: Naveen sent the Norton pre-read at gtmplan.dallasandrews.dev to all attendees.

**2. No 404.html means typos silently serve index.html with a 200.** Confirmed live on dwo-deck.pages.dev: `/custommer` returned 200 and served the full deck. On any project mixing internal and external content, a mistyped URL can therefore hand someone the internal version. Always ship a `404.html`, and prefer one Pages project per audience over one project with paths.

**3. `_headers` works on direct upload.** `/*\n  X-Robots-Tag: noindex\n  Referrer-Policy: no-referrer` keeps unlisted links out of search results.

**4. Pages links are public to anyone with the URL.** There is no auth on a plain Pages project; unlisted is not access-controlled. If a deliverable ever needs real gating, that is Cloudflare Access (Zero Trust), a separate setup.

**5. Wrangler CLI is now authenticated (Jul 31 2026).** OAuth login completed on the personal account (andrewsdallas3@gmail.com); Claude can now create Pages projects and deploy directly via `npx wrangler pages deploy <folder> --project-name=<name>`, so drag-and-drop is no longer the only path (it remains the loop for Rachel/Melissa). First CLI-deployed project: `gtm-outbound-plan` (the Naveen operating plan), built via `build_deploy.py` which now includes it as `5-outbound-plan`. The OAuth token scope has pages:write and zone:read but NOT DNS-record write, so custom-domain attachment stays a one-click dashboard step. Cloudflare's official Claude Code plugin (cloudflare@cloudflare, MCP servers incl. main API + docs) installed Jul 31; its tools become available after a session restart and may open a cleaner API path than raw wrangler.

**Standing decision (Jul 30 2026):** stay on Direct Upload with a custom domain for now rather than moving to Git. Git's real wins (auto-deploy on push, version history, personal-Mac/work-Mac sync per [[work-laptop-sync-queued-jul27]]) are genuine, but the repo would hold Intradiem IP and a personal GitHub account is the wrong home for it; this company already scrutinizes third-party cloud ([[mem0-enterprise-compliance-flag-jul17]] — Jason Jones flagged Mem0 in #ai). Revisit when there is an Intradiem-owned GitHub org. Marketing (Rachel, Melissa) will not use git either way, so the drag-and-drop path plus `build_deploy.py` stays the maintenance loop.
