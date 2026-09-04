---
name: feedback-rep-deliverables-are-deployed-pages
description: Sep 4 2026 Dallas rule - anything delivered to a rep or partner ships as a deployed page on the house standard, never a Desktop HTML file, a markdown file, or a Claude artifact link
metadata:
  type: feedback
---

Sep 4 2026, on the Nathan and Rachel maps: "anything I'm delivering to Nate and or Rachel needs to be sent as a deployed page with the same standards we have set."

**Why:** a Desktop file or a Claude artifact link is not durable, cannot be reshared inside Intradiem, and does not carry the brand system the rest of the work is judged on. A rep who gets a link should land on the working artifact on the house design system, at a URL that still resolves next month.

**How to apply:** build the page, stage it into the motion's `deploy-*` folder as `<audience>/index.html`, deploy the whole folder to its Cloudflare Pages project, verify every path returns 200 with the right title, and confirm any pre-existing URL is byte-identical so nobody's old link breaks. Then hand Dallas the URLs, not file paths. Delete the Desktop copies. Related: [[feedback-deliver-html-not-md]], [[feedback-links-land-on-the-thing]], [[nate-front-office-maps-sep4]], [[html-deliverable-standard]].
