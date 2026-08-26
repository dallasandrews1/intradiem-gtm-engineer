---
name: lemlist-sharpener-applied-aug6
description: Aug 6 2026 lemlist copy-sharpener fixes 1-5 applied to all 5 draft campaigns; what remains open before launch
metadata: 
  node_type: memory
  type: project
  originSessionId: 568c8f8e-c684-4803-8629-8a31b3eae733
  modified: 2026-08-06T16:38:42.206Z
---

On Aug 6 2026 the copy-sharpener fixes (1-5 from `Intradiem GTM Engineer/Lemlist_Copy_Sharpener_Review_Aug6.md`) were applied to lemlist: 27 step updates across all 5 draft campaigns (UK Airlines, UK Insurance/FS, Stars Finance, Stars Quality, Stars Resurrection). Includes the "eating my words" Resurrection breakup rewrite (subject changed on those 2 steps) and the fix-7 "only reason I'm calling" call-script line, both explicitly approved by Dallas. A/B-tested steps and all other subject lines were deliberately left untouched.

Still open before launch: £680 FOS case-fee verification against the 2026/27 fee schedule (launch-blocker), Scotland five-year claim-window caveat check for the airline pool, fix 7 Clay-side variable-seam checks, and the sharpener pass on the Clay MessageGen prompts (opener_line, vm_hook, contract_line, voice_script).

Architecture decision, same session: per-prospect message generation stays in Clay MessageGen (full enrichment context, one canonical prompt library, QA gates); lemlist stays delivery/sequencing/A-B only, fixed template copy lives in lemlist. All 5 campaigns have zero lemlist AI-variable prompts and that is intentional.
