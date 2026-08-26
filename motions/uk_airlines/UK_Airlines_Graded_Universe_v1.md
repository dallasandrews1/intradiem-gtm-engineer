# UK/Ireland Airlines, graded universe v1

Built Aug 1 2026, Jack Ohagan's lane two. Sourced once in full per the wave runbook; later waves pull from this file and the companion committee CSV, they never re-source. Companion: `UK_Airlines_Committee_Contacts_v1.csv` (76 contacts, wave 1 tagged). Sender identity: Jack Ohagan. NOTHING loads to Lemlist until Jack's do-not-contact list lands.

## The forcing function (verified)

Every passenger who lands 3+ hours late for a reason within the airline's control is owed a fixed cash payment under UK261: **£220** (flights under 1,500km), **£350** (1,500-3,500km), **£520** (over 3,500km, delayed 4+ hours; £260 at 3-4 hours). Per passenger, per flight, set by law, claimable for up to six years. One delayed A320 at ~180 seats is a five-figure exposure event on a single rotation.

Sources: [CAA, Delays](https://www.caa.co.uk/air-passengers/travel-problems-and-rights/flight-delays-and-cancellations/delays/) (compensation bands and thresholds), corroborated by [Which?](https://www.which.co.uk/consumer-rights/advice/i-had-a-flight-delay-or-cancellation-can-i-get-compensation-a366S8c1zHl2) and [MSE](https://www.moneysavingexpert.com/travel/flight-delay-compensation/).

The summer context, also verified at the primary source ([Eurocontrol Flash Briefing week 30, 2026](https://www.eurocontrol.int/publication/eurocontrol-flash-briefing-2026-week-30)):
- All-time European traffic record: **37,659 flights on 24 July 2026**.
- **51,586 flights delayed by ATFM restrictions in week 30 alone — 20% of all flights**.
- Arrival punctuality 72% (i.e. more than one in four flights arrives late).
- Honesty note: week 30 ATFM delay per flight (3.10 min) was DOWN 29% vs week 29's spike. The claim that survives scrutiny is "record traffic, one flight in five held by ATFM restrictions," not "meltdown."

The wedge, same structural shape as the £680 FOS case fee: a public number with a price tag attached, landing on the surfaces Intradiem touches. When disruption hits, the cost isn't only the compensation, it's the claims backlog, the contact-centre surge, and the re-accommodation queue that follow, all workforce-orchestration surfaces. Unresolved complaints escalate to the CAA-approved ADR schemes (AviationADR and CEDR), and the [CAA publishes passenger complaints data](https://www.caa.co.uk/data-and-analysis/uk-aviation-market/passenger-complaints/) by carrier.

**[UNVERIFIED], stays OUT of copy:** the "easyJet June 1 2026, 755 disruptions" figure (secondary aggregators only); any ADR backlog size; per-airline punctuality rankings not read from a CAA dataset; the "8-week to 6-week ADR referral change" (that is an Ofcom telecoms rule, not aviation — do not use).

## Universe

Segments: (1) UK passenger airlines, (2) Irish passenger airlines, (3) major ground-handling operations with large UK/IE workforces (their wedge is turnaround/SLA and the same disruption cascade, not UK261 directly).

Addressability cut, same honesty test as Stars and FS: only carriers whose disruption-cost drivers plausibly move with workforce orchestration (claims-handling backlog, contact-centre surge capacity, ops-control staffing, ground-ops turnaround). Cargo and wet-lease carriers with no consumer claims surface are excluded (ASL Airlines Ireland, CityJet).

| # | Account | Segment | Scale note | Committee found | Wave |
|---|---|---|---|---|---|
| 1 | easyJet (+ holidays arm) | UK airline | Largest UK short-haul operator, Sprint-1 account per the Jul 31 pick | 9 | 1 |
| 2 | Jet2 | UK airline | Leisure carrier, strong contact-centre + ground-ops committee density found | 9 | 1 |
| 3 | Ryanair | IE airline | Europe's largest carrier by passengers, Dublin ops control | 8 | 1 |
| 4 | Aer Lingus | IE airline (IAG) | Full committee incl. COO found | 8 | 1 |
| 5 | Virgin Atlantic | UK airline | Long-haul, £520-band exposure, COO + Head of Customer Contact found | 5 | 1 |
| 6 | British Airways | UK airline (IAG) | Largest UK carrier; thin committee via Clay (4), backfill later | 3 | 1 |
| 7 | Swissport | Ground handling | Largest handler footprint in the pull (12 contacts) | 12 | 2 |
| 8 | dnata | Ground handling | Major UK stations | 9 | 2 |
| 9 | Menzies Aviation | Ground handling | Edinburgh HQ | 3 | 2 |
| 10 | Emerald Airlines | IE regional (Aer Lingus Regional) | Small, keep for IE coverage | 4 | 2 |
| 11 | Loganair | UK regional | Small | 3 | 2 |
| 12 | Wizz Air UK | UK airline | Thin committee via Clay (2); note fined/criticised publicly on claims handling in prior years — check before copy | 2 | 2 |

**Coverage gap, logged honestly: TUI Airways = 0 contacts.** Three identifier passes (tui.co.uk, tuigroup.com, linkedin.com/company/tui, tui.com) resolved nothing in Clay's dataset. TUI is a top-5 UK leisure carrier and belongs in this universe; source its committee via Sales Nav or Apollo in a later pass. Do not treat this universe as TUI-complete.

## Launch window (staged Aug 1 after the premortem)

Airlines wave 1 is deliberately NOT an August launch. Ops, ground and OCC seats are in peak firefighting and FS-style August responsiveness doesn't exist in an airline summer. Target: Start in the last week of August at the earliest, so the sequence's back half (calls, "six years", breakup) lands in early-to-mid September, right after peak ends, while the summer's claims backlog is arriving and the pain is fresh. The Eurocontrol figures in copy are July-stamped; if Start slips past mid-September, refresh them from the then-current flash briefing before load. The insurance/FS lane has no season and can start as soon as its gates clear; it goes first.

## Grading logic

Wave 1 = the six passenger airlines with the largest UK/IE consumer disruption surface and the committee density to run Jack's sprint (42 contacts, inside the 30-50 wave band). easyJet leads as the agreed Sprint-1 account. Ground handlers are wave 2: real workforce-orchestration targets, but the UK261 wedge lands differently (their exposure is contractual SLA, not passenger compensation), so their copy needs its own forcing-function line and must NOT reuse the airline spine.

## Buying committee, seats as found

| Seat | Wave-1 count | Why they care |
|---|---|---|
| COO / Ops Director | 13 | Economic buyer; owns the disruption cost end to end |
| Ground/Airport Ops Director | 13 | Owns turnaround and the delay-minutes the compensation clock runs on |
| Customer Operations / CX / Contact Centre | 9 | Owns the claims queue and the surge the day after disruption |
| Resource Planning / WFM / Ops Control | 7 | Operational validator; ops control is the airline's real-time nerve centre |

Complaints/claims-titled seats came back near-zero at airlines (unlike insurers, airlines fold claims into customer relations/CX). The Cust Operations/CX seat carries the complaints wedge here.

## Exclusions and gates

- No current-customer exclusions applied yet: **Jack's DNC list is the hard gate and has not landed.** Two of the largest UK insurers and the largest UK utility being customers says nothing about airlines, but Jack has touched nearly every account they target; assume nothing.
- Sourcing was zero-credit Clay native search. Nothing enriched, nothing billed, no emails pulled. Email waterfall + ZeroBounce run per wave, post-DNC, as a separate credit decision.
- Entity hygiene per the TELUS rule: 2 contact-level mismatches dropped at source (Hastings Direct, RAuxAF); 1 EA and 1 maintenance manager dropped at committee cut; Jet2 carries two "Louise Smith" profiles with different titles — verify which is current before any load.
