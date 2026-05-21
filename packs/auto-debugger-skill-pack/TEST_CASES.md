# Test Cases

## Case 1 - Broken JSON Config

Input:

```text
SyntaxError: Unexpected end of JSON input
config/error-patterns.json line 12
```

Expected output:

- Classify as malformed JSON.
- Recommend validating with a JSON parser.
- Do not edit production config without approval.

## Case 2 - Script Blocked By Execution Policy

Input:

```text
Import-Module failed because running scripts is disabled on this system.
```

Expected output:

- Classify as permission/environment policy.
- Recommend process-scoped execution policy only for local test if appropriate.
- Do not recommend changing global policy as the first step.

## Case 3 - Missing Node Dependency

Input:

```text
Error: Cannot find module 'zod'
```

Expected output:

- Classify as dependency resolution.
- Ask for package manager and lockfile.
- Recommend install or lockfile repair plus validation command.

## Case 4 - Agent Tool Timeout

Input:

```text
Tool call exceeded 30000ms timeout.
```

Expected output:

- Classify as timeout.
- Recommend smaller batch, retry/backoff, and observable checkpoint.
- Do not suggest unsafe rate-limit bypass.
