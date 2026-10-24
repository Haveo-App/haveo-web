# Haveo homepage search snippet candidate

Work ID: `priority-growth:2026-10-15:haveo:s1`

Round: `2026-10-15`; action: `owned_site_ctr`

Baseline: `73df06d3bdaea300714733d67012798bcbbf78cb`

## Decision and scope

A person searching for Haveo needs to recognize the app and know where to get
it. The existing homepage title describes networking preparation for introverts
but omits the platform. Add iPhone to that title in Title Case and an explicit
free App Store mention to the description, retaining the intro, out-loud
practice and pocket Cheat Sheet while fully respecting Haveo's COPY-RULES.md.
The hypothesis is clearer app recognition and higher search CTR, with App Store
visits as the next action. No uplift has been measured.

The sealed brief contains 75 site impressions and zero clicks for October 5
through October 11, with branded `haveo` query rows pointing to `/`. Those
are historical brief observations, not a fresh GSC query or proof of present-day
CTR. Low volume is inconclusive. This candidate targets that exact page and
query; it does not expand into unrelated guide content.

Only the HTML title and search description change in `index.html`. Existing social
previews, visible copy, controls, styles, structured data and analytics stay identical.
Canonical taste and the website experience contract were read; RailFaq and the current
shared review rules were inspected. No component adoption or visual redesign is
needed for this metadata change. Phone, desktop, motion and conversion-flow
retests are excluded because their markup and behavior are unchanged; no visual
approval is claimed.

## Source and dependency evidence

- The immutable brief, graph and shared packet hashes matched the dispatch:
  - Brief SHA-256: `5c751beeb66cc00d2767c2413eb709b49dee04152ea3c7e4d3d9ac58806eaf4d`
  - Graph SHA-256: `86dd8c5dc6202669dbc617e5f3ce470fec8fe7942ef5c63c101b5a55e75db11d`
  - Context packet SHA-256: `756aa9f903d38c05cbdcdcf500f70b878b7333b8ea1112bb79577edee4f65cc8`
- Graphify connects `content.py` to `build-pages.py` and its render function;
  `page-check.py` and `scripts/page-contract.py` provide deterministic checks.
  Source inspection confirms homepage metadata lives in `index.html`.
- A live GET of `https://haveo.app/` confirmed HTTP 200 and the old metadata before editing.
  Apple's lookup for app `6774740212` confirmed the free price, iPhone support,
  intro preparation, voice practice and Cheat Sheet. Exact source URLs and
  timestamps are in the adjacent JSON.

## Candidate copy

Title (54 characters):

> Haveo — Networking Event Prep for Introverts on iPhone

Description (155 characters):

> Haveo prepares you for a networking event on iPhone: build your intro, practice out loud, and keep a Cheat Sheet in your pocket. Free on the App Store.

## Verification performed

- `python3 build-pages.py`: built 92 guides; only the two intended homepage
  metadata lines differ afterward. No date, sitemap or generated-guide drift.
- `python3 page-check.py`: `92 pages, all gates clean (positive control 92/92)`.
- `python3 scripts/page-contract.py`: `93/93 pages` and `PASS`.
- `git diff -U0 -- index.html | python3 /Users/gonzalo/code/portfolio-ops-pg-lane/scripts/metadata_specificity_guard.py`:
  exit 0; no loss of concrete detail.
- Hashing recipe: sha256 of raw GET response body bytes for https://haveo.app/ matches index.html byte-for-byte (`8c9769ff236a912a00328dfe559e9b4bdecf0cef2d82b30c1a594cc57afe8521`).
- `git diff --check`: clean.

The committed-candidate acceptance command is:

```sh
/Users/gonzalo/code/portfolio-ops-pg-lane/scripts/priority-growth-project-verify.sh \
  --site haveo \
  --repo /Users/gonzalo/.claude/state/priority-growth-release/site-adapter/worktrees/haveo/567c843d59147ae8f4c3 \
  --baseline 73df06d3bdaea300714733d67012798bcbbf78cb \
  --require-commit
```

## Coordinator handoff

Before release, cto-qa-lead coordinates independent reviews. This bounded builder
did not invoke providers recursively, push, open a PR or deploy. The candidate
commit carries the work ID, round and immutable-brief hash in its message.
