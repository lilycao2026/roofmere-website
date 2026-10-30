# Roofmere Brand & Positioning Change Control

Status: ACTIVE — approved by product owner, 2026-10-28.

## Non-negotiable rule
Brand strategy and approved customer-facing identity are **locked by default**. No AI assistant, contributor, or automated refactor may silently rewrite, reinterpret, or replace them. A request to edit layout, video, UI, CSS, SEO, copy, or content is **not** permission to change the brand.

### Protected decisions
- Product positioning, target audience, core promise, differentiation, edition positioning, and pricing/entitlement claims.
- Approved brand slogan/tagline and exact wording.
- Approved page hero titles/headlines and subtitles/subheadlines, including homepage, Product, and other major landing pages.
- Brand tone, messaging hierarchy, and other explicitly approved strategic language.

### Current approved reference (verify against last owner-approved version)
- Brand slogan: **Your wealth. Your knowledge. Your future.**
- Homepage hero: **Your finances. One clear picture.**
- Product page hero: **Build a financial picture you can review and reuse.**
These are protected baselines, **not permission to replace other previously approved wording**. For any subtitle or wording whose approved version is uncertain, consult the owner or the documented approval history; do not guess or invent a replacement.

### Change process for protected decisions
1. **Stop before editing**. Identify the exact existing wording, where it is used, and the proposed change.
2. **Discuss together** with the product owner: why change, evidence/user feedback, positioning impact, affected pages, alternatives, and tradeoffs.
3. **Obtain explicit approval** of the final exact wording and scope. Silence, general authorization to improve UX, or a previous suggestion is not approval.
4. **Record an ADR** under `docs/brand/decisions/` *before implementation*: date, owner, status, old/new exact copy, rationale, evidence, alternatives, impacts, approved decision, and affected files.
5. Only then implement, limiting edits to the approved scope. Review diffs for accidental brand changes.
6. If the approved wording is not discoverable, leave it unchanged and ask rather than guessing.

### Allowed without special approval
Page layout, responsive styling, video presentation and playback, visual hierarchy, section order, and supporting explanatory content may be improved, **provided protected wording and strategic meaning stay intact**. Corrections to ordinary content must not introduce unsupported product claims.

### Mandatory pre-commit review
Before every website edit, compare the diff against the protected items above. If any protected item changed without its approved ADR, **do not commit**. Keep video/UX fixes separate from brand changes where possible. Apply the same guard to AI-generated code and third-party PR reviews.

## Change log
- 2026-10-28: Product owner established the lock-and-document policy after an unapproved hero headline change during a video UX update. Existing approved brand wording is restored; this document formalizes prevention.
