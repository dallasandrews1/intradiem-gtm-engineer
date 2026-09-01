# Dry run for the Prototype Builder agent

Use this once after creating the agent, before any PM touches it. It repeats the run that produced `prototypes/holiday_calendar/` so the result is comparable.

1. Open the Prototype Builder agent, start a new chat.
2. Attach `prototypes/holiday_calendar/PRD_source.md`.
3. Paste this message exactly:

> Build the prototype for Screen 7, Holiday Calendar, from the attached PRD. Draft the brief first and show it to me before building. Use the attached DS_Tokens.md for the design system. Widths that matter: 1920 and 1440. Build it.

4. Expected: a draft brief, one HTML artifact, and a handover in the order What works / Self-check result / Decisions I made / Not implemented / For the review.
5. Download the artifact, save it as `index.html`, double-click it, press **Checks**.

Report three things: whether the artifact downloaded as `.html`, whether the Checks button shows, and the `N pass, N fail, N manual` line. The reference run gave 6 pass, 1 fail, 1 manual first time and 7 pass, 0 fail, 1 manual after one fix message:

> Check AC-6 fails: [paste the line from the Checks panel]. Fix that and keep everything else the same.
