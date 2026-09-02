# Genesys, EMEA channel research pass (Sep 2 2026, signal-researcher, public sources only)

## Vendor context

Genesys runs EMEA as a first-class region: 1,600+ employees (about a quarter of global headcount), 20+ sites in 17 countries, R&D in France, Hungary and Ireland, with Gabriel Frasconi named VP Partner Sales EMEA and Joffray Anduze VP France on Dec 2 2025 (Genesys newsroom); Daniel Bailey moved from SVP EMEA to SVP Global Strategic Partnerships on Jul 7 2026. Program structure: the Ascend Partner Program launched May 4 2021 with Bronze, Silver, Gold and Platinum tiers; an Elite designation above Platinum now exists and is being awarded in EMEA (Sabio Apr 2026, Kerv May 2025). The current public partner page uses four types: Solution Provider, Referral Partner, Services Partner, and Technology Solutions Distributor, with distribution explicitly "North America only" (Genesys Ascend page, fetched 2026-09-02). Treat EMEA as a direct-to-partner (no distributor tier) model, inferred, MEDIUM. Named GSIs on genesys.com are Accenture, Capgemini, Deloitte Digital and IBM. Published share: Metrigy puts Genesys at 20.0% of global CCaaS revenue in 2025 (NiCE 22.3%, Five9 12.7%) and 12.9% of on-prem/dedicated platforms (Avaya 36.3%, Cisco 10.0%) (Metrigy, 2026-03-30); no vendor-level Europe or EMEA share is public. Genesys itself says nearly 45% of Genesys Cloud revenue comes from outside North America at $2.8B ARR, up ~35% YoY (Intelligent CIO, 2026-06-05). EMEA awards that are public: Kerv UKI Partner of the Year 2024; Sabio EMEA Partner of the Year 2021; Foehn EMEA Cloud Partner of the Year 2020. No 2025 EMEA regional winners list is public.

## PARTNERS

```json
[
  {
    "name": "Sabio Group",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "France", "Netherlands", "Spain"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Elite (Ascend, highest tier), awarded Apr 2026; EMEA Partner of the Year 2021",
    "evidence": "Genesys VP Channel Sales EMEA Gabriel Frasconi quoted on Sabio reaching Elite after nearly 30 years and hundreds of Genesys deployments.",
    "also_carries": ["Avaya (listed technology partner on sabiogroup.com)", "Amazon Connect (listed technology partner)", "Verint (listed technology partner, WFO adjacent)", "Twilio", "Google Cloud", "Salesforce"],
    "scale_signal": "Practices in UK, France, Netherlands and Spain (Dec 2021); 'dominant provider of Genesys solutions in EMEA' self-claim (Dec 2021); no public headcount or revenue found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://sabiogroup.com/news/sabio-group-achieves-genesys-elite-partner-status/", "date": "2026-04-15", "note": "Elite status, Frasconi quote, vendor list"},
      {"url": "https://www.callcentrehelper.com/sabio-genesys-partner-of-year-201996.htm", "date": "2021-12-02", "note": "EMEA Partner of the Year, country practices"},
      {"url": "https://sabiogroup.com/partners/genesys/", "date": "fetched 2026-09-02", "note": "25+ years, Elite wording, partner roster"}
    ]
  },
  {
    "name": "Kerv Experience (formerly Foehn)",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "EMEA deployments"],
    "partner_type": "msp",
    "genesys_relationship": "Elite (May 2025); UKI Partner of the Year 2024; EMEA Cloud Partner of the Year 2020 (as Foehn)",
    "evidence": "Kerv states 100+ Genesys Cloud deployments in EMEA and claims to be the longest-standing Genesys Cloud partner in EMEA with the most deployments.",
    "also_carries": ["Microsoft (Teams, Dynamics 365; no second CCaaS platform named, Kerv Experience is Genesys-only)", "Verint (Elite, per Kerv partners page)"],
    "scale_signal": "Kerv group 750+ employees; 100+ Genesys Cloud deployments in EMEA (May 2025); 50,000 Genesys agents across 80+ customers (CCMA directory)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://kerv.com/company-news/kerv-experience/kerv-is-genesys-elite-partner/", "date": "2025-05-20", "note": "Elite, 100+ EMEA deployments"},
      {"url": "https://kerv.com/company-news/kerv-experience/kerv-experience-named-uki-genesys-partner-of-the-year-2024/", "date": "2024-07-04", "note": "UKI Partner of the Year 2024"},
      {"url": "https://kerv.com/about-kerv/", "date": "fetched 2026-09-02", "note": "750+ employees, Microsoft focus"},
      {"url": "https://kerv.com/about-kerv/our-partners/", "date": "fetched 2026-09-02", "note": "Genesys Elite, Verint Elite, Microsoft"}
    ]
  },
  {
    "name": "Orange Business",
    "hq_country": "France",
    "emea_coverage": ["France", "Belgium", "multi-country EMEA", "global (65 countries)"],
    "partner_type": "carrier",
    "genesys_relationship": "Elite (Orange partner page; Belgian page also says Platinum)",
    "evidence": "Orange reports 25+ years with Genesys, 120+ joint customers, 48,550 Genesys licences under management and 170+ certifications; sponsor of Genesys Future of CX Belgium Oct 2025.",
    "also_carries": [],
    "scale_signal": "48,550 Genesys licences managed; 120+ joint customers; Orange Business 30,000+ B2B customers in 65 countries",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.orange-business.com/en/partners/genesys", "date": "fetched 2026-09-02", "note": "Elite, 25+ years, licence and customer counts"},
      {"url": "https://www.genesys.com/en-gb/events/genesys-future-of-cx-belgium-2025", "date": "2025-10-02", "note": "Event sponsor list"}
    ]
  },
  {
    "name": "NTT DATA",
    "hq_country": "Japan",
    "emea_coverage": ["Germany", "Belgium", "Netherlands", "Italy", "UK", "pan-EMEA"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Global Elite Partner (nttdata.com global page)",
    "evidence": "NTT DATA claims 150,000+ Genesys seats deployed and the largest Genesys customer base, with EMEA case studies for SIXT, ORES (Belgium) and DynaGroup; sponsor of Genesys Future of CX Belgium Oct 2025.",
    "also_carries": ["Cisco (listed collaboration partner on NTT DATA partners page)", "AWS, Microsoft, Salesforce, ServiceNow (listed partners)"],
    "scale_signal": "150,000+ Genesys seats deployed; 30K contact center professionals; 35+ years in CX",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.nttdata.com/global/en/about-us/partners/genesys", "date": "fetched 2026-09-02", "note": "Global Elite, 150,000 seats, EMEA case studies"},
      {"url": "https://www.nttdata.com/global/en/about-us/partners", "date": "fetched 2026-09-02", "note": "Partner roster incl. Cisco"}
    ]
  },
  {
    "name": "BT Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "global reseller scope"],
    "partner_type": "carrier",
    "genesys_relationship": "Global reseller of Genesys Cloud and Genesys Multicloud CX (expanded from Gold, Oct 2020); current Ascend tier not public",
    "evidence": "BT was Platinum sponsor at Genesys Xperience UKI 2024 and cites 20+ years with Genesys, including migrating the UK Home Office's contact centres to Genesys Cloud.",
    "also_carries": [],
    "scale_signal": "Serves deployments from 25 users to tens of thousands (2020 PR); no partner-level seat count public",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.genesys.com/en-gb/company/newsroom/announcements/genesys-extends-global-cloud-customer-experience-relationship-with-bt", "date": "2020-09-30", "note": "Global reseller agreement, prior Gold status"},
      {"url": "https://business.bt.com/insights/genesys-xperience-2024/", "date": "2024-07-19", "note": "Platinum sponsor, Home Office migration"}
    ]
  },
  {
    "name": "TTEC Digital",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Ireland", "Bulgaria", "Europe (delivery)"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Platinum; CX Evolution Partner of the Year 2024; 15x Genesys Partner of the Year",
    "evidence": "TTEC Digital cites 170+ Genesys Cloud certifications, 300+ Genesys resources and 1,000+ clients across North America, Europe and APAC; VoiceFoundry won the inaugural AWS Amazon Connect Partner of the Year (UKI) 2021.",
    "also_carries": ["Amazon Connect (VoiceFoundry, AWS UKI Partner of the Year 2021)", "Cisco (Cloud Contact Center Partner of the Year, TTEC EMEA page)", "Microsoft (Digital Contact Center Platform launch partner)", "Salesforce, Pega"],
    "scale_signal": "2,000 technologists; 1,000+ clients; TTEC 52K+ employees globally",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.ttecdigital.com/partners/genesys", "date": "fetched 2026-09-02", "note": "Platinum, awards, certification counts"},
      {"url": "https://www.ttec.com/emea/about-us", "date": "fetched 2026-09-02", "note": "EMEA sites, AWS/Cisco/Microsoft awards"}
    ]
  },
  {
    "name": "Teleperformance (TP Infinity, incl. Majorel X)",
    "hq_country": "France",
    "emea_coverage": ["France", "Benelux", "Spain", "Germany", "UK", "pan-EMEA BPO footprint"],
    "partner_type": "bpo_cx_outsourcer",
    "genesys_relationship": "Global Platinum Partner and reseller (Dec 2023); TP Infinity page says 'global Genesys Gold Elite Partner' (undated)",
    "evidence": "Teleperformance SVP Paul Joustra said TP invested to reach Global Platinum status to consult, deliver, integrate and customise Genesys; Majorel X folded in after the Majorel acquisition.",
    "also_carries": ["Amazon Connect (TP Infinity technology page)", "Talkdesk (TP Infinity technology page)", "Sprinklr, Cognigy, Kore.ai, CallMiner"],
    "scale_signal": "No Genesys-specific seat count public; group-level BPO scale only",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://customerfirst.nl/nieuws/2023/12/teleperformance-maakt-debuut-op-g-summit/index.xml", "date": "2023-12-20", "note": "Global Platinum, reseller, Majorel X"},
      {"url": "https://www.tpinfinity.com/technology/tech-solutions/cx-management/genesys-cloud-cx/", "date": "fetched 2026-09-02", "note": "Gold Elite wording, other platforms"}
    ]
  },
  {
    "name": "Konecta",
    "hq_country": "Spain",
    "emea_coverage": ["Spain", "Portugal", "France", "Italy", "Germany", "UK"],
    "partner_type": "bpo_cx_outsourcer",
    "genesys_relationship": "listed partner (Genesys Cloud CX delivery and resale inside BPO or standalone); tier not public",
    "evidence": "Konecta has implemented Genesys Cloud CX at 30+ large companies with 6,000+ concurrent agents across EMEA and the Americas and named France, Italy, Germany and the UK as expansion markets.",
    "also_carries": ["AWS (AWS generative AI case study; Amazon Connect not specifically named)"],
    "scale_signal": "109,000 employees; EUR 2B revenue; 28 countries; 500+ clients; 6,000+ concurrent Genesys agents",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://konecta.com/news-insights/konecta-and-genesys-partner-to-help-companies-transform-customer-management-operations-with-generative-ai", "date": "2023-10-26", "note": "Partnership, scale figures"}
    ]
  },
  {
    "name": "KPN",
    "hq_country": "Netherlands",
    "emea_coverage": ["Netherlands"],
    "partner_type": "carrier",
    "genesys_relationship": "Elite ('KPN is Elite Partner van Genesys', kpn.com)",
    "evidence": "KPN sells Genesys Cloud in three packaged tiers to large enterprises; Budget Thuis moved 200+ agents onto Genesys Cloud via KPN in Jun 2024, alongside Greenchoice and Continuum.",
    "also_carries": ["Anywhere365 (Microsoft Teams dialogue platform, KPN CX portfolio)"],
    "scale_signal": "Named enterprise CX clients only (WoningNet, Continuum, Yource, Stater, Budget Thuis, Eneco, Greenchoice); no seat total public",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.kpn.com/zakelijk/grootzakelijk/customer-experience/genesys-cloud", "date": "fetched 2026-09-02", "note": "Elite wording, packages, Anywhere365"},
      {"url": "https://www.ziptone.nl/nieuws/budget-thuis-kiest-voor-kpn-en-genesys-cloud/", "date": "2024-06-24", "note": "200+ agents"}
    ]
  },
  {
    "name": "Proximus NXT",
    "hq_country": "Belgium",
    "emea_coverage": ["Belgium", "Luxembourg"],
    "partner_type": "carrier",
    "genesys_relationship": "listed partner (Genesys Cloud implementer); tier not public",
    "evidence": "Proximus NXT delivered Genesys Cloud for OCTA+ in six weeks and sponsored Genesys Future of CX Belgium Oct 2025.",
    "also_carries": [],
    "scale_signal": "250+ cloud specialists, 500+ enterprise customers (search summary of Proximus page, unfetched)",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.proximus.be/en/id_b_cl_octa_plus/companies-and-public-sector/news/news-blog/customer-talks/contact-center-software.html", "date": "search result, fetch failed", "note": "OCTA+ Genesys Cloud case"},
      {"url": "https://www.genesys.com/en-gb/events/genesys-future-of-cx-belgium-2025", "date": "2025-10-02", "note": "Sponsor list"}
    ]
  },
  {
    "name": "Telia",
    "hq_country": "Sweden",
    "emea_coverage": ["Sweden", "Nordics"],
    "partner_type": "carrier",
    "genesys_relationship": "Gold Certified Partner in the Nordics (contactcenter.telia.se, unfetched); Genesys Cloud listed on telia.se",
    "evidence": "Telia's business site lists two contact center offers, its own Telia ACE and Genesys Cloud; the Telia Genesys page describes 10+ years implementing Genesys.",
    "also_carries": ["Telia ACE (Telia's own contact center platform)"],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.telia.se/foretag/losningar/kontaktcenter", "date": "fetched 2026-09-02", "note": "Telia ACE plus Genesys Cloud"}
    ]
  },
  {
    "name": "Damovo",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Ireland", "Poland", "UK", "Belgium", "Switzerland", "14 countries direct"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Silver (US, Ireland, Germany, Poland)",
    "evidence": "Damovo implemented Genesys Cloud for Deutsche Glasfaser (340 agents, three months) and BarmeniaGothaer, and holds Genesys Silver in four countries.",
    "also_carries": ["Cisco (Cisco 360 Partner, 200+ certifications in Germany; Webex Contact Centre named)", "Avaya (Diamond Partner, Multi-Country Co-Delivery)", "Mitel (Platinum Integrator Partner)", "NICE CXone and NiCE Cognigy", "Zoom (Gold, Zoom CX named)", "Microsoft Teams"],
    "scale_signal": "EUR 160M+ turnover; 600+ employees; 2,600+ customers; 14 countries direct, 150+ supported",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.damovo.com/partners/", "date": "fetched 2026-09-02", "note": "Genesys Silver countries, full vendor roster, scale"},
      {"url": "https://www.genesys.com/customer-stories/deutsche-glasfaser", "date": "fetched 2026-09-02", "note": "340 agents, Damovo named"}
    ]
  },
  {
    "name": "Telefonica Tech",
    "hq_country": "Spain",
    "emea_coverage": ["Spain"],
    "partner_type": "carrier",
    "genesys_relationship": "Gold Partner (Oct 2018, Spain: PureCloud, PureConnect, PureEngage); current tier not public",
    "evidence": "Telefonica Espana took Gold status to distribute, sell and support Genesys in Spain; Telefonica Tech's current partner page still names a strategic agreement with Genesys (page returned 403 in this run).",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://noticiasbancarias.com/general/18/10/2018/telefonica-ofrecera-en-espana-las-soluciones-omnicanal-de-la-multinacional-genesys/166927.html", "date": "2018-10-18", "note": "Gold Partner, scope"}
    ]
  },
  {
    "name": "Deutsche Telekom (T-Systems)",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Austria"],
    "partner_type": "carrier",
    "genesys_relationship": "listed partner (Genesys-based Telekom Contact Center Suite, cloud pay-per-use since 2012); current Ascend tier not public",
    "evidence": "Telekom Deutschland built its SMB cloud contact center suite on Genesys in 2012; group affiliate Magenta Telekom is a Genesys Cloud customer.",
    "also_carries": ["Avaya (T-Systems and Avaya cloud contact center partnership per telekom.com, page not fetched)"],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.destinationcrm.com/Articles/CRM-News/CRM-Featured-Articles/Genesys-and-Telekom-Deutschland-Announce-New-Cloud-Based-Contact-Center-Solution---84937.aspx", "date": "2012-09-12", "note": "Original Genesys-based cloud suite"},
      {"url": "https://www.genesys.com/customer-stories/magenta-telekom", "date": "search result", "note": "Magenta Telekom Genesys Cloud customer"}
    ]
  },
  {
    "name": "IP Integration (IPI)",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "listed partner; Silver Sponsor at Genesys Xperience UKI 2026; three own applications for Genesys Cloud",
    "evidence": "IPI markets Genesys Cloud delivery (Co-op Group cited) and premium add-on applications for Genesys Cloud.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.ipintegration.com/", "date": "fetched 2026-09-02", "note": "Genesys Cloud focus, Xperience 2026 sponsor"}
    ]
  },
  {
    "name": "Cognizant",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Ireland", "Netherlands", "Germany", "Nordics (delivery presence)"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Platinum (Aug 2022, upgraded from Gold); named in Genesys Jul 2026 ecosystem release",
    "evidence": "Cognizant reached Platinum after transforming contact centers for 75+ clients on Genesys Cloud CX and Multicloud CX.",
    "also_carries": ["NICE (Cognizant partners page)", "Cisco (Cognizant partners page)", "Calabrio (Cognizant partners page, WFM adjacent)", "Talkdesk", "Microsoft, Salesforce, ServiceNow, AWS"],
    "scale_signal": "75+ Genesys clients (2022); no EMEA split public",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://news.cognizant.com/2022-08-24-Cognizant-Earns-Platinum-Partner-Status-with-Genesys,-Helping-Clients-Improve-Customer-Experience", "date": "2022-08-24", "note": "Platinum, 75+ clients"},
      {"url": "https://www.cognizant.com/us/en/about-cognizant/partners", "date": "fetched 2026-09-02", "note": "Vendor roster incl. NICE, Cisco, Calabrio"}
    ]
  },
  {
    "name": "Deloitte Digital",
    "hq_country": "United Kingdom (DTTL network)",
    "emea_coverage": ["Belgium (event sponsor)", "pan-EMEA member firms"],
    "partner_type": "consultancy",
    "genesys_relationship": "GSI Partner of the Year 2024 and Global Influence Partner of the Year 2024; named GSI on genesys.com; strategic alliance Feb 2025",
    "evidence": "Genesys CSO Larry Shurtz announced Deloitte Digital as 2024 GSI Partner of the Year; Deloitte sponsored Genesys Future of CX Belgium Oct 2025.",
    "also_carries": [],
    "scale_signal": "470,000 people, 150+ countries (firm level); no Genesys practice size public",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.deloitte.com/us/en/about/press-room/deloitte-digital-named-global-systems-integrator-partner-of-the-year.html", "date": "2025-03-06", "note": "Two 2024 awards"},
      {"url": "https://www.genesys.com/partners/global-system-integrators", "date": "fetched 2026-09-02", "note": "Named GSI"}
    ]
  },
  {
    "name": "Capgemini",
    "hq_country": "France",
    "emea_coverage": ["France", "pan-EMEA"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Named GSI on genesys.com; named in Genesys Jul 2026 ecosystem release; tier not public",
    "evidence": "Genesys lists Capgemini as one of four Global System Integrators (340,000 staff, 50+ countries).",
    "also_carries": [],
    "scale_signal": "340,000 team members, 50+ countries (firm level)",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.genesys.com/partners/global-system-integrators", "date": "fetched 2026-09-02", "note": "Named GSI"}
    ]
  },
  {
    "name": "Accenture",
    "hq_country": "Ireland",
    "emea_coverage": ["pan-EMEA"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Named GSI on genesys.com; named in Genesys Jul 2026 ecosystem release; tier not public",
    "evidence": "Genesys lists Accenture as a Global System Integrator delivering Genesys Cloud with its own accelerators.",
    "also_carries": [],
    "scale_signal": "none found at Genesys-practice level",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.genesys.com/partners/global-system-integrators", "date": "fetched 2026-09-02", "note": "Named GSI"}
    ]
  },
  {
    "name": "IBM Consulting",
    "hq_country": "United States",
    "emea_coverage": ["pan-EMEA"],
    "partner_type": "systems_integrator",
    "genesys_relationship": "Named GSI on genesys.com ('one of the most experienced Genesys system integrators'); tier not public",
    "evidence": "Genesys GSI page credits IBM with many large Genesys implementations end to end.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.genesys.com/partners/global-system-integrators", "date": "fetched 2026-09-02", "note": "Named GSI"}
    ]
  },
  {
    "name": "Concentrix",
    "hq_country": "United States",
    "emea_coverage": ["UK", "France", "Spain", "Germany", "Nordics (Webhelp footprint)"],
    "partner_type": "bpo_cx_outsourcer",
    "genesys_relationship": "listed partner (self-described GSI partner for Genesys Cloud); tier not public",
    "evidence": "Concentrix markets Genesys Cloud CCaaS implementation and managed services plus a Salesforce-and-Genesys Next Generation Customer Care offer, and exhibited at Genesys Xperience 2025.",
    "also_carries": ["Salesforce (NGCC offer)"],
    "scale_signal": "none found at Genesys-practice level",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.concentrix.com/partners/genesys/", "date": "fetched 2026-09-02", "note": "Genesys services page"},
      {"url": "https://www.concentrix.com/events/genesys-xperience-2025/", "date": "2025-09-08", "note": "Xperience 2025 participation"}
    ]
  },
  {
    "name": "Telenet Business",
    "hq_country": "Belgium",
    "emea_coverage": ["Belgium"],
    "partner_type": "carrier",
    "genesys_relationship": "listed sponsor only (Genesys Future of CX Belgium Oct 2025); partnership terms not public",
    "evidence": "Telenet appears alongside Proximus, Orange, NTT Data, Deloitte and DDM Consulting as a sponsor of the Genesys Belgium event.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.genesys.com/en-gb/events/genesys-future-of-cx-belgium-2025", "date": "2025-10-02", "note": "Sponsor list"}
    ]
  }
]
```

## SHARE

```json
{
  "vendor_emea_share": "no public figure",
  "sources": [
    {"url": "https://www.metrigy.com/product/ccaas-contact-center-platforms-quarterly-market-share-forecast-report-2025-4q25/", "date": "2026-03-30", "note": "Global CCaaS 2025: NiCE 22.3%, Genesys 20.0%, Five9 12.7%; on-prem/dedicated 2025: Avaya 36.3%, Genesys 12.9%, Cisco 10.0%"},
    {"url": "https://www.inflectioncx.com/intelligence/guides/ccaas-market-guide-2026", "date": "2026", "note": "Europe 27 to 29% of global CCaaS revenue; IDC European MarketScape Leaders cited as NICE, Content Guru, Zoom"},
    {"url": "https://www.idc.com/resource-center/blog/idc-publishes-the-first-european-ccaas-marketscape-a-region-that-deserves-its-own-lens/", "date": "2025-10-13", "note": "European CCaaS USD 1.5B (2024) to USD 3.7B (2029), 20% CAGR; no vendor shares"},
    {"url": "https://www.genesys.com/company/newsroom/announcements/122907", "date": "2023-06-29", "note": "Genesys ranked #1 growth leader in Frost Radar European Cloud Contact Center Market 2023"},
    {"url": "https://www.intelligentcio.com/eu/2026/06/05/genesys-cloud-reaches-us2-8-billion-arr-as-enterprise-ai-adoption-accelerates/", "date": "2026-06-05", "note": "Genesys Cloud ARR USD 2.8B, ~35% YoY, nearly 45% of Genesys Cloud revenue outside North America"},
    {"url": "https://www.genesys.com/en-gb/company/newsroom/announcements/genesys-strengthens-emea-leadership-team", "date": "2025-12-02", "note": "1,600+ EMEA employees (~25% of global), 17 countries"}
  ],
  "notes": "No analyst has published a Genesys-specific Europe or EMEA revenue share. Best public proxies: Metrigy global CCaaS share (20.0% for 2025, second to NiCE), Europe at 27 to 29% of global CCaaS revenue, Genesys's own statement that nearly 45% of Genesys Cloud revenue is non-North American, and Frost naming Genesys the #1 growth leader in its European Cloud Contact Center Radar 2023. Partner-level share signals that are public: Kerv 'longest standing Genesys Cloud partner in EMEA with the most deployments' (100+, May 2025); Sabio 'dominant provider of Genesys solutions in EMEA' and EMEA Partner of the Year 2021; NTT DATA 'largest base of Genesys customers' at 150,000+ seats (global); Orange Business 48,550 Genesys licences under management. All are vendor or partner self-claims."
}
```

## Gaps

- No public list of 2025 Genesys EMEA regional Partner of the Year winners; the Genesys Partner Finder loads dynamically and could not be read.
- No public Genesys EMEA distributor: the Ascend page limits Technology Solutions Distributors to North America.
- Not verified as Genesys partners in EMEA: Vodafone Business, Capita, Kapsch BusinessCom (now under CANCOM), Econocom, Axians, Prodware, Elisa, Telenor, ISG, BSS. Route 101 (UK) is a Zendesk and NICE CXone shop, not Genesys.
- Thin sub-regions: Italy (only NTT DATA and Konecta), CEE (only Damovo Poland Silver), Gulf (no named partner reached), South Africa (a Genesys Partner Day ran Aug 18 2026 in Johannesburg, no partners listed), Nordics beyond Telia.
