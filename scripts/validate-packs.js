const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const packsDir = path.join(root, "packs");
const requiredFiles = [
  "README.md",
  "SKILL.md",
  "SAFETY.md",
  "TEST_CASES.md",
  "DELIVERY_TEMPLATE.md",
];

const requiredSkillSections = [
  "Purpose",
  "Inputs",
  "Workflow",
  "Output",
  "Boundaries",
];

const riskyPhrases = [
  "send payment outside",
  "share your password",
  "private key",
  "seed phrase",
  "bypass kyc",
  "disable security",
  "open external payment",
];

const safeContextMarkers = [
  "do not",
  "never",
  "refuse",
  "refusal",
  "requires user action",
  "customer action",
  "not allowed",
  "prohibited",
  "redirect",
  "hold",
];

function read(file) {
  return fs.readFileSync(file, "utf8");
}

function fail(message) {
  console.error(`Pack validation failed: ${message}`);
  process.exitCode = 1;
}

if (!fs.existsSync(packsDir)) {
  fail("packs/ directory is missing.");
  process.exit();
}

const packNames = fs
  .readdirSync(packsDir, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

if (packNames.length === 0) {
  fail("packs/ has no pack directories.");
}

for (const packName of packNames) {
  const packDir = path.join(packsDir, packName);

  for (const requiredFile of requiredFiles) {
    const file = path.join(packDir, requiredFile);
    if (!fs.existsSync(file)) {
      fail(`${packName} is missing ${requiredFile}.`);
    }
  }

  const skillPath = path.join(packDir, "SKILL.md");
  if (fs.existsSync(skillPath)) {
    const skill = read(skillPath);
    for (const section of requiredSkillSections) {
      if (!skill.includes(`## ${section}`)) {
        fail(`${packName}/SKILL.md is missing section "${section}".`);
      }
    }
  }

  for (const requiredFile of requiredFiles) {
    const file = path.join(packDir, requiredFile);
    if (!fs.existsSync(file)) continue;
    const lines = read(file).toLowerCase().split(/\r?\n/);
    for (const phrase of riskyPhrases) {
      for (const line of lines) {
        if (!line.includes(phrase)) continue;
        const isSafeContext = safeContextMarkers.some((marker) =>
          line.includes(marker),
        );
        if (!isSafeContext) {
          fail(`${packName}/${requiredFile} contains risky phrase "${phrase}".`);
        }
      }
    }
  }
}

if (!process.exitCode) {
  console.log(`Validated ${packNames.length} pack(s): ${packNames.join(", ")}`);
}
