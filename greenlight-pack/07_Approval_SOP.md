# Approval SOP (adopted Jul 8 2026)

The human gate stays. How it's operated depends on whether copy varies per row.

## Lane 1: template sends (current sequencer campaign)
Copy is fixed, only structured merge fields vary. Slop risk lives in the data, not the prose, so the data is what gets checked.

1. Formula pre-gate (already live): critic_email_valid PASS + send_ready logic + campaign sync run condition (send_ready == "READY"). Empty merge fields or FAIL emails never reach approval.
2. Human step per wave: open a filtered view of the wave, review a ~10% sample plus every edge row (blank fields, odd names, out-of-range QBP numbers), then bulk-check human_approved on the selection. Minutes per wave, not hours.
3. Structural backstops make blanket review unnecessary: plaintext templates, daily send caps, 20-min spacing, auto-pause on reply, pause-same-company.

## Lane 2: per-row generated copy (future MessageGen column)
1. First 50 rows: 100% human review (per 03_MessageGen_Deployment_Sheet.md).
2. After 50: exception-based review. A critic column checks every draft against Verified Metrics / Claims (claims, length, persona, banned phrases). PASS rows flow to the wave-level sample review; FAIL rows route to a human individually.
3. Any critic-FAIL pattern appearing twice gets fixed in the system prompt, not hand-edited per row.

## Collision control (1:1 vs 1:many, same contact)
The sequencer is the ambient email layer for the whole committee; 1:1 work rides on top. Rules:
- A reply auto-pauses the lead (and same-company leads) in the campaign. From that moment the contact belongs to a human.
- When a BDR claims a contact for manual 1:1 email work before any reply, they check bdr_claimed on the contact row. That one checkbox does both jobs (LIVE as of Jul 8): the sync run condition (send_ready == "READY" && bdr_claimed != true) blocks the contact from ever entering the campaign, and the Pause lead in campaign action fires automatically to pause them if they are already sequenced.
- BDRs never run a parallel manual email cadence to an active campaign lead. Their lanes: replies, calls, voicemail, LinkedIn, voice notes, bespoke exec touches from the strike room.

## Ownership
Dallas owns templates, prompts, gates, and the ledger. BDRs own approvals-by-exception on their waves and everything after a reply.
