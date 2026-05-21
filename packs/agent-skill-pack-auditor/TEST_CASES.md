# Test Cases

## Case 1 - Mixed Skill Folder

Input: folder contains Markdown, PowerShell, JSON, logs, and backups.

Expected output:

- Inventory by file type.
- Exclude logs and broken backups from import.
- Recommend highest-value safe packs first.

## Case 2 - Unclear Source

Input: folder includes a README stating the source is leaked.

Expected output:

- Mark as architecture-only reference.
- Do not copy source.
- Record boundary note.

## Case 3 - High Permission Pack

Input: skill claims broad filesystem or terminal control.

Expected output:

- Mark high risk.
- Require safety boundaries and tests before release.
