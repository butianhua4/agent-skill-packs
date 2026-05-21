# AI Workflow Log Debug Skill

## Purpose

Turn messy AI workflow logs into a scoped diagnosis and client-ready fix report.

## Inputs

- Error log or failed run excerpt
- Workflow type, if known
- Expected behavior
- Recent change, if known
- Constraints such as no production access or no private credentials

## Workflow

1. Identify the system boundary: model, tool, script, CI, workflow runner, or API.
2. Classify the failure: syntax, schema, permission, timeout, missing dependency,
   rate limit, unsafe tool call, or unclear.
3. Extract the smallest reproducible failure signal.
4. Separate evidence from assumptions.
5. Produce a fix plan with low-risk first steps.
6. Mark anything requiring customer access, payment, credentials, or admin approval
   as customer action.
7. Return a concise report with confidence level and next step.

## Output

Use `DELIVERY_TEMPLATE.md` and fill every section.

## Boundaries

- Do not request passwords, private keys, seed phrases, payment access, or KYC data.
- Do not open unknown customer external links.
- Do not claim a fix is complete unless it was validated.
- Do not modify production systems without explicit user approval.
- If the issue requires private data, ask for a redacted reproduction instead.
