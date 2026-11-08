# Screenshot and spreadsheet import move to Local Free — edition copy

Date: 2026-11-08 (America/Los_Angeles)
Owner: Lily Cao
Status: Owner requested; exact wording pending owner approval in the pull request

## Decision

The owner moved screenshot import and custom Excel/CSV mapping from Local Pro to Local Free (product decision: roofmere-template ADR-0018, 2026-11-08). The owner asked that the homepage and every other place stating the editions be aligned with it. Local Pro keeps cash-flow transaction imports, planning, reports, AI Context Export and the other Pro features; prices, refund terms, slogan, hero copy and positioning do not change.

## Old → new exact copy

**index.html — "Import & update faster" card**
- Old: Free and Pro include supported app imports (such as Fidelity Full View and Positions). Pro adds screenshot recognition, custom Excel/CSV field mapping and cash-flow transaction imports. Always review recognized figures before saving.
- New: Free and Pro include supported app imports (such as Fidelity Full View and Positions), screenshot recognition and custom Excel/CSV field mapping. Pro adds cash-flow transaction imports. Always review recognized figures before saving.

**index.html — "Import & batch updates" card**
- Old: Free and Pro support basic imports from compatible apps, including supported Fidelity Full View and Positions formats. Pro adds screenshot recognition, custom Excel/CSV field mapping and cash-flow transaction imports. Verify imported amounts.
- New: Free and Pro support basic imports from compatible apps, including supported Fidelity Full View and Positions formats, plus screenshot recognition and custom Excel/CSV field mapping. Pro adds cash-flow transaction imports. Verify imported amounts.

**index.html — Local Free edition card:** new list item after "Basic imports from supported apps…": "Screenshot import and custom Excel/CSV mapping".

**index.html — Local Pro edition card**
- Old: two list items, "Import files: supported Fidelity exports, custom Excel/CSV mapping and cash-flow transactions" and "Screenshot Import (image recognition)".
- New: one list item, "Cash-flow transaction imports". ("Everything in Local Free" above it covers the rest.)

**index.html — comparison table:** "Screenshot Import" and "Custom Excel/CSV field mapping" change from — to ✓ in the Local Free column.

**product.html — editions table, Local Pro row**
- Old: Advanced imports, reporting and AI Context Export with your own data
- New: Cash-flow transaction imports, reporting and AI Context Export with your own data

**get-started.html**
- Old: Local Free is permanently free, with unlimited accounts and properties, the full net-worth dashboard and supported app imports.
- New: Local Free is permanently free, with unlimited accounts and properties, the full net-worth dashboard, supported app imports, screenshot import and custom Excel/CSV mapping.

## Rationale and evidence

Screenshot and spreadsheet reading run in the buyer's browser at no running cost; gating them blocked the fastest way into setup. Reasoning in ADR-0018.

## Alternatives

Free during setup only, then Pro: implemented, then dropped before merge (hard to explain; the gate leaked through Add accounts).

## Timing and impacts

The site deploys from `main` (GitHub Pages). Merge only once the Local release that contains ADR-0018 is live at roofmere.netlify.app; before that, the site would promise Free users a feature their app still locks. Internal docs (launch follow-up, SEO research) are not changed.

## Affected files

`index.html`, `product.html`, `get-started.html`.
