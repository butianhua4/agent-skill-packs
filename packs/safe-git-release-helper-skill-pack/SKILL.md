# Safe Git Release Helper Skill

## Purpose

Prepare public repository changes for safe release, proof, and buyer handoff.
Use this when a public GitHub repo, demo repo, skill-pack repo, or open-source
patch needs change review, validation planning, commit wording, release notes,
or a delivery-ready summary.

This is a controlled Git workflow helper. It improves release discipline without
performing risky account, history, credential, or private-repo operations.

## Inputs

Accept one or more of:

- `git status --short`
- Changed file list
- Diff summary or selected diff snippets
- Validation commands and results
- README, docs, release notes, package metadata, or demo output
- Target audience: buyer, open-source maintainer, community, or internal owner
- Release goal: bug fix, docs update, demo asset, skill pack, template, or small
  feature

Reject or stop when inputs require:

- Private repositories or confidential customer code
- Secrets, tokens, cookies, account recovery data, identity documents, payout
  details, KYC material, or tax forms
- Force-push, destructive branch deletion, shared-history rewrite, or automated
  merge without human review
- OAuth, app installation, wallet, payment, subscription, or high-permission
  authorization

## Workflow

1. Identify the release context:
   - Public demo
   - Buyer delivery repo
   - Skill-pack library
   - Open-source contribution
   - Documentation-only update
2. Build a changed-file risk map:
   - Docs only
   - Tests / examples
   - Runtime code
   - Build / CI config
   - Generated assets
   - Unknown or high-risk files
3. Check scope hygiene:
   - Separate unrelated edits
   - Preserve user-created changes
   - Avoid committing local caches, secrets, logs, or binary clutter
   - Confirm whether generated assets are intentional
4. Plan validation:
   - Prefer the repo's existing preflight, test, lint, typecheck, build, or smoke
     command
   - If no command exists, specify the closest manual verification
   - Record command, result, and residual risk
5. Prepare commit and release wording:
   - Choose conventional style only when it matches the repo
   - Make the message explain user or buyer value
   - Avoid hype and unverifiable claims
6. Prepare release notes:
   - What changed
   - Why it matters
   - How to verify
   - Known limits
   - Next recommended step
7. Produce a release decision:
   - Ready to commit
   - Needs validation
   - Needs owner confirmation
   - Stop due to safety boundary

## Output

Return a concise Markdown release report:

- Release readiness score
- Current state summary
- Changed-file risk map
- Validation plan and results
- Commit message options
- Release notes draft
- Buyer/community handoff message
- Stop conditions
- Next 30-minute action

Use this table:

| Area | Status | Risk | Recommended action |
| --- | --- | --- | --- |

## Boundaries

- Do not touch private repositories.
- Do not include secrets, tokens, cookies, confidential buyer files, payout
  details, KYC material, tax forms, or identity documents.
- Do not force-push, rewrite shared history, delete branches, or auto-merge
  without explicit owner instruction and review.
- Do not install GitHub apps, grant OAuth access, change repository permissions,
  or handle billing/subscription settings.
- Do not claim tests passed unless validation was actually run or the limitation
  is clearly stated.
- Prefer a safe release plan over a fast but unclear commit.
