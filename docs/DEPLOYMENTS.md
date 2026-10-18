# What is online, where — Roofmere deployments

One row per live site or listing. Update this file in the same PR that adds, renames, redeploys or retires one. "Built from" says exactly which code is on the site; a site is not updated by merging code.

Last updated: 2026-10-18.

| What | URL | Platform · project name | Built from | Visibility | Purpose / notes |
| --- | --- | --- | --- | --- | --- |
| Product website | https://lilycao2026.github.io/roofmere-website/ | GitHub Pages · repo `roofmere-website` | `main` branch, published automatically | Public | Marketing page and guides. |
| **Local Free** (offline, installable) | https://roofmere-local-free.netlify.app | Netlify (Drop) · `roofmere-local-free` (was `serene-travesseiro-5ee272`, renamed 2026-10-18) | `node build-local.js` from roofmere-template commit `d8334e3` (L-01, **not yet merged into `dev`**) · deployed 2026-10-17 by hand | Public | Linked from the website's Local Free card. Visitors' data lives in their browser **under this exact address**: never rename it or move Free to a new address without a backup/restore path. |
| **Local Pro sample** | https://cute-tarsier-c639b4.netlify.app/?sample | Netlify · `cute-tarsier-c639b4` | A Local **Pro test build** (`build-local.js --pro`), around 2026-10-14; exact commit not recorded | Public | Website links only to `?sample` (fictional family, nothing saved). Without `?sample` this site is a working **unlicensed Pro** that saves data: not for real customers. Rebuild it from `dev` once L-01 is merged. |
| Private Cloud beta (store) | https://lilycao.gumroad.com/l/roofmere | Gumroad · product `roofmere` | Legacy Basic / Family / Complete ZIPs | Public | Current paid beta. |
| Cloud setup video | https://youtu.be/JVVJcDkPMus | YouTube | — | Public / unlisted (check) | Linked from the Private Cloud card. |
| Setup guide (wizard) | to confirm | repo `roofmere-setup-preview` | `main` | to confirm | Buyers use it to install Private Cloud; record its URL here. |

## Rules
- **Local sites keep data per address.** Changing the Netlify project name changes the address, and the data people saved under the old one does not follow. Pick the final name first.
- **Test builds:** new Netlify Drop sites stay Private until checked; give each a row here, with the commit it was built from.
- **Pro test builds:** the website links to them only with `?sample`. They are replaced by licensed Pro once licensing exists.
