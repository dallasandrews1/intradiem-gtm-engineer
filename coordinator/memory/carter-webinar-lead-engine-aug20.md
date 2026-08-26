---
name: carter-webinar-lead-engine-aug20
description: "Aug 20 2026 evening build for the Aug 21 Carter meeting: Clay workflow `Webinar Registrant Enrich + Route` PUBLISHED live on the Webinar Leads segment, all 1,016 registrants backfilled via a manual-trigger twin + bulk routine (170 credits), results stamped onto Audiences records (5 new fields), branded brief + CSV in motions/marketing"
metadata: 
  node_type: memory
  type: project
  originSessionId: 89c2a123-02d8-4510-98d1-b221ec71a34d
  modified: 2026-08-20T20:24:42.822Z
---

Dallas's call 2026-08-20 ~15:45 CT: "spend credits where needed, I do not want to show up tomorrow with half-baked plans." What shipped by ~16:30 CT:

- **Live workflow** `wf_0tk333zvDnGg4YcikFp` (published v1 20:10 UTC), trigger = audience_segment on `Webinar Leads (Lead Source contains Webinar)` `audseg_0tk335bt7YKafui6nbh` (1,016). 13 nodes: triage (personal/competitor/internal exit) → Enrich person (cpj-enrich-person, 0.5 cr only when a profile is found) → merge → fn_persona_key → rules fallback (catches "Sr Workforce Planner" = wfm) → upsert-audiences-record write-back → persona gate → bdr_review / nurture terminals. Fires automatically for every NEW entrant.
- **Backfill**: live audience triggers do not backfill existing members and `runs test --audience-segment --limit 10` re-runs the same first 10 each call, so a manual-trigger twin `wf_0tk344sg8uVq27RAKd3` + routine `workflow:wf_0tk344sg8uVq27RAKd3` + `clay routines runs start --bulk` (1,016 rows, `run_0tk349aSF8rzYcafve6`) did it in about a minute. **Credits: 3.0 (test batches) + 167.0 (bulk) = 170.0**, balance 71,037.3 → 70,867.3, ledger rows appended (est + actual).
- **Audiences fields (people)**: Clay Persona Key `audf_0tk33nse4Dbnq9ofgGM`, Clay Webinar Route `audf_0tk33nscwuvhobuKwH8`, Clay Enriched Title `audf_0tk33nsYJyeCWonp4FA`, Clay Company Domain `audf_0tk33ntxQy4KyigBAmi`, Clay Triage `audf_0tk33ntEfhyygaiHmYb`. 1,012 of 1,016 stamped.
- **Results**: route bdr_review 560 / nurture 315 / skipped 137 (90 personal, 34 competitor: Alvaria 10, Genesys 7, NICE 7, Verint 5, Aspect 3, Five9 2; 13 internal). Persona in BDR pool: wfm 431, cc_ops 116, bo_shared 10, bo_claims 2, cx 1. BDR pool by SF: Prospect 176, Not in SF sync 275, Customer (flag or alias) 94, Unclassified/Partner 15. Director+ in BDR pool 52 (7 at Prospects, 39 not-in-SF). Enrichment: 334 profiles found (38% of 875 reachable), 277 titles corrected, 104 domains corrected. Lead Status empty on 954/1,016.
- **Deliverables**: `motions/marketing/Webinar_Leads_Brief_Aug21.html` (Naveen design system, Google Fonts link) + artifact copy with inline Roboto; `motions/marketing/Webinar_Leads_Enriched_Routed_Aug20.csv` (1,016 rows, persona/route/triage/SF type/enriched title/domain); agenda `Carter_Clay_Strategy_Agenda_Aug21.md`.
- **Known loose ends**: 4a/4b route-packet nodes still pin persona_key to node 3 (stamps are correct, packets are cosmetic; `nodes update` returned no applied updates); the syf.com test trigger `064f4f4f...` was deleted from the draft but the live v1 still carries it until a republish; test segment `audseg_0tk33z1rkwiPju4BttM` archive call returned nulls, verify; the `WebHelp Registration` segment (2,831) is customer help-portal signups, not marketing.

**Why:** proof for Carter that the Clay layer is agent-built, live, cheap, and writes back into the shared data, not a slide.

**How to apply:** for any future "run it on everyone" ask on Audiences: build the live workflow on the segment trigger, then a manual-trigger twin + bulk routine for the backlog. Related: [[clay-audiences-live-cli-capability-aug20]], [[html-deliverable-standard]], [[feedback-deliverables-carry-the-why]].
