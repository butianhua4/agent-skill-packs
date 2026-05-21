# Test Cases

## Case 1 - JSON Parse Failure

Input: agent run failed with `Unexpected token` in a JSON response.

Expected output:

- Classify as schema/format failure.
- Recommend adding structured output validation.
- Provide a minimal reproduction step.

## Case 2 - Missing Dependency

Input: CI log says `Cannot find module`.

Expected output:

- Classify as dependency or package resolution failure.
- Ask for package manager and lockfile context.
- Provide fix plan without guessing production access.

## Case 3 - Rate Limit

Input: workflow fails with HTTP 429.

Expected output:

- Classify as rate limit.
- Recommend backoff, queueing, model routing, or smaller batches.
- Do not suggest account sharing or unsafe bypass.
