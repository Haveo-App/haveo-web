# Haveo homepage search snippet candidate

Work ID: `priority-growth:2026-10-11:haveo`

Round: `2026-10-11`; action: `owned_site_ctr`

Baseline: `73df06d3bdaea300714733d67012798bcbbf78cb`

## Decision and scope

A person searching for Haveo needs to recognize the app and know where to get
it. The existing homepage title describes networking preparation for introverts
but omits the platform. Add iPhone to that title and an explicit free App Store
invitation to the description, retaining the intro, out-loud practice and pocket
Cheat Sheet. The hypothesis is clearer app recognition and more qualified search
clicks, with App Store visits as the next action. No uplift has been measured.

The sealed brief contains 64 site impressions and zero clicks for September 29
through October 5, with three branded `haveo` query rows pointing to `/`. Those
are historical brief observations, not a fresh GSC query or proof of present-day
CTR. Low volume is inconclusive. This candidate targets that exact page and
query; it does not expand into unrelated guide content.

Only the HTML title and search description change. Existing social previews,
visible copy, controls, styles, structured data and analytics stay identical.
Canonical taste and the gonzalo-web workflow were read; RailFaq and the current
shared review rules were inspected. No component adoption or visual redesign is
needed for this metadata change. Phone, desktop, motion and conversion-flow
retests are excluded because their markup and behavior are unchanged; no visual
approval is claimed.

## Source and dependency evidence

- The immutable brief, graph and shared packet hashes matched the dispatch.
  The adjacent JSON preserves the brief, hashes and source readback.
- Graphify connects `content.py` to `build-pages.py` and its render function;
  `page-check.py` and `scripts/page-contract.py` provide the deterministic checks.
  Source inspection confirms homepage metadata lives in `index.html`. The builder
  reads its styles/analytics and updates its marked guide links, not its title.
- A live GET of `https://haveo.app/` confirmed the old metadata before editing.
  Apple's lookup for app `6774740212` confirmed the free price, iPhone support,
  intro preparation, voice practice and Cheat Sheet. Exact source URLs and
  timestamps are in the adjacent JSON.
- The prior October 10 dispatch record reports provider failures and no candidate
  diff. This work does not treat those attempts as shipped improvements.

## Candidate copy

Title (54 characters):

> Haveo — Networking event prep for introverts on iPhone

Description (141 characters):

> Get Haveo free on the App Store for iPhone. Build your intro, practice out loud, and take a Cheat Sheet in your pocket for networking events.

## Verification performed

- `python3 build-pages.py`: built 92 guides; only the two intended homepage
  metadata lines differ afterward. No date, sitemap or generated-guide drift.
- `python3 page-check.py`: `92 pages, all gates clean (positive control 92/92)`.
- `python3 scripts/page-contract.py`: `93/93 pages` and `PASS`.
- `git diff -U0 -- index.html | /usr/bin/python3 /Users/gonzalo/code/portfolio-ops-pg-lane/scripts/metadata_specificity_guard.py`:
  exit 0; no loss of concrete detail.
- A temporary localhost HTTP server returned 200 and the candidate HTML.
  HTMLParser found one description, the correct canonical and the candidate
  title. JSON-LD parsed successfully. Normalizing only the two edited tags made
  the entire document byte-identical to baseline. Body SHA-256:
  `1cc9a7a77fb193fde9d90e4b11a8bb2c61096e40cd9bea3fa4c267012380beba`.
- `git diff --check`: clean. The pre-existing untracked `.serena/project.yml`
  was preserved; a local `.serena/.gitignore` excludes that tool directory and
  its local build log. No application source is hidden by it or left uncommitted.

The committed-candidate acceptance command is:

```sh
/Users/gonzalo/code/portfolio-ops-pg-lane/scripts/priority-growth-project-verify.sh \
  --site haveo \
  --repo /Users/gonzalo/.claude/state/priority-growth-release/site-adapter/worktrees/haveo/6f3a8ed147c4655bb1ad \
  --baseline 73df06d3bdaea300714733d67012798bcbbf78cb \
  --require-commit
```

## Coordinator handoff

Before release, cto-qa-lead should obtain the independent Antigravity review and
Claude fidelity verification as sibling dispatches. This bounded builder did
not invoke providers recursively, push, open a PR or deploy. The candidate
commit carries the work ID, round and immutable-brief hash in its message.

After the adapter releases the candidate, verify the homepage's raw HTML against
`production_probe` in the adjacent JSON. The existing Pages workflow already
submits changed HTML URLs to IndexNow; check that run rather than submitting the
unpublished candidate. Google may select different title/snippet text; raw HTML
verification cannot prove its search presentation or CTR effect.

The growth coordinator should use the existing follow-up process at release +7
and +14 days, allowing for GSC reporting delay. Re-read a comparable pre-release
window and compare query `haveo`, page `https://haveo.app/`, clicks, impressions,
CTR and position; separately inspect homepage App Store clicks. Do not equate
clicks with installs or call sparse data a win. Persist this note and a hot.md
pointer in the Haveo project vault through the coordinator: this call's write
authority is confined to the builder worktree. `qa/` is excluded from the site
publication by the existing Pages workflow.
