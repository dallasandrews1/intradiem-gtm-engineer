---
name: clay-functions-build-status
description: "8 shared Clay Functions being extracted from motion-specific columns so one fix propagates everywhere; 3 of 7 live, one confirmed hardcoded leak found+fixed, fn_persona_key wfm branch now fixed+live-verified (Jul 17), cx branch still open"
metadata:
  node_type: memory
  type: project
  originSessionId: catchup-jul17-2026
---

Dallas is extracting repeated Clay logic (critic, send-ready gate, malformed guard, email waterfall, persona routing, eligibility, tokens-ready, later a voice critic) into shared Functions, sourced from the hardened Cost-Mandate columns (not the older Stars ones), so a single fix propagates to every motion.

As of Jul 16-17: **3 of 7 built and published live** (`fn_draft_critic`, `fn_send_ready`, `fn_persona_key`); 4 spec'd but blocked by concrete Clay UI limits (no group-level "save as function" for a waterfall, no standalone `eligible` column to extract).

**Motion-neutrality audit of all 7** (required before WFM-Adjacency could safely stamp off the golden scaffold, see [[clay-motion-factory-scaffold-system]]) found **one confirmed hardcoded leak:** `fn_tokens_ready` had a literal `Universe == "install_base"` clause that would fail every non-Back-Office row — fixed and verified live. `fn_draft_critic` was found to have three unbound figure fields (`disclosed_figure`, `disclosed_figure_source`, `product_angle`) — investigated and determined to be a safe, fail-closed gap (can only false-reject a legitimate proof stat, never pass a fabricated number), left as a deliberate unresolved design decision rather than a rush-fix. `fn_persona_key` was missing a `wfm` branch (the confirmed WFM-Adjacency blocker) and a `cx` branch — **the `wfm` branch was fixed and live-verified Jul 17**: a live Cost-Mandate workflow test with job_title "Director of Workforce Management" returned `persona_key="wfm"` and routed `in_icp` through the gate (node 3 failed only on a missing test `company_domain`, harmless). `cx` branch still open. An 8th Function, `fn_draft_voice_critic`, was spec'd because voice/cadence judging has zero motion-specific inputs — "structurally impossible to leak," the cleanest one to centralize. See [[messagegen-voice-cadence-standing-rule]].

**Open/blocked:** `fn_email_verified`, `fn_eligible`, `fn_draft_clean`, `fn_tokens_ready`-replacement still need building as live Functions; `fn_persona_key` still needs a `cx` branch (`wfm` is done, see above); the `fn_draft_critic` figure-field binding is an open verified-claims policy call, explicitly Dallas's to make, not to auto-apply.
