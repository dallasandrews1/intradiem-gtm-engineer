# Prototype brief: Holiday Calendar (Screen 7)

Drafted from PRD-Intradiem-Scheduling-Service v1.0 (March 2026, Draft, Internal), sections 5.2, 5.4, 6 and 7. Sections 1, 2, 3 and 6 are filled in the PM's words from the PRD. Section 7 lists what the PRD does not settle. Sections 8 and 9 are the PM's to fill; 8 is left as "Not held".

## 1. Feature and source

Holiday Calendar, Screen 7 of the Scheduling Service. Multi-level calendar system for public holidays, company closures, and site-specific non-working days. Goal G3: multi-level holiday calendar management (country to region to site) with automatic schedule impact analysis. Phase 1 MVP. Source: PRD-Intradiem-Scheduling-Service v1.0, section 5.2 (FR-HC-001 to FR-HC-008), plus the global shell requirement FR-SV-011.

## 2. Who uses it and what they need to do

- WFM Systems Admin (3 to 5 per enterprise, full admin): configures holiday calendars as part of configuration work alongside the shift pattern library, role permissions and integrations.
- Schedule Planner (50 to 100 per enterprise): sees which days are non-working before creating and publishing schedules.
- Regional WFM Manager (5 to 10 per enterprise, read, approve, override): reviews multi-site calendars and site-level exceptions.

They need to see, for any country, region or site, which days are non-working and where each day comes from; add company-specific non-working days at any tier; override an inherited day locally; and see the schedule impact (agents and intervals affected) before committing a change.

## 3. Screen, controls and data

One screen inside the global shell (FR-SV-011: persistent sidebar navigation, site/team selector, timezone indicator, notification badge).

Controls on Screen 7, from the PRD:

- Scope tree: Country, Region, Site, with inheritance (site inherits region, region inherits country) and local overrides (FR-HC-001).
- Year selector: pre-loaded public holiday data for every country where the customer operates, from a holiday data provider (FR-HC-002); recurring annual holidays, fixed date and floating date (for example 3rd Monday of January), generated for future years (FR-HC-003).
- Add non-working day: company-specific days (annual company shutdown, training days) at any tier (FR-HC-004).
- Calendar view, colour-coded by tier, and list view sortable by date, name or tier (FR-HC-005).
- Impact before commit: when a holiday is added or removed, show the number of agents and intervals affected before committing; recalculation runs as a background task (FR-HC-006, NFR-P-005).
- Search and tier filters on both views.

Data: a five-country footprint (United States, United Kingdom, Canada, Philippines, India), 12 regions, 16 sites, 11,600 agents, with real 2026 public holidays per country and region and a handful of company closures and training days.

## 4. Widths and environment

1920 and 1440 wide (PM's message; the PRD's NFR-U-002 says planner views are optimised for 1920x1080 minimum). Opens by double-click as a single HTML file, no setup.

## 5. Design system

The attached DS_Tokens.md (DS v1 per the Skills Editor PRD v2.0, May 2026). It takes precedence over the PRD's NFR-U-001 reference to the Harmoniq Scheduler design system (Inter, #1B3A5C), per the project instructions: the attached sheet wins.

## 6. Acceptance checks

| Id | Check | Verified by |
|---|---|---|
| AC-1 | Selecting a site shows its own days plus the days inherited from its region and country, each labelled with the tier it comes from; a day overridden at a region is worked at every site under it while the country still observes it (FR-HC-001). | Computed in the prototype: composes Phoenix, AZ and counts entries per tier; applies a scratch override at US Central and checks Dallas, TX and Omaha, NE against United States and Atlanta, GA. |
| AC-2 | Public holidays for 2026 are pre-loaded for every configured country, and recurring days regenerate on their correct 2027 dates, including floating dates and observed substitutes (FR-HC-002, FR-HC-003). | Computed: 12 known dates across both years (MLK Day, Good Friday, Thanksgiving, Victoria Day, UK Boxing Day substitute, US Independence Day observed, National Heroes Day) plus a minimum of three provider holidays per country per year. |
| AC-3 | A non-working day added at any tier is saved and is still there after switching to another scope and back (FR-HC-004). | Computed: adds a test entry at the current scope through the save path, switches to another country and back, confirms it is still composed, then removes it. |
| AC-4 | The calendar view colour-codes days by tier, and the list view sorts by date, name and tier (FR-HC-005). | Computed: three distinct tier chip styles in the legend; list re-sorted by each key and the rendered order verified. |
| AC-5 | Before a day is added or removed, the impact shows the number of agents and intervals affected, and nothing changes until it is confirmed (FR-HC-006). | Computed: previews an add at the current scope, checks agents and intervals are finite and consistent, walks the add dialog to the impact step and confirms the saved data is unchanged. |
| AC-6 | Chrome follows the attached DS tokens: buttons 36px tall with 4px radius, sidebar 256px, list rows 48px, and only token colours appear on screen. | Computed: measures every visible button, the sidebar and every list row; scans computed background, text, border, outline and SVG fill colours of every element against the token list. |
| AC-7 | The screen works at 1440 and 1920 wide: no horizontal scrollbar, no broken value text on screen, and every control has a handler. | Computed at the current window width (the detail line names the width and reminds you to resize to the other): page and list overflow, a scan of visible text for broken values, and a check that every button, select and input is bound to an action. |
| AC-8 | The add flow can be completed with the keyboard only (assumed from the source, NFR-U-004). | Manual: Tab to "Add non-working day", Enter, type a name and a date, Tab to "Review impact", Enter, Tab to "Add and recalculate", Enter. Under a minute. |

## 7. Open questions

1. Can a site restore a day that its region marked as worked, or does the override live only at the tier that set it?
2. Does an override apply to every year or only to the selected year?
3. Which holiday data provider, and does it also supply each country's substitute-day rules (Saturday to Friday in the US, next weekday in the UK and Canada)?
4. For "intervals affected", is the count based on agents actually rostered that day, or headcount multiplied by intervals per day? What is the interval granularity?
5. Should the calendar view show one month at a time or the whole year?
6. How many future years does the recurrence engine generate?
7. Who may add at the Country tier: WFM Systems Admin only, or Regional WFM Manager as well?
8. The PRD names the Harmoniq Scheduler design system (NFR-U-001) but the attached token sheet is the Intradiem DS v1. Which one is right for Screen 7?

## 8. Decisions

Not held.

## 9. Out of scope

- FR-HC-007 half-day holidays (Should, Phase 1+).
- FR-HC-008 religious and cultural observance overlays (Could, Phase 2), and Screen 12 Agent Self-Service.
- Configuring the holiday data provider itself (FR-HC-002 names it configurable; no settings screen in this prototype).
- Role-based permissions, UTC storage and display conversion (NFR-D-001), the 100,000-agent recalculation at scale (NFR-P-005 is simulated as a short background task).
- Every other screen in the shell (Schedules, Shift patterns, Leave, Settings): the sidebar items exist so the shell reads as the PRD describes, but they do not open other screens.
- Mobile widths (NFR-U-002 applies those to agent self-service, not planner views).
