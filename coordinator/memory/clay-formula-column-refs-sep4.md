---
name: clay-formula-column-refs-sep4
description: "Clay formula columns resolve a reference to the column ID, so a name typed with different capitalization fails as 'Invalid field'; always read the live column name and the real JSON keys before writing a formula"
metadata:
  type: feedback
---

Sep 4 2026, debugging `Contact Center Platform, Latest` on the Stars demo table. The formula box kept reporting **Invalid field**. Root cause: the column is named `Contact Center Platforms` (title case) but every formula, both Clay's AI-generated one and Claude's pasted one, referenced `{{Contact center platforms}}` in lower case. Clay stores a reference as the column id (`{{f_0tkvfhmrG47gd85qKVm}}?.technologiesFound` on the sibling column), so a name that matches no column never resolves. The AI version had a second bug: it read `?.vendor_name`, a key PredictLeads does not return.

**Why:** Claude wrote the column name in a UI sheet in lower case, Dallas named the real column in title case, and the AI formula helper faithfully copied the lower-case name out of the prompt text. Three attempts were spent guessing at editor syntax when the reference itself was the bug. Dallas's instruction was explicit: "figure out what you're getting wrong and fix it", not move on.

**How to apply:** before writing ANY Clay formula, (1) read the live column name and id with `clay tables columns get <tableId>` and reference the column by picking it with `/` so it resolves to an id, and (2) read the real JSON shape from a populated cell, or run the action once via `clay workflows actions test <packageId> <actionKey> --inputs '{...}'` (1 credit) when every cell is empty. Never infer key names from the "Add data as columns" dialog's prettified labels: that dialog showed "Last Seen At" and "Technologies Found" while the payload carries `last_seen_at` and `technologiesFound`. Validate the finished expression against the real payload with `node` before handing it over. Related: [[feedback-no-guessed-ui-steps]].
