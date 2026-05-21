# Market Opportunity Radar Skill

## Purpose

Convert public market signals into a prioritized list of sellable AI agent,
automation, workflow, or skill-pack opportunities. The goal is to help an
operator decide what to publish, package, or demo next.

## Inputs

Accept one or more of:

- Public market notes or daily intelligence summaries
- Buyer comments, redacted inbox snippets, or platform demand notes
- Competitor service titles, public descriptions, or price ranges
- GitHub issue or community discussion summaries
- Existing offer assets, packs, demos, or portfolio proof

Reject or ask for redaction when inputs contain:

- Passwords, tokens, cookies, secret signing material, payout details, KYC
  material, or ID
  documents
- Private buyer data, private repositories, or off-platform payment requests
- Content from login-only or access-controlled sources unless the user provides a
  safe summary instead of raw data

## Workflow

1. Normalize signals into short evidence bullets.
2. Identify repeated buyer pains, urgent blockers, or willingness-to-pay clues.
3. Group similar signals into opportunity themes.
4. Score each theme:
   - Demand: 1-5
   - Urgency: 1-5
   - Deliverability in 1-2 days: 1-5
   - Proof asset availability: 1-5
   - Safety and platform risk: 1-5, where 5 is low risk
5. Recommend a package:
   - Entry diagnosis
   - Fixed-scope implementation
   - Skill-pack bundle
   - Delivery/reporting template
   - Portfolio/demo asset
6. Produce the next practical action, such as a gig title, buyer reply, demo
   brief, or delivery template.

## Output

Return a concise Markdown report with:

- Executive decision
- Ranked opportunity table
- Top 3 recommended offers
- Suggested title, price band, and delivery promise
- Required proof asset
- Safety boundary
- Next 30-minute action

Use this table format:

| Rank | Opportunity | Evidence | Offer | Price band | Risk | Next action |
| --- | --- | --- | --- | --- | --- | --- |

## Boundaries

- Do not scrape private sites, bypass login walls, or use cookies/session tokens.
- Do not promise guaranteed revenue, search rank, platform approval, or virality.
- Do not recommend work that requires payout, wallet, KYC, tax, payment, or
  account recovery handling.
- Do not use private buyer data; ask for redacted samples.
- Prefer small, verifiable offers that can become a demo or delivery template.
