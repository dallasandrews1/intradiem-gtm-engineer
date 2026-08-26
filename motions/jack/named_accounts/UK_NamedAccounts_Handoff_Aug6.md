# Named Accounts handoff, Aug 6 2026

Everything built today, what needs your hands, and the message to Jack. Nothing has been sent. Nothing can send: `cam_GK8kMPNrjyHc5N3g6` is draft, zero leads, no sender attached.

## What exists now

| Asset | Where |
|---|---|
| Motion spec, sequencing, hold register, gates, calendar | `UK_NamedAccounts_Motion_Spec_v1.md` |
| 27-contact roster with per-contact copy for the 11 wave-1 leads | `UK_NamedAccounts_Roster_v1.csv` |
| Offer notes 4 and 5 (integration-era ops, migration co-existence) | `motions/shared/Offer_Notes_Aug3.md` |
| lemlist campaign, 15 steps, 3 sequences, draft | `cam_GK8kMPNrjyHc5N3g6` |

## Order of operations, do not skip ahead

The trap here is loading before the signals are confirmed. Every first email leads with a dated event from Jack's own research, and every one of his four pages is headed "SIGNAL, CHECK STILL LIVE" in his own words. A stale signal in touch one on an account that already ignored six good messages is worse than not sending.

1. **You, now: send Jack the message below.** It carries the three asks that unblock everything: contact data, signal confirmation, and the Rubertazzi call.
2. **Jack: confirms the four signals are still live.** Blocking.
3. **Jack: exports contacts with emails and LinkedIn URLs.** Blocking. He said on the call he has all the names. If they carry emails, this costs nothing. Only enrich the residual, and only on your explicit go.
4. **Jack: connects his mailbox and LinkedIn in lemlist, and records his voice.** This is the only readiness error on the campaign right now. It was already his to-do from the call.
5. **You: run `gtm-copy-reviewer` over the 11 contacts' copy.** Self-gated already for verified claims and house style; the adversarial pass has not run.
6. **You: load wave 1, preview one real lead per email step.** An unmapped variable renders as a literal `{{opener_line}}` and the preview is the only place that gets caught.
7. **You: settings pass.** Europe/London, weekday business hours, clicks off, reply-stops on.
8. **You: Start, on your word only.**

Steps 5 through 8 all wait on 2, 3 and 4. Until Jack comes back, there is nothing to do here that is not a regression.

## Message to Jack, drafted and held

Not sent. Your call whether it goes as-is.

> Jack, went through the one-pagers properly. They're the best account input I've been given here, honestly. The failure diagnosis per contact is the part most people skip.
>
> I've built the sequence off them rather than off a vertical, like we said on the call. Four accounts, 27 contacts. 11 go in, 16 don't, and the 16 is the bit I'd want you to check. Bradley Tan is the only BA contact in it, because your own read is that the blocker there is channel trust, not targeting, so Monk goes through CCMA and the rest go to video and ROI-shaped touches instead. Shaw's held until one of Bonnar, Bourke or Dalton moves, or the week of 1 Oct, whichever lands first. MacEwan's held until the reframe's written. Michele's on her own track since her silence predates the M&A news.
>
> Every first email is a different message. Bonnar's is about a synergy target landing on a real time planning desk, Chapman's is about two sets of planning assumptions, McCarville's quotes his own trigger back at him and owns the follow-ups that missed it. First touch offers a note instead of asking for a meeting, per your feedback.
>
> Three things from you and it's ready:
>
> 1. Those four signals, are they all still live? Your pages all say check, so I'm checking. If Vodafone's synergy number has already been briefed out or the Sky timeline's moved, the copy changes.
> 2. Can you export those contacts with emails and LinkedIn URLs? You said you've got all the names. If they've got emails on them we skip enrichment entirely.
> 3. Rubertazzi. Your page names him as primary target for the buyout angle, but your sequencing line only puts Bonnar, Bourke and Dalton first. I've staggered him three days behind so he gets the new angle without recreating the all-at-once thing. Say the word if you want him in the first group.
>
> Also, mailbox, LinkedIn and the voice recording in lemlist when you get a minute. That's the only thing the campaign's actually flagging right now.

## Copy-paste prompts for me, once Jack replies

Paste whichever applies.

**Signals confirmed, contacts received:**

```
Jack confirmed the four signals are live and sent the contact file. Load wave 1 of the Named Accounts campaign cam_GK8kMPNrjyHc5N3g6: map the roster variables, preview one real lead per email step, run the settings pass. Do not start it.
```

**Signals changed:**

```
Jack came back on the Named Accounts signals: [paste what changed]. Rewrite the affected contacts' copy in UK_NamedAccounts_Roster_v1.csv and update the motion spec.
```

**Rubertazzi decision:**

```
Jack's call on Rubertazzi: [wave 1 / keep him staggered at 1B]. Update the roster and spec.
```

**Manual track assets, unblocked now, does not wait on Jack:**

```
Write the seven manual-track assets for the Named Accounts motion: video scripts for Pat Davis, Teresa Restucci and Finola O'Sullivan; the ROI-led message for Simon White; the data-led message for Hannah Fuller; the MacEwan protect-the-lean-team reframe; the Sheldon champion approach; and the Michele Douglas diagnostic question. Same gates.
```

**CCMA check, unblocked now:**

```
Check whether BA or the Newcastle contact centre is shortlisted for the CCMA UK National Contact Centre Conference on 29 Sept, and confirm the Intradiem membership and sponsorship position. It changes whether the Tim Monk track is a scheduled encounter or a hopeful one.
```
