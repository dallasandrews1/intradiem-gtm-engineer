# Greenlight addendum for Prototype Builder

Only if the agent runs in Greenlight (Sonnet, short reply limit). Paste this after section 2 of PROJECT_INSTRUCTIONS.md. Do not use it in the Claude Project; there it only costs quality.

## 2a. Size budget (hard limit)

Long replies fail in this tool, so every prototype fits one reply.

- The whole file stays under 20 KB, about 450 lines. Count as you go; if you are heading past it, cut scope, not the self-check panel.
- Mock data is small and realistic: one context (one country, one team, one account), one year, 6 to 12 records. Never a full catalogue.
- Build only the screen the brief names. No global shell beyond a header bar and, if the source has one, a sidebar list of at most five disabled items.
- Four to six acceptance checks, computed where cheap.
- Compact code: one stylesheet with shared classes, no comments, no repeated markup, data as arrays, one render function per panel, no library.
- Write the file directly. Do not run code, do not test in a sandbox, do not narrate before the file. The handover comes after it.
- If the brief needs more than the budget allows, build the core interaction first and end the handover with a "Second pass" list. The product manager asks for those one at a time, and each answer returns the whole file again.

