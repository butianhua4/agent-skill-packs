# Auto Debugger Skill Pack

## Purpose

Classify and diagnose automation failures, then produce a safe, scoped fix plan.

## Inputs

- Error log or stack trace
- Workflow name or command that failed
- Expected behavior
- Actual behavior
- Recent changes
- Environment notes such as OS, Node.js version, package manager, CI runner, or
  automation platform

## Workflow

1. Create a failure summary in one paragraph.
2. Classify the failure:
   - syntax
   - dependency
   - permission
   - missing file
   - malformed JSON or schema mismatch
   - timeout or rate limit
   - network or API error
   - configuration mismatch
   - unknown
3. Extract evidence from logs and separate it from assumptions.
4. Rate risk as low, medium, or high.
5. Propose the lowest-risk fix first.
6. Define a validation command or manual check.
7. Mark any action needing private access, production access, payment, identity,
   or admin permission as user-owned.
8. Return the report using `DELIVERY_TEMPLATE.md`.

## Output

Use the delivery template and include the confidence level for each conclusion.

## Boundaries

- Do not modify production systems by default.
- Do not request credentials, tokens, payment access, KYC data, or private keys.
- Do not open unknown customer external links.
- Do not auto-run destructive commands.
- Do not claim the issue is fixed until validation passes.
- If the logs are incomplete, ask for a redacted minimal reproduction.
