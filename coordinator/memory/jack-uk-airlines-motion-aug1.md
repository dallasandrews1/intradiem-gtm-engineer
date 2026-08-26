---
name: jack-uk-airlines-motion-aug1
description: "Aug 1 build - Jack's lane two (UK/Ireland airlines) sourced and campaign built; universe 12 accounts / 76 committee contacts (41 wave-1 with critic-gated variables), lemlist \"UK - Airlines (Jack)\" = cam_fHGtNHbbj7LmThFgX in Draft, zero credits spent, launch gated on DNC + channels + Start"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9dbb9a5f-a026-4fa9-b6fa-fbf7823862ef
  modified: 2026-08-01T22:25:49.438Z
---

Aug 1 2026, built end to end at Dallas's direction (he pre-confirmed all lemlist step creation). Companion assets in `motions/uk_airlines/`: graded universe, committee CSV, wave-1 variable stage, workbook UI sheet.

**Forcing function (verified, the airlines analog of the £680 FOS fee):** UK261 fixed compensation £220/£350/£520 per passenger (£260 long-haul at 3-4h) once a controllable delay crosses 3 hours, claimable 6 years (CAA). Summer context from Eurocontrol wk30 2026: all-time record 37,659 flights Jul 24, 20% of all flights ATFM-held, 72% punctuality. Campaign numbers: E1 subject "the three hour mark", mid email "six years". [UNVERIFIED] and kept out: easyJet June-1 disruption counts (secondary sources only), ADR backlog sizes, the 8-to-6-week ADR change (that's Ofcom telecoms, not aviation).

**Universe:** 6 wave-1 airlines (easyJet incl. holidays arm, Jet2, Ryanair, Aer Lingus, Virgin Atlantic, British Airways) + wave-2 ground handlers (Swissport, dnata, Menzies) + Emerald, Loganair, Wizz Air UK. Cargo/wet-lease excluded. **TUI = 0 contacts, Clay's index would not resolve it on four identifiers; source via Sales Nav/Apollo later.** Committee 76 (Director+/head floor), 0 overlap with the FS committee, sourced via zero-credit Clay native search like the Jul 31 FS pull. Airlines have near-zero complaints-titled seats; the CX/customer-operations seat carries that wedge. Jet2 has two "Louise Smith" profiles, one flagged DUPLICATE-SUSPECT.

**Wave discipline applied:** variables (opener_line, contract_line, vm_hook, voice_script, prompt airlines-v1.0) generated Claude-side through first-draft-engine + copy-sharpener for the 41 wave-1 contacts ONLY, critic-gated by gtm-copy-reviewer, stored as columns in the committee CSV. Ground-handler copy must NOT reuse the airline spine (their exposure is SLA, not UK261). Workbook "Jack UK Airlines" is a UI-creation step (sheet written); no enrichment columns until post-DNC wave go (~1.5 credits/contact if run).

**Campaign cam_fHGtNHbbj7LmThFgX "UK - Airlines (Jack)":** exact clone of the insurance/FS shape ([[jack-uk-lemlist-campaign-aug1]]): Draft, Europe/London, no senders/leads, 22 steps. Main: E1 + visit + note-less manual invite + day-2 call/VM (subject-referencing, Jack named at END) + invite-accepted conditional (2d). Accepted: Jack's "thought LinkedIn might be quicker" DM, manual voice-note placeholder (swap to Jack's AI clone pre-launch), call 2, "six years", "closing the file". Fallback splits hasPhoneNumber: phone branch call / manual WhatsApp 1 / double-tap / "six years" / manual WhatsApp 2 / breakup; no-phone like+follow+visit / "six years" / breakup. Sign-off Jack d1-5, Jack Ohagan d6+, zero Intradiem stats. Mapped to the "jack" route in `automation/config/lemlist_channels.json` (canary mode untouched).

**Credits:** 0 spent (balance 72,822.1 unchanged); ledger row logged 2026-08-01.

**Premortem hardening (same evening):** strategic-premortem verdict was Moderate confidence for insurance landing meetings, Low for airlines "quickly," with three fixes applied immediately: (1) every email step in BOTH Jack campaigns now carries an opt-out line ("If you'd rather not hear from me, one word and I'll stop"; breakups carry "Either way, this is my last note"), closing the UK-solicitation gap both builds had; (2) airlines E1 and 9 money-first openers inverted to lead with the recovery-runs-a-shift-behind idea, fee bands demoted to second position (prompt v1.2), because UK261 fee-first copy pattern-matches to the AirHelp-style claims-vendor spam airline ops seats delete on sight; (3) airlines launch window staged to Start no earlier than late August so the sequence back half lands early-to-mid September post-peak; insurance goes first (seasonless). Standing premortem risks: the launch dependency chain (DNC + Jason's seat decision) is the real speed gate, and the Jack voice pass against UK-Email&Linkedin-Bookings.xlsx is still open, best done live with Jack in the Monday session.

**Open gates, all still closed:** (1) Jack's DNC list = hard gate, nothing loads; (2) Jack's paid seat + mailbox/LinkedIn/WhatsApp channels; (3) campaign settings pass (weekday schedule, clicks off, reply-stops) like the Stars campaigns; (4) email/phone enrichment per wave post-DNC; (5) Dallas's explicit Start. Related: [[jack-uk-motion-strategy-call]], [[lemlist-standard-sequence-jul31]], [[banned-phrases-comparing-notes-jul31]].
