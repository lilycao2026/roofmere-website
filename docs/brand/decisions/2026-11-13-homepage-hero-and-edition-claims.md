# Homepage hero, "More than a financial snapshot" section, and edition claims

Date: 2026-11-13 (America/Los_Angeles)
Owner: product owner
Status: Approved — the owner approved the exact wording below in chat on 2026-11-13 ("这版我觉得已经可以定稿了"). Not yet committed or deployed.

## Why

- The live hero headline ("Your Finance is / One Clear Picture.") is ungrammatical and does not match the approved baseline in `brand-governance.md` ("Your finances. One clear picture.").
- Three independent AI reviews and one tester found the hero explained the mechanism before the problem, never stated the privacy stance, and left the theme unclear on mobile.
- The owner rejected an "organizer only" page: Roofmere also keeps the records behind the numbers (notes, Document Vault) and lets the household choose what to export, at what level of detail, and for whom (AI-ready export). These appear right after the hero, labelled Pro, so the hero itself describes only what Local Free does.
- The homepage edition claims were out of date. The owner confirmed on 2026-11-13: Home and Money, including screenshot and file import, are in Local Free; Plan, Records and Export are Pro; Local Pro includes Document Vault. Product `dev` code matches (`app/local.js`, `app/core.js`; ADR-0013, ADR-0018).

## Hero — exact copy

| Element | Old | New |
| --- | --- | --- |
| Eyebrow | Household Financial Organizer | unchanged |
| Slogan | Your wealth. Your knowledge. Your future. (above the headline) | unchanged wording; moved below the CTAs |
| Headline | Your Finance is / One Clear Picture. | Your household finances, all in one clear view. |
| Description | Import supported financial files instead of entering everything by hand. Roofmere organizes the information into one household view; you review the results and decide when to update. No bank connection or daily expense tracking required. | Start with a screenshot, a supported file, or a few manual entries. Organize your accounts, investments, property, and debts without connecting your bank or tracking daily expenses. |
| Privacy line | — | Your financial data stays on your device or in your own cloud, not on our servers. |
| CTAs and note | Explore sample data → · See How It Works · Sample data · No sign-up · Changes aren’t saved | unchanged |

The headline matches the approved sharing description ("Your household finances, all in one place.", decision 2026-10-29).

## New section after the hero — exact copy

- Eyebrow: More than a financial snapshot
- Heading: Keep the context. Share what matters.
- Card [Pro]: **Keep more than just the numbers** — Notes, documents, and important details stay alongside your financial information.
- Card [Pro]: **Share on your terms** — Choose what to export, and at what level of detail, for a person or an external AI tool. Nothing is shared automatically.
- Layout: icon on the left and the Pro tag on the right of the same row, above the card title.

Multi-user access (Private Cloud only, self-hosted) stays in the editions section: selective export is not shared household access.

## Edition claims — corrections

- Import cards ("Import & update faster", "Import & batch updates"): screenshot recognition, Excel/CSV with field mapping and mortgage statement PDFs are in Free and Pro. Pro keeps cash-flow transaction imports.
- Local Free card: lists Screenshot Import and Excel/CSV, mortgage statement PDF and supported-app import. Removes "Works offline once opened." (the page elsewhere says offline use is not yet a verified launch promise).
- Local Pro card: removes Screenshot Import and custom Excel/CSV mapping; adds cash-flow transaction import, rental property detail, and Document Vault (files kept in this browser).
- Comparison table: Screenshot Import and Custom Excel/CSV field mapping are ✓ for Local Free; Document Vault is ✓ for Local Pro.
- Document Vault card: tag "Pro editions"; Local Pro keeps files in the browser, Private Cloud in the owner's cloud storage, Local Free has no file uploads.
- Architecture alt text and summary, and the "Which edition includes Document Vault?" FAQ: Local Pro keeps Vault files in browser storage; backups include Vault files as a separate ZIP.

## Evidence for the privacy line

Checked in product `dev` code: Local records are stored in the browser's IndexedDB; screenshot text recognition (Tesseract.js) runs in the browser and the screenshot is not uploaded; Private Cloud records live in the owner's own Supabase project; the Pro licence service holds email, purchase and activation details only, never balances or documents.

## Alternatives considered

- "Your household finances, together in one clear view." with an organizing-only description. Rejected by the owner: it presents Roofmere only as an organizer.
- "Your household finances in one clear view — shared only on your terms." with three points in the hero. Rejected: five-line headline on a phone pushed the first CTA to the bottom of the screen.
- "Your household finances, organized and under your control." Rejected: "control" reads as budgeting language.

## Release dependency

The import changes are listed under "Unreleased" in the product CHANGELOG, and the desktop screenshot-import fix is product PR #213. Publish this website change together with, or after, the app release that contains them. No deploy is authorized by this record.

## Affected files

`index.html` only.
