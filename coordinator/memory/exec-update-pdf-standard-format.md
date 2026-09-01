---
name: exec-update-pdf-standard-format
description: "Standing output format for Naveen/John/exec-facing deliverables: a branded green-forward update-page PDF built from the value-repository-update template"
metadata:
  node_type: memory
  type: feedback
---

FEEDBACK (Jul 21 2026): when Dallas asks for something to be MADE for Naveen, John (CRO), or other leadership/exec, the default deliverable is a **branded update-page PDF**, not a plain text blurb.

**Why:** Dallas standardized on this after the Stars beta update to John. He wants exec-facing artifacts to look like a finished, on-brand page, matching the value repository update he liked.

**How to apply:**
- Use the official **Intradiem brand** (green-forward, per [[intradiem-brand-kit]] / dallas-brand two-mode rule), NOT personal blurple. Exec/external = Intradiem green.
- **ALWAYS add the Intradiem logo** (Jul 21 2026, standing rule from Dallas). Source lockup: `strike-room-kit/logo.svg` (pinwheel mark in gold/orange/lime/green + "intradiem" wordmark in forest `#014637`, with ® ). Inline the full SVG into a header `.brandbar` at top-left (height ~32px), with a forest bottom rule and an optional mono kicker (e.g. "GTM Engineering") right-aligned. Inline it, don't `<img src>` a relative path, so the HTML is self-contained and Chrome renders it into the PDF. This applies to every made deliverable, not just this one.
- Match the template at `04-value-repository/Value_Repository_Update_2026-07-21.html`: Playfair Display headings in forest `#16432C`, DM Sans body, JetBrains Mono uppercase eyebrows/labels, warm paper `#FAFBF7`, white cards with soft shadow, chips for status, orange `#FE5000` reserved for ONE spark (eyebrow + single hero number), a `.note` "Net:" block, quiet foot line.
- Metrics render as **stat tiles** (mono label + Playfair number + small descriptor), 3-up grid. This is the scannable "table" read leadership prefers.
- Build the `.html` in `exec-updates/` then render to PDF with headless Chrome:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="OUT.pdf" --no-margins "file://ABSOLUTE/PATH.html"`
- Screenshot-verify the render before delivering (`--screenshot`, read the PNG).
- **ACCESS (Jul 21 2026):** Dallas can't click chat links to files outside his primary workspace root. Standing rule: copy every finished deliverable into `~/Desktop/Intradiem Deliverables/` (`$HOME/Desktop/Intradiem Deliverables`, already created and pinned) so he has one durable place to find everything. Do this automatically on every deliverable, not just exec PDFs. He chose the pinned folder over auto-open / reveal-in-Finder, so default to copy-to-folder; don't auto-launch apps unless asked.
- Content still obeys house style: no em dashes, surfaced vs realized never blended, only verified figures read as verified, head-start framing, no UHG until MAC approval.

**No plumbing metrics in leadership deliverables (Jul 21 2026 lesson):** the first Stars PDF included a deliverability block with a "sender reputation 96%" stat. Naveen (the reader) had to ask "what is sender reputation?" and Dallas confirmed the number "isn't relevant" during warmup (it goes to ~100% when warm; it only matters later, as a number to PROTECT). Lesson: keep technical/ops metrics (sender reputation, bounce rate, warmup %, deliverability internals) OUT of exec/CRO deliverables. There is nobody to explain a one-way PDF, so a jargon metric reads as a question mark, and a mid-warmup number understates the real state. Use plain-language outcome only (e.g. "delivering cleanly from a warmed mailbox") if any reassurance is needed. Deliverability block was removed from the Stars update accordingly.

First instance: `exec-updates/StarRatings_Beta_Update_2026-07-21.pdf` (Stars campaign beta update for John, from Naveen). Note: Naveen later took the John email onto his own plate (bundling back-office), so the immediate send need shifted; the PDF stands as the reusable artifact.
