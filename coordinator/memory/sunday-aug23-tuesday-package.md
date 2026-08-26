---
name: sunday-aug23-tuesday-package
description: "Aug 23 2026 Sunday build for the Aug 25 Naveen cadence: State Farm + Centene committee pages staged (gate clear, deploy NOT run), BO Insurance Titles segments live (15 cust / 68 prospects, 0 credits), verint_backoffice trigger in TAM config, back-office ICP skill updated with CAO/Claims Shared Services intel, messaging-study intake + Jack workflow-builder draft written"
metadata:
  type: project
---

Built Sun 2026-08-23 for the Tue Aug 25 Naveen GTM cadence (ABM test: State Farm + Centene, ten buying groups x ten angles).

- **Committee pages**: both accounts cleared the customer-exclusion gate. Staged at `~/Desktop/Intradiem Deliverables/deploy-icp-committees/_staging/`, handoff doc `STATE_FARM_CENTENE_REFRESH_Aug23.md`, render-assert PASS, live index.html untouched. Deploy command staged, NOT run. Katie Oakley removed from Centene BOO reference data (moved to Blue Cross NC; Centene has an open req for the seat). **State Farm QO/contact-center lane is a real gap** (only candidate: Deon Johnson, SVP w/ call-center scope) — needs a Clay/Apollo pull before it can go on the wheel. Naveen-title finds surfaced but not force-fit: Mary Schmidt (State Farm CAO), Jeffrey Lev (State Farm Chief Actuary), Shannon Bagley (Centene CAO).
- **Clay segments (0 credits, balance 67,861.8 unchanged)**: BO Insurance Titles - Customers `audseg_0tk8rc0Kc2YeAJXC7uq` (15) / Prospects `audseg_0tk8rc7a69SasaaDFj4` (68), all Director+ by construction; registry updated. Centene has an Executive VP, Chief Administration Officer in-database.
- **TAM engine**: `verint_backoffice` trigger (w20) added to `tam-outbound-engine/config/triggers.json`, tests 21/21. Engine still has NO back-office persona key (only cc_ops/wfm/cx/finance) — add `bo_ops` when the BO motion goes live there.
- **Skill**: intradiem-backoffice-icp updated (CAO + SVP Admin economic tier; Shared Services sits UNDER Claims per CNI org chart, so "Claims Shared Services" is the pull string; Actuarial secondary lane; Verint fit signal). Ask Naveen for his written department map.
- **Drafts**: `motions/messaging-study/` (intake + rubric + analysis prompt, in the worktree) and `Workflow_Builder_UseCases_Draft_for_Jack.md` (two-column honest framing + 60-day pilot).

**Why:** Tuesday package + Monday-morning send batch prepped in advance; follow-through is the credibility lever.

**How to apply:** Tue cadence walks through pages → segments → gap (State Farm QO pull is the ask); deploy only when Dallas says. Note: builds live in the vs-code-agents-window-usage WORKTREE, not the main checkout — merge or copy before referencing from main-repo jobs. Related: [[week-aug24-commitments]], [[sep2-webinar-invite-lists-aug21]].
