# Fable rerun prompt: QBP on my real universe and my addressability framework

Paste this entire message into the same Fable thread. No edits needed.

---

Good work on the methodology and the CMS citations. Keep that benchmark-and-rebate base intact. I need two corrections before you rerun, then a clean deliverable.

**Correction 1, the universe.** My real Star Ratings motion is the 93 contracts listed at the bottom, not the top 40 by enrollment. Use exactly this set, and use the enrollment and star values I give you. Do not substitute the figures from your earlier run.

**Correction 2, what gets measured.** Your first run computed gross forgone QBP: the entire dollar gap from being under 4.0. I sell on an addressability basis, because a finance or actuarial buyer will reject any number that assumes I can move clinical measures I cannot touch. Every contract has a measure_profile split into two star scores:
- **CS** = customer-service and administrative measures (CAHPS, complaints, call center, appeals, access, admin). Our product moves these.
- **Clin** = clinical and HEDIS measures. Our product does not move these.

Our platform (Queue Optimizer and the wider Dynamic Workforce Orchestration suite) acts on the CS side. So the number I put in front of a buyer is the CS-attributable slice of the forgone QBP, not the gross.

**Use this exact addressability formula. Do not invent your own weighting.**
```
CS_gap   = max(0, 4.0 - CS_star)
Clin_gap = max(0, 4.0 - Clin_star)

if CS_gap + Clin_gap > 0:
    addressable_pct = CS_gap / (CS_gap + Clin_gap)
else:
    addressable_pct = 0        # both sides already at/above 4.0

addressable_forgone_qbp_musd = gross_forgone_qbp_musd * addressable_pct
```
This means a contract whose clinical stars are already at or above 4.0 (Clin_gap = 0) is 100% addressable: its entire sub-4.0 problem lives on the CS side we own. A contract whose CS is already at/above 4.0 is 0% addressable and not a fit. That is the intended behavior.

**Return exactly two things:**

1. A CSV code block, columns in this exact order:
`contract_id,parent_org,marketing_name,members,cs_star,clin_star,gross_forgone_qbp_musd,addressable_forgone_qbp_musd,addressable_pct,confidence,primary_sources`
- Parse cs_star and clin_star out of the measure_profile I give you.
- Round dollar columns to one decimal, addressable_pct to two decimals (e.g. 0.57).
- Keep the same confidence and source-tag logic from your first run.

2. A short methodology addendum, CS-addressability only. State the formula above verbatim, explain in two or three sentences why the CS-attributable slice is the defensible number to show finance, and note it is a first-order model that weights by the star-level gap. Do not restate your benchmark or rebate methodology; that base stands.

Flag any contract whose measure_profile looks internally inconsistent rather than silently smoothing it. Do not drop or reorder contracts; return all 93.

**My 93-contract universe:**

```csv
contract_id,parent_org,marketing_name,members,measure_profile,current_addressable_qbp_musd
H5216,Humana,Humana,2470763,CS 3.7 / Clin 3.3,820.3
H5619,Humana,Humana,490987,CS 3.6 / Clin 3.1,163.0
H8768,UnitedHealth,UnitedHealthcare,317637,CS 3.4 / Clin 3.1,111.5
H0028,Humana,Humana,342600,CS 3.6 / Clin 3.4,113.7
H6622,Humana,Humana,341511,CS 3.6 / Clin 3.4,113.4
H0543,UnitedHealth,UnitedHealthcare,256685,CS 3.2 / Clin 3.6,85.2
H3387,UnitedHealth,UnitedHealthcare,158177,CS 3.5 / Clin 3.7,52.5
H4514,UnitedHealth,UnitedHealthcare,148399,CS 3.7 / Clin 3.2,49.3
H4604,UnitedHealth,UnitedHealthcare,139923,CS 3.8 / Clin 3.5,46.5
R7444,UnitedHealth,UnitedHealthcare,80000,CS 3.6 / Clin 3.2,28.1
H8889,Medica Holding Company,Medica,111604,CS 3.8 / Clin 3.4,37.1
H3379,UnitedHealth,UnitedHealthcare,99682,CS 3.6 / Clin 3.5,33.1
H5970,Humana,Humana,87568,CS 3.4 / Clin 3.1,29.1
H0504,California Physicians' Service,Blue Shield of California,56505,CS 3.4 / Clin 3.6,19.8
H3113,UnitedHealth,UnitedHealthcare,81332,CS 3.4 / Clin 3.3,27.0
H3817,Cambia Health Solutions  Inc.,Regence BlueCross BlueShield of Oregon,52151,CS 3.5 / Clin 3.3,18.3
H0885,Horizon Mutual Holdings  Inc,Braven Health,50096,CS 3.7 / Clin 3.3,17.6
H3528,EmblemHealth  Inc.,ConnectiCare,48699,CS 3.5 / Clin 3.4,17.1
H3931,CVS / Aetna,Aetna Medicare,71855,CS 3.7 / Clin 3.2,23.9
H2230,Blue Cross and Blue Shield of Massachusetts  Inc.,Blue Cross Blue Shield of Massachusetts,45119,CS 3.6 / Clin 3.8,15.8
H6898,Blue Cross Blue Shield of Michigan Mutual Ins. Co.,Vermont Blue Advantage,45000,CS 3.8 / Clin 3.3,15.8
H2246,Intermountain Health Care  Inc.,Select Health,45000,CS 3.6 / Clin 3.3,15.8
H8070,UCare Minnesota,UCare,45000,CS 3.8 / Clin 3.8,15.8
H0302,Blue Cross Blue Shield of Arizona,Blue Cross Blue Shield of Arizona (AZ Blue),43003,CS 3.1 / Clin 4.0,15.1
H2261,Blue Cross and Blue Shield of Massachusetts  Inc.,Blue Cross Blue Shield of Massachusetts,41074,CS 3.9 / Clin 3.5,14.4
H5549,Visiting Nurse Service of New York,VNS Health Medicare,60060,CS 2.8 / Clin 4.4,19.9
H0174,Centene,Wellcare,57828,CS 3.4 / Clin 3.0,19.2
H3330,EmblemHealth  Inc.,EmblemHealth,35500,CS 3.5 / Clin 3.1,12.5
H3864,PacificSource,PacificSource Medicare,53306,CS 3.6 / Clin 3.1,17.7
H1032,Centene,Wellcare,50482,CS 3.6 / Clin 3.5,16.8
H5496,Imperial Health Plan of California,Imperial Health Plan of California  Inc.,49913,CS 2.7 / Clin 4.3,16.6
H4506,Centene,Wellcare,29470,CS 3.6 / Clin 3.6,10.3
H4868,Centene,Wellcare,42434,CS 3.3 / Clin 3.2,14.1
H2247,UnitedHealth,UnitedHealthcare,39257,CS 3.3 / Clin 2.8,13.0
H3949,The Cigna Group,Cigna Healthcare,37336,CS 3.5 / Clin 3.6,12.4
H6453,Louisiana Health Service & Indemnity Company,Blue Cross and Blue Shield of Louisiana,36665,CS 3.8 / Clin 3.4,12.2
H5854,Elevance,Anthem Blue Cross and Blue Shield,35903,CS 3.5 / Clin 3.3,11.9
H3832,Hawaii Medical Service Association,HMSA Akamai Advantage,35723,CS 3.6 / Clin 3.3,11.9
H4624,Zing Health Consolidator  Inc,Zing Health,32919,CS 3.1 / Clin 3.2,10.9
H0624,UnitedHealth,UnitedHealthcare,32447,CS 3.0 / Clin 3.5,10.8
H6396,CareSource,CareSource,29364,CS 3.4 / Clin 3.5,9.7
H8634,HCSC,Blue Cross and Blue Shield of IL  NM,27389,CS 3.5 / Clin 3.1,9.1
H3192,CVS / Aetna,Aetna Medicare,26877,CS 3.7 / Clin 3.3,8.9
H8298,Horizon Mutual Holdings  Inc,Horizon Blue Cross Blue Shield of New Jersey,25926,CS 3.5 / Clin 3.5,8.6
H5590,Centene,Wellcare by Allwell,25825,CS 3.4 / Clin 2.9,8.6
H9485,Mass General Brigham Incorporated,Mass General Brigham Health Plan,17040,CS 3.8 / Clin 3.7,6.0
H9207,Thomas Jefferson University,Jefferson Health Plans,25023,CS 3.8 / Clin 3.5,8.3
H2226,UnitedHealth,UnitedHealthcare,24604,CS 3.4 / Clin 4.0,8.2
H2225,Commonwealth Care Alliance  Inc.,Commonwealth Care Alliance Massachusetts,18086,CS 3.7 / Clin 4.0,6.0
H7220,Indiana University Health,Indiana University Health Plans,11476,CS 3.4 / Clin 3.4,4.0
H4623,Humana,Humana,11445,CS 3.6 / Clin 3.2,4.0
H5273,Point32Health  Inc.,CarePartners of Connecticut,11033,CS 3.7 / Clin 3.5,3.9
H8597,CVS / Aetna,Aetna Medicare,15267,CS 3.3 / Clin 3.4,5.1
H8578,Baystate Health  Inc.,Health New England Medicare Advantage Plans,9748,CS 3.4 / Clin 3.5,3.4
H2686,Devoted Health  Inc.,Devoted Health,9481,CS 3.4 / Clin 4.2,3.3
H5859,CareOregon  Inc.,CareOregon Advantage,13962,CS 3.3 / Clin 3.3,4.6
H9306,LifeBridge Health  Inc.,Alterwood Advantage,13103,CS 3.4 / Clin 3.0,4.4
H1607,Elevance,Anthem Blue Cross and Blue Shield,8508,CS 3.5 / Clin 3.2,3.0
H5928,California Physicians' Service,Blue Shield of California,8167,CS 3.4 / Clin 3.4,2.9
H1914,Centene,Wellcare,12143,CS 3.2 / Clin 3.0,4.0
H9585,BMC Health System  Inc.,WellSense Health Plan,12000,CS 3.3 / Clin 3.9,4.0
H9763,Ochsner Clinic Foundation,Ochsner Health Plan,12000,CS 3.5 / Clin 3.5,4.0
H2425,Aware Integrated  Inc.,Blue Plus,11563,CS 3.7 / Clin 3.5,3.8
H2056,CVS / Aetna,Aetna Medicare,7272,CS 3.3 / Clin 3.0,2.6
H4931,Banner Health,Banner Medicare Advantage,10955,CS 3.4 / Clin 3.0,3.6
H2224,Molina,Senior Whole Health,10836,CS 3.7 / Clin 3.7,3.6
H5843,Banner Health,Banner Medicare Advantage,6977,CS 3.6 / Clin 3.1,2.4
H4005,Guidewell Mutual Holding Corporation,Triple-S Advantage,6676,CS 3.7 / Clin 3.5,2.3
H8928,Fallon Community Health Plan  Inc.,Fallon Health,9927,CS 3.7 / Clin 3.9,3.3
H3080,Devoted Health  Inc.,Devoted Health,9657,CS 3.1 / Clin 3.7,3.2
H1822,SCAN Group,SCAN Health Plan,9248,CS 3.1 / Clin 3.7,3.1
H3443,Alignment Healthcare USA  LLC,Alignment Health Plan,9056,CS 3.1 / Clin 4.5,3.0
H4711,CVS / Aetna,Aetna Medicare,8582,CS 3.3 / Clin 3.0,2.8
H0712,Centene,Wellcare,7571,CS 3.5 / Clin 3.2,2.5
H2737,Baystate Health  Inc.,Health New England Medicare Advantage Plans,4854,CS 3.6 / Clin 3.6,1.7
H2486,Humana,Humana,4301,CS 3.4 / Clin 3.2,1.5
H8010,Clover Health Holdings  Inc.,Clover Health,3632,CS 3.1 / Clin 3.8,1.3
H6988,Centers Plan for Healthy Living  LLC,Centers Plan for Healthy Living,5464,CS 3.0 / Clin 4.4,1.8
H9884,Devoted Health  Inc.,Devoted Health,3531,CS 3.1 / Clin 3.9,1.2
H0978,SCAN Group,SCAN Health Plan,5207,CS 3.1 / Clin 4.0,1.7
H5608,Denver Health and Hospital Authority,Elevate Medicare Advantage,5091,CS 3.4 / Clin 3.7,1.7
H6545,Devoted Health  Inc.,Devoted Health,2593,CS 3.1 / Clin 4.4,0.9
H9907,Point32Health  Inc.,Tufts Health Plan,1958,CS 3.4 / Clin 3.5,0.7
H1360,UnitedHealth,UnitedHealthcare,2653,CS 3.3 / Clin 3.3,0.9
H5209,Molina,My Choice Wisconsin,2555,CS 3.1 / Clin 3.3,0.8
H8547,HCSC,Blue Cross and Blue Shield of Illinois,1577,CS 3.7 / Clin 3.7,0.6
H5991,EmblemHealth  Inc.,EmblemHealth,2332,CS 3.2 / Clin 3.0,0.8
H9191,Rifkin Managed Care Holding  LLC,Provider Partners Health Plans,1359,CS 3.4 / Clin 3.5,0.5
H8649,CVS / Aetna,Aetna Medicare,1331,CS 3.6 / Clin 3.2,0.4
H3800,Rifkin Managed Care Holding  LLC,Provider Partners Health Plans,1207,CS 3.7 / Clin 3.2,0.4
H2237,Humana,iCare,898,CS 3.6 / Clin 3.1,0.3
H1644,Longevity Health Founders  LLC,Longevity Health Plan,898,CS 3.4 / Clin 3.4,0.3
H5852,AIDS Healthcare Foundation,AHF,607,CS 3.5 / Clin 3.2,0.2
```
