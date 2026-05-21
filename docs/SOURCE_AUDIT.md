# Source Audit Helper

Use this before importing a local skill folder:

```bash
npm run audit:source -- "C:\Users\33065\Desktop\OpenClaw自定义技能包"
```

The audit script reports:

- missing `SKILL.md`
- missing `README.md`
- missing tests
- backup, broken, archived, original, log, or zip files
- mojibake signals in text files
- high-permission folder names such as terminal, self, update, security, swarm,
  orchestrator, or god
- an import recommendation: `candidate`, `cleanup-first`, or `hold`

This is a static risk screen. It does not prove a pack is safe or functional.
Every imported pack still needs manual cleanup, pack-level test cases, and
`npm run preflight`.
