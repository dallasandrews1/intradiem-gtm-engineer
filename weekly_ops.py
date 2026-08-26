#!/usr/bin/env python3
"""Generate a weekly GTM Engineer operating plan from a small template."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from textwrap import dedent


def build_plan(motion: str, goal: str, target_count: int, output_path: Path) -> str:
    today = date.today().strftime("%Y-%m-%d")
    motion_title = motion.replace("-", " ").title()
    plan = dedent(
        f"""\
        # GTM Engineer Weekly Operating Plan

        Generated: {today}
        Motion: {motion_title}
        Goal: {goal}
        Target count: {target_count}

        ## 1. Week posture
        - Primary motion: {motion_title}
        - Objective: create one small, measurable wave and capture signal
        - Success bar: at least one tracked reply or one clear next-step action
        - Operating posture: keep measurement explicit and treat targets as provisional

        ## 1a. Current motion context
        - Star Ratings is already live and has sent 23 emails, so this is now an optimization and orchestration phase, not a pre-launch phase.
        - The work already present in VS Code includes automation built in Claude Code, multiple live workbooks, and the supporting Clay motion structure.
        - The next priority is to review actual replies, meetings, and performance from the current sends, then tighten the workflow and sequencing where the signal is strongest.
        - Cost-Mandate and WFM-Adjacency remain useful second-wave motions, but they should be evaluated against the learnings from the current live motion rather than treated as the first thing to build from scratch.

        ## 2. Weekly checklist
        ### Monday
        - Review the target universe and choose one wedge
        - Confirm the buyer angle and the outreach thesis
        - Pull the relevant repo assets: the canonical universe, the motion runbook, and the credit ledger

        ### Tuesday
        - Draft the message variants and verify claims against the repo guidance
        - Set the wave size and the approval gate
        - Record the expected credit cost before any expensive Clay step

        ### Wednesday
        - Launch the small wave
        - Keep the send volume tight and instrumented
        - Confirm the motion is tied to a named next step

        ### Thursday
        - Review replies and classify them
        - Decide whether to continue, adjust, or stop the wave
        - Update the weekly scorecard

        ### Friday
        - Summarize what worked, what did not, and what to do next week
        - Capture the leading indicators for the manager update
        - Flag risk early, especially around credit usage or deliverability

        ## 3. Credit guardrails
        - Estimate credits before any enrichment run or large Clay build
        - Keep the spend tied to a named sales outcome
        - Pause if the motion is not producing signal after one small wave
        - Review spending if monthly burn approaches 60 percent of the budget

        ## 4. Scorecard
        - Accounts targeted: {target_count}
        - Messages sent: to be recorded after send
        - Replies received: to be recorded after review
        - Qualified replies: to be recorded after review
        - Meetings or next-step actions: to be recorded after review
        - Credits spent: to be recorded after each Clay run

        ## 5. Suggested first-wave defaults
        - one narrow audience
        - one core angle
        - two message variants
        - one human approval gate

        ## 6. Next action
        - Start with the smallest useful wave and make the first review count
        """
    ).strip() + "\n"

    output_path.write_text(plan, encoding="utf-8")
    return str(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a weekly GTM operating plan")
    parser.add_argument("--motion", default="star-ratings", help="Motion name to place in the plan")
    parser.add_argument("--goal", default="Generate one small, measurable wave", help="Primary objective")
    parser.add_argument("--target-count", type=int, default=30, help="Target account count for the week")
    parser.add_argument("--output", default="weekly_ops_plan.md", help="Output markdown file path")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = repo_root / output_path

    output_file = build_plan(args.motion, args.goal, args.target_count, output_path)
    print(f"Wrote weekly operating plan to {output_file}")


if __name__ == "__main__":
    main()
