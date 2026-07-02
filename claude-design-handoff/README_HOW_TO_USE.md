# How to use this handoff in Claude Design

**Goal:** build a single-page showcase site — your mirror of Naveen's onboarding site — that explains and demos everything you have ready, works live as a presentation, and self-explains if you just share the link.

## Steps
1. Open **Claude.ai** → start a **new Project** (or use the artifact builder / "Claude Design").
2. Upload all six files in this folder as **project knowledge**:
   - `00_BUILD_PROMPT.md` ← the master instructions
   - `01_CONTENT_sections.md` ← the actual copy/data per section
   - `02_BRAND_intradiem.md` ← colors, type, feel
   - `03_VERIFIED_METRICS_and_integrity_rules.md` ← **the number-labeling rules (most important)**
   - `04_REFERENCE_naveen_site_IA.md` ← the structure to mirror
   - `05_INVENTORY_whats_ready.md` ← the full "everything ready" index
3. In the chat, paste the **contents of `00_BUILD_PROMPT.md`** as your first message (even though it's attached — pasting it makes it the active instruction). Add one line: *"Build it now as a single self-contained index.html. Use the attached files for all facts and copy."*
4. Let it build, then iterate: *"open Presenter mode by default for my walkthrough"*, *"tighten section 03"*, *"make the integrity chips more prominent"*, etc.
5. When happy, download the `index.html`. To publish: drag it onto **Netlify Drop** (app.netlify.com/drop) for an instant shareable link, exactly like Naveen's.

## The one thing to watch
Every number must carry its chip — **VERIFIED** (green) / **DRY-RUN** (amber) / **TARGET** (neutral). If you see a bare engine number that looks like real pipeline, send it back: *"that's seeded — chip it DRY-RUN."* This protects you: no one can ever say you presented seeded data as real results.

## Tone reminder
Partnership, not parallel-system flex. The site is *"strong thinking I prepared to accelerate us — let's shape the targets together,"* matching Naveen's "rough sketch" framing. Confident on the engineering, humble on the numbers.
