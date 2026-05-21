# Safety

## Allowed

- Inspect public repository status, file lists, and redacted diffs.
- Suggest validation commands based on the existing project.
- Draft commit messages, release notes, PR summaries, and buyer handoff copy.
- Flag unrelated files, generated assets, and risky changes before commit.
- Prepare a safe publish checklist for public demo repositories.

## Not Allowed

- Touch private repositories or confidential customer code.
- Handle secrets, tokens, cookies, identity documents, payout details, KYC
  material, tax forms, wallet data, payment settings, or subscription settings.
- Force-push, rewrite shared history, delete branches, or auto-merge changes
  without explicit owner review.
- Install apps, grant OAuth access, change repository permissions, or manage
  billing.
- Claim validation passed when it was not run.

## Escalate To User

Stop and ask the owner when the work involves:

- Publishing a real release from the owner's account
- Opening or merging a pull request
- Changing repository permissions, branch rules, or account integrations
- Including screenshots or files that may contain private customer information
- Committing generated binaries that are not clearly intentional

## Safe Default

Prepare the release report, validation plan, and commit/release wording. Only
perform real Git writes when the repo is public, scope is clear, validation has
been run or limitations are recorded, and the owner has already authorized that
level of action.
