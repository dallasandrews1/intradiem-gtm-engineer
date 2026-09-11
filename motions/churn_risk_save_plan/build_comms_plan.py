#!/usr/bin/env python3
"""Cleveland Clinic communication plan on the ADT save precedent (PMO tracker export, 2024-25).
Emits data/comms_plan_cleveland_clinic.json: routes around the blocker, four lanes with owners by role,
dated moves, and the four messages (drafted through the first-draft engine, checked by the sharpener)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent; DATA = HERE / "data"

ROUTES = [
 {"id": "peer-door", "name": "The peer door into IT", "via": "Scott Faini (in Salesforce) to Bob Ganem, Terri Horan and Katherine Neal",
  "why": "The RFP evaluators sit in IT, not under Rena. Faini already knows us. The conversation is platform continuity, which is their question, not ours.", "lane": "Inger", "adt": "ADT: identify contacts within the account, utilize April Mitchell to set up meetings"},
 {"id": "groundswell", "name": "The user groundswell", "via": "Supervisors accepting Coach Now (79.6% acceptance in August) and the AUX teams self-curing 93.8% of alerts",
  "why": "Their own numbers, in their own words, become the impact summary Rena has not seen. Leadership cannot say nobody uses it.", "lane": "Amy", "adt": "ADT: customer references and voice of the customer"},
 {"id": "parallel-team", "name": "The parallel team", "via": "Access to Care leaders already in Salesforce (Patty Nahra, Lisa Griffin) hearing what the hub teams run",
  "why": "A friendlier department with the same workflow. Peer proof travels sideways when it cannot travel up.", "lane": "Amy", "adt": "ADT: new line of business pilot socialised alongside the renewal"},
 {"id": "exec-voice", "name": "The executive voice, held", "via": "Matt McConnell to Dennis Laraway or Bill Peacock, naming Rena and Scott Faini as the engaged team",
  "why": "A different voice at the top, the ADT move that worked. Held until the savings method is agreed with Shantel, because a disputed number at the CFO speeds the exit.", "lane": "Executive voice", "adt": "ADT: CEO outreach, Matt McConnell as a different voice"},
 {"id": "high-and-wide", "name": "High and wide", "via": "Nicole's monthly one-pager to the verified contacts and the Salesforce-known layer, sent as Amy's alias",
  "why": "Keeps the brand in front of everyone who is not in the room while the save runs. Nothing account-specific, nothing to reply to.", "lane": "Nicole and marketing", "adt": "ADT: high-and-wide campaign to 100+ contacts, ISR and AE follow-up calls"},
 {"id": "renewal-track", "name": "The renewal track", "via": "Amy and Mary Ann on the two options, Harmonic presented as continuity with the open issues carried in",
  "why": "Inger's read: a bad migration is the exit trigger. Continuity is the renewal message.", "lane": "Amy", "adt": "ADT: renewal 3-year execution, deal desk engaged"},
]

LANES = [
 {"lane": "Inger", "role": "Account manager", "owns": "The peer door, the executive review, the plan itself"},
 {"lane": "Amy", "role": "Success manager", "owns": "The savings method, cases, paused rules, user proof, the parallel team, Harmonic as continuity"},
 {"lane": "Nicole and marketing", "role": "Marketing", "owns": "High and wide: the verified list, the monthly one-pager, voice-of-customer alignment to every executive contact"},
 {"lane": "Executive voice", "role": "Matt McConnell, Mary Ann Chandler", "owns": "The note to the top, held until the number holds; the Yerian review"},
]

# Dated moves. week = Monday of the week the move belongs to. status: planned | held | done
MOVES = [
 ("Inger", "2026-09-15", "2026-09-19", "Brainstorm with Clint, Nicole and leadership; owners confirmed on the PMO list from this plan", "planned"),
 ("Amy",   "2026-09-15", "2026-09-25", "Case closure dates in writing to the CCF team (00322148, 00321545, 00321947, 00321814, 323900)", "planned"),
 ("Amy",   "2026-09-15", "2026-09-25", "Why End of Shift and Leave Early were paused on Jun 12, and what restarts them", "planned"),
 ("Nicole and marketing", "2026-09-22", "2026-09-26", "Campaign brief accepted; verified list loaded to lemlist as a draft, nothing sent", "planned"),
 ("Inger", "2026-09-22", "2026-09-26", "Call with Scott Faini: platform continuity through the RFP, and who else in IT should hear it", "planned"),
 ("Amy",   "2026-09-22", "2026-10-10", "Savings method session with Shantel, line by line, open since Nov 18 2025", "planned"),
 ("Inger", "2026-09-29", "2026-10-03", "Message 1 to Ganem, Horan and Neal (platform continuity), same week, same numbers", "planned"),
 ("Amy",   "2026-09-29", "2026-10-10", "Two-sentence statements from Coach Now supervisors and the AUX self-cure teams", "planned"),
 ("Nicole and marketing", "2026-10-06", "2026-10-06", "One-pager 1 to the verified contacts and the Salesforce-known layer, sent as Amy's alias", "planned"),
 ("Amy",   "2026-10-06", "2026-10-10", "Message 2, the impact summary, to Rena with the supervisors' words in it", "planned"),
 ("Amy",   "2026-10-13", "2026-10-17", "Message 3, the peer note, to Patty Nahra and Lisa Griffin", "planned"),
 ("Inger", "2026-10-13", "2026-10-17", "Executive review prep with Mary Ann: what Yerian hears, what the CFO note says", "planned"),
 ("Executive voice", "2026-10-20", "2026-10-24", "Message 4, Matt McConnell to Dennis Laraway (or Bill Peacock), naming Rena and Scott Faini", "held"),
 ("Amy",   "2026-10-20", "2026-10-31", "Harmonic migration presented as continuity, open issues carried into the plan", "planned"),
 ("Nicole and marketing", "2026-11-03", "2026-11-03", "One-pager 2; voice-of-customer alignment to every executive contact in Salesforce", "planned"),
 ("Executive voice", "2026-11-03", "2026-11-14", "Mary Ann with Lisa Yerian: the reviewed number, the RFP-agnostic integration, the migration plan", "planned"),
 ("Amy",   "2026-11-17", "2026-11-21", "Monthly adoption review with the reviewed method, the supervisors' statements, the paused rules restarted or retired", "planned"),
 ("Nicole and marketing", "2026-12-01", "2026-12-01", "One-pager 3", "planned"),
 ("Inger", "2026-12-01", "2026-12-09", "Renewal option chosen; Hancock line approached as back-office expansion on its own track", "planned"),
]

# The four messages. Senders: Inger (AM), Amy (SM), Matt McConnell (executive voice). Voice to match each sender's own sent mail before use.
MESSAGES = [
 {"id": "m1", "name": "Message 1: RFP evaluators", "to": "Bob Ganem, Terri Horan, Katherine Neal (Scott Faini by call first)", "from": "Inger", "when": "Week of Sep 29", "route": "peer-door",
  "one_idea": "Whichever platform the RFP picks, Intradiem keeps running on top of it, so the platform decision and the Intradiem decision do not have to be the same decision.",
  "persona": "Back-office technology / ops systems row: integration surface, nothing new to govern, nothing to rip out",
  "subject": "the RFP and what stays put",
  "body": """Hi {{firstName}},

With the contact center RFP open this fall, one part of the stack does not need to move with it: Intradiem runs alongside Avaya today and integrates the same way with Genesys Cloud, NICE and the other platforms on a shortlist like yours, on top of the Verint schedules your teams already keep.

That means the alerts and schedule adjustments the hubs use every day carry across whichever platform wins, without a second migration for the agents.

Would a short technical read on how the integration works against your shortlist help the evaluation?

Inger""",
  "claims": [("Runs on top of existing WFM, integrates with Genesys Cloud, NICE and others without replacing them", "Value Repository, UK stack diversity row and line 86, VERIFIED 1:1"),
             ("Avaya as the current ACD", "Audiences platform read 2026-02-25 (inside 12 months), BO_Customer_CC_Platforms_Sep5.csv"),
             ("Verint as the WFM", "Cleveland Clinic Success Plan (Enhanced Staffing hold note), customer's own record")],
  "qc": "Opens on their world with the dated signal (the fall RFP). Product sentence is concrete. One idea. One question naming the topic. 96 words. No numbers claimed beyond the platform facts. Sender voice to match Inger's own sent mail."},
 {"id": "m2", "name": "Message 2: impact summary for Rena", "to": "Rena Thompson", "from": "Amy", "when": "Week of Oct 6, after the supervisors' statements are in", "route": "groundswell",
  "one_idea": "Here is what your teams did with it last month, in their numbers and their words, and the savings method review is where we agree the rest before January.",
  "persona": "Contact centre / Ops Director row: scale and timing, tied to the live event (the January decision)",
  "subject": "August, in your teams' numbers",
  "body": """Hi Rena,

Before the renewal options get weighed, here is August in your teams' own numbers from the adoption review: supervisors accepted 79.6% of the coaching sessions offered, the AUX teams cleared 93.8% of their own alerts before anyone stepped in, and 4,461 leave-early offers were accepted.

[Two or three sentences from the supervisors, in their words, once Amy has them.]

The savings method is the piece still open from November, and the line-by-line with Shantel is how we close it. Once that number is one you accept, the renewal conversation is about continuity, not a debate.

Can we hold the method session before the options go to your leadership?

Amy""",
  "claims": [("79.6% coaching acceptance, 93.8% AUX self-cure, 4,461 Leave Early accepted (August 2026)", "Cleveland Clinic Adoption Meeting 09.2026 deck, the customer's own data, under 90 days"),
             ("Savings method open since November", "Success Plan notes, 2025-11-06 and Active sheet 2025-11-18")],
  "qc": "Uses only the customer's own adoption numbers; the disputed $719K and 1.9x are deliberately absent. One idea. One ask. Placeholder for the supervisors' words is marked and must be filled before send. Sender voice to match Amy's."},
 {"id": "m3", "name": "Message 3: peer note to the parallel team", "to": "Patty Nahra (Executive Director, Access to Care), Lisa Griffin (Director, Access Optimization)", "from": "Amy", "when": "Week of Oct 13", "route": "parallel-team",
  "one_idea": "The hub teams next to yours run the same workflow with fewer manual adjustments, and the configuration is already built.",
  "persona": "Customer / Service Director row: one lever moving cost and service the same direction",
  "subject": "what the hub teams are running",
  "body": """Hi {{firstName}},

The contact center hubs have been running Intradiem on top of the Verint schedules for two years, and in August the AUX teams cleared 93.8% of their own adherence alerts before a supervisor had to step in, while 4,461 leave-early offers went out and were accepted when volume dropped.

Access to Care carries the same shape of day, so the same configuration would apply without a new build.

Would it be useful to see the hub setup next to your queues?

Amy""",
  "claims": [("93.8% AUX self-cure and 4,461 Leave Early accepted (August 2026)", "Adoption Meeting 09.2026 deck, customer's own data"),
             ("Two years on Verint", "Success Plan Closed sheet: use cases launched May 2024")],
  "qc": "Sideways peer proof, their own numbers. Product named once with a concrete action. One question. 84 words. Recipients are Salesforce-known contacts, not the sponsor line."},
 {"id": "m4", "name": "Message 4: executive note, held", "to": "Dennis Laraway (or Bill Peacock)", "from": "Matt McConnell", "when": "Week of Oct 20, only after the savings method is agreed with Shantel", "route": "exec-voice",
  "one_idea": "The teams under Rena and Scott are already in a working thread on continuity through the RFP; the January decision should not cost their agents a second migration.",
  "persona": "Group / C-level: air cover only, after a thread is live, naming engaged colleagues",
  "subject": "continuity through the RFP",
  "body": """Dennis,

Rena Thompson's contact center team and Scott Faini's group are working through how Intradiem carries across whichever platform your RFP selects, so the January renewal and the platform decision stay separate for the agents.

The savings method has now been reviewed line by line with your team and agreed. I would like fifteen minutes with you before the options go to your leadership, to make sure the commitment we put in the contract matches what you need for 2027.

Matt""",
  "claims": [("Savings method agreed", "MUST BE TRUE before send; Amy's session with Shantel closes it"),
             ("Contract commitment", "Value Repository line 80: a 2X guarantee written into the contract, VERIFIED 1:1, exact contract wording to confirm with Naveen before it is quoted; this draft does not quote the number")],
  "qc": "Under 80 words. Names the engaged colleagues. Held: sends only when the agreed-method line is true. Sender voice to match Matt's."},
]

out = {"account": "Cleveland Clinic", "as_of": "2026-09-11", "precedent": "ADT save play, PMO Progress tracker export (Nov 2024 to Feb 2025): CEO outreach, high-and-wide marketing, customer references, partners, voice of the customer, renewal track",
       "routes": ROUTES, "lanes": LANES,
       "moves": [{"lane": l, "week": w, "due": d, "move": m, "status": s} for l, w, d, m, s in MOVES],
       "messages": MESSAGES,
       "rules": ["Nothing account-specific goes to the sponsor line (Rena, Shantel) except from Amy or Inger.",
                 "The disputed savings figures ($719K YTD, 1.9x) never leave Intradiem until the method is agreed.",
                 "Message 4 is held until the agreed-method line is true.",
                 "Every recipient has a verified email; nobody is added without one.",
                 "Marketing sends as Amy's alias only for the one-pager; no account-specific copy from marketing."]}
(DATA / "comms_plan_cleveland_clinic.json").write_text(json.dumps(out, indent=1))
print("routes", len(ROUTES), "lanes", len(LANES), "moves", len(MOVES), "messages", len(MESSAGES))
for m in MESSAGES: print(m["id"], len(m["body"].split()), "words")
