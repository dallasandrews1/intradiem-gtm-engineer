# Nathan's review of the four BO customer campaigns (Slack DM, Sep 4 2026, 09:51-10:03 CT)

Source: Dallas asked Nathan to scan the contacts and copy in the four paused customer-lane campaigns
(Healthcare Payer 67, Financial Services 79, Insurance 33, BPO 20) and give a thumbs up or changes.

## Verdicts by campaign

| Campaign | lemlist id | Nathan's read | Action |
|---|---|---|---|
| Insurance | cam_HCu4jiFB8oinz2s3F | "The Insurance messaging is great IMO. Would not change that one. Hits the mark." | None. Copy locked as reviewed. |
| Healthcare Payer | cam_N92Tgg29ncHWnYAD9 | "Healthcare is good." Thumbs up. | None. |
| BPO | cam_Fy287YF9X5fjPYBSo | Thumbs up ("all except Financial"), plus: "Are you able to add MAXIMUS in there? They use Verint for their back office and I've been told that they don't like it all that much." | DONE Sep 4: five Maximus back-office leaders loaded (see below). |
| Financial Services | cam_x8ehMHnWSjBr2CLQe | "Financial one I am thinking through." No thumbs up yet. | OPEN. Wait for his notes; do not start FS until he weighs in. |

Contacts: no contact-level objections on any list.

## What Nathan committed to
- "10-4 on the messaging. I'll get some things your way": replies and emails that landed well, outside our campaigns,
  as context for the messaging models (Dallas's ask at 09:54).
- Earlier (Aug 31): a good list for the VITO DWO campaign.

## Maximus add (executed Sep 4)
- Status: NOT a current customer or partner (Salesforce segment Sep 1 2026), not registered by any partner in the
  pre-pipeline; clear to work. Verint Operations Visualizer / Operations Productivity, about 1,510 seats per the 3xG
  licensing sheet (internal, no public corroboration). Nathan's "they don't like it" read lines up with that footprint.
- One thing to know: Maximus is on Frank's 3xG partner-pilot whitespace list (partner brief built Sep 1,
  motions/partner_channel/briefs/data/maximus.json). Direct outreach from Nathan and a partner-led motion on the same
  account should know about each other. Registration is routing context, not a gate.
- Cohort (six per account, four lanes): Baylinson (GM U.S. Services), Howard (SVP U.S. Services), French (MD Federal
  Program Ops Support), Hillman (Sr Dir WFM), Fitzwater (VP Strategic Workforce Planning), Biernacki (SVP AI
  Transformation and Experience).
- Loaded 5: doughoward@, cindy.french@, marc.hillman@, drexfitzwater@, danbiernacki@ (all maximus.com, ZeroBounce valid;
  Fitzwater's address also matches his Salesforce record). Email 1 previewed on Hillman, every variable renders.
- Held 1: Ilene Baylinson, Enrich Person returned no current role on her LinkedIn URL. Confirmed on maximus.com
  leadership page as GM U.S. Services. Needs a Sales Nav look before she loads.
- Bench (cohorts/maximus_bpo_sep4_bench.csv): Teresa Weipert (GM Federal, no LinkedIn URL on file), Jennifer Springs
  (Dir WFM) and Nizar Mechergui (Sr Mgr Workforce Planning) from the Sep 2 net-new pool, Dave Harkess (VP Contact
  Center Ops, front office).
- Salesforce: Fitzwater has a record on a Maximus account (001V5000006bHWQIA2); Hillman's only SF record is a stale
  Anthology address; Howard's name match is a different person at Nationwide.
- Credits: 6.5 (ledger row 2026-09-04). BPO campaign 20 -> 25, still paused, nothing started.

## Open with Nathan
1. Financial Services notes (his call).
2. Good replies and emails for the messaging context.
3. Whether to give Frank a heads-up on Maximus before the BPO campaign starts.

## Last week's asks, audited Sep 4
| Ask | Date | Status |
|---|---|---|
| Duplicate "Strike Room" for back office only | Aug 24 | Answered indirectly by the back-office maps and the net-new package; no separate strike room built (the Cowork strike room is Enterprise-owned and was broken Sep 1). Decision open. |
| Centene for Rachel | Aug 27 | Centene back-office map went to Nathan Aug 31, never to Rachel. Fixed Sep 4: Centene two-map page for Rachel DiBello (Desktop: "Centene Maps for Rachel - Sep 4.html"). |
| Six accounts, back office / front office / both | Aug 28 | Back office built Aug 31. Front office promised Aug 31, built Sep 4: 87 people on six maps (Desktop: "Nate Front Office Maps - Sep 4.html"). |
| Build the six back-office maps in Sales Nav | Aug 31 | Still open, Dallas's hands (sets/nate.json built list is empty). |
| VITO DWO list from Nathan | Aug 31 | On Nathan. |

## Live pages (deployed Sep 4, house standard)
| Page | URL | For |
|---|---|---|
| Back office maps, Nate's six | https://backoffice-maps.pages.dev/nate/ | Nathan |
| Front office maps, Nate's six | https://backoffice-maps.pages.dev/nate/front-office/ | Nathan |
| Centene, two maps | https://backoffice-maps.pages.dev/centene/ | Rachel DiBello |
| Back office maps, Inger's twelve | https://backoffice-maps.pages.dev/ | Mary Ann and Inger, unchanged |

Deploy source is `deploy-backoffice-maps/` in this folder. Rebuild the page, copy it into the matching subfolder, then redeploy the whole folder.
