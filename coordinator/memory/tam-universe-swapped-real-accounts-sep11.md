---
name: tam-universe-swapped-real-accounts-sep11
description: "Sep 11 2026, the TAM engine's seed CSVs were replaced by a 16-account sourced net-new universe (every row cites employees, labels agent_count as public or banded ESTIMATE, carries PredictLeads tech reads with dates, 34 URL-cited triggers); snapshot published, brain strike_list serves 16 cited rows; seed CSVs kept only as the test fixture"
metadata:
  type: project
---

Built Sep 11 2026 on Dallas's ask ("swap the TAM seed data for real accounts").

**Universe (16, all Salesforce Prospects, none on the customer denylist):** centene.com (Sep 5 row kept, fourth trigger now sourced to the Apr 6 2026 restructure release), medica.com, point32health.org, blueshieldca.com, cambiahealth.com, iehp.org, statefarm.com, truist.com, regions.com, td.com, fidelity.com, breadfinancial.com, lincolnfinancial.com, onemain.com, nationalgrid.com, paychex.com.

**Left out, and why:** healthfirst.org, amerihealthcaritas.com, lv.com, cunamutual.com (TruStage) have no sourceable employee count (AmeriHealth's fact-sheet PDF and LV's Companies House accounts need a manual pull; TruStage is a mutual with no disclosure). navient.com excluded: servicing outsourced to a vendor in 2024, 670 employees, motion no longer fits ([[feedback-motion-fit-on-company-change]]). hcsc.com dropped from the file (confirmed customer, denylist covers it). TruStage's July 2026 cyberattack shut its contact centers for a month and claims were still backlogged Sep 4; a strong why-now with no row.

**Method:** seven signal-researcher agents (three accounts each, strongest model per [[feedback-best-model-every-account]]) returned strict JSON: employees with URL + verbatim quote, any public contact-centre headcount, up to three dated triggers since May 14 in the eight taxonomy families with verbatim quote + URL. Assembler (scratchpad assemble_tam.py, logic worth keeping) merged with data/cc_platform_reads_all_sep5.csv for acd/wfm (latest per lane, `predictleads:<vendor url>`, observed date). agent_count = public figure when one exists (only Paychex: 7,000 customer support experts, a marketing claim) else employees x ratio (Health Insurance .15, Banking .08, Financial Services .10, Insurance .10, Other .06; overrides Paychex .20, National Grid .05, OneMain .25), rounded to 100, labelled "banded ESTIMATE" with the band sensitivity in `source`. Triggers cited only to aggregators (layoffhedge, theofficialboard, rocketreach, nerdwallet) are dropped. Employee counts from stockanalysis.com (Bread, Lincoln) are filing-derived and say so, same precedent as Centene.

**Results:** ranked list has no [SEED]; Centene 88 T1, Truist 74, TD 73, Point32Health 71, Regions 70. Tests 60/60 after pointing test_account_engine.py at tests/fixture_seed/ (the old seed CSVs, frozen; the suite pins AmeriHealth fit 85 / $7.1M / copy strings). publish_gtm_state.sh --deploy published generated_at 2026-09-11T20:12:09Z, 16 accounts, 0 seed, 0 customer-excluded; local brain run against the published URL: /v1/strike and MCP strike_list both serve 16 rows with seed false and figures present. Render picks it up within the 300s TTL.

**Open:** sellers.csv has only Centene (Nathan Belfield) and Keegan Sanders on Fidelity/Bread/Lincoln (derived from SF owner id 005V5000001gAGSIA2 via Keegan's Aug 3 list; email and Slack handle CONSTRUCTED). Other SF owner ids have no name map locally. Agent-count estimates want the exact-title Audiences count per account (0 credits). The data change is uncommitted on main of the primary checkout.
