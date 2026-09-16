---
name: league-brand-audit
description: >
  Programmatic brand compliance auditor for League documents. Runs any PPTX, DOCX, or HTML
  file through the League design token system and produces a compliance scorecard with specific
  violations, off-brand colors, font issues, and actionable fixes. Trigger on: audit this deck,
  check brand compliance, run a brand audit, is this on-brand, check this document, brand check,
  compliance check, token audit. Also trigger proactively when a user has just finished creating
  a PPTX or DOCX deliverable — offer to audit it before they share it. Load this skill alongside
  league-brand-assistant for the full brand compliance workflow.
---

# League Brand Compliance Auditor

This skill programmatically audits any League document against the official design token system. It catches the subtle drift that human review misses — hex values that are 2 steps off, font names registered wrong, bold weights that render as 700 instead of 600.

## When to Use

- After generating any PPTX, DOCX, or PDF deliverable
- When reviewing a document someone else created
- When a user asks "is this on-brand?" or "check this deck"
- Proactively: after any skill produces a visual deliverable, offer to audit it

## How It Works

The audit reads the document programmatically and checks every element against `league-design-tokens.json`. It produces:

1. **Compliance scores** — color, font, and size compliance as percentages
2. **Specific violations** — every off-brand element with its slide/page number, the wrong value, and the correct token
3. **Near-misses** — colors within 5 hex steps of an approved token (likely drift, not intentional)
4. **Actionable fixes** — exactly what to change to reach 100%

## Running the Audit

### For PPTX files

Use python-pptx to extract all colors, fonts, and sizes from every run, shape fill, and background:

```python
from pptx import Presentation
from pptx.util import Pt
import json

# Load tokens
with open("league-design-tokens.json") as f:
    tokens = json.load(f)

# Build approved color set from tokens
approved = {}
for name, t in tokens["color"]["primary"].items():
    approved[t["value"].upper()] = f"primary.{name}"
for family, shades in tokens["color"]["secondary"].items():
    for shade, t in shades.items():
        approved[t["value"].upper()] = f"secondary.{family}.{shade}"

prs = Presentation("target.pptx")

for slide_num, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    # CHECK: Font must be "Outfit" (not "Outfit SemiBold", not system fonts)
                    # CHECK: font.bold must be False (semibold handled by embedding script)
                    # CHECK: font.size >= 8pt
                    # CHECK: text color must be in approved set
                    pass
        # CHECK: shape fills against approved colors
        # CHECK: background fills against approved colors
```

### For DOCX files

Use python-docx to extract fonts, colors, and styles from every run and paragraph:

```python
from docx import Document

doc = Document("target.docx")
for para in doc.paragraphs:
    for run in para.runs:
        # CHECK: run.font.name == "Outfit"
        # CHECK: run.font.size >= Pt(8)
        # CHECK: run.font.color.rgb in approved set
        pass
```

### Color Distance Check

For colors not in the approved set, calculate hex distance to find near-misses:

```python
def hex_distance(c1, c2):
    r1, g1, b1 = int(c1[1:3],16), int(c1[3:5],16), int(c1[5:7],16)
    r2, g2, b2 = int(c2[1:3],16), int(c2[3:5],16), int(c2[5:7],16)
    return ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5

# If distance < 15, it's likely drift from an approved color
# Flag as "near-miss" and recommend normalizing to the closest token
```

## Output Format

```
BRAND COMPLIANCE AUDIT — [filename]
═══════════════════════════════════

SCORES
  Color compliance:  XX% (N of M uses on-brand)
  Font compliance:   XX% (N of M runs using Outfit)
  Size compliance:   XX% (all sizes >= 8pt: YES/NO)

VIOLATIONS
  [Slide/Page N] Font "Arial" on heading → Should be "Outfit"
  [Slide/Page N] Color #1A0940 on shape fill → Nearest token: blurple-deep #19063A (distance: 4.2)
  [Slide/Page N] Bold=True on run → Should be Bold=False + embed script for Semibold 600

NEAR-MISSES (drift from approved tokens)
  #1A0940 (6 uses) → normalize to #19063A (blurple-deep)
  #180A3D (4 uses) → normalize to #19063A (blurple-deep)

RESTRICTION CHECKS
  [PASS/FAIL] Teal #00C29B used only in logo
  [PASS/FAIL] #501CD2 not used as background
  [PASS/FAIL] Secondary palette not used for text
  [PASS/FAIL] Lilac 450 #8479A9 used only for eyebrow text
  [PASS/FAIL] No decorative separator lines
  [PASS/FAIL] No italic as decoration

FIXES TO REACH 100%
  1. [specific fix]
  2. [specific fix]
```

## Token Reference

The audit reads from `league-design-tokens.json` located in the `league-design-system/` directory. This file contains:

- 7 primary color tokens with usage rules and restrictions
- 10 secondary color tokens across Lilac, Seafoam, and Periwinkle families
- 9 semantic tokens for intent-based color decisions
- Typography specs (Outfit only, weights 400/600, minimum 8pt)
- Implementation rules per output type (PPTX, DOCX, HTML)

When the Figma Genesis integration goes live, the token file auto-updates and the audit automatically uses the new values. Zero changes needed to this skill.

## Important Notes

- The "Outfit SemiBold" font name issue is a python-pptx artifact. The correct approach is `font.name = "Outfit"` with `font.bold = False`, then run the embedding script. Flag "Outfit SemiBold" as a violation with the specific fix.
- Near-miss colors (hex distance < 15 from an approved token) are almost always unintentional drift. Recommend normalizing rather than flagging as a hard violation.
- Bold=True renders as weight 700 in most contexts. The League spec caps at Semibold 600. Always flag Bold=True with the embedding script fix.
