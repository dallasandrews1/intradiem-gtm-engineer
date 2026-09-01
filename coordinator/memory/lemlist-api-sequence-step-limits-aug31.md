---
name: lemlist-api-sequence-step-limits-aug31
description: Aug 31 2026 - lemlist API adds linkedinVoiceNote steps only on a root sequence (refused inside a condition branch), refuses step deletion once leads are reviewed, title max 100 chars; two labeled STRAY steps remain in Stars - Resurrection (Nate) for Dallas to delete in the UI; AI voice step and script are in the Aug 31 UI sheet
metadata:
  type: project
---

Aug 31 2026, while adding an AI voice step to lemlist "Stars - Resurrection (Nate)" (`cam_sh3JCJoxtEHyjGrsw`):

- `POST /api/sequences/{seqId}/steps` with `type: linkedinVoiceNote, recordMode: ai` works on the ROOT sequence but returns "You are not allowed to add a step to this sequence" on a condition-branch child sequence (a `manual` step on the same child is accepted). Voice notes need the accepted-invite branch, so the placement must be done in the UI.
- `DELETE /api/sequences/{seqId}/steps/{stepId}` returns "You can't remove steps because you already reviewed some leads" once leads sit in review state, even with the campaign in Draft/paused. Probe steps are therefore permanent via API. Rule: never create a test step on a campaign that holds leads; probe on an empty draft campaign instead.
- Step `title` max 100 characters (API error "Title can't be longer than 100 characters").
- `PATCH /api/sequences/{seqId}/steps/{stepId}` works for message, delay, title, recordMode (type must be repeated and cannot change).

State left behind: two steps titled "STRAY STEP from an API test (Dallas): delete this step, it does nothing" (stp_MPXXucbkXwjkiiJSP at the end of the Yes path, stp_6eBfPTm3Y92XNT363 at the end of the root). The day 1 DM was reverted to its original copy so nothing references a voice note before it exists. Sheet with the voice script, delete steps, and the on-go DM prompt: `motions/star_ratings/Stars_Resurrection_AI_Voice_UISheet_Aug31.md`. Jason Jones (AI security, Slack U0608L8HG3C) kept AI voice out of the initial pilot; on Aug 31 an exception ask with guardrails was drafted into Dallas's Slack DM with Jason (not sent by Claude); Jason's reply is the launch gate for the voice step. A bulk lead pull-out/reload route to finish the sequence surgery by API exists; single-lead removals now run through the allow-listed helper ~/.local/bin/lemlist-lead-remove (43 calls would be needed), still only on Dallas's explicit go. The Slack tool rule: unreviewed outward messages go out as drafts, not sends.

Related: [[lemlist-linkedin-backfill-pattern-aug31]], [[feedback-no-guessed-ui-steps]].
