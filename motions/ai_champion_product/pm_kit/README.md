# Prototype kit for product managers

Turn a one-page brief (or an existing PRD) into a working prototype you can click through in a review. Runs in Greenlight. No install, no repo, no engineering time.

## What is in this folder

| File | What it is | What you do with it |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | The builder's instructions: build rules, design tokens, the self-check panel, what it hands back | Paste as the Project instructions |
| `Prototype_Brief_Template.docx` | The one-page brief, nine sections | Fill in sections 1 to 7 before you build; 8 after the review |
| `DS_Tokens.md` | Design system tokens the prototype must use | Upload to the Project; swap for design's current sheet when they send one |

## Set up once (about five minutes)

1. In Greenlight, create a new Project and name it `Prototypes`.
2. Open `PROJECT_INSTRUCTIONS.md`, copy everything, and paste it into the Project's instructions.
3. Upload `DS_Tokens.md` to the Project's files.

If your Greenlight does not show Projects, do this instead: start a new chat, paste the whole of `PROJECT_INSTRUCTIONS.md` as your first message, attach `DS_Tokens.md`, and carry on from step 2 below in the same chat.

## Build a prototype

1. Fill in the brief. Section 1 (the decision the prototype settles) and section 6 (five to eight acceptance checks) matter most. If all you have is a PRD, skip the brief; the builder drafts one from the PRD and shows it to you first.
2. Start a chat in the Project, attach the brief or the PRD, and type:

   > Build the prototype from the attached brief.

   or, for a PRD that covers several screens:

   > Build the prototype for Screen [number or name] from the attached PRD. Draft the brief first and show it to me before building.

3. Read the draft brief if it drafted one. Correct anything in your words, then say `Build it`.
4. Download the HTML artifact. Save it as `index.html`. Double-click to open.
5. Click the **Checks** button in the bottom-right corner (or press `?`). The panel lists your acceptance checks with pass, fail, or manual. Do each manual check yourself; each one takes under a minute.
6. Save `index.html` and the brief in the feature's SharePoint folder so the review opens the same link.

## When a check fails

Say what failed, in one message, in the words from the panel:

> Check 4 fails: the coverage preview shows 0 agents affected. Fix that and keep everything else the same.

You get the whole file back. Download it, replace `index.html`, reopen, press `?` again. Fix one thing at a time so the room sees the same prototype with one change.

If a check is marked manual and you find it fails when you do it by hand, report it the same way.

## When the builder asks you a question

It asks only when the source does not settle something it needs: which screen, which widths, what the data stands for. Answer in one line. Anything you leave open, it decides itself and lists under "Decisions I made" in the handover, so you can overrule it.

## The review

Review on the prototype, not on a document. The room clicks; you fill in section 8 of the brief with what was decided per question in section 7. Section 8 is what engineering builds from. A PRD is written afterwards only where a compliance or contract record requires one.

## Questions

Dallas Andrews, AI champion for Product.
