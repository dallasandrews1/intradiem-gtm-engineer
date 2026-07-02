# Intradiem Brand Kit
### For all Intradiem-context deliverables — internal decks, ELT material, customer-facing work, and the tools you run on the job

> **Two-mode rule.** Use *this* kit for anything that represents Intradiem. Keep your personal blurple/creme (`dallas-brand`) only for personal thought-leadership and portfolio pieces. Reason: blurple reads as League-adjacent — on Intradiem work, their orange signals "one of us."
>
> **Source note.** Primary color `#FE5000` is confirmed from Intradiem's live site theme color. The neutrals, secondary, and fonts below are a tasteful, professional system built around it — confirm against the official brand guide once you're in, and I'll tighten it.

---

## The idea behind the palette

Intradiem's whole pitch is *acting in the moment* — real-time, decisive, energetic. The palette encodes that: a serious industrial **ink** for authority and structure, with a single high-energy **orange** as the spark of action. That's the whimsical-but-serious duality translated into Intradiem's world — disciplined dark + decisive orange. Orange is the *energy/action* color; never wallpaper, always the spark.

**Narrative arc:** dark **ink** cover that commands → warm **paper** interior that breathes → orange used sparingly for the moments that matter (the highlight, the number, the CTA).

---

## Color tokens

| Token | Hex | Role |
|---|---|---|
| Intradiem Orange | `#FE5000` | Primary accent — highlights, key numbers, links, CTAs, the spark. Use sparingly. |
| Orange Deep | `#D8400A` | Hover / pressed / darker accent |
| Orange Light | `#FF8A5C` | Highlighted phrases on dark, soft emphasis |
| Orange Tint | `#FFE9DF` | Accent backgrounds, pills, soft callout fills |
| Ink | `#14181F` | Authority — cover/header backgrounds, section bars |
| Ink-2 | `#2A323C` | Secondary dark, gradient partner, dividers on dark |
| Text | `#1B1F26` | Primary text on light |
| Paper | `#FAF8F6` | Warm page background |
| White | `#FFFFFF` | Cards, surfaces |
| Line | `#EFEBE6` / `#DED8D0` | Borders, card edges, table rules |
| Row Tint | `#FBF3EE` / `#F7E7DC` | Alternating table rows (warm) |
| Slate (secondary) | `#C24A12` | Deep-orange secondary for second data series / accents |
| Gray | `#5A5F66` | Supporting body text |

Semantic (keep separate from brand — for status only): green `#2f8f4e`, amber `#b5751a`, red `#c0392b`.

## Type
- **Headings / numbers / labels:** Outfit (700–800). Confident, modern, slightly geometric.
- **Body:** Inter or Lato (400/700).
- Confirm Intradiem's official typeface from the brand guide; Outfit/Inter is the safe stand-in.

## Do / Don't
- **Do** keep orange to ~10% of the surface — the highlight, not the field. Let ink + paper carry the weight.
- **Do** lead a multi-page piece with a dark ink cover, then go warm/light inside.
- **Don't** flood backgrounds with orange (it stops meaning "action" and starts shouting).
- **Don't** mix in blurple/League purples on Intradiem deliverables.
- **Don't** color status data orange — orange is brand, green/amber/red are status.

## Copy-paste CSS tokens

```css
:root{
  --orange:#FE5000; --orange-deep:#D8400A; --orange-light:#FF8A5C; --orange-tint:#FFE9DF;
  --ink:#14181F; --ink-2:#2A323C; --text:#1B1F26; --paper:#FAF8F6; --white:#FFFFFF;
  --line:#EFEBE6; --line-2:#DED8D0; --row:#FBF3EE; --row-2:#F7E7DC;
  --secondary:#C24A12; --gray:#5A5F66;
  --ok:#2f8f4e; --warn:#b5751a; --bad:#c0392b;
}
```

---

*Built June 2026 around Intradiem's confirmed primary `#FE5000`. Pair with the emotional/design philosophy of `dallas-brand` (dark→light arc, whitespace as a tool, 2–3 discovered details) applied to these colors. Refine fonts + secondary palette against the official brand guide once available.*
