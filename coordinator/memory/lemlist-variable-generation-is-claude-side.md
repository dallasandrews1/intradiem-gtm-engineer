---
name: lemlist-variable-generation-is-claude-side
description: "opener_line/vm_hook/contract_line/voice_script are generated Claude-side per contact and loaded as lemlist lead custom variables, NOT by any Clay column or Clay MessageGen prompt"
metadata: 
  node_type: memory
  type: project
  originSessionId: ed37ff75-857a-4f90-8d0f-af74c45047b8
  modified: 2026-08-06T19:26:52.160Z
---

The four per-lead lemlist variables across the five campaigns (UK Airlines `cam_fHGtNHbbj7LmThFgX`, UK Insurance/FS `cam_nwKASgttBM6QT8XGq`, Stars Finance `cam_2gy9hmEvMjYEuPZ8A`, Stars Quality `cam_viEbB6HkYsCPtxKbi`, Stars Resurrection `cam_sh3JCJoxtEHyjGrsw`) are generated Claude-side per contact, critic-gated, then loaded as lemlist `customVariables`. There is no Clay table, column, or MessageGen prompt behind them. Resurrection uses none of the four; it carries only `firstName` and `plan_name`.

The Clay MessageGen system prompts (`Clay_MessageGen_SystemPrompt_v2.md` and the BackOffice/CostMandate siblings) are a different surface: they generate email subject and body for the Clay-driven motions, not these lemlist variables.

**Why it matters:** because there was no durable generation prompt, each wave rediscovered the template seams from scratch (airlines v1.0-v1.5, FS fs-v1.0/c1, Stars hand-written), which produced systematic seam defects: 41/41 airlines vm_hooks render lowercase after a full stop, 82/131 voicemails blow the 25-second cap, and both Stars contract_line seams leave a demonstrative dangling.

**How to apply:** the durable block now lives in `Intradiem GTM Engineer/motions/shared/Variable_Seam_Contract_Aug6.md` (seam-v1.0, PROPOSED as of Aug 6 2026). Append it to every per-lead variable generation run. The punctuation contract differs per campaign: Airlines templates supply the trailing full stop after `{{vm_hook}}`, FS and both Stars lanes do not. Never assume one house rule across campaigns; read the live template both sides of the variable first. Ties to [[always-confirm-live-clay]], [[verify-cross-session-status-claims]].
