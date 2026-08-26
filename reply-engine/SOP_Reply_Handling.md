# SOP — Handling a Prospect Reply (v1, Jul 14 2026)

Applies to every reply from any motion (Stars Wave 1, back-office, install-base). The engine sources conversations; this loop keeps them alive without ever letting automation talk past a human who has raised their hand.

## The loop

**0. A reply lands** (Nathan's mailbox, or forwarded by an AE/CSM).

**1. Classify.** Run it through the engine:
```bash
python3 reply_engine.py --reply "<their exact words>" --contact "<name>" --account <domain> --output <Account>_Objection_Response.md
```
Seven categories, mirrored from `intradiem-objection-handler`. `unclassified` or an ambiguity flag means Dallas reads it before anything is drafted. Positive replies ("yes, let's talk") skip this SOP entirely: book the meeting, then do steps 4-6.

**2. Draft.** The engine's template is the starting point, not the send. Run it through `intradiem-first-draft-engine` thinking if the situation is non-standard, then `intradiem-copy-sharpener` always. Any figure passes the verified-claims gate or ships as mechanism language.

**3. Approve.** Nathan reads the final text. His voice, his name, his call. If he edits, the edit wins.

**4. Claim the row — the same minute the reply is handled.** In Clay → Contacts (Buying Committee), check **`bdr_claimed`** on the contact's row. The live send_ready formula (`critic PASS && human_approved && !bdr_claimed`) drops the row READY → HOLD instantly, so no later touch in any campaign can fire at someone who already replied. This is the collision gate from the Norton demo, used for its real purpose.

**5. Confirm the company pause.** Persona 2 (Finance lane) has "Pause leads at the same company on reply" ON — verify it caught the account. Persona 1 gets the same setting at launch (never Save P1's Setup until the source fix); until then, manually claim any P1 rows at the same account.

**6. Log the outcome.** Two places, always:
   - The Contacts row's closed-loop columns: outcome=replied, the category key, response-sent date.
   - `impact/outcomes.csv`: `date, account, type=reply, value, note` — this is the "realized" side of the scorecard; never blend it with engine-surfaced estimates.

**7. Calendar the follow-up.** Each category names its cadence (5 days for send-info, 30 for competitor eval, 45 for bad timing, etc.). The engine prints the target date. No orphan replies: every reply has either a booked meeting or a named next date.

## Category-specific side effects

- **Evaluating Competitor** → also generate the `intradiem-competitive-intel` wedge brief for the named vendor, same day.
- **We Have WFM** → log the vendor name on the account record.
- **No Budget** → log the stated reforecast window; re-engage 2-3 weeks ahead of it.
- **Wait for October** → calendar release week; be first in the inbox with their published movement.
- **Send Info** → one-pager or interactive artifact, never the deck.

## What this SOP protects

Fail-closed (a claimed row cannot be re-touched by automation), human gate (Nathan approves every send), measurement before volume (every reply logged as a realized outcome), and the verified-claims discipline (no number reaches a prospect that the Value Repository can't back).
