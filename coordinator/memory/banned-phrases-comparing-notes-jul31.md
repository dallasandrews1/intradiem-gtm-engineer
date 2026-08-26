---
name: banned-phrases-comparing-notes-jul31
description: Jul 31 corrections - "comparing notes" is a banned phrase in all outreach copy, connection requests always go blank (no note), and voice notes open with first and last name only, never the company
metadata:
  type: feedback
---

Dallas, Jul 31 2026, reviewing the lemlist standard build: caught "comparing notes" in email 1 and banned it ("you need to be following our standards all the way"), and separately ruled "never add a message to a connect request. always send without a note."

**Why:** Claude swapped the approved house CTA for an invented phrase while chasing an interest-CTA strategy, which is exactly the drift the copy-sharpener exists to prevent. The house CTA form ("thought it might be worth [topic]. Have 15 min in the next few weeks?") already IS the soft interest CTA; no new phrasing was needed. And an invite note is a pitch surface that lowers accept rates and burns the blank-slate advantage; the sharpener's own rule ("connection requests always go blank") was in the skill all along and Claude built noted invites anyway.

**How to apply:** (1) "comparing notes" / "compare notes" never appears in any prospect-facing copy, any channel. (2) Every LinkedIn connection request in every campaign is note-less; in lemlist, an invite's note cannot be cleared by updating with an empty string (the API silently drops it and the old note stays, verified live Jul 31), so a noted invite must be DELETED and re-added with no message parameter. (3) Run the full [[intradiem-copy-sharpener]] guardrail list on EVERY piece of copy Claude writes, including variable values and call/voicemail/voice-note scripts, not just email bodies; the same sweep also caught the forbidden "leverage/lever" family and voice notes naming Intradiem (voice notes open "it's Nathan Belfield", first and last name, no company, per the spoken-word standard). Related: [[natural-cta-supersedes-onboarding-sample]], [[lemlist-standard-sequence-jul31]].
