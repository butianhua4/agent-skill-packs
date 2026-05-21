# Agent Skill Pack Portfolio Proof

This repository demonstrates a reusable agent/skill-pack system for business
workflows. It is designed to show buyers that the service is more than a prompt:
each pack includes operating instructions, safety rules, test cases, and a
delivery template.

## Current Bundle

| Pack | Buyer problem | Proof included |
| --- | --- | --- |
| `ai-workflow-log-debug-skill` | Failed agent or automation logs are hard to inspect. | Debug workflow, scoped fix report template, safety boundaries |
| `auto-debugger-skill-pack` | Automation failures need triage before code changes. | Failure classification, fix-plan workflow, validation cases |
| `agent-skill-pack-auditor` | Existing skills are messy or risky. | Audit checklist, risk classification, upgrade plan template |
| `client-proposal-generator` | Sellers need scoped proposals quickly. | Proposal workflow, tested source concept, delivery template |
| `error-handler-skill-pack` | Workflows lack structured error handling. | Error taxonomy, logging plan, recovery checklist |
| `progress-reporter-skill-pack` | Buyers need clear progress updates. | Progress report workflow, blocker notes, buyer message template |
| `delivery-packager-skill-pack` | Finished work needs clean handoff. | Manifest, setup notes, validation summary, acceptance checklist |

## Why This Matters

Many AI automation projects fail because the workflow is only described as a
chat prompt. A usable skill pack needs:

- a clear input and output contract
- trigger rules
- safe refusal boundaries
- realistic test cases
- delivery templates
- handoff notes for future maintenance

This bundle packages those pieces into a repeatable structure.

## Example Buyer Outcomes

1. A founder can turn an internal SOP into an AI agent workflow.
2. A seller can standardize a repeatable client delivery process.
3. A developer can add safety rules and tests around an existing agent prompt.
4. A team can document agent behavior before connecting tools or private data.

## Validation Evidence

The repository includes a local quality gate:

```bash
npm run preflight
```

Current result:

- 7 packs validated
- required files checked for every pack
- risky phrases screened
- delivery templates included

## Delivery Standard

Every custom pack should include:

- `README.md`
- `SKILL.md`
- `SAFETY.md`
- `TEST_CASES.md`
- `DELIVERY_TEMPLATE.md`

## Client-Safe Boundaries

The service does not handle:

- payment, payout, tax, KYC, wallet, or subscription tasks
- OAuth or high-permission account authorization
- suspicious external buyer links
- private repositories unless explicitly provided and approved by the owner
- unclear-license, leaked, or proprietary source code

## Suggested Offer Positioning

Use this as a portfolio proof for:

- custom AI agent skill packs
- AI workflow SOP packaging
- agent safety boundary design
- agent debugging and handoff documentation
- reusable prompt-to-skill conversion

## Short Portfolio Caption

I build reusable AI agent skill packs with operating instructions, safety rules,
test cases, and delivery templates. This public bundle includes 7 validated
packs covering debugging, error handling, progress reporting, delivery packaging,
proposal generation, and skill audits.
