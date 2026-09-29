#!/usr/bin/env python3
"""Assert every published page carries what makes it findable and measurable.

$0, no LLM, no network. Pure stdlib over the checked-out HTML.

WHY THIS EXISTS
---------------
This repo is what actually publishes haveo.app (GitHub Pages, from main). Its
only workflow was the Pages deploy, which runs on push and therefore reports
NOTHING on a pull request. The portfolio merge gate fails closed when a PR has
no checks, so every PR here was unmergeable by default — a growth lane could
open work against this repo forever and none of it could ever land.

It asserts the two things that are invisible until they are missing:

  * the page can be found  — <title>, canonical, meta description
  * the page can be counted — the GA4 tag is present and is the RIGHT property

A page with no analytics is not finished; a page with the wrong measurement id
is worse, because it looks measured and reports into someone else's property.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

# The property haveo.app reports into. Pinned deliberately: a typo or a
# copy-paste from another brand's page is silent data loss, and the only way to
# catch it is to compare against a known value.
GA4_ID = "G-FVW5T8KNGX"

# Not every HTML file is a content page. Search-engine verification files are
# fixed tokens the provider serves back to itself — they have no title and no
# analytics BY DESIGN, and requiring either would make this gate permanently
# red for a file nobody reads.
SKIP_NAMES = {"404.html"}
SKIP_PATTERNS = (
    re.compile(r"^google[0-9a-f]{16}\.html$", re.I),   # Search Console
    re.compile(r"^BingSiteAuth\.xml$", re.I),
)

TITLE = re.compile(r"<title[^>]*>\s*(.+?)\s*</title>", re.I | re.S)
CANONICAL = re.compile(r"""<link[^>]+rel=["']canonical["'][^>]*>""", re.I)
DESCRIPTION = re.compile(r"""<meta[^>]+name=["']description["'][^>]*>""", re.I)


def pages() -> list[pathlib.Path]:
    out = []
    for p in sorted(ROOT.rglob("*.html")):
        if ".git" in p.parts or p.name in SKIP_NAMES:
            continue
        if any(pat.match(p.name) for pat in SKIP_PATTERNS):
            continue
        out.append(p)
    return out


def check(path: pathlib.Path) -> list[str]:
    html = path.read_text(encoding="utf-8", errors="replace")
    fails: list[str] = []

    title = TITLE.search(html)
    if not title or not title.group(1).strip():
        fails.append("no <title>")
    elif len(title.group(1).strip()) < 10:
        fails.append(f"<title> too short to be a real title: {title.group(1)!r}")

    if not CANONICAL.search(html):
        fails.append("no rel=canonical")
    if not DESCRIPTION.search(html):
        fails.append("no meta description")

    # Measurement. Both halves matter: the loader has to be there AND the id has
    # to be ours. Checking only for the word "gtag" would pass a page that ships
    # another brand's property.
    if "googletagmanager.com/gtag/js" not in html:
        fails.append("no GA4 loader")
    if GA4_ID not in html:
        found = set(re.findall(r"G-[A-Z0-9]{6,}", html))
        fails.append(
            f"GA4 id {GA4_ID} missing"
            + (f" (found {sorted(found)} instead)" if found else " (no id at all)")
        )
    return fails


def main() -> int:
    found = pages()
    if not found:
        # A gate that silently checks nothing is worse than no gate: it reports
        # green forever. If the layout changes so no page is discovered, fail.
        print("FAIL: no HTML pages found — the gate would be asserting nothing")
        return 1

    bad = 0
    for path in found:
        fails = check(path)
        if fails:
            bad += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for f in fails:
                print(f"       - {f}")

    print(f"\n{len(found) - bad}/{len(found)} pages carry title, canonical, description and GA4 {GA4_ID}")
    if bad:
        print(f"FAILED: {bad} page(s) below contract")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
