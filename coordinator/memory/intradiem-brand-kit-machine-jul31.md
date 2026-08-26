---
name: intradiem-brand-kit-machine-jul31
description: The machine-readable Intradiem HTML brand kit (tokens, CSS, linter, assets) built Jul 31 2026 that resolves Rachel's rules into enforceable code
metadata:
  type: reference
---

Built Jul 31 2026 at `~/Desktop/Intradiem Deliverables/brand-kit/`. This is the enforceable form of [[rachel-brand-standard-jul31]]. Anything HTML, external, exec, or Naveen-facing should be generated against it and linted before it ships.

- `brand-tokens.json` : the ONLY place a brand value is defined. Ten hexes with roles, font stack, 13px type floor, 8px radius, section recipes, CTA spec, the two open questions for Rachel.
- `intradiem-brand.css` : generated from the tokens. Drop-in `:root` plus base layer, `.section-dark/.section-light/.section-callout/.section-brand`, `.btn-primary`. Never hand-type a hex again.
- `brand-check.py` : the linter. Strips base64 before analysis so it is safe on 800KB decks. Checks off-palette colour, accent-used-as-text, opacity-as-text, gray text, 13px floor, all-caps, letter-spacing, font stack, text-shadow, centred text, black backgrounds, radius, and decodes embedded logos to catch opaque white boxes. `--json` for machine use. Exit 1 on any error.
- `assets/brand-background.jpg` (2400px, 39KB, Rachel's own file) and `assets/intradiem-logo.png`.

Measured on the live deck at dwostoryqbr.netlify.app it returned 189 errors. On the rebuilt deck it returns 0 errors and 1 intentional warn.

**Resolutions this kit locks in, all sourced from Rachel's own attachment, not guessed:**
- Deep Green is `#228751`. Her email's `#22875` dropped a digit; the attachment states `#228751` in both the palette and the CSS reference.
- Intradiem Green is `#2CB56E`. Her attachment gives RGB 44, 181, 110 and 44 = `2C`, which confirms her hex and proves the Jul 30 kit's `#2DB56E` wrong.
- Orange `#F58220` is legitimate and is in her palette as the primary CTA fill. Melissa's "the orange looks off" was about `#FE5000`, an older red-orange still live in the deck. There was never a conflict to resolve, only a wrong hex to replace.
- Accent colours (`#2CB56E`, `#F58220`, `#A5CE38`, `#FDBE3E`) are never typeset. Her email permits green as text but her section table forbids it; the kit takes the stricter reading so it passes either.
- Reduced-opacity rgba is banned as a text colour, so all secondary text is solid white or `#363636`. Hierarchy comes from weight and size.
