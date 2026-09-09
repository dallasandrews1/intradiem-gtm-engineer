---
name: wrangler-pages-create-force-sep9
description: "Sep 9 2026: wrangler 4.130 delegates `pages project create` to a Workers flow that fails with 'missing worker entrypoint or assets directory'; pass --force once to create the Pages project directly, then deploy as usual (wrangler@3 pin was blocked by the classifier)"
metadata:
  type: reference
---

`npx wrangler pages project create <name> --production-branch=main --force` creates a real Pages project on wrangler 4.130+. Without `--force` the command is delegated to Cloudflare Workers and errors. `--force` is only for the create step; `pages deploy . --project-name=<name> --commit-dirty=true --branch=main` already skips delegation because of those args. New projects return 522 on the first poll and 200 within about 15 seconds. Account id 37eeacfb7a4767c44ee8f40243b62c96 via `CLOUDFLARE_ACCOUNT_ID`.

**Why:** first hit Sep 9 2026 creating adoption-telemetry; the classifier blocks pulling `wrangler@3` as a workaround. Related: [[feedback-deploy-everything-to-pages]].
