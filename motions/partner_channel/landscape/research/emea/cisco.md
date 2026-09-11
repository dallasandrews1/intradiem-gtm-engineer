# Cisco contact center, EMEA channel research pass (Sep 2 2026, signal-researcher, public sources only)

## Vendor context

Cisco's EMEA revenue was $14.824B in fiscal 2025, about 26% of $56.7B total, with Collaboration segment revenue of $4.154B (Cisco Q4 FY25 release, Aug 13 2025). Contact center goes to market almost entirely through partners under the Cisco 360 Partner Program, launched Jan 25 2026, which retired Gold/Premier/Select on Jan 24 2026 and replaced them with Preferred Partner and Portfolio Partner designations per architecture (Collaboration is one of five), plus Solution Specializations and Cisco Powered Services accreditations, of which "Webex Contact Center" is one. Pre-2026 sources still cite Gold, Master Collaboration, and the "Customer Experience" specialization. Cisco recognises CX partners mainly through the WebexOne partner awards (EMEA Customer Experience winners: BrightCloud Group 2023, Cisilion 2024, Natilik 2025 EMEA and Global) and Partner Summit geo awards (EMEA Partner of the Year 2025: Emircom; EMEA Distributor of the Year 2025: TD SYNNEX; Global SP Partner of the Year 2025: Telefonica). Distribution runs through Comstor (Westcon-Comstor, self-described "#1 Cisco distributor" and the only Cisco-dedicated VAD, with Webex Contact Centre enablement services) and TD SYNNEX. Published share: no Europe- or EMEA-specific Cisco contact center share figure is public. Frost & Sullivan sized EMEA cloud contact center at EUR 1.7B (2023) growing 17% and plotted Cisco among 19 vendors without disclosing shares (Jul 4 2024). IDC's "European Contact Center Market Shares, 2024" names Genesys, Avaya and Zendesk as the top three, so Cisco is outside the European top three by IDC's cut. Global proxies: Metrigy 2025 CCaaS: Cisco unranked by percentage but fastest-growing at 41.8% YoY; Metrigy MetriRank Jul 9 2025 ranks Cisco #4 overall and #8 by market share; Gartner CCaaS MQ 2025 moved Cisco from Challenger (2024) to Niche Player. Cisco's own global figures: Webex Contact Center seats up 75% in FY24 and roughly 30% of wins net-new logos (Cavell, Oct 2024).

## PARTNERS

```json
[
  {
    "name": "Natilik",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Gold Partner (legacy), Quad Master, Customer Experience Specialised, Webex Contact Centre authorised; WebexOne 2025 Customer Experience Partner of the Year EMEA and Global",
    "evidence": "Named EMEA and Global Customer Experience Partner of the Year at WebexOne 2025 for Webex Contact Center bookings and enablement.",
    "also_carries": ["NiCE (Gold Partner; NICE Disruptor Partner of the Year 2025 per Natilik awards page)", "Verint (listed partner)", "Calabrio (listed partner)", "Microsoft (Solutions Partner Modern Work)"],
    "scale_signal": "Offices London, New York, Sydney; Webex blog says it supports 'tens of thousands of agents'; no revenue or headcount found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://blog.webex.com/collaboration/announcing-the-2025-webex-partner-award-winners/", "date": "2025-10-02", "note": "EMEA CX Partner of the Year"},
      {"url": "https://www.natilik.com/news/natilik-is-named-global-customer-experience-partner-of-the-year-at-webexone/", "date": "2025-10-03", "note": "Global CX award"},
      {"url": "https://www.natilik.com/partners/cisco/", "date": "fetched 2026-09-02", "note": "tiers and Webex CC authorisation"},
      {"url": "https://www.natilik.com/partners/", "date": "fetched 2026-09-02", "note": "Cisco, NICE, Verint, Calabrio listed"}
    ]
  },
  {
    "name": "NTT DATA",
    "hq_country": "Japan",
    "emea_coverage": ["UK", "Ireland", "DACH", "Benelux", "France", "Iberia", "Italy", "Nordics", "CEE", "Gulf", "South Africa"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco Global Gold (legacy); Cisco Powered Services specialisation in Webex Contact Center; Global Sustainability Partner of the Year 2025",
    "evidence": "NTT DATA blog states it holds the Cisco Powered Services specialisation for Webex Contact Center and sells it inside its CX Managed Services; Cisco blog confirms Webex Calling plus Webex Contact Center delivery worldwide.",
    "also_carries": [],
    "scale_signal": "Up to 2 million joint-customer users expected to migrate to cloud voice over 36 months (Cisco blog, Apr 18 2023)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://services.global.ntt/en-us/insights/blog/ntt-data-and-cisco-an-innovative-future-proof-partnership", "date": "undated, surfaced 2026-09-02", "note": "Webex CC Cisco Powered Services claim"},
      {"url": "https://blogs.cisco.com/partner/answering-the-need-for-cloud-calling-and-collaboration-with-cisco-webex-and-ntt", "date": "2023-04-18", "note": "Global Gold, Webex CC, 2M users"}
    ]
  },
  {
    "name": "Orange Business",
    "hq_country": "France",
    "emea_coverage": ["France", "UK", "DACH", "Benelux", "Iberia", "Italy", "Nordics", "CEE", "Gulf", "Africa"],
    "partner_type": "carrier",
    "cisco_relationship": "Cisco Global Partner; Global Gold Integrator (UC); Preferred Collaboration Partner in 10+ countries under Cisco 360; Webex Contact Center in the 'Workplace Together' bundle",
    "evidence": "Orange's 'Workplace Together [Webex]' bundle includes Webex Contact Center; Webex customer story (Aug 1 2025) says 100+ customers on Workplace Together Essentials.",
    "also_carries": ["Genesys (Unified Engagement Suite Genesys listed on Orange Cisco partner page)"],
    "scale_signal": "250,000 Webex licences deployed; 360+ multinationals served (Orange Cisco partner page)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://blog.webex.com/customer-stories/how-orange-business-moved-seamlessly-from-on-premise-to-the-cloud-with-webex/", "date": "2025-08-01", "note": "Webex CC in portfolio, 100+ customers"},
      {"url": "https://www.orange-business.com/en/about-us/partners/cisco", "date": "fetched 2026-09-02", "note": "tiers, Genesys suite, licence counts"}
    ]
  },
  {
    "name": "BT Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "pan-EMEA via BT Global"],
    "partner_type": "carrier",
    "cisco_relationship": "Cisco Preferred Partner (Cisco 360); Global and EMEA Networking Partner of the Year 2025; Webex Contact Centre product page live",
    "evidence": "BT Business sells a Webex Contact Centre product page alongside its other CC platforms.",
    "also_carries": ["Five9 (BT Business Five9 cloud contact centre)", "Verint (Optimise Cloud Contact, Verint-powered)", "RingCentral RingCX"],
    "scale_signal": "Physical access nodes in 47+ countries (BT Global page); no CC seat figure",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://business.bt.com/calling-messaging-tools/contact-centres/webex-contact-centre/", "date": "fetched 2026-09-02", "note": "Webex CC product page"},
      {"url": "https://business.bt.com/calling-messaging-tools/contact-centres/", "date": "fetched 2026-09-02", "note": "Five9, Verint, RingCX line-up"},
      {"url": "https://business.bt.com/about-us/partnerships/bt-cisco/", "date": "cites 2025 awards", "note": "Preferred Partner, awards"}
    ]
  },
  {
    "name": "Logicalis",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "Channel Islands", "Portugal", "Spain", "Germany", "Netherlands", "Nordics", "CEE"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco Preferred Partner across all five architectures (UK&I and Ireland, Cisco 360); Logicalis Portugal 'Cisco Webex Contact Center Specialized Partner' (May 24 2021)",
    "evidence": "Logicalis UK&I delivered Webex Contact Centre plus managed service to Birmingham City University; Portugal unit holds the Webex CC specialisation.",
    "also_carries": [],
    "scale_signal": "Services in 30+ territories",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.uki.logicalis.com/cisco", "date": "fetched 2026-09-02", "note": "Preferred Partner, BCU Webex CC case"},
      {"url": "https://www.pt.logicalis.com/pt-pt/artigo/news/cisco-webex-contact-center-specialized-partner", "date": "2021-05-24", "note": "Portugal Webex CC specialised"}
    ]
  },
  {
    "name": "Damovo",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Austria", "Switzerland", "Belgium", "Netherlands", "Luxembourg", "Poland", "Ireland", "Sweden", "Finland", "UK"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco 360 Partner; Global Partner Network and Multinational Europe certifications; 200+ Cisco certifications in Germany; Growth Partner of the Year Germany 2025",
    "evidence": "Dedicated Cisco Webex Contact Centre product page plus contact centre consulting practice.",
    "also_carries": ["Genesys (Silver)", "Avaya (Diamond)", "Mitel (Platinum)", "NICE CXone / Cognigy", "Zoom (Gold)", "Microsoft Teams"],
    "scale_signal": "14 countries direct, 150+ supported, 2,600+ customers, 600+ employees, 1.9M endpoints managed",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.damovo.com/products/cisco-webex-contact-centre/", "date": "fetched 2026-09-02", "note": "Webex CC offer, scale"},
      {"url": "https://www.damovo.com/partners/", "date": "fetched 2026-09-02", "note": "all vendor tiers"}
    ]
  },
  {
    "name": "Cisilion",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco 360 Preferred/Portfolio Partner across Collaboration, Networking, Security, Cloud and AI, Services; Webex Contact Centre accreditation; WebexOne 2024 Reimagine Customer Experiences Partner of the Year EMEA",
    "evidence": "Webex blog names Cisilion the 2024 EMEA CX partner of the year for contact center revenue growth; Cisilion lists Webex Contact Centre accreditation.",
    "also_carries": ["Microsoft (licensing, Teams)"],
    "scale_signal": "Two UK offices; no revenue or headcount found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://blog.webex.com/collaboration/2024-webex-partner-award-winners/", "date": "2024-10-30", "note": "EMEA CX award"},
      {"url": "https://www.cisilion.com/news-blog/cisco-360-partner-statuses-cisilion/", "date": "2026-01-25", "note": "360 statuses, Webex CC accreditation"}
    ]
  },
  {
    "name": "BrightCloud Group",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "WebexOne 2023 Reimagine Customer Experiences Partner of the Year EMEA; described by Webex as a UK contact center specialist",
    "evidence": "Webex blog credits BrightCloud with large Webex Contact Center wins fuelling triple-digit growth in 2023.",
    "also_carries": [],
    "scale_signal": "Triple-digit growth claim (Webex, 2023); no absolute figures",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://blog.webex.com/hybrid-work/2023-webex-partner-award-winners", "date": "2023-10-27", "note": "EMEA CX award"}
    ]
  },
  {
    "name": "Bucher + Suter",
    "hq_country": "Switzerland",
    "emea_coverage": ["Switzerland", "Germany", "DACH"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco Preferred Partner (Cisco 360); Webex CX partner spotlight Nov 2025; installed the first Cisco IPCC in 2000; 20+ years Cisco contact center",
    "evidence": "Webex blog lists Bucher + Suter among top Cisco CX partners with 600% YoY growth and deep Salesforce integration; company pages sell Webex Contact Center.",
    "also_carries": ["Salesforce (Service Cloud Voice, Agentforce; partner since 2012)", "ServiceNow, Microsoft Dynamics (CRM integration)"],
    "scale_signal": "120+ specialists, 400+ projects, offices in Switzerland, Germany, USA; 600% YoY growth (Webex, Nov 2025)",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://blog.webex.com/customer-experience/shining-a-spotlight-on-our-top-cisco-partners-driving-webex-cx-transformation/", "date": "2025-11-14", "note": "only EMEA partner in Cisco's top CX list"},
      {"url": "https://www.bucher-suter.com/", "date": "fetched 2026-09-02", "note": "Preferred Partner, Webex CC"}
    ]
  },
  {
    "name": "Deutsche Telekom (T-Systems)",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Austria", "Netherlands", "CEE", "pan-Europe via T-Systems"],
    "partner_type": "carrier",
    "cisco_relationship": "Cisco Preferred Collaboration Partner (Telekom Germany page); T-Systems Gold Integrator and Master Collaboration (legacy); WebexOne 2025 Employee Experience Partner of the Year EMEA (1,500+ Webex Suite deals in FY25)",
    "evidence": "Telekom's business site sells Webex Contact Center for customer service; Telekom also runs Webex Contact Center internally (3,500 agents, Webex Luminary award Oct 7 2025).",
    "also_carries": [],
    "scale_signal": "1,500+ Webex Suite deals FY25; internal Webex CC 3,500 agents",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://geschaeftskunden.telekom.de/business/loesungen/digitalisierung/zusammenarbeit-produktivitaet/cisco-webex", "date": "fetched 2026-09-02", "note": "Webex CC offer, Preferred Collaboration Partner"},
      {"url": "https://blog.webex.com/collaboration/announcing-the-2025-webex-partner-award-winners/", "date": "2025-10-02", "note": "EMEA Employee Experience award"},
      {"url": "https://www.t-systems.com/de/en/partners/cisco", "date": "fetched 2026-09-02", "note": "T-Systems tiers"}
    ]
  },
  {
    "name": "Westcon-Comstor",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Ireland", "DACH", "Benelux", "France", "Iberia", "Italy", "Nordics", "CEE", "Gulf", "South Africa"],
    "partner_type": "distributor",
    "cisco_relationship": "Comstor: self-described '#1 Cisco distributor' and only Cisco-dedicated value-add distributor; Comstor Webex team supports partners on Webex Contact Centre",
    "evidence": "Comstor Middle East Webex page names Webex Contact Centre enablement services for partners.",
    "also_carries": [],
    "scale_signal": "'25 years exclusive Cisco focus' claim",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.westconcomstor.com/me/en/vendors/cisco/collaboration/webex.html", "date": "surfaced 2026-09-02", "note": "Webex CC support services"},
      {"url": "https://www.westconcomstor.com/se/en/comstor.html", "date": "fetched 2026-09-02", "note": "#1 Cisco distributor claim"}
    ]
  },
  {
    "name": "TD SYNNEX",
    "hq_country": "United States",
    "emea_coverage": ["UK", "Germany", "Norway", "Nordics", "Benelux", "France", "Iberia", "Italy", "CEE"],
    "partner_type": "distributor",
    "cisco_relationship": "Cisco Global Distributor of the Year 2025; EMEA Distributor of the Year 2025; Distributor of the Year Germany and Norway 2025",
    "evidence": "TD SYNNEX IR release lists the 2025 Cisco distributor awards; collaboration hub covers Webex but no Webex CC-specific programme found.",
    "also_carries": [],
    "scale_signal": "Award-level only; no Cisco EMEA revenue split public",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://ir.tdsynnex.com/news/news-details/2025/TD-SYNNEX-Wins-Global-and-Regional-Distributor-of-the-Year-Honors-at-Cisco-Partner-Summit-2025/default.aspx", "date": "2025-11-10", "note": "EMEA Distributor of the Year"}
    ]
  },
  {
    "name": "Virgin Media O2 Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK"],
    "partner_type": "carrier",
    "cisco_relationship": "listed partner (Cisco Webex Contact Centre product page, no tier stated)",
    "evidence": "VMO2 Business sells a Cisco Webex Contact Centre product page (voice, chat, email, social, text).",
    "also_carries": [],
    "scale_signal": "none found",
    "confidence": "HIGH",
    "sources": [
      {"url": "https://www.virginmediao2business.co.uk/voice-solutions/cisco-webex-contact-centre/", "date": "fetched 2026-09-02", "note": "Webex CC product page"}
    ]
  },
  {
    "name": "Vodafone Business",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Germany", "Italy", "Spain", "Ireland", "Portugal", "Greece", "CEE"],
    "partner_type": "carrier",
    "cisco_relationship": "listed partner; 'Vodafone Business Contact Center - Webex Service' described in contract terms as a SaaS omnichannel CC integrated with Cisco IP telephony (inferred from contract document)",
    "evidence": "Vodafone service terms document describes a Webex-based contact center service; product marketing page not located.",
    "also_carries": [],
    "scale_signal": "none found for CC",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://manuals.plus/m/223a62f531a434e2ca7d7f661192fb7e3b723a853043b2396648e6bd3ea61a41_pdf", "date": "surfaced 2026-09-02", "note": "contract text naming Contact Center - Webex Service"}
    ]
  },
  {
    "name": "Axians (VINCI Energies)",
    "hq_country": "France",
    "emea_coverage": ["France", "Germany", "Netherlands", "Belgium", "Portugal", "Spain", "Italy", "Switzerland", "Austria", "CEE"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "listed Cisco partner; published a Webex Contact Center CCaaS positioning article; Webex Calling partner microsite (NL)",
    "evidence": "Axians news article 'Webex Contact Center: Redefining Intelligent CCaaS' describes Webex as a strategic CX partner.",
    "also_carries": [],
    "scale_signal": "VINCI Energies ICT brand, multi-country",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.axians.com/news/redefining-intelligent-contact-centers-with-webex/", "date": "undated", "note": "Webex CC article"}
    ]
  },
  {
    "name": "CANCOM (incl. CANCOM Austria, ex Kapsch BusinessCom)",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Austria", "Switzerland", "CEE"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco 360 partner (tier not stated); long-standing collaboration partner; Webex Contact Center listed on CANCOM's Cisco UCC page",
    "evidence": "CANCOM's Cisco UCC page lists Webex Contact Center among supported Webex products.",
    "also_carries": [],
    "scale_signal": "Kapsch BusinessCom pre-acquisition: 1,300+ employees, EUR 300M+ revenue",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://cisco.cancom.de/ucc/", "date": "fetched 2026-09-02", "note": "Webex CC listed"}
    ]
  },
  {
    "name": "IST Networks",
    "hq_country": "Egypt (Saudi Arabia operations)",
    "emea_coverage": ["Saudi Arabia", "Egypt", "UAE", "Gulf"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "listed partner selling Cisco Webex Cloud Contact Center (tier not stated)",
    "evidence": "Dedicated Webex Cloud Contact Center page targeting Saudi Arabia.",
    "also_carries": ["Genesys (Cloud CX, Connect, DX, IWD)", "Verint (WFO, QM, performance management)"],
    "scale_signal": "none found",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.istnetworks.com/webex-cloud-contact-center/", "date": "fetched 2026-09-02", "note": "Webex CC page, Genesys and Verint lines"}
    ]
  },
  {
    "name": "solutions by stc",
    "hq_country": "Saudi Arabia",
    "emea_coverage": ["Saudi Arabia", "UAE", "Bahrain", "Kuwait", "Jordan", "Qatar", "Oman", "Iraq"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "WebexOne 2024 Webex Managed Services Award EMEA; stc was first Cisco WebEx authorised partner in Middle East (2009)",
    "evidence": "Webex blog names Solutions by STC the 2024 EMEA managed services winner; contact center specificity not confirmed.",
    "also_carries": [],
    "scale_signal": "Network across 9 Gulf and Levant countries",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://blog.webex.com/collaboration/2024-webex-partner-award-winners/", "date": "2024-10-30", "note": "EMEA managed services award"}
    ]
  },
  {
    "name": "Emircom",
    "hq_country": "United Arab Emirates",
    "emea_coverage": ["UAE", "Saudi Arabia", "Egypt"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco EMEA Partner of the Year 2025 (Partner Summit)",
    "evidence": "Cisco names Emircom EMEA Partner of the Year 2025; Emircom site lists Contact Center under Collaboration and a managed CCaaS ('PowerEngage'), platform vendor not stated.",
    "also_carries": [],
    "scale_signal": "6 offices, 4 countries, founded 1984",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://blogs.cisco.com/partner/celebrating-excellence-our-2025-global-award-winners", "date": "2025-11-06", "note": "EMEA Partner of the Year"},
      {"url": "https://www.emircom.com/", "date": "fetched 2026-09-02", "note": "CC offering, offices"}
    ]
  },
  {
    "name": "Pure IP",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "pan-EMEA PSTN"],
    "partner_type": "carrier",
    "cisco_relationship": "Certified Calling Provider, Cloud Connect for Webex Calling; supports high-volume Webex Contact Center deployments",
    "evidence": "Pure IP release states its Cloud Connect service supports demanding high-volume Webex Contact Center deployments.",
    "also_carries": ["Microsoft Teams (Operator Connect / Direct Routing)", "Zoom Phone"],
    "scale_signal": "Voice coverage 137 countries",
    "confidence": "MEDIUM",
    "sources": [
      {"url": "https://www.prnewswire.com/news-releases/pure-ip-launches-webex-calling-solution-for-pstn-connectivity-301691723.html", "date": "2022-12", "note": "Webex CC deployment support"}
    ]
  },
  {
    "name": "Atea",
    "hq_country": "Norway",
    "emea_coverage": ["Norway", "Sweden", "Denmark", "Finland", "Baltics"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Highest Cisco partner status (Atea strategic partner list); WebexOne 2025 Future Proof Workplaces Partner of the Year EMEA",
    "evidence": "Awards are device and meeting-room focused; no Cisco contact center sale or delivery evidence found (inferred).",
    "also_carries": [],
    "scale_signal": "~NOK 37B (EUR 3.2B) revenue 2025, 8,000+ employees, 88 cities",
    "confidence": "LOW",
    "sources": [
      {"url": "https://blog.webex.com/collaboration/announcing-the-2025-webex-partner-award-winners/", "date": "2025-10-02", "note": "EMEA workplaces award"},
      {"url": "https://www.atea.com/partners/", "date": "fetched 2026-09-02", "note": "scale, strategic partners"}
    ]
  },
  {
    "name": "Telefonica Tech",
    "hq_country": "Spain",
    "emea_coverage": ["Spain", "UK (via VMO2)", "Germany"],
    "partner_type": "carrier",
    "cisco_relationship": "Cisco Global Service Provider Partner of the Year 2025; Telefonica Tech launched Webex Calling in Spain; contact center resale not confirmed (inferred)",
    "evidence": "Cisco 2025 global awards name Telefonica SP Partner of the Year; Webex Calling launch covers Attendant Console, not Webex Contact Center.",
    "also_carries": [],
    "scale_signal": "none pulled",
    "confidence": "LOW",
    "sources": [
      {"url": "https://blogs.cisco.com/partner/celebrating-excellence-our-2025-global-award-winners", "date": "2025-11-06", "note": "SP Partner of the Year"}
    ]
  },
  {
    "name": "Computacenter",
    "hq_country": "United Kingdom",
    "emea_coverage": ["UK", "Germany", "France", "Netherlands", "Belgium", "Switzerland"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco Gold (legacy) and self-described fastest-growing Cisco partner in USA and EMEA; Cisco Splunk Partner of the Year EMEA 2025",
    "evidence": "No public evidence of Computacenter selling or delivering Cisco contact center in EMEA found in this run (inferred from collaboration practice only).",
    "also_carries": [],
    "scale_signal": "$500M Cisco US revenue (Computacenter Cisco PDF, undated)",
    "confidence": "LOW",
    "sources": [
      {"url": "https://blogs.cisco.com/partner/celebrating-excellence-our-2025-global-award-winners", "date": "2025-11-06", "note": "Splunk Partner of the Year EMEA"}
    ]
  },
  {
    "name": "Bechtle",
    "hq_country": "Germany",
    "emea_coverage": ["Germany", "Switzerland", "Austria", "Netherlands", "Belgium", "France", "UK", "Iberia", "CEE"],
    "partner_type": "systems_integrator",
    "cisco_relationship": "Cisco Master Collaboration Partner (Jun 21 2021), Gold Integrator; Bechtle Schweiz Gold 2024",
    "evidence": "Collaboration credentials cover cloud calling and Webex; no contact center sale or delivery evidence found (inferred).",
    "also_carries": [],
    "scale_signal": "236 Cisco-certified specialists, 900+ Cisco certifications (2021)",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.bechtle.com/de-en/about-bechtle/press/press-releases/2021/bechtle-becomes-cisco-master-collaboration-partner", "date": "2021-06-21", "note": "Master Collaboration"}
    ]
  },
  {
    "name": "Swisscom",
    "hq_country": "Switzerland",
    "emea_coverage": ["Switzerland"],
    "partner_type": "carrier",
    "cisco_relationship": "WebexOne 2024 Reimagine Work Partner of the Year EMEA; first EMEA SP to move SMB customers from BroadWorks to Webex Calling Wholesale",
    "evidence": "Webex publishes a Wingo (Swisscom brand) customer story on modernising customer care in the cloud, implying a Webex CC deployment; page returned 403 in run (inferred).",
    "also_carries": [],
    "scale_signal": "none pulled",
    "confidence": "LOW",
    "sources": [
      {"url": "https://blog.webex.com/collaboration/2024-webex-partner-award-winners/", "date": "2024-10-30", "note": "EMEA award"}
    ]
  },
  {
    "name": "Proximus NXT",
    "hq_country": "Belgium",
    "emea_coverage": ["Belgium", "Luxembourg", "Netherlands"],
    "partner_type": "carrier",
    "cisco_relationship": "listed Cisco Webex partner (Webex Teams/meetings in Luxembourg); HCLTech partnership references a Webex-based CCaaS offer for Benelux (inferred)",
    "evidence": "Telindus/Proximus NXT sells Webex collaboration; a Webex Contact Center product page was not found.",
    "also_carries": [],
    "scale_signal": "none pulled",
    "confidence": "LOW",
    "sources": [
      {"url": "https://www.telindus.lu/en/products/cisco-webex-teams", "date": "undated", "note": "Webex resale"}
    ]
  }
]
```

Negative findings: Sabio Group partner page names Genesys, Avaya, Amazon Connect, Twilio, Verint, Salesforce and Google Cloud, no Cisco. Britannic Technologies names Five9, 8x8, Mitel, Verint, Puzzel; only Cisco Meraki, no Cisco contact center. Kerv names Genesys only, no Cisco or Webex.

## SHARE

```json
{
  "vendor_emea_share": "no public figure",
  "sources": [
    {"url": "https://store.frost.com/frost-radar-emea-cloud-contact-centers-2024.html", "date": "2024-07-04", "note": "EMEA cloud CC EUR 1.7B (2023), 17% growth, Cisco one of 19 plotted, no share disclosed"},
    {"url": "https://my.idc.com/getdoc.jsp?containerId=EUR153039425", "date": "2025", "note": "IDC European Contact Center Market Shares 2024: top 3 Genesys, Avaya, Zendesk; Cisco not top 3"},
    {"url": "https://metrigy.com/ccaas-metrirank-2025-nice-retains-top-spot/", "date": "2025-07-09", "note": "Global: Cisco #4 overall, #8 by market share"},
    {"url": "https://metrigy.com/2025-enterprise-as-a-service-revenue-continues-to-grow-ccaas-posts-largest-yoy-growth/", "date": "2026", "note": "Global 2025 CCaaS: Cisco fastest growth 41.8% YoY, share % not published"},
    {"url": "https://www.cxtoday.com/contact-center/gartner-magic-quadrant-for-contact-center-as-a-service-ccaas-2025-the-rundown/", "date": "2025", "note": "Cisco Niche Player 2025, Challenger 2024"},
    {"url": "https://www.cavell.com/webex-one-2024-cisco-concentrating-on-its-key-areas-of-strength/", "date": "2024-10", "note": "Global: 75% YoY cloud CC licences, ~30% net-new logos"},
    {"url": "https://investor.cisco.com/news/news-details/2025/CISCO-REPORTS-FOURTH-QUARTER-AND-FISCAL-YEAR-2025-EARNINGS/default.aspx", "date": "2025-08-13", "note": "EMEA $14.824B of $56.7B (~26%); Collaboration $4.154B; no CC split"}
  ],
  "notes": "No analyst house publishes a Cisco EMEA or Europe contact center share number in the open. Best public triangulation: Cisco is inside the top 19 EMEA cloud CC vendors (Frost 2024) but outside IDC's European top three (2024) and 8th globally by CCaaS share (Metrigy 2025) while posting the fastest global growth. Partner-level share signals: Comstor '#1 Cisco distributor' (self-claim); Natilik EMEA and Global CX partner of the year 2025 (Cisco claim); no partner publicly claims 'largest Cisco contact center partner' in any country."
}
```

## Gaps

- Ingram Micro, ALSO, Exclusive Networks and Nuvias Cisco distribution status in EMEA was not verified.
- Cisco Partner Summit 2024 and 2025 EMEA country-level award lists (Collaboration and CX winners) were not extracted.
- Italy, France (beyond Orange and Axians), Benelux (KPN), Nordics (Telia, Telenor), CEE and South Africa (Vox, BCX) partner sweeps were not run; Cisco made Webex Calling and Webex Contact Centre GA in South Africa on Jan 29 2025, no local reseller named.
- Partner scale (revenue, headcount) missing for Natilik, Cisilion, BrightCloud, IST Networks and Emircom.
