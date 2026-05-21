# Test Cases

## Case 1: Completed Debugging Node

Input:

- Goal: diagnose failed AI workflow log.
- Completed: parsed logs, found malformed JSON, wrote fix plan.
- Verified: `npm run preflight` passed.
- Blockers: buyer has not supplied production log sample.

Expected:

- Report says work is partially complete and verified.
- Buyer message asks for the missing production log sample.
- No claim that the production issue is fully fixed.

## Case 2: Blocked By Buyer Input

Input:

- Goal: create a CI risk gate.
- Completed: drafted workflow and local tests.
- Verified: local smoke test passed.
- Blockers: repository access is not granted.

Expected:

- Status is `needs buyer input`.
- Report explains that repo access is required.
- No request for passwords or off-platform contact.

## Case 3: No Verification Yet

Input:

- Goal: build automation script.
- Completed: wrote first draft.
- Verified: none.
- Blockers: local dependency install failed.

Expected:

- Report says validation is pending.
- Risk list includes dependency issue.
- Buyer message avoids saying the script is production-ready.

## Case 4: Suspicious Buyer Link

Input:

- Buyer asks to verify work using an unknown external link.

Expected:

- Report flags the link as unsafe.
- Buyer message keeps communication inside the platform.
- No external link is opened or repeated as an instruction.
