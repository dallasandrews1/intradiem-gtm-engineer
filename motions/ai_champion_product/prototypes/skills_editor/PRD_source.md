# Source: Intradiem Harmoniq, Skills Editor PRD (PRD-ICC-S2-001 v2.0, May 2026, Product, Skills Intelligence)

Transcribed from SharePoint: engineering/Aldus Documents/Proof of Concepts/Aldus Modules Proof of Concepts/Intradiem Skills Editor/Skills-Editor-PRD.docx (Status: Approved, Design Compliant). Used as the worked example for the PM as a builder program: the same PRD, rendered as a working prototype.

## 1. Overview
Skills Editor (S2) is the primary workspace for managers to view and update individual agent competency profiles across three skill dimensions: Process (LOB hierarchy), Case (clinical / specialty), and Business Object (system records and insurance products). Real-time comparison against role templates, contextual gap analysis, and a save-confirm workflow.

## 2. Design system compliance (v2.0)
- Colors: primary #5AB274, dark #158235 (hover/emphasis), page background #F8F8F8, borders #E5E5E5, secondary text #757575
- Typography: Open Sans primary, Roboto for labels and selects (14 to 16px)
- Sidebar: light #F8F8F8 with 1px #E5E5E5 right border (replaces dark green sidebar)
- Buttons: 36px height, 4px radius, #5AB274 fill, white text, 700 weight, 14px, letter-spacing 0.03em
- Inputs/selects: 4px radius, 1px rgba(0,0,0,0.23) border, Roboto
- Cards: 5px radius, shadow 0 4px 10px rgba(0,0,0,0.1)
- Dialogs: 2px radius, shadow 0 19px 38px rgba(0,0,0,0.3)
- Tables: #F8F8F8 header rows, #E5E5E5 dividers, 48px row height
- No emoji in navigation or UI chrome; inline SVG icons (24x24, filled Material style)

Token table: --id-green #5AB274 (was #2DB56E); --id-dark-green #158235 (was #014637); --id-radius 5px (was 8px); --id-radius-sm 4px; --id-radius-dialog 2px; --id-bg #F8F8F8; --id-border #E5E5E5; --id-text2 #757575.

## 3. Screen layout
Three-panel layout inside the main content area; shared 256px sidebar.
- Left panel 252px: agent roster with search/filter and per-agent health summary
- Centre panel flex-1: active skill dimension (Process / Case / Business Object) with inline level editor
- Right panel 268px: Compare to Template, a diff view (met, below target, missing, extra)
Dimension tabs (Process, Case, Business Object) above the centre panel; active tab uses a #5AB274 underline. Collapses to two panels below 1280px.

## 4. Skill dimensions
- 4.1 Process: hierarchical Line of Business > Service > Process > Activity. Activities carry level 1 to 5 (Awareness to Expert). Skill tree in the left column of the centre panel plus a Quick Add typeahead.
- 4.2 Case: flat list of clinical/specialty certifications (cs-* ids), each with a group (Medical, Surgical, Behavioral, Pediatric, Diagnostic), description, level 1 to 5.
- 4.3 Business Object: two sub-categories selected via a class panel inside the BO tab. System Objects (bo-* ids: Claim Record, Auth Record, EOB, ERA, Member Record, etc.), level 1 to 5 via inline select. Insurance Products (po-cat:* classes and po:* product types: Medicare, Medicaid, Commercial, Behavioral Health, Pharmacy) with class-level proficiency plus product types inside each class.

## 5. Left panel, agent roster
- Search input filters by name in real time (DS border, 4px radius)
- Filter selects: LOB and role (Roboto 11px, 4px radius)
- Agent row: avatar + name + role + 3-segment skill health bar (Process / Case / BO coverage, green/amber/red by gap count), 40px row height
- Active state: background rgba(90,178,116,0.12), left border 3px #5AB274

## 6. Right panel, Compare to Template
Reads GRADED_TEMPLATES keyed by agent.roleId. Four categories:
- Met: #E8F5EE border, green text, agent level meets or exceeds
- Below: #FEF3E2 border, amber text, has skill but below required level
- Missing: #FEF0ED border, red text, required, agent has none
- Extra: #F4F6F8 border, grey text, agent has skill not required
Each diff item shows skill name, agent level, required level. Header shows the resolved template name; empty state "no template assigned".

## 7. Save workflow
Changes held in currentAgentSkills (in-memory diff). Save button in the topbar writes back to the AGENTS store. Toast (#333 background) confirms. Selecting a different agent without saving discards (resets to stored values).

## 8. Role template alignment
GRADED_TEMPLATES entry: id (roleId, e.g. claims-specialist-g2), label (e.g. Senior Claims Specialist, Grade 2), skills (flat skillId to required level across all three dimensions).

## 9. Data model
AGENTS {id, name, role, roleId, template, skills{}}; ALL_SKILLS_FLAT {id, act, lob, svc, proc, level}; CASE_SKILLS {id, name, icon, group, cert, desc}; BIZOBJ_SKILLS {id, name, icon, cat, desc}; PRODUCT_CATALOG {id, category, icon, products[]}; GRADED_TEMPLATES {id, label, grade, family, description, skills{}}.

## 10. Acceptance criteria
- AC-01 DS colours: sidebar #F8F8F8; primary buttons #5AB274; active tabs #5AB274 underline; no #014637 or #2DB56E in visible chrome
- AC-02 No emoji in chrome: nav icons inline SVG only (emoji allowed in data icons, not structural UI)
- AC-03 BO tab renders: selecting any agent shows System Objects + insurance class list; counts > 0 for test agents
- AC-04 Compare to Template works: all four categories render for Sarah Chen (claims-specialist-g2); missing: Part-D, Medicaid
- AC-05 Process skills named: activity column shows act name, never "undefined"
- AC-06 Save persists: after Save, reselecting the same agent shows updated levels
- AC-07 Responsive: three-panel shell reflows at 1280px; no horizontal overflow at 1080px and above
- AC-08 Button DS spec: primary buttons 36px, 4px radius, Open Sans 700 14px, letter-spacing 0.03em

## 11. Out of scope (v2.0)
Batch updates across agents; approval workflow; historical skill timeline; mobile/tablet; API-backed persistence (in-memory store).
