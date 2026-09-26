---
name: canonical-rep-host-intradiem-accounts-sep25
description: Sep 25 2026 - the link reps get is intradiem-accounts.pages.dev/<rep>/, never backoffice-maps or save-rooms, because reps sell every product; old hosts keep serving, redirects still phase two
metadata:
  type: feedback
---

Dallas, Sep 25 2026: "we need to be calling this intradiem-accounts.pages.dev/Rachel/ not back office that doesn't make sense when they are selling multiple products."

**Why:** the hostname is part of the message. A page called back-office tells an AE selling Queue Optimizer and Contact Center Automation that the page is not for them.

**How to apply:** every link handed to a rep, in a DM, email or canvas, is on intradiem-accounts.pages.dev (layout /<rep>/, /<rep>/<account>/, /<rep>/<account>/map/, /<rep>/alumni/). Deploy order stays maps, rooms, plans; the plans step assembles the new tree, and the _staged_pre_job6 snapshot must be refreshed from the staged folders whenever the old folders were rebuilt (else check_plans_site fails on step 5). backoffice-maps and save-rooms are never deleted (links in the wild). Redirects from the old hosts are phase two and need Dallas's explicit go. Related: [[rep-index-pages-sep20]], [[shared-links-gate-sep20]], [[rachel-four-account-package-sep25]].

**Sep 26 2026 lesson:** moving the alumni page from /<rep>/alumni/map/ to /<rep>/alumni/ broke a link Keegan and Nathan hold and failed the shared links gate after a maps deploy. Any path change on the new host keeps the old path served (assemble_plans_site.py now writes a same-host meta-refresh page at the old path). When the gate fails on a plans-host link, the plans deploy has to run directly with wrangler from Dallas's terminal, because the script's own pre-gate blocks it.
