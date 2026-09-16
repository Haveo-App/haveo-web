# haveo.app — the page plan

**What this is.** The full shape of the site at ~50 pages, decided once so that
adding a page is never a fresh argument. `build-pages.py` renders whatever is in
`content.py`; this file says what goes in next and why.

**Why a plan at all.** On 15 September the site had one page earning search
impressions, and every query was somebody typing "haveo" or misspelling it.
There was no surface for a person who had not already heard of the app. Fifty
pages is not a traffic trick — it is one page per real question, because the
questions are genuinely separate and a person searching one of them does not
want the other forty-nine.

## How the site is shaped

Six **hubs**. Each hub answers a broad question completely and links to the
narrow pages under it. Each narrow page answers one question and links back.
That is the whole structure — no page is an orphan, and nothing is more than two
clicks from the home page.

Where a hub already had a URL earning impressions, that URL became the hub. A
second page competing with it would split the same search between two of our own
pages, which is a self-inflicted wound.

| Hub | For the person who |
|---|---|
| `/networking-with-social-anxiety/` | dreads the room itself |
| `/networking-for-introverts/` | can do it but it costs them |
| `/what-to-say-when-you-dont-know-anyone/` | freezes on the words |
| `/how-to-follow-up-after-a-networking-event/` | went, and then did nothing |
| `/neurodivergent-networking/` | is ADHD, autistic or dyslexic |
| `/job-search-networking/` | has to network because they need work |

## Where the queries came from

Google Autocomplete, mined 2026-09-15 for 33 seed phrases. Not a keyword tool
and not a guess — it is what Google itself completes when a person starts
typing. Two things it showed that changed the plan:

- **"social anxiety post event rumination"** and **"post event processing"** are
  real, repeated searches. That is the exact moment Haveo's Reflect step exists
  for, and nothing on the site addressed it.
- **ADHD and autistic networking searches are thin**, mostly "events near me".
  So neurodivergence is how every page is *written* — short paragraphs, the
  answer first, one action — and one hub, not forty pages of it. Building the
  site around a keyword that is not searched would have been a nice story and no
  traffic.

## Rules for anything added here

1. One question per page. If two questions share a page, neither ranks.
2. The complete answer is in the first paragraph. A person who reads only that
   has been helped, and an AI engine quoting only that has quoted something true.
3. It goes in `content.py`, never hand-written as HTML. One template, one design.
4. `COPY-RULES.md` applies to every word. No promised feelings, no idioms, US
   spelling, three sentences to a paragraph.
5. A page joins the queue with the query that justifies it written next to it.
   No query, no page.

## The queue

**All of it is live as of 2026-09-15** — 50 guide pages plus the home page.
`[x]` means shipped. Anything added below this line is the order to build in,
and joins the list only with the search query that justifies it.

### Hub: /networking-with-social-anxiety/ — live
- [x] the hub itself
- [x] `social-anxiety-after-a-networking-event` — "social anxiety post event rumination", "post event processing"
- [x] `the-hour-before-a-networking-event` — "social anxiety before event"
- [x] `how-to-leave-a-networking-event-early` — "when can i leave a networking event"
- [x] `how-to-go-to-a-networking-event-alone` — "going to a networking event alone"
- [x] `what-to-do-if-you-panic-at-an-event` — "networking event panic"
- [x] `do-i-actually-have-to-network` — "do i have to network", "i hate networking"

### Hub: /networking-for-introverts/ — live
- [x] the hub itself
- [x] `how-many-people-should-i-talk-to` — "how many people to talk to at networking event"
- [x] `networking-when-youre-already-drained` — "after work networking events"
- [x] `conferences-for-introverts` — "conference networking tips", "introvert conference"
- [x] `online-networking-for-introverts` — "virtual networking introvert"

### Hub: /what-to-say-when-you-dont-know-anyone/ — live
- [x] the hub itself
- [x] `what-to-say-instead-of-what-do-you-do`
- [x] `how-to-join-a-group-already-talking` — "how to join a conversation at a networking event"
- [x] `how-to-end-a-conversation-politely` — "how to leave a conversation politely"
- [x] `what-to-say-when-your-mind-goes-blank` — "mind goes blank networking"
- [x] `when-you-forget-someones-name` — "what to say when you forget someone's name"
- [x] `how-to-introduce-yourself-at-a-networking-event` — "how to introduce yourself networking"
- [x] `small-talk-questions-that-arent-boring` — "small talk questions", "small talk topics"
- [x] `how-to-introduce-two-people` — "how to introduce two people"

### Hub: /how-to-follow-up-after-a-networking-event/ — live
- [x] the hub itself
- [x] `follow-up-email-after-a-networking-event` — "networking follow up email template" (very high volume)
- [x] `linkedin-message-after-meeting-someone` — "linkedin networking message example"
- [x] `follow-up-email-subject-lines` — "networking follow up email subject line"
- [x] `what-to-do-with-the-business-cards` — "what to do with business cards after networking"
- [x] `following-up-late` — "how to follow up when you forgot", "is it too late to follow up"
- [x] `how-to-remember-who-you-met` — "how to remember people you met"
- [x] `what-to-say-in-a-coffee-chat` — "networking coffee chat questions"

### Hub: /neurodivergent-networking/ — live
- [x] the hub itself — "neurodivergent networking", "networking with adhd"
- [x] `networking-with-adhd` — "networking adhd reddit"
- [x] `autistic-networking-events` — "autism networking events"
- [x] `networking-with-dyslexia` — name badges, note-taking, written follow-up
- [x] `sensory-overload-at-events` — "sensory overload networking event"
- [x] `masking-at-work-events` — "masking at work events"
- [x] `rejection-sensitivity-after-networking` — "rsd after social event"

### Hub: /job-search-networking/ — live
- [x] the hub itself — "networking for a job"
- [x] `career-fair-what-to-say` — "career fair what to say", "job fair what to say"
- [x] `career-fair-with-social-anxiety` — "career fair social anxiety reddit"
- [x] `informational-interview-questions` — "informational interview questions"
- [x] `linkedin-networking-message-examples` — "linkedin networking message template"
- [x] `networking-as-a-student` — "how to network in college"
- [x] `networking-after-a-layoff` — "networking after being laid off"
- [x] `how-to-ask-for-a-referral` — "how to ask for a referral"
- [x] `networking-for-a-career-change` — "networking career change"

## What is deliberately NOT here

- **"networking events near me", "networking events miami".** The biggest
  volume in the whole mine, and wrong for us: those people want a list of
  events this Thursday. Haveo is not an events directory, and a page pretending
  otherwise would rank, disappoint, and bounce.
- **"elevator pitch examples".** High volume, and it belongs to books and
  templates. Worth revisiting once the site has any authority; pointless now.
- **Anything in Spanish.** The app ships in English. A translated page for an
  English-only app sends a person to an App Store listing they cannot read.

---

# Wave 2 — neurodivergence and anxiety at work

Added 2026-09-15. The first fifty pages are all about a networking event. This
wave widens the net to the same people in the rest of their working life, which
is where the searches actually are.

## Two lines this wave must not cross

**1. Nothing medical.** The site says, in its own words, "Haveo is a preparation
tool. It does not diagnose, treat or provide therapy." The mine is full of
queries that would contradict that, and they are excluded on purpose:

- `social anxiety disorder`, `dsm 5`, `icd 10`, `social anxiety test`, `treatment`
- `presentation anxiety medication`, `meds`, `pills`, `propranolol`
- `adhd at work symptoms`, `adhd quiz`, `autistic burnout symptoms`,
  `autistic burnout vs depression`, `autistic burnout quiz`

Some of those are high volume. They are still out. A preparation tool writing
about diagnosis is both untrue to itself and the kind of claim Apple and Google
both look at closely.

**2. Nothing that reads as legal advice.** `dyslexia at work discrimination`,
`ada accommodations`, and the `disclosing adhd to employer uk/canada/australia`
variants are employment law, and it differs by country. The disclosure pages
here describe **the decision a person is making and what people actually do** —
never what an employer is obliged to do. Each says plainly that it is not legal
advice and that the rules vary by country.

## Do not cannibalise wave 1

These already exist and are about an EVENT. The work pages must stay on the
working day, and link across rather than repeat:

`/networking-with-adhd/` · `/networking-with-dyslexia/` ·
`/autistic-networking-events/` · `/masking-at-work-events/` ·
`/sensory-overload-at-events/` · `/rejection-sensitivity-after-networking/`

So: no general "masking at work" page — the events one owns that phrase. No
second ADHD-and-networking page.

## The queue

### Hub: /adhd-at-work/ — "adhd at work tips", "adhd at work support"
- [x] the hub itself
- [x] `adhd-job-interview` — "adhd job interview tips/adjustments/prep" (strongest in the whole mine)
- [x] `adhd-in-meetings` — "adhd meetings at work", "adhd zoom meetings"
- [x] `adhd-remote-work` — "adhd remote work tips/accommodation"
- [x] `adhd-note-taking` — "adhd note taking template/methods/tips"
- [x] `adhd-time-blindness-at-work` — "adhd time blindness at work/late for work"
- [x] `adhd-and-email-at-work` — "adhd email overwhelm"
- [x] `telling-your-employer-you-have-adhd` — "should you disclose adhd to employer"
- [x] `adhd-accommodations-at-work` — "asking for accommodations at work adhd"

### Hub: /dyslexia-at-work/ — "dyslexia at work support/adjustments"
- [x] the hub itself
- [x] `dyslexia-email-signature` — "dyslexia email signature/disclaimer" (thin and real)
- [x] `reading-out-loud-at-work` — "dyslexia difficulty reading out loud"
- [x] `writing-emails-with-dyslexia` — "dyslexic email"
- [x] `dyslexia-and-note-taking` — meetings, names, actions
- [x] `dyslexia-in-a-job-interview` — on-the-spot reading and written tests
- [x] `telling-your-employer-you-have-dyslexia` — "should i tell employer i have dyslexia"
- [x] `dyslexia-accommodations-at-work` — "dyslexia adjustments at work"

### Hub: /social-anxiety-at-work/ — "social anxiety at work events/meetings/functions"
- [x] the hub itself
- [x] `speaking-up-in-meetings` — "difficulty speaking up in meetings", "confidence speaking up"
- [x] `work-parties-and-socials` — "work party anxiety", "work events give me anxiety"
- [x] `the-office-christmas-party` — "work christmas party anxiety" (seasonal, strong)
- [x] `first-day-at-a-new-job` — "first day new job anxiety" (strong)
- [x] `video-call-anxiety` — "why do video calls make me anxious"
- [x] `performance-review-anxiety` — "annual review anxiety"
- [x] `one-on-ones-with-your-manager` — "one on one with manager anxiety"
- [x] `team-lunches-and-work-food` — "work lunch anxiety"
- [x] `going-back-to-the-office` — "return to office anxiety"
- [x] `imposter-syndrome-at-work` — "imposter syndrome at work examples"
- [x] `presenting-at-work` — "presentation anxiety tips" (tips ONLY, no medication)

### Hub: /autistic-at-work/
- [x] the hub itself
- [x] `autistic-burnout-after-work-events` — recovery framing only, never symptoms or diagnosis
- [x] `asking-for-accommodations-at-work` — "asking for accommodations at work autism"
- [x] `sensory-issues-in-an-office` — open plan, lighting, noise
- [x] `small-talk-in-the-office` — "office small talk"
- [x] `telling-your-employer-you-are-autistic`

### Hub: /job-interviews/
- [x] the hub itself
- [x] `social-anxiety-in-interviews` — "social anxiety interview"
- [x] `video-interview-anxiety`
- [x] `what-to-say-about-your-weakness` — "adhd job interview weakness"
- [x] `asking-for-interview-adjustments` — "adhd job interview adjustments/accommodations"
- [x] `interview-questions-you-can-prepare`
- [x] `the-day-before-an-interview`

**All shipped 2026-09-15.** 92 guide pages plus the home page: 93 URLs.
