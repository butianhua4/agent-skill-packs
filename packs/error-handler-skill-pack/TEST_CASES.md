# Test Cases

## Case 1 - Missing File Error

Input:

```text
ENOENT: no such file or directory, open './config.json'
```

Expected output:

- Classify as missing file or configuration error.
- Recommend path validation and preflight check.
- Include a logging schema field for `expected_path`.

## Case 2 - Permission Error

Input:

```text
Access denied while writing report.json
```

Expected output:

- Classify as permission error.
- Recommend checking path and write permission.
- Mark elevated permission changes as user-confirmed.

## Case 3 - Flaky API Timeout

Input:

```text
Request timed out after 30000ms
```

Expected output:

- Classify as timeout/network error.
- Recommend retry with backoff and timeout budget.
- Do not recommend bypassing rate limits.

## Case 4 - Schema Mismatch

Input:

```text
Expected field "riskLevel" but got "risk_level"
```

Expected output:

- Classify as schema mismatch.
- Recommend input/output contract validation.
- Include prevention rule for schema tests.
