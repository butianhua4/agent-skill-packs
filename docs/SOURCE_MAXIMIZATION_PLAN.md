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
| `markdown-to-social` | Candidate social distribution pack | Repost proof assets | Next |
| `product-builder` | Candidate offer builder pack | Turn market signal into product | Next |
| `seo-optimizer` | Candidate AEO/SEO audit pack | Search visibility service | Later |
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

1. `markdown-to-social` as a safe content repurposing pack for turning GitHub
   proof assets into Fiverr, X, LinkedIn, Xiaohongshu, and domestic-platform
   posts.
2. `product-builder` as an offer builder pack that converts market-radar output
   into title, package, proof asset, buyer requirements, and delivery template.
3. `seo-optimizer` as an AEO/AI-search readiness pack.

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

