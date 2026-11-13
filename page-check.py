#!/usr/bin/env python3
"""Deterministic gates for the generated pages. No model, no network, no cost.

Run by build-pages.py after every build, so a page that breaks a rule cannot be
committed by a person or by the nightly loop. Exits non-zero on any failure.

WHAT IT CHECKS, AND WHY EACH ONE IS HERE
  idiom / promised feeling  COPY-RULES.md rules 2 and 3. Rule 3 is the one a
                            well-meaning proofreader breaks first.
  placeholder               __PROVIDER_ID__ shipped live in a PR once. A live
                            href must never contain one.
  external script           the home page promises "no tracking". A beacon
                            under that sentence makes the page untrue.
  one primary CTA           product thesis: one primary action per screen.
  answer card               the complete answer must be above everything else.
  paragraph length          three sentences. The audience is anxious, ADHD and
                            dyslexic readers; a four-sentence block is where
                            they lose the line.
  JSON-LD                   must parse, and there must be exactly two blocks —
                            the Article and the FAQ. Three means the homepage's
                            schema leaked in again (it did once).

TWO DELIBERATE EXEMPTIONS, because a rule that fires on correct work gets
switched off:
  - the answer card (.tldr). It is the whole answer in one place by design, and
    it is the one paragraph allowed to run long.
  - a paragraph that is a quoted template. An email someone will copy is not
    prose and does not get read like prose.
"""
import glob, html, json, re, sys

IDIOMS = (r"work(?:ing)? the room|break the ice|mailshot|practise|crush it|nail it|"
          r"touch base|circle back|low-hanging|hit it off|put yourself out there|game plan")
# COPY-RULES rule 3: never promise a feeling or an outcome. This used to be a
# list of two literal phrases, so "You will feel calm" walked straight through
# it (Gloria, 2026-09-16). It is now the SHAPE of the promise — any
# second-person "you will feel/be/look/come across <adjective>", and any
# "it will be <adjective>" — which catches the sentence nobody has written yet.
FEELINGS = (
    r"you'?(?:ve| have) got this|you'?(?:ll| will) (?:do|be) (?:great|fine|grand)|"
    r"you (?:are|'re) ready|don'?t worry|no need to (?:worry|be nervous)|"
    # you will / you'll + feel|be|look|seem|come across + an adjective
    r"you'?(?:ll|d| will| are going to| going to)? ?(?:feel|be|look|seem|sound|appear|come across|end up)"
    # Intensifiers are optional and repeatable — "you will feel very confident"
    # and "you will appear calm" both got through the first version.
    r"\s+(?:(?:so|very|much|totally|completely|perfectly|really|absolutely|"
    r"a lot|far|way|a bit|pretty|quite)\s+)*"
    r"(?:calm|calmer|confident|relaxed|fine|great|ready|better|amazing|okay|ok|"
    r"at ease|nervous-free|unstoppable)\b|"
    r"it (?:will|'ll) (?:be|feel) (?:fine|easy|great|okay|ok|better)\b"
)

# Not a medical product — the line is on every page, and the text must not
# contradict it. Haveo does not treat, cure, reduce or manage a condition, and
# it is not therapy. This gate was added after "treats your symptoms" survived
# a full build (Gloria, 2026-09-16). It fires on Haveo/the app/this making a
# clinical promise, not on the page describing therapy as a thing that exists.
MEDICAL = (
    # "your" is OPTIONAL throughout. It used to be mandatory on manages/reduces,
    # so "Haveo reduces anxiety" walked through (CTO review, 2026-09-16).
    r"\b(?:treats?|treating|cures?|curing|heals?|healing|fixes?|fixing|"
    r"diagnoses|diagnosing|manages?|managing|reduces?|reducing)\s+"
    r"(?:your\s+|the\s+)?(?:symptoms?|anxiety|social anxiety|adhd|autism|dyslexia|"
    r"depression|condition|disorder)\b|"
    r"\b(?:clinically proven|medically proven|therapeutic(?:ally)?|"
    r"a form of therapy|replaces? therapy|instead of therapy|"
    r"instead of a therapist)\b"
)

# COPY-RULES rule 2: US spelling. The gate knew one word — "practise" — and 24
# pages shipped with CV, colour, behaviour, realise and organised on them.
# A word list is the right shape here: each entry is a spelling that is simply
# wrong for this site, with the spelling that replaces it.
BRITISH = {
    "colour": "color", "colours": "colors", "behaviour": "behavior",
    "behaviours": "behaviors", "behavioural": "behavioral", "realise": "realize",
    "realised": "realized", "realising": "realizing", "organise": "organize",
    "organised": "organized", "organising": "organizing", "recognise": "recognize",
    "recognised": "recognized", "recognising": "recognizing", "apologise": "apologize",
    "apologised": "apologized", "apologising": "apologizing", "memorise": "memorize",
    "memorised": "memorized", "prioritise": "prioritize", "prioritised": "prioritized",
    "summarise": "summarize", "summarised": "summarized", "specialise": "specialize",
    "specialised": "specialized", "minimise": "minimize", "minimised": "minimized",
    "analyse": "analyze", "analysed": "analyzed", "analysing": "analyzing",
    "practise": "practice", "practised": "practiced", "practising": "practicing",
    "licence": "license", "defence": "defense", "offence": "offense",
    "travelled": "traveled", "travelling": "traveling", "cancelled": "canceled",
    "cancelling": "canceling", "labelled": "labeled", "labelling": "labeling",
    "whilst": "while", "amongst": "among", "learnt": "learned", "spelt": "spelled",
    "grey": "gray", "centre": "center", "metre": "meter", "favourite": "favorite",
    "neighbour": "neighbor", "neighbours": "neighbors", "humour": "humor",
    "rumour": "rumor", "catalogue": "catalog", "programme": "program",
    "aeroplane": "airplane", "flatmate": "roommate",
    "timetable": "schedule", "cheque": "check", "enrol": "enroll",
    "fulfil": "fulfill", "instalment": "installment", "storey": "story",
}
BRITISH_RE = re.compile(r"\b(" + "|".join(sorted(BRITISH, key=len, reverse=True)) + r")\b", re.I)

# Two words that are only British in one sense, so the word list would fail
# correct US English: "lift your chin" and "give someone a lift" are fine, and
# "CV" is legitimate as computer vision. Matched as phrases instead, which is
# the sense that is actually wrong for this site. Found by the CTO review,
# 2026-09-16 — the first version failed both.
BRITISH_PHRASES = [
    # "the lift" only. "a lift" is a ride ("ask a friend for a lift") and
    # "lift your chin" is a verb — both correct US English, both flagged by the
    # first version of this rule.
    (re.compile(r"\bthe\s+lift\b", re.I), "lift (the elevator) -> elevator"),
    (re.compile(r"\bCV\b"), "CV -> resume"),          # case-sensitive: computer vision is "cv"
    # "flat" is deliberately NOT here. The determiner rule fired on "A flat
    # conversation is usually not about you" the first time it ran, and a gate
    # that flags correct prose is a gate someone switches off. The British
    # sense (a home) does not appear on this site; if it ever does, write the
    # phrase, not the word.
]
PLACEHOLDER = r"__[A-Z_]+__"


def norm(t):
    """Fold typographic punctuation so a rule written with ' still matches '."""
    return t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')


def sentences(t):
    return len(re.findall(r'[.!?]["”]?(?:\s|$)', t))


def main():
    files = sorted(glob.glob("*/index.html"))
    if not files:
        print("page-check: no pages found — did build-pages.py run?", file=sys.stderr)
        return 1

    fails = []
    # The home title is the search-result promise for the product's own name.
    # It drifted into audience-only wording several times, leaving the title
    # unable to say what Haveo is, where it runs, or what it helps with. Keep
    # the stable, source-backed facts in the raw HTML: Haveo is an iPhone app
    # for networking event prep. If the platform or product changes, update
    # this assertion deliberately alongside the public copy.
    try:
        home = open("index.html", encoding="utf-8").read()
    except FileNotFoundError:
        print("page-check: missing home index.html", file=sys.stderr)
        return 1
    title_match = re.search(r"<title>(.*?)</title>", home, re.S | re.I)
    home_title = html.unescape(title_match.group(1)).strip() if title_match else ""
    required_home_title_terms = ("haveo", "iphone", "networking", "event prep")
    missing_home_title_terms = [term for term in required_home_title_terms
                                if term not in home_title.lower()]
    if missing_home_title_terms:
        fails.append(("index.html", "home title missing product fact",
                      ", ".join(missing_home_title_terms)))

    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', home, re.S | re.I)
    home_desc = html.unescape(desc_match.group(1)).strip() if desc_match else ""
    required_home_desc_terms = ("haveo", "networking", "cheat sheet", "92", "ios")
    missing_home_desc_terms = [term for term in required_home_desc_terms
                               if term not in home_desc.lower()]
    if missing_home_desc_terms:
        fails.append(("index.html", "home meta description missing product fact",
                      ", ".join(missing_home_desc_terms)))

    og_title_m = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', home, re.S | re.I)
    og_title = html.unescape(og_title_m.group(1)).strip() if og_title_m else ""
    missing_og_title_terms = [term for term in required_home_title_terms
                              if term not in og_title.lower()]
    if missing_og_title_terms:
        fails.append(("index.html", "home og:title missing product fact",
                      ", ".join(missing_og_title_terms)))

    og_desc_m = re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']', home, re.S | re.I)
    og_desc = html.unescape(og_desc_m.group(1)).strip() if og_desc_m else ""
    missing_og_desc_terms = [term for term in required_home_desc_terms
                             if term not in og_desc.lower()]
    if missing_og_desc_terms:
        fails.append(("index.html", "home og:description missing product fact",
                      ", ".join(missing_og_desc_terms)))

    tw_title_m = re.search(r'<meta\s+name=["\']twitter:title["\']\s+content=["\'](.*?)["\']', home, re.S | re.I)
    tw_title = html.unescape(tw_title_m.group(1)).strip() if tw_title_m else ""
    missing_tw_title_terms = [term for term in required_home_title_terms
                              if term not in tw_title.lower()]
    if missing_tw_title_terms:
        fails.append(("index.html", "home twitter:title missing product fact",
                      ", ".join(missing_tw_title_terms)))

    tw_desc_m = re.search(r'<meta\s+name=["\']twitter:description["\']\s+content=["\'](.*?)["\']', home, re.S | re.I)
    tw_desc = html.unescape(tw_desc_m.group(1)).strip() if tw_desc_m else ""
    missing_tw_desc_terms = [term for term in required_home_desc_terms
                             if term not in tw_desc.lower()]
    if missing_tw_desc_terms:
        fails.append(("index.html", "home twitter:description missing product fact",
                      ", ".join(missing_tw_desc_terms)))

    ws_desc_m = re.search(r'"@type":\s*"WebSite",.*?"description":\s*"(.*?)"', home, re.S)
    ws_desc = html.unescape(ws_desc_m.group(1)).strip() if ws_desc_m else ""
    missing_ws_desc_terms = [term for term in required_home_desc_terms
                             if term not in ws_desc.lower()]
    if missing_ws_desc_terms:
        fails.append(("index.html", "home WebSite structured data description missing product fact",
                      ", ".join(missing_ws_desc_terms)))

    app_desc_m = re.search(r'"@type":\s*"MobileApplication",.*?"description":\s*"(.*?)"', home, re.S)
    app_desc = html.unescape(app_desc_m.group(1)).strip() if app_desc_m else ""
    missing_app_desc_terms = [term for term in required_home_desc_terms
                              if term not in app_desc.lower()]
    if missing_app_desc_terms:
        fails.append(("index.html", "home MobileApplication structured data description missing product fact",
                      ", ".join(missing_app_desc_terms)))

    org_desc_m = re.search(r'"@type":\s*"Organization",.*?"description":\s*"(.*?)"', home, re.S)
    org_desc = html.unescape(org_desc_m.group(1)).strip() if org_desc_m else ""
    missing_org_desc_terms = [term for term in required_home_desc_terms
                              if term not in org_desc.lower()]
    if missing_org_desc_terms:
        fails.append(("index.html", "home Organization structured data description missing product fact",
                      ", ".join(missing_org_desc_terms)))

    # Verify that homepage WebSite structured data includes SiteNavigationElement hasPart items matching visible guide hubs.
    ws_haspart_m = re.search(r'"@type":\s*"WebSite",.*?"hasPart":\s*(\[.*?\])\s*,\s*"publisher"', home, re.S)
    if not ws_haspart_m:
        fails.append(("index.html", "home WebSite structured data missing hasPart SiteNavigationElement links", ""))
    else:
        try:
            ws_parts = json.loads(ws_haspart_m.group(1))
            nav_urls = [p.get("url", "").strip() for p in ws_parts if isinstance(p, dict) and p.get("@type") == "SiteNavigationElement"]
            if len(nav_urls) < 11:
                fails.append(("index.html", "home WebSite hasPart missing navigation elements", f"expected at least 11, found {len(nav_urls)}"))
        except json.JSONDecodeError as exc:
            fails.append(("index.html", "home WebSite hasPart JSON-LD invalid", str(exc)))

    # Verify that homepage FAQPage structured data stays synchronized with the visible FAQ.
    faq_ld_m = re.search(r'"@type":\s*"FAQPage",\s*"mainEntity":\s*(\[.*?\])\s*\}', home, re.S)
    if not faq_ld_m:
        fails.append(("index.html", "home FAQPage structured data missing or malformed", ""))
    else:
        try:
            faq_entities = json.loads(faq_ld_m.group(1))
            faq_ld_questions = [q.get("name", "").strip() for q in faq_entities if isinstance(q, dict)]
        except json.JSONDecodeError as exc:
            fails.append(("index.html", "home FAQPage JSON-LD invalid", str(exc)))
            faq_ld_questions = []

        visible_faq_questions = [q.strip() for q in re.findall(r"<summary>(.*?)</summary>", home)]
        if not visible_faq_questions:
            fails.append(("index.html", "home visible FAQ summaries missing", ""))
        else:
            missing_in_ld = [q for q in visible_faq_questions if q not in faq_ld_questions]
            if missing_in_ld:
                fails.append(("index.html", "home FAQPage schema missing visible questions",
                              ", ".join(missing_in_ld)))

    # Verify that homepage has apple-itunes-app meta tag for iOS Smart App Banner to convert mobile branded searchers.
    itunes_m = re.search(r'<meta\s+name=["\']apple-itunes-app["\']\s+content=["\']app-id=6774740212["\']\s*/?>', home)
    if not itunes_m:
        fails.append(("index.html", "home missing apple-itunes-app meta tag for iOS App Banner", "expected app-id=6774740212"))

    # Metadata-only CTR edits kept recurring while the first rendered screen
    # still made a visitor infer the product identity. Keep the same grounded
    # facts in the initial header: this is Haveo, it is a free iPhone app, and
    # it prepares someone for a networking event. This is deliberately scoped
    # to visible body copy, not JSON-LD or <head> metadata.
    header_m = re.search(r"<header\b[^>]*>(.*?)</header>", home, re.S | re.I)
    hero_text = html.unescape(re.sub(r"<[^>]+>", " ", header_m.group(1))) if header_m else ""
    required_hero_terms = ("haveo", "free iphone app", "networking event")
    missing_hero_terms = [term for term in required_hero_terms
                          if term not in hero_text.lower()]
    if missing_hero_terms:
        fails.append(("index.html", "first screen missing grounded product identity",
                      ", ".join(missing_hero_terms)))

    # Positive control. If the searches below come back clean because the text
    # never loaded, this is the line that says so. A clean result is only
    # evidence if the check could have come back dirty.
    control = sum(1 for f in files if "haveo" in open(f, encoding="utf-8").read().lower())
    if control != len(files):
        print(f"page-check: positive control failed — 'haveo' found in only "
              f"{control}/{len(files)} pages. The reader is broken, not the pages.",
              file=sys.stderr)
        return 1

    for f in files:
        s = open(f, encoding="utf-8").read()
        m = re.search(r'<main class="doc">(.*?)</main>', s, re.S)
        if not m:
            fails.append((f, "no <main class=doc>", ""))
            continue
        body = m.group(1)
        text = html.unescape(re.sub(r"<[^>]+>", " ", body))

        for pat, name in ((IDIOMS, "idiom"), (FEELINGS, "promised feeling"),
                          (MEDICAL, "medical claim")):
            for hit in re.findall(pat, norm(text), re.I):
                fails.append((f, name, hit if isinstance(hit, str) and hit else pat))
        # Placeholders are hunted over the WHOLE file, not the stripped text.
        # The one that shipped was __PROVIDER_ID__ inside an href, which tag
        # stripping cannot see. A negative control caught this rule being dead.
        for hit in re.findall(PLACEHOLDER, s):
            fails.append((f, "unreplaced placeholder", hit))

        # Exactly ONE external script is allowed: the GA4 tag on the approved
        # stream. The rule used to be "none", because the page promised no
        # tracking at all; on 2026-09-15 that promise was made precise ("no
        # tracking inside the app") and the site began saying plainly that it
        # counts page views and App Store clicks. The gate narrows rather than
        # disappears — a SECOND tag, or a different property, still fails,
        # because the thing being protected is the sentence on the page.
        for src in re.findall(r'<script[^>]+src="([^"]+)"', s):
            if not src.startswith("https://www.googletagmanager.com/gtag/js?id=G-FVW5T8KNGX"):
                fails.append((f, "unapproved external script", src[:70]))
        if "cloudflareinsights" in s:
            fails.append((f, "external script", "cloudflare beacon"))
        if "G-FVW5T8KNGX" in s and "app_store_click" not in s:
            fails.append((f, "GA4 tag without the key event", "app_store_click missing"))
        if 'class="tldr"' not in s:
            fails.append((f, "no answer card", ""))
        n_cta = s.count('class="btn btn-appstore"')
        if n_cta != 1:
            fails.append((f, "primary CTA count", f"{n_cta}, want exactly 1"))

        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        if len(blocks) != 2:
            fails.append((f, "JSON-LD block count", f"{len(blocks)}, want 2"))
        for b in blocks:
            try:
                json.loads(b)
            except json.JSONDecodeError as e:
                fails.append((f, "JSON-LD does not parse", str(e)[:60]))

        tldr = re.search(r'<div class="tldr">.*?</div>', body, re.S)
        tldr_text = tldr.group(0) if tldr else ""
        for p in re.findall(r"<p>(.*?)</p>", body, re.S):
            if p in tldr_text:
                continue                      # the answer card may run long
            t = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
            if t.startswith(('"', "“")):
                continue                      # a quoted template is not prose
            n = sentences(t)
            if n > 3:
                fails.append((f, f"paragraph is {n} sentences", t[:70]))

    # --- US spelling -------------------------------------------------------
    # Over the visible text of every page AND the home page, because the home
    # page is a page the same reader reads. COPY-RULES rule 2.
    import os as _os
    for f in files + (["index.html"] if _os.path.exists("index.html") else []):
        s = open(f, encoding="utf-8").read()
        m = re.search(r'<main class="doc">(.*?)</main>', s, re.S)
        # The home page has no <main class="doc">, so it is read whole — and
        # whole means its comments, CSS and JS too, where "border-colour" in a
        # note to the next editor is not a copy breach. Strip those first: the
        # rule is about what a reader reads.
        raw = m.group(1) if m else s
        raw = re.sub(r"<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>",
                     " ", raw, flags=re.S)
        text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
        for hit in BRITISH_RE.findall(text):
            fails.append((f, "British spelling", f"{hit} -> {BRITISH[hit.lower()]}"))
        for rx, msg in BRITISH_PHRASES:
            if rx.search(text):
                fails.append((f, "British spelling", msg))

    # --- GEO structure -----------------------------------------------------
    # Every page must connect its answer to the app, or a model that quotes the
    # answer has no machine-readable reason to name Haveo. That connection is
    # the entire point of writing the answers.
    for f in files:
        s = open(f, encoding="utf-8").read()
        types = []
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                d = json.loads(b)
            except json.JSONDecodeError:
                continue
            types += ([n.get("@type") for n in d["@graph"]] if "@graph" in d
                      else [d.get("@type")])
        for needed in ("Article", "MobileApplication", "Organization", "WebSite", "FAQPage"):
            if needed not in types:
                fails.append((f, "schema entity missing", needed))
        if "apps.apple.com" not in s:
            fails.append((f, "schema has no App Store URL", "MobileApplication.sameAs"))

    # llms.txt and sitemap.xml are NOT html. An &amp; in either is a literal
    # broken link — it shipped once, in the App Store URL in llms.txt.
    for plain in ("llms.txt", "sitemap.xml"):
        try:
            t = open(plain, encoding="utf-8").read()
        except FileNotFoundError:
            fails.append((plain, "missing", "build-pages.py writes it"))
            continue
        if "&amp;" in t:
            fails.append((plain, "html entity in a non-html file", "&amp;"))

    # --- attribution ---------------------------------------------------------
    # Apple caps ct at 39 characters. With the section number on the END of the
    # token it was the number that got truncated, so every section of a
    # long-slug page reported as one placement — 77 collisions, and no way to
    # tell which part of a page produced a download. Uniqueness IS the feature.
    import collections
    seen = []
    for f in files + (["index.html"] if __import__("os").path.exists("index.html") else []):
        t = open(f, encoding="utf-8").read()
        for ct in re.findall(r"ct=([a-z0-9-]+)&amp;mt=8", t):
            seen.append((ct, f))
            if len(ct) > 39:
                fails.append((f, "campaign token over Apple's 39-char cap", ct))
    counts = collections.Counter(c for c, _ in seen)
    for ct, n in counts.items():
        if n > 1:
            where = sorted({f for c, f in seen if c == ct})[:3]
            fails.append(("(site)", f"campaign token used {n} times", f"{ct} in {where}"))

    # --- search-result truncation ------------------------------------------
    # Google cuts titles around 65 characters and meta descriptions around 165.
    # A truncated title loses the words at the end, which are usually the
    # specific ones the page is meant to rank for. Include index.html so the
    # brand homepage title and description are strictly guarded against truncation.
    for f in files + (["index.html"] if _os.path.exists("index.html") else []):
        t = open(f, encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        if m and len(m.group(1).strip()) > 65:
            fails.append((f, f"title {len(m.group(1).strip())} chars", "Google truncates over 65"))
        d = re.search(r'<meta name="description" content="(.*?)"', t, re.S)
        if d and len(d.group(1)) > 165:
            fails.append((f, f"meta description {len(d.group(1))} chars", "Google truncates over 165"))

    if fails:
        print(f"page-check: {len(fails)} failure(s) across {len(files)} pages\n",
              file=sys.stderr)
        for f, what, detail in fails:
            print(f"  {f}\n    {what}: {detail}", file=sys.stderr)
        return 1

    print(f"page-check: {len(files)} pages, all gates clean "
          f"(positive control {control}/{len(files)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
