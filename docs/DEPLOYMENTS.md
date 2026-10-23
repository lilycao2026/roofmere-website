# What is online, where — Roofmere deployments

One row per live site or listing. Update this file in the same PR that adds, renames, redeploys or retires one. "Built from" says exactly which code is on the site; a site is not updated by merging code.

Last updated: 2026-10-23.

**Target: two sites.** The product website, and one Roofmere App that is Free by default, unlocks Pro with a licence, and shows the sample family at `?sample`. The Pro test build below is retired once the App's sample shows the Pro features. Private Cloud buyers deploy their own copy; we host only the store listing and the setup guide.

| What | URL | Platform · project name | Built from | Visibility | Purpose / notes |
| --- | --- | --- | --- | --- | --- |
| Product website | https://roofmere.com/ (old https://lilycao2026.github.io/roofmere-website/ redirects here) | GitHub Pages · repo `roofmere-website`, custom domain via `CNAME` | `main` branch, published automatically | Public | Marketing page and guides. Search Console: submit `https://roofmere.com/sitemap.xml` under a `roofmere.com` property. |
| **Roofmere App** — Local Free today; Pro will unlock here once licensing exists (offline, installable) | https://roofmere.netlify.app | Netlify (Drop) · `roofmere` (was `serene-travesseiro-5ee272`, then `roofmere-local-free`; final name set 2026-10-18) | `node build-local.js` from roofmere-template commit `d8334e3` (L-01, **not yet merged into `dev`**) · deployed 2026-10-17 by hand | Public | Linked from the website's Local Free card. Planned to be the only app site: Free, licensed Pro and `?sample`. Visitors' data lives in their browser **under this exact address**: never rename it again without a backup/restore path. |
| **Local Pro sample** | https://cute-tarsier-c639b4.netlify.app/?sample | Netlify · `cute-tarsier-c639b4` | A Local **Pro test build** (`build-local.js --pro`), around 2026-10-14; exact commit not recorded | Public | Website links only to `?sample` (fictional family, nothing saved). Without `?sample` this site is a working **unlicensed Pro** that saves data: not for real customers. Rebuild it from `dev` once L-01 is merged. |
| Private Cloud beta (store) | https://lilycao.gumroad.com/l/roofmere | Gumroad · product `roofmere` | Legacy Basic / Family / Complete ZIPs | Public | Current paid beta. |
| Cloud setup video | https://youtu.be/JVVJcDkPMus | YouTube | — | Public / unlisted (check) | Linked from the Private Cloud card. |
| Setup guide (wizard) | to confirm | repo `roofmere-setup-preview` | `main` | to confirm | Buyers use it to install Private Cloud; record its URL here. |

## Rules
- **Local sites keep data per address.** Changing the Netlify project name changes the address, and the data people saved under the old one does not follow. Pick the final name first.
- **Test builds:** new Netlify Drop sites stay Private until checked; give each a row here, with the commit it was built from.
- **Pro test builds:** the website links to them only with `?sample`. They are replaced by licensed Pro once licensing exists.

## Domain
- `roofmere.com`, bought 2026-10-23 at Cloudflare Registrar for 1 year; due for renewal around 2027-10-23. The owner signs in with their Gmail account (address deliberately not written here: this repo is public).
- DNS: apex A records to GitHub Pages, `www` CNAME to `lilycao2026.github.io`, all DNS-only (proxy off). Keep auto-renew, two-step login and transfer lock on.
