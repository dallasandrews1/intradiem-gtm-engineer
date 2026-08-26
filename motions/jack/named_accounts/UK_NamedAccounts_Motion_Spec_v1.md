# UK Named Accounts / Prospect Clinic, motion spec v1 (Aug 6 2026)

> **Aug 10 2026 addendum, give-first rework (v1.1).** Jack's feedback: lead with value and deliverables before any time ask. Four per-account give notes now exist as notes 8 to 11 in `motions/shared/Offer_Notes_Aug3.md` (superseding notes 4 and 5 as the send for this lane). Per-lead variables rewritten give-first for the 9 cold wave-1 contacts in `UK_NamedAccounts_Roster_v1.1.csv` (v1 preserved; Rankin and McCarville deliberately unchanged as warm re-entries): the LinkedIn DM now delivers the note's core point and offers the full note, the voice note asks one sharp question plus the note offer, and the first meeting ask moves to E2. Three shared-spine template edits are STAGED, not applied (session permissions blocked lemlist writes): both E2 bodies and the accepted-branch call-2 script still carry the old hard ask, so do not load leads before those edits land. Full set, per-contact verdicts and the staged edits: `UK_NamedAccounts_GiveFirst_Rework_Aug10.md`. Adversarial gtm-copy-reviewer pass still owed on all v1.1 copy.

Built from Jack Ohagan's `Combined_OnePagers.docx` (sent in Slack DM 10:40 CDT Aug 6, prepared for the UK QBR) plus the Aug 6 sync transcript. Sits alongside the Jack UK Engine (`motions/jack/Jack_UK_Engine_Aug3.md`) as a **named-account lane**, not a sixth vertical.

## Why this lane exists

On the Aug 6 call Jack asked directly: "Does it have to be vertical, or can it just be like six top priority accounts?" Answer on the call was yes. He also named the real constraint, and it is not prospecting:

> "Prospecting isn't necessarily the problem. We know everyone we need. There's no new names. I have all of the names already. It's just them not engaging. These are the people that do not pick up their phones, non-responsive over LinkedIn and email."

So this lane is not a sourcing motion. Every contact came from Jack. The whole job is **re-entry into accounts that have already been touched and have already gone quiet**, which makes the sequencing rules and the hold list the actual product here, not the copy.

The one-pagers are unusually good input: for each account they carry a dated live signal, an honest diagnosis of what failed, a named contact list with the failure mode per contact, and kill criteria. That is close to a full motion brief already. This spec turns it into something loadable.

## The four accounts

| Account | Live signal | Deadline shape | Wave 1 contacts |
|---|---|---|---|
| VodafoneThree | 100% buyout completed 3 Aug 2026; investor briefing 8 Oct | Land before 8 Oct | Bonnar, Bourke, Dalton, then Rubertazzi |
| Sky | NBCUniversal spin plus ITV broadcast acquisition, both multi-year | Rankin's own Aug/Sep window | Mottram, Rankin |
| British Airways | "Nimbus" migration live; CCMA conference 29 Sept | 29 Sept, and the shortlist check before it | Tan only |
| Ageas (incl. esure) | esure integration live; MacEwan combined role Jan 2026; Saga book incoming | None fixed, integration is running now | Hudson, McCarville, Hicks, Chapman |

27 contacts total in the roster. **11 go into the sequence. 16 do not.** That split is the point.

## The sequencing, per Jack's own rules

Every ordering decision below is lifted from Jack's "How We Get There" sections, not invented:

- **VodafoneThree:** Bonnar and Bourke first (freshest, most literal fit, one touch each so far), Dalton in parallel. Shaw held. No more all-contacts-at-once, which is the diagnosed failure on this account.
- **Sky:** open with Mottram, not Rankin, because she owns the function directly and does not need Graham's introduction that no longer exists. Rankin runs as a warm re-entry on the window he set himself. Smith and Canellas only after operational engagement is real.
- **British Airways:** Bradley Tan is the only contact in the sequence. The account's diagnosis is broken channel trust, not bad targeting. Everyone else is on a manual, channel-specific track.
- **Ageas:** Hudson first (no history to walk back, owns the technology landing), McCarville second (his own trigger, quoted back), Hicks and Chapman fresh on the legacy side. MacEwan held until the reframe exists.

### Judgement calls I made, flag any you disagree with

1. **Rubertazzi placed in wave 1B, staggered 3 business days behind Bonnar and Bourke.** Jack's doc calls him "primary target for the buyout angle" but the sequencing line only names Bonnar, Bourke and Dalton first. Staggering honours both: he gets the new angle without recreating the shotgun. **Jack's call to confirm.**
2. **The £700m synergy figure, the £1.6bn ITV figure, the £17m Newcastle figure and the CEO's on-record staffing quote are all kept OUT of the outreach copy.** They are ammunition for the room and for the internal case, not for a cold email. Leading a Chief Transformation Officer with a public redundancy quote reads as a threat, and it directly contradicts the protect-the-team reframe the same document argues for on the Ageas account. Signals are referenced by event, not by number.
3. **John Rankin's private "single point of failure" phrasing is used only with Rankin.** Reusing his own words with Mottram would leak a confidence he gave in a discovery call. His copy references it, hers does not.
4. **Michele Douglas is off the sequence entirely.** Her silence predates both announcements and has an unresolved cause. Automating a touch to her repeats exactly what already failed. One manual, low-pressure question instead.
5. **Simon White is held rather than sequenced** despite being called the strongest single use-case fit, because he needs an ROI-led message and the operational spine would waste him. Run `intradiem-roi-business-case` before touching him.

## The sequence spine

**Built and live in lemlist as a draft: `cam_GK8kMPNrjyHc5N3g6`, "UK - Named Accounts / Prospect Clinic (Jack)", Europe/London, 15 steps across 3 sequences. Zero leads. Readiness check returns one error only, "no senders configured", which is correct: Jack's mailbox is not connected yet.**

| Sequence | ID | Role |
|---|---|---|
| Main | `seq_c9YYXwfjEkGE7SWkW` | Steps 1 to 5, up to the branch |
| Accepted | `seq_LviKNjymLcxiLaCbH` | Connection accepted within 3 days |
| Not accepted | `seq_yg5EWJZmphviijMMr` | Fallback |

Account-agnostic scaffolding, everything specific carried in per-lead variables. That is the only way one campaign serves telco, media, airline and insurance without going generic, which is the exact failure the VodafoneThree page diagnoses ("a generic, non-specific pitch went word-for-word to 3 different roles").

Per-lead variables: `subject_1`, `opener_line`, `signal_line`, `pattern_line`, `offer_object`, `vm_hook`, `li_dm`, `voice_script`, `e2_subject`, `e2_line`. All ten are written per contact for all 11 wave-1 leads in `UK_NamedAccounts_Roster_v1.csv`.

**Main sequence**
1. Email 1, day 0. Subject `{{subject_1}}`. Offer CTA, no meeting ask (UK doctrine, mandatory). Opt-out line.
2. LinkedIn profile visit, day 0.
3. LinkedIn connect, day 0, manual, no note.
4. Call, day 1. Voicemail from `{{vm_hook}}` if no answer, name at the end.
5. Branch on connection accepted within 3 days.

**Accepted branch**
6. LinkedIn DM, manual, `{{li_dm}}`. This is where the meeting ask starts, per doctrine.
7. LinkedIn voice note, day 1, `{{voice_script}}`. Manual until Jack's voice clone is recorded, then AI.
8. Call 2, day 2, no voicemail.
9. Email 2, day 2. `{{e2_subject}}` / `{{e2_line}}`.
10. Email 3, day 3. "closing the file", shared body, works across all four accounts.

**Not-accepted branch**
6. Like last post, follow, day 0.
7. Call 2, day 2, no voicemail.
8. Email 2, day 2.
9. Email 3, day 3.

No WhatsApp leg on this lane. With 11 contacts and this much account history, channel volume is not the missing ingredient.

**Closing email body (shared, no variable):**

> Hi {{firstName}}, I'll close the file here. One thought worth keeping: in the middle of a change this size, the operations that come out ahead are usually the ones that could see what their people were absorbing while it was happening, rather than in the report afterwards. That's the seam I work. Glad to help whenever the timing fits.
>
> Either way, this is my last note.
>
> Jack Ohagan

## Hold register, with release conditions

Nothing here is parked and forgotten. Each has a trigger.

| Contact | Account | Release condition |
|---|---|---|
| Jon Shaw | VodafoneThree | First response from Bonnar, Bourke or Dalton, OR week of 1 Oct, whichever comes first |
| Michele Douglas | Sky | Manual diagnostic question sent and answered |
| Andrew Smith | Sky | Real operational engagement with Mottram or Rankin |
| Laura Canellas | Sky | Same as Smith |
| New Head of Planning | Sky | The seat gets filled. Watch item |
| Tim Monk | BA | 3 to 4 weeks of genuine comment engagement, then CCMA 29 Sept |
| Pat Davis, Restucci, O'Sullivan | BA | Personal video recorded, with transparency opener |
| Adam Greghni | BA | Background verified |
| Simon White | BA | ROI-led message written |
| Hannah Fuller | BA | Data-led message written |
| Alan MacEwan | Ageas | Protect-the-lean-team reframe written and critic-gated |
| Caroline King | Ageas | King / MacEwan structural relationship clarified |
| Tracy Sheldon | Ageas | Champion approach written. Never a target |
| Ian Clarkson | Ageas | Background verified |

## Standing account rules, inherited from Jack's doc

- **British Airways: never cold-call a personal mobile without the transparency opener.** Name the tool and the company in the first two sentences. This is a standing rule on this account, not a one-off fix, after two immediate hang-ups asking how we got the number.
- **VodafoneThree: no generic pitch, ever again, on any contact.** Every touch has to match the bar set by the best messages already sent to Bourke, Bonnar and Dalton.
- **Ageas: no second efficiency pitch to MacEwan or Sheldon.** The reframe is protecting and optimising the lean team they already built, never further headcount reduction.

## Kill criteria, carried straight through from the one-pagers

- **VodafoneThree:** all four silent by next pipeline review, deprioritise. Bounded bet.
- **Sky:** still unreachable when the ITV deal formally enters regulatory review, deprioritise until there is organisational clarity.
- **British Airways:** if the CCMA-anchored approach also produces nothing, the blocker is deeper than channel trust and the account needs a full strategy reset, not another tactic.
- **Ageas:** if tailored approaches to McCarville, Hicks, Chapman and Sheldon all go quiet, long-term nurture rather than near-term close.

These go in the ledger, not just this doc. A kill criterion nobody checks is a comfort blanket.

## Gates before any load, in order

1. **Current-customer exclusion.** Checked against the Aug 3 UK customer list (7 accounts: Amex GBT, AXA UK, British Gas, Capita, Centrica, Virgin Media O2, VitalityHealth). None of the four named accounts appear. **Clean, but re-confirm with Jack** since Virgin Media O2 being a customer while VodafoneThree is a target is exactly the kind of adjacency worth a second pair of eyes.
2. **Signal freshness.** Every one of Jack's four pages is headed "SIGNAL, CHECK STILL LIVE" in his own words. The copy is signal-led, so a stale signal is a credibility problem, not a cosmetic one. Jack confirms all four before load.
3. **Contact data.** Blocking. See below.
4. **Copy critic pass.** Run `gtm-copy-reviewer` over all 11 contacts' variables before load. Self-checked already for the verified-claims gate (zero Intradiem statistics anywhere in the copy) and house style (zero em dashes). The adversarial pass has not run yet.
5. **Cross-campaign dedup.** British Airways now appears in two campaigns: the airlines committee list holds BA operations contacts (Mark Shaw, Viktorija Diestelkamp, René de Groot), this lane holds BA customer-care contacts. Different people, same account. **If both ever run live at once, that is a same-account double-touch.** Airlines is staged for late August; sequence this lane first and hold the BA rows in the airlines campaign, or accept it deliberately.
6. **Settings pass.** Europe/London, weekday business hours, click tracking off, reply-stops on.
7. **Dry-run default.** Nothing starts without Dallas's explicit word.

## Contact data, enriched Aug 6

Closed via Clay. **141 credits**, 72,597.3 to 72,456.3, full breakdown in `Clay_Credit_Ledger.md`.

| | Wave 1 / 1B (11) | All contacts (26) |
|---|---|---|
| Work email | 11 | 25 |
| LinkedIn URL | 10 | 23 |
| Mobile phone | 8 | 8 (wave 1 only, tiered) |
| Title verified | 11 | 22 |

**10 of 11 wave-1 contacts are fully loadable.** Bradley Tan is the exception.

lemlist could not do the phone enrichment: `bulk_enrich_data` returned MISSING_FUNDS on all 26 items with zero credits consumed, because the team is on `lemlist1-freetrial-monthly-usd` and the trial carries no enrichment balance. Clay's "Enrich Person and Find Contact Details" covered it instead, returning mobile phone and corroborating the email off a LinkedIn URL. Worth carrying into the seat case: on the trial, lemlist cannot enrich at all.

### What the enrichment changed

1. **Domains were wrong in v1.** VodafoneThree is `vodafonethree.com`, not `vodafone.co.uk`. McCarville sits on `esure.com`. Three credits of domain resolution prevented a batch of wrong-domain guesses. VodafoneThree emails are still fragmented across three legacy domains, which is what a fresh merger looks like.
2. **Jack's research verified.** McCarville's 15 years, Hicks's 10 years, MacEwan's Jan 2026 role, Rubertazzi's 15-month role and Clarkson's 5 months all confirmed to the month.
3. **Bonnar: Jack was right, Clay's cheap index was stale.** The search index showed an old title. The full profile shows he moved to Scheduling & Real Time Planning Manager on 2026-06-01. Standing lesson: never overrule a rep's first-hand read on the cheap index alone.
4. **Bonnar's copy is rewritten and is now the strongest email in the wave.** His own summary states he runs demand and supply across on and offshore contact centres and that this "currently also includes co-existence as we migrate all our customers onto a new platform." A live migration with a co-existence window, in his own words. Subject is now "co-existence"; the synergy-target angle is gone. Same seam as the BA Nimbus angle.
5. **Chapman's opener sharpened** off his summary claiming 20+ years in WFM, stronger than the tooling-change assumption.

### Residual gaps, all needing Jack

- **Bradley Tan, no LinkedIn URL.** The only BA contact in the sequence. Absent from Clay's index under ba.com and from a name-only UK search. Davis, White, O'Sullivan and Fuller are also absent; BA is the thinnest account in Clay's people data at 3 of 8. Jack sourced them, so Jack is the route.
- **Richard Bourke, `richard@vodafone.com`.** First-name-only on a legacy domain. Two Clay paths agree, which may mean one shared upstream source. Verify before send.
- **Liz Hicks** is Elizabeth on LinkedIn; the email is a guess on the short form.
- **Dave Hudson's number** is an 01793 Swindon landline, not a personal mobile.
- **Finola O'Sullivan**: nothing found on any field.

## Calendar, working backwards

| Date | What has to be true |
|---|---|
| **Thu 13 Aug** | lemlist trial cutoff. Everything that needs the trial has to be proven before this |
| **~Mon 1 Sept** | Wave 1 running so VodafoneThree lands well before the briefing |
| **Tue 29 Sept** | CCMA UK National Contact Centre Conference, QEII Centre. Monk encounter. Shortlist check needed weeks earlier |
| **Wed 1 Oct** | Jon Shaw release date if no earlier signal |
| **Wed 8 Oct** | VodafoneThree investor briefing. After this, Shaw is fielding a hundred vendor pitches |

The 13 Aug trial cutoff is the near-term forcing function and it is 5 business days out.

## What is not built yet, ranked

1. **Manual track assets:** the video scripts for Davis, Restucci and O'Sullivan; the ROI-led message for Simon White; the data-led message for Hannah Fuller; the MacEwan reframe; the Sheldon champion approach; the Michele Douglas diagnostic question. Seven pieces, all short, none of them blocked.
2. **The CCMA shortlist check** for BA/Newcastle. A web check, cheap, and it changes whether 29 Sept is a scheduled encounter or a hopeful one.
3. **Jack's LinkedIn content cadence.** Raised on the call: his engagement dropped off and he is posting twice a week. Separate build, and it is the prerequisite for the Monk track, which needs him visible in contact centre comment sections for 3 to 4 weeks before the conference.
4. **The opportunity-channel automation** Jack asked about on the call (Salesforce meeting created, Slack channel auto-created per opportunity account). Real build, own scope, needs the AE routing layer that is already a build item on the UK engine.
