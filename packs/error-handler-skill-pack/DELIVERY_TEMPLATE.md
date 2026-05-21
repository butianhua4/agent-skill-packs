# Error Handling Plan

## Workflow

`<workflow name or description>`

## Error Categories

| Category | Example Signal | Severity | Recovery |
| --- | --- | --- | --- |
| `<category>` | `<signal>` | `<low/medium/high>` | `<safe recovery>` |

## Structured Log Schema

```json
{
  "timestamp": "<ISO timestamp>",
  "level": "<debug|info|warn|error|fatal>",
  "category": "<error category>",
  "message": "<human readable message>",
  "context": {
    "workflow": "<workflow name>",
    "step": "<step name>",
    "requestId": "<optional id>"
  },
  "suggestedAction": "<next safe step>"
}
```

## Recovery Strategy

1. `<safe automated recovery>`
2. `<manual or user-confirmed action>`
3. `<prevention rule>`

## Validation

- [ ] `<test or command>`
- [ ] `<expected result>`

## Client Handoff

`<short summary suitable for delivery>`
