---
name: feedback-rep-read-pages-deployed
description: Sep 4 2026, anything Nate (or any rep) has to read must be a deployed shareable page (Cloudflare Pages), never a Desktop file; Desktop HTML is Dallas-only, and a rep-facing page carries no credits, prompts or internal mechanics
metadata:
  type: feedback
---
Dallas, Sep 4 2026: "if you need him to read something it's gotta be deployed as a page I can share." The DWO Nate read went live at https://dwo-exec-read.pages.dev (project `dwo-exec-read`, deploy folder ~/Desktop/Intradiem Deliverables/deploy-dwo-exec-read/, `npx wrangler pages deploy . --project-name=<p> --branch=main --commit-dirty=true`, account 37eeacfb7a4767c44ee8f40243b62c96, wrangler via npx is logged in).

**Why:** Dallas shares links in Slack; a file on his Desktop cannot be handed to Nate. Rep-facing pages also must not carry credit spend, copy-paste prompts, removal tables or other internal mechanics (those stay on the Dallas-only Desktop page).

**How to apply:** for every rep or leadership read: build a clean page, deploy to its own Pages project, put the URL in chat with a short Slack-voice note. Related: [[feedback-links-land-on-the-thing]], [[feedback-deliver-html-not-md]].
