# Amazon Connect, EMEA channel research pass (Sep 2 2026, signal-researcher, public sources only)

## Vendor context

AWS sells Amazon Connect in EMEA through the standard APN Services Path (Select, Advanced, Premier tiers) plus service-specific specializations. The Amazon Connect Service Delivery designation launched May 15, 2019 with 15 launch partners, four of them EMEA-relevant (Accenture, Deloitte, Connect Managed Services UK, tecRacer Germany, plus TCS and Cognizant). On June 16, 2026 AWS announced the Amazon Connect Customer Services Competency, the first AWS Competency aligned to a single service, with two categories (Contact Center Transformation, AI-Powered Customer Experience); it replaces the Service Delivery designation, which is deprecated June 1, 2027. Named launch competency partners (global list, no region tags): Accenture, Caylent, Deloitte, Genpact, Infosys, NeuraFlash, NTT DATA, PwC, Pronetx, Salesforce, TTEC Digital, USAN, Zendesk. The product itself is now marketed as "Amazon Connect Customer" inside an "Amazon Connect" family of agentic products (Aug 2026). Monthly APN "Say Hello" posts tagged new EMEA Connect delivery partners Feb 2025 to Dec 2025: LionGate AG, Route 101, Elastic Move/Buzzcloud (now Awiant), SnapTec, BlueSky Digital Solutions, HWS Informationssysteme. The 2025 EMEA partner awards (Dec 2, 2025) have no Connect-specific category; the only Connect-specific EMEA award on record is the inaugural 2021 Amazon Connect Partner of the Year UKI, won by VoiceFoundry/TTEC Digital. Distribution: Westcon-Comstor (EEA plus Switzerland plus UKI, Nov 28, 2024), TD SYNNEX (EMEA Distributor Partner of the Year Public Sector 2025), Ingram Micro (Global Distributor of the Year, Dec 16, 2025, with new Middle East resell authorization), Arrow (Rising Star Distributor EMEA 2025); none publish Connect-specific figures. Published share: Frost Radar EMEA Cloud Contact Centers 2024 names AWS a Leader (AWS post Sep 16, 2024, no figure); Gartner MQ CCaaS Sep 8, 2025 names AWS a Leader for the third year; Research and Markets' July 10, 2025 worldwide CCaaS share report ranks Amazon Connect #3 by seats behind NICE and Genesys (global); Amazon's Q3 2025 release (Oct 30, 2025) states Connect reached a $1B annualized revenue run rate (global). No EMEA or Europe share figure for Amazon Connect is public.

## PARTNERS

```json
[
  {
    "name": "Sabio Group",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Spain", "France", "Netherlands", "Nordics", "South Africa"],
    "partner_type": "systems_integrator",
    "connect_relationship": "listed partner (self-described 'Amazon Certified Specialist and Service Provider Partner' for Amazon Connect; no APN designation string verified)",
    "evidence": "Sabio lists Amazon Connect as one of seven core CX vendors and sponsored the UK Independent User Group for Amazon Connect on May 22, 2025.",
    "also_carries": ["Genesys (Elite)", "Avaya", "Verint", "Twilio", "Salesforce", "Google Cloud"],
    "scale_signal": "650+ customers globally (Jan 12, 2023 press release); operations in UK, Spain, France, Netherlands, Malaysia, Singapore, South Africa, India",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://sabiogroup.com/event/3rd-independent-user-group-for-amazon-connect/", "date": "2025-05-22", "note": "Sabio sponsor of UK Amazon Connect user group"},
      {"url": "https://sabiogroup.com/partners/amazon-connect/", "date": "2025", "note": "Connect partner page, vendor list"},
      {"url": "https://www.prnewswire.co.uk/news-releases/sabio-group-expands-into-the-nordic-region-and-strengthens-genesys-capability-301717976.html", "date": "2023-01-12", "note": "650+ customers, Nordic Genesys unit from Sopra Steria"}
    ]
  },
  {
    "name": "CloudInteract",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Service Delivery designation, AWS Advanced tier",
    "evidence": "Advanced Consulting tier with Amazon Connect Service Delivery designation, 7 Amazon Connect Ambassadors, 50+ enterprise deployments, joint Pega/Connect agentic voice partnership with Red Kite June 2026.",
    "also_carries": ["Pega (joint delivery with Red Kite, Jun 4 2026)"],
    "scale_signal": "Revenue passing GBP 3M for FY to Mar 2025, GBP 5M target FY26 (IT Channel Oxygen, Jan 29 2025); one early customer at 6,000 agents",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.cloudinteract.io/why-cloudinteract", "date": "2026", "note": "tier, designation, Ambassadors"},
      {"url": "https://itchanneloxygen.com/meet-the-uk-amazon-connect-partner-causing-a-stir-in-the-us/", "date": "2025-01-29", "note": "revenue and headcount plans"},
      {"url": "https://www.businesswire.com/news/home/20260604645983/en/CloudInteract-and-Red-Kite-Launch-Joint-Delivery-Partnership-for-Agentic-AI-Voice-on-Amazon-Connect-and-Pega", "date": "2026-06-04", "note": "Red Kite partnership"}
    ]
  },
  {
    "name": "Connect Managed Services",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "South Africa"],
    "partner_type": "msp",
    "connect_relationship": "Amazon Connect Service Delivery accreditation (2019 launch partner), AWS Advanced tier since Jul 2022",
    "evidence": "One of the 15 original Amazon Connect Service Delivery launch partners (May 2019) and self-described as one of five Nuance-replacement strategic partners selected by Amazon.",
    "also_carries": ["Five9", "Genesys", "Salesforce Service Cloud Voice", "Zendesk", "Verint (for regulated environments)"],
    "scale_signal": "Founded 1990, offices UK, South Africa, India, USA",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/building-a-cloud-based-contact-center-with-amazon-connect-service-delivery-partners", "date": "2019-05-15", "note": "launch partner list"},
      {"url": "https://www.weconnect.tech/insights/press-releases/connect-attains-aws-advanced-partner-status/", "date": "2022-07-26", "note": "Advanced tier, Connect SDP"},
      {"url": "https://www.weconnect.tech/how-we-do-it/cx-technology-partners/amazon-connect-contact-centre-partner/", "date": "2026", "note": "vendor list, regions"}
    ]
  },
  {
    "name": "TTEC Digital",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Ireland", "Europe (offices stated, not itemised)"],
    "partner_type": "systems_integrator",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026; 2019 Service Delivery launch partner; AWS 2021 Amazon Connect Partner of the Year UKI",
    "evidence": "Only partner on record with a Connect-specific EMEA AWS award (inaugural UKI Connect Partner of the Year, Dec 9 2021), and a named launch partner of the 2026 Connect Customer competency.",
    "also_carries": ["Cisco", "Five9", "Genesys", "NICE", "Verint", "Alvaria and Aspect", "Calabrio", "Talkdesk, Zoom, Salesforce, Pega, ServiceNow, Zendesk"],
    "scale_signal": "TTEC acquired VoiceFoundry Aug 2020 with UK office; no EMEA Connect seat count published",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.ttec.com/newsroom/press-release/voicefoundry-ttec-digital-business-wins-inaugural-aws-2021-amazon-connect", "date": "2021-12-09", "note": "UKI Connect Partner of the Year"},
      {"url": "https://aws.amazon.com/blogs/apn/from-legacy-to-ai-powered-transform-your-customer-experience-with-amazon-connect-customer-competency-partners/", "date": "2026-06-16", "note": "competency launch partner"},
      {"url": "https://ttecdigital.com/partners", "date": "2026", "note": "other vendors carried"}
    ]
  },
  {
    "name": "tecRacer",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Austria", "Switzerland", "Portugal"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Service Delivery Partner (2019 launch partner), AWS Premier Tier Services Partner, MSP, Reseller",
    "evidence": "Amazon Connect is among tecRacer's AWS Service Delivery validations and it was a 2019 launch partner; it has marketed a Connect practice in DACH since 2018.",
    "also_carries": [],
    "scale_signal": "About 150 employees, offices Hannover, Berlin, Duisburg, Frankfurt, Hamburg, Vienna, Zurich, Lisbon",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.tecracer.com/consulting/aws-consulting/", "date": "2026", "note": "Premier tier, Connect validation, offices"},
      {"url": "https://aws.amazon.com/blogs/apn/building-a-cloud-based-contact-center-with-amazon-connect-service-delivery-partners", "date": "2019-05-15", "note": "launch partner"}
    ]
  },
  {
    "name": "Route 101",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "reseller",
    "connect_relationship": "Amazon Connect Service Delivery (added Jan 2025, APN post Feb 13 2025)",
    "evidence": "Named as an EMEA Amazon Connect Service Delivery partner in the APN January 2025 additions post and lists Amazon Connect alongside NICE and Zendesk as its CCaaS lines.",
    "also_carries": ["NICE CXone", "Zendesk", "Calabrio (WEM partner)", "PolyAI, Omilia, Ada"],
    "scale_signal": "none found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/say-hello-to-201-new-aws-competency-service-delivery-service-ready-and-msp-partners-added-in-january/", "date": "2025-02-13", "note": "Route 101 Ltd, EMEA, Connect SDP"},
      {"url": "https://www.route101.com/partners", "date": "2026", "note": "vendor list"}
    ]
  },
  {
    "name": "SVL Business Solutions",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "reseller",
    "connect_relationship": "listed partner (Amazon Connect/AWS practice; no APN designation string verified)",
    "evidence": "SVL markets Amazon Connect design, deployment and managed services and states accreditation on Amazon Connect, NICE CXone and Calabrio.",
    "also_carries": ["NICE CXone, NICE WFM, Cognigy", "Calabrio (WEM)"],
    "scale_signal": "25+ Blue Light (emergency services) organisations; 55 years trading",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.svlbusinesssolutions.com/", "date": "2026", "note": "vendors, clients"}
    ]
  },
  {
    "name": "Acceleraate",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "msp",
    "connect_relationship": "listed partner (AWS Partner Network member, AWS Marketplace seller, G-Cloud listing for Amazon Connect managed services)",
    "evidence": "Manchester-based Connect specialist working with Amazon Connect since its 2017 launch, with a UK G-Cloud managed-services listing.",
    "also_carries": ["Zoom Contact Center, Zoom Virtual Agent, Zoom Phone"],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://acceleraate.com/platforms/aws/amazon-connect", "date": "2026", "note": "Connect since 2017, Zoom lines"}
    ]
  },
  {
    "name": "Ventrica",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "bpo_cx_outsourcer",
    "connect_relationship": "listed partner (offers Amazon Connect licences; no APN designation verified)",
    "evidence": "Ventrica sells flexible CX licences for Zendesk and Amazon Connect (AWS) with rapid setup as part of its outsourced contact centre offer.",
    "also_carries": ["Zendesk (Premier Partner)", "Twilio"],
    "scale_signal": "16+ years trading",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.ventrica.co.uk/", "date": "2026", "note": "Connect and Zendesk licences"}
    ]
  },
  {
    "name": "PwC",
    "hq_country": "United Kingdom (PwC UK)",
    "emea_coverage": ["UK"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026",
    "evidence": "PwC UK runs Execution Managed Services on Amazon Connect and PwC is a named launch partner of the 2026 Connect Customer competency.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/from-legacy-to-ai-powered-transform-your-customer-experience-with-amazon-connect-customer-competency-partners/", "date": "2026-06-16", "note": "competency partner"}
    ]
  },
  {
    "name": "Accenture",
    "hq_country": "Ireland",
    "emea_coverage": ["UK", "Ireland", "Austria", "Switzerland", "EMEA-wide"],
    "partner_type": "systems_integrator",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026; 2019 Service Delivery launch partner",
    "evidence": "2025 AWS Consulting Partner of the Year for UK and Ireland and for Alps, and a named launch partner of the Connect Customer competency; no EMEA-specific Connect case study surfaced in this run.",
    "also_carries": [],
    "scale_signal": "AWS Consulting Partner of the Year UKI and Alps, Dec 2 2025",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/announcing-the-regional-2025-aws-partners-of-the-year-for-europe-middle-east-and-africa/", "date": "2025-12-02", "note": "UKI and Alps awards"},
      {"url": "https://aws.amazon.com/blogs/apn/from-legacy-to-ai-powered-transform-your-customer-experience-with-amazon-connect-customer-competency-partners/", "date": "2026-06-16", "note": "competency partner"}
    ]
  },
  {
    "name": "Deloitte Digital",
    "hq_country": "United Kingdom (DTTL)",
    "emea_coverage": ["Benelux", "Germany", "Sub-Saharan Africa", "EMEA-wide"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026; 2019 Service Delivery launch partner",
    "evidence": "Deloitte's global AWS alliance page carries a 'Tailored Customer Experiences via Amazon Connect' offer, and Deloitte won 2025 Consulting Partner of the Year in Benelux, Germany and Sub-Saharan Africa.",
    "also_carries": [],
    "scale_signal": "Three 2025 EMEA regional Consulting Partner of the Year awards, Dec 2 2025",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.deloitte.com/global/en/alliances/aws.html", "date": "2026", "note": "Connect offer, Premier tier"},
      {"url": "https://aws.amazon.com/blogs/apn/announcing-the-regional-2025-aws-partners-of-the-year-for-europe-middle-east-and-africa/", "date": "2025-12-02", "note": "regional awards"}
    ]
  },
  {
    "name": "Reply (Storm Reply)",
    "hq_country": "Italy",
    "emea_coverage": ["Italy", "Germany", "UK", "France"],
    "partner_type": "systems_integrator",
    "connect_relationship": "listed partner (Storm Reply markets 'Boost your CX with Amazon Connect'; AWS Premier; no Connect designation verified)",
    "evidence": "Storm Reply publishes an Amazon Connect offering and Reply cites an AWS-based contact center for Generali Country Italia; Reply was 2025 AWS Consulting Partner of the Year Italy.",
    "also_carries": [],
    "scale_signal": "1,000+ AWS certifications, 16 competencies; Storm Reply offices in 5 German, 3 Italian, 7 UK cities plus Paris",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.reply.com/storm-reply/en/", "date": "2026", "note": "Connect offering, offices"},
      {"url": "https://aws.amazon.com/blogs/apn/announcing-the-regional-2025-aws-partners-of-the-year-for-europe-middle-east-and-africa/", "date": "2025-12-02", "note": "Italy award"}
    ]
  },
  {
    "name": "LionGate AG",
    "hq_country": "Germany",
    "emea_coverage": ["Germany"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Service Delivery (added Jan 2025, APN post Feb 13 2025)",
    "evidence": "Named as an EMEA Amazon Connect Service Delivery partner in the APN January 2025 additions; site positions Salesforce Agentforce Contact Center alongside.",
    "also_carries": ["Salesforce Agentforce Contact Center"],
    "scale_signal": "50+ employees, 300+ large projects (own claims)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/say-hello-to-201-new-aws-competency-service-delivery-service-ready-and-msp-partners-added-in-january/", "date": "2025-02-13", "note": "LionGate AG, EMEA, Connect SDP"},
      {"url": "https://www.liongate.de/", "date": "2026", "note": "scale, Salesforce focus"}
    ]
  },
  {
    "name": "Awiant (formerly Elastic Move / Buzzcloud)",
    "hq_country": "Sweden",
    "emea_coverage": ["Sweden", "Nordics"],
    "partner_type": "consultancy",
    "connect_relationship": "Amazon Connect Service Delivery (added Oct 2025 under Elastic Move AB / Buzzcloud AB, APN post Nov 3 2025); AWS Advanced Consulting Partner",
    "evidence": "Elastic Move/Buzzcloud were tagged as an EMEA Connect Service Delivery partner in Nov 2025; both domains now redirect to Awiant, whose site does not mention Connect.",
    "also_carries": [],
    "scale_signal": "Offices Stockholm, Malmö, Karlstad; customers named include Scania, Thule, Volkswagen Financial Services",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/say-hello-to-322-new-aws-competency-service-delivery-service-ready-and-msp-partners-added-in-october/", "date": "2025-11-03", "note": "Elastic Move AB / Buzzcloud AB, EMEA, Connect SDP"},
      {"url": "https://awiant.com/", "date": "2026", "note": "rebrand, Advanced tier"}
    ]
  },
  {
    "name": "Synthesis Software Technologies",
    "hq_country": "South Africa",
    "emea_coverage": ["South Africa"],
    "partner_type": "consultancy",
    "connect_relationship": "listed partner (Amazon Connect services and Contact Center Intelligence referenced; AWS Advanced Consulting Partner; no Connect designation verified)",
    "evidence": "Synthesis lists Amazon Connect and CCI services and was 2025 AWS Rising Star Consulting Partner for Sub-Saharan Africa.",
    "also_carries": [],
    "scale_signal": "Client roster includes Absa, Standard Bank, Nedbank, FNB, Capitec, Vodacom, Pick n Pay",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.synthesis.co.za/", "date": "2026", "note": "Connect and CCI services, clients"},
      {"url": "https://aws.amazon.com/blogs/apn/announcing-the-regional-2025-aws-partners-of-the-year-for-europe-middle-east-and-africa/", "date": "2025-12-02", "note": "SSA Rising Star"}
    ]
  },
  {
    "name": "Infosys",
    "hq_country": "India",
    "emea_coverage": ["Europe (generic presence; no EMEA Connect deployment verified)"],
    "partner_type": "systems_integrator",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026",
    "evidence": "Named launch partner of the 2026 Connect Customer competency; no EMEA case study verified.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/from-legacy-to-ai-powered-transform-your-customer-experience-with-amazon-connect-customer-competency-partners/", "date": "2026-06-16", "note": "competency partner"}
    ]
  },
  {
    "name": "NTT DATA",
    "hq_country": "Japan",
    "emea_coverage": ["UK", "South Africa", "Europe (generic)"],
    "partner_type": "systems_integrator",
    "connect_relationship": "Amazon Connect Customer Services Competency (Contact Center Transformation), named Jun 16 2026; NTT Communications was a 2019 Service Delivery launch partner; AWS strategic collaboration agreement for AI contact center Oct 2025",
    "evidence": "Named launch partner of the 2026 Connect Customer competency; signed a strategic collaboration agreement with AWS to deliver AI-powered contact center solutions (Oct 6 2025).",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/from-legacy-to-ai-powered-transform-your-customer-experience-with-amazon-connect-customer-competency-partners/", "date": "2026-06-16", "note": "competency partner"},
      {"url": "https://de.tradingview.com/news/reuters.com,2025-10-06:newsml_Zaw7KwDvw:0-pressr-ntt-data-signs-strategic-collaboration-agreement-with-aws-to-deliver-ai-powered-contact-center-solutions", "date": "2025-10-06", "note": "AWS SCA for AI contact center"}
    ]
  },
  {
    "name": "Cognizant",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Europe (generic; no EMEA Connect deployment verified)"],
    "partner_type": "systems_integrator",
    "connect_relationship": "Amazon Connect Service Delivery launch partner (May 2019)",
    "evidence": "One of the 15 original Connect Service Delivery partners; Cognizant AWS page returned 404 in this run.",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://aws.amazon.com/blogs/apn/building-a-cloud-based-contact-center-with-amazon-connect-service-delivery-partners", "date": "2019-05-15", "note": "launch partner"}
    ]
  },
  {
    "name": "Concentrix",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Europe (generic BPO footprint)"],
    "partner_type": "bpo_cx_outsourcer",
    "connect_relationship": "listed partner (AWS on partners page; no Connect-specific designation verified)",
    "evidence": "Concentrix's partners page lists AWS alongside Genesys and NICE; no Connect-specific EMEA evidence found.",
    "also_carries": ["Genesys", "NICE", "Salesforce, Microsoft, Google"],
    "scale_signal": "none found",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.concentrix.com/partners/", "date": "2026", "note": "vendor list"}
    ]
  },
  {
    "name": "Westcon-Comstor",
    "hq_country": "United Kingdom",
    "emea_coverage": ["EEA (30+ countries)", "Switzerland", "UK", "Ireland"],
    "partner_type": "distributor",
    "connect_relationship": "AWS authorised distributor and AWS Marketplace channel (no Connect-specific programme published)",
    "evidence": "Signed Europe-wide AWS distribution covering the EEA plus Switzerland and UKI on Nov 28, 2024, with Rebura (Premier) as its services arm.",
    "also_carries": [],
    "scale_signal": "30+ countries under the AWS agreement",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.westconcomstor.com/global/en/news/announcements/2024/westcon-comstor-to-distribute-aws-solutions-across-europe.html", "date": "2024-11-28", "note": "AWS Europe distribution"}
    ]
  },
  {
    "name": "TD SYNNEX",
    "hq_country": "United States",
    "emea_coverage": ["EMEA-wide"],
    "partner_type": "distributor",
    "connect_relationship": "AWS Distributor, Premier Tier Services Partner, AWS Marketplace via StreamOne (no Connect-specific programme published)",
    "evidence": "AWS EMEA Distributor Partner of the Year (Public Sector) 2025; marketplace enablement via StreamOne.",
    "also_carries": [],
    "scale_signal": "none Connect-specific",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.barchart.com/story/news/36413753/td-synnex-awarded-2025-aws-partner-awards", "date": "2025-12", "note": "2025 AWS awards"}
    ]
  },
  {
    "name": "Ingram Micro",
    "hq_country": "United States",
    "emea_coverage": ["EMEA-wide", "UAE, Saudi Arabia, Qatar, Bahrain, Kuwait, Oman, Lebanon, Jordan (resell authorised)"],
    "partner_type": "distributor",
    "connect_relationship": "AWS Distributor (Global Distributor Partner of the Year, four consecutive years); no Connect-specific programme published",
    "evidence": "Dec 16, 2025 release confirms dual 2025 global distributor awards and new commercial and public sector AWS resell authorisation across eight Middle East countries.",
    "also_carries": [],
    "scale_signal": "8 AWS competencies, 14 service validations, 500+ AWS certifications (global)",
    "confidence": "LOW",
    "sources": [
      {"url": "https://ir.ingrammicro.com/press-releases/detail/951/ingram-micro-strengthens-global-aws-leadership-with-dual-2025-aws-partner-awards", "date": "2025-12-16", "note": "awards, Middle East authorisation"}
    ]
  }
]
```

## SHARE

```json
{
  "vendor_emea_share": "no public figure",
  "sources": [
    {"url": "https://aws.amazon.com/blogs/contact-center/frost-radar-recognizes-aws-as-a-2024-leader-for-contact-center-as-a-service-in-apac-and-emea", "date": "2024-09-16", "note": "Frost Radar Cloud Contact Centers EMEA 2024: AWS named a Leader; no share or seat figure"},
    {"url": "https://pages.awscloud.com/GLOBAL-brand-awareness-content-download-25-gartner-ardm-magic-quadrant-for-contact-center-as-a-service-mq-learn.html", "date": "2025-09-08", "note": "Gartner MQ CCaaS 2025: AWS a Leader, third consecutive year; global, no figure"},
    {"url": "https://www.cmswire.com/contact-center/ai-powered-contact-center-as-a-service-vendors-battle-for-market-share-in-2025/", "date": "2025-07-14", "note": "Research and Markets worldwide CCaaS share report (Jul 10 2025): seat ranking NICE #1, Genesys #2, Amazon Connect #3, Five9 #4 as of Dec 2024; global, no percentages"},
    {"url": "https://ir.aboutamazon.com/news-release/news-release-details/2025/Amazon-com-Announces-Third-Quarter-Results/", "date": "2025-10-30", "note": "Amazon: Connect reached a $1B annualized revenue run rate; 12 billion interaction minutes over the past year; global"},
    {"url": "https://6sense.com/tech/cloud-contact-center-software/amazon-connect-market-share", "date": "2026", "note": "Web-tech tracker, not analyst data: 5,251 tracked Connect customers, UK 428 customers (9.34 percent of tracked base). Directional footprint signal only"}
  ],
  "notes": "No Gartner, IDC, Frost, Omdia, Cavell or Metrigy figure for Amazon Connect share in EMEA or Europe is public. The nearest published positioning is Frost Radar EMEA 2024 (Leader) and the IDC European MarketScape Oct 2025, where the secondary summary does not place AWS among the three Leaders. Partner-level share: none published; the only partner scale signals are self-reported (CloudInteract GBP 3M to 5M revenue, Sabio 650+ customers across all vendors)."
}
```

## Gaps

- Checked and NOT verified as Amazon Connect partners: Kerv (Genesys Elite, Verint Elite, Microsoft), Zoi, Nordcloud/IBM, Knowit, Orange Business (Connect page 404), iOCO, BBD, e& enterprise.
- Not reached at all: Capgemini, HCLTech, Tech Mahindra, Wipro, BT Business, Vodafone Business, T-Systems, Telefonica Tech, Teleperformance, Webhelp, Eviden/Atos, Rackspace, Slalom, EY, KPMG, Cloud4C, Bespin, Integra, Devoteam.
- Regional holes with zero named Connect delivery partners verified: Benelux, France (beyond Storm Reply's Paris office), Iberia (beyond Sabio Spain), CEE, Turkey, Israel, Gulf (SnapTec only, HQ inferred and dropped from the map).
- AWS Partner Finder detail pages are JavaScript-rendered, so designation strings for Sabio, SVL, Acceleraate, Ventrica, Storm Reply, and Synthesis remain "listed partner".
- No EMEA-specific Connect case study was found for any GSI; their inclusion rests on global competency or 2019 launch-partner status.
