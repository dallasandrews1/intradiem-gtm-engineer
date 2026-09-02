# Avaya, EMEA channel research pass (Sep 2 2026, signal-researcher, public sources only)

## Vendor context

Avaya filed a prepackaged Chapter 11 on Feb 14 2023 and emerged May 1 2023 with roughly $3B of debt removed and $650M liquidity (Avaya newsroom, May 1 2023). Since then it has narrowed to large enterprise: analysts and Avaya's own briefings describe a focus on its top ~1,500 customers (No Jitter, Apr 23 2025), and on Feb 17 2025 it announced a 200-seat monthly minimum for AXP Public from Jun 30 2025, discontinuation of SIP trunking and CPaaS on Apr 28 2025, and pushed sub-200-seat customers to cancel, upsize, or move via partners, naming BT, Maintel and Sabio as certified BYOC options (CX Today, Feb 17 2025). Avaya Infinity was announced Apr 22 2025 (Avaya newsroom) with a 2026 update Apr 16 2026. The partner program is still Avaya Edge with gem tiers Diamond/Sapphire/Emerald (Channel Futures, program launch coverage 2017-2019; partner sites in 2024-2026 still self-describe as "Edge Diamond"); a third-party listing updated Aug 2026 describes levels "Select through Diamond," so current tier naming is not confirmable from Avaya's own site (avaya.com/en/partners returned 404 on Sep 2 2026). CRN gave the program a 5-star rating for the 17th year on Mar 24 2025. EMEA route to market: Westcon-Comstor was named Avaya's Master Agent/Distributor for EMEA (Westcon announcement, 2021), is master agent for Avaya cloud/CCaaS across Europe (IT Europa 2021), holds Diamond status and claims one of the largest Avaya stock holdings in distribution (Westcon UK Avaya vendor page, fetched Sep 2 2026), and sponsored the PCC EMEA Spring Conference in Brussels Apr 14-17 2024 where Fadi Moubarak spoke as VP Channels Avaya International. On Sep 25 2024 Moubarak became VP Sales and Channels for Middle East, Africa and Central Asia, with Avaya stating "many of our largest and most advanced global customers are based in this region." No other EMEA distributor (ScanSource, TD Synnex, Ingram Micro, Nuvias/Infinigate, ALSO) could be verified as a current Avaya distributor from 2024-2026 sources; the only TD Synnex evidence is an undated Azlan UK release. Published share: Metrigy puts Avaya at 37.5% of global dedicated/on-prem contact center platform revenue in 3Q25 (Jan 7 2026); IDC's "European Contact Center Market Shares, 2024" (doc EUR153039425, Oct 2025) reportedly ranks Genesys, Avaya, Zendesk as the top three in Europe but the abstract was not retrievable (403), so treat as unverified. No public EMEA-specific Avaya share percentage was found; last public EMEA revenue mix is pre-restructuring (28% of revenue in Q3 FY2014; EMEA $1,073M in FY2015, SEC filings).

## PARTNERS

```json
[
  {
    "name": "Westcon-Comstor",
    "hq_country": "United Kingdom (Westcon International, Datatec group)",
    "emea_coverage": ["UK", "Ireland", "DACH", "Benelux", "France", "Nordics", "Iberia", "Italy", "CEE", "Middle East", "Africa"],
    "partner_type": "distributor",
    "avaya_relationship": "Master Agent/Distributor EMEA (2021 award); Avaya Diamond Partner and Authorised Avaya Learning Partner",
    "evidence": "Named Avaya Master Agent/Distributor for EMEA in 2021, master agent for Avaya CCaaS across Europe after a UK pilot, and its UK vendor page still lists AXP, Avaya Cloud Office, Spaces and devices with Diamond status; sponsored PCC EMEA 2024 in Brussels.",
    "also_carries": ["AWS (Europe distribution agreement, Westcon announcement 2024)", "Cisco, Juniper, CrowdStrike and other Comstor/Westcon lines (Westcon news 2024-2025)"],
    "scale_signal": "Claims one of the largest Avaya stock holdings in distribution (Westcon UK Avaya page, fetched Sep 2 2026); no Avaya-specific revenue disclosed",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.westconcomstor.com/global/en/news/announcements/westcon-named-avaya-s-master-agent-distributor-for-emea-2021.html", "date": "2021", "note": "Master Agent/Distributor EMEA award, regions EMEA and APAC"},
      {"url": "https://www.westconcomstor.com/uk/en/vendors/avaya.html", "date": "fetched 2026-09-02", "note": "Diamond, Learning Partner, AXP/ACO/Spaces, stock holding claim"},
      {"url": "https://iteuropa.com/news/westcon-secures-european-master-agent-deal-avaya-ccaas", "date": "2021", "note": "CCaaS master agent extended from UK to all Europe"},
      {"url": "https://partners.avaya.com/ev-emea-pcc24-brussels", "date": "2024-04-14", "note": "Sponsor of PCC EMEA Spring Conference 2024"}
    ]
  },
  {
    "name": "Sabio Group",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Spain", "France", "Netherlands", "Denmark", "South Africa"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Diamond Edge Partner (self-described, nearly 30 years); Avaya Enterprise Cloud Partner of the Year (year not stated)",
    "evidence": "Sabio's Avaya page claims Diamond Edge status and Enterprise Cloud Partner of the Year, cites a 2,500-user de Volksbank private-cloud migration, and Avaya named Sabio a certified BYOC option for AXP customers in Feb 2025.",
    "also_carries": ["Genesys (Elite status, Apr 2026; Demand Generation Partner of the Year 2025)", "Verint (Premier partner, only UK third party certified on full Verint WFO suite per ContactCenterWorld profile)", "Amazon Connect (listed partner)", "Google Cloud, Salesforce, Twilio, Cognigy, Microsoft (listed partners)"],
    "scale_signal": "Operations in UK, Spain, France, Netherlands, Denmark, Malaysia, South Africa, India (ContactCenterWorld profile, undated); no headcount or revenue found on site",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.sabiogroup.com/partners/avaya", "date": "fetched 2026-09-02", "note": "Diamond Edge, Enterprise Cloud Partner of the Year, de Volksbank"},
      {"url": "https://www.cxtoday.com/contact-center/avaya-to-stop-supporting-public-cloud-contact-centers-with-fewer-than-200-seats/", "date": "2025-02-17", "note": "Sabio named certified BYOC option"},
      {"url": "https://www.sabiogroup.com/partners", "date": "fetched 2026-09-02", "note": "Partner list incl. Genesys Elite Apr 2026"},
      {"url": "https://www.contactcenterworld.com/company/sabio.aspx", "date": "undated", "note": "Verint Premier, country list"}
    ]
  },
  {
    "name": "Damovo",
    "hq_country": "Germany (Düsseldorf)",
    "emea_coverage": ["Germany", "Switzerland", "Ireland", "Belgium", "Luxembourg", "Poland", "Czech Republic", "Italy", "UK"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Diamond Partner (since Feb 2017) with Multi-Country Co-Delivery status",
    "evidence": "Damovo's Avaya page lists Diamond plus Multi-Country Co-Delivery and awards: Partner of the Year Damovo Switzerland 2024, DACH Partner Excellence Award 2024, Technical Excellence Germany 2024, Customer Champion Germany and Ireland 2024, Biggest Value Partner 2023, Swiss AXP Partner of the Year 2023; supports Aura Elite, Aura Contact Center and AXP.",
    "also_carries": ["Cisco (contact centre offerings listed)", "Genesys (Silver partner)", "NICE CXone (listed with WFO)", "Mitel (listed)", "Microsoft, Zoom, Cognigy, Pexip (listed)"],
    "scale_signal": "About 600 employees, 160+ million euro turnover, 2,600+ customers, direct presence in 14 countries (damovo.com about page, fetched Sep 2 2026)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.damovo.com/en/about-us/partners/avaya-diamond", "date": "fetched 2026-09-02", "note": "Tier, co-delivery, 2023-2024 awards"},
      {"url": "https://www.damovo.com/partners/", "date": "fetched 2026-09-02", "note": "Full vendor list incl. Genesys Silver, NICE CXone, Cisco"},
      {"url": "https://www.damovo.com/en/about-us/", "date": "fetched 2026-09-02", "note": "Scale figures"},
      {"url": "https://www.uctoday.com/unified-communications/damovo-first-bring-avaya-cloud-solutions-ireland/", "date": "2017-06-27", "note": "Diamond granted Feb 2017; Ireland cloud launch"}
    ]
  },
  {
    "name": "WTG",
    "hq_country": "Germany (Münster)",
    "emea_coverage": ["Germany", "Switzerland", "Austria", "Poland", "Spain"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Edge Diamond Partner; self-claimed largest Avaya service partner in Germany; Avaya Biggest Partner of the Year 2024",
    "evidence": "WTG's Avaya pages state Edge Diamond status, the 2024 Biggest Partner of the Year award, 3,000+ Avaya customers and 1.5 million ports; T&N AG and BrainConsult (Switzerland/Austria) are group companies.",
    "also_carries": ["Claims 105 vendor partners and manufacturer independence but names none on the corporate page; no Genesys, Cisco, Five9 or NICE evidence found"],
    "scale_signal": "500+ employees, 22 locations across DE/CH/AT/PL/ES, 3,000+ Avaya customers, 1.5M ports, 700+ projects a year (wtg.com, fetched Sep 2 2026)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.wtg.com/avaya-partner-edge-diamond-spezialist-fuer-avaya/tenovis-telefonanlagen", "date": "fetched 2026-09-02", "note": "Diamond, Biggest Partner of the Year 2024, largest in Germany claim"},
      {"url": "https://www.wtg.com/avaya", "date": "fetched 2026-09-02", "note": "Diamond since 2006, 3,000 customers, 1.5M ports"},
      {"url": "https://www.wtg.com/unternehmen", "date": "fetched 2026-09-02", "note": "Headcount, locations, group companies"}
    ]
  },
  {
    "name": "T&N AG (WTG group)",
    "hq_country": "Switzerland",
    "emea_coverage": ["Switzerland", "Austria"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Diamond partner (self-described)",
    "evidence": "T&N states Diamond status, 20+ years with Avaya and Avaya systems implemented at 500+ companies in Switzerland and Austria, covering Aura, Aura Contact Center and IP Office.",
    "also_carries": [],
    "scale_signal": "500+ Avaya installations in CH/AT (tn-ict.com, fetched Sep 2 2026)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.tn-ict.com/en/about-us/partners/avaya-integrator", "date": "fetched 2026-09-02", "note": "Diamond, 500 companies, products"}
    ]
  },
  {
    "name": "Maintel",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "msp",
    "avaya_relationship": "Avaya Diamond Edge Partner and DevConnect member",
    "evidence": "Maintel's partner page lists Avaya Diamond Edge in both CX and UC, and Avaya named Maintel a certified BYOC option for AXP customers in Feb 2025.",
    "also_carries": ["Genesys (Premier accredited, AppFoundry partner)", "Mitel (Platinum)", "Cisco (Diamond, Master MSP)", "RingCentral (UK wholesale partner)", "Zoom (Platinum, contact centre)", "Gamma (CCaaS), AWS, Twilio, Sycurio (listed)"],
    "scale_signal": "LSE-listed since 2004 (maintel.co.uk); revenue and headcount not captured",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://maintel.co.uk/about-us/technology-partners/", "date": "fetched 2026-09-02", "note": "Tier statements for all vendors"},
      {"url": "https://www.cxtoday.com/contact-center/avaya-to-stop-supporting-public-cloud-contact-centers-with-fewer-than-200-seats/", "date": "2025-02-17", "note": "Certified BYOC option"}
    ]
  },
  {
    "name": "FourNet",
    "hq_country": "United Kingdom (Manchester)",
    "emea_coverage": ["UK"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Edge Diamond Cloud Integrator; Avaya Cloud Partner of the Year two years running (years not stated)",
    "evidence": "FourNet's Avaya page claims Edge Diamond Cloud Integrator status, 15-year partnership and Avaya EMEA/Engage awards, with public-sector references (HMCTS, WMAS, SWAST, Lancashire Police).",
    "also_carries": ["NICE (NICE UK Partner of the Year 2024)", "Cisco (Gold, Master Collaboration/Security via Nowcomm acquisition)", "Microsoft Teams Voice (deployments cited)"],
    "scale_signal": "Palatine Private Equity majority owner since Jun 2021; five merged businesses; no headcount or revenue found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://fournet.co.uk/about-us/partnership/avaya/", "date": "fetched 2026-09-02", "note": "Diamond Cloud Integrator, awards"},
      {"url": "https://fournet.co.uk/about-us/", "date": "fetched 2026-09-02", "note": "Ownership, NICE 2024 award, Cisco"}
    ]
  },
  {
    "name": "IP Integration (IPI)",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Diamond Partner (20+ years top tier, self-described)",
    "evidence": "IPI's Avaya page states Diamond status and carries a quote from Avaya UK&I MD Steve Joyner on 20+ years of partnership; references include Securitas and The Caravan and Motorhome Club.",
    "also_carries": ["Genesys (IPI showcasing Genesys Cloud applications; Genesys sponsoring IPI Xperience 2026)"],
    "scale_signal": "none found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://ipintegration.com/avaya-partner/", "date": "fetched 2026-09-02", "note": "Diamond, Avaya UK&I MD quote, Genesys"}
    ]
  },
  {
    "name": "Connect Managed Services",
    "hq_country": "United Kingdom (London)",
    "emea_coverage": ["UK", "South Africa"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Diamond Partner and co-delivery partner; self-described leading Avaya partner in South Africa",
    "evidence": "Connect's Avaya page claims Diamond status, co-delivery partner status, Avaya practice since 2007 and leadership in South Africa; Feb 2025 article positions Connect for Avaya legacy on-prem estates.",
    "also_carries": ["Amazon Connect (listed CCaaS)", "Five9 (listed CCaaS)", "Salesforce Service Cloud Voice (listed)", "Zendesk (listed)"],
    "scale_signal": "Offices UK, South Africa, India, USA; founded 1990; no headcount or revenue found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.weconnect.tech/how-we-do-it/cx-technology-partners/avaya-diamond-partner/", "date": "fetched 2026-09-02", "note": "Diamond, co-delivery, SA leadership claim, other CCaaS vendors"},
      {"url": "https://www.weconnect.tech/insights/articles/2025/02/navigate-the-avaya-landscape-flexibly-with-an-experienced-partner/", "date": "2025-02", "note": "Avaya landscape positioning"}
    ]
  },
  {
    "name": "Axians (VINCI Energies)",
    "hq_country": "France (Axians NL delivering)",
    "emea_coverage": ["Netherlands", "France", "Germany"],
    "partner_type": "msp",
    "avaya_relationship": "listed partner (managed services provider for Avaya UC and contact centre; tier not published)",
    "evidence": "VodafoneZiggo extended its Axians contract for Avaya UC and contact centre managed services (Omnia platform, UCaaS/CCaaS) for four more years, a relationship running since 2018.",
    "also_carries": ["ServiceNow partner (servicenow.com partner finder)"],
    "scale_signal": "Part of VINCI Energies; no Avaya-specific figures",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.telecompaper.com/news/vodafoneziggo-extends-axians-contract-for-avaya-managed-services--1567822", "date": "2026-04-10", "note": "Four-year extension, Avaya UC and CC managed services"}
    ]
  },
  {
    "name": "BT Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "pan-European via BT Global"],
    "partner_type": "carrier",
    "avaya_relationship": "Certified BYOC-Standard carrier for Avaya Experience Platform (tier not published)",
    "evidence": "Avaya's Feb 2025 customer notice recommends BT as a certified Bring-Your-Own-Carrier option for AXP customers losing Avaya SIP trunking.",
    "also_carries": [],
    "scale_signal": "none found in this run",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.cxtoday.com/contact-center/avaya-to-stop-supporting-public-cloud-contact-centers-with-fewer-than-200-seats/", "date": "2025-02-17", "note": "BT named certified BYOC option"}
    ]
  },
  {
    "name": "CGC (Converged Generation Communications)",
    "hq_country": "Saudi Arabia (Riyadh)",
    "emea_coverage": ["Saudi Arabia"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Self-described one of the largest Avaya partners in Saudi Arabia; Avaya CCaaS distribution rights; Avaya Contact Centre Partner award (Central region) Aug 2023",
    "evidence": "CGC's Nov 2024 post says it holds CCaaS distribution rights and is among the largest Avaya partners in KSA; Avaya's Aug 2023 Saudi awards named CGC Contact Centre Partner, describing it as a platinum partner managing enterprise call centres.",
    "also_carries": ["Freshworks (partnership Dec 4 2023)"],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://cgc-sa.com/2024/11/12/cgc-largest-avaya-partner-in-saudi-arabia/", "date": "2024-11-12", "note": "Largest-partner claim, CCaaS rights"},
      {"url": "https://www.dayofdubai.com/news/avaya-highlights-commitment-saudi-arabia-market-awards-kingdoms-top-performing-partners", "date": "2023-08-08", "note": "Contact Centre Partner award"}
    ]
  },
  {
    "name": "United Technologies (KSA)",
    "hq_country": "Saudi Arabia",
    "emea_coverage": ["Saudi Arabia"],
    "partner_type": "reseller",
    "avaya_relationship": "Avaya Best Mid-Market Partner, Western region (Aug 2023)",
    "evidence": "Avaya's Aug 2023 Saudi awards said United Technologies doubled growth and captured 15% of the mid-market segment.",
    "also_carries": [],
    "scale_signal": "15% of Avaya KSA mid-market segment per Avaya award write-up (Aug 2023)",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.dayofdubai.com/news/avaya-highlights-commitment-saudi-arabia-market-awards-kingdoms-top-performing-partners", "date": "2023-08-08", "note": "Award and 15% claim"}
    ]
  },
  {
    "name": "Aflak Solutions",
    "hq_country": "Saudi Arabia",
    "emea_coverage": ["Saudi Arabia"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya Public Sector Partner, Central region (Aug 2023); newly onboarded partner at that time",
    "evidence": "Named in Avaya's Aug 2023 Saudi partner awards for government ICT projects.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.dayofdubai.com/news/avaya-highlights-commitment-saudi-arabia-market-awards-kingdoms-top-performing-partners", "date": "2023-08-08", "note": "Award"}
    ]
  },
  {
    "name": "Concentrix",
    "hq_country": "United States (large EMEA delivery footprint)",
    "emea_coverage": ["UK", "Ireland", "Iberia", "France", "CEE", "South Africa", "Egypt"],
    "partner_type": "bpo_cx_outsourcer",
    "avaya_relationship": "listed partner (Avaya cloud contact center design, build, run and managed services; tier not published)",
    "evidence": "Concentrix maintains an Avaya partner page offering cloud migration and managed services on Avaya; EMEA delivery coverage is inferred from its global BPO footprint, not from the Avaya page.",
    "also_carries": [],
    "scale_signal": "none captured in this run",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.concentrix.com/partners/avaya/", "date": "fetched 2026-09-02", "note": "Avaya partner page"}
    ]
  },
  {
    "name": "CCT Solutions",
    "hq_country": "Germany (Frankfurt)",
    "emea_coverage": ["Germany", "Switzerland"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "Avaya reseller since 2012, Selected Product Partner, DevConnect compliance tested",
    "evidence": "CCT's site states a worldwide Avaya reseller contract since 2012, ACIS/ACSS certifications and Avaya Aura, Contact Center and IPO-CC specialisation.",
    "also_carries": ["NICE CXone (listed)", "Microsoft Teams contact center integration", "Nuance and Lumenvox speech"],
    "scale_signal": "Offices Frankfurt, Augsburg, Langenfeld, Sulzbach, Steinhausen (CH), North Miami (US)",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://cct-solutions.com/index.php/en/product-overview-en/solutions/uc-und-ucc-en", "date": "fetched 2026-09-02", "note": "Avaya status and NICE CXone"}
    ]
  },
  {
    "name": "LIPINSKI TELEKOM",
    "hq_country": "Germany (Berlin)",
    "emea_coverage": ["Germany"],
    "partner_type": "reseller",
    "avaya_relationship": "Certified Avaya Business Partner since 1990; Diamond Enterprise status appears in a search snippet but the fetched page states no tier",
    "evidence": "Lipinski's site describes a long-certified, award-winning Avaya partner for IP Office and Aura Communication Manager with nationwide German coverage.",
    "also_carries": ["Microsoft Teams"],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.lipinski-telekom.de/header/ueber-uns/avaya-business-partner-in-berlin-hamburg-kassel.html", "date": "fetched 2026-09-02", "note": "Partner status and locations"}
    ]
  },
  {
    "name": "Syscom",
    "hq_country": "United Arab Emirates",
    "emea_coverage": ["UAE", "Saudi Arabia", "Qatar"],
    "partner_type": "reseller",
    "avaya_relationship": "Avaya Diamond Partner in UAE per search snippet (site returned 403 on fetch); listed on Elioplus Avaya partner directory",
    "evidence": "Search result summary of sysllc.com stated Syscom is an Avaya Diamond Partner in UAE; Elioplus lists syscom distribution (UAE) as an Avaya channel partner.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.sysllc.com/avaya-partner-in-uae/", "date": "fetched 2026-09-02 (403)", "note": "Diamond claim from search snippet only"},
      {"url": "https://elioplus.com/profile/channel-partners/avaya", "date": "fetched 2026-09-02", "note": "Directory listing"}
    ]
  },
  {
    "name": "BCS (Business Continuity Solutions)",
    "hq_country": "United Arab Emirates (Dubai)",
    "emea_coverage": ["UAE", "Saudi Arabia", "Qatar", "Oman", "Kuwait"],
    "partner_type": "reseller",
    "avaya_relationship": "Self-described Avaya distributor and partner, positioned on IP Office and cloud phones (SMB weighted)",
    "evidence": "BCS vendor page claims number-one Avaya partner status for IP Office, cloud phones and collaboration in the UAE and references Avaya CCaaS.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://bcs-me.com/ourvendor/avaya", "date": "fetched 2026-09-02", "note": "Self-claims, countries"}
    ]
  },
  {
    "name": "TD SYNNEX",
    "hq_country": "United States (UK operation via Azlan)",
    "emea_coverage": ["UK"],
    "partner_type": "distributor",
    "avaya_relationship": "Appointed Avaya distributor in the UK (Azlan SDG release; undated, page body not retrievable)",
    "evidence": "A TD SYNNEX UK press release records Azlan SDG appointed to distribute Avaya's collaboration portfolio in the UK under an extended Tech Data Europe agreement; no 2024-2026 confirmation found.",
    "also_carries": [],
    "scale_signal": "none Avaya-specific",
    "confidence": "LOW",
    "sources": [
      {"url": "https://uk.tdsynnex.com/Intouch/MVC/Microsite/PressReleases?categorypageid=1200&msmenuid=2584&corpregionid=14&culture=en-GB&pressreleaseid=636&pressreleasetype=0", "date": "undated", "note": "Azlan Avaya appointment; body not retrievable"}
    ]
  },
  {
    "name": "Diyar United Company",
    "hq_country": "Kuwait",
    "emea_coverage": ["Kuwait", "Saudi Arabia", "UAE", "Qatar", "Oman"],
    "partner_type": "systems_integrator",
    "avaya_relationship": "listed partner (inferred from support role; tier not published)",
    "evidence": "A Diyar United system engineer job posting lists support and maintenance of Avaya telephone systems; no Avaya tier or award found (corporate page 403).",
    "also_carries": [],
    "scale_signal": "Branches in KSA, UAE, Qatar, Oman, India (search summary of diyarme.com)",
    "confidence": "LOW",
    "sources": [
      {"url": "https://app.qureos.com/jobs/system-engineer-kuwait-1764332651610", "date": "2025", "note": "Avaya support in job scope"}
    ]
  },
  {
    "name": "Charterhouse Voice & Data (CVD Group)",
    "hq_country": "United Kingdom (London)",
    "emea_coverage": ["UK"],
    "partner_type": "reseller",
    "avaya_relationship": "listed partner in Elioplus directory; Avaya absent from current cvdgroup.com partner list (likely lapsed)",
    "evidence": "Elioplus lists Charterhouse UK as an Avaya channel partner, but the current CVD Group site names Mitel, 8x8, Microsoft, Gamma and others with no Avaya, and its recent Teleware acquisition is Teams-native CX.",
    "also_carries": ["Mitel (listed)", "8x8 (listed)", "Microsoft (listed; Teleware AI agent/CX IP acquired)", "Cisco Meraki, Gamma, BT, Vodafone (listed)"],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://elioplus.com/profile/channel-partners/avaya", "date": "fetched 2026-09-02", "note": "Directory listing"},
      {"url": "https://www.cvdgroup.com/", "date": "fetched 2026-09-02", "note": "Current vendor list without Avaya"}
    ]
  },
  {
    "name": "Vodafone Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Germany", "Spain", "Italy"],
    "partner_type": "carrier",
    "avaya_relationship": "Historic Avaya contact centre reseller; the Vodafone UK URL still named avaya-contact-centre now markets storm and RingCX with no Avaya mention (de-emphasised)",
    "evidence": "Vodafone UK's /avaya-contact-centre page serves Vodafone Business storm and RingCX only; Vodafone and RingCentral announced a UCaaS/CCaaS partnership for UK, Spain, Germany and Italy on Dec 2 2020.",
    "also_carries": ["RingCentral RingCX (current page)", "Vodafone storm (own CCaaS)"],
    "scale_signal": "none Avaya-specific",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.vodafone.co.uk/business/unified-communications/contact-centre-solutions/avaya-contact-centre", "date": "fetched 2026-09-02", "note": "No Avaya content on Avaya-named URL"},
      {"url": "https://www.ringcentral.com/whyringcentral/company/pressreleases/vodafone-business-and-ringcentral-announce-strategic-partnership-to-deliver-new-cloud-based-communications-services.html", "date": "2020-12-02", "note": "RingCentral CCaaS partnership"}
    ]
  }
]
```

## SHARE

```json
{
  "vendor_emea_share": "no public figure",
  "sources": [
    {"url": "https://www.metrigy.com/product/contact-center-platforms-market-share-forecast-3q25/", "date": "2026-01-07", "note": "Global only: Avaya 37.5% of dedicated/on-prem CC platform revenue in 3Q25 (market $421.6M in quarter, down 22.4% YoY); Genesys 12.3%, Cisco 12.0%; CCaaS led by NICE 22.5%, Genesys 20.6%, Five9 12.5%"},
    {"url": "https://my.idc.com/getdoc.jsp?containerId=EUR153039425", "date": "2025-10", "note": "IDC European Contact Center Market Shares, 2024; search summary says top three in Europe are Genesys, Avaya, Zendesk; abstract not retrievable (403), percentages not public"},
    {"url": "https://www.sec.gov/Archives/edgar/data/1116521/000111652114000055/ex992080514avaya3qerfina.htm", "date": "2014-08-05", "note": "EMEA 28% of Avaya revenue in Q3 FY2014 (pre-restructuring, historical only)"},
    {"url": "https://www.nojitter.com/contact-centers/avaya-goes-to-infinity-and-beyond", "date": "2025-04-23", "note": "Top ~1,500 customer focus; Infinity shown to 200 largest Middle East customers and partners at GITEX"},
    {"url": "https://www.avaya.com/en/newsroom/2024/pr-uae-240925/", "date": "2024-09-25", "note": "Avaya: many of its largest and most advanced global customers are based in MEA"}
  ],
  "notes": "No analyst or Avaya statement gives an EMEA or Europe share percentage for Avaya contact center in 2024-2026. The strongest public proxy is Metrigy's global on-prem/dedicated platform share (37.5%, 3Q25) alongside a shrinking on-prem pool, which supports the installed-base thesis but must not be presented as an EMEA figure. Partner-level share signals are self-claims: WTG 'largest Avaya service partner in Germany' and 'Biggest Partner of the Year 2024'; CGC 'one of the largest Avaya partners in Saudi Arabia' (Nov 2024); Connect 'leading Avaya partner in South Africa'; Sabio 'Enterprise Cloud Partner of the Year' (undated); Damovo multiple 2023-2024 DACH/Swiss/Ireland awards; United Technologies '15% of KSA mid-market' (Avaya award copy, Aug 2023)."
}
```

## Gaps

- Search budget exhausted at 200 calls; unresolved: Avaya EMEA/International Partner of the Year winners 2024 and 2025; Nordics, Ireland, Poland/CEE, Italy, Iberia, France and Turkey named Diamond partners (Elioplus lists only small firms).
- Checked and found NO Avaya evidence on current partner pages (do not list as Avaya partners without new evidence): Kerv (Genesys Elite, Verint Elite; Avaya absent), Britannic (Mitel, Five9, 8x8, Verint listed; Avaya absent from current page), Orange Business (Genesys Elite, 48,550 Genesys licences managed, 120+ joint customers; Avaya absent), GBM, Alpha Data, Mannai, Datacentrix, Kapsch BusinessCom/CANCOM Austria, Atos (Unify/RingCentral, a competitor line), Econocom, Proximus, Injazat/Core42, Jeraisy.
- Telefonica appears as an Avaya Aura customer, not a verified channel partner.
- NTT DATA: 2025 evidence points to Amazon Connect (AWS SCA, Oct 2025) rather than Avaya.
- BT: only the Feb 2025 BYOC certification is sourced; BT's Avaya resale or managed-service tier is unverified.
- Computacenter: not an Avaya reseller in evidence; it consumes Avaya CX and Verint via Sabio.
- Distributors beyond Westcon: ScanSource is described as Avaya's largest distributor globally but no EMEA operation evidence in 2024-2026; Ingram Micro, Nuvias/Infinigate and ALSO returned no Avaya distribution evidence.
- Current Avaya program tier names: avaya.com/en/partners 404; treat any tier beyond partner self-description as unverified.
- IDC Europe 2024 share percentages and Omdia/Cavell/Frost EMEA Avaya figures: not public in any retrievable form.
