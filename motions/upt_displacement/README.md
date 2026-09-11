# UPT displacement (Verint attack, NICE attack)

Started Sep 9 2026 from Naveen's Sep 8 1:1 ask: two lists of companies running Verint DPA and NICE Desktop Analytics, front and back office, the DWO contacts at each, and a recommended sequence per attack, ready for his Thursday Sep 10 meeting with John. Product: User Productivity Tracking (UPT), the desktop layer.

| File | What |
|---|---|
| `UPT_Attack_Brief_Sep10.html` | The one-page brief for Naveen and John. Live at https://gtm-operating-map.pages.dev/upt-attack-brief/ (subpath of the operating-map Pages project; deploy folder `~/Desktop/Intradiem Deliverables/deploy-gtm-operating-map/upt-attack-brief/`, copy the built page to index.html there and redeploy the folder with the operating-map command). Also on the Desktop under Intradiem Deliverables. Built by `build_attack_brief.py`. Pre-send edits Sep 9: no gate detail or customer names on the page, one rendered email with the swap label, Nate cited as a field read, tier-D opener variant in the sequences file. |
| `UPT_Attack_Sequences_Sep9.md` | Verint attack and NICE attack copy: four angles, the Sep 4 cadence, Email 1 to 5, calls, voicemails, LinkedIn, QC lines 1 to 12. |
| `build_lists.py` | Writes `lists/verint_estate.csv` (60) and `lists/nice_estate.csv` (142); Verizon and The Hartford are added to the Verint estate by profile evidence (stack read shows NICE only) from the Sep 9 Audiences pull, drops customers, splits six-vertical fit, joins the DWO wave-1 executives. 0 credits. |
| `lists/sku_signals.json` | The Sep 9 desktop-analytics signal sweep: 34 accounts with a public vendor or module signal, tier, quote, source URL, date, NICE use tag. |
| `lists/found_outside_list.json` | Named desktop-analytics users not on either list (Continuum Global Solutions, Absa) plus two customer references (Cigna postings, Guardian Life story). |
| `lists/summary.json` | Counts the page reads, tiers and NICE tags included. |
| `lists/segments_made.json` | The six saved Audiences segments (two company, four people) with ids. |
| `lists/excluded_customers.csv` | The 11 SF customers, 7 registry or parent-company holds (Duke Energy, Optum360, Aetna subsidiary, Express Scripts, American Bankers Life, Oak Street Health, BT Business), 2 merged entities (First Utility, Vivint Solar) and 1 blank-type account held out. |

## Evidence tiers (sweep of Sep 9 2026)
A = the desktop-analytics module named for this account, from a vendor case study, a current-role profile that names the product, or the rep's read: BCBS Louisiana, New York Life (Head of WFM and a systems admin), Blue Shield of California (WFM Lead), Verizon (Verint support for 60K subscribers), The Hartford, Allstate (a Speech and Desktop Analytics consultant on staff), Gainwell, TTEC, Teleperformance, and Maximus at A- (Nate's read plus a matching blinded Verint story). B = vendor confirmed in public, module not named. C = third-party listing or an unconfirmed profile match. D = stack read only. NICE rows carry a use tag.

Method: both vendors' case-study and press archives, public board packets, job boards, AppsRunTheWorld; then a Clay profile search (0 credits) across all list domains on the product terms in headline, about and current-role text, with Enrich Person (0.5 cr each, 10 profiles) to read the exact sentence. Clay's job-posting index returned nothing for the terms. Skills sections are not searchable; a Sales Navigator skills pass by Nate remains the one unreached source.

## The honest limit
No stack-read source detects the desktop-analytics module as a product; PredictLeads sees Verint WFM and NICE CXone/inContact/WFM. The lists are vendor estates. The `evidence_tier`, `sku_signal`, `sku_signal_source`, `sku_signal_date` and `nice_use_tag` columns come from `lists/sku_signals.json`; blank signal means tier D. Maximus is the rep-confirmed worked example (Nate, Sep 4). No account loads without a signal.

## Rules carried
Module, never the layer (Verint WFM and NICE are integration partners; the UK base runs NICE IEX). Verint first, NICE second (Nate's Aug 18 and Sep 4 field reads). Operating executives at 53 of these accounts are already in the DWO Executives campaign and never get a second sequence. Verified numbers only; customer exclusion at build and at load; Nate reads every wave; nothing sends from Dallas's hand.
