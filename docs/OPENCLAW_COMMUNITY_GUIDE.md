# OpenClaw Community Guide

This guide is for OpenClaw or agent-workflow community readers who want to test,
review, request, or adapt the public packs in this repository.

Repository:
https://github.com/butianhua4/agent-skill-packs

## What This Repo Provides

This repository contains 12 reusable AI agent and skill packs. Each pack is
designed as a small, inspectable operating unit rather than a loose prompt.

Every pack should include:

- `README.md` - what the pack does and when to use it
- `SKILL.md` - operating instructions
- `SAFETY.md` - boundaries, refusals, and escalation rules
- `TEST_CASES.md` - realistic test scenarios
- `DELIVERY_TEMPLATE.md` - reusable buyer/client-facing output

## Quick Local Check

Clone the repository and run:

```bash
npm install
npm run preflight
```

Expected result:

```text
Validated 12 pack(s)
```

The validator checks pack structure and basic safety wording. It does not send
data to external services.

## How To Try A Pack Manually

1. Open a pack under `packs/`.
2. Read `README.md` to understand the use case.
3. Read `SAFETY.md` before using the pack on real client or workflow material.
4. Pick one scenario from `TEST_CASES.md`.
5. Run the pack logic manually using `SKILL.md` as the operating procedure.
6. Compare the output shape against `DELIVERY_TEMPLATE.md`.

Use redacted examples only. Do not paste private customer data, credentials,
payment details, wallet details, tokens, cookies, KYC documents, or production
secrets into any agent runner.

## Best Packs To Start With

| Need | Start here |
| --- | --- |
| Debug a failed AI agent run | `packs/ai-workflow-log-debug-skill/` |
| Audit a folder of prompts or skills | `packs/agent-skill-pack-auditor/` |
| Turn a rough idea into a scoped service | `packs/offer-builder-skill-pack/` |
| Write a buyer-ready progress update | `packs/progress-reporter-skill-pack/` |
| Package completed work for handoff | `packs/delivery-packager-skill-pack/` |
| Prepare a public repo release | `packs/safe-git-release-helper-skill-pack/` |

## Suggested Community Feedback

Open a GitHub issue with one of these request types:

- Pack idea: a workflow you repeat often and want packaged
- Test case: a realistic redacted scenario that should be covered
- Safety gap: a risky instruction, missing refusal, or unclear boundary
- Delivery gap: missing output fields in `DELIVERY_TEMPLATE.md`
- Compatibility note: how the pack behaves in an OpenClaw-style runner

Useful issue format:

```text
Pack or workflow:
What I tried:
Expected output:
Actual output or gap:
Safety concern, if any:
Example input, redacted:
```

## What Not To Submit

Do not submit:

- Login credentials
- API keys or tokens
- Session cookies
- Buyer messages with names or private details
- Payment, payout, KYC, tax, wallet, or banking material
- Private repository code
- Proprietary source code you do not have permission to share

## How To Request A New Pack

Use this template:

```text
Workflow name:
Who uses it:
Input material:
Expected output:
What must be refused:
What a good test case looks like:
How this could become a reusable delivery template:
```

Good candidates are repeatable workflows that can be validated with redacted
examples in 30-120 minutes.

## Roadmap For Community Use

Next community-facing improvements:

1. Add runner-specific notes for OpenClaw-style skill loading.
2. Add a `CONTRIBUTING.md` with pack naming and review rules.
3. Add more filled sample outputs for popular packs.
4. Add issue templates for pack requests, safety gaps, and test cases.
5. Publish a small release post using `docs/GITHUB_RELEASE_DRAFT.md`.

