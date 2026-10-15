# Roofmere website and launch follow-up

Date: 2026-10-15 UTC
Sources inspected: website main bcb43b5; product dev 8511cc7; docs/LOCAL_MODE.md. This is an implementation backlog, not a public feature promise.

## Implemented in this website update
- Keep the centered text-only hero and existing purple brand; do not add a mockup.
- Link hero and header to the existing Local sample mode (?sample), with fictional-data and no-save disclosure.
- Keep edition comparison and visible 10-account / 1-property Free limits.
- Distinguish sample availability from the pending Free public release, Pro checkout/license and trial.
- Mark post-trial behavior as planned rather than an implemented purchase flow.

## Existing product capabilities: do not duplicate
Product dev already has IndexedDB writes, save-failure feedback/rollback, manual JSON backup/restore, a last-backup banner (warning when none or 30+ days), Free limits, Pro feature gates and Local Vault refusal. These source checks are not a substitute for real-device acceptance testing.

## Next small release: before public Local launch
- Publish and verify a dedicated Free deployment; then change the hero to Start Free, with sample as an optional secondary path. Never label the current Pro test build as the released Free product.
- Product docs say --pro is a founder test build that must not be publicly published, while the website already linked a public Pro preview. This update points visitors to sample mode only; it does not secure or change that deployment. Resolve the intended preview policy before promotion.
- Verify iPhone Safari and desktop: first run, 11th account/second property refusal, imported duplicates, quota/write failures, backup/restore, clearing site data, update persistence and sample isolation. Use synthetic fixtures only.
- Explain no automatic sync, private-window limitations and backup responsibilities at first run and before checkout. Avoid unreliable private-mode detection and unsupported blanket Safari retention claims.
- Validate primary and secondary CTA paths, phone layout, keyboard access, contrast and image readability. Track visits and funnel only after a minimal privacy/data-collection design; do not silently introduce analytics.

## Separate design decisions / larger upgrades
### Purchase, license and trial
- $39 beta / $49 web Pro and $49 iPhone buyout are hypotheses, not validated demand or launched offers.
- Choose storefront and verify current vendor APIs before implementation; payment does not itself activate Roofmere.
- Design purchase verification, activation/recovery, allowed devices, offline entitlement behavior, refund/revocation, trial start/end and over-limit data preservation.
- Define included updates and support. No blanket lifetime-all-features or unlimited-support promise.
- No need to require a license just to use Free unless a concrete requirement is approved.

### Offline/installable web experience
- Manifest, asset caching, update/recovery strategy, offline imports/OCR dependency packaging and real iPhone tests. IndexedDB alone does not prove full offline operation.

### iPhone app feasibility
- Explore Capacitor with shared HTML/CSS/JS business logic before rewriting in Swift.
- Small proof: launch, synthetic record persistence, backup/export/import, update persistence.
- Native storage adapter, file/share integration, keyboard/safe areas, purchase restore, app lifecycle and recovery all need testing.
- Decide macOS/Xcode or cloud-Mac build environment, signing ownership and CI/TestFlight distribution. A temporary CI runner is not an interactive remote simulator desktop.
- No App Store release, conversion forecast or $49 purchase promise before feasibility and demand checks.

### Sync and family access
- Local web and Local iPhone are separate data stores unless migration/sync is implemented. Native packaging does not add sync or a Local Vault.
- Decide demand and architecture for optional sync, conflicts, backup and family permissions separately. Preserve existing Private Cloud as an advanced self-hosted option.

## Marketing principles adopted from the Gemini discussion
- Keep the first action simple; distinguish preview from release.
- Explain privacy with specific data flows, not zero-risk/security absolutes.
- Make paid value about time saved (screenshot/table imports, batch update, history/planning), not concealed limits.
- Keep Cloud setup outside the main Local onboarding path.
- Test demand through completion, repeat use and actual paid conversion; do not infer sales from downloads or App Store presence.
