# Polar inbox

Landing folder for files downloaded from a Polar task (the AI browser on Dallas's personal Mac).
Polar has NO access to this Mac (probe Sep 13 2026): it runs in a cloud sandbox. Its report is the REPORT block at the end of its final message, which Dallas pastes back (`polar_intake.py --paste <slug>`). Screenshots or exports live in Polar's workspace behind download links; when one matters Dallas downloads it to `automation/inbox/polar/<task-slug>/` or `~/Downloads/polar/<task-slug>/`, both scanned by the intake.

`python3 automation/polar_intake.py` (dry run by default, `--apply` to write) finds new files,
mints an `evt: polar-intake-<date>#<task-slug>` anchor, appends `automation/logs/polar-intake-<date>.md`
with the files and the verification that still closes the task, and records the files in `.intake-state`.
The daily rundown reads that log. A Polar report is a claim; the CLI or connector read named per task in
`automation/config/polar_tasks.json` is what closes it.

Nothing in this folder is ever loaded into Clay, lemlist or Salesforce by the intake. Nobody but Dallas.
