---
name: feedback-open-items-are-not-blockers
description: "Sep 22 2026: don't let remaining follow-ups read as blockers on a deliverable that is already ready; say what ships now and put the rest under a separate heading"
metadata:
  type: feedback
---

Dallas, Sep 22 2026, after the BCBS of Michigan and Vanguard strike rooms were finished: "Can't we just send these strike plans as-is? speed is most important here at this point."

Nothing was actually blocking. The rooms were complete, the copy was QC'd, eleven addresses were ZeroBounce valid, both gates passed. What I had done was end several messages on a "what's left" list, which made a finished deliverable read like a draft waiting on dependencies. The BCBS NC handle-time number was the clearest case: the copy was deliberately written to work without it, and I still closed on it twice as though it held the send.

**Why:** a list of open items at the end of a handoff sets the reader's last impression. If the work is ready, leading with what is missing costs real days on something that could have gone out the same hour. Dallas moves fast and reads a trailing to-do list as a gate.

**How to apply:** when a deliverable is done, say it is done and hand it over in the same message. Open items go under their own heading, after the handover, each one labelled with what it actually changes, for example "changes one sentence, does not hold the send" or "holds the load." Never end a handoff on the open items. If something genuinely does block, say the word blocked and say what it blocks, so the word keeps its meaning. Related: [[deliverable-strength-framing]], [[feedback-deliver-the-send-version]], [[answer-length-keep-it-short]].

Practical note from the same session: Slack canvas creation (`slack_create_canvas`) returned Internal Server Error on three attempts across an hour, so it is not a reliable delivery path right now. The working route for rep-facing documents is markdown source, `motions/shared/md_to_page.py` to branded HTML, then headless Chrome to PDF (`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer --print-to-pdf`), because PDFs preview inline in Slack. `slack_send_message_draft` stages the message in the channel for Dallas to attach files and send himself.
