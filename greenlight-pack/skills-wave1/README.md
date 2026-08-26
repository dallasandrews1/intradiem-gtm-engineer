# Greenlight skills, Wave 1

Six skills packaged for Greenlight's skill-attachment release. Each folder is a standard Claude Agent Skill: SKILL.md with trigger phrasing in the frontmatter description, instructions in the body.

Install order matters for one of them:

1. **intradiem-verified-metrics** first. This is the claims gate. It's the source-of-truth skill the copy skills call before letting any Intradiem number or customer story into prospect-facing output. Everything unverified gets marked instead of silently included.
2. **intradiem-first-draft-engine** + **intradiem-copy-sharpener** as a pair. Draft thinking framework, then the send-ready quality gate. Together they take a rep from blank page to C-suite-ready copy.
3. **intradiem-objection-handler**. Prospect pushback to a calm 3-4 sentence reframe in the rep's voice, seven objection categories.
4. **intradiem-competitive-intel**. Competitor mention (Verint, NICE, Calabrio, in-house RPA, status quo) to counter-narrative brief with wedge analysis.
5. **intradiem-roi-business-case**. Call transcript with an economic buyer to a 1-page business case: current state, projected impact, cost of inaction, timeline.

Notes for deployment:
- All copy-generating skills carry the verified-claims discipline. That's the answer to "what if reps send made-up numbers."
- These are self-serve: a rep triggers them with plain phrases (in each SKILL.md description). No dependency on me at runtime.
- Wave 2 (signal-to-play, strike-sequence, content-engine, daily-war-room, launch-kit, backoffice-icp) is ready when Wave 1 feedback lands.
