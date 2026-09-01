# Dry run for the Prototype Builder agent

Use this once after creating the agent, before any PM touches it. It repeats the run that produced `prototypes/holiday_calendar/` so the result is comparable.

1. Open the Prototype Builder agent, start a new chat.
2. Attach `prototypes/holiday_calendar/PRD_source.md`.
3. Paste this message exactly:

> Build the prototype for Screen 7, Holiday Calendar, from the attached PRD. Scope: Phase 1 Must requirements only (FR-HC-001 to FR-HC-006), United States only with two regions and four sites, year 2026 only, five acceptance checks. Draft the brief first, then build it in the same reply. Use the attached DS_Tokens.md for the design system. Width that matters: 1440. Keep the whole file under 20 KB.

If the reply still fails partway through, send a second message: "Build the calendar view and the scope tree only, under 12 KB. List and add flow go in the second pass." Then ask for the second pass as its own message.

4. Expected: a draft brief, one HTML artifact, and a handover in the order What works / Self-check result / Decisions I made / Not implemented / For the review.
5. Download the artifact, save it as `index.html`, double-click it, press **Checks**.

Report three things: whether the artifact downloaded as `.html`, whether the Checks button shows, and the `N pass, N fail, N manual` line. The reference run (a larger scope, built outside Greenlight) gave 6 pass, 1 fail, 1 manual first time and 7 pass, 0 fail, 1 manual after one fix message. With the scoped message above, expect a smaller file and five checks; the pass line is what matters, not the count:

> Check AC-6 fails: [paste the line from the Checks panel]. Fix that and keep everything else the same.
