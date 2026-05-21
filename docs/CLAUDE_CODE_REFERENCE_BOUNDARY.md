# Claude Code Reference Boundary

Source inspected:

- `C:\Users\33065\Desktop\claude-code-source-code-backup`

The included README describes this material as leaked source code. This
repository will not copy source code, implementation details, internal file
contents, or proprietary behavior from that backup.

Allowed reference level:

- High-level architecture patterns
- Publicly explainable concepts such as tools, skills, commands, validation,
  memory, hooks, and permission boundaries
- Generic repo organization ideas

Not allowed:

- Copying source code
- Porting implementation logic
- Reusing internal names as a compatibility claim
- Publishing any proprietary files
- Using the backup as a dependency

## Architecture Ideas Worth Recreating From Scratch

- Each tool or skill should define inputs, boundaries, and output shape.
- Skills should be validated before publication.
- Risky operations need explicit permission boundaries.
- Agent work should produce auditable logs and user-facing summaries.
- Commands, skills, and tools should be modular and testable.
