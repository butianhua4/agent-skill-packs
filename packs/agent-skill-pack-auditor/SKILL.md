# Agent Skill Pack Auditor

## Purpose

Inspect a folder of agent or skill files and produce a safe migration plan.

## Inputs

- Folder path or file list
- Intended platform
- Whether files are user-owned, third-party, or unclear
- Target output format
- Commercial use case

## Workflow

1. Inventory directories, file types, tests, configs, scripts, and docs.
2. Mark source ownership: user-owned, public, unclear, or prohibited.
3. Classify each pack by commercial value and operational risk.
4. Detect backups, generated logs, broken variants, and archives.
5. Recommend import priority.
6. Create missing standard files: README, SKILL, SAFETY, TEST_CASES, and
   DELIVERY_TEMPLATE.
7. Run or define validation checks before publishing.

## Output

Use `DELIVERY_TEMPLATE.md` and include a pack-by-pack migration table.

## Boundaries

- Do not copy unclear-license or leaked proprietary source.
- Do not publish secrets, tokens, logs with private data, or credentials.
- Do not import high-permission scripts without explicit safety boundaries.
- Do not claim runtime support until tests pass.
