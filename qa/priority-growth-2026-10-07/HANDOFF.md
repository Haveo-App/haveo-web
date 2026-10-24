# Haveo homepage download focus — local candidate

Work ID: `priority-growth:2026-10-07:haveo` · round `2026-10-07` · action `local_gbp_conversion`.
Immutable brief: `341ef6a2518369dea78d964b0f436bf9ce04b7c082227b2c26c64d3a8d801e78`.

The homepage now identifies the app/platform directly and gives its existing App Store action priority. Social and feedback links stay available below the privacy reassurance. Phone decorations no longer overlap the reading area. The new homepage update date feeds the generator-owned sitemap date. No guide, metadata, analytics, destination or internal link was removed or rewritten.

This is an owned-site conversion improvement under the supplied taxonomy, with no unsupported Google Business Profile work. The input search snapshot is a rationale for inspecting the conversion path, not proof of a conversion problem or measured uplift. See `build-spec.md` and `binding.json` for scope, measurement and source/production bindings.

## Verification

- `checks.txt`: 92 guide checks; 93 page contracts; byte-identical generator round trip; whitespace check; experience contract validation.
- `verification.json`: 8 browser/viewport cases (WebKit and Chromium; 375×667, 390×844, 390×600, 1280×800). Primary action fits every first screen; secondary actions are at least 44px. Trusted touch/keyboard, feedback destination, no overflow, no-JS and reduced motion checked.
- Chromium opens the unchanged App Store URL on touch and Enter. Synthetic `app_store_click`, `placement=site-hero`, `page_path=/` is observed with all GA delivery blocked. No production collector or install result is asserted.
- macOS WebKit opens an `example.com` diagnostic popup but does not create a browser tab for `apps.apple.com`. WebKit checks therefore suppress the native handoff and assert trusted activation/href/event. Native iPhone/App Store handoff remains unverified. Safari link focus uses Option+Tab under the host's default keyboard preference.
- The first attempt used Python Playwright with a mismatched WebKit revision; final checks use Playwright 1.63.0 with its matching installed WebKit/Chromium. QA-only dependencies were downloaded within ignored worktree scratch storage, then removed. No app dependency changed.
- `live-source-checks.json`: fresh GETs returned HTTP 200 for Haveo and the Apple listing; the listing confirms name, free pricing, device support and the described prep features.
- `human-consumption-before.json` and `human-consumption.json`: both AMBER, zero RED. At 390×844, download moved from y=543 to y=496; product-card position moved from 1886px to 1754px. Existing warnings persist: 84-word paragraph, 3 contrast findings, 23 small text blocks, 11 images flagged for empty alt, no scroll analytics (automation is filtered). These are not silently claimed fixed.
- Builder inspected the before/after short-phone, regular phone, short 390×600, desktop, Chromium and reduced-motion frames. New candidate has not received independent craft approval.

## Applicable editorial checks

| Rule | Result and evidence |
|---|---|
| E01–E03 | PASS in changed hero: original character faces remain complete; no controls cover them. Captures `after-webkit-*` and `after-chromium-*`; original `illustrations/ai-assistant.svg`. No poster text involved. |
| E05 / E18 | PASS for primary action across tested viewports, measured in `verification.json`; no fixed dock. Secondary links may require scroll on a 600px-high screen. |
| E08–E10 | PASS for changed hero: original rounded button, clear destination, no decorative emoji, reduced-motion press. Native device handoff remains PENDING. |
| E13–E14 | PASS for scoped hierarchy: short description and one primary button; native FAQ remains available. Whole-page readability remains AMBER. |
| E15 | PASS: root begins at hero and feedback link reaches the feedback section. |
| E16 | PASS for added copy: source listing stored in `live-source-checks.json`; no fabricated location, conversion or install claim. |
| E17 | Builder inspected actual frames; independent Antigravity/Claude reviews PENDING. |

E04/E06/E07 (carousel), E11/E12 (game/form) do not apply. No new narrative animation, scene, keyboard input or card system was introduced; a motion film and virtual-keyboard layout audit are not relevant to this local hierarchy repair.

## Reproduce and deliver

From this checkout: run `python3 page-check.py`, `python3 scripts/page-contract.py`, and `python3 build-pages.py` (the rebuild must leave tracked files unchanged). For browser checks, serve the checkout locally on port 8769 and run `verify-home.mjs` with `PLAYWRIGHT_MODULE` pointing to Playwright 1.63.0. Collection is blocked inside the probe. No dependencies belong in the publish artifact; `qa/` is already excluded by the Pages workflow.

The prior candidate's rejection recorded a temporary-file permission failure, not a demonstrated UI defect. Run the required acceptance with `TMPDIR` pointing to this worktree's ignored `qa/priority-growth-2026-10-07/.scratch` directory. The exact required command is:

```sh
/Users/gonzalo/code/portfolio-ops-pg-lane/scripts/priority-growth-project-verify.sh --site haveo --repo /Users/gonzalo/.claude/state/priority-growth-release/site-adapter/worktrees/haveo/db1710d79f2c3f996abe --baseline 21cd40942dc64d2a48498a4d8ff4caa4c0e4d661 --require-commit
```

Coordinator / cto-qa-lead: independently review this exact new candidate before release, including the supplied frames and noted native-handoff limit. Adapter owns PR/merge/publish and the existing post-publish IndexNow action. Run `binding.json` production probes after publication. Growth lead: retrieve the handoff baseline and compare equivalent 14-day windows after release; installs and low sample uncertainty remain separate.

Vault handoff: this provider is confined to the supplied worktree. Coordinator should copy this durable note into Haveo's canonical vault and add its hot.md pointer during the release handoff. No vault, credential, primary checkout, scheduler, PR or remote branch was written by this provider.
