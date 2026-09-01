---
name: product-ai-goals-build-aug31
description: "Aug 31 2026: the three open Product (Dallas) goals on the Monday AI Initiatives board built as far as they go without Product input: PM as a builder kit (brief template, pm-prototype skill, Skills Editor PRD rendered as a self-checking prototype), pmo-action-extractor agent (read-only, weekdays 7:25, validation queue for accuracy), BOO sales kit as an interactive page from the Jun 2 Product deck; Monday % updates staged for Dallas, not written"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1164f90f-c0cb-4597-b831-24abf3f2ed45
  modified: 2026-09-01T01:09:10.941Z
---

Monday board 18418380280 (AI Initiatives, Operational Excellence), group "Product (Dallas)". Items: 12664076586 AI enabled prospecting (Done 100%), 12664083282 AI enabled prototyping / PM as a builder (In Progress 0%, Q3), 12664120782 AI enabled PMO (Not Started 0%, Q4), 12746065434 Interactive sales enablement (In Progress 25%, Q3). Columns: status, numeric_mm4e2yjb (% Complete), text_mm5he7hz (Status Notes).

Built Aug 31 2026 in `motions/ai_champion_product/` (worktree branch agents/vs-code-agents-window-usage):
- Page system templates `_tpl/` (base.css, fonts_head.html with embedded Roboto, logo_symbol.html, present.js) and `build_pages.py --check` (fails on em dashes and leftover placeholders). Pages: `BOO_Sales_Kit.html`, `PM_Builder_Program.html`, `AI_PMO_Extractor.html`.
- PM as a builder: `Prototype_Brief_Template.md`, skill `~/.claude/skills/pm-prototype`, worked example `prototypes/skills_editor/index.html` from the Skills Editor PRD v2.0 (SharePoint engineering/Aldus Documents/Proof of Concepts; 78 KB, all 8 ACs computed and passing). No cohort, no PM named; those are Product's.
- AI PMO: agent `~/.claude/agents/pmo-action-extractor.md`, wrapper `automation/run_pmo_action_extractor.sh`, plist `com.dallasandrews.gtm.pmoextractor` (weekdays 7:25), outputs `automation/pmo/action_register.csv` + `validation_queue.csv` (verdicts: correct, wrong_owner, wrong_date, not_an_action, duplicate), log family `pmo-actions`, rundown source 12. Proof run covers Dallas's own records only. Dallas graded 20 rows on Aug 31 2026 with `automation/pmo/grade.py`: precision 95% (19 correct, 1 wrong_date; all Otter and all high-confidence rows correct). 65 rows still ungraded.
- Sales enablement: `BOO_Sales_Kit.html` transcribed from "Back Office Optimizer Early Stage Enablement.pptx" (Product, SharePoint productmanagement/GTM/Sales Enablement/Back Office Optimizer/Training, Jun 2 2026); ROI calculator reproduces the deck's $748K example (overstaffing line interpreted as 2% of buffer headcount cost, flagged on page). Skill `~/.claude/skills/intradiem-interactive-enablement`. Next decks in the same folder: Queue Optimizer deck (beta) sales kit, BOO customer-facing Presentation.pptx.

**Why:** Dallas asked (Aug 31) for everything on the three goals that can be finished without the Product team, and then said: never hallucinate or assume, say plainly what needs Product. So every page carries an "Open with Product" section and no invented calendars, rosters, or accuracy numbers.

**How to apply:** Monday % complete and Status Notes were NOT written by the agent; Dallas sets them (staged prompt in the Aug 31 session). Dallas approved the deploys the same evening: live at boo-sales-kit.pages.dev, pm-builder.pages.dev (prototype under /prototype), ai-pmo-7yo.pages.dev (noindex, Pages projects boo-sales-kit, pm-builder, ai-pmo; deploy folders in ~/Desktop/Intradiem Deliverables/). Before sending to Naveen the PMO page was scrubbed to Dallas-owned sample rows with no colleague names or past-due items, and the DM line about what he needs from Product was dropped as too demanding. Related: [[ai-champion-product-role-aug17]], [[html-deliverable-standard]], [[feedback-no-showy-deliverable-copy]].
