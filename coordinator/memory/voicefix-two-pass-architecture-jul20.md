---
name: voicefix-two-pass-architecture-jul20
description: "The two-pass Voice Fix architecture (MessageGen writes facts, Voice Fix rewrites voice) is what finally passed both Draft Audit and Voice Audit for Stars. Prompt rules on a single pass could not."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T07:40:25.639Z
---

Jul 20 2026: SOLVED the Stars messaging quality loop. Root lesson: one MessageGen pass cannot reliably nail all the facts AND perfect human cadence at once; piling more rules onto its prompt made it worse (stacking <-> chopping pendulum). The fix is architectural, a TWO-PASS pipeline on the live Contacts table `t_0thtm73HHxyiupTuepK`:

1. **MessageGen Email 1 (v2.2)** (claude-sonnet-5) -> writes the raw draft, owns the FACTS (numbers, attribution, contract scope). Passes Draft Audit.
2. **Voice Fix** column (GPT-5.6 Sol/Terra, single Claygent prompt box) -> reads Msg1Subject + Msg1Body (raw), rewrites ONLY the voice, outputs revised_subject + revised_body. Owns CADENCE.
3. Extractor formula columns **VoiceFix Subject** = `{{Voice Fix}}?.["revised_subject"]`, **VoiceFix Body** = `{{Voice Fix}}?.["revised_body"]`.
4. **Draft Audit + Voice Audit + the sync** all read the VoiceFix columns (the polished output), NOT raw MessageGen. Msg1Body/Msg1Subject stay pointed at raw MessageGen (they are Voice Fix's input, do NOT repoint or you loop).

Voice Fix prompt keys: fix STACKING (comma-piled 3+ fact sentences) AND CHOPPING (short disconnected fact-list) with the SAME cure = CONNECT the pieces with logic (so/which/because/though); most sentences medium and connected; opener = one spoken idea; kill false-contrast ("it's not X, it's Y"); preserve every number/fact exactly; FINAL SELF-CHECK block drives HIGH confidence. Result: all 6 sampled drafts passed both audits.

Other Jul-20 decisions in this build: LinkedIn hook (`li_recent_post_hook`) turned OFF for the proof wave via a "LINKEDIN HOOK OFF" line in MessageGen system prompt (nano model + unverified post dates = hallucination/timing risk); hardened hook prompt written (GPT-5.6 Terra, 30-day recency, fail-safe empty) for later. Voice Audit runs gpt-5.6-terra with a FALSE CONTRAST fail mode added. See [[stars-live-table-dollar-wiring-jul20]].

## Update Jul 20 PM — Voice Fix ported into the workflow (all 5 touches)
Voice Fix pass is now wired into all 5 touches of `wf_0tiegzuo3PzJ4UtUGFA` and validates clean. Each touch: MessageGen En -> Voice Fix En (gpt-5.5) -> malformed guard + critic + voice audit (all read the Voice Fix revised_body/revised_subject). Voice Fix node IDs: E1 wfn_0tigswnfnCnyxXAXKow, E2 wfn_0tigt20dkAoEw6sdDF6, E3 wfn_0tigt2ayVRBMpsgz5xz, E4 wfn_0tigt2kgHEsiVCnt2ui, E5 wfn_0tigt2uRrgzgkQSn7sA. Explainer docs: motions/star_ratings/Stars_Email_Engine_MAP.md and Stars_Outbound_Engine_ENDGOAL.md.
REMAINING for full autonomous E1-E5 engine: (1) write the 5 polished emails back to the Contacts table as Msg1-5 columns for the sequence to pull; (2) reconcile workflow's shared fn_draft_critic dollar-grain vs the table's fixed CS-slice (E2-E5 compose nodes still need the dollar/star signal_evidence patch node 8a got); (3) real-row test through all 5 touches.
