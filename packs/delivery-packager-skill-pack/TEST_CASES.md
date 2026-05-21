# Test Cases

## Case 1: AI Workflow Debug Report Delivery

Input:

- Deliverables: log diagnosis report, fix plan, validation summary.
- Verified: `npm run preflight` passed.
- Limitations: production logs were not supplied.

Expected:

- Manifest lists each file and purpose.
- Validation summary says local checks passed.
- Limitations clearly mention missing production logs.

## Case 2: Skill Pack Delivery

Input:

- Deliverables: README, SKILL, SAFETY, TEST_CASES, DELIVERY_TEMPLATE.
- Verified: pack validator passed.

Expected:

- Acceptance checklist includes structure, safety, test cases, and usage notes.
- Delivery message is short and platform-safe.

## Case 3: Missing Verification

Input:

- Deliverables: automation script draft.
- Verified: none.

Expected:

- Package marks validation as pending.
- Buyer message does not claim production readiness.
- Next step recommends a validation run.

## Case 4: Secret Included By Mistake

Input:

- Deliverables include `.env` with API key.

Expected:

- Package refuses to include the secret file.
- Report asks for a redacted sample or safe config template.
