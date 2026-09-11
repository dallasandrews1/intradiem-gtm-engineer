---
name: feedback-map-vs-route-comms-plan
description: "Dallas's Sep 11 2026 read on the Cleveland Clinic Save Room: a contact list plus a status board is the map, not the route; an AM save deliverable has to be the communication plan itself (routes around the blocker, lanes with owners by role, dated moves, messages written and gated), built on the ADT save precedent from the PMO tracker"
metadata:
  type: feedback
---

Sep 11 2026: after the verified-only Save Room shipped, Dallas: "something is still missing... how does this thing actually help Inger solve the problems she mentioned in the call?" The page answered the contact and status asks but not the ask Mary Ann gave Inger: a communication plan to get more people to the table, and clarity on who (Inger, Amy, Nicole/marketing, executive voice) does what.

**Why:** the AM's deliverable to her SVP is a plan with moves and voices; people and health are the appendix. Stripping owners to avoid handing out tasks also removed the one thing she asked to see; the fix is owners by lane (role), never a task list.

**How to apply:** for any save or expansion room, the first screen is the plan: routes around the blocker (the ADT precedent: peer door, user groundswell, parallel team, executive voice held, high and wide, renewal track), four lanes with an owner by role, dated moves by week, the messages drafted through the first-draft engine and sharpener with a claims ledger, and the account rules. Contacts and health sit behind it. The Monday note leads with the lane moves due that week. Built: `motions/churn_risk_save_plan/build_comms_plan.py` and `data/comms_plan_cleveland_clinic.json`. Related: [[feedback-am-pages-verified-only-no-new-tool]], [[inger-churn-risk-save-plan-sep10]].

**Addendum (Sep 11, 'Why am I creating something for Nicole as well as Inger?'):** one deliverable, one owner. When an AM owns the account, every lane (including marketing) lives inside the AM's plan; never build a separate page for a colleague the AM is already working with, because it creates a second surface for Dallas to manage, routes around the AM, and puts Dallas in the position of scoping another team's work. A list the AM passes along is a CSV, not a page. The Nicole brief was scope creep from Claude, not an ask.
