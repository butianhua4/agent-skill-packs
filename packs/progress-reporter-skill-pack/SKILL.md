# Progress Reporter Skill

## Purpose

Create honest, buyer-readable progress reports from technical activity logs,
implementation notes, validation output, and remaining blockers.

## Inputs

- Goal or order scope.
- Completed actions.
- Files, features, or assets changed.
- Verification commands and results.
- Known blockers, risks, or missing buyer inputs.
- Next recommended action.

## Workflow

1. Restate the buyer goal in one plain sentence.
2. Separate completed work from planned work.
3. Convert technical details into business impact.
4. List verification evidence, including commands, tests, screenshots, or manual
   checks.
5. Flag blockers without blame or overpromising.
6. Recommend the next smallest useful step.
7. Produce both a short platform-ready update and a detailed internal report.

## Output

The final report should include:

- `Status`: on track, blocked, needs buyer input, or ready for review.
- `Completed`: concrete finished items.
- `Verified`: evidence that the work is real.
- `Risks`: issues that may affect delivery.
- `Next`: the next action.
- `Buyer message`: a short copy-ready update.

## Boundaries

- Do not invent completed work.
- Do not claim a test passed unless there is evidence.
- Do not include credentials, private links, private files, or personal data.
- Do not promise refunds, payments, or off-platform communication.
- Escalate when buyer approval, identity, payment, tax, OAuth, or private system
  access is required.
