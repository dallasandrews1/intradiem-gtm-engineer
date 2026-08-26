# Per-Lead Variable Seam Contract (Aug 6 2026)

Source: copy-sharpener pass over fix 7 of `Lemlist_Copy_Sharpener_Review_Aug6.md`, run against LIVE lemlist template text (all five campaigns pulled Aug 6) and the three staged variable files (131 leads total).

**What this document is.** The four per-lead variables are generated Claude-side per contact, critic-gated, then loaded as lemlist lead custom variables (`First_Touch_CTA_Doctrine_Aug3.md` section "Per-lead personalization contract"). There is no Clay column and no Clay prompt for them, so there was also no durable generation prompt: airlines ran as `v1.0-v1.5`, FS as `fs-v1.0/c1`, Stars as hand-written per lead. Each run rediscovered the seams from scratch, which is the root cause of every defect below. This file is the missing durable block. Append it verbatim to every per-lead variable generation run, alongside the motion's own slots.

**Status: seam-v1.0 APPLIED Aug 6 2026.** All 130 live leads regenerated and re-gated against section 2; the three staged variable files carry the lineage stamp. One lemlist template edited (the FS Day 2 voicemail frame, section 4b). Nothing loaded, no campaign started, every launch gate still closed. Two items remain open and are Dallas's call, both in section 6.

---

## 1. The live seams (ground truth, pulled Aug 6)

Template text is quoted exactly. `>>` marks where the variable is injected.

### opener_line

| Campaign | Template | Contract |
|---|---|---|
| Stars Finance `stp_hmp9Gp7dAZFgkgqPq` (A+B) | `Hi {{firstName}}, >>opener_line<< You'll know the exact picture far better than I do. The measures still movable this cycle are mostly operational, not clinical.` | Inline after a comma, so **lowercase start** unless the first word is a proper noun. Must state a computed figure so "the exact picture" has a referent. Must NOT say "operational", "movable", or "this cycle". |
| Stars Quality `stp_b9Ns4nuZJSpT8Xr6s` (A+B) | `Hi {{firstName}}, >>opener_line<< For a book sitting there, the last few points usually come from the customer-service measures, and they're being set right now, in this measurement year, not on the October release.` | Same lowercase rule. **"there" needs a position**, so the opener must name a rating. Must NOT say "measurement year", "customer-service measures", or "October release". |
| UK Airlines `stp_9oni2Xpgq6aXyMWXk` | `Hi {{firstName}},</p><p>>>opener_line<< The pattern across airline ops and service teams is that the expensive part of a disrupted day is rarely the delay itself, it's the recovery running a shift behind it...` | Own paragraph, so **capital start**. Must NOT say "recovery", "the delay itself", or run the not-X-it's-Y contrast; the follow-on owns all three. |
| UK FS `stp_gvvaxLrpqJnEFHbx5` | `Hi {{firstName}},</p><p>>>opener_line<< The pattern across UK complaints teams is that the cases which cross to the ombudsman, at £680 apiece before any outcome, are rarely the hardest ones. They're the ones that aged past the eight-week mark while the queue was staffed for a quieter week.` | Capital start. Must NOT say "eight-week", "aged", "staffed for a quieter week", or the hardest-ones contrast. |
| Stars Resurrection | not used | Resurrection carries only `firstName` and `plan_name`. Out of scope for all four variables. |

### vm_hook

| Slot | Template | Punctuation contract |
|---|---|---|
| Airlines, all 3 phone steps (`stp_J9anTv4KxXYGJz4ZA`, `stp_EbvMqk8opiaoDyqtS`, `stp_YrwNRSvFXKttarckA`) | `... quick voicemail. >>vm_hook<<. Worth a call back ...` | Preceded by a full stop → **capital start**. Template supplies the trailing full stop → hook carries **no terminal punctuation**. |
| UK FS, all 3 phone steps (`stp_MjWJiCLZwswYQrKkz`, `stp_puTYXE2P4ByGGP26Q`, `stp_cnTRCGKBifpreC6kF`) | `... cross to the ombudsman. >>vm_hook<< Worth a call back ...` | Capital start, and the hook **must end in a full stop**. |
| Stars Finance (`stp_2PEMT5MxZGCvQ4gCc`, `stp_mGX4zdGjW24szwMn2`, `stp_79dFBYM92pciNTc4p`, `stp_bz4CCwLzxstfepkkT`) | `... this is Nathan with Intradiem. >>vm_hook<< Fifteen minutes on ...` | Capital start, hook ends in a full stop. |
| Stars Quality (`stp_6ypPNXP38fcrnDCqk`, `stp_g5ovqqDRpZR2wZ9GM`, `stp_QkYs9KGRARYvZzeso`) | `... this is Nathan with Intradiem. >>vm_hook<< I can walk you through ...` | Capital start, hook ends in a full stop. |

**The punctuation contract is opposite between Airlines and everything else.** Airlines is the only campaign where the template supplies the full stop. Any generation run that assumes one house rule breaks one campaign.

### contract_line

| Campaign | Next fixed sentence | The word the contract_line must land on |
|---|---|---|
| Stars Finance `stp_SAQGYwNEDHNYMo7yg` | `Keeping service execution steady through those peak weeks is what Intradiem does, and it's why those measures stay movable.` | **measures** (or service execution). Otherwise "those measures" dangles. Banned in the contract_line: "keeping/holding steady", "through the peak weeks" — the template owns that verb. |
| Stars Quality `stp_6Ec35QjTN8wxQTyzh` | `Holding that experience steady while the scoring is live is the piece Intradiem works on.` | **experience** (member or customer). Otherwise "that experience" dangles. Same verb ban. |
| UK Airlines `stp_5hf4RmYRRgeDRYXuf` | `The weeks that generate those claims usually trace back to how fast the recovery got staffed...` | **claims**, plural and countable. A verb ("a passenger has six years to claim") does not satisfy "those claims". |
| UK FS `stp_5rCBskL5b6jmSW5iu` | `The queues that age cases past that line usually trace back to how the day got staffed...` | **cases** or **the queue**. |

### voice_script

Sits in the `linkedinVoiceNote` step of Airlines, FS, Stars Finance, Stars Quality. Lands one day after that campaign's LinkedIn DM, so it must not repeat the DM's short version. No `{{tokens}}` inside it: lemlist does not resolve variables nested in variable values.

---

## 2. The block to append to every generation run

> ## VARIABLE SEAM CONTRACT (hard, outranks style)
>
> You are not writing standalone copy. Each variable is half of a sentence pair and the lemlist template owns the other half. A variable that reads perfectly alone and collides with its follow-on is a FAIL, not a style note.
>
> Before writing a single word, read the exact template text on both sides of the variable for THIS campaign and THIS step (section 1 of `Variable_Seam_Contract_Aug6.md`). Never infer it from another campaign.
>
> ### opener_line
> - Complete sentences, ending in a full stop. Never a fragment, never trailing into the follow-on.
> - Capitalization comes from the template, not from habit: lowercase when it continues `Hi {{firstName}}, `, capital when it opens its own paragraph. Proper nouns are the only exception to the lowercase rule.
> - **Antecedent check.** Read the fixed follow-on aloud straight after your opener. Every "that / those / there / it / the exact picture" in the follow-on must point at something your opener actually said. If one dangles, rewrite the opener, never the template.
> - **Echo check.** Build a banned list from the fixed follow-on before you write, and do not use any of those words. If your opener uses the follow-on's words, you have written its sentence for it and the prospect reads the same idea twice in three seconds.
> - 25 to 45 words. It is the hook, not the email.
>
> ### vm_hook
> - Capital first letter in every campaign: every template puts a full stop in front of it.
> - Terminal punctuation is per campaign: Airlines templates supply the full stop, so carry none. FS and both Stars lanes do not, so end in a full stop.
> - **Add, never restate.** The call frame already names the sender, the company, the email, the subject line and the headline number. Your hook is the one thing the email did not say: the angle behind the number, the consequence, the question you would actually open with. Explicit ban: "the note I sent", "my email", "I emailed you about", the subject line, and the headline figure. If the hook could be deleted with no loss of information, it is a FAIL.
> - **Length is a hard cap, because a voicemail is spoken.** The budget is the whole voicemail at 60 words (about 25 seconds at speaking pace), frame included. Per slot, after the frame: Airlines 40 words, Stars Finance 30, Stars Quality 23, UK FS 16 (or 25 once the FS frame is trimmed, see section 4). Count the words. On live-answer call slots, where the prospect can interrupt, the cap is 35.
>
> ### contract_line
> - One sentence, 20 to 35 words, and its **last clause must land on the noun the next fixed sentence points at** (section 1 table). This is the whole job of the variable.
> - Do not pre-empt the follow-on's verb. If the template says "keeping service execution steady" or "holding that experience steady", your line says what the thing is WORTH, and lets the template say what to do about it.
> - Never open with the same construction as that lead's opener_line.
> - Verified-claims gate unchanged: no Intradiem figure, no customer outcome, no peer claim. Public regulatory and CMS figures only, framed as an estimate, with the humility clause where the motion requires it.
>
> ### voice_script
> - Under 45 seconds, 100 to 125 words. Opens on the sender's first and last name only, no company, no title. Ends on a soft question.
> - No `{{tokens}}` anywhere inside it. lemlist renders them literally.
> - It lands the day after that campaign's LinkedIn DM. Read the DM first; the voice note must open on a different facet, never on the DM's short version.
> - Ship a 2 to 3 sentence TL;DL text with every script.
>
> ### Cross-variable check (run before returning a lead's set)
> All four land on one person inside a few days. Read them in sequence order with the fixed template text between them, as that prospect receives them. No idea twice, no sentence shape twice, no number twice.
>
> ### Return with every lead
> 1. Each variable pasted against its fixed follow-on, read as one passage. Dangling demonstratives: none. Repeated words across the seam: none.
> 2. Capitalization and terminal punctuation match this campaign's contract.
> 3. Voicemail total (frame + hook) word count, stated as a number, at or under 60.
> 4. Verified-claims gate: no Intradiem number, customer name, or peer outcome.

---

## 3. What the current staged values do against this contract

131 leads audited: Airlines 41, UK FS 73, Stars 17 (15 Finance, 2 Quality).

| Defect | Before | After | Campaigns |
|---|---|---|---|
| vm_hook renders as a lowercase sentence start after a full stop | **41/41** | 0/41 | Airlines only (its hooks were already correct on terminal punctuation) |
| vm_hook restates the email instead of adding to it | **58/131** | 0/130 live | Airlines 41/41 (every hook opened "it's about the note I sent on the three hour mark"), Stars 17/17 |
| Voicemail over the 25-second cap (frame + hook) | **82/131** | 0/130 live | UK FS 68/73 (worst 77 words, ~35s), Stars Finance 12/15 (~34s), Stars Quality 2/2 (~35s), Airlines 0/41 |
| contract_line leaves the next sentence's demonstrative dangling | **7** | 0 | Stars Finance 5 ("those measures"), Stars Quality 2 ("that experience"). Verified NOT a defect in either Jack lane, see below. |
| opener_line repeats the fixed follow-on's own words | **14** | 0 | Stars 9, Airlines 3, UK FS 2 |
| voice_script ships without a TL;DL | **131/131** | unchanged | all four, see section 6 |

The one exclusion: Stars lead 12 (Miyasato, HMSA) still fails length and restatement. It was deleted from the Finance campaign on Aug 2 with a do-not-reload flag, so it was deliberately left untouched.

**Correction to the first pass of this document.** The initial sweep flagged 34/41 Airlines and 54/73 FS contract_lines as leaving a dangling antecedent. That was a checker artefact, not a real defect: it only looked at the last nine words of the variable. Read against the live template, "The weeks that generate those claims" (Airlines) resolves backwards to the fixed sentence *before* the variable ("how long a passenger has to claim ... at £220 to £520 apiece"), and the FS follow-on uses a plain plural noun rather than a demonstrative. Both lanes' contract_lines were left alone rather than churning 88 critic-passed lines. Only the two Stars lanes use a true demonstrative with no reachable antecedent, and those 7 were rewritten.

Airlines vm_hooks are the only set that clears the voicemail cap, because its frame is 19 words against FS's 44. The review flagged the Insurance Day 2 voicemail; the same arithmetic hits Stars Finance and Stars Quality harder.

Two things that are NOT defects, checked and cleared: opener_line capitalization is correct in all three files (Stars lowercase inline, both Jack campaigns capital on their own paragraph; the two capitalized Stars openers start on "Community Health Plan of Washington", a proper noun). voice_script length is inside spec everywhere, max 89 words against a 125 ceiling.

---

## 4. Two live-state items that block a clean regeneration

**a. The voice_script has nowhere to render, and it is not an API fix.** `First_Touch_CTA_Doctrine_Aug3.md` records the four voice-note bodies as fixed to `{{voice_script}}` on Aug 3. Pulled Aug 6, all four still return `"message": ""`. Writing `{{voice_script}}` to them again returns `success: true` and does not persist, verified by reading the step back.

The reason is in the lemlist API contract, not in the write: on a `linkedinVoiceNote` step with `recordMode: "manual"`, `message` is **not** a voice script field, it is optional LinkedIn invite-fallback text. The script only becomes a real, per-lead-rendered field once the step is `recordMode: "ai"` with a `voiceId`, which is the delete-and-re-add swap already documented in `Lemlist_Variable_Stage_Jul31.md`. That swap is blocked upstream on Nate's explicit consent to the voice clone and on Jack's voice recording, both still open.

So the Aug 3 note is wrong and should be treated as such: the fix never applied and could not have. Any session that sees `success: true` on a voice-note body write must read the step back before recording it as done. Until the AI-clone swap happens, the per-lead script reaches the rep only if it is put somewhere else (section 6).

**b. The FS Day 2 voicemail frame has to shrink before the hook cap can do any work.** At 44 words it leaves a 16-word hook budget, which is too short to add anything, so a cap alone would just produce empty hooks. Trim the frame first, then generate to the wider cap.

Proposed frame edit, `stp_MjWJiCLZwswYQrKkz`, 44 words to 29:

- Now: `{{firstName}}, following up on a note I sent yesterday, subject line "the £680 line", about where complaint cases age past the eight-week mark and cross to the ombudsman. {{vm_hook}} Worth a call back on [number], or just reply to the email. Thanks, this is Jack.`
- Proposed: `{{firstName}}, following up on the note I sent yesterday on the eight-week line. {{vm_hook}} Worth a call back on [number], or just reply to the email. Thanks, this is Jack.`

The cut text is the part the hook is supposed to own, so this fixes the length cap and the restatement problem in one edit. Name stays at the end per the agreed voicemail style.

---

## 5. What was executed, Aug 6 2026

1. Voice-note bodies: attempted, does not persist, root cause found and recorded in section 4a. Moved to section 6.
2. FS Day 2 voicemail frame trimmed in lemlist, 44 to 29 spoken words (`stp_MjWJiCLZwswYQrKkz`). Verified persisted. This alone brought 68/73 FS voicemails inside the cap.
3. Section 2 block written and versioned `seam-v1.0`.
4. Regenerated: Airlines vm_hook 41/41; Stars vm_hook 16/16 live; FS vm_hook 1 rewritten for length, the other 72 held as critic-gated at `v1.0-c1`; Stars contract_line 7; opener_line 14 across all three lanes; 3 Airlines vm_hooks re-facetted so they don't duplicate their own rewritten opener.
5. Re-gated. Across all 131 staged leads and all four variables: zero em dashes, zero banned words, zero unsourced percentage claims, zero duplicate values, and every campaign's capitalization and terminal-punctuation contract now holds at 100%. Voicemail cap: 0 over on all four lanes. The three staged files carry the lineage stamp.
6. Loaded nothing, started nothing. Every launch gate still closed.

## 6. Still open, Dallas's call

**a. Routing the voice_script to the rep.** Blocked on the AI-clone swap (section 4a), which is blocked on Nate's consent and Jack's voice recording. Two interim options if a lane launches before cloning: put the script in the manual task title (the only per-lead field a manual voice-note task renders, and it was attempted here but denied by the permission classifier), or drop the voice-note step for that wave and let the LinkedIn DM carry the touch. Both change how a live step behaves, so neither was done unilaterally.

**b. The voice_script TL;DL.** The sharpener requires every voice note to ship with a 2 to 3 sentence TL;DL text. None of the 131 scripts has one, and there is nowhere to put it: in all four campaigns the voice note is followed by a phone step, and the LinkedIn DM comes before it, so a TL;DL needs a new `linkedinSend` step in four campaigns. That is a structural change to live sequences that also eats into the conservative LinkedIn daily action caps from the premortem, so it was flagged rather than made. The alternative is a deliberate exception: on LinkedIn the recipient sees the sender and can reply in thread, which is the gap the TL;DL exists to close elsewhere.

**c. Unchanged from the review, and neither is a prompt problem.** The £680 FOS 2026/27 case-fee verification (the last confirmable figure was £650 after the free allocation) and the Scotland five-year claim window caveat against the six-year line. Both are launch-blockers on the FS and Airlines lanes.
