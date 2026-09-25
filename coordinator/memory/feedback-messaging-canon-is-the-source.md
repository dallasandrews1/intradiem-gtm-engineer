---
name: feedback-messaging-canon-is-the-source
description: Sep 25 2026 - talk tracks, angles and the AE-facing POV decided in messaging conversations are recorded in motions/shared/messaging_canon.json and every room, kit and draft reads the current entry
metadata:
  type: feedback
---

Dallas, Sep 25 2026: "we need to be remembering the talk tracks and angles we decide on in these messaging conversations like we did with marketing earlier, and ensure that our verbiage or suggestions etc in these rooms reflects the most up to date iterations of the best form of messaging we can be sending to prospects and the POV we are presenting to AEs."

**Why:** angles were being decided in Slack DMs, calls and review passes and then re-derived per build, so a room could carry an older idea than the one agreed last week, and the AE-facing reasoning behind a line lived nowhere.

**How to apply:** the canon lives at motions/shared/messaging_canon.json (rendered to messaging_canon.md by messaging_canon.py; never hand-edit the md). Every entry has an angle, a talk track, a written line, the POV for AEs, who decided it, when and where, and what it supersedes. A new decision is a new entry that supersedes the old one, never an edit of history. Colleague proposals (Naveen's Stars closer, Sep 25) stay "proposed" until Dallas decides. Builders reference canon ids in KIT["canon"]; check_messaging_canon.py flags a room carrying a superseded or unbacked angle. The first-draft engine and copy sharpener read the canon before drafting. Related: [[ae-package-review-rules-sep25]], [[feedback-deliver-the-send-version]], [[stars-messaging-authored-in-claude-code]].
