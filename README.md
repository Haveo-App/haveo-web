# Haveo Landing Page — haveo.app

The public site at **https://haveo.app**. `index.html` is the whole page;
`404.html` catches wrong links with a real 404 status — GitHub Pages serves it
for any address that is not a file. (On Netlify a wildcard redirect used to
return the home page with a 200; that is gone and must not come back.)

Page dates live in `page-dates.json`, written by `build-pages.py` from a hash of
each page's content: `published` is set once, `modified` moves only when the text
actually changes. Commit that file — without it the next build looks like a
rewrite of all 92 guides.

**This is not a waitlist and it never became one.** It started life as a
pre-launch demand test that measured email signups. The app has been live on the
App Store since 13 August 2026, so the page's job now is different: explain what
Haveo is, and send people to the App Store. Feedback arrives by email: the
"Send us feedback" button opens a message to hello@haveo.app. There is no signup rate to measure any more.

It's safe to share **publicly** (no API key in it, unlike the app link).

---

## How to put it live (since 2026-09-16: GitHub Pages)

**A push to `main` of this repository is the publish.** GitHub Actions runs
`.github/workflows/pages.yml`: `page-check.py` first — if it fails, nothing goes
live — then it uploads the site without the source files (this README,
PAGE-QUEUE.md, build-pages.py, content.py, page-check.py, page-dates.json,
netlify.toml, qa/). Live about a minute later. Progress: the repo's **Actions** tab.

```
python3 build-pages.py   # after editing content.py
python3 page-check.py    # the same gate CI runs
git push origin main     # this IS the publish
```

- `CNAME` holds the domain. Do not delete it: without it GitHub Pages drops
  haveo.app and serves the site at a github.io address.
- 404.html is served for any unknown path, with a real 404 status.
- **Feedback** is an email link (`mailto:hello@haveo.app`). The old form used
  Netlify Forms, which GitHub Pages does not have.
- Undo: `git revert` the commit and push. Or Actions → an older successful run →
  "Re-run all jobs".
- DNS lives at Namecheap: four A records to GitHub Pages (185.199.108.153,
  .109.153, .110.153, .111.153) and `www` as a CNAME to `gloriaaecu-rgb.github.io`.
  Leave the MX, SPF and google-site-verification records alone — they are email
  and Search Console.

**History.** Until 2026-09-16 this folder was `landing/` in the private app
repository, built by the Netlify site `meet-haveo` from the branch
`web-publicada`. It moved because Netlify's free credits ran out and deploys were
skipped. That branch no longer publishes anything.

## The demo-video script (record ~60–90 sec on your phone)

Add this video to the page later, OR post it straight to Reddit/TikTok with the
landing link. Keep it real and unpolished — authenticity converts better than
a glossy ad. Screen-record the **live app** doing the Create Your Intro flow.

**[0:00–0:08] — Hook (talk to camera or text on screen)**
> "If you get nervous before networking events… I built this for us."

**[0:08–0:35] — Show the magic moment (screen recording)**
- Open Create Your Intro.
- Type something real: *"I'm changing careers from teaching into UX design and I freeze when people ask what I do."*
- Let the AI respond and generate a warm, natural intro.
- Voiceover: *"You tell it your situation, and it helps you build an intro you'd actually say out loud."*

**[0:35–0:55] — Show one more tool (talking points or role-play by typing)**
- Voiceover: *"It also gives you talking points, and lets you practice the whole conversation — before you're in the room."*

**[0:55–1:10] — The ask**
> "It's free and early. If you've got an event coming up and want to try it,
> the link's below. I'd love your honest feedback."

**Recording tips:**
- iPhone: Control Center → Screen Recording. Talk over it after, or narrate live.
- Don't aim for perfect. A real, slightly-nervous founder voice is the point.
- 60–90 sec max. Front-load the hook in the first 3 seconds.

---

## What to measure now that the app is live

The signup rate this page was built to measure no longer exists — there is
nothing to sign up for. What is worth watching instead:

- **Taps on "Download on the App Store"**, against visits. That is the one
  number this page is now responsible for.
- **What the feedback form says.** A handful of real sentences about what is
  confusing beats any percentage at this stage.
- **Where they came from:** note which post drove each batch.

Retention and install numbers live in `RETENTION-PLAN.md`, not here.
