---
name: icp-committees-recast-aug10
description: "ICP Buying Committees recast Aug 10 per Naveen - one account per committee, Gatekeeper renamed Integration owner"
metadata: 
  node_type: memory
  type: project
  originSessionId: e5679cea-fee0-4449-896b-bdd11562ecd5
  modified: 2026-08-10T18:08:02.155Z
---

On Aug 10 2026 Naveen asked (Slack DM) that each product's ICP buying committee show people from ONE account, and named the accounts: Centene for front office Queue Optimizer, State Farm for Back Office Optimizer, Humana for Engagement Hub. Dallas also asked to retire the role name "Gatekeeper" (too derogatory); it is now "Integration owner" everywhere.

Shipped same day: deploy-icp-committees/index.html reworked (featured single-account committee per product and lane, sector tabs kept as ICP reference), deployed to the icp-committees Cloudflare Pages project. Lanes: QO Centene (prospect) / RBC (customer), BOO State Farm (prospect) / Humana (customer), EH Humana (customer) / Centene (prospect). New people added from public-source research: Kelli Reese (Humana Director, Stars/Quality and Risk Adjustment; replaced first pick Amy Heilman after a verification pass found she likely left Humana, her headline was stale), Stephanie Zevitas (promoted from bench), Mohammed Inayathullah (Humana, Genesys agent assist), and the State Farm four: Wensley J. Herbert (SVP P&C Claims, on the official leadership page), Sean Rae (Director Workforce Analytics), Dana Jokerst (Senior Operations Manager P&C Claims, title corrected via Clay repair), Andrew Galligan (Technology Director P&C Claims). Photos: 4 of 7 obtained same day via the Aug 6 photo playbook (Clay Profile Photo Fetch wf_0tjdq6dDxvgdXTvYvAG + Profile URL Repair wf_0tjdqg1qkx3VYdSpTRV, 8.5 credits, ledger entry Aug 10; Herbert's came from the State Farm leadership page after his LinkedIn media URL expired). Reese, Zevitas, Jokerst have no public photo, initials fallback. Titles still worth a live LinkedIn glance before outreach use.

Aug 6 versions archived in "Intradiem Deliverables/_archive/icp-committees superseded Aug 10". Per-sector committee data retained in the payload (meta.recast notes this). Rebuild scripts: scratchpad rework_icp.py + gen_derivatives.py (session-temporary; the payload itself is the durable source). Related: [[deliverables-folder-convention]], [[naveen-facing-comms-rules]].
