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
- `docs/SOURCE_MAXIMIZATION_PLAN.md` - plan for safely reusing the user's
  OpenClaw material while using Claude backup material only as architecture
  inspiration.

## Sellable Bundle

- `docs/AGENT_SKILL_PACK_LISTING.md` - Fiverr and Chinese platform listing copy
  for selling custom agent/skill packs as a service.
- `docs/AGENT_SKILL_PACK_PORTFOLIO.md` - compact proof page for showing the
  current skill-pack bundle to buyers.
- `docs/AGENT_SKILL_PACK_UPLOAD_CHECKLIST.md` - step-by-step upload checklist
  for Fiverr, GitHub visibility, OpenClaw community posts, and domestic service
  platforms.
- `docs/AGENT_SKILL_PACK_BUYER_REPLY_PACK.md` - buyer replies and Custom Offer
  drafts for converting qualified inquiries into scoped work.
- `assets/agent-skill-pack-bundle-cover.svg` - reusable cover image for the
  skill-pack bundle.

## Current Starter Packs

| Pack | Use case | Status |
| --- | --- | --- |
| `ai-workflow-log-debug-skill` | Diagnose failed AI agent or automation logs and produce a scoped fix report. | Ready for review |
| `auto-debugger-skill-pack` | Classify automation failures and produce safe fix plans with validation steps. | Cleaned from OpenClaw concept |
| `agent-skill-pack-auditor` | Audit a folder of skills, classify risks, and create an upgrade plan. | Ready for review |
| `client-proposal-generator` | Generate scoped proposals for AI automation, agent workflow, or skill-pack services. | Tested source concept, cleaned pack |
| `content-distribution-skill-pack` | Turn one GitHub/Fiverr/proof asset into safe multi-platform launch copy. | Rebuilt from OpenClaw concept |
| `delivery-packager-skill-pack` | Package completed service work into a clean handoff bundle with manifest, QA notes, and buyer instructions. | Rebuilt from OpenClaw concept |
| `error-handler-skill-pack` | Design structured error handling, logging, recovery, and prevention plans. | Rebuilt from OpenClaw concept |
| `market-opportunity-radar-skill-pack` | Turn public market notes into ranked sellable AI agent and automation opportunities. | Rebuilt from OpenClaw concept |
| `offer-builder-skill-pack` | Turn a market signal, proof asset, or skill pack into a sellable service package. | Rebuilt from OpenClaw concept |
| `progress-reporter-skill-pack` | Turn technical work logs into buyer-ready progress updates, status reports, and next-step summaries. | Rebuilt from OpenClaw concept |

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

## Add A New Pack

```bash
npm run new:pack -- workflow-debug-skill
npm run preflight
```

See `docs/PACK_TEMPLATE.md` for the naming and quality standard.

## Audit A Source Folder

```bash
npm run audit:source -- "C:\Users\33065\Desktop\OpenClaw自定义技能包"
```

See `docs/SOURCE_AUDIT.md` before importing local or third-party material.

## Roadmap

1. Import and clean the safest OpenClaw packs first.
2. Add tests for each imported pack.
3. Publish small, buyer-friendly packs for Fiverr/GitHub visibility.
4. Add examples for OpenClaw, Codex, Claude-style skill runners, and generic agent
   workflows.
