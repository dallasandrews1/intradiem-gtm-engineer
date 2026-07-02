# BRAND — Intradiem design system (use this, not League blurple)

**Arc:** dark **ink** hero that commands → warm **paper** interior that breathes → **orange** as the spark only on the highlight / key number / CTA (~10% of surface; never wallpaper). This encodes Intradiem's pitch — acting in the moment: disciplined dark + decisive orange.

## CSS tokens (copy in)
```css
:root{
  --orange:#FE5000; --orange-deep:#D8400A; --orange-light:#FF8A5C; --orange-tint:#FFE9DF;
  --ink:#14181F; --ink-2:#2A323C; --text:#1B1F26; --paper:#FAF8F6; --white:#FFFFFF;
  --line:#EFEBE6; --line-2:#DED8D0; --row:#FBF3EE; --row-2:#F7E7DC;
  --secondary:#C24A12; --gray:#5A5F66;
  --ok:#2f8f4e; --warn:#b5751a; --bad:#c0392b;   /* STATUS ONLY — never orange */
}
```
Integrity-chip colors: VERIFIED = `--ok` green · DRY-RUN = `--warn` amber · TARGET = `--gray`/`--ink-2` neutral · LIVE = `--orange`.

## Type
- Headings / numbers / labels: **Outfit** 700–800 (confident, geometric).
- Body: **Inter** 400/600.
- One Google Fonts link allowed: `Outfit:wght@600;700;800` + `Inter:wght@400;500;600`.

## Do / Don't
- **Do** lead with a dark ink hero, then go warm/light inside. Keep orange to the highlight, the number, the CTA.
- **Do** use generous whitespace — airy, scannable, never cramped. Every element earns its place.
- **Don't** flood backgrounds with orange. **Don't** color status data orange. **Don't** use any League blurple/purple — on Intradiem work their orange signals "one of us."

## Feel (Dallas's brand soul — "whimsical-but-serious")
Hold two energies at once: **inventive** (someone who sees what others miss — unexpected accent, elegant contrast, handcrafted not templated) AND **engineered** (every choice deliberate, clean hierarchy, disciplined). The result should feel designed by someone who works at an AI company, not generated. Target descriptors: whimsical, light, warm, airy, clean, impactful, rememberable, confident, modern, scannable, purposeful, professional. If it reads as a default template, it has failed.

*Source: Intradiem primary `#FE5000` confirmed from their live site; neutrals/fonts are a tasteful professional system — confirm against the official brand guide once available.*
