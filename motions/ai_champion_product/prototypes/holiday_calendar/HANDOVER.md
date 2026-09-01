# Handover: Holiday Calendar prototype (Screen 7)

Download `index.html` and save it as `index.html`. Double-click it to open. The brief is in `Prototype_Brief_HolidayCalendar.md`.

## What works

- Global shell: 256px sidebar with five nav items, site/team selector in the top bar (mirrors the scope tree), timezone indicator for the selected scope, notification badge with a popover that clears the count when opened.
- Scope tree: 5 countries, 12 regions, 16 sites with agent counts; selecting any node recomposes the calendar with inheritance (site inherits region inherits country) and shows the breadcrumb and totals.
- Year selector: 2026 and 2027, with recurring days regenerated per year (fixed dates, nth weekday, last weekday, Easter-relative, Monday-on-or-before, plus observed substitutes for the US, UK and Canada).
- Calendar view: one month at a time with previous and next, chips colour-coded by tier, overridden days shown dashed and struck through, legend; selecting a day opens the add dialog with that date filled in.
- List view: date, name, type, tier and scope, status, action; sortable by date, name and tier from the column headers, with direction toggle.
- Search as you type on name; tier checkboxes hide or show country, region and site entries in both views.
- Add non-working day: name, date, type (company closure, training day, public holiday), repeat every year; validation; then the impact step (agents, intervals, sites, per-site table); nothing is saved until "Add and recalculate".
- Overrides: "Work this day" on any inherited or own day, "Restore" at the scope that set the override, "Remove" on days added in this session; each goes through the same impact step first.
- Recalculation: after confirm, a toast reports the background task and a notification lands 1.5 seconds later with the agent and interval counts.
- Toast, Escape to close dialogs and popovers, focus returns to the control that opened a dialog.
- Self-check panel: "Checks" button bottom-right and the ? key, summary line in `#sc-summary`, `window.__selfcheck()` returns the results, re-run every time the panel opens. Badge bottom-left reads "Prototype built from PRD-Intradiem-Scheduling-Service v1.0 (March 2026), Screen 7".

## Self-check result

7 pass, 0 fail, 1 manual (expected; not run here, this cold run had no browser).

Each computed check (AC-1 to AC-7) is expected to pass at 1440 and 1920. None of the seven is hard-coded: AC-1 composes Phoenix, AZ and applies a scratch override; AC-2 compares 12 generated dates against known 2026 and 2027 dates; AC-3 adds, re-selects, and removes a test entry through the real save path; AC-4 re-sorts the rendered list and compares legend chip styles; AC-5 previews and walks the add dialog to the impact step; AC-6 measures buttons, sidebar, rows and scans every element's computed colours; AC-7 measures overflow, scans visible text and audits every control for a bound action.

Manual check:

- AC-8 (keyboard-only add flow): Tab to "Add non-working day", Enter, type a name and a date, Tab to "Review impact", Enter, Tab to "Add and recalculate", Enter. Under a minute.

## Decisions I made

1. Brief section headings. The instructions say the brief has nine sections and name only 6 (acceptance checks), 7 (open questions), 8 (decisions) and 9 (out of scope). I used: 1 Feature and source, 2 Who uses it and what they need to do, 3 Screen, controls and data, 4 Widths and environment, 5 Design system.
2. Scope: Phase 1 Must requirements only (FR-HC-001 to FR-HC-006). FR-HC-007 (Should, Phase 1+) and FR-HC-008 (Could, Phase 2) are not built.
3. Design system: the attached DS_Tokens.md, not the PRD's Harmoniq Scheduler system (NFR-U-001), per the instruction that an attached sheet wins. No Inter font.
4. Tier colour coding from DS tokens only: Country = primary tint fill with a primary left border, Region = primary dark fill with white text, Site = white fill with a secondary-text border, Worked (overridden) = dashed secondary-text border with strikethrough.
5. Overrides apply to every loaded year, and only the scope that set an override can restore it; a site sees "Set at US West" rather than a Restore button.
6. Impact model: agents = headcount at the sites whose calendar actually changes (computed as the before/after difference); intervals = agents x 32 (15-minute intervals over an 8-hour scheduled day); weekend dates counted the same as weekdays.
7. Years loaded: 2026 and 2027. Month navigation crosses year boundaries inside that range and stops at the edges with a toast.
8. Substitute-day rules: United States Saturday to Friday and Sunday to Monday; United Kingdom and Canada Saturday or Sunday to the next free weekday; none applied for the Philippines and India.
9. Pre-loaded public holidays cannot be removed, only marked as worked. "Remove" exists only for days added in the session.
10. Default state: scope Phoenix, AZ (so inheritance and a region override are visible on first load), January 2026, calendar view. The add dialog defaults to "Company closure"; the tier of a new day is the selected scope, so the dialog shows it rather than asking again.
11. Calendar view shows one month at a time rather than a full year.
12. Sidebar items outside Screen 7 show a toast saying the screen is not in this prototype; the active item resets the screen to its defaults. That was the least dishonest way to satisfy "never ship a button that does nothing" without inventing other screens.
13. Primary buttons are white text on `#5AB274` as the DS specifies, which is below the 4.5:1 contrast the instructions ask for. I followed the DS. Elsewhere I kept secondary text off the `#F8F8F8` page background so every other text pairing clears 4.5:1.
14. Mock data stands in for a multi-country back-office footprint of the kind Intradiem's enterprise customers run (a large payer or bank): 16 sites in the United States (Atlanta, Tampa, Richmond, Dallas, Omaha, Phoenix, Salt Lake City), United Kingdom (Leeds, Manchester, Glasgow), Canada (Toronto, Montreal), Philippines (Quezon City, Taguig) and India (Bengaluru, Hyderabad), 11,600 agents. Public holidays are real 2026 dates per country and region; England and Scotland differ (Easter Monday, summer bank holiday, 2 January, St Andrew's Day), Ontario and Quebec differ (Family Day, Civic Holiday, Saint-Jean-Baptiste), Karnataka and Telangana differ (Kannada Rajyotsava, Telangana Formation Day). Holi and Diwali are one-off provider-dated entries because they are lunar. Canada's Remembrance Day is left out because Ontario and Quebec do not observe it as a statutory day. Company closures and training days (Day after Thanksgiving, US West regional training day, Dallas and Bengaluru training days, Leeds office move, Quezon City building maintenance, Phoenix all-hands) are invented but typical.
15. The pre-existing override "US West works Columbus Day" is seeded so the review can see an inherited override without creating one.

## Not implemented

- FR-HC-007 half-day holidays with start and end times: Should, Phase 1+, not in the Phase 1 MVP.
- FR-HC-008 religious and cultural observance overlays and agent self-selection: Could, Phase 2, and it depends on Screen 12.
- Configuring the holiday data provider (FR-HC-002 says "configurable"): no provider settings screen; provider data is pre-loaded.
- NFR-P-005 at 100,000 agents: recalculation is simulated as a 1.5-second background task with a notification, not measured.
- NFR-D-001 UTC storage and conversion: the timezone indicator shows the site's zone, but dates are calendar dates with no time component.
- Role-based access (FR-SV-011 and section 4 roles): everyone is the WFM Systems Admin.
- Other screens in the shell (Schedules, Shift patterns, Leave, Settings): sidebar items exist but do not open screens.
- Mobile widths: NFR-U-002 applies those to agent self-service, not planner views.

## For the review

1. Can a site restore a day that its region marked as worked, or does the override live only at the tier that set it?
2. Does an override apply to every year or only to the selected year?
3. Which holiday data provider, and does it also supply each country's substitute-day rules (Saturday to Friday in the US, next weekday in the UK and Canada)?
4. For "intervals affected", is the count based on agents actually rostered that day, or headcount multiplied by intervals per day? What is the interval granularity?
5. Should the calendar view show one month at a time or the whole year?
6. How many future years does the recurrence engine generate?
7. Who may add at the Country tier: WFM Systems Admin only, or Regional WFM Manager as well?
8. The PRD names the Harmoniq Scheduler design system (NFR-U-001) but the attached token sheet is the Intradiem DS v1. Which one is right for Screen 7?

## Fix 1

Reported: AC-6 failed with "non-token colours: input text rgb(0, 0, 0)".

Cause: the checkbox inputs (the three tier filters and "Repeats every year") took the browser's default text colour. The DS colour rule covered text, date and search inputs and selects, but not checkboxes.

Change: one CSS rule added, `input,select,button{color:var(--text)}`, so every form control carries the DS text token. Nothing else in the file changed; mock data, layout and checks are identical.

Self-check line expected after the fix: 7 pass, 0 fail, 1 manual (expected, not run here).
