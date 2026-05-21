# Delivery Template

## Safe Git Release Report: [Repository / Change Name]

### Executive Summary

- Repository:
- Release goal:
- Target audience:
- Current readiness:
- Main risk:
- Recommended next action:

### Release Readiness Score

| Category | Score | Notes |
| --- | --- | --- |
| Scope clarity | /20 | |
| Change separation | /15 | |
| Validation evidence | /20 | |
| Release notes clarity | /15 | |
| Buyer/community handoff | /15 | |
| Safety boundaries | /15 | |

### Changed-File Risk Map

| Area | Files | Risk | Recommended action |
| --- | --- | --- | --- |
| Docs | | | |
| Tests / examples | | | |
| Runtime code | | | |
| Build / CI config | | | |
| Generated assets | | | |
| Unknown | | | |

### Validation Plan And Results

| Command or check | Result | Evidence | Residual risk |
| --- | --- | --- | --- |
| [command] | [passed/failed/not run] | [output summary] | [risk] |

### Commit Message Options

1. `[message]`
2. `[message]`
3. `[message]`

### Release Notes Draft

#### What Changed

- [Change]

#### Why It Matters

- [Buyer/user value]

#### How To Verify

- [Command or manual check]

#### Known Limits

- [Limit]

### Buyer / Community Handoff Message

[Short message explaining what changed, how it was verified, and what the next
step is.]

### Stop Conditions

- [ ] Requires private repository access
- [ ] Requires secret values or credentials
- [ ] Requires payout, KYC, tax, payment, OAuth, or account-permission changes
- [ ] Requires destructive Git history operation
- [ ] Validation failed or was not run

### Next 30-Minute Action

[Run the missing validation, split unrelated files, draft release notes, or
prepare the commit.]
