# Pack Template Guide

Use this when adding a new pack manually or with:

```bash
npm run new:pack -- workflow-debug-skill
```

## Naming

- Use lowercase kebab-case.
- Name the buyer problem, not the internal implementation.
- Prefer small, focused packs.

Good:

- `auto-debugger-skill-pack`
- `client-proposal-generator`
- `ci-risk-gate-agent`

Avoid:

- `misc-tools`
- `god-mode-agent`
- `super-agent-everything`

## Required Files

Every pack must include:

- `README.md`
- `SKILL.md`
- `SAFETY.md`
- `TEST_CASES.md`
- `DELIVERY_TEMPLATE.md`

## Minimum Quality Bar

- The README explains who buys or uses the pack.
- The skill has Purpose, Inputs, Workflow, Output, and Boundaries sections.
- Safety rules explicitly handle credentials, payments, private data, external
  links, production access, and validation.
- Test cases include missing input or unsafe-request behavior.
- Delivery template can be pasted into a client handoff.

## Validation

Run:

```bash
npm run preflight
```
