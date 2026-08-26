# Jack UK Engine, v1 (Aug 3 2026)

The end-to-end plan to make the GTM engine the number one source of Jack Ohagan's meetings, built from the Aug 3 Matt & Jack sync (Matt Rumins joined mid-call; Simon Bland joins next week's). Companion to the Keegan Attainment Engine on the US side. Jack's quarterly target is **10 meetings, quality over quantity**; his stated ambition on the Jul 31 strategy call was to **double output** once the motion is automated. The engine's number: make 20 a quarter normal, and traceable.

## Ground truth from the Aug 3 call

- **Jack is already producing:** 2 meetings booked last week off his own BPO campaigns, before the engine has sent a single email. That validates the BPO lane he was told wouldn't work, again.
- **Territory friction is the tax on success:** those BPO meetings ran off EMEA signals into globally-spread orgs, and one landed on a US-owned target whose AE (based in India) pushed back, despite zero prior activity in the account. Nate's fine; the AE isn't. Matt's stance: "we should all be trying to grow together, a meeting is a meeting." Dallas's read: EMEA and US sides of a big account operate separately and should be worked separately; if a booked meeting can't be covered, Simon takes it. Jack had a follow-up call with the AE same day.
- **The Barclays problem, named by Jack:** 90% of the account's activity is UK, the best contact sits in the US, and the US has an opportunity on it after heavy UK groundwork. His direct ask: can Clay encode logic for which AE a signal-sourced meeting belongs to? Answer on the call: yes, and the Keegan TAM CSV request already started the compartmentalize-by-AE work on the US side. This becomes a build item (below).
- **Messaging verdict (the "brutal truth"):** a meeting ask in the first touch won't work in this market. First touch offers something instead ("is it worth me sending over how other airlines are approaching this"). Applied same day, see `motions/shared/First_Touch_CTA_Doctrine_Aug3.md`. The opt-out line stays; Jack accepted the deliverability and solicitation-law rationale.
- **Matt's read:** loves the sequencing and the fail-fast structure ("this is the dream, thousands of people rather than tens"), wants the Dallas-skills-plus-Jack-market-knowledge balance made explicit, flagged send timing across timezones as a real detail, and challenged test validity on airlines: not a big European vertical, maybe ~40 reachable people, "it was okay, didn't tell us much" is the outcome he wants to avoid. He approved airlines AND insurance (insurance must not collide with Jack's existing insurance work).
- **Volume answer given:** the 10-day blitz is the test unit because insight goes stale in weeks, not months; a 10-day multi-channel run forces a yes or a buzz-off, and either is data. Volume is a campaign-structure choice; the ceilings are deliverability and Jack's mailbox allowance, not the tooling.
- **Lemlist money:** Matt spoke to Naveen the same day and is "putting things in place" to secure it; Jack is also pushing. Three seats planned: Dallas, Jack, Nate. Jack explicitly wants his own license to build campaigns himself, starting with **pre- and post-event follow-ups**, a lane the engine hadn't listed.
- **Friday Aug 7: AI champions kickoff.** Naveen asked Jack to write up what the AI motion means for the UK and his role. That writeup doubles as internal advocacy for the Lemlist spend.
- **Working rhythm agreed:** Dallas joins the existing Matt/Jack weekly sync (path of least resistance, no new meeting), Simon in from next week; Dallas and Jack set a separate working cadence this week; Matt gets added to the GTM Outbound Jack Slack channel where the agents post blitz activity, replies, and suggested responses hourly.
- **Per-lead personalization, Jack asked directly:** confirmed. Personalization variables are per lead ({{opener_line}}, {{contract_line}}, {{vm_hook}}, {{voice_script}}), generated per contact Claude-side, critic-gated, loaded as lead custom variables; the template holds only the shared spine. Load-time verification contract lives in the doctrine doc.

## The five lanes

### Lane 1: Insurance / FS (first out, the fair test)
Seasonless, biggest addressable universe, strongest proof points, and it answers Matt's volume concern in a way airlines can't. Campaign `cam_nwKASgttBM6QT8XGq` built, E1 now offer-CTA. Jack's UKTA priority overlays it (Admiral, Ageas, Saga, LV=, L&G, D&G, Esure, Lloyds with the changed angle). Gates before load: exclusion list confirmed complete by Jack, committee re-pulls where domains failed, per-wave enrichment.

### Lane 2: Airlines (staged, late-August start)
Campaign `cam_fHGtNHbbj7LmThFgX` built, E1 now offer-CTA. Small universe (76 committee contacts, 41 wave-1) means it's a learning lane, not the readout lane; Matt is right that it can't carry the verdict on the motion. Start stays staged no earlier than late August so the back half lands post-peak.

### Lane 3: BPOs (Jack's proven lane, now with rules)
Two meetings last week prove it. Before it scales through the engine, it needs the territory rules from the friction case: an EMEA-signal meeting on a globally-spread org routes to the AE the routing layer names, and if it books into a US timezone, Simon or the named US AE takes it, decided at booking time, not after. This lane feeds the AE-routing build below.

### Lane 4: Events (new, Jack's own ask)
Pre- and post-event follow-up sequences Jack runs himself once seated. Not built yet; goes on the ranked sheet like everything else. It's also the strongest argument for his own license, so it leads the Lemlist-case writeup.

### Lane 5: Netherlands (queued behind Rabo)
Separately written blunt copy per Jack's standing rule, never localized. Rabo on the UKTA list pulls it forward in the ranking conversation.

## Build item: AE routing layer (the Barclays fix)

What Jack asked for, generalized: every account in a universe carries **owning AE, geography split, and signal-origin attribution**, so a meeting is routed the moment it books, not litigated after. Shape: a routing column set in the Clay workbooks (account → EMEA owner / US owner / escalation rule) plus a line in every booked-meeting log naming which signal sourced it. The Keegan TAM CSV (owed by Nate) is the US half of the same map. Check existing Clay workflows before building anything new, per standing rule. Until it exists, the manual rule stands: EMEA signals worked by Jack, US-owned accounts flagged to Matt before outreach, Simon as the timezone backstop.

## The ranked sheet (the process Matt bought)

Agreed on the call, top-down: Jack brain-dumps **every** campaign idea onto one sheet, the sheet gets ranked by likelihood of producing pipeline now, and the engine attacks one at a time, one complete thought and campaign per cycle, days not weeks. The five lanes above seed the sheet; Jack's working session this week fills it out and ranks it. No motion starts until it has a rank.

## Gates, standing, never skipped

1. **Exclusion list** confirmed complete by Jack before any load (7-account UK customer list landed Aug 3; AXA's 8 contacts already excluded). Hard gate.
2. **Verified claims** on every number; the offer notes carry zero stats by design.
3. **Dry-run default**; no Start without Dallas's explicit ask; Jack's channels (mailbox, LinkedIn, WhatsApp) and paid seat before any send.
4. **Send-window pass per campaign** (Matt's timezone point): Europe/London weekday business-hours schedule, clicks off, reply-stops, checked in the settings pass before Start.
5. **Per-lead variable check at load:** preview one real lead per email step; an unmapped variable is only catchable there.

## This week, in order (traps called out)

1. **Done today:** first-touch CTA fix on both campaigns, offer notes written, doctrine doc saved, Nate A/B mounted. Nothing for Jack to redo.
2. **Dallas + Jack working session (set the cadence today):** brain-dump and rank the sheet; voice pass against `UK-Email&Linkedin-Bookings.xlsx` (still open from the premortem); record Jack's voice for the AI voice notes. Trap: don't generate more per-lead copy for new lanes until the voice pass lands, or it all gets regenerated.
3. **Jack's AI-champions writeup for Friday:** offer the draft; frame events + his own campaigns as the license case. Trap: keep it head-start framing, the motion is a build in progress, not a finished machine.
4. **Add Matt to the Slack channel** when Slack allows; Simon onto next week's sync invite.
5. **Hold on loads:** exclusion confirmation from Jack, then insurance wave 1 enrichment, then the settings pass, then Start on Dallas's word. Airlines holds until late August regardless.
6. **Background:** spec the AE routing layer against existing Clay workflows; pair it with Nate's Keegan TAM CSV when that lands so both sides of the map ship together.

## How we'll know it's working

- Every booked meeting lands in `Jack_Meeting_Ledger.md` with lane, signal source, and routed AE attached; engine-sourced vs Jack-manual never blended.
- The offer CTA gets judged on reply-and-note-request rate against the old ask (the two booked BPO meetings are the pre-engine baseline).
- Quarter read: 10 is the floor, the engine's job is to make the second 10 cheap.
