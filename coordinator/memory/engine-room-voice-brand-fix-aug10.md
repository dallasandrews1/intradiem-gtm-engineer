---
name: engine-room-voice-brand-fix-aug10
description: The Engine Room page read as AI-written and had drifted off the current brand kit; the specific tells and the palette fixes, reusable for any deliverable
metadata:
  type: feedback
---

10 Aug 2026. Dallas on the Engine Room page: *"this needs to read as me as if I created this, not like AI created it"* plus a prompt to re-check the brand kit. Both were right. What was actually wrong, worth reusing as a checklist.

## The AI tells that were in it

Not em dashes (already zero) and not jargon. Subtler things:

- **Zero contractions across the whole page.** This is the single biggest tell and it contradicts [[no-aiisms-house-style]], which says contractions are fine and good. Fixed copy went from 0 to 213.
- **Formal constructions everywhere**: "It is", "That is", "There is", "cannot", "does not", "is not". All driven to zero.
- **An aphorism at the end of nearly every paragraph.** Roughly 15 of them. Real writing doesn't land a perfect closing line every time. Cut to about four, spread out.
- **The "not X, it is Y" antithesis tic**, used eight times ("A motion is not a campaign. It is a universe...", "Not the output, the machinery").
- **Artifact narration**: "The point of this section is the denominator", "Below are four of those checks", "Everything else is scaffolding". Don't explain how to read the thing.
- **Intensifiers as filler**: deliberately, genuinely, precisely, exactly.
- **Uniform rhythm**: every section was assertive h2 + two-sentence dek + block. Vary it.

Check with: `grep -c "n't\|'s \|'re "` for contractions, and count "It is / That is / There is" occurrences before shipping.

## The brand drift

Page had four hand-picked greens that are in no token set: `#0d6a4e` and `#00382c` (body gradient stops), `#013a2e` (statband and steps panels), `#0a5843` (declared unused). It also declared `--lime:#A5CE3A` and `--yellow:#FDBF40`, which are **logo-icon-only colors** and don't belong in a deliverable palette, and used `--cream:#F4F1EA` from the superseded kit as primary text.

Fixes, per [[intradiem-brandkit-current-jul30]]:
- Hero glow is the kit's signature move, `radial-gradient(rgba(45,181,110,.30) ... )` over `#014637`, not hand-picked hex stops.
- Panel surfaces are `var(--forest)`, not a custom dark green.
- Text `#FFFFFF` on dark, mono labels on forest are `#9DBBAE`.
- Delete lime/yellow/forest-2 from `:root` entirely so they can't get used by accident.

This is the same anti-pattern the Jul 30 rebuild called out: "off-token green shades picked by hand." Grep any new deliverable for hex values that aren't in the token list before shipping.

Related: [[engine-room-deliverable-aug7]], [[deliverable-strength-framing]], [[dallas-voice-professional-vs-personal]].
