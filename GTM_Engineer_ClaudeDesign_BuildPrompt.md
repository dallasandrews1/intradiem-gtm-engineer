# Claude Design — Build Prompt
### How to use this file
1. Open **Claude Design** (Anthropic Labs → Claude Design; research preview on Pro/Max/Team/Enterprise).
2. Start a new design and **upload `GTM_Engineer_Operating_System.docx`** (the content source).
3. **Paste everything below the line** as your first message.
4. Refine with inline comments / sliders, then export to **HTML** (and/or PDF).

---

Build an interactive, single-page web document from the uploaded Word file (`GTM_Engineer_Operating_System.docx`). Use the document's text as the source of truth for all content — do not invent new facts. The result should feel like a premium SaaS product page (think Linear / Stripe / Notion), not a slide deck or a generated template.

## Brand system (use exactly)
- **Fonts:** Outfit (headings, numbers, labels) + Lato (body). Load from Google Fonts.
- **Palette:**
  - Deep blurple `#250D53` — cover/header background, section accents
  - Blurple text `#19063A` — primary headings/body on light
  - Blurple mid `#501CD2` — numbers, links, accents, active states
  - Warm creme `#F9F7F6` — page background
  - Lilac `#ECEAF1` / `#D9D6E5` — card + table fills, borders
  - Seafoam `#B8D6D8` / `#4E6B6D` — thin accent stripe, eyebrow labels, "discovered detail" touches
  - Periwinkle `#F3F5FF` / `#E1E7FE` — alternating table rows
  - Gray `#666666` — supporting body text
- **Narrative arc:** dark, commanding header (deep blurple, thin seafoam→blurple gradient stripe at top) → warm creme interior that breathes. Generous whitespace. Bold AND warm. Whimsical-but-serious: every choice deliberate, with 2–3 small details that reward a second look.

## Header
- Eyebrow: `GTM ENGINEERING · OPERATING SYSTEM`
- Title: **Turn Salesforce + Slack into a self-running deal-intelligence machine.** (color the phrase "self-running deal-intelligence machine" in a lighter blurple)
- Subhead: the one-line method description from the doc.
- Three meta pills: `Dallas Andrews · GTM Engineer` · `Intradiem · Day 1: July 6, 2026` · `Stack: Salesforce + Slack`

## Required interactivity (this is the point — make it genuinely interactive)
1. **Two top-level tabs** the user clicks to switch views:
   - **Tab A — "The Method"**: the thesis + architectural-conviction callout, the 7-move Operating Loop, the four-layer architecture table, and the two "prompt is the product" rules.
   - **Tab B — "Day-1 Application"**: the Day 1→Week 1 timeline, the Day-1 diagnostic kit (3 columns: Stack & Gap, Foundation, Hygiene & Access), and the operating beliefs.
2. **The 7 moves are click-to-expand cards.** Collapsed = number + title + one-line tagline. Expanded = the full description from the doc. Smooth expand/collapse. Big blurple number tile on each.
3. **The Day-1 timeline items are checkable.** Each step (Day 1, Days 2–3, Days 4–5, Throughout) has a checkbox; checking it dims/strikes the step so it reads as a live progress tracker. Show a small "X of 4 complete" counter.
4. **The diagnostic questions are checkable too** (so it doubles as a walk-in checklist).
5. The four-layer table uses alternating periwinkle/white rows and a seafoam left-border accent on the first column.

## Footer
Confident, centered, deep-blurple band: title · "Extracted from builds shipped at League · Tool-agnostic, anchored on Salesforce + Slack" · "Dallas Andrews // GTM Engineer, Intradiem // Day 1: July 6, 2026".

## Constraints
- Single self-contained file (inline CSS/JS). No external data calls.
- Must be print-clean (a clean PDF export with no orphaned headings or huge whitespace gaps).
- No emojis. No dead space. Skimmable: a reader should absorb the structure without reading every word.
