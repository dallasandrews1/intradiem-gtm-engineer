# All-hands demo recording script (target 6:30)

One recorded video, narrated live at the all-hands (safer than baked-in audio: you can pause, ad lib, and match the room). Six beats: Claude Code (the brain) → Clay (data + AI research + automation) → lemlist (the send) → the loop. Every beat is something that already exists and runs; nothing is staged for the camera.

## Why these beats

- Naveen's outline says "Demo - Clay", so Clay carries the middle and the longest beat (rows enriching live is the single best visual in the whole stack).
- Opening in Claude Code sets the real story: the AI isn't one tool, it's the layer that runs the whole outbound motion. lemlist closes the loop so the audience sees work leave the building, not just get prepared.
- Everything shown is read-only or re-runs existing rows. Nothing sends during the recording.

## Pre-flight (do these before recording, in order)

1. **Clean the lemlist sequence first.** Stars - Resurrection still has the two steps labeled STRAY in the sequence editor (queued for UI deletion since Aug 31). Delete them in the UI before recording, or keep the recording on the campaign review/leads screens and stay off the sequence editor.
2. **Dry-run the enrichment beat off camera.** In the Clay table you'll record, duplicate 4 or 5 rows (or pick rows you're comfortable re-running), run the research and draft columns once, and confirm they fill clean. Estimated cost is a few credits per row, well under the 100-credit line. If a column errors, pick different rows; never debug on camera.
3. **Stage the tabs in show order** so the recording is one continuous take with tab switches, no URL typing:
   - Tab 1: Claude Code (terminal, full screen, font bumped to ~16pt)
   - Tab 2: Slack DM with the daily rundown (this morning's brief)
   - Tab 3: Clay Audiences
   - Tab 4: the motion table with the pre-tested rows
   - Tab 5: Clay workflow "Webinar Registrant Enrich + Route" (wf_0tk333zvDnGg4YcikFp), open on the graph, run history visible
   - Tab 6: lemlist, Stars - Resurrection campaign (cam_sh3JCJoxtEHyjGrsw, 43 leads, voice steps)
4. **Screen hygiene:** Do Not Disturb on, bookmarks bar hidden, browser at 110 to 125 percent zoom so the room can read cells, close every unrelated tab and window. Keep the Clay credit balance off screen where the UI allows; cost isn't part of the story.
5. **Recording:** QuickTime screen recording, full screen, 1080p or better. Record each beat as its own take with 2 seconds of still screen at both ends, then trim and join (QuickTime Edit > Add Clip to End works; iMovie if you want crossfades). One continuous take is fine too if the dry run was clean.
6. **Content check on camera-visible data:** the rows you enrich and the leads you show in lemlist are prospects, not customers. Skip any row with an odd name or a sensitive account. No 6sense anywhere in frame.

## The beats

### Beat 1 · 0:00 to 1:10 · Claude Code, the brain
**Screen:** Terminal with Claude Code open. Type one ask, for example: "Build the strike plan for [a real target account from the TAM engine]." Let the plan stream: fit score, triggers, the buying committee, the recommended sequence.
**While it streams, flip briefly to Tab 2:** the morning rundown DM that was waiting at 7:50am, written by agents overnight.
**Say roughly:** "This is where my day starts. Nineteen agents ran overnight: market scans, account triggers, audits. This brief was waiting for me this morning. And when I need a full account plan, I ask for it in plain English and the engine builds it from live data. This is the same engine that built the ICP buying-committee pages leadership is working from."

### Beat 2 · 1:10 to 2:10 · Clay, the database
**Screen:** Clay Audiences. Show the top line: 140,000+ people, 2,300 companies, synced from Salesforce. Build one segment live, for example back-office operations leaders at insurance companies. The count lands in seconds.
**Say roughly:** "Everyone we know, in one place, synced from Salesforce. Watch what a list build looks like now." Pause while the count appears. "That used to be days of export and spreadsheet work. Zero cost, and it stays current on its own."

### Beat 3 · 2:10 to 3:40 · Clay, AI research and drafts (the centerpiece)
**Screen:** the motion table. Select the pre-tested rows, re-run the enrichment and draft columns, and let the room watch cells fill left to right: person found, work email verified, current role confirmed, research summary written, then a personalized five-touch sequence per contact.
**Say roughly:** "Here's the part that used to be a full-time job. For every contact: find them, verify the email, confirm they're still in the seat, research what they care about, and write five touches in the rep's own voice. Watch it happen for five people at once." Let 10 to 15 seconds run with no narration; the screen carries it. Then: "Every draft still passes a checkpoint before anything sends. The checkpoints are tuned per motion and widen as each motion earns trust."

### Beat 4 · 3:40 to 4:30 · Clay, automation
**Screen:** the published "Webinar Registrant Enrich + Route" workflow. Show the graph (trigger → enrich → classify → route), then the run history with real runs.
**Say roughly:** "This one runs without me. Someone registers for a webinar, and by the time marketing looks up, they're enriched, classified, and routed to the right owner. It handled a thousand registrants the week we turned it on."

### Beat 5 · 4:30 to 5:40 · lemlist, the send layer
**Screen:** Stars - Resurrection campaign. Show the loaded leads, then one lead's rendered sequence: email steps with every variable filled with that person's actual details, the LinkedIn step, the call step, the AI voice note step.
**Say roughly:** "Cleared contacts land here. Email, LinkedIn, and a call step per person, and every line you see was drafted by the engine in the rep's voice, personalized to that individual. The rep owns the send and the conversation; the engine did the hours of sourcing, research, and drafting behind it."

### Beat 6 · 5:40 to 6:30 · the loop, beyond outbound
**Screen:** back to Slack: a routed reply or activity alert landing with the account owner (use a real recent one). Then the closer: backoffice-maps.pages.dev, scrolling one of Inger's account maps, the org chart, lanes, and the bench.
**Say roughly:** "Replies come back and route to the owner with a suggested response, and every motion is measured on cost per meeting like any other channel. And this isn't just outbound. When the account management team needed back-office maps for twelve strategic accounts, the same engine sourced the people, checked them against Salesforce, and delivered these as a live page. That's the point: it's an engine, and it can run work like this for any team."
**Note:** the maps page shows real names at real accounts; that's fine for an internal all-hands, but stay on one account and keep scrolling so no single person is on screen long.

## Fallback

If any beat breaks on recording day, the operating map's animated system view (gtm-operating-map.pages.dev) narrates the same story slide-style; and beats 2, 5, and 6 are read-only screens that cannot fail. The only beat with live execution risk is beat 3, which is why it gets a dry run first.

## Timing discipline

6:30 total. If a take runs long, cut narration, not screens; the room reads the screen faster than it listens. Beat 3 is the only one that should ever get longer.
