# Agent Skill Packs

Reusable AI agent and skill packs for business workflows.

This repository is a public library of practical agent packs, skill packs, prompts,
trigger rules, safety boundaries, test cases, and delivery templates. The goal is
to make agent work easier to inspect, package, sell, and maintain.

## What Is Included

- `packs/` - reusable agent and skill packs with clear scope, safety rules, tests,
  and delivery templates.
- `docs/` - import audits, quality standards, testing notes, and roadmap.
- `scripts/validate-packs.js` - local quality gate for pack structure and content.

## Current Starter Packs

| Pack | Use case | Status |
| --- | --- | --- |
| `ai-workflow-log-debug-skill` | Diagnose failed AI agent or automation logs and produce a scoped fix report. | Ready for review |
| `agent-skill-pack-auditor` | Audit a folder of skills, classify risks, and create an upgrade plan. | Ready for review |

## Pack Standard

Every pack should include:

- `README.md` - buyer/user-facing summary
- `SKILL.md` - executable operating instructions
- `SAFETY.md` - boundaries, refusals, and escalation rules
- `TEST_CASES.md` - realistic validation scenarios
- `DELIVERY_TEMPLATE.md` - reusable client-facing output

## Source Policy

This repo can reuse the user's own OpenClaw skill-pack material after audit and
cleanup. It must not copy leaked, private, proprietary, or unclear-license source
code. Claude Code backup material is used only as architecture inspiration, not
as copied implementation.

## Validate

```bash
npm run validate
```

## Roadmap

1. Import and clean the safest OpenClaw packs first.
2. Add tests for each imported pack.
3. Publish small, buyer-friendly packs for Fiverr/GitHub visibility.
4. Add examples for OpenClaw, Codex, Claude-style skill runners, and generic agent
   workflows.
