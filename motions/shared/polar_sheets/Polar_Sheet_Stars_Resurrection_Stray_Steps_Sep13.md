# Polar sheet: delete the two STRAY steps in Stars - Resurrection

> Task slug `stars-resurrection-stray-steps`. The Aug 31 API probe left two empty steps in lemlist campaign "Stars - Resurrection (Nate)". The API refuses to delete them because leads have been reviewed, so this is a UI delete. Two steps, both titled so they cannot be confused with a live step, nothing else in the campaign changes.

## Ground truth (read Sep 13 2026 via the lemlist connector, get_campaign_sequences)

| Item | Value |
|---|---|
| Campaign | Stars - Resurrection (Nate), `cam_sh3JCJoxtEHyjGrsw`, running since Sep 4 |
| Stray step 1 | `stp_6eBfPTm3Y92XNT363`, type LinkedIn voice note, manual, empty message, last step of the root sequence `seq_D4jpFJfsipwr33bny` (after the Accepted-invite condition) |
| Stray step 2 | `stp_MPXXucbkXwjkiiJSP`, type manual task, empty, last step of the Accepted-invite branch `seq_WbTtwaYkMggGu9ztX` (after the "one more before the window closes" email) |
| Both titled | `STRAY STEP from an API test (Dallas): delete this step, it does nothing` |
| Everything else | 11 live steps across 5 sequences: visit, connect, condition, LinkedIn message, call, email, call, email A/B, condition, two closing emails. None is touched. |
| Expected end state | 11 steps, neither stray id present, campaign state unchanged (running), no lead state changed |
| Credits | 0 |

Button labels in lemlist's sequence editor are not verified from docs; read the screen. A delete confirmation dialog may appear; confirm only when the step title on screen reads STRAY.

## Paste into Polar (the task)

```
TASK stars-resurrection-stray-steps. lemlist, campaign "Stars - Resurrection (Nate)" (id cam_sh3JCJoxtEHyjGrsw). Follow the numbered steps only. Do not improvise. You have no access to this Mac's files: keep the screenshot in your own workspace and give its download link; end your final message with the REPORT block in step 8, then stop. Do not pause, resume, launch, or edit any other step, lead, or setting of this or any campaign.

1. Open the campaign and its sequence editor. Confirm the campaign name reads "Stars - Resurrection (Nate)" and the URL contains cam_sh3JCJoxtEHyjGrsw. If not, STOP and hand back.
2. Find the step whose title begins "STRAY STEP from an API test (Dallas)" at the END of the main sequence (after the Accepted-invite condition block, a LinkedIn voice note). Confirm the title text on screen before doing anything.
3. STOP-AND-HAND-BACK: show Dallas the selected step. Only after he confirms, delete that step (the step's own menu, then the delete entry; label not documented, read the screen). If a confirmation dialog appears, confirm only if the dialog names this step or shows its STRAY title.
4. Find the second step with the same STRAY title at the END of the "Accepted invite" branch (a manual task after the email titled "one more before the window closes"). Confirm the title text on screen.
5. STOP-AND-HAND-BACK: show Dallas the selected step. Only after he confirms, delete it the same way.
6. If lemlist asks to save or publish the sequence, save. If it offers to change the campaign status (pause, resume, launch) do NOT touch it; STOP and hand back.
7. Screenshot the full sequence with both strays gone, keep it as after.png in your workspace.
8. End your final message with a block that starts with the line REPORT stars-resurrection-stray-steps and lists: the two step titles you deleted, whether a confirmation dialog appeared and what it said, whether lemlist asked to save and what you clicked, the campaign status shown at the end (expected: running, unchanged), anything that did not match this sheet, and the download link for after.png.
9. Stop. Do not message anyone. Do not open any other campaign.
```

## Stop-and-hand-back lines

- Campaign name or id does not match (step 1).
- Before each delete, always (steps 3 and 5).
- A step with the STRAY title cannot be found where the sheet says, or a third STRAY title appears (there are exactly two).
- Any prompt to pause, resume, launch, or change campaign status (step 6).

## Report-back

Polar has no access to this Mac (probe, Sep 13 2026). The report is the REPORT block at the end of its final message. Dallas pastes it back to Claude Code; the intake logs it as a claim with `python3 automation/polar_intake.py --paste stars-resurrection-stray-steps` (text on stdin). The screenshot stays in Polar's workspace behind a download link; download it to `~/Downloads/polar/stars-resurrection-stray-steps/` only if it matters.

## Verification that closes the task (Claude Code, not Polar)

1. lemlist `get_campaign_sequences` on `cam_sh3JCJoxtEHyjGrsw`: neither `stp_6eBfPTm3Y92XNT363` nor `stp_MPXXucbkXwjkiiJSP` present; the other 11 step ids unchanged; campaign status unchanged.
2. Log line under `evt: polar-intake-<date>#stars-resurrection-stray-steps`. Registry status to `verified`; memory `lemlist-api-sequence-step-limits-aug31` notes the strays as deleted.

Note: never probe API step creation on a campaign that holds leads again; the reason these strays exist is that lemlist makes API-created steps permanent once any lead is reviewed.
