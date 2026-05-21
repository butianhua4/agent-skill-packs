# Source Maximization Plan

This repo uses two local sources differently:

1. `OpenClaw custom skill pack` - user-owned source material that can be audited,
   cleaned, rebuilt, and imported as reusable packs.
2. `claude-code-source-code-backup` - unclear-license source material used only
   for high-level architecture inspiration. Do not copy source code, file-level
   implementation, naming patterns that imply ownership, or proprietary logic.

## OpenClaw Utilization Path

Highest-value candidates:

| Source folder | Rebuilt as | Commercial value | Import status |
| --- | --- | --- | --- |
| `auto-debugger` | `auto-debugger-skill-pack` | Debug failed workflows | Done |
| `client-proposal-generator` | `client-proposal-generator` | Faster buyer proposals | Done |
| `error-handler` | `error-handler-skill-pack` | Safer automation design | Done |
| `progress-reporter` | `progress-reporter-skill-pack` | Buyer updates and reporting | Done |
| `delivery-packager` | `delivery-packager-skill-pack` | Clean service handoff | Done |
| `market-radar` | `market-opportunity-radar-skill-pack` | Find sellable opportunities | Done |
| `markdown-to-social` | `content-distribution-skill-pack` | Repost proof assets | Done |
| `product-builder` | `offer-builder-skill-pack` | Turn market signal into product | Done |
| `seo-optimizer` | `aeo-search-readiness-skill-pack` | Search visibility service | Done |
| `git-automation` | Candidate safe Git workflow pack | Public repo delivery | Later |

## Claude Backup Inspiration Only

Allowed inspiration themes:

- Structured command surfaces
- Session/history separation
- Tool boundary design
- Cost/effort tracking ideas
- Event/log based debugging
- Permission and trust gates
- Progressive disclosure for plugins and skills

Not allowed:

- Copying TypeScript source
- Reusing private implementation details
- Shipping files derived from the backup
- Claiming compatibility based on copied internals

## Next Import Queue

1. `git-automation` as a safe public-repo release helper with no private repo
   access or high-permission operations.
2. Add demo input/output examples for the highest-value packs.

## Validation Rule

Every imported pack must pass:

```bash
npm run preflight
```

Every imported pack must include:

- `README.md`
- `SKILL.md`
- `SAFETY.md`
- `TEST_CASES.md`
- `DELIVERY_TEMPLATE.md`
