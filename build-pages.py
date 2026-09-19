#!/usr/bin/env python3
"""Build Haveo's intent pages.

One question per page, answered in the first sentence. Every page reuses
index.html's <style> block verbatim, so the design system stays in one file:
edit index.html's CSS and re-run this script.

    python3 build-pages.py

Writes each page to <slug>/index.html, plus sitemap.xml and llms.txt.
"""
import re, os, sys, json, hashlib, datetime

ROOT   = os.path.dirname(os.path.abspath(__file__))
ORIGIN = "https://haveo.app"
# App Store link WITH install attribution.
#
# pt is the App Store Connect provider id, read from the live account on
# 2026-09-15 (ra/user/detail -> contentProvider.contentProviderId). There is
# exactly one associated account, so there is no ambiguity about which provider
# this is. ct is the placement, and it is what App Store Connect reports on —
# it is how a download from a guide page is told apart from one from TikTok.
#
# Verified at the real boundary, not assumed: the attributed URL returns 200 and
# Apple's redirect to /us/app/haveo-networking-event-prep/ PRESERVES pt and ct.
# A parameter that is dropped in the redirect would attribute nothing.
#
# This shipped once as pt=__PROVIDER_ID__ in PR #102 — a live href containing a
# placeholder. page-check.py now fails the build on exactly that, over the whole
# file rather than the visible text, because the first version of that rule
# could not see inside an href.
PROVIDER_ID = "128642904"
APP_ID      = "6774740212"


def app_link(ct, html=True):
    """App Store URL for one placement. ct is what shows up in App Analytics.

    html=True escapes the ampersands for an href. llms.txt and sitemap.xml are
    NOT html — an &amp; there is a literal broken link, which is exactly what
    shipped the first time this was written.
    """
    amp = "&amp;" if html else "&"
    return (f"https://apps.apple.com/app/haveo/id{APP_ID}"
            f"?pt={PROVIDER_ID}{amp}ct={ct}{amp}mt=8")


APP    = app_link("site-guide")
# The same Apple mark index.html uses on its two App Store buttons.
APPLE_SVG = '<svg viewBox="0 0 384 512" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>'
TODAY  = datetime.date.today().isoformat()

index_html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

# Comments first. index.html has a comment that contains the literal text
# "after <style>", and a plain search for the first "<style>" matched THAT —
# so STYLE became everything from that comment to </style>, which swept the
# homepage's JSON-LD (its FAQPage and MobileApplication) into every guide page,
# inside a <style> element. Wrong structured data on five URLs, and invisible
# in the browser. Strip comments before looking for the tag.
_no_comments = re.sub(r"<!--.*?-->", "", index_html, flags=re.S)
_style = re.search(r"<style>(.*?)</style>", _no_comments, re.S)
if not _style:
    raise SystemExit("index.html: no <style> block found — nothing to inherit.")
STYLE = _style.group(1)
if "application/ld+json" in STYLE or "<script" in STYLE:
    raise SystemExit("index.html: the captured <style> swallowed markup. Fix the regex.")
ANALYTICS = re.search(r"<!-- analytics -->.*?<!-- /analytics -->", index_html, re.S)
ANALYTICS = ANALYTICS.group(0) if ANALYTICS else ""

# The pages live in content.py. See its header for the field list and for why
# the template is shaped the way it is.
from content import PAGES

# --- page dates -----------------------------------------------------------
# datePublished, dateModified and <lastmod> used to be today's date, written
# fresh on every build. The nightly build therefore told Google that all 92
# guides had been rewritten, every single day — a freshness signal that is
# false, and one that crawlers learn to ignore. Gloria caught it on
# 2026-09-16.
#
# So the dates live in page-dates.json, next to this script, and are derived
# from the CONTENT rather than from the clock:
#   published — the first day this slug was ever built. Never changes again.
#   modified  — the day its text last actually changed, detected by hashing
#               the page's own entry in content.py.
# A build that changes nothing changes no date. Pages that already existed
# before this file did inherit 2026-09-15, the day the 50 guides shipped, and
# the wave-2 pages the day they were added — that is the honest answer for
# them, and from here on every date is exact.
DATES_PATH = os.path.join(ROOT, "page-dates.json")
FIRST_PUBLISHED = "2026-09-15"   # the day the site's guides went live

def _fingerprint(page):
    """Everything a reader would see. Ordering-independent, so a reshuffle of
    content.py does not read as a rewrite."""
    return hashlib.sha256(
        json.dumps(page, sort_keys=True, ensure_ascii=False, default=str)
        .encode("utf-8")).hexdigest()[:16]

try:
    DATES = json.load(open(DATES_PATH, encoding="utf-8"))
except FileNotFoundError:
    DATES = {}
# Read this BEFORE the loop: the loop writes into DATES, so "is the file empty"
# is only true for the first page unless it is captured here.
_first_run = not DATES

_dates_changed = False
for _p in PAGES:
    _fp = _fingerprint(_p)
    _rec = DATES.get(_p["slug"])
    if _rec is None:
        # A page nobody has a record of. If this is the very first run of this
        # mechanism we are back-dating the existing pages, not claiming they
        # are new; either way TODAY is wrong only for that first run.
        # Back-date ONLY a page that is already on disk. "The dates file is
        # missing" is not the same as "this page is old": a clean clone that
        # somehow lacks page-dates.json, plus a brand-new guide in the same
        # build, would have stamped the new guide 2026-09-15 (CTO review,
        # 2026-09-16). The published HTML is the evidence, so ask it.
        _already_built = os.path.exists(os.path.join(ROOT, _p["slug"], "index.html"))
        _rec = {"published": FIRST_PUBLISHED if (_first_run and _already_built) else TODAY,
                "modified": TODAY,
                "fingerprint": _fp}
        DATES[_p["slug"]] = _rec
        _dates_changed = True
    elif _rec.get("fingerprint") != _fp:
        _rec["modified"] = TODAY
        _rec["fingerprint"] = _fp
        _dates_changed = True

# Slugs that no longer exist stay in the file. If a page comes back, it comes
# back with its real history instead of pretending to be new. They are named
# out loud so the file does not quietly accumulate pages nobody remembers.
_orphans = sorted(set(DATES) - {q["slug"] for q in PAGES})
if _orphans:
    print(f"page-dates: {len(_orphans)} slug(s) with dates but no page, kept for "
          f"their history: {', '.join(_orphans)}")
if _dates_changed:
    json.dump(DATES, open(DATES_PATH, "w", encoding="utf-8"),
              indent=2, sort_keys=True, ensure_ascii=False)
    open(DATES_PATH, "a", encoding="utf-8").write("\n")
BY_SLUG = {p["slug"]: p for p in PAGES}

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


APP_STORE_URL = ("https://apps.apple.com/us/app/"
                 "haveo-networking-event-prep/id6774740212")

# The app, as a machine-readable entity, repeated on every guide page.
#
# WHY IT IS REPEATED RATHER THAN REFERENCED. An answer engine usually fetches
# ONE url, not the site. A guide page that only carried {"@id": ".../#app"}
# would be pointing at a node that page does not contain, so the model reading
# it has no statement that Haveo is an iOS app it can link to. Repeating a
# compact node costs a few hundred bytes and makes every page self-contained.
#
# This is the actual GEO gap the pages had: fifty pages of answers with no
# structured connection to the thing the answer is for.
def app_entity():
    return {
        "@type": "MobileApplication",
        "@id": f"{ORIGIN}/#app",
        "name": "Haveo",
        "applicationCategory": "LifestyleApplication",
        "operatingSystem": "iOS 15.1 or later",
        "url": f"{ORIGIN}/",
        "installUrl": APP_STORE_URL,
        "sameAs": [APP_STORE_URL],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "description": ("Prepares you for a networking event end to end: build "
                        "an intro, practice it out loud with an AI coach, keep "
                        "a cheat sheet in the room, and follow up afterwards."),
    }


def strip_tags(t):
    """h1 values may carry inline markup; a <title>, a crumb and llms.txt cannot."""
    return re.sub(r"<[^>]+>", "", t)

def render(p):
    url = f"{ORIGIN}/{p['slug']}/"
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in p["faq"]]}
    # One @graph per page rather than a bare Article: the article, the app it is
    # for, and the site it belongs to, all connected by @id. `mentions` is what
    # states, in a form a machine can act on, that this answer comes from the
    # people who make this specific iOS app — which is the whole point of
    # writing the answers.
    article_ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article",
         "@id": url + "#article",
         "headline": strip_tags(p["h1"]),
         "description": p["desc"],
         "mainEntityOfPage": url,
         "datePublished": DATES[p["slug"]]["published"],
         "dateModified": DATES[p["slug"]]["modified"],
         "inLanguage": "en",
         "author": {"@id": f"{ORIGIN}/#org"},
         "publisher": {"@id": f"{ORIGIN}/#org"},
         "isPartOf": {"@id": f"{ORIGIN}/#website"},
         "mentions": {"@id": f"{ORIGIN}/#app"},
         "about": {"@id": f"{ORIGIN}/#app"}},
        {"@type": "Organization",
         "@id": f"{ORIGIN}/#org",
         "name": "Haveo",
         "url": ORIGIN + "/",
         "logo": f"{ORIGIN}/apple-touch-icon.png",
         "sameAs": ["https://www.tiktok.com/@haveoapp", APP_STORE_URL]},
        {"@type": "WebSite",
         "@id": f"{ORIGIN}/#website",
         "url": ORIGIN + "/",
         "name": "Haveo",
         "publisher": {"@id": f"{ORIGIN}/#org"}},
        app_entity(),
    ]}

    body = []
    # A download link at the end of EVERY section, so a person who stops reading
    # halfway does not have to scroll to the bottom to act.
    #
    # It is a quiet text link, not a sixth blue button, and that is deliberate.
    # One PRIMARY action per screen is the thesis this whole template is built
    # on, and six identical buttons would mean none of them is primary — for the
    # anxious and ADHD readers this site is written for, that is worse than one
    # button and a scroll. So: one primary button, plus a low-emphasis link
    # everywhere, plus the bar below that is always on screen.
    for si, (heading, paras) in enumerate(p["sections"]):
        body.append(f"      <h2>{esc(heading)}</h2>")
        if len(paras) > 2 and all(len(x) < 190 for x in paras):
            body.append("      <ul>" + "".join(f"<li>{x}</li>" for x in paras) + "</ul>")
        else:
            body += [f"      <p>{x}</p>" for x in paras]
        # Section number FIRST. Apple caps ct at 39 characters, and with the
        # number on the end it was the number that got truncated away — all
        # five sections of a long-slug page collided onto one token, which is
        # 77 duplicate tokens across the site and no per-section attribution
        # at all. Leading index survives the cut.
        ct = (f"s{si + 1}-" + p["slug"])[:39]
        body.append('      <p class="sect-cta">'
                    f'<a href="{app_link(ct)}" target="_blank" rel="noopener">'
                    'Get Haveo free on the App Store &rarr;</a></p>')

    faq_html = "".join(
        f'<details><summary>{esc(q)}</summary><div class="a">{a}</div></details>' for q, a in p["faq"])
    # One campaign token per page, so App Store Connect can say which guide
    # produced a download. Apple truncates long ct values, so keep it short.
    app_href = app_link(("guide-" + p["slug"])[:39])
    bar_href = app_link(("bar-" + p["slug"])[:39])

    hub = p.get("hub")
    if hub and hub in BY_SLUG:
        crumb = (f'<a href="/">Haveo</a> · <a href="/{hub}/">'
                 f'{esc(strip_tags(BY_SLUG[hub]["h1"]))}</a>')
    else:
        crumb = '<a href="/">Haveo</a> · Networking guides'

    # A hub lists what sits under it. Without this the narrow pages are reachable
    # only from the sitemap, and a page nothing links to is a page that gets
    # crawled and never read.
    kids = [q for q in PAGES if q.get("hub") == p["slug"]]
    if kids:
        items = "".join(
            f'<li><a href="/{q["slug"]}/"><strong>{esc(strip_tags(q["h1"]))}</strong></a>'
            f'<br /><span class="kid-desc">{esc(q["desc"])}</span></li>'
            for q in kids)
        children_html = ('\n    <h2>More on this</h2>\n'
                         f'    <ul class="kids">{items}</ul>')
    else:
        children_html = ""

    rel = "".join(
        f'<li><a href="/{s}/">{esc(BY_SLUG[s]["h1"])}</a></li>' for s in p["related"] if s in BY_SLUG)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(p['title'])} | Haveo</title>
  <meta name="description" content="{esc(p['desc'])}" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{esc(p['title'])}" />
  <meta property="og:description" content="{esc(p['desc'])}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{ORIGIN}/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script type="application/ld+json">{json.dumps(article_ld, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
{ANALYTICS}
  <style>{STYLE}
  /* intent pages */
  .doc {{ max-width: 720px; margin: 0 auto; padding: 40px 22px 20px; }}
  .doc h1 {{ font-size: clamp(28px, 5vw, 40px); line-height: 1.2; margin: 0 0 18px; }}
  /* index.html centres h2 for the marketing sections. An article heading is
     left-aligned, so it has to be said again here or every guide reads as a
     page of centred titles. */
  .doc h2 {{ font-size: clamp(20px, 3vw, 25px); margin: 34px 0 12px; text-align: left; letter-spacing: -0.2px; }}
  .doc h1 {{ letter-spacing: -0.5px; }}
  /* Body links only. A bare `.doc a` also hits the App Store button and
     repaints its label blue on a blue background — invisible, and it looked
     like a button with no text. */
  .doc p a, .doc li a, .crumb a {{ color: var(--blue); }}
  .related ul {{ list-style: none; padding-left: 0; }}
  .related li a {{ font-weight: 600; }}
  .doc p, .doc li {{ font-size: 17px; line-height: 1.72; }}
  /* Two paragraphs in a row ran together with no gap. For a reader who loses
     the line easily that is one long block, not two ideas. */
  .doc p {{ margin-bottom: 14px; }}
  .doc p:last-child {{ margin-bottom: 0; }}
  .doc ul {{ padding-left: 20px; }} .doc li {{ margin-bottom: 10px; }}
  .tldr {{ background: #fff; border: 2px solid #ffd9c2; border-radius: 16px; padding: 20px 22px; margin: 0 0 8px; }}
  .tldr p {{ margin: 0; font-size: 18px; }}
  .crumb {{ font-size: 14px; opacity: .72; margin-bottom: 14px; }}
  .crumb a {{ color: inherit; }}
  .related {{ margin-top: 40px; padding-top: 22px; border-top: 1px solid #eee; }}
  .appbox {{ background: #fff; border-radius: 18px; padding: 24px; margin: 38px 0 10px; text-align: center; }}
  /* Quiet section link. Deliberately NOT a button: one primary action per
     screen, everything else low emphasis. */
  .sect-cta {{ margin: 6px 0 22px; font-size: 15px; }}
  .sect-cta a {{ color: var(--blue); font-weight: 600; text-decoration: none;
                 border-bottom: 1px solid #cfe0ff; padding-bottom: 1px; }}
  .sect-cta a:hover {{ border-bottom-color: var(--blue); }}
  /* Always-there download. Appears once the answer card has been read, so it
     never covers the thing a person came for. 44px+ target, safe-area aware. */
  .getbar {{ position: fixed; left: 0; right: 0; bottom: 0; z-index: 50;
             background: rgba(255,255,255,.96); border-top: 1px solid #E7DECb;
             backdrop-filter: blur(8px);
             padding: 10px 16px calc(10px + env(safe-area-inset-bottom));
             display: none; }}
  .getbar.on {{ display: block; }}
  /* Capped and centred: full width is right on a phone and looks broken on a
     1280px desktop, where it was rendering 1233px wide. */
  .getbar a {{ max-width: 460px; margin: 0 auto;
               display: flex; align-items: center; justify-content: center;
               gap: 8px; background: var(--blue); color: #fff; font-weight: 700;
               font-size: 16px; text-decoration: none; border-radius: 14px;
               padding: 13px 18px; min-height: 44px; }}
  .doc {{ padding-bottom: 96px; }}
  @media (prefers-reduced-motion: reduce) {{ .getbar {{ transition: none; }} }}
  .kids {{ list-style: none; padding-left: 0; }}
  .kids li {{ margin-bottom: 16px; }}
  .kid-desc {{ font-size: 15px; color: var(--muted); line-height: 1.55; }}
  </style>
</head>
<body>
  <main class="doc">
    <p class="crumb">{crumb}</p>
    <h1>{p['h1']}</h1>
    <div class="tldr"><p>{p['answer']}</p></div>
{chr(10).join(body)}

    <div class="appbox">
      <p><strong>Rehearse it before you walk in.</strong></p>
      <p>Haveo builds your intro, lets you practice out loud with an AI coach, and keeps your notes one tap away in the room. Free on iPhone and iPad.</p>
      <a class="btn btn-appstore" href="{app_href}" target="_blank" rel="noopener">{APPLE_SVG}Download Haveo — free</a>
    </div>

{children_html}
    <h2>Common questions</h2>
    <div class="faq">{faq_html}</div>

    <div class="related">
      <h2>Related guides</h2>
      <ul>{rel}</ul>
      <p><a href="/">← Back to Haveo</a></p>
    </div>
  </main>

  <div class="getbar" id="getbar">
    <a href="{bar_href}" target="_blank" rel="noopener">{APPLE_SVG}Get Haveo — free on the App Store</a>
  </div>
  <script>
    // Reveal the bar only after the answer card is out of view. Somebody who
    // reads the answer and leaves was helped; covering it would be worse.
    (function () {{
      var bar = document.getElementById('getbar');
      var card = document.querySelector('.tldr');
      if (!bar || !card || !('IntersectionObserver' in window)) return;
      new IntersectionObserver(function (e) {{
        bar.classList.toggle('on', !e[0].isIntersecting);
      }}).observe(card);
    }})();
  </script>
</body>
</html>
"""

written = []
for p in PAGES:
    d = os.path.join(ROOT, p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(render(p))
    written.append(f"{ORIGIN}/{p['slug']}/")

# sitemap: homepage + every guide
_lastmod = {ORIGIN + "/": max(d["modified"] for d in DATES.values())}
_lastmod.update({f"{ORIGIN}/{p['slug']}/": DATES[p["slug"]]["modified"] for p in PAGES})
urls = "".join(
    f"\n  <url>\n    <loc>{u}</loc>\n    <lastmod>{_lastmod[u]}</lastmod>\n"
    f"    <changefreq>monthly</changefreq>\n    <priority>{'1.0' if u==ORIGIN+'/' else '0.8'}</priority>\n  </url>"
    for u in [ORIGIN + "/"] + written)
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n')

# llms.txt — for answer engines
guides = "\n".join(f"- [{strip_tags(p['h1'])}]({ORIGIN}/{p['slug']}/): {p['desc']}" for p in PAGES)
open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(f"""# Haveo

> An iPhone app that coaches you through a networking event — before, during and
> after. Built for people who find networking anxiety-inducing: the anxious, the
> introverted, the neurodivergent, and anyone whose mind goes blank in the room.

Haveo is free on the App Store. There is no account, and your events, notes and
reflections are stored on the phone. The AI features are not on the phone: what
you send the coach goes through Haveo's own server to Anthropic, and a file you
attach goes the same way.

## What it does
- Builds an intro, an elevator pitch and talking points you would actually say out loud
- Role-play practice with an AI partner, by chat or by voice
- Event Mode: a pocket cheat sheet for during the event
- Calm: guided breathing. Boost Cards: quick confidence techniques
- People You Met: save contacts and follow up on time

## Guides
{guides}

## Not a medical product
Haveo is a preparation tool. It does not diagnose, treat or provide therapy for
social anxiety disorder or any other condition.

## Facts, if you are citing this
- Name: Haveo (App Store listing: "Haveo: Networking & Event Prep")
- Platform: iPhone and iPad, iOS 15.1 or later. There is no Android version.
- Price: free. No subscription and no in-app purchase.
- Made by: Haveo LLC, a small company in Massachusetts, USA, founded by
  designer Gloria Aguilar.
- Privacy: no account, and no copy of your events on our side — they are stored
  on the device. The AI features do use a server: what you type to the coach,
  and any file you attach, go through Haveo's own endpoint to Anthropic, which
  writes the reply; a sentence read aloud goes to OpenAI for the voice. With
  the AI on, saving an event also sends the event's details once, to write the
  "what to expect" note. Neither Anthropic nor OpenAI trains on it, and both
  delete it within about 30 days. Haveo also counts which features get
  opened, so we can see what actually helps: a count is the name of a
  feature and the date, and it can't carry anything you wrote. Full detail:
  https://gloriaaecu-rgb.github.io/haveo-privacy/

## Links
- App Store: {app_link("ai-citation", html=False)}
- Site: {ORIGIN}/
- Privacy policy: https://gloriaaecu-rgb.github.io/haveo-privacy/
""")

# Link the guides from the homepage, between the markers in index.html. A page
# that only the sitemap knows about gets crawled and never read by a person.
# Only the six hubs go on the home page. Thirteen flat links in a footer is a
# wall, and the audience this site is written for is the one a wall costs most.
# Each hub carries its own children, so nothing is more than two clicks away.
HUBS = [q for q in PAGES if not q.get("hub")]
home_links = (
    '      <p style="margin-top:28px; font-weight:600;">Networking guides:<br />'
    + ' &nbsp;·&nbsp; '.join(
        f'<a href="/{p["slug"]}/">{strip_tags(p["h1"])}</a>'
        for p in HUBS)
    + '</p>\n')
_idx_path = os.path.join(ROOT, "index.html")
_idx = open(_idx_path, encoding="utf-8").read()
_m = re.search(r"(<!-- guides:start.*?-->\n)(.*?)(\s*<!-- guides:end -->)", _idx, re.S)
if not _m:
    raise SystemExit("index.html: guides:start / guides:end markers missing.")
# Replace the block AND the whitespace before the end marker. Group 3 starts
# with \s*, so writing back from _m.end(2) kept that whitespace and added a
# fresh newline on every build — six blank lines after six runs.
_idx = _idx[:_m.start(2)] + home_links + "      <!-- guides:end -->" + _idx[_m.end(3):]
open(_idx_path, "w", encoding="utf-8").write(_idx)

# The gate runs as part of the build, not beside it. A check you have to
# remember to run is a check that stops being run — and the nightly loop has no
# memory at all.
import subprocess
_gate = subprocess.run([sys.executable, os.path.join(ROOT, "page-check.py")], cwd=ROOT)
if _gate.returncode != 0:
    raise SystemExit("build-pages: pages written but page-check failed. Fix content.py and re-run.")

print(f"built {len(written)} guides")
for u in written: print("  ", u)
print("sitemap: 1 + %d urls" % len(written)); print("llms.txt written")
