const fs = require("fs");
const path = require("path");

const sourceArg = process.argv[2];

if (!sourceArg) {
  console.error("Usage: npm run audit:source -- <source-folder>");
  process.exit(1);
}

const sourceRoot = path.resolve(sourceArg);
if (!fs.existsSync(sourceRoot) || !fs.statSync(sourceRoot).isDirectory()) {
  console.error(`Source folder not found: ${sourceRoot}`);
  process.exit(1);
}

const highRiskNameTerms = [
  "god",
  "terminal",
  "self",
  "security",
  "update",
  "swarm",
  "orchestrator",
];

const generatedOrUnsafeTerms = [
  "backup",
  "broken",
  "archive",
  "archived",
  "original",
  "log",
  ".zip",
];

const mojibakeSignals = ["�", "锛", "璇", "閿", "畖", "绫", "鎿", "瀵"];

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...walk(full));
    } else if (entry.isFile()) {
      files.push(full);
    }
  }
  return files;
}

function hasMojibake(file) {
  const ext = path.extname(file).toLowerCase();
  if (![".md", ".json", ".ps1", ".psm1", ".py", ".txt"].includes(ext)) {
    return false;
  }
  let content = "";
  try {
    content = fs.readFileSync(file, "utf8");
  } catch {
    return false;
  }
  return mojibakeSignals.some((signal) => content.includes(signal));
}

const topDirs = fs
  .readdirSync(sourceRoot, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

const rows = [];
for (const name of topDirs) {
  const dir = path.join(sourceRoot, name);
  const files = walk(dir);
  const lowerName = name.toLowerCase();
  const riskFlags = [];

  const suspiciousFiles = files.filter((file) => {
    const rel = path.relative(dir, file).toLowerCase();
    return generatedOrUnsafeTerms.some((term) => rel.includes(term));
  });

  const mojibakeFiles = files.filter(hasMojibake);
  const skillMd = fs.existsSync(path.join(dir, "SKILL.md"));
  const readme = fs.existsSync(path.join(dir, "README.md"));
  const tests = files.filter((file) => /\\tests?\\|test|quick-test/i.test(file));
  const scripts = files.filter((file) =>
    [".ps1", ".psm1", ".py", ".ahk", ".bat"].includes(
      path.extname(file).toLowerCase(),
    ),
  );
  const configs = files.filter((file) => path.extname(file).toLowerCase() === ".json");

  if (!skillMd) riskFlags.push("missing-skill-md");
  if (!readme) riskFlags.push("missing-readme");
  if (tests.length === 0) riskFlags.push("missing-tests");
  if (suspiciousFiles.length > 0) riskFlags.push("backup-or-generated-files");
  if (mojibakeFiles.length > 0) riskFlags.push("mojibake");
  if (highRiskNameTerms.some((term) => lowerName.includes(term))) {
    riskFlags.push("high-permission-name");
  }

  const score =
    (skillMd ? 2 : 0) +
    (readme ? 2 : 0) +
    (tests.length > 0 ? 2 : 0) +
    (scripts.length <= 5 ? 1 : 0) +
    (configs.length <= 5 ? 1 : 0) -
    suspiciousFiles.length -
    mojibakeFiles.length -
    (riskFlags.includes("high-permission-name") ? 2 : 0);

  const hasHighPermissionName = riskFlags.includes("high-permission-name");
  const recommendation =
    score >= 4 && mojibakeFiles.length === 0 && !hasHighPermissionName
      ? "candidate"
      : score >= 0
        ? "cleanup-first"
        : "hold";

  rows.push({
    name,
    files: files.length,
    scripts: scripts.length,
    configs: configs.length,
    tests: tests.length,
    skillMd,
    readme,
    suspiciousFiles: suspiciousFiles.length,
    mojibakeFiles: mojibakeFiles.length,
    riskFlags,
    importScore: score,
    recommendation,
  });
}

console.log(JSON.stringify({ sourceRoot, generatedAt: new Date().toISOString(), rows }, null, 2));
