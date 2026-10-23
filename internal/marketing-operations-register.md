# Roofmere — Marketing Operations Register

Internal working document. Do not publish this document on the public website. Never store passwords, recovery codes, API keys, tokens, or 2FA backup codes in Git.

## Launch gate
- Product: stable public Local Free and sample demo verified on mobile; Netlify floating UI removed.
- Commerce: Lemon Squeezy live checkout, license activation, refund path and customer feedback tested end-to-end.
- Operations: PR #74 (refund workflow) and PR #75 (orders table / sync) reviewed and tested before merge or deployment.
- Separate TEST transactions from REAL revenue.

## Accounts and channels
Fill in only verified details. Store credentials in Apple Passwords or a dedicated password manager, and record the vault item name here.

| Channel | Purpose | Login URL | Username / handle | Email alias (optional) | Password manager item | Status | Next action |
|---|---|---|---|---|---|---|---|
| Google Search Console | Indexing and performance | https://search.google.com/search-console | TBD | | | New domain unverified | Verify roofmere.com; submit sitemap |
| GitHub | Website and product development | https://github.com | lilycao2026 (repository owner; confirm login) | | | Existing | Maintain website |
| Cloudflare | Domain and DNS | https://dash.cloudflare.com | TBD | | | roofmere.com DNS set | Record ownership details |
| Netlify | Hosting | https://app.netlify.com | TBD | | | Existing | Verify public vs test sites |
| Gumroad | Sales | https://gumroad.com | TBD | | | Existing | Verify live checkout |
| Lemon Squeezy | Sales and licensing | https://app.lemonsqueezy.com | TBD | | | Testing | Complete license/refund UAT |
| X | Product announcements | https://x.com | Not created/confirmed | | | Planned | Reserve brand handle |
| Reddit | Participate in relevant communities | https://www.reddit.com | Not created/confirmed | | | Planned | Read each community's promotion rules |
| Indie Hackers | Founder build-in-public | https://www.indiehackers.com | Not created/confirmed | | | Planned | Prepare genuine founder story |
| Product Hunt | Launch discovery | https://www.producthunt.com | Not created/confirmed | | | Planned | Wait for stable checkout |

## Content pipeline
| ID | Channel | Topic / working title | Audience / search intent | Stage | Planned publish | Published URL | Outcome |
|---|---|---|---|---|---|---|---|
| SEO-001 | Roofmere Guides | How to Track Your Net Worth Without Linking Bank Accounts | Privacy-first manual net-worth tracking | Published | | https://roofmere.com/guides/track-net-worth-without-bank-connections/ | Indexing pending |
| SEO-002 | Roofmere Guides | How to Estimate Household Spending Without Tracking Every Transaction | Financial planning without detailed bookkeeping | Idea | | | |
| POST-001 | X / Indie Hackers | Why I built a household finance dashboard without bank connections | Product story | Draft needed | | | |
| POST-002 | Reddit | What do people actually need from a household financial dashboard? | Research and discussion, not disguised advertising | Draft needed | | | |

## Publishing workflow
1. Draft ahead of time. Distinguish educational content from promotional posts.
2. Review facts, product claims, pricing, links, and community rules.
3. Publish only to channels where promotion is allowed; avoid repetitive cross-post spam.
4. Log publish date, URL, impressions, clicks, signups, trials, and purchases when available.
5. Review monthly; optimize for qualified visitors and purchases, not vanity impressions.

## SEO checklist
- Domain: https://roofmere.com/
- Sitemap: https://roofmere.com/sitemap.xml
- robots.txt: https://roofmere.com/robots.txt
- GitHub Pages CNAME and canonical URLs updated October 23, 2026.
- Google Search Console domain verification and sitemap submission still pending; no claim of Google indexing.
- Recheck crawl/indexing after verification and allow for delays.

## Safety and ownership
- No plaintext credentials, tokens, license keys, recovery phrases, or customer data here.
- Enable MFA on sales, hosting, domain and social accounts.
- This file is internal operations planning, not public website content. Keep it out of GitHub Pages published files.
