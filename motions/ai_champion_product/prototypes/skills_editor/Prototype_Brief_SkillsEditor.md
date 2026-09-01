# Prototype brief: Skills Editor (worked example)

Filled in from the Skills Editor PRD (PRD-ICC-S2-001 v2.0, May 2026, SharePoint engineering/Aldus Documents/Proof of Concepts) to show what the one-page brief looks like when the source is an existing PRD. Sections 7 and 8 are what the PM would fill in; they are left as the questions the PRD leaves open, not as decisions anyone has made.

**Feature:** Harmoniq Skills Editor (S2), multi-dimensional competency management
**PM:** Product, Skills Intelligence (as named in the PRD)
**Date:** brief drafted Aug 31 2026 from a May 2026 PRD
**Prototype link:** `prototypes/skills_editor/index.html`

## 1. The decision this prototype settles
Whether a manager can view and update one agent's skills across Process, Case and Business Object dimensions, compare them to a role template, and save, inside a three-panel layout that still works at 1280px.

## 2. Who uses it and what they are doing
A team manager in claims or member services, in the middle of a staffing change, checking one agent's competency profile against the role template and fixing gaps before work is routed to them.

## 3. What the prototype does
- Left panel: agent roster with live search, LOB and role filters, a three-segment health bar per agent
- Centre: dimension tabs (Process / Case / Business Object) with inline level editing; Process has a skill tree and Quick Add typeahead; Business Object has a class panel (System Objects, Insurance Products)
- Right: Compare to Template with Met / Below / Missing / Extra groups
- Save writes the in-memory diff to the store and confirms with a toast; switching agent without saving discards

## 4. Data it shows
Mock agents, skills, business objects, insurance product classes and graded role templates that imitate the stores named in the PRD (AGENTS, ALL_SKILLS_FLAT, CASE_SKILLS, BIZOBJ_SKILLS, PRODUCT_CATALOG, GRADED_TEMPLATES). Sarah Chen (claims-specialist-g2) is constructed so all four compare categories render and Missing shows Part-D and Medicaid, as AC-04 requires.

## 5. Design system
Intradiem DS v1 as specified in PRD section 2: primary #5AB274, dark #158235, backgrounds #F8F8F8, borders #E5E5E5, Open Sans with Roboto for labels and selects, 36px / 4px buttons, 5px cards, 2px dialogs, 48px table rows, inline SVG icons, no emoji in chrome.

## 6. Acceptance checks
| # | Check | Pass condition | Verified by |
|---|-------|----------------|-------------|
| AC-01 | DS colours | sidebar #F8F8F8, primary buttons #5AB274, active tab underline #5AB274, no #014637 or #2DB56E in chrome | prototype |
| AC-02 | No emoji in chrome | nav icons are inline SVG | manual |
| AC-03 | BO tab renders | any agent shows System Objects and insurance classes, counts above 0 | prototype |
| AC-04 | Compare to Template | all four categories for Sarah Chen; Missing includes Part-D and Medicaid | prototype |
| AC-05 | Process skills named | activity column never shows "undefined" | prototype |
| AC-06 | Save persists | after Save, reselecting the agent shows the updated levels | prototype |
| AC-07 | Responsive | three panels reflow at 1280px; no horizontal overflow at 1080px and above | prototype |
| AC-08 | Button spec | 36px height, 4px radius, 700 14px, letter-spacing .03em | prototype |

## 7. Open questions for the review (left open; the PRD does not settle them)
- Does the Compare to Template panel belong beside the editor, or as a step before Save?
- At 1280px the right panel drops under the centre; is that acceptable for managers on laptops?
- Should Quick Add insert at level 1 or ask for a level?

## 8. Decision record
Not held. No review has taken place on this prototype.

## 9. Out of scope
Batch updates across agents, approval workflow, historical timeline, mobile, API persistence (PRD section 11).
