# Haveo homepage download focus

Work: `priority-growth:2026-10-07:haveo:s1`; round `2026-10-07`.
Action: `local_gbp_conversion`, applied to the owned-site App Store handoff for this mobile application. No GBP record, local address, or local-business schema is asserted or changed.

The visitor has searched for Haveo and needs to understand the app and download it. The sealed brief selects the homepage. Its Search Console rows describe search impressions and clicks, not installs or a measured site conversion rate. The layout hypothesis is that one prominent download button, followed by compact social/feedback links, is clearer than three equally large buttons. Keep the existing Haveo blue, cream, Quicksand and character art. Keep all destinations, placement attribution and guide links. State device support before the action. Native anchors work without JavaScript; no new runtime or collector.

The graph maps content.py -> build-pages.py -> guide HTML, with the generator importing the homepage first CSS block and analytics. The repair therefore adds a separate homepage-only style block and leaves the shared block unchanged. RailCta and RailFaq manifests/refusals plus REVIEW.md were read. Existing static native links are the appropriate reuse for this small HTML site; introducing React would add unnecessary runtime. New styles retain the brand button radius, visible keyboard focus, 44px secondary hit areas, and reduced-motion behavior.

Success for this candidate: download and its device context are visible on short and normal phone screens; actual touch/keyboard navigation preserves pt and ct; feedback still opens its section; no horizontal overflow, no header axe violations, and unchanged generated guides after rebuilding. Updated date is visible and feeds the generated homepage sitemap date. The existing publish workflow submits changed HTML through IndexNow after release.

Business readout belongs to cto-growth-lead: compare human homepage visits -> app_store_click (placement site-hero), then App Store campaign installs, for comparable seven-day windows after deployment. Baseline conversion and install rate are unmeasured in this builder call. Low volume is inconclusive. Keep only if the observed rate does not degrade; do not infer impact from rendered geometry.

Coordinator: independent Antigravity craft review and Claude fidelity verification before adapter release; cto-qa-lead verifies the committed candidate and production App Store handoff. This bounded provider cannot invoke sibling reviewers, publish, or write the canonical vault. The coordinator should copy the handoff into haveo hot.md and a durable page in this release run, before marking delivery complete.
