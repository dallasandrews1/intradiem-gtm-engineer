---
name: intradiem-content-engine
description: Content repurposing engine. Turns one source asset (webinar, customer story, podcast, long-form blog, conference talk, analyst report) into a full multi-channel content set — blog post, LinkedIn carousel + single posts, a 3-touch nurture sequence, a sales one-pager, and social pull-quotes — all on-brand and consistent. Trigger on "repurpose this", "turn this into content", "spin up content from [asset]", "make a content set from this webinar/story", "I need a campaign out of this", or any moment a single piece of source material needs to become a coordinated content drop for Marketing. Built for the GTM Engineer to give Marketing volume and consistency from one input.
---

# Intradiem Content Engine

## Why this exists
Marketing's two constant pains are volume and consistency. One strong source asset
usually dies after a single use. This skill multiplies it: one input becomes a
coordinated, on-brand content set across every channel, with a single message spine
so nothing drifts. It is the fastest way for the GTM Engineer to make Marketing's
output go further without more headcount.

## Inputs (ask for anything missing before running)
- **Source asset** — file, transcript, link, or pasted text (required)
- **Primary audience** — front-office (contact-center / CX) leaders, back-office /
  operations leaders (claims, lending, billing, fulfillment), or WFM leaders, plus the
  vertical (Healthcare / Financial Services / Insurance / Retail / Telecom / Utilities).
  Intradiem = Dynamic Workforce Orchestration across the whole workforce, not just call
  centers — pick the use case that fits the audience.
- **Campaign goal** — awareness, demand-gen, event promo, or sales enablement
- **Optional** — target channels, length limits, any claim/legal constraints

## Pipeline

### 1. Extract the message spine
Read the source asset and pull:
- One **core thesis** (one sentence the whole set ladders up to)
- 3-5 **supporting points** worth their own piece
- Any **quotable lines** or customer language verbatim
- Every **stat or claim** — route each through `intradiem-verified-metrics`. Never
  invent or paraphrase a number into something stronger than the source. Flag
  anything unverified as `[VERIFY]`.

### 2. Map spine → channels
Decide which supporting points become which assets. Keep the thesis identical across
all of them; only the format and depth change.

### 3. Produce the content set (all of the below)

**A) Blog post** — 600-900 words, the thesis fully argued, one verified proof point,
clear takeaway. SEO-aware headline + meta description.

**B) LinkedIn**
- One carousel outline (6-8 slides, one idea per slide, strong hook slide)
- Two standalone single posts (different angles on the thesis, <1,300 chars each)

**C) 3-touch nurture sequence** — email 1 (problem/hook) → email 2 (proof) → email 3
(soft CTA). Subject line options for each.

**D) Sales one-pager outline** — the same thesis reframed for a rep to hand a
prospect: the problem, the shift, the proof point, the next step.

**E) Social pull-quotes** — 3-5 short quotable lines drawn from the source (verbatim
where possible).

## Constraints
- Single message spine — the thesis must be identical across every asset.
- Apply Dallas's brand voice and Intradiem brand guidance where those skills exist.
- Every stat verified or flagged `[VERIFY]`. No claim stronger than its source.
- Tone: clear, peer-level, no hype.

## Verification step (run before finishing)
Self-check and report:
1. All five asset types present.
2. Thesis is identical across the set (no drift).
3. Every stat verified or flagged.
4. Each asset honors its length limit.
5. Headlines/hooks pass a "would this stop the scroll" read.

## Trigger phrases
"repurpose this", "turn this into content", "make a content set from [asset]",
"spin up a campaign from this webinar/story", "give Marketing a content drop from this".
