# Intradiem Scheduling Service PRD, v1.0 (excerpt attached by the PM)

Source: SharePoint engineering / Aldus Documents / Proof of Concepts / Aldus Modules Proof of Concepts / Intradiem Scheduling System (on top of core) / PRD-Intradiem-Scheduling-Service.docx. Status Draft, Version 1.0, March 2026, Author Intradiem Product and Engineering, Classification Internal, Product Review. Depends on Scheduling Core Microservice and ISM Skills Module. UI spec: Figma AI Screen Mockups (22 screens). The PM attached the parts relevant to Screen 7.

## 1. Executive summary
The Scheduling Service is the planner-facing module that enables enterprise WFM teams to set up, manage, and publish workforce schedules for 100,000+ back-office staff across multiple sites, time zones, and lines of business. It sits on top of the Scheduling Core Microservice (the domain-agnostic calendar engine), consumes skill data from the Intradiem Skills Manager (ISM), and feeds planned queue assignments to the Agent-to-Queue Allocation Service.

## 2. Scope (in scope, relevant lines)
- Holiday calendar management per country, region, and site
- Settings and administration (time zones, DST rules, interval granularity, role-based access)

Phase 1 MVP (months 1 to 6) includes holiday calendars. Phase 1+ (months 6 to 9) fast-follow. Phase 2 (months 9 to 15) differentiators.

## 3. Goals (relevant)
G3: Implement multi-level holiday calendar management (country to region to site) with automatic schedule impact analysis.

## 4. User roles (relevant)
| Role | Primary use | Access | Scale |
|---|---|---|---|
| WFM Systems Admin | Configuration: shift pattern library, holiday calendars, role permissions, integrations | Full admin | 3 to 5 per enterprise |
| Schedule Planner | Day-to-day schedule creation, shift assignment, leave approval, publication | Full edit, publish, approve | 50 to 100 per enterprise |
| Regional WFM Manager | Multi-site schedule review, planner oversight, capacity gap analysis | Read, approve, override | 5 to 10 per enterprise |

## 5.2 Holiday Calendar Management
Multi-level calendar system for public holidays, company closures, and site-specific non-working days.

| ID | Requirement | Priority | Phase | Screen | Depends on |
|---|---|---|---|---|---|
| FR-HC-001 | System shall support a three-tier holiday calendar hierarchy: Country, Region, Site, with inheritance (site inherits region, region inherits country) and local overrides | Must | 1 | Screen 7: Holiday Calendar | Scheduling Core (layered composition) |
| FR-HC-002 | System shall provide pre-loaded public holiday data for all countries where the customer operates, sourced from a configurable holiday data provider | Must | 1 | Screen 7 | |
| FR-HC-003 | System shall support recurring annual holidays (fixed date and floating date, e.g. 3rd Monday of January) with automatic future-year generation | Must | 1 | Screen 7 | Scheduling Core (recurrence engine) |
| FR-HC-004 | System shall allow administrators to add company-specific non-working days (e.g. annual company shutdown, training days) at any tier | Must | 1 | Screen 7 | |
| FR-HC-005 | System shall display a visual calendar view with colour-coded holidays by tier and a list view sortable by date, name, or tier | Must | 1 | Screen 7 | |
| FR-HC-006 | System shall recalculate all affected schedules when a holiday is added or removed, showing the impact (number of agents/intervals affected) before committing | Must | 1 | Screen 7 | Scheduling Core (layered composition) |
| FR-HC-007 | System shall support half-day holidays (e.g. Christmas Eve afternoon) with configurable start/end times | Should | 1+ | Screen 7 | |
| FR-HC-008 | System shall support religious/cultural observance calendars as an optional overlay that agents can self-select | Could | 2 | Screen 7, Screen 12: Agent Self-Service | |

## 5.4 Schedule views (relevant)
FR-SV-011: System shall provide a global shell with persistent sidebar navigation, site/team selector, timezone indicator, and notification badge across all views (Must, Phase 1, Screen 1: Global Shell).

## 6. Non-functional requirements (relevant)
- NFR-P-005: Holiday calendar recalculation (100K agents) completes in 60 seconds or less as a background task.
- NFR-U-001: Design system: all screens must conform to the Harmoniq Scheduler design system (Primary #1B3A5C, Secondary #2E75B6, Accent #4CAF50, Font: Inter). 100% design system compliance.
- NFR-U-002: Responsive layout: planner views optimised for 1920x1080 minimum; agent self-service responsive down to 375px mobile width.
- NFR-U-003: WCAG 2.1 Level AA for all screens.
- NFR-U-004: Keyboard navigation: all critical planner workflows completable via keyboard.
- NFR-D-001: All schedule timestamps stored in UTC; display conversion based on site/user timezone configuration.

## 7. UI screen map (relevant row)
| # | Screen | Source | Area | Key requirements |
|---|---|---|---|---|
| 7 | Holiday Calendar | Main Spec | Holiday Calendars | FR-HC-001 to FR-HC-008 |

## 10.1 Related documents (relevant)
WFM Schedule Planner Figma AI Spec (14 screen prompts, Harmoniq Scheduler design system); HarmoniqScheduler Prototype (HTML), interactive browser-based prototype with 6 screens. Neither is attached.
