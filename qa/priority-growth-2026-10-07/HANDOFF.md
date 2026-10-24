# Haveo candidate handoff — 2026-10-07

Work ID: `priority-growth:2026-10-07:haveo:s1`.
Action: `local_gbp_conversion` on the owned homepage-to-App-Store path.
Baseline: `21cd40942dc64d2a48498a4d8ff4caa4c0e4d661`.
Sealed brief, graph and shared packet hashes: `binding.json`.

## Result

One primary download button replaces the three equally prominent hero actions; all original destinations remain. Device context precedes the button. Decorative shapes no longer cross mobile copy. The homepage update date also feeds the generated sitemap. The first shared style block, analytics, App Store campaign links and generated guides are unchanged. No GBP eligibility, local presence, ranking gain or conversion uplift is asserted.

On WebKit at 375x667, the download button moves from y=538.48–596.83 to y=491.50–549.84. The header shrinks from 825px to 695px. At 390x600, the whole button fits with 46.16px beneath it; previously its lower edge was below the viewport. See the before/after PNGs and `verification.json`.

## Verification

- Rebuild: 92 guide copy checks pass; rerunning the build changes no tracked output.
- Page contract: 93/93 candidate site pages pass title, canonical, description and GA4 checks. Executed the unmodified checker on a git-listed HTML snapshot because ignored QA npm dependencies contain tool HTML which its root-wide rglob otherwise mistakes for site pages. These dependencies are excluded from both the commit and publication.
- Chromium and WebKit: eight candidate viewport checks; no horizontal overflow or header axe violations; visible keyboard focus, touch/keyboard activation, feedback anchor, no-JavaScript and reduced-motion states checked.
- Whole-page human-consumption gate: AMBER before and after; zero RED. Existing three contrast findings, 23 small-text blocks, 11 decorative/alt warnings and no scroll analytics signal remain unchanged. Current analytics intentionally skips webdriver and tracks store clicks, not scrolling. No collector delivery or installation is claimed.
- Chromium follows the actual App Store destination. Independent live curl: HTTP 200 with `pt=128642904` and `ct=site-hero` preserved; see `app-store-probe.txt`. Apple's lookup confirms the price and iPhone/iPad support; source recorded in `binding.json`.
- WebKit emits an unprevented click for the original App Store href but does not expose a popup/navigation for that Apple URL in this automated runtime. Native iPhone handoff remains unverified; this is not a claim that a real install succeeded.
- Raw initial HTML contains device context, the attributed action and updated date. No new scripts, calls or dependencies ship.
- The experience sidecar validator passes; its owner status remains unreviewed. Builder inspected the captured short phone, normal phone, desktop and reduced-motion images.

Applicable design checks: E01/E02/E03/E09/E10/E13/E16/E17 PASS for the changed header only (original character art intact, text clear of shapes, real native destinations, no new emoji, short supporting copy, sourced claims, images actually inspected). Keyboard/touch sizes and reduced motion pass. Carousel/game/keyboard-entry rules do not apply to these native links. Independent craft approval is PENDING.

## Coordinator actions in this release run

Before release, dispatch Antigravity for independent rendered review and Claude/cto-qa-lead for fidelity and the committed acceptance check. Confirm the App Store handoff on a real iPhone. The bounded builder must not recursively dispatch reviewers, push, open a PR or deploy.

Copy this handoff and binding into the Haveo vault hot.md and a durable page during this release run; the builder's write scope excludes the vault. Adapter owns PR/release and the post-release checks in `binding.json`. The existing publish workflow sends IndexNow after deployment; no new background loop was created.

cto-growth-lead reads comparable seven-day homepage -> store-click -> campaign-install data at deployment +7 days. The supplied Search Console brief is not a conversion baseline; low volume stays inconclusive. Business impact is unmeasured.
