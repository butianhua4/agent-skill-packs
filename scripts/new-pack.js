const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const packsDir = path.join(root, "packs");
const name = process.argv[2];

function usage() {
  console.error("Usage: npm run new:pack -- <pack-name>");
  process.exit(1);
}

if (!name) usage();

if (!/^[a-z0-9][a-z0-9-]*[a-z0-9]$/.test(name)) {
  console.error(
    "Pack name must be lowercase kebab-case, for example: workflow-debug-skill",
  );
  process.exit(1);
}

const packDir = path.join(packsDir, name);
if (fs.existsSync(packDir)) {
  console.error(`Pack already exists: ${name}`);
  process.exit(1);
}

fs.mkdirSync(packDir, { recursive: true });

const title = name
  .split("-")
  .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
  .join(" ");

const files = {
  "README.md": `# ${title}

One-paragraph summary of the customer problem this pack solves.

Best for:

- <use case one>
- <use case two>
- <use case three>

Deliverable:

- <buyer-facing output one>
- <buyer-facing output two>
`,
  "SKILL.md": `# ${title}

## Purpose

Explain the job this pack performs.

## Inputs

- <input one>
- <input two>

## Workflow

1. <step one>
2. <step two>
3. <step three>

## Output

Use \`DELIVERY_TEMPLATE.md\`.

## Boundaries

- Do not request credentials, payment details, KYC data, or private keys.
- Do not open unknown customer external links.
- Do not claim completion until validation passes.
`,
  "SAFETY.md": `# Safety

Allowed:

- <safe action>

Requires user confirmation:

- <sensitive action>

Hold or refuse:

- Credential collection
- Off-platform payment instructions
- Bypassing platform security
`,
  "TEST_CASES.md": `# Test Cases

## Case 1 - Basic Success

Input:

\`\`\`text
<sample input>
\`\`\`

Expected output:

- <expected result>

## Case 2 - Missing Input

Input:

\`\`\`text
<incomplete input>
\`\`\`

Expected output:

- Ask for the missing safe input.
`,
  "DELIVERY_TEMPLATE.md": `# Delivery Template

## Summary

\`<summary>\`

## Inputs Reviewed

- \`<input>\`

## Findings

- \`<finding>\`

## Recommended Next Step

1. \`<step>\`

## Validation

\`<validation result or next validation command>\`
`,
};

for (const [file, content] of Object.entries(files)) {
  fs.writeFileSync(path.join(packDir, file), content, "utf8");
}

console.log(`Created pack template: packs/${name}`);
