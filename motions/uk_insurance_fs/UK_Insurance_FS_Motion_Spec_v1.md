# UK Insurance + Financial Services Motion, spec v1

Built Jul 31 2026 for the Monday Aug 3 session with Jack Ohagan and Matt Rumins. Grounded in the Dallas/Jack strategy call transcript and the Jul 21 GTM launch update, not in hypothesis. Companion memory: `jack-uk-motion-strategy-call.md`.

## Why this lane

Jack's own ranking, verbatim: insurance and financial services have "the strongest proof points." Two of the largest UK insurers are customers. Financial services is the enterprise-scale prize and is tricky, which is exactly what a systematic motion is for.

Deliberately not water, despite the Jul 15 straw-man ranking Ofwat C-MeX first. Jack: water runs five-year budget cycles, so a deal outside the current cycle waits five years. The signal was right, the buying reality kills it.

Airlines is specced as lane two below. Untouched, seasonally urgent right now, and Matt's own push.

## The forcing function

Every complaint that reaches the Financial Ombudsman costs the firm **£680 per case in 2026/27**, win or lose, after a £2,000 annual case-fee allowance. Cases referred by professional representatives and decided for the firm drop to £500. Complaint volumes are published by named firm on a recurring cycle.

Source: [FOS case fees](https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/case-fees), [FOS 2026/2 Fees Manual](https://api-handbook.fca.org.uk/files/instrument/GLOSSARY-FEES-DISP/FOS%202026/2-2026-03-26.pdf). Third-party regulatory data, not an Intradiem claim, so it clears the verified-claims gate when cited as external.

The wedge: it's a public number with a price tag attached, which is the same structural shape as the Stars cliff edge, and it lands on service and back-office operations, which is the surface Intradiem touches.

Positioning constraint from Matt Graves (Jul 21): financial services SLAs are mostly self-imposed, so do not pull the SLA lever the way healthcare does. Lead with action and instance volume, what actually got done and how much capacity came back, not SLA language. This goes into the MessageGen prompt for this motion.

## Universe

Geography: UK and Ireland primary, Netherlands as the second geography once UKI is running. Germany is excluded (workers' rights make the technology effectively unusable). Nordics are cold (four-day weeks, agents not burnt out). South Africa is a ~6-month-out play.

Segments:
1. UK general insurers and life/pensions providers with published complaint volumes.
2. UK retail and commercial banks, building societies, and consumer credit firms with published complaint volumes.
3. Irish equivalents of both.

Grading inputs, all public:
- Published complaint volume, absolute and per 1,000 accounts or policies.
- Uphold rate, the share decided against the firm.
- Trajectory across the last two publication cycles. Rising is the trigger; a firm whose number is already falling has a story and doesn't need us.
- Agent population proxy, since Jack's own evidence is that larger agent populations see more value.

Addressability cut, same honesty test as Stars: only target firms whose complaint drivers plausibly move with workforce orchestration (handling delays, backlog, capacity, coaching gaps, adherence). A firm whose complaints are driven by pricing or product design is not addressable and gets dropped, no matter how bad the number looks.

## Buying committee

Five seats, Director and above, per the back-office qualification gate:

| Seat | Why they care |
|---|---|
| Head of Complaints / Customer Relations | Owns the published number and the per-case fee directly. Sharpest entry point for this wedge. |
| Director of Customer Operations / Service | Owns the queue and the agent population. |
| Head of Claims Operations or Claims Transformation | The back-office surface, and the bridge to the Back Office Optimizer at GA. |
| Head of Resource Planning / WFM | Operational validator, kills or blesses the technical story. |
| COO or Operations Director | Economic buyer, the seat that shortens the 18-month cycle if engaged early. |

## The 10-day sprint

Channel order is LinkedIn and WhatsApp first, phone worked in, email tactful and bucketed by account. Never blasted. UK and EU solicitation rules make spray-and-pray a legal exposure, not just a deliverability question, and opt-out language is required on email. This is the cadence Dallas and Jack agreed on the call.

| Day | Touch | Notes |
|---|---|---|
| 1 | Email, then LinkedIn profile view, then connection request | All three the same day. The profile view is what makes the connect land. |
| 2 | Call, leave a voicemail | Voicemail references the email's subject line and names Jack at the END, never the opening. "Add value, get out." |
| 3 | LinkedIn message | "Shot you a note via email, thought LinkedIn might be quicker," short version of the email, soft CTA. |
| 5 | Email 2, reply into the day-1 thread | Different angle on the same single idea, not a nudge. |
| 7 | Call 2 + WhatsApp where the number is mobile and appropriate | WhatsApp is Jack's market, not a US habit. |
| 10 | Breakup email | More direct, bigger problem framing, clean exit that leaves the door open. |

Every sequence ends in a reply, a meeting, or a clean answer. Two accounts in flight at a time.

## Draft copy, day 1 email

Persona: Head of Complaints / Customer Relations. Voice pass pending against Jack's booked-meeting messages.

Subject: your ombudsman numbers

> Hi {{first}},
>
> Every case that reaches the ombudsman now costs {{company}} £680 whether it's upheld or not, and the volumes get published with your name on them twice a year.
>
> Most of the complaint drivers we see aren't decision quality, they're timing. Work sitting in a queue longer than it should, capacity not where the volume is, coaching that arrives after the complaint rather than before it.
>
> Thought it might be worth comparing notes on what's actually driving your volume. Have 15 minutes next week?
>
> Jack

Claims discipline: the £680 is cited as the ombudsman's published fee, not an Intradiem stat. No Intradiem figures appear. Humana is available as approved 1:many proof if a proof line is needed, but it's a US health insurer, so it earns its place only where the analogy is genuinely close.

## Netherlands variant, when that geography opens

Written separately, never localised from the UK copy. Jack's rule from booking meetings there: lead with the ask. "The reason I'm contacting you is to find out whether this is relevant, and if it is, to set up a conversation." No pitch, no warm-up, no "hope you're well." Job titles, seniority and budget ownership all differ, and a manager may hold the entire budget with no external signal, which is where Clay earns its keep.

## Lane two, airlines

Specced, not built. Jack: "completely untouched... now is the time where you should be going after airlines. They're going to be feeling it a lot more. It's summer, it's busy." Matt wants airlines and retail pushed. Forcing function is different: UK261 compensation exposure and published punctuality and complaint data rather than ombudsman case fees. Same committee shape, same 10-day sprint. Build after UKI insurance and financial services is running.

## Gates

1. **Do-not-contact, hard blocker.** Jack owes the full customer account list with per-account context. Two of the largest UK insurers and the largest UK utility are customers. Nothing loads to Lemlist until that list is in hand and the exclusion check runs on real rows, including legal-name variants and UK subsidiaries. Synthetic validation does not count here.
2. **Verified claims.** No Intradiem number enters copy unless the Value Repository carries it. Jack's "two of the largest UK insurers" cannot be named or alluded to until contracts and marketing clear it. Getting that clearance is the highest-leverage ask for the Monday session.
3. **Consent and opt-out.** Email carries opt-out language. No blasting.
4. **Campaign built paused.** Only Dallas starts it. LinkedIn steps stay manual-approve.

## Open items

- Jack's `UK-Email&Linkedin-Bookings.xlsx` (posted to the group DM Jul 21) plus any message that produced a booked meeting. This drives the voice pass on all copy above.
- Jack's do-not-contact zip.
- Clearance question on naming the two UK insurers.
- Map the resulting Lemlist campaign IDs to `jack` in `automation/config/lemlist_channels.json` so `#gtm-outbound-jack` stops being silent.
