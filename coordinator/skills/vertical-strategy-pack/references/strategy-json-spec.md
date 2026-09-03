# strategy.json spec + deliverable structures

## The single source of truth

All research lands in one `strategy.json`. The build script turns it into the .xlsx and .html; you write the messaging .md by hand from the same content. Keeping one JSON prevents the three deliverables drifting apart.

```json
{
  "title": "UK Utilities",
  "subtitle": "Meeting-booking strategy · researched July 2026 · Jack O'Hagan",
  "reframe": {
    "heading": "THE BIG REFRAME — [the one belief to flip]",
    "text": "2-4 sentences. The counterintuitive read that turns an apparent blocker into the reason to strike now."
  },
  "stats": [
    {"n": "5", "label": "Tier 1 accounts"},
    {"n": "9", "label": "Tier 2 accounts"},
    {"n": "3", "label": "Live M&A events"},
    {"n": "2", "label": "Displacement windows"}
  ],
  "tiers": [
    {
      "tier": 1,
      "name": "Tier 1 — Strike now",
      "tag": "live timing event, act this month",
      "accounts": [
        {
          "name": "Account Name",
          "badge": "NOW — contract expiring",
          "badge_type": "now",
          "meta": "est. 2,000–3,000 agents · part of X Group",
          "signal": "The dated, specific reason to act (1-2 sentences).",
          "targets": "Persona 1 · Persona 2 · Persona 3",
          "hook": "The one-sentence opening angle, written as you'd say it.",
          "play": "Channel + order + ask (2-3 sentences).",
          "warmnote": "optional — only for warm/prior contact",
          "est_agents": "2,000–3,000 (est.)",
          "org_status": "M&A / org context for the xlsx column",
          "timing": "NOW - this month",
          "warmth": "Cold / warm-ish detail for the xlsx column"
        }
      ]
    }
  ],
  "playbook": [
    {"icon": "&#128222;", "title": "Channel mix", "text": "..."},
    {"icon": "&#128101;", "title": "3×3 multi-threading", "text": "..."},
    {"icon": "&#127919;", "title": "The ask", "text": "..."},
    {"icon": "&#9876;", "title": "Displacement angles", "text": "..."},
    {"icon": "&#128197;", "title": "Sequencing", "text": "..."}
  ],
  "parked": [
    {"account": "Name", "reason": "Already in pipeline / too small / build in-house"}
  ],
  "footer": "Click any card for the full play. Internal use only."
}
```

`badge_type` values: `now` (red — live event), `soon` (amber — this quarter), `warm` (green — prior relationship), `nurture` (grey).

Tier definitions: **Tier 1** = live timing event (contract expiry, merger closing, site opening, leadership change) — strike this month. **Tier 2** = strong fit + signals but no deadline — active pursuit. **Tier 3** = qualify/nurture/park. Aim for 3–6 Tier 1, 5–10 Tier 2. Anything already in pipeline, under the 200-agent floor, or a known build-in-house shop goes in `parked` with the reason.

## Running the build

```bash
pip install openpyxl --break-system-packages   # once
python3 <skill>/scripts/build_pack.py strategy.json <output_dir>
```

Produces `<Title>_Meeting_Strategy.xlsx` (sheets: Strategy Tracker, Playbook, Removed - Parked) and `<Title>_Strategy_Map.html` (interactive tiered card map, cards expand on click). Open the HTML after building and check every card renders with a signal, hook and play — an empty hook means the JSON entry was incomplete.

## Messaging .md structure

Filename: `<Vertical>_Email_LinkedIn_Messaging.md`.

```markdown
# Outreach Messaging — [Vertical] (Tier 1 + Tier 2)
*Emails kept under ~110 words. Cadence suggestion: Email 1 → LinkedIn connect (day 2) →
Email 2 (day 4) → LinkedIn message (day 7) → Email 3 breakup (day 11). Phone the
planning personas between touches — they answer.*

---

## 1. [ACCOUNT] — ⭐ NAMED CONTACTS[, situational flag]
**Top N:** Name (Title — role tag) · Name (Title — role tag) · ...
**Fresh signals:** dated, specific, one line each.
**Routing:** who first, who same week, who lands last, and why.

### [Contact sequences per messaging-guide.md §3, one per named contact]

**Coordination note:** [per messaging-guide.md §7]

---

## [next account...]

---

## Usage notes
[The standing rules: personalise line 1, benchmark ask never demo, phone between
touches for planners, 3×3 multi-threading, swap in current approved stats.]
```

Where contacts aren't yet named, write the sequence against the title (e.g. "### Head of Resource Planning (name still needed — find via Lusha, phone-first once found)") with `{{firstName}}` placeholders, and flag the gap in the coordination note.
