# Intradiem Brand Kit
### For all Intradiem-context deliverables — internal decks, ELT material, customer-facing work, and the tools you run on the job

> ## SUPERSEDED, 2026-07-30. DO NOT USE THIS KIT FOR NEW WORK.
>
> This is the older green / Playfair Display / DM Sans kit, taken from Naveen's onboarding
> site. It is kept only as history. **The current standard for every Intradiem deliverable is
> the Roboto system**: `--forest:#014637`, `--green:#2DB56E`, `--green-300:#7BD3A0`, with
> `--orange:#F58220` as the action accent only, plus the official inline SVG logo mark.
>
> Canonical spec: `~/coordinator/memory/intradiem-brandkit-current-jul30.md`.
> Reference implementations: `dwo-html-deck/` in this repo. Summary: the `## Brand` section
> of `CLAUDE.md`.
>
> `#FE5000` below is retired and must not appear in new work.


> The official Intradiem system is **green-forward** — forest and green carry the structure, with orange as a single, sparing secondary spark. Fonts are Playfair Display, DM Sans, and JetBrains Mono. Use the tokens below for anything that represents Intradiem.
>
> **Two-mode rule.** Use *this* kit for anything that represents Intradiem. Keep your personal blurple/creme (`dallas-brand`) only for personal thought-leadership and portfolio pieces — blurple reads as League-adjacent, and on Intradiem work you want their green/orange to signal "one of us."

---

## The idea behind the palette

Intradiem's pitch is *acting in the moment* — real-time, decisive. The palette encodes that with a serious **forest green** for authority and structure, a brighter **green/lime** for growth and momentum, and a single high-energy **orange** kept for the one moment that matters (the spark of action). Green carries the weight; orange is the strike, never the field.

**Narrative arc:** deep **forest** cover/header that commands → warm **paper** interior that breathes → green for structure and progress → orange used sparingly for the single highlight, number, or CTA.

---

## Color tokens

| Token | Hex | Role |
|---|---|---|
| Forest | `#16432C` | Primary authority — hero/header/footer backgrounds, section bars, dark cards |
| Green | `#1F7340` | Structure — headings on light, borders, primary accents |
| Green Bright | `#25B56F` | Progress, positive motion, gradient partner |
| Lime | `#B6D94C` | Highlight-on-dark, eyebrow labels, priority pills, accent stripe |
| Ink | `#15231B` | Primary text on light |
| Ink Soft | `#3E4D44` | Secondary text |
| Dim | `#7A877E` | Muted/meta text |
| Paper | `#FAFBF7` | Warm page background |
| Card | `#FFFFFF` | Cards, surfaces |
| Mist | `#F0F4ED` / `#E7EEE3` | Soft fills, alternating rows, callout backgrounds |
| Line | `#E2E7DD` / `#D4DCCE` | Borders, card edges, table rules |
| Spark (Orange) | `#FE5000` | **Secondary accent only** — the single highlight, key CTA, "spark of action" kicker. Use sparingly (~5% of the surface). |
| Gold | `#E0A23B` | Warm secondary accent, soft-warning fills |

Semantic (status only, keep separate from brand): green `#2f8f4e`, amber `#9a6313`, red `#9B2C2C`.

## Type

- **Headings / display:** Playfair Display (600–900). Serif, editorial, confident.
- **Body / UI:** DM Sans (400–700).
- **Labels / kickers / code / numbers:** JetBrains Mono (400–700), uppercase with wide letter-spacing for eyebrows.

Google Fonts import:
```
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
```

## Do / Don't

- **Do** let forest + green carry the structure; reserve orange for the one thing you want the eye to land on.
- **Do** lead a multi-page piece with a forest cover, then go warm/light inside.
- **Do** use JetBrains Mono uppercase for small labels/eyebrows — it's the system's signature.
- **Don't** flood the page with orange. Orange is the spark, not the brand field.
- **Don't** use Outfit/Inter — Playfair + DM Sans is the pairing.
- **Don't** mix in blurple/League purples on Intradiem deliverables.
- **Don't** color status data orange — orange is a brand spark, green/amber/red are status.

## Copy-paste CSS tokens

```css
:root{
  --forest:#16432C; --green:#1F7340; --green-bright:#25B56F; --lime:#B6D94C;
  --ink:#15231B; --ink-soft:#3E4D44; --dim:#7A877E;
  --paper:#FAFBF7; --card:#FFFFFF; --mist:#F0F4ED; --mist-2:#E7EEE3;
  --line:#E2E7DD; --line-2:#D4DCCE;
  --spark:#FE5000; --gold:#E0A23B;
  --ok:#2f8f4e; --ok-bg:#E7EEE3; --amber:#9a6313; --amber-bg:#FBF1E1; --red:#9B2C2C; --red-bg:#F9EAEA;
  --ff-head:'Playfair Display',serif; --ff-body:'DM Sans',system-ui,sans-serif; --ff-label:'JetBrains Mono',monospace;
}
```

---

*Source: the official Intradiem system, matching Naveen's onboarding site and the live token set in `Start_Here_Index.html`. Pair with the emotional/design philosophy of `dallas-brand` (dark→light arc, whitespace as a tool, 2–3 discovered details) applied to these green tokens.*
