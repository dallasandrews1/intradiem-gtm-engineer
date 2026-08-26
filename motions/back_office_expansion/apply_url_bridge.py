#!/usr/bin/env python3
"""Apply the Clay MCP find-and-enrich-list-of-contacts results (Aug 25 2026, 0 credits) to inger_backoffice_candidates.csv.
Fills linkedin_url, refreshes title from the live profile, and excludes people the bridge shows have left the account."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "inger_backoffice_candidates.csv")

# name_key -> (url, current_company, current_title)
B = {
"Don Johnson":("https://www.linkedin.com/in/don-johnson-3a583925/","Assurant","SVP Global Housing P&C Claims"),
"Tania Sanfiel":("https://www.linkedin.com/in/taniasanfiel/","Assurant","AVP, Claims Strategy and Transformation"),
"Jack Nicholls":("https://www.linkedin.com/in/jack-nicholls-b8a21938/","Assurant","AVP, Claims"),
"Molly Parker Miller":("https://www.linkedin.com/in/molly-parker-miller-7aa780103/","Assurant","AVP, Financial Services Claims"),
"Alan Haskins":("https://www.linkedin.com/in/alan-haskins-0421138/","Assurant","Vice President, Global Claims Fraud Risk Mitigation"),
"Michael Campbell":("https://www.linkedin.com/in/michaelcampbellinsurance/","Assurant","Chief Operating Officer - Assurant Inc."),
"Susan Heiden":("https://www.linkedin.com/in/susan-heiden-981379/","Assurant","Senior Director Claims Business Technology"),
"Amber Gladman":("https://www.linkedin.com/in/amber-gladman-038bbb214/","Assurant","Director, Loss Drafts Business Process Management"),
"Alina Socarras":("https://www.linkedin.com/in/alinasocarras/","Prudential Financial","Manager, Comptroller's Department"),
"Patricia Quint":("https://www.linkedin.com/in/patricia-quint-8418b33b/","Assurant","Vice President Claims"),
"Bryan Gofus":("https://www.linkedin.com/in/bryan-gofus-6217783b/","Assurant","Director of Claims"),
"Ron Norman":("https://www.linkedin.com/in/ron-norman-88660614/","Assurant","Claims Director"),
"Susan Beck":("https://www.linkedin.com/in/susan-beck-205084343/","Assurant","Vice President of Quality and Shared Services"),
"John Singleton":("https://www.linkedin.com/in/john-singleton-mba-75a00226/","Assurant","Vice President Homeowners-LPI & Shared Services"),
"Dimitry DiRienzo":("https://www.linkedin.com/in/dimitry-dirienzo-bb0175b/","Assurant","Chief Accounting Officer and Controller"),
"Sarah Charai":("https://www.linkedin.com/in/sarah-charai/","Cleveland Clinic","Executive Director, Supply Chain Operations"),
"Lauren Klein":("","", ""),
"Kimberly Kotora":("https://www.linkedin.com/in/kimberly-kotora-mba-bsn-ne-bc/","Allegheny Health Network","Vice President, Hospital and Institute Philanthropy"),
"Scott Dwyer":("https://www.linkedin.com/in/scott-dwyer-17844a5/","Cleveland Clinic","Senior Director Supply Chain Management - Commodity Sourcing"),
"Kevin Nelson":("https://www.linkedin.com/in/kevin-nelson-80232713/","Cleveland Clinic","Senior Director International and Emerging Markets Finance Operations"),
"James Millar":("https://www.linkedin.com/in/james-millar-7980522b/","Cleveland Clinic","Enterprise Director of Continuous Improvement - Shared Services"),
"Michael Waterman":("https://www.linkedin.com/in/michael-waterman-15b8a711/","Cleveland Clinic","CI Director II, Clinical Shared Services"),
"Tracy Peffley":("https://www.linkedin.com/in/tracy-peffley-0566488/","Cleveland Clinic","Vice President, Revenue Cycle Management"),
"Daniel Medve":("https://www.linkedin.com/in/daniel-medve-60a7666/","Cleveland Clinic","Director, Revenue Cycle Management"),
"Nick Judd":("https://www.linkedin.com/in/nick-judd-mba-rhia-b2847571/","Cleveland Clinic","Executive Director, HIM and Clinical Revenue Cycle Services"),
"Deborah Knight-Lauricia":("https://www.linkedin.com/in/dlauricia/","Cleveland Clinic","Senior Director, Revenue Cycle"),
"Michelle Rigsby":("https://www.linkedin.com/in/michelle-rigsby-79b79710a/","Cleveland Clinic","Senior Director HR - Shared Services"),
"Janice Murphy":("https://www.linkedin.com/in/janice-murphy-44aa32111/","Cleveland Clinic","Chief Operating Officer Regional Hospitals and FHC"),
"Diane Costa":("https://www.linkedin.com/in/diane-costa-b62a13a/","Cleveland Clinic","Director-Patient Financial Services"),
"K. Kelly Hancock":("https://www.linkedin.com/in/k-kelly-hancock-dnp-rn-ne-bc-faan-93325974/","Cleveland Clinic","Executive Vice President, Chief Caregiver Officer & Chief Administrative Officer"),
"David Burns":("https://www.linkedin.com/in/david-burns-5692803/","Cox Communications","AVP/Executive Director - Network Automation & Shared Services"),
"Montie Pace":("https://www.linkedin.com/in/montie-pace-41373455/","Cox Communications","Senior Vice President of Business Operations"),
"Michele Eramian":("https://www.linkedin.com/in/michele-eramian-a429973/","Cox Communications","Assistant Vice President - Business Operations, Finance & Analysis"),
"Syed Ahmed":("https://www.linkedin.com/in/syed-i-ahmed/","Cox Communications","Senior Director, Order Management & Recovery Services"),
"Greg Horton":("https://www.linkedin.com/in/greg-horton-08614a2/","Cox Communications","Director, Cox Business Operations"),
"Bob Kantoris":("https://www.linkedin.com/in/bob-kantoris-17aa81/","Cox Communications","Director Operations Management"),
"Kathy Grimes":("https://www.linkedin.com/in/kathy-grimes-123221b/","Cox Communications","VP of Business Operations"),
"Daniel Houck":("https://www.linkedin.com/in/daniel-houck-277a0626/","Cox Enterprises","Director Facilities and Sustainability"),
"Kathryn Nix":("https://www.linkedin.com/in/kathryn-nix-3004015/","Cox Communications","Sr. Director, Fraud & Credit Strategy & Analytics"),
"Jim Bolzenius":("https://www.linkedin.com/in/jim-bolzenius-91657265/","Cox Communications","Vice President Fraud, Credit and Revenue Operations"),
"Jim Miller":("https://www.linkedin.com/in/jim-miller-94b87572/","Cox Communications","Sr. Director, Fraud Operations"),
"Amanda King":("https://www.linkedin.com/in/amandashuking/","Cox Communications","Sr. Director, Commercial Billing and Collections"),
"Steve Chapman":("https://www.linkedin.com/in/steve-chapman-84415910/","Cox Communications","Regional Director, Collections and Loss Prevention"),
"Colleen McKay Langner":("https://www.linkedin.com/in/colleen-mckay-langner/","Cox Communications","Executive Vice President, Chief Residential Officer"),
"Heather Manning":("https://www.linkedin.com/in/heather-manning-a242aaa/","Cox Communications","CFO, Residential Division"),
"Ann Whalen":("https://www.linkedin.com/in/ann-whalen/","DIRECTV","Sr. Director of Billing Operations"),
"Tom Lockwood":("https://www.linkedin.com/in/tom-lockwood-287575a/","DIRECTV","Director of Business Operations"),
"Kailey Matthews":("https://www.linkedin.com/in/kailey-matthews-453a4153/","DIRECTV","AVP, Business Operations"),
"Donja Wehrfritz":("https://www.linkedin.com/in/donja-wehrfritz-36a6603/","DIRECTV","Senior Director - Business Operations"),
"Bert Cabello Jr":("https://www.linkedin.com/in/bert-cabello-jr-39284127/","DIRECTV","Director of Business Operations"),
"Kara Johnson":("https://www.linkedin.com/in/kara-johnson-45535822/","DIRECTV","AVP Business Operations"),
"Jeff Bollaro":("https://www.linkedin.com/in/jeff-bollaro-6b8a56a8/","DIRECTV","Sr. Director, Business Operations"),
"Christopher Brady":("https://www.linkedin.com/in/christopher-brady-23136445/","DIRECTV","Senior Director Business Operations"),
"Mary Ann Jensen":("https://www.linkedin.com/in/mary-ann-jensen-1b7b673/","DIRECTV","Associate Director, Global Billing Operations - Data Services"),
"Alemseged Starling":("https://www.linkedin.com/in/alemseged-starling-48748b9/","DIRECTV","Director, Business Operations"),
"Shereen Small":("https://www.linkedin.com/in/shereen-small-020a3a145/","DIRECTV","Director, Business Operations"),
"Michael W.":("https://www.linkedin.com/in/michael-w-809564218/","DIRECTV","Chief Operating Officer"),
"Amiena Murad":("https://www.linkedin.com/in/amiena-murad-b938a033/","DIRECTV","Sr. Director Business Operations"),
"Shane Rutledge":("https://www.linkedin.com/in/shane-rutledge-43372699/","DIRECTV","Director of Business Operations"),
"Ray C.":("https://www.linkedin.com/in/raycarp/","DIRECTV","Chief Financial Officer"),
"Manavjeet Singh":("https://www.linkedin.com/in/manavjeet/","Guardian Life","Head of Group Benefits Operations Technology"),
"Matthew Darula":("https://www.linkedin.com/in/matthewdarula/","Guardian Life","Head of Business Operations and Experience, Financial Protection and Retirement Solutions"),
"Garlande Patz":("https://www.linkedin.com/in/garlande-patz-mba-clms-69100452/","Guardian Life","Head of Business Transformation, Group Claims"),
"Kathy Earle":("https://www.linkedin.com/in/kathleen-earle-b771189/","Guardian Life","Head of Claims & Service Finance"),
"Sandra McKenna":("https://www.linkedin.com/in/sandra-mckenna-562b79a/","Guardian Life","Head of Operations, Service, Claims and Transformation, Shared Services, Group Benefits"),
"Jane M Elliott":("https://www.linkedin.com/in/jane-m-elliott-mba-b397b3a/","Guardian Life","Head of Group Benefits Underwriting Process & Technology"),
"Patrick Ouellette":("https://www.linkedin.com/in/patrick-ouellette/","Guardian Life","Head of Group Benefits Claims Technology"),
"Brad Nowers":("https://www.linkedin.com/in/brad-nowers-90638690/","Guardian Life","Head of FP&A for Underwriting & Operations, Group Benefits"),
"Meredith Heibert":("https://www.linkedin.com/in/meredith-heibert-140102116/","Guardian Life","Head of Life & Annuity Claims"),
"Nora Bargfrede":("https://www.linkedin.com/in/nora-bargfrede-9a89b277/","Guardian Life","Head of Disability Clinical, Group Claims"),
"Micah Pace":("https://www.linkedin.com/in/micah-pace-36b1b721/","Guardian Life","Head of Underwriting Operations"),
"Melanie Wiltrout":("https://www.linkedin.com/in/melanie-wiltrout/","Guardian Life","Head of Best Practices, Group Claims & Service"),
"Kevin Molloy":("https://www.linkedin.com/in/kevinmolloy212/","Guardian Life","Chief Financial Officer"),
"Maria Milazzo":("https://www.linkedin.com/in/maria-milazzo/","Guardian Life","CFO, Group Insurance"),
"Stuart Staggs":("https://www.linkedin.com/in/stuart-staggs-5b7a877/","McKesson","Vice President, Transformation & Shared Services"),
"Carla McKinnie":("https://www.linkedin.com/in/carla-mckinnie-7b40b428/","McKesson","Senior Director Shared Services Accounting"),
"Elyse Baksh Lowe":("https://www.linkedin.com/in/elyse-baksh/","McKesson","Director of Internal Controls - Financial Shared Services"),
"Humeyra Etik":("https://www.linkedin.com/in/humeyra-etik-04bbaa35/","McKesson","Director of Business Operations"),
"Francisco Fernandez":("https://www.linkedin.com/in/francisco-fernandez-055766a/","McKesson","Director, FP&A – Financial Shared Services"),
"JA Reynolds RMC":("https://www.linkedin.com/in/reynoldsja/","McKesson","Chief Operating Officer"),
"Napoleon Rutledge":("https://www.linkedin.com/in/napoleon-rutledge-0688558/","McKesson","Chief Accounting Officer (CAO)"),
"Traci Shaw":("https://www.linkedin.com/in/traci-shaw-a1b5ba15/","McKesson","Director, Business Operations CoverMyMeds - Pharmacy and Affordability"),
"Greg Dye":("https://www.linkedin.com/in/greg-dye-794a2213/","McKesson","Director, Business Operations"),
"Tim Davis":("https://www.linkedin.com/in/tim-davis-8463792/","McKesson","Director, Accounting Shared Services"),
"Jenefer Hughes":("https://www.linkedin.com/in/jenefer-hughes-8246255a/","Chesterfield County","Commissioner of the Revenue"),
"Justin Bowers":("https://www.linkedin.com/in/jjbowers/","McKesson","Senior Vice President & General Manager, Finance Shared Services"),
"Andrew N.":("https://www.linkedin.com/in/andrew-nikolishyn/","Rogers Communications","Senior Director Credit Risk, Collections & Fraud Management"),
"Andrew Masson":("https://www.linkedin.com/in/andrew-masson-8331797/","Rogers Communications","Sr. Director HR, Business Operations at Rogers"),
"Dave Difelice":("https://www.linkedin.com/in/dave-difelice/","Rogers Communications","COO Rogers Bank"),
"Aaron Conlin":("https://www.linkedin.com/in/aaron-conlin-b5640529/","Rogers Communications","Director Shared Services"),
"Haris Alukic":("https://www.linkedin.com/in/haris-alukic-7898b888/","Rogers Communications","Senior Director, Collections and Recovery Program"),
"Jerry Janicki":("https://www.linkedin.com/in/jerry-janicki-5168815/","Rogers Communications","Sr. Director., Provisioning, MW, Core Services"),
"Glenn Brandt":("https://www.linkedin.com/in/glenn-brandt-70907b10/","Rogers Communications","Chief Financial Officer"),
"Jason Giff":("https://www.linkedin.com/in/jasongiff/","Rogers Communications","Senior Director Of Operations"),
"Cory Chemerys":("https://www.linkedin.com/in/cory-chemerys-503556130/","Rogers Communications","Director of Operations"),
"Everton Chin":("https://www.linkedin.com/in/everton-chin-mba-15783718/","Travelers","Senior Director, Business Process Management"),
"Esther M.":("https://www.linkedin.com/in/esther-m-9b4567106/","Travelers","Director Property Claims Management"),
"Kimberly Garth":("https://www.linkedin.com/in/kimberly-garth/","Travelers","Director, Business Process Management"),
"Elaine Baisden":("https://www.linkedin.com/in/elaine-baisden-a095575/","Travelers","Senior Vice President Operations, Personal Insurance"),
"Robert DeStefano":("https://www.linkedin.com/in/robert-destefano-1437b853/","Home","Retired"),
"David Lanciano":("https://www.linkedin.com/in/david-lanciano-ccla-85057b49/","Travelers","Director, Business Delivery - Claim Shared Services"),
"Cynthia Finley":("https://www.linkedin.com/in/cynthia-finley-30b7482b/","Travelers","Senior Director Billing Operations"),
"Gary Pedvin":("https://www.linkedin.com/in/garypedvin/","Travelers","Senior Director, Operational Effectiveness/Business Insurance Operations Quality Lead"),
"Andy Bessette":("https://www.linkedin.com/in/andy-bessette-499923121/","Travelers","Executive Vice President and Chief Administrative Officer"),
"Amy Millen":("https://www.linkedin.com/in/amy-millen-26a75b15b/","Travelers","AVP, Billing Operations"),
"Chris Miller":("https://www.linkedin.com/in/sophia-john-893995122/","Travelers","Chief Operating Officer"),
"Tom Ignaffo":("https://www.linkedin.com/in/tom-ignaffo-jr-mba-01984112/","Travelers","AVP Claim Shared Services Operations"),
"Bryan Ott":("https://www.linkedin.com/in/ott-mba/","Travelers","Managing Director, Claim Shared Services Operations"),
"Vincent Seaver":("https://www.linkedin.com/in/vincent-seaver/","Travelers","Vice President, Business Insurance Operations"),
"Ruki Mazumdar":("https://www.linkedin.com/in/ruki-mazumdar-5354922/","Travelers","Vice President - Bond & Specialty Insurance Operations"),
"Barry Perkins":("https://www.linkedin.com/in/barry-perkins-1a922b14/","Zurich North America","Chief Operating Officer ZNA"),
"Terry-Dawn Thomas":("https://www.linkedin.com/in/terry-dawn-thomas-1259161b6/","Zurich North America","Head of Technical Underwriting Operations & Sustainability"),
"Thomas Markun":("https://www.linkedin.com/in/thomas-markun-955ba18/","Zurich North America","Vice President, Finance Operations"),
"Rajiv Rao":("https://www.linkedin.com/in/rajiv-rao-9023a61/","Zurich North America","AVP - Operations Management"),
"Diana Wirkus":("https://www.linkedin.com/in/dianawirkus/","Zurich North America","Head of Claims Operations"),
"Laura Boehm":("https://www.linkedin.com/in/laura-boehm-3538a693/","Zurich North America","Director of Underwriting Services"),
"Karen Anderson":("https://www.linkedin.com/in/karen-anderson-15266182/","Zurich North America","AVP Finance Operations"),
"Ewa Peczkowicz":("https://www.linkedin.com/in/ewa-peczkowicz/","Zurich North America","Head of Claims Shared Services"),
"Keith Daly":("https://www.linkedin.com/in/kgdalyzna/","Zurich North America","Chief Claims Officer"),
"Shelley Garrett":("https://www.linkedin.com/in/shelley-garrett-90020a48/","Zurich North America","Regional Finance & Insurance Executive"),
"Carlos Gallardo":("https://www.linkedin.com/in/carlosgallardo3611/","Zurich North America","Regional F&I Executive"),
"Chavonne Hudson":("https://www.linkedin.com/in/chavonnehudson/","Zurich North America","Head of Operational Performance & Domestic Servicing"),
"Elijah A.":("https://www.linkedin.com/in/eadedire/","Zurich North America","VP, Multinational Servicing Leader - Large Property"),
"Cody Bonham":("https://www.linkedin.com/in/codybonham/","Zurich North America","VP, Multinational Casualty Servicing Leader"),
"Brian Parotto":("https://www.linkedin.com/in/brian-parotto-aa85576/","Zurich North America","AVP, Billing & Collections"),
}
ACCT_CO = {"Assurant":"Assurant","Cleveland Clinic":"Cleveland Clinic","Cox Communications":"Cox Communications","DIRECTV":"DIRECTV",
           "Guardian Life":"Guardian Life","McKesson":"McKesson","Rogers Communications":"Rogers Communications","Travelers":"Travelers","Zurich North America":"Zurich North America"}
# extra manual exclusions from the bridge read
MANUAL = {"Chris Miller": "profile URL does not match the name (sophia-john); unverifiable",
          "Shelley Garrett": "F&I executive (dealer finance sales), not back-office ops",
          "Carlos Gallardo": "F&I executive (dealer finance sales), not back-office ops",
          "Mary Ann Jensen": "Associate Director, below band",
          "Jerry Janicki": "network provisioning / core services, technical not administrative"}

rows = list(csv.DictReader(open(P)))
cols = list(rows[0].keys())
filled = left = 0
for r in rows:
    if r["excluded_reason"].strip():
        continue
    key = r["full_name"].split(",")[0].strip()
    b = B.get(key)
    if b is None:
        continue
    url, co, title = b
    if not url:
        r["excluded_reason"] = "not found by the URL bridge"; continue
    r["linkedin_url"] = url
    if co != ACCT_CO[r["account"]]:
        r["excluded_reason"] = f"no longer at account per live profile (now {co}: {title})"; left += 1; continue
    if key in MANUAL:
        r["excluded_reason"] = MANUAL[key]; continue
    r["title"] = title
    filled += 1
with open(P, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
kept = sum(1 for r in rows if not r["excluded_reason"].strip())
print(f"urls filled {filled}, left account {left}, kept now {kept}")
