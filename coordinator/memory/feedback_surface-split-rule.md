---
name: surface-split-rule
description: "Any surface (Cowork, VS Code, browser download) that touches a project file must write to the canonical repo location, not a stray copy, and sync memory same day."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bc54fe22-1c3e-4602-b3dc-6518811893f7
---

Standing rule: any surface that creates or edits a project deliverable must write it into the canonical working repo (for Intradiem GTM work, `~/Claude/Projects/Intradiem GTM Engineer`), not into `~/Downloads`, a sibling folder, or any other side location. If a surface can't target the repo directly, the resulting file must be consolidated into the repo and the stray copy turned into a redirect stub the same day.

**Why:** Cowork and other surfaces have repeatedly written working files to `~/Downloads` or the sibling `Clay Builds and Strategy/` folder instead of the main repo, producing silent duplicates. Once duplicates exist, an edit applied to one copy (e.g. a de-rhyme fix to [[wfm-messagegen-canonical]]) doesn't propagate to the others, and someone can copy from a stale, half-fixed version without knowing it's stale.

**How to apply:** Whenever a message claims a file was "written back" or "saved" by a surface other than this one, verify the actual path on disk before trusting the claim. If it landed outside the canonical repo, consolidate: make the repo copy authoritative, prepend a `SUPERSEDED` redirect notice to every stray copy with original content preserved below (never delete outright), and confirm no stray copy still needs to be the one people paste from.
