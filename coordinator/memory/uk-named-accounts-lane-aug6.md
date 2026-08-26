---
name: uk-named-accounts-lane-aug6
description: "UK Named Accounts / Prospect Clinic lane built Aug 6 2026 off Jack's Combined_OnePagers: cam_GK8kMPNrjyHc5N3g6, 27 contacts / 11 sequenced / 16 held, reworked give-first Aug 10 (notes 8-11 + roster v1.1), 3 lemlist template edits still staged, Bradley Tan still missing a LinkedIn URL"
metadata:
  node_type: memory
  type: project
---

A sixth Jack lane exists as of Aug 6 2026: **named accounts, not a vertical**. Jack asked for it directly on the Aug 6 sync ("Does it have to be vertical, or can it just be like six top priority accounts?") and named the real constraint: prospecting is not the problem, he already has every name, the accounts have gone non-responsive across phone, LinkedIn and email.

Input was Jack's `Combined_OnePagers.docx` (Slack DM Aug 6, built for the UK QBR). Four accounts: **VodafoneThree, Sky, British Airways, Ageas incl. esure.** Each page carries a dated live signal, an honest per-contact failure diagnosis, and kill criteria. It is the best account input received at Intradiem so far, and the format is worth asking Jack (and Nate/Keegan) to repeat.

Built: `motions/jack/named_accounts/` holds the motion spec, the 27-contact roster with per-contact copy, and the handoff. Offer notes 4 and 5 added to `motions/shared/Offer_Notes_Aug3.md`. lemlist campaign `cam_GK8kMPNrjyHc5N3g6`, 15 steps, draft, zero leads.

**The design decision that matters: 11 contacts go in the sequence, 16 do not.** On accounts whose diagnosed failure is over-touching and generic messaging, the hold list is the product, not the copy. Every hold has a written release condition. Bradley Tan is the only British Airways contact in the sequence, because that account's blocker is broken channel trust, not targeting.

**Contact data closed Aug 6 via Clay, 141 credits.** 25 of 26 emails, 23 of 26 LinkedIn URLs, 8 wave-1 mobiles, all 11 wave-1 titles verified. 10 of 11 wave-1 contacts fully loadable. lemlist could NOT enrich: `bulk_enrich_data` returns MISSING_FUNDS on the free-trial plan, so phone fell back to Clay. Residual gaps all need Jack: Bradley Tan has no LinkedIn URL and is the only BA contact in the sequence (BA is Clay's thinnest account, 3 of 8 found). See [[uk-first-touch-offer-cta-aug3]] for the touch-one doctrine this lane inherits and [[matt-jack-sync-aug3]] for the engine it sits inside.

**Give-first rework, Aug 10 2026.** Jack's verdict on the v1 messaging: lean on value and deliverables before any time ask. Reworked same day: four per-account give notes (notes 8 to 11 in `motions/shared/Offer_Notes_Aug3.md`, superseding notes 4 and 5 for this lane), roster `UK_NamedAccounts_Roster_v1.1.csv` with give-first li_dm and voice_script for the 9 cold contacts (Rankin and McCarville kept as warm re-entries), first meeting ask moved to E2. **Three lemlist template edits are STAGED not applied** (session classifier blocked campaign writes): both E2 bodies and accepted-branch call 2 still carry the old hard ask, so template edits must land before any lead load. Review set: `motions/jack/named_accounts/UK_NamedAccounts_GiveFirst_Rework_Aug10.md`, copy in the Deliverables folder. Adversarial gtm-copy-reviewer pass still owed.

Dated forcing functions now in the calendar: **13 Aug** lemlist trial cutoff, **29 Sept** CCMA conference (Tim Monk track), **1 Oct** Jon Shaw release, **8 Oct** VodafoneThree investor briefing.
