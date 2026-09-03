---
name: feedback-plain-spoken-lemlist-spacing
description: "Sep 3 2026 rule - outreach copy must pass the \"would a person say this out loud\" test, no writerly filler; lemlist emails need explicit blank-line paragraphs (<p><br></p>) or they render bunched"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 864a99bb-87d2-49b7-8d95-dcb3da162f63
  modified: 2026-09-03T17:45:29.693Z
---

Sep 3 2026, Dallas on the first rewrite of Nate's campaigns: "you're still using unnecessary filler words that wouldn't be said by an actual person speaking. 'the scoring window has kept closing since, which is the only reason I'm back.' what does that even mean? 'In one line, in case the first note didn't land' is not natural at all. also, the formatting is wrong in the emails regarding the spacing of the lines etc it's all bunched together."

**Why:** the doctrine's plain-spoken rule was in the skill but I still wrote clever transitions. Every line has to survive being read aloud on a phone call. And lemlist's editor renders bare `<p>` tags with zero margin, so a body built as `<p>a</p><p>b</p>` shows as one block.

**How to apply:**
- Before pushing any email, read each sentence aloud in the rep's voice. Cut anything a person would not say: "in one line", "in case the first note didn't land", "which is the only reason", "the ground between", "the seam I work", "I'm easy to find", "eating my words", "the cheapest version of it". Prefer "Quick version:", "One thing I didn't say clearly", "reach out", "I'll stop here".
- Email HTML for lemlist: `<p>para</p><p><br></p><p>para</p>`, salutation on its own line, blank line before the sign-off. The `P()` helper in `motions/star_ratings/nate_rewrite_sep3.py` does this.
- Preview on a real lead after pushing and look at the paragraph breaks, not just the variables.
Related: [[nate-campaign-rewrite-sep3]], [[messaging-doctrine-sep3]].
