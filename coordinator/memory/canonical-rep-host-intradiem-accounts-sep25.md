---
name: canonical-rep-host-intradiem-accounts-sep25
description: Sep 25 2026 - the link reps get is intradiem-accounts.pages.dev/<rep>/, never backoffice-maps or save-rooms, because reps sell every product; old hosts keep serving, redirects still phase two
metadata:
  type: feedback
---

Dallas, Sep 25 2026: "we need to be calling this intradiem-accounts.pages.dev/Rachel/ not back office that doesn't make sense when they are selling multiple products."

**Why:** the hostname is part of the message. A page called back-office tells an AE selling Queue Optimizer and Contact Center Automation that the page is not for them.

**How to apply:** every link handed to a rep, in a DM, email or canvas, is on intradiem-accounts.pages.dev (layout /<rep>/, /<rep>/<account>/, /<rep>/<account>/map/, /<rep>/alumni/). Deploy order stays maps, rooms, plans; the plans step assembles the new tree, and the _staged_pre_job6 snapshot must be refreshed from the staged folders whenever the old folders were rebuilt (else check_plans_site fails on step 5). backoffice-maps and save-rooms are never deleted (links in the wild). Redirects from the old hosts are phase two and need Dallas's explicit go. Related: [[rep-index-pages-sep20]], [[shared-links-gate-sep20]], [[rachel-four-account-package-sep25]].
