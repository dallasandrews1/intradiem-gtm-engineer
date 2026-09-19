---
name: needle-movers-wins-board-sep18
description: "Sep 18 2026: Needle Movers wins board staged (not deployed) in ~/Desktop/Intradiem Deliverables/deploy-wins-board/; one page on the Rachel brand kit, five seeded wins, scope filter, data-driven so a new win is one JSON entry"
metadata:
  type: project
---

Built Sep 18 2026 as the fifth idea in Dallas's Needle Movers email to Jen Lee ([[spot-bonus-program-sep18]]), so it is ready to show if she says yes. STAGED ONLY: Dallas said do not deploy until he says go.

- Folder: `~/Desktop/Intradiem Deliverables/deploy-wins-board/` (index.html, intradiem-brand.css copied from brand-kit, assets/ with logo and background, _headers noindex). brand-check.py passes clean.
- Every win is one entry in the `wins-data` JSON block at the top of index.html (title, scope team/teams/org, builtBy, team, builtFor, constraint, built, impact, reuse, proofLabel, proofUrl, date). Counts and the scope filter compute from the data; a how-to comment sits above the block.
- Public-page wording on purpose: no partner names (3xG, SagesS3), no Cleveland Clinic renewal or RFP detail, save-room proof points at the save-rooms index. The email to Jen named those; a pages.dev page must not.
- Deploy when told: `npx wrangler pages project create needle-movers-wins --production-branch main --force` then `npx wrangler pages deploy . --project-name needle-movers-wins --branch main --commit-dirty=true --force`, and delete the `.wrangler` folder before and after (wrangler 4.135 routes to workers.dev without --force and uploads its own cache).

**Lesson:** the kit's `.section-brand` does not set heading colour, so an h1 inside it renders dark green on dark green and the linter does not catch it; always set `header.section-brand h1{color:var(--id-white)}` and check the header in a render.
