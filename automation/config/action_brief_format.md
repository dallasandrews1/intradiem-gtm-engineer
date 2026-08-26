# Daily Action Brief, format spec (v2.4, Aug 2 2026: v2.3's call contract plus for-dummies rep instructions: plain-action footer with a real-name example, send-from-your-inbox reply wording, pinned per-channel explainer, zero plumbing words in rep-facing copy)

## SPOKEN VOICE (outranks every layout rule; applies to ALL rendered copy: drafts, scripts, voicemails, voice notes, DMs)

Everything a rep will say or send has to pass one test: would a real person say this out loud, word for word, in a real conversation, without sounding like they're reading? If not, it does not ship. This mirrors voice_core.md (motion-stamp library), which is the canonical standard.

- No writerly phrasing: no rhetorical antithesis ("holds or slips", "decided on the floor, not in the scorecard" as a constructed flourish), no aphorisms, no elevated verbs where a plain one works, no noun-stack phrases nobody says ("the movable points this cycle are operational", "what it prices at").
- No stacking (facts comma-spliced into one long sentence) and no chopping (flat fragments with no connectors). Connect thoughts the way people talk: so, because, and, which means.
- Contractions always. "It's Nathan", never "This is Nathan speaking."
- WARM, NEVER CURT. A draft can decline to answer something, but it never sounds like a refusal. "I'm not going to give you a list" is the named defect; the shape is "fair to ask, I would too" plus an honest reason, then the pivot. Respect first, then redirect.
- Objection-handle blocks: the CLAIMS, mechanism, and facts come from `playbook_sources` and may not change or strengthen, but the wording renders in spoken form (the playbook versions were written for email). Never add a number or a new claim while converting.
- Voice scripts (voicemail, voice note) end on a soft question or a simple sign-off, and read naturally at talking pace.

Reference drafts (the tone bar for composed reply drafts; match this register, never reuse them verbatim for other leads):

A "who else are you working with" reply:
> Marc,
>
> Fair to ask, I would too. I'd rather earn the call on whether this actually holds at Aer Lingus than on whose logo I can wave around, so let me try it that way.
>
> The morning after a disrupted day, the queue that lands on your team was mostly decided the night before, when the staffing call got made. If that matches what you see, that's the conversation I'm after.
>
> Worth 15 minutes this week?
>
> Jack

A "we already handle this internally" reply:
> Thornton,
>
> Fair question, and honestly, on the modeling side, probably nothing. That's your actuarial team's job and they'll do it better than we would.
>
> The part we get pulled into comes after the model. The customer-service measures get decided by how the floor actually runs week to week, and that's execution, not forecasting.
>
> If that side's already covered at Clover, then fair enough, I'll leave you alone. Worth 15 minutes to find out?
>
> Nathan

One Slack message per brief, plus threaded messages under it (see THREADING). Slack markdown. Every script or paste-ready copy sits in a triple-backtick code block so it's one tap to copy on mobile. Bold names, lane tag after the company where the brief spans lanes. Section order is FIXED and matches the rep's Lemlist task-queue order: 1 Replies, 2 Calls, 3 Approvals, 4 Voice note, 5 Autopilot. The sections are ACTIVITY BLOCKS, that's the point of the order: the rep runs the brief top to bottom as time blocks (clear the inbox, then one dialing block, then LinkedIn admin in one batch, then record), so one activity is never scattered across the brief and no layout or overflow decision may interleave activities. Every task of a type sits in that type's block, across lanes. The per-lane split of an oversized brief (see HARD COMPOSITION RULES) repeats the blocks per lane and is the last resort for exactly this reason: threading preserves the activity blocks, splitting multiplies them.

## THREADING (hard contract: never claim what wasn't posted)

- The brief NEVER says a draft is "threaded below" or "in this thread" unless this run actually posted that threaded message. Claiming an attachment that doesn't exist is a defect (it shipped once; never again).
- **Fresh reply drafts thread.** When the brief drafts a reply (no relay draft exists), the main message shows the reply entry WITHOUT the draft body and says: "Your reply is drafted, first message in this thread. Send it from your inbox (edit it first if you want), then reply `<Name> DONE` here. Want a different angle? Say it here and I'll redraft." (Plain action words: the rep must know the draft does NOT send itself and that sending happens from their own inbox.) Live=true mechanics: compose every threaded message BEFORE posting anything; post the main brief, capture its `ts` from the post response, then immediately post one threaded reply per draft: `✉️ Draft reply for **<Name>** (<Company>):` followed by the email-formatted code block. If a threaded post fails after one retry, log the draft body under a FAILED-THREAD header so the daily rundown surfaces it; the rep still has the Lemlist task.
- **Relay-owned drafts do not re-thread.** When the relay log already carries a draft for this reply, the brief references it ("draft is in the relay alert above, ready to edit") and composes nothing.
- **Autopilot sends ALWAYS thread.** The full-copy breakdown of today's automated sends (see AUTOPILOT SENDS) never sits in the main message; it posts as its own threaded message (or messages, split per lane or per step if one would exceed ~5000 chars). Thread order: fresh reply drafts first, then any overflow sections in section order, then the autopilot sends breakdown last. The main message's pointer line ("full copy of today's sends is in this thread") appears ONLY when this run actually posts that thread, same never-claim rule as reply drafts.
- **Overflow threads.** Past ~4000 chars, the main message carries header + replies + calls; approvals, voice notes, and the autopilot summary thread under it, in order, each as its own threaded message. When sections move to the thread, the main message ends with the plain pointer: "The rest of today (approvals, voice note, autopilot) is in this thread." Never a list of section names without the words "the rest of today"; the rep should never wonder if something is missing.
- **Dry run / fixture:** the log renders every would-be threaded message immediately after its parent brief under an explicit marker line: `↳ THREAD: <what it is>` (colon, never an em dash; the no-em-dash rule covers log markers and the brief titles in action_brief.json too). The render must show the same split that live mode would post.

## PER-TYPE LAYOUTS (every item renders in the shape of its step)

**Email (reply drafts, and any email copy shown in a brief).** Renders inside its code block like a real email, never a run-on paragraph:
- `Subject: <subject>` as the first line ONLY for a new outbound email (replies keep the thread's subject; omit the line).
- Greeting on its own line (`Thornton,`), blank line after it.
- Body in short paragraphs with a blank line between each.
- Sign-off (`Nathan`) on its own line at the end.

**Call scripts.** A call is NEVER one merged paragraph. It renders as labeled segments, each label a bold line followed by its own code block, in this order, rendering ONLY the segments that exist in source (lead variables / staged copy / the motion playbook), never inventing a missing one and never folding two into one block. Call structure and the universal branch handles come from `motions/shared/Cold_Call_Playbook_Aug2.md` (in every brief's `playbook_sources`); motion-specific objection handles come from the motion's own playbook doc. The Calls section opens with ONE fixed italic line, once per brief, never per call: `_Slower than feels natural, pause after their name, let the ask sit. On a yes, lock a slot before you hang up._`
- **Opener** — assembled per the cold-call playbook's four-beat skeleton: their name (a beat of pause), who you are ("It's <first last> at/with Intradiem"), the reason for the call in one sentence carrying the lead's real hook (a true anchor like "we connected on LinkedIn this week" may lead in, but the reason lands in the same breath; an email reference alone is never the reason), then the 30-second contract with the prospect in control ("Have you got 30 seconds, and you can tell me if it's not relevant?" UK / "Can I take 30 seconds, and you tell me if it's not for you?" US). BANNED OPENER FAMILY (hard rule): any availability yes/no that precedes the reason: "did I catch you at a bad time / at an OK moment / with 30 seconds", "is now a good time". No fact, number, or name beyond the lead's variables and the playbook sources.
- **If they engage** — the 20-30 second expansion, when source copy carries one. It MUST end on a check question that hands the prospect the floor ("Does that match what you see on your side?"), never run straight into the meeting ask.
- **The ask** — the CTA sentence(s), naming what the prospect gets in the 15 minutes. An honest-exit clause is welcome where it fits ("if that's already handled, I'll say so and leave you alone").
- **If they're busy** — dial tasks only: the busy branch per the cold-call playbook shape (respect, ten-second reason, trade up to a real slot), motion slot filled from the lead's variables.
- **If they brush you off** — dial tasks only: the brush-off branch per the cold-call playbook shape (accept immediately, one either/or question, warm release), motion slot filled from the lead's variables. The block ALWAYS ends on the release line; nothing renders after it (the playbook's hard stop: the answer is logged intel, never a second pitch).
- **BRANCH CAP** — a dial task renders at most seven labeled blocks total and at most two If-pushback blocks, chosen by relevance to this lead; the motion doc keeps the full set. A relevance rule, not a size rule: it never trims the wording of any block that renders, and it does not override SCRIPTS NEVER DROP (which governs staged copy, all of which still renders).
- **If pushback: "<objection>"** — one block per relevant objection, the handle sourced from this brief's `playbook_sources` files (the motion's objection quick-handles), rendered in spoken form per SPOKEN VOICE: claims, facts, and mechanism unchanged and never strengthened, wording adapted to how it'd be said aloud. Include only handles relevant to this call (e.g. the timing handle on a Stars call). If the playbook has no matching handle, omit the block; never write a new handle in the brief.
- **No answer: voicemail** — when the task includes a voicemail fallback, its own labeled block, read as written.
- Segment labels use colons, never em dashes: the no-em-dash rule covers LABELS too, not just script copy. ("If pushback — ..." shipped once in a render; it's a defect.)

**Voicemail-only tasks.** Bold line `Leave this voicemail`, then one code block, read as written, with `[your number]` kept as the literal placeholder. If source copy carries a live-call script for the same lead, render it above the voicemail as **If they pick up** with the same segment rules.

**Voice notes.** One code block, "under 30 seconds, read as written." No segmentation.

**LinkedIn DM / WhatsApp / InMail.** One code block each, copy as-is.

**Connect requests.** Grouped on one line in plain action words: `Approve these connects in Lemlist (they send blank, no note): **<Name>** (<Company>) · ...`. Names + companies only. A connect WITH a note renders its note in a code block.

## SECTION RULES (unchanged from v1 unless noted)

1. **Replies first.** Every reply always outranks every task. Quote the reply text (blockquote). **The relay owns reply drafts**: when the relay's log shows a draft for this reply, the brief links back to it and NEVER composes a second draft. Only when no relay draft exists does the brief draft fresh (threaded, per THREADING), under the same voice rules: rep's calm peer-level voice, contractions, zero Intradiem stats, no em dashes, no banned phrases, no implied customers.
2. **Calls.** One entry per call task: bold name, title/company, lane tag, what kind of call (call 1 no voicemail / leave voicemail / double-tap), then the segmented script per PER-TYPE LAYOUTS. Scripts render the lead's real custom variables (vm_hook etc). Keep "[your number]" as the literal placeholder.
3. **Approvals.** Per PER-TYPE LAYOUTS.
4. **Voice note to record.** Per PER-TYPE LAYOUTS.
5. **Autopilot.** Two parts; the copy always ships in full.
   - **Main message: the summary line.** What fires automatically today (emails, visits, likes/follows) with counts per lane, then "⏳ Nothing overdue" or the overdue count, then yesterday's done/skipped tally. When a sends thread posts this run, add the pointer: "Full copy of today's emails is in this thread."
   - **The sends thread (see AUTOPILOT SENDS).** Every automated EMAIL firing today renders in full, threaded under the brief. Profile visits, likes, and follows stay counts only; there is no copy to show.

## AUTOPILOT SENDS (full-copy contract, added v2.2)

The rep sees every word going out under their name today, human-sent or automated. The breakdown groups by campaign step:

- Bold header line per step: `📧 <lane or campaign> · <step name or number> · sends to <N> leads`.
- Recipient list (names + companies) under the header.
- The email per the Email layout, `Subject:` line included (these are new sends).
- **Distinct copy per lead** (MessageGen variants, per-lead resolved variables that change the body): render EACH lead's email in full, lead's name bolded above its block.
- **Shared template** (identical copy where only {{firstName}}/{{companyName}}-class variables differ): render the email ONCE with the {{variables}} left visible, above the recipient list. Never render eight near-identical emails when one template tells the rep everything.
- Copy comes ONLY from the Lemlist campaign sequence via the API (plus each lead's variables), or the fixture's staged sends. If today's exact recipient set is not derivable from the API, render the in-flight step's copy with the campaign-level count and the line "recipient schedule is in Lemlist"; NEVER fabricate a recipient list. If a step's copy itself will not resolve, name the step and point to Lemlist; NEVER invent or reconstruct send copy.
- Send copy never trims. Size pressure splits the thread into more messages (per lane, then per step), it never shortens an email.

Footer (rep-facing words only, zero system plumbing; `<Name>` is the FIRST call or reply lead's first name in TODAY'S brief, so the example is always real):
`_Finished an item? Reply here: "<Name> DONE". Not doing one? "<Name> SKIP". Something feel off? "<Name> HOLD" and Dallas takes a look (their emails keep sending until he pauses them). Same tasks, same order, in your Lemlist queue. New here? See the pinned how-it-works._`
Never mention the relay, hourly reads, logs, or any internal mechanism in rep-facing copy; the rep needs the action, not the machinery.

Header shape:
`<emoji> **<title from action_brief.json>**` then the second line `**<Weekday D Mon> · Wave N, Day N · <lane counts or leads-in-sequence count> · campaign: <name>**` (lane counts for Nate, single campaign line for Jack).

## HARD COMPOSITION RULES

- NEVER invent copy. If a task's variables can't be resolved from the API, show the task with "copy is loaded in the Lemlist task" instead of a guessed script. Objection handles come only from `playbook_sources` (spoken-form rendering per SPOKEN VOICE, claims unchanged).
- OPENER FACT CHECK (live runs): composed openers assemble from the cold-call playbook skeleton plus the lead's stored variables ONLY. Before shipping, every number, name, and fact in a composed opener must trace to a lead variable or this brief's playbook sources; anything untraceable means recompose without it or fall back to "copy is loaded in the Lemlist task". The run writes one OPENER-CHECK line per composed dial script to the log (lead, facts used, source variable each). Fixture-staged scripts render verbatim and skip this check.
- NEVER claim the brief did something this run didn't do (thread a draft, queue an approval, attach anything). Every claim about the brief's own mechanics must be true at post time.
- Draft replies never use "comparing notes"/"compare notes", the leverage/lever family, or the forbidden buzzword list, and never imply other customers, carriers, or live conversations that are not Repository-verified. "Who else are you working with" gets a straight acknowledge-and-pivot, never an implied roster.
- A brief with zero replies AND zero open tasks across its campaigns is NOT composed and NOT posted. Silence on empty, per lane. The log gets one skip line.
- No em dashes anywhere. That includes SEPARATORS: lead lines join name, title, company, and lane with `·` (e.g. `**Pedro Rivera** · NYC Health + Hospitals · Quality`), never an em dash. Composers have slipped on separator dashes twice; it's a named defect. Contractions. No Intradiem stats in any rendered draft.
- SCRIPTS NEVER DROP. No size rule may trim a call, DM, WhatsApp, or voice-note script, and segmentation never shortens copy, it only lays it out. Under 5000 characters per Slack message; overflow threads per THREADING. Approvals may compress to names only; that is the only compressible section.
- Nate's cross-lane brief splits when big: if his combined brief would exceed ~4000 characters even after threading, post one brief per lane (Finance, Quality, Resurrection, in that order, skipping empty lanes), same rules as Jack's per-lane briefs.
- The "Yesterday: N done, M skipped" tally renders ONLY from real sources: Lemlist task completions plus the relay's brief-thread-ingest log (DONE/SKIP replies). If neither source has data, omit the tally line entirely rather than inventing numbers.
- Section numbering uses the emoji digits (1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣) and section separators are plain blank lines with a final `---` before the footer.
- Wave/day numbers come from lead state if derivable; if not derivable, omit the "Wave N, Day N" fragment rather than guessing.

## PINNED EXPLAINER (one-time per rep channel, not part of the daily brief)

Each rep channel gets ONE pinned "how it works" message, posted at launch (and re-posted only when its content changes). It exists so the daily footer stays two lines: the brief teaches the action, the pin teaches the system. Rep-facing words only, zero plumbing. Canonical text (swap the example name for a lead from the rep's own motion):

> 📌 **Your Daily Brief · how it works (60 seconds)**
>
> Every weekday morning you get one message here: your whole day, in order. Work it top to bottom.
>
> 1️⃣ **Replies** · someone wrote back. Your reply is already drafted, first message in the thread. Send it from your inbox (edit it first if you want). It never sends itself.
> 2️⃣ **Calls** · dial from your Lemlist task so it checks itself off. The script is on screen: opener, what to say if they engage, what to say if they push back. It's a map, not a teleprompter.
> 3️⃣ **Approvals** · one click each in Lemlist. Connect requests always send blank, no note.
> 4️⃣ **Voice note** · under 30 seconds, read it as written.
> 5️⃣ **Autopilot** · emails that send themselves today. Full copy is in the thread so you always know what goes out under your name. Nothing for you to do.
>
> When you finish an item, reply in the thread with the name plus one word:
> • "Pedro DONE" = did it
> • "Pedro SKIP" = not doing this one
> • "Pedro HOLD" = something feels off, Dallas takes a look (their emails keep sending until he pauses them)
>
> That's it. Autopilot items need no reply. Questions, edits, a different angle on any draft: just say it in the thread, plain words work.

## SOURCE AND FALLBACK (one system, two data sources)

The brief's data source is the Lemlist API (tasks, sequences, lead variables). If the Lemlist purchase is not approved at trial end, the SAME brief format, channels, and DONE/SKIP/HOLD loop continue; the composer switches to staged per-day task lists built from the motion sequence docs (reversion runbook: motions/shared/Manual_Fallback_Register_Aug2.md). Never build a second rep-facing delivery method for the fallback world; the format is source-agnostic by design.

## PLAYBOOK SOURCES

Each brief in `action_brief.json` lists `playbook_sources`: the motion's canonical copy docs (strike-room sequences, persona-sequence docs with objection quick-handles). They are the ONLY permitted source for objection-handle blocks and live-call structure beyond what the lead's variables carry. Read them; quote them; never paraphrase a handle into new claims.

Reference renders (staged data, format is the contract): the Aug 1 relay-test samples show v1; the first v2 samples supersede them as the visual reference once posted.
