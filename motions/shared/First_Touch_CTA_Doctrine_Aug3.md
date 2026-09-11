> **Superseded Sep 3 2026 by `Messaging_Doctrine_Sep3.md`.** The offer-note ending survives there as one of two allowed Email 1 closes (the other is the benchmark question); the no-calendar rule survives; the market split, the per-lead variable contract and the state notes below remain accurate history.

# First-Touch CTA Doctrine (Aug 3 2026)

Source: Jack Ohagan's direct feedback on the Aug 3 Matt & Jack sync ("the CTA won't work. I don't think a meeting ask in the first touch") plus Dallas's decision to A/B the same idea on the US side. This doctrine binds every prompt that generates first-touch email copy from here forward: MessageGen prompts, first-draft-engine runs, motion-stamp assemblies, and any new campaign build.

## The rule

**UK / Europe (mandatory):** no meeting ask in the first email, ever. The first-touch CTA offers something instead, in the "is it worth me sending over ___?" shape, explicitly detached from a meeting ("No meeting attached, I'll just send it over."). Meeting asks begin at the day-3 LinkedIn DM (Jack's own design) and escalate in directness through day 10, unchanged.

**US (A/B, evidence pending):** variant A keeps the natural meeting ask ("Have 15 minutes...?"), variant B runs the offer CTA. Same subject line and body on both variants so the test isolates the CTA. Winner becomes doctrine per market once there's enough send volume for a directional read; with wave sizes this small the read is directional, not statistical, so judge on replies and reply quality, not opens.

**Netherlands (unchanged):** separate blunt copy per Jack's rule, lead with the ask for relevance, never localized from UK copy. This doctrine's offer-CTA shape still applies to the first email, but written natively.

## Why (so the prompt layer can reason with it)

- A first-touch meeting ask prices the email at 15 minutes of a stranger's calendar. An offer prices it at one reply word. UK buyers, per Jack, delete the former on sight.
- The offer is a qualification engine: a "yes, send it over" is a warmer signal than an open, and it earns the follow-up conversation the meeting ask was trying to skip to.
- The offer must be real. Every offer CTA has a matching note in `motions/shared/Offer_Notes_Aug3.md`, pattern-level, zero stats, zero customer names, sent as a plain reply within hours of a yes. Never ship an offer CTA without its note existing first. That is an ordering trap: CTA live before asset exists means a yes gets silence.

## What changed today (state)

- "UK - Airlines (Jack)" cam_fHGtNHbbj7LmThFgX E1 (stp_9oni2Xpgq6aXyMWXk): meeting ask replaced with the recovery-gap offer CTA.
- "UK - Insurance / FS (Jack)" cam_nwKASgttBM6QT8XGq E1 (stp_gvvaxLrpqJnEFHbx5): meeting ask replaced with the eight-week-line offer CTA.
- Nate Stars, all three campaigns, first email A/B enabled with variant B = offer CTA, variant A untouched: Quality stp_b9Ns4nuZJSpT8Xr6s (etp_LQ2Jet7D9TE3zMTCa), Finance stp_hmp9Gp7dAZFgkgqPq (etp_ymYvqArvhFEqa8kMT), Resurrection "just tried you" stp_afdYJbTbPXLZkvxkC (etp_vv96WMw6J4Badmo4C).
- All new copy critic-gated by gtm-copy-reviewer Aug 3; two invented figures ("ten minute decisions", "week four/week seven") removed at the gate.
- Everything remains Draft, zero leads, all launch gates still closed. Nothing sends.

## Prompt-layer application

Any prompt generating first-touch email copy must include:
1. Market flag (UK/EU vs US vs NL) and this doctrine's rule for that market.
2. The offer object: what note is being offered, matching an existing entry in Offer_Notes.
3. The detachment line: the offer is explicitly not a meeting ("No meeting attached").
4. Later-touch CTAs keep the existing escalation ladder untouched; this doctrine governs touch one only.

## Variable visibility fixes (later Aug 3, after Dallas's UI check)

- Root cause of "variables not showing" in the lemlist UI: Jack's campaigns had zero leads, so the editor had nothing to resolve {{opener_line}} against and the variables didn't exist anywhere in the campaign. Nate's campaigns already rendered correctly (verified by preview on real loaded leads: Quality and Finance E1 opener_lines resolve to distinct per-plan copy).
- Voice-note steps in all four campaigns that have them (Jack x2, Nate Quality, Nate Finance) had EMPTY bodies with the script only referenced in the task title. ~~Fixed: each voice-note step body is now {{voice_script}}, so the per-lead script shows in the task when the rep opens it.~~ **CORRECTED Aug 6 2026: this fix never applied and could not have.** The write returns `success: true` and does not persist. On a `linkedinVoiceNote` step with `recordMode: "manual"`, lemlist's `message` field is not a voice script, it is optional LinkedIn invite-fallback text; the script only becomes a rendered per-lead field after the delete-and-re-add swap to `recordMode: "ai"` with a voiceId, which is blocked on Nate's voice-clone consent and Jack's voice recording. All four bodies still read `""`. See `motions/shared/Variable_Seam_Contract_Aug6.md` sections 4a and 6a. Standing rule from this: read a lemlist step back before recording any write as applied.
- One labeled TEST lead loaded per Jack campaign so the variables exist and E1 previews render fully personalized: lea_JW9YMZJRa7eppPBNu (airlines, Adrian Dunne's staged v1.1 values, email andrewsdallas3+test-aerlingus@gmail.com) and lea_bfuEidAhDYEDFAx95 (insurance/FS, Richard Thorne / Admiral, email andrewsdallas3+test-admiral@gmail.com). Both lastNames carry TEST-DELETE-BEFORE-LAUNCH and both emails route to Dallas. **Launch gate addition: delete both TEST leads before any Start.** These are structural smoke tests, not gate proof; the real-row gate validation rule stands.
- **Open gap found doing this: the FS committee CSV has NO per-contact variable columns.** Airlines wave 1 has 41 contacts with staged critic-gated variables; insurance/FS has none generated yet. The FS test lead carries a sample fs-v0.1 set written today (verified £680/eight-week facts only). Since insurance goes FIRST, the FS wave-1 variable generation pass (first-draft engine + copy-sharpener + critic, per contact, into the CSV) is now the critical-path build item before any FS load.

## Per-lead personalization contract (reaffirmed Aug 3, Jack asked directly)

First-touch personalization is per lead, not per campaign: {{opener_line}}, {{contract_line}}, {{vm_hook}}, {{voice_script}} are lead-level custom variables carrying distinct per-contact copy generated Claude-side and critic-gated before load. The template only holds the shared spine. At load time (per wave, post-DNC):
1. Import maps every variable column from the committee CSV to lead custom variables, exact names.
2. Run preview_email on at least one real loaded lead per email step and read it end to end; an unmapped variable renders as a literal `{{opener_line}}` and that check is the only place it gets caught before a send.
