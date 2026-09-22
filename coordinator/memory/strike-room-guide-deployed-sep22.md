---
name: strike-room-guide-deployed-sep22
description: "strike-room-guide.pages.dev is the deployed field guide; method only by design, and the rule for what may be deployed vs what ships as a PDF"
metadata:
  type: project
---

Live Sep 22 2026: **https://strike-room-guide.pages.dev** (Cloudflare Pages project `strike-room-guide`). 200, noindex header, branded 404, 11 present-mode slides, registered in the shared links manifest, gate PASS at 118 URLs.

Source: `motions/shared/strike_room_guide/` (`How_To_Work_A_Strike_Room_Sep22.md`, `deck.py`, `build_site.py`, plus `deck_layer.css/js` copied from the hc_qo set). Built on the shared `_tpl` page system per the Sep 21 lesson that a flat `build_md_page.py` page is below the bar for a shared link. Redeploy: `python3 build_site.py --stage`, then from the deploy folder `npx wrangler pages deploy . --project-name=strike-room-guide --branch=main --commit-dirty=true` (no `--force`, the project exists), deleting `.wrangler` before and after.

**The deploy rule this established:** the field guide is deployed because it is method only. The two account strike rooms are deliberately NOT deployed, because they carry 21 people's work emails and mobile numbers and a pages.dev URL is unauthenticated. They ship as PDF attachments in the DM instead. `build_site.py` enforces the split in code: a BANNED list fails the build if any account domain, committee surname, customer name or "@" appears on the page.

Apply this generally. **Method, framework and process pages can be links. Anything carrying contact detail, account intel or an unreleased customer name is a file.**

Delivery format note: Slack canvas (`slack_create_canvas`) returned Internal Server Error on every attempt across the session, so the working route for rep-facing documents is markdown, then `md_to_page.py` to branded HTML, then headless Chrome to PDF, because PDFs preview inline in Slack. `slack_send_message_draft` stages the message for Dallas to attach files and send.

Related: [[strikerooms-bcbsm-vanguard-sep22]], [[feedback-no-fluff-scannable-deliverables]], [[shared-links-gate-sep20]], [[wrangler-pages-force-delegation-trap]]
