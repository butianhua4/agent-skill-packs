# Error Handler Skill Pack

## Purpose

Design a safe, structured error handling and logging plan for an automation,
agent, script, or CI workflow.

## Inputs

- Workflow or script description
- Current error examples
- Runtime environment
- Existing logging format, if any
- Desired alerting or reporting behavior
- Constraints such as no production access or no private credentials

## Workflow

1. Identify the workflow boundary and expected success path.
2. Classify known errors into syntax, runtime, dependency, permission, network,
   configuration, schema, data, or unknown.
3. Define a structured log schema with timestamp, level, category, message,
   context, and suggested action.
4. Map each error category to a recovery strategy.
5. Separate safe automated recovery from actions requiring user confirmation.
6. Add prevention rules such as validation, retries, timeouts, and preflight
   checks.
7. Prepare a client-facing incident or implementation report.

## Output

Use `DELIVERY_TEMPLATE.md`.

## Boundaries

- Do not request credentials, payment details, KYC data, private keys, or tokens.
- Do not open unknown customer external links.
- Do not silently change production logging, alerting, or recovery behavior.
- Do not recommend global security-policy changes as a first step.
- Do not claim a recovery path is safe unless its validation condition is clear.
