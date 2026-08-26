# reply-engine — Reply Engine v1

Turns an inbound prospect reply into a classified objection, a drafted reframe response in Nathan's voice, and a checklist that keeps the human gate intact. Built before any sends flow, because replies are where the meetings mandate actually lives.

**This tool never sends anything.** It classifies and drafts. Sending is Nathan, from Nathan's mailbox, after the copy-sharpener pass.

## Run

```bash
python3 reply_engine.py --reply "we just rolled out NICE last year" --contact "Jane Doe" --account elevancehealth.com
python3 reply_engine.py --reply "..." --output Humana_Objection_Response.md   # write the response doc
python3 reply_engine.py --list                                               # show the taxonomy
python3 test_reply_engine.py                                                 # checks
```

## How it works

1. **Classify** — keyword scoring against `config/reply_categories.json` (the 7 categories from `intradiem-objection-handler`: Bad Timing, We Have WFM, Built In-House RPA, Evaluating Competitor, No Budget, Send Info, Wait for October). Ties and no-hits route to `unclassified` for manual review; the engine never auto-drafts on a low-confidence match.
2. **Draft** — fills the category's template (Acknowledge → Insight Pivot → Soft CTA, 3-4 sentences, Nathan's voice, no em dashes, humility clause, verified-claims discipline).
3. **Checklist** — prints the SOP: sharpen → Nathan approves → send from Nathan → **flip `bdr_claimed` on the Contacts row** (send_ready drops READY → HOLD via the live formula, the cadence stops) → confirm same-company pause → log outcome to the closed-loop columns and `impact/outcomes.csv` → calendar the category's follow-up.

## Config over code

Everything a human would want to tune lives in `config/reply_categories.json`: trigger phrases, root causes, strategies, response templates, follow-up cadences, voice rules. `reply_engine.py` only knows how to score, fill, and print.

## The SOP in one line

Classify → draft → sharpen → Nathan approves → send from Nathan → claim the row (bdr_claimed=TRUE) → log the outcome → calendar the follow-up. See `SOP_Reply_Handling.md` for the full loop.

## Data swap points

None — this engine consumes reply text passed on the command line. When the Slack/mailbox bridge lands, pipe the reply body into `--reply` and nothing else changes.
