#!/usr/bin/env python3
"""Haveo's page content. Data only — `build-pages.py` renders it.

WHY THIS FILE IS SEPARATE. The renderer is a template and changes rarely; the
content changes constantly, and a daily loop adds to it. Keeping them apart
means adding a page is a data edit that cannot break the design system, and a
template fix is one diff instead of fifty.

HOW A PAGE IS BUILT, AND WHY IT IS BUILT THAT WAY
=================================================
The reader Haveo is written for finds dense pages hard: the app's own audience
skews anxious, ADHD and dyslexic. So the template is not a style preference, it
is the product thesis applied to a web page.

  - The complete answer is in the first paragraph, inside a bordered card, above
    everything else. Somebody who reads that and leaves has been helped.
  - Paragraphs run to three sentences. Longer ones get split.
  - Body text is left-aligned, 17px, line-height 1.72, and the column is capped
    at 720px, which lands near the 65-character line that stops a dyslexic
    reader losing their place between lines.
  - Headings are left-aligned and carry real weight contrast, not just size.
  - Options are lists, never a paragraph with commas in it.
  - ONE primary call to action per page, in one place, with an icon AND a word.
  - The FAQ is collapsed. It is there for the person who wants it and invisible
    to the person who does not.
  - No autoplay, no decorative motion, no external script.

FIELDS
  slug      the URL segment. /<slug>/
  hub       the slug of the hub page this sits under. None for a hub.
  h1        the page's real heading, in the words a person would use
  title     the <title>. Title Case. Never ALL CAPS (COPY-RULES.md).
  desc      the meta description, and the sentence llms.txt shows
  answer    the whole answer in ~45 words. HTML allowed, one <strong> at most.
  sections  [(heading, [paragraph or list-item, ...]), ...]
  faq       [(question, answer), ...]
  related   slugs to link at the foot

COPY RULES THAT APPLY TO EVERY WORD HERE — the full set is in COPY-RULES.md.
  - Never promise a feeling or an outcome. Not "you've got this", not "you'll
    feel confident". Describe what to DO.
  - Plain words. No idioms. US spelling. Maya does not read English natively and
    an idiom is a sentence she cannot use.
  - Warmth comes from naming something true, never from cheering.
"""

PAGES = [
{
 "slug": "what-to-say-when-you-dont-know-anyone",
 "hub": None,
 "h1": "What to say at a networking event when you don't know anyone",
 "title": "What to Say When You Don't Know Anyone",
 "desc": "Three openers that work on a room full of strangers, what to say after the first line, and how to leave a conversation kindly.",
 "answer": "Walk up to someone standing alone and say: <strong>\"Mind if I join you? I don't know anyone here either.\"</strong> It works because it is true, it gives the other person an easy yes, and it names the thing you are both already feeling. You do not need a clever line. You need one sentence you have said out loud before you arrive.",
 "sections": [
   ("The three openers that actually work", [
     "<strong>The honest one.</strong> \"Mind if I join you? I don't know anyone here either.\" Best on a person standing alone — which, at any event, is most people at some point in the night.",
     "<strong>The logistics one.</strong> \"Is this your first time at one of these?\" It works on anyone, it has no wrong answer, and it hands them the talking.",
     "<strong>The shared-situation one.</strong> \"How did you end up here?\" People like answering this. It is a story question disguised as small talk.",
   ]),
   ("What to say after the first line", [
     "The opener is not the hard part — the next ninety seconds are. Have two follow-up questions ready before you arrive, tied to <em>this</em> room rather than to them personally: what brought you here, what are you working on, what's been the best thing you've seen today.",
     "If your mind goes blank, describe the room. \"That coffee queue is not moving.\" Shared circumstance is the cheapest conversational fuel there is, and nobody has ever been judged for mentioning it.",
   ]),
   ("How to leave without it being awkward", [
     "Say the true thing plus a next step: \"I'm going to grab a drink — it was good to meet you.\" You do not owe anyone an excuse. Ending a conversation cleanly is a kindness, not a rejection, and it is what lets you talk to more than one person all evening.",
   ]),
   ("Prepare the opener before you go", [
     "Every line above works better if you have said it out loud once. That is the whole idea behind Haveo: write your intro, rehearse it by speaking, and keep it one tap away in your pocket when the room gets loud.",
   ]),
 ],
 "faq": [
   ("What if they're already in a group?", "Approach groups of three or more rather than pairs — pairs are usually mid-conversation, groups have gaps. Stand at the edge, wait for a pause, and say \"mind if I join?\" Most people will widen the circle without breaking stride."),
   ("What if I run out of things to say?", "Ask them to expand on the last thing they said: \"How did that go?\" or \"What made you pick that?\" You do not have to introduce a new topic — you can always go one level deeper on the current one."),
   ("Is it obvious that I'm nervous?", "Almost never. Speakers overestimate how visible their own nerves are — in Savitsky and Gilovich's 2003 speech study (<em>Journal of Experimental Social Psychology</em>), speakers judged their anxiety far more visible than their audience did. You feel your heart; they see a person talking."),
 ],
 "related": ["networking-with-social-anxiety", "what-to-say-instead-of-what-do-you-do"],
},
{
 "slug": "networking-with-social-anxiety",
 "hub": None,
 "h1": "How to prepare for a networking event when you have social anxiety",
 "title": "How to Prepare for a Networking Event With Social Anxiety",
 "desc": "A preparation routine for anxious networkers: what to write down, what to rehearse out loud, and what to do in the first ten minutes.",
 "answer": "Prepare three things and nothing else: <strong>one sentence about who you are, two questions you will ask, and one exit line.</strong> Rehearse them out loud, not in your head — saying a sentence aloud once makes it dramatically easier to say it again under stress. Then give yourself permission to leave after one real conversation.",
 "sections": [
   ("Why preparation works better than confidence advice", [
     "\"Just be yourself\" and \"be confident\" are not instructions — they are outcomes. Anxiety before a room full of strangers is largely a <em>preparation</em> problem wearing a personality costume. You are not bad at this. You are walking in without a script, which would make anyone freeze.",
   ]),
   ("The three things to write down", [
     "<strong>Your one sentence.</strong> Who you are and what you are into, in a form you would actually say aloud. Not a job title recital — a sentence a human would use.",
     "<strong>Two questions.</strong> Prepared, generic, reusable. \"What brought you here?\" and \"What are you working on?\" will carry an entire evening.",
     "<strong>One exit line.</strong> Knowing how you will leave a conversation is what makes it safe to start one.",
   ]),
   ("Rehearse out loud, not in your head", [
     "Reading your intro silently is not rehearsal. Say it aloud — to a mirror, a voice recorder, or an AI that will not judge how it comes out. The first time you hear your own sentence should not be in front of a stranger.",
   ]),
   ("The first ten minutes", [
     "Arrive early if you can. An empty room is far easier to enter than a full one, and the people who arrive early are usually the ones who also find this hard.",
     "Get a drink so your hands have a job. Then talk to one person standing alone.",
   ]),
   ("Set a finish line before you arrive", [
     "Decide in advance what \"done\" means — one real conversation, or thirty minutes. Having a defined end makes the whole thing survivable, and you will usually stay longer than you planned once the first conversation is behind you.",
   ]),
 ],
 "faq": [
   ("Is networking anxiety the same as social anxiety disorder?", "No. Feeling anxious before a room of strangers is extremely common and is not in itself a disorder. Social anxiety disorder is a clinical diagnosis made by a professional. Haveo is a preparation tool, not treatment, and it does not diagnose anything."),
   ("Should I go if I'm dreading it?", "Set a small, specific goal — one conversation — and let yourself leave after it. Most of the dread is about the imagined whole evening, not the part you actually have to do."),
   ("What if I freeze mid-conversation?", "Silence is far shorter than it feels. Ask a question you prepared, or say \"sorry, I lost my thread\" — which is a completely normal thing that people say to each other."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "networking-for-introverts"],
},
{
 "slug": "what-to-say-instead-of-what-do-you-do",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "What to say instead of \"so, what do you do?\"",
 "title": "Better Questions Than \"So, What Do You Do?\"",
 "desc": "Why the standard opener falls flat, and eight questions that get a real answer instead of a job title.",
 "answer": "Ask <strong>\"what are you working on at the moment?\"</strong> instead. It gets you a real answer rather than a job title, it works whether the person is employed, freelancing, studying or between things, and it invites them to talk about the part they actually find interesting.",
 "sections": [
   ("Why the standard question falls flat", [
     "\"What do you do?\" asks for a label. It also lands badly on anyone who is between jobs, changing careers, or does something hard to say in three words — which is a large share of any room. You get a title, you say \"oh, nice,\" and you are both stuck.",
   ]),
   ("Eight questions that get a real answer", [
     "What are you working on at the moment?",
     "How did you end up here?",
     "What's been the best thing you've seen today?",
     "What's taking up most of your time right now?",
     "Is this your first one of these?",
     "What made you want to come?",
     "What would make tonight worth it for you?",
     "What are you hoping to figure out this year?",
   ]),
   ("What to do when they ask you", [
     "They will still ask you the standard question — so have a sentence ready that answers the label question and hands back something to grab onto: what you do, plus what you are into right now. That second half is what turns an exchange of titles into a conversation.",
   ]),
 ],
 "faq": [
   ("Isn't \"what do you do\" fine in a professional setting?", "It is fine, it is just low-yield. You can ask it and immediately follow with \"and what part of that do you actually like?\" — the follow-up is where the conversation starts."),
   ("What if I don't have an impressive answer?", "Nobody is grading you. \"I'm figuring out my next thing\" is a completely normal sentence and often a more interesting conversation than a job title."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "how-to-follow-up-after-a-networking-event"],
},
{
 "slug": "how-to-follow-up-after-a-networking-event",
 "hub": None,
 "h1": "How to follow up after meeting someone at a networking event",
 "title": "How to Follow Up After a Networking Event (With Examples)",
 "desc": "When to send the message, what to write, and a short template that doesn't read like a form letter.",
 "answer": "Send it <strong>within 48 hours</strong>, keep it to three sentences, and name one specific thing you talked about. Something like: \"Hi Sam — good to meet you at the design meetup. Still thinking about what you said about hiring juniors. Would be good to stay in touch.\" That is the whole job.",
 "sections": [
   ("Send it within 48 hours", [
     "The specific detail that makes a follow-up land is the one you forget first. Two days out you still remember the conversation; a week out you are sending a generic note, and generic notes read as transactional — which is exactly the reason most people never send one at all.",
   ]),
   ("The three-sentence shape", [
     "<strong>Where you met.</strong> One clause. They met a lot of people too.",
     "<strong>The specific thing.</strong> Something they actually said. This is the entire message — it proves you listened.",
     "<strong>The low-pressure close.</strong> \"Would be good to stay in touch.\" No ask, no meeting request, no pitch.",
   ]),
   ("What makes a follow-up feel impersonal", [
     "Templates that could have been sent to anyone, an ask in the first message, and flattery with no detail behind it. If your note would still make sense addressed to a different person, it is not a follow-up — it is a mass email.",
   ]),
   ("Write the note before you forget", [
     "Capture the detail while you are still there — a line in your phone as you leave. Haveo has this built in: save who you met, keep the one thing you talked about, and set your own reminder to send the message.",
   ]),
 ],
 "faq": [
   ("Should I connect on LinkedIn or send an email?", "Either, but always add a note. A bare connection request is the same as no follow-up. If you have their email and the conversation was substantial, email carries more weight."),
   ("What if I don't have a reason to follow up?", "\"Good to meet you, would be good to stay in touch\" is a complete and sufficient reason. Not every message needs a purpose attached."),
   ("What if they don't reply?", "Very often nothing is wrong — people are busy and inboxes are full. One follow-up is generous; a second, weeks later with something genuinely useful attached, is fine. Beyond that, let it go."),
 ],
 "related": ["what-to-say-instead-of-what-do-you-do", "networking-for-introverts"],
},
{
 "slug": "networking-for-introverts",
 "hub": None,
 "h1": "Networking for introverts",
 "title": "Networking for Introverts — A Practical Approach",
 "desc": "How to get through a networking event as an introvert: fewer, longer conversations, an energy budget, and preparation that removes the improvisation.",
 "answer": "Do not try to meet everyone. <strong>Aim for two or three real conversations, not twenty introductions</strong> — depth is the introvert advantage, and it is also what people remember. Prepare your opener, give yourself a defined end time, and take a break outside when you need one.",
 "sections": [
   ("Play to depth, not volume", [
     "The extrovert model of networking — circulate, collect cards, meet everyone — is not the only model and it is not the effective one. One person who remembers a real conversation with you is worth more than twenty who half-remember your name.",
   ]),
   ("Budget your energy honestly", [
     "Decide before you arrive how long you are staying and hold to it. Leaving at your planned time having done the thing is a success. Staying three hours and dreading the next event is not.",
     "Stepping outside for five minutes is a legitimate strategy, not a failure of nerve.",
   ]),
   ("Prepare so you're not improvising", [
     "Improvisation is the expensive part for introverts — it burns energy fast. Written and rehearsed material means you spend the evening listening rather than composing. Prepare your sentence, two questions and an exit line, and rehearse them out loud.",
   ]),
   ("Arrive early", [
     "Entering a half-empty room is far easier than joining a loud one, conversations start naturally, and the people already there are usually the ones who also find this hard.",
   ]),
 ],
 "faq": [
   ("Is being an introvert a disadvantage at networking events?", "No — introverts tend to be better listeners and to hold longer, more memorable conversations. The disadvantage is only in the format, which rewards circulating. Change the goal and the format stops mattering."),
   ("How many people should I talk to?", "Two or three real conversations is a good night. Counting introductions is the wrong metric."),
   ("What if I need to leave early?", "Then leave. \"I'm heading off — it was good to meet you\" needs no justification."),
 ],
 "related": ["networking-with-social-anxiety", "what-to-say-when-you-dont-know-anyone"],
},
]

# ============================================================ hubs and tranche 2
# Added 2026-09-15. Two new hubs plus the six highest-demand children from the
# autocomplete mine. See PAGE-QUEUE.md for the whole plan and the query behind
# each page.

PAGES += [
{
 "slug": "neurodivergent-networking",
 "hub": None,
 "h1": "Networking when you are ADHD, autistic or dyslexic",
 "title": "Networking When You Are ADHD, Autistic or Dyslexic",
 "desc": "Networking rooms assume a brain that filters noise, holds names and improvises. If yours does not, the fix is preparation and a shorter night.",
 "answer": "A networking room asks you to filter noise, hold new names in your head, read a badge across a table and improvise a sentence, all at once. <strong>If that is hard for you, the room is the problem, not your effort.</strong> Write your sentences down, plan to leave early, and take notes on your phone instead of trying to remember.",
 "sections": [
   ("What the room is actually asking of you", [
     "Filter a loud space down to one voice. Hold three new names long enough to use them. Read small print on a badge at arm's length.",
     "Produce a fluent sentence about yourself with no warning. Track when a conversation is ending. Do all of it for two hours without a break.",
     "Most advice about networking skips every one of those and goes straight to \"be confident\". That is why it does not help.",
   ]),
   ("Decide the shape of the night before you go", [
     "<strong>Pick an end time.</strong> Not a hope, a time. Leaving at your planned time having spoken to two people is the night working, not the night failing.",
     "<strong>Pick one goal.</strong> Two real conversations, or one specific person. A goal you can finish is a goal you can stop chasing.",
     "<strong>Plan the break.</strong> Five minutes outside, at a decided point, not when you are already past it.",
   ]),
   ("Write the sentences down", [
     "Improvising is the expensive part. A sentence you have said out loud once costs almost nothing to say again; a sentence you are composing in a loud room costs everything you have.",
     "Three pieces are enough: who you are, two questions you will ask, and one line for leaving. Say each one aloud before you go.",
   ]),
   ("Take the notes, do not carry them", [
     "Type the name and one detail into your phone the moment you walk away. Nobody minds, and everybody assumes you are answering a message.",
     "This is the single change that fixes the most: the follow-up you cannot write is almost never a writing problem, it is that the detail is gone.",
   ]),
   ("What Haveo does with this", [
     "Haveo is built on the assumption that the preparation is the hard part. You write your sentences, practice them out loud with an AI that is not judging how it comes out, and keep them one tap away in the room. The notes and the reminder to follow up live in the same place.",
   ]),
 ],
 "faq": [
   ("Should I tell people I am neurodivergent?", "You never owe anyone that. If you want a practical accommodation you can ask for the thing without the label: \"can we step somewhere quieter\" works on its own."),
   ("Is it worse to leave early or to stay and go quiet?", "Leave. A person who spoke to two people and left is remembered as those two conversations. A person who stayed three hours and went silent is remembered as quiet, if at all."),
   ("Everyone says just practice more. Does it get easier?", "The specific parts get easier with repetition — your own sentence, joining a group, leaving a conversation. The noise and the name-holding do not, which is why the answer is notes and a shorter night rather than more exposure."),
 ],
 "related": ["networking-with-adhd", "networking-with-dyslexia", "networking-with-social-anxiety"],
},
{
 "slug": "networking-with-adhd",
 "hub": "neurodivergent-networking",
 "h1": "Networking with ADHD",
 "title": "Networking With ADHD — What Actually Helps",
 "desc": "Interrupting, losing the thread, forgetting names, then not following up. The fix for each, and why the follow-up is the one worth solving first.",
 "answer": "The hard parts are usually four: you interrupt, you lose the thread mid-sentence, you forget every name, and you never send the follow-up. <strong>Fix the follow-up first</strong> — it is the one that costs you something real, and it is solved by typing a name and one detail into your phone the second you walk away.",
 "sections": [
   ("The follow-up is the one that costs you", [
     "The other three are awkward in the moment and forgotten by everyone but you. The follow-up you never sent is the job, the client or the friend that did not happen.",
     "It fails for a reason that has nothing to do with discipline: by the time you are home, the name and the reason are gone. You cannot write a message you have no material for.",
     "So the note is not admin, it is the whole thing. Name, and one detail you would not find on their LinkedIn.",
   ]),
   ("Interrupting", [
     "You are not being rude, you are offloading a thought before it disappears. That is a real constraint and it has a physical fix: put the thought somewhere else.",
     "Type three words into your phone, or hold one finger against your leg. Saying \"sorry, go on — I want to come back to something\" also works, and most people read it as interest.",
   ]),
   ("Losing the thread halfway through a sentence", [
     "Say so plainly. \"I have completely lost where I was going with that\" is a normal sentence that costs you nothing, and the other person almost always supplies the thread.",
     "The alternative — talking on while searching for the point — is the thing that actually reads badly.",
   ]),
   ("Names", [
     "Use it once immediately: \"good to meet you, Priya.\" Then type it into your phone within a minute. Do not rely on repeating it in your head, because the next voice will take it.",
     "If it is already gone, see the page on forgetting a name. Asking again on the same night is completely ordinary.",
   ]),
   ("Set an end time before you arrive", [
     "Hyperfocus and a crash both live in the same evening. Deciding when you leave, before you are inside, is what stops the night ending on whichever one arrives first.",
   ]),
 ],
 "faq": [
   ("Is it better to go early or late?", "Early. A half-empty room is quieter, conversations start without you having to break into anything, and the people who arrive early are usually the ones who also find this hard."),
   ("What if I talk too much?", "Ask a question roughly every third thing you say. It is a mechanical rule rather than a personality change, which is why it works when you are not monitoring yourself."),
   ("Does medication timing matter?", "That is a question for whoever prescribes it, not for us. What we can say is that people who plan the evening around their own predictable crash report an easier night than people who plan around the event's schedule."),
 ],
 "related": ["neurodivergent-networking", "when-you-forget-someones-name", "how-to-follow-up-after-a-networking-event"],
},
{
 "slug": "networking-with-dyslexia",
 "hub": "neurodivergent-networking",
 "h1": "Networking with dyslexia",
 "title": "Networking With Dyslexia",
 "desc": "Name badges you cannot read at arm's length, a written follow-up you keep putting off, and reading aloud you did not agree to. What to do about each.",
 "answer": "Three things make a networking room harder with dyslexia: badges in small print, notes you cannot take fast enough, and the written follow-up afterwards. <strong>Say the name back instead of reading it, dictate your notes instead of typing them, and draft the follow-up by speaking it.</strong>",
 "sections": [
   ("Badges", [
     "Nobody reads a badge well at conversational distance, so asking is normal and nobody marks it. \"Sorry, say your name again for me?\" is a sentence people hear ten times a night.",
     "Then say it back once. Hearing it and saying it puts it somewhere more reliable than having glanced at it.",
   ]),
   ("Notes, without writing", [
     "Use dictation. Step aside, hold the microphone key and say \"Priya, runs ops at the bakery place, wants a supplier in Leeds.\" It takes eight seconds and you never spell anything.",
     "A voice memo works the same way. The point is to capture it while it is still in your head, in whatever form is fastest for you.",
   ]),
   ("The follow-up message", [
     "This is where most of the cost lands. The message gets delayed because writing it is effortful, and then it is too late to send, and the whole evening is wasted.",
     "Speak it first, then tidy it. Dictate the message as if you were talking to them, then fix what needs fixing. A short, plain message sent on Tuesday beats a polished one that never goes.",
   ]),
   ("If you are asked to read something out", [
     "You are allowed to decline without a reason. \"I'd rather not read it cold — can you summarize it?\" ends it, and nobody investigates.",
   ]),
   ("What Haveo does with this", [
     "You can talk to Haveo instead of typing — your phone turns your voice into text, and on iPhone that happens on the device itself. Your intro, your notes and your follow-up can all be spoken rather than written.",
   ]),
 ],
 "faq": [
   ("Should I tell people?", "Only if you want to. Every fix on this page works without explaining anything — asking for a name and dictating a note are things people without dyslexia do constantly."),
   ("What about spelling someone's name in the follow-up?", "Copy it from their LinkedIn or their card rather than from memory. Getting a name wrong in writing is the one error worth a few seconds of checking."),
   ("Are printed notes in my pocket a bad idea?", "No, but they are hard to use in a room. A phone screen you can enlarge, and that can read a line back to you, is usually easier than paper you have to find good light for."),
 ],
 "related": ["neurodivergent-networking", "how-to-follow-up-after-a-networking-event", "what-to-say-when-you-dont-know-anyone"],
},
{
 "slug": "job-search-networking",
 "hub": None,
 "h1": "Networking when you need a job",
 "title": "Networking When You Need a Job",
 "desc": "Networking under pressure is a different problem: you need something, they can tell, and asking directly usually fails. What to ask for instead, and when.",
 "answer": "Do not ask for a job. <strong>Ask for information, and ask the person most likely to actually answer</strong> — someone doing the work you want, one level above you, not a hiring manager. A specific question about their work gets a reply; \"are you hiring\" almost never does.",
 "sections": [
   ("Why asking for a job does not work", [
     "The person you are asking usually cannot give you one. Even when they can, the request puts them in the position of saying no to someone who needs help, so many people simply do not reply.",
     "A question they can answer in three sentences has none of that weight. And the person who answered a question is the person who thinks of you when something opens.",
   ]),
   ("Who to actually talk to", [
     "<strong>Someone doing the job you want, a level or two above you.</strong> They know what the work is really like and what gets someone hired, and their inbox is not full of applicants.",
     "<strong>Someone who moved from where you are to where you want to be.</strong> They have made the argument for a person like you before.",
     "<strong>Not, usually, a recruiter or hiring manager cold.</strong> They are the right people to reach once someone inside can mention you.",
   ]),
   ("What to ask", [
     "\"What does the first ninety days actually look like in your team?\" \"What did you not know about this move before you made it?\" \"What would make you look twice at someone coming from my background?\"",
     "Each of those is answerable, none of them is a favor, and all of them tell you something you cannot get from a job posting.",
   ]),
   ("When to say what you need", [
     "At the end, once, plainly: \"I'm looking for a role in X — if anything crosses your desk I'd appreciate a heads up.\" No pressure, no attachment, no follow-up question.",
     "That sentence converts far better after they have spent ten minutes talking about their work than it does in a first message.",
   ]),
   ("If you were laid off", [
     "Say it early and without apology. \"My role was cut in the restructure, so I'm looking\" is a complete explanation and it is extremely common right now.",
     "People help far more readily when the reason is clear and they do not have to guess whether asking is rude.",
   ]),
 ],
 "faq": [
   ("Is it worth going to general networking events for a job?", "Less than a targeted message to one person. General events are good for practice and for finding out what is happening in an industry; they are inefficient as a job channel."),
   ("How many people should I reach out to?", "Few, well. Five specific messages to people whose work you can actually reference beat fifty generic ones, and the fifty will damage how you feel about doing it at all."),
   ("What if they do not reply?", "Most will not, and it is almost never about you. One follow-up after ten days, then leave it."),
 ],
 "related": ["career-fair-what-to-say", "how-to-follow-up-after-a-networking-event", "networking-with-social-anxiety"],
},
{
 "slug": "career-fair-what-to-say",
 "hub": "job-search-networking",
 "h1": "What to say at a career fair",
 "title": "What to Say at a Career Fair",
 "desc": "The thirty seconds at the table, the question that makes a recruiter remember you, and how to leave with something you can follow up on.",
 "answer": "Say who you are, what you are looking for, and one specific thing about them, in about twenty seconds. <strong>Then ask what they look for in someone in your position.</strong> Before you walk away, get a name and an email — a table with no name is a table you cannot follow up.",
 "sections": [
   ("The twenty seconds", [
     "\"Hi, I'm Sam — I'm finishing a computer science degree and looking for a junior backend role. I saw you moved your platform onto Go last year.\"",
     "Three parts: who, what you want, one specific thing. The third part is what separates you from the hundred people who said the first two.",
   ]),
   ("The question to ask", [
     "\"What do you look for in someone applying at my level?\" It is a question they know the answer to and like giving, and the answer tells you exactly how to write your application.",
     "Avoid \"what does your company do\" — the answer is on the banner behind them, and asking it says you did not look.",
   ]),
   ("Leave with a name", [
     "\"Can I get your name and the best address to send my application to?\" Then write both down before you reach the next table.",
     "Without this, a career fair is an afternoon of conversations you cannot act on.",
   ]),
   ("Plan which tables, and how many", [
     "Pick five before you go. Walking a whole hall means arriving at the tables you care about tired and out of sentences.",
     "Do your worst-fit table first. The first conversation is always the roughest one and it is better spent on a company you do not want.",
   ]),
   ("What to bring", [
     "A phone you can take notes on, and enough copies of a résumé for your five tables. Most recruiters will tell you to apply online anyway — the paper is a prompt for the conversation, not the application.",
   ]),
 ],
 "faq": [
   ("What if there is a queue behind me?", "Keep it to the twenty seconds and one question, get the name, and leave. A short, clear conversation is remembered better than a long one that held people up."),
   ("Do I have to wear a suit?", "Match the industry, and when in doubt go one step smarter than you think. Nobody has ever been marked down for it, and it is one fewer thing to think about on the day."),
   ("Is it worth going if I am not graduating yet?", "Yes, and it is easier. \"I'm a year out, I'm trying to work out what to aim at\" takes all the pressure off and recruiters are noticeably more relaxed about it."),
 ],
 "related": ["job-search-networking", "networking-with-social-anxiety", "how-to-follow-up-after-a-networking-event"],
},
{
 "slug": "social-anxiety-after-a-networking-event",
 "hub": "networking-with-social-anxiety",
 "h1": "When you cannot stop replaying it afterwards",
 "title": "When You Cannot Stop Replaying a Networking Event",
 "desc": "Going over every sentence for days afterwards has a name — post-event processing. What it is, why the replay is not accurate, and what to do on the night instead.",
 "answer": "Going over the evening line by line afterwards is called post-event processing, and it is one of the most documented parts of social anxiety. <strong>The replay is not a recording — it is heavily weighted toward your worst moments.</strong> Writing down what actually happened, on the night, is what stops it becoming the memory.",
 "sections": [
   ("What is happening", [
     "After a social event, attention turns inward and reviews it. The review is not neutral: it keeps the moments that felt bad and drops the ordinary ones.",
     "So the version you are left with a week later is made almost entirely of the two seconds you winced at, and none of the forty minutes that were fine.",
     "This is why arguing with it does not work. You are not reasoning against a memory, you are reasoning against a highlight reel of one kind of moment.",
   ]),
   ("Write it down before you sleep", [
     "Three lines, on your phone, on the way home. Who you spoke to, one thing that went normally, and one thing you would do differently.",
     "The third line is what does the work. It gives the replay somewhere to land, and it turns a vague dread into one specific thing that is usually small.",
   ]),
   ("Check the evidence, once", [
     "Did anyone react at the time? Not in your reading of their face afterwards, but at the moment — did the conversation continue normally?",
     "It almost always did. People are occupied with their own version of this and are not tracking yours.",
   ]),
   ("Do not replay to prepare", [
     "The replay feels like preparation for next time. It is not. It rehearses the feeling rather than the behavior, and the next event arrives with the dread refreshed and nothing practiced.",
     "Practicing out loud is the version that transfers. Going over it silently is the version that does not.",
   ]),
   ("What Haveo does with this", [
     "Haveo's reflection step asks the three questions above, on the night, and keeps the answers. Before the next event you can read what actually happened last time instead of what you remember about it.",
   ]),
 ],
 "faq": [
   ("How long does it usually last?", "For most people the sharpest part is the first night and it fades over a few days. If it is lasting weeks and shaping what you will agree to attend, that is worth raising with a professional — this page is a preparation tool, not treatment."),
   ("Does avoiding the next event help?", "It ends the replay quickly and makes the next invitation harder. That trade is the thing to be aware of when you decline."),
   ("Is it the same as overthinking in general?", "It is more specific: it is tied to a social event, it starts after it, and it focuses on how you came across. The name for it in the research is post-event processing, from Clark and Wells' 1995 cognitive model of social phobia."),
 ],
 "related": ["networking-with-social-anxiety", "neurodivergent-networking", "how-to-follow-up-after-a-networking-event"],
},
{
 "slug": "follow-up-email-after-a-networking-event",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "The follow-up email, with templates you can actually send",
 "title": "Follow-Up Email After a Networking Event — Templates",
 "desc": "Four short templates for the message after you meet someone: the normal one, the one with an ask, the late one, and the one where you barely spoke.",
 "answer": "Send it within two days, keep it under five sentences, and put the specific thing you talked about in the first line. <strong>If the message would still make sense sent to somebody else, it is not a follow-up.</strong> Four templates below, all short on purpose.",
 "sections": [
   ("What every version needs", [
     "Where you met, in four words. The specific thing you talked about. One clear next step, or none at all.",
     "That is it. Length does not read as effort, it reads as a task, and a message that is a task gets postponed.",
   ]),
   ("The normal one", [
     "Subject: <em>Good to meet you at [event]</em>",
     "\"Hi [name] — good to meet you at [event] on Thursday. I've been thinking about what you said about [specific thing]; it hadn't occurred to me that [the point]. If you ever want to carry that on over a coffee I'd enjoy it. Either way, glad we met.\"",
   ]),
   ("The one with an actual ask", [
     "\"Hi [name] — we spoke briefly at [event] about [specific thing]. You mentioned [the thing they offered or knew]. Would you be open to twenty minutes in the next couple of weeks? Happy to work around whatever suits.\"",
     "One ask, sized so the answer can be yes. \"Twenty minutes\" gets replies that \"a chat sometime\" does not.",
   ]),
   ("The late one", [
     "Do not apologize at length, and do not skip it because it has been three weeks. Name it in half a sentence and move on.",
     "\"Hi [name] — we met at [event] last month and I've been meaning to write since. You said [specific thing], which I keep coming back to. If you're open to it I'd like to hear more.\"",
   ]),
   ("The one where you barely spoke", [
     "\"Hi [name] — we only said hello at [event], but I saw you're working on [thing]. I'm [one line about you]. Thought it was worth connecting properly.\"",
     "Honest about how thin the contact was, which is better than pretending to a conversation neither of you had.",
   ]),
   ("What to do if you have no specific thing", [
     "Then you have found the real problem, and it is not the email. The detail has to be captured on the night — a name and one line, typed into your phone as you walk away.",
   ]),
 ],
 "faq": [
   ("How soon?", "Within two days while they can still place you. After about a week you are relying on them remembering the room rather than you."),
   ("Email or LinkedIn?", "Whichever one they actually gave you. If you have both, email — a LinkedIn request sits unread for weeks far more often."),
   ("Do I follow up on the follow-up?", "Once, after about ten days, and then stop. Two unanswered messages is information, not an invitation to send a third."),
 ],
 "related": ["how-to-follow-up-after-a-networking-event", "job-search-networking", "networking-with-dyslexia"],
},
{
 "slug": "how-to-end-a-conversation-politely",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "How to end a conversation without it being awkward",
 "title": "How to End a Conversation Politely",
 "desc": "The exit line is what makes it safe to start a conversation at all. Four that work, why you do not owe an excuse, and what to do when they will not stop talking.",
 "answer": "Say a true thing plus a next step: <strong>\"I'm going to grab a drink — it was good to meet you.\"</strong> You do not owe an excuse, and ending a conversation cleanly is a kindness rather than a rejection. Knowing how you will leave is what makes it safe to start.",
 "sections": [
   ("Four lines that work", [
     "<strong>The errand.</strong> \"I'm going to get a drink — good to meet you.\" True, unarguable, and you can do it immediately.",
     "<strong>The handoff.</strong> \"You should meet Dana, she's doing the same thing.\" The best one, if you have a Dana: you leave and they gain something.",
     "<strong>The honest close.</strong> \"I'm going to go and talk to a few more people, but I'm glad we met.\" Nobody has ever objected to this.",
     "<strong>The next step.</strong> \"I'd like to carry this on — are you on LinkedIn?\" Ends the conversation and keeps the person.",
   ]),
   ("Why you do not need an excuse", [
     "Everyone at the event knows that the point is to talk to more than one person. Leaving a conversation is the expected behavior, not a breach of one.",
     "An elaborate excuse is what makes it awkward, because it implies something needed covering up.",
   ]),
   ("Land it properly", [
     "Say their name, say the good-to-meet-you, and then actually move. Standing there afterwards undoes it and you have to do the whole thing again.",
     "Three seconds of deliberate movement is the difference between a clean ending and a drifting one.",
   ]),
   ("When they will not stop", [
     "Raise it to something unambiguous. \"I'm going to let you go\" while stepping back is a complete sentence and it is understood everywhere.",
     "If it still does not land, you are allowed to be plain: \"I'm going to move on — take care.\" You have not been rude. You have been clear.",
   ]),
   ("Why this is the first thing to prepare", [
     "People who dread these rooms usually do not dread starting a conversation. They dread being stuck in one. An exit line you have said out loud once removes that, and the starting gets easier on its own.",
   ]),
 ],
 "faq": [
   ("What if we were in the middle of something?", "\"I want to hear the rest of that — can I find you later, or are you on LinkedIn?\" You keep the thread and still leave."),
   ("Is it rude to leave a group?", "Less than leaving a pair. A group closes the gap behind you without anyone noticing, which is also why groups are easier to join."),
   ("How long should a conversation last?", "There is no correct length. Ten minutes is a good conversation and ninety seconds is a perfectly normal one."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "networking-for-introverts", "what-to-say-instead-of-what-do-you-do"],
},
]

# ---------------------------------------------- tranche 3: the anxiety hub
PAGES += [
{
 "slug": "the-hour-before-a-networking-event",
 "hub": "networking-with-social-anxiety",
 "h1": "The hour before a networking event",
 "title": "The Hour Before a Networking Event",
 "desc": "What to do in the last hour: what to eat, what to read, what to rehearse, and the two decisions to make before you leave the house.",
 "answer": "Decide two things before you leave: <strong>what time you are going home, and what would make the night worth it.</strong> Then say your opening sentence out loud once. Eat something. Do not re-read the attendee list — at this point it only raises the stakes.",
 "sections": [
   ("Make the two decisions", [
     "<strong>An end time.</strong> A real one, on the clock. Everything gets easier when the evening has a known edge.",
     "<strong>One thing that would make it worth it.</strong> Two real conversations, or one specific person. Something you can finish and then stop.",
   ]),
   ("Say it out loud once", [
     "Your opening sentence, spoken, not read. Thirty seconds. The first time you hear your own voice say it should not be in front of a stranger.",
     "If it sounds wrong out loud, that is the point of doing it now, when there is still time to change it.",
   ]),
   ("Eat something", [
     "Anxiety and an empty stomach produce almost identical physical symptoms, and at an event with a drink in your hand they compound.",
     "It is the least interesting advice on this page and the one most likely to change how the first hour feels.",
   ]),
   ("Stop researching", [
     "Reading the attendee list one more time does not prepare you. It enlarges the room and adds names you now feel you should recognize.",
     "If you were going to look someone up, that was yesterday's job.",
   ]),
   ("Expect the doorway to be the worst part", [
     "For most people the peak is arriving, not talking. Knowing that the hardest ninety seconds are the ones in the entrance, and that they pass, is worth more than another rehearsal.",
   ]),
 ],
 "faq": [
   ("Should I have a drink first?", "One, if you normally drink, is a personal call. Two is the amount people regret, because the thing that makes the first conversation easier also makes the fourth one harder to remember."),
   ("What if I want to cancel?", "Decide to go and to leave at your planned time. Going for forty minutes is a completely different commitment from going for the night, and it is the version that is hard to talk yourself out of."),
   ("Is arriving late better?", "Usually worse. A full room means joining conversations already underway, which is the harder skill. Early is quieter and people are more open."),
 ],
 "related": ["networking-with-social-anxiety", "how-to-go-to-a-networking-event-alone", "how-to-leave-a-networking-event-early"],
},
{
 "slug": "how-to-leave-a-networking-event-early",
 "hub": "networking-with-social-anxiety",
 "h1": "How to leave a networking event early",
 "title": "How to Leave a Networking Event Early",
 "desc": "When it is fine to go, what to say on the way out, and why leaving at a planned time is the thing that makes the next event easier.",
 "answer": "Leave when you have done the thing you came to do, not when the room empties. <strong>You do not need to announce it or say goodbye to everyone</strong> — finish your current conversation properly, thank whoever invited you if they are nearby, and go.",
 "sections": [
   ("You are allowed to go", [
     "Nobody is tracking your arrival and departure. The organizer is counting heads at the start, not the end.",
     "An hour spent in two real conversations is a better night than three hours of standing near the wall, and it is the version you will agree to repeat.",
   ]),
   ("End the last conversation properly", [
     "Do not drift toward the exit mid-sentence. Close it: \"I'm going to head off — it was good to meet you.\" Then leave.",
     "A clean ending is what the other person remembers. A vanishing is what they notice.",
   ]),
   ("Whether to find the host", [
     "If they are nearby and free, thirty seconds is a kindness and they will remember you came. If they are mid-conversation across the room, do not cross it.",
     "A short message the next day covers it completely.",
   ]),
   ("Set the time before you arrive", [
     "This is the whole trick. \"I'll leave at eight\" decided at six is a plan; decided at half past seven it is an escape, and it feels like one afterwards.",
     "Leaving at a planned time having done the thing is a night that worked. That framing is what makes the next invitation answerable.",
   ]),
 ],
 "faq": [
   ("What if someone asks why I'm leaving?", "\"I've got an early start\" is true often enough and nobody follows up. You also do not have to give a reason at all."),
   ("Is it rude to leave before the talks?", "Check the running order when you arrive. If the content is the reason you came, stay for it; if the room is the reason, the talks are the natural moment to go."),
   ("How early is too early?", "If you have had one real conversation, you have got something out of it. Twenty minutes and nobody spoken to is worth pushing through — that is usually the doorway, not the event."),
 ],
 "related": ["networking-with-social-anxiety", "how-to-end-a-conversation-politely", "the-hour-before-a-networking-event"],
},
{
 "slug": "how-to-go-to-a-networking-event-alone",
 "hub": "networking-with-social-anxiety",
 "h1": "How to go to a networking event alone",
 "title": "How to Go to a Networking Event Alone",
 "desc": "Arriving with nobody to stand next to. Where to go first, who to approach, and why going alone is usually easier than going with a friend.",
 "answer": "Go straight to the drinks table, get something to hold, and then approach <strong>someone else standing on their own</strong> — they are the easiest person in the room and they are hoping somebody does. Arriving alone is an advantage: nobody expects you to already have people.",
 "sections": [
   ("Do not stop in the doorway", [
     "The entrance is where the room looks most impossible, because you are seeing every conversation at once and none of them include you.",
     "Walk to a destination. The drinks table, the coat rack, the registration desk. Moving with a purpose buys you two minutes and a thing to hold.",
   ]),
   ("Find the other person standing alone", [
     "There is always one, usually several, and they are strongly motivated to be spoken to. \"Mind if I join you? I don't know anyone here either\" is true and it works.",
     "Approaching one person is much easier than joining a group, and it is the conversation most likely to last.",
   ]),
   ("Going alone beats going with a friend", [
     "A friend is a place to hide. Two people who already know each other read as closed, and you can spend a whole evening talking only to the person you came with.",
     "Alone, you have no option but the thing you came for, and everybody in the room reads you as available.",
   ]),
   ("Arrive early", [
     "A half-empty room has no groups to break into. People who arrive early are usually the ones who also find this hard, and conversations start from proximity rather than nerve.",
   ]),
   ("Have a reason to be standing where you are", [
     "Near the food, by the schedule board, looking at whatever is on the wall. A person examining something is approachable; a person scanning the room is not.",
   ]),
 ],
 "faq": [
   ("What do I do with my hands?", "Hold a drink. It is not a joke — it solves the hands, it gives you a reason to move to the bar, and it makes a pause look normal."),
   ("Is it obvious I don't know anyone?", "No. Everyone is watching their own situation. The people you assume all know each other usually met an hour ago."),
   ("What if nobody talks to me?", "Then you approach, which is the plan anyway. Waiting to be approached is the one strategy that reliably produces an evening of not talking."),
 ],
 "related": ["networking-with-social-anxiety", "what-to-say-when-you-dont-know-anyone", "the-hour-before-a-networking-event"],
},
{
 "slug": "what-to-do-if-you-panic-at-an-event",
 "hub": "networking-with-social-anxiety",
 "h1": "What to do if it becomes too much while you are there",
 "title": "What to Do if It Becomes Too Much at an Event",
 "desc": "Leaving the room, slowing your breathing, and deciding whether to go back in. A plan for the moment rather than advice for next time.",
 "answer": "Leave the room. <strong>A bathroom, a corridor or the street outside — any of them, now, without explaining to anyone.</strong> Then breathe out for longer than you breathe in for about two minutes. Decide whether to go back only after that, not during it.",
 "sections": [
   ("Leave first, think afterwards", [
     "You do not need a reason and nobody will ask. Walking out of a room is the most ordinary thing a person at an event does.",
     "Trying to decide whether it is bad enough to leave, while still standing in it, is what makes it worse.",
   ]),
   ("Make the out-breath longer", [
     "In for four, out for six or eight. The long out-breath is the part that does the work; breathing in deeply on its own can make it sharper.",
     "Two minutes. Set the timer on your phone so you are not also judging whether it has been long enough.",
   ]),
   ("Put your attention on something outside you", [
     "Name five things you can see. It sounds trivial and it interrupts the loop, because the loop runs on inward attention.",
     "Cold water on your wrists does something similar and is available in every bathroom.",
   ]),
   ("Then decide, and either answer is fine", [
     "Going back in for one more conversation is a good outcome. Going home is also a good outcome. The bad outcome is standing in the corridor for an hour deciding.",
     "If you go home, write down what happened tonight before you sleep — it stops the replay becoming the memory.",
   ]),
   ("Afterwards", [
     "This is worth raising with a professional if it happens often, or if it is shaping what you will agree to attend. Haveo is a preparation tool, not treatment, and it does not pretend otherwise.",
   ]),
 ],
 "faq": [
   ("Will people notice I left?", "Almost never, and if they do the reading is that you took a call or went to the bathroom. Nobody assumes the real answer."),
   ("Should I tell someone?", "Only if you want to. If you came with someone you trust, a message saying you are stepping out means they do not look for you."),
   ("Can I stop it happening?", "Not reliably, and aiming to is its own pressure. Planning an end time, a break and an exit line makes the evening smaller, which is what usually helps."),
 ],
 "related": ["networking-with-social-anxiety", "social-anxiety-after-a-networking-event", "sensory-overload-at-events"],
},
{
 "slug": "do-i-actually-have-to-network",
 "hub": "networking-with-social-anxiety",
 "h1": "Do you actually have to network?",
 "title": "Do You Actually Have to Network?",
 "desc": "An honest answer. What networking is really for, when it matters, and the versions that work if rooms full of strangers are not for you.",
 "answer": "No, not in the form you are picturing. <strong>What you cannot skip is being known by a few people who do what you do</strong> — and a room full of strangers is only one way to get there, and not the most reliable one.",
 "sections": [
   ("What it is actually for", [
     "Almost every useful thing that comes through people comes through someone who already knows roughly what you do. Jobs, clients, advice, a name passed on.",
     "The room is a means to that, not the goal. Confusing the two is why \"networking\" feels both compulsory and pointless.",
   ]),
   ("The versions that work without a room", [
     "<strong>One conversation at a time.</strong> A specific person, a specific question, twenty minutes. Far more effective per unit of effort than an evening of small talk.",
     "<strong>Doing visible work.</strong> Writing, building, answering questions in public. It brings people to you, and it is the only version that works while you sleep.",
     "<strong>Staying in touch with people you already know.</strong> The most underrated one. Your existing contacts already like you, which is the hard part solved.",
   ]),
   ("When a room genuinely is the right tool", [
     "When you do not yet know who to talk to. A room is a way to find out who exists in a field, quickly, and that is hard to replicate.",
     "When the industry runs on one annual event and everyone is in the same building. Sometimes that is just true.",
   ]),
   ("If you do go, go smaller", [
     "A workshop or a small meetup where there is a shared activity beats a large mixer, because the thing you are doing supplies the conversation.",
     "Volunteering at an event is the cheat code: you have a role, a reason to talk to people, and something to do with your hands.",
   ]),
 ],
 "faq": [
   ("Is my career damaged if I never do it?", "Not if people who do what you do know your name. The risk is not from skipping events, it is from nobody being able to describe your work."),
   ("What about people who say it's all about who you know?", "They are mostly right and it does not mean what they imply. Knowing people happens through repeated small contact, not through one night in a hotel function room."),
   ("Why does Haveo exist then?", "Because sometimes you have to go, and the preparation is the part that makes it survivable. It is a tool for the events you have decided to attend, not an argument that you should attend more of them."),
 ],
 "related": ["networking-with-social-anxiety", "job-search-networking", "networking-for-introverts"],
},
]

# ------------------------------------------ tranche 4: the what-to-say hub
PAGES += [
{
 "slug": "how-to-join-a-group-already-talking",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "How to join a group that is already talking",
 "title": "How to Join a Group That Is Already Talking",
 "desc": "Which groups to approach, where to stand, what to say, and why a group of four is easier to join than two people.",
 "answer": "Approach a group of <strong>three or more, never a pair</strong>. Stand at the edge of the circle, wait for a pause rather than a gap in one sentence, and say \"mind if I join you?\" Most groups widen without breaking stride.",
 "sections": [
   ("Pick the right group", [
     "Three or more. A pair is usually mid-conversation and there is no physical space in the shape they are standing in.",
     "Look for a circle with a gap in it. People leave that gap without noticing, and it is an invitation whether or not anyone means it as one.",
   ]),
   ("Stand there first", [
     "Move to the edge and face in. Do not say anything for a few seconds. This is normal and nobody finds it strange.",
     "You will usually be absorbed without having to ask, because somebody will glance over and widen the circle.",
   ]),
   ("If you do need words", [
     "\"Mind if I join you?\" is enough. So is \"sorry, I heard you say [thing] — what happened in the end?\"",
     "The second one is better when you have actually heard something, because it gives them a reason to include you rather than just permission.",
   ]),
   ("Then listen for a minute", [
     "Do not open with your own subject. Take the thread that is running and add to it.",
     "The fastest way to be unwelcome in a group is to arrive and change the topic to yourself.",
   ]),
   ("If it does not work", [
     "Occasionally a group is genuinely closed — two people solving something, or a conversation that was private. Say \"sorry, carry on\" and move. It is not about you and it costs nothing.",
   ]),
 ],
 "faq": [
   ("Is it rude to interrupt?", "Joining is not interrupting. Waiting for the end of a sentence rather than the end of a story is the whole difference."),
   ("What if they stop talking when I arrive?", "They are making room, not shutting you out. Say who you are, or ask them to carry on — both restart it immediately."),
   ("Is a group better than one person?", "One person is easier to start with and a group is easier to stay in. Early in a night, go for the person on their own."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "how-to-end-a-conversation-politely", "how-to-go-to-a-networking-event-alone"],
},
{
 "slug": "what-to-say-when-your-mind-goes-blank",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "What to say when your mind goes blank",
 "title": "What to Say When Your Mind Goes Blank",
 "desc": "The three sentences that restart a conversation when you have lost it, and why describing the room works every time.",
 "answer": "Say the true thing: <strong>\"sorry, I have completely lost my train of thought.\"</strong> It is a normal sentence and the other person almost always supplies the thread. If you want something easier, describe the room — the queue, the coffee, how loud it is.",
 "sections": [
   ("Name it, do not cover it", [
     "Talking on while searching for the point is what reads badly. Stopping and saying so does not.",
     "Nine times out of ten they will say \"you were saying about the...\" and you are back.",
   ]),
   ("Describe the room", [
     "\"That coffee queue has not moved in ten minutes.\" \"It is much busier than last year.\" \"I cannot hear a thing in here.\"",
     "Shared circumstance is the cheapest conversational fuel there is, and nobody has ever been judged for mentioning it.",
   ]),
   ("Hand the talking over", [
     "\"What about you — what brought you here?\" You do not have to introduce a new subject. Ask them to expand on the last one.",
     "\"How did that go?\" and \"what made you pick that?\" work on almost anything somebody has just said.",
   ]),
   ("Why it happens", [
     "Working memory is the first thing a loud room and adrenaline take. It is not a sign you are bad at this, and it happens to people who look completely comfortable.",
     "It is also why two prepared questions in your pocket are worth more than any amount of confidence.",
   ]),
 ],
 "faq": [
   ("What if it keeps happening all night?", "That is usually noise and tiredness rather than nerves. Step outside for five minutes — it resets more than pushing through does."),
   ("Should I apologize?", "Once, in half a sentence. A long apology makes a two-second pause into the subject of the conversation."),
   ("Is it worse if I am not a native English speaker?", "Searching for a word is a different problem from losing the thread, and the same sentence covers both. \"Sorry, I have lost the word\" is completely ordinary and people are glad to help."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "networking-with-adhd", "small-talk-questions-that-arent-boring"],
},
{
 "slug": "when-you-forget-someones-name",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "When you forget someone's name",
 "title": "When You Forget Someone's Name",
 "desc": "How to ask again without it being awkward, how to get out of it when you cannot ask, and how to stop losing names in the first place.",
 "answer": "Ask. <strong>\"I'm so sorry — your name has gone completely.\"</strong> It costs two seconds and everyone has been on both sides of it. The version that actually goes wrong is a whole conversation spent avoiding their name while they notice.",
 "sections": [
   ("Just ask", [
     "Say it early rather than late. Asking in the first minute is nothing; asking after twenty is a small event.",
     "\"Remind me of your name?\" and \"I've completely lost your name, sorry\" both work and neither needs a reason attached.",
   ]),
   ("When you cannot ask", [
     "Introduce someone else to them. \"Have you met Dana?\" usually makes them say their own name without prompting.",
     "Or ask how they spell it — this only works for names that plausibly have two spellings, and it fails loudly on a Tom.",
   ]),
   ("Stop losing them in the first place", [
     "Use it once, immediately: \"good to meet you, Priya.\" Saying it aloud is far stronger than hearing it.",
     "Then type it into your phone within the minute, with one detail. Repeating it silently in your head does not survive the next introduction.",
   ]),
   ("Why it is not a character flaw", [
     "A name is arbitrary information attached to a face under stress, in noise, with no context. It is the single hardest thing the room asks you to do.",
     "People who appear to be good at it are almost always people with a system, not people with a better memory.",
   ]),
 ],
 "faq": [
   ("What if I've met them several times?", "Own it plainly: \"this is embarrassing, we've met twice and your name has gone.\" Honesty ends it; a third conversation of avoidance does not."),
   ("Are badges not enough?", "Only if you can read one at conversational distance, which many people cannot. Asking is faster than staring."),
   ("What if they forget mine?", "Say it again unprompted. \"Sam, by the way\" mid-conversation is a kindness and it lets them off entirely."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "networking-with-adhd", "how-to-remember-who-you-met"],
},
{
 "slug": "how-to-introduce-yourself-at-a-networking-event",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "How to introduce yourself at a networking event",
 "title": "How to Introduce Yourself at a Networking Event",
 "desc": "A sentence that works whether you are employed, freelancing, studying or between things — and what to do with the pause afterwards.",
 "answer": "Name, what you do in plain words, and one thing you are into right now. <strong>\"I'm Sam — I build booking systems for clinics, and lately I'm mostly untangling other people's old code.\"</strong> The third part is what gives them something to ask about.",
 "sections": [
   ("The three parts", [
     "<strong>Your name.</strong> First name is enough and it is the part people actually need.",
     "<strong>What you do, said like a person.</strong> Not the job title on your contract. What you would tell a friend you spent the week on.",
     "<strong>What you are into right now.</strong> A current project, a problem, something you are learning. This is the hook and most people leave it out.",
   ]),
   ("Why the title alone fails", [
     "\"I'm a senior product manager\" gives the other person nothing to do except say \"oh, nice.\" Then you are both stuck.",
     "The specific thing is what lets someone say \"wait, how does that work?\" — which is the conversation actually starting.",
   ]),
   ("If your situation is complicated", [
     "Between jobs: \"my role was cut in the restructure, so I'm looking — I do X.\" Plain, extremely common, and it tells people how to help.",
     "Studying: \"I'm finishing a degree in X and trying to work out what to aim at.\" This gets more help than any confident version would.",
     "Freelancing or several things: pick the one relevant to this room. You are not misrepresenting yourself, you are answering the question asked.",
   ]),
   ("Rehearse it out loud, once", [
     "Not read, said. Twenty seconds. A sentence you have heard yourself say is a completely different object under pressure from one you have only thought.",
   ]),
   ("Then stop talking", [
     "Say your sentence and let the pause exist. Filling it with more about yourself is the most common way a good introduction turns into a monologue.",
   ]),
 ],
 "faq": [
   ("How long should it be?", "Under fifteen seconds. If it needs a second breath it is a pitch, and a pitch is for when somebody asks a second question."),
   ("Do I need a different one for each event?", "The last part changes with the room; the first two do not. That is why keeping them separate is worth doing."),
   ("What if my work is hard to explain?", "Say what it is for rather than what it is. \"I make sure the payment doesn't break\" beats any accurate description of the systems."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "what-to-say-instead-of-what-do-you-do", "job-search-networking"],
},
{
 "slug": "small-talk-questions-that-arent-boring",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "Small talk questions that are not boring",
 "title": "Small Talk Questions That Are Not Boring",
 "desc": "Twelve questions that get a real answer instead of one word, why the weather question fails, and how to follow up on what you get.",
 "answer": "Ask about the present and the specific. <strong>\"What are you working on at the moment?\" beats \"what do you do?\"</strong> because it has an answer the person actually finds interesting. A good question is one they have not answered nine times tonight.",
 "sections": [
   ("Twelve that work", [
     "What are you working on at the moment?",
     "How did you end up here?",
     "What is the best thing you have seen today?",
     "Is this your first one of these?",
     "What is taking up most of your time right now?",
     "What made you want to come?",
     "What would make tonight worth it for you?",
     "What are you hoping to figure out this year?",
     "What is something you changed your mind about recently?",
     "What part of your job would surprise people?",
     "Who else should I be talking to here?",
     "What are you reading or watching that is any good?",
   ]),
   ("Why the standard ones fail", [
     "\"What do you do?\" asks for a label, and it lands badly on anyone between jobs or doing something hard to say in three words.",
     "The weather is not a bad opener, it is a bad second question. It has no follow-up, so the conversation has to be restarted immediately.",
   ]),
   ("The follow-up matters more than the question", [
     "Whatever they answer, go one level deeper rather than moving on: how did that go, what made you pick that, what was the hard part.",
     "Most conversations die because both people keep introducing new topics instead of finishing one.",
   ]),
   ("Two is enough to prepare", [
     "You do not need twelve in your head. Pick two you would actually say out loud and they will carry an entire evening.",
   ]),
 ],
 "faq": [
   ("Are these too personal for a work event?", "None of them asks anything private. They ask about work and interests, just in the present tense, which is what makes them answerable."),
   ("What if they give a one-word answer?", "Take it at face value and follow up once. If the second one is also short, they may not want to talk — move on, it is not a verdict on you."),
   ("Is it strange to ask who else I should talk to?", "It is one of the best questions in the room. People like being the person who made an introduction, and you often get walked over to someone."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "what-to-say-instead-of-what-do-you-do", "what-to-say-when-your-mind-goes-blank"],
},
{
 "slug": "how-to-introduce-two-people",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "How to introduce two people to each other",
 "title": "How to Introduce Two People to Each Other",
 "desc": "The two-line introduction that leaves them with something to talk about, and why doing it is the fastest way to be useful in a room.",
 "answer": "Names, then <strong>one reason they should care about each other</strong>. \"Dana, this is Sam — he builds booking systems, and you were just saying yours is held together with tape.\" Without that second half you have made two strangers stand next to each other.",
 "sections": [
   ("The shape", [
     "Name, name, and a hook for each. Ten seconds.",
     "The hook is the whole job. \"This is Sam\" hands them the work of finding a subject while you watch.",
   ]),
   ("Aim the hook at the other person", [
     "Pick the thing about Sam that matters to Dana specifically, not the most impressive thing about Sam.",
     "If you know something they share — a city, a former employer, the same problem — lead with that.",
   ]),
   ("Then get out of the way", [
     "Let the next question be theirs. Standing there steering it keeps it a three-way conversation that neither of them owns.",
     "If you want to leave, this is also the cleanest exit you will get all night: you have handed each of them somebody.",
   ]),
   ("Why it is worth doing", [
     "It is the fastest route to being the useful person in a room, and it requires no confidence at all — you are talking about other people.",
     "It is also the single best way to end a conversation you want to leave without anyone feeling dropped.",
   ]),
 ],
 "faq": [
   ("What if I have forgotten one of their names?", "Introduce the one you know and pause. \"Dana, have you met...?\" and the other person nearly always fills it in."),
   ("What if I get the hook wrong?", "They will correct it and that is a conversation too. A slightly wrong hook still works better than none."),
   ("Should I introduce people if I barely know them?", "Yes. \"You two should talk — you are both doing X\" is enough, and neither expects you to be an authority on them."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "how-to-end-a-conversation-politely", "how-to-join-a-group-already-talking"],
},
]

# ------------------------------------------- tranche 5: the follow-up hub
PAGES += [
{
 "slug": "linkedin-message-after-meeting-someone",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "The LinkedIn message after you meet someone",
 "title": "LinkedIn Message After Meeting Someone",
 "desc": "What to write in the connection note, why the default blank request wastes the meeting, and three short versions to copy.",
 "answer": "Always add a note, and put where you met in the first six words. <strong>\"We met at the Leeds meetup on Thursday — you were talking about the warehouse migration.\"</strong> A blank request makes them work out who you are, and most people will not bother.",
 "sections": [
   ("Send it the same night", [
     "This is the one message that is better sent immediately. They are still on their phone and they still remember the room.",
     "Waiting until the morning is fine. Waiting a week means you are relying on them recognizing a name with no context.",
   ]),
   ("Three versions", [
     "<strong>Normal.</strong> \"Good to meet you at [event] tonight — enjoyed the bit about [thing]. Sending a connection so I can follow what you are working on.\"",
     "<strong>You barely spoke.</strong> \"We only said hello at [event], but I saw you are working on [thing] — worth connecting properly.\"",
     "<strong>You want something.</strong> Connect first with a plain note, then ask in a separate message a few days later. Doing both at once is what makes people decline.",
   ]),
   ("Do not pitch in the connection note", [
     "The note is for being recognized, not for selling. A request that arrives as a pitch gets declined, and a decline is much harder to recover from than silence.",
     "The ask works far better once they have accepted and you have been visible for a week.",
   ]),
   ("Email beats LinkedIn when you have both", [
     "If they gave you a card or an address, use it. LinkedIn requests sit unread for weeks more often than email does, and there is no way to tell from your side.",
   ]),
 ],
 "faq": [
   ("Is a connection request enough on its own?", "It keeps the contact. It does not start anything. If you actually want to talk, the message is the thing that does it, not the connection."),
   ("What if they do not accept?", "Plenty of people check LinkedIn twice a year. It is not a signal, and it is not worth a second attempt."),
   ("Should I follow rather than connect?", "If they have a large following and post a lot, following is lower friction and you can still message later. For someone you actually met, connect."),
 ],
 "related": ["how-to-follow-up-after-a-networking-event", "follow-up-email-after-a-networking-event", "linkedin-networking-message-examples"],
},
{
 "slug": "follow-up-email-subject-lines",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "Subject lines for a follow-up email",
 "title": "Follow-Up Email Subject Lines",
 "desc": "Ten subject lines that get opened, why the clever ones do worse, and the one word that does most of the work.",
 "answer": "Put the event in the subject line. <strong>\"Good to meet you at the Leeds meetup\"</strong> beats anything clever, because the only job of the subject is to stop them deleting an email from a name they half recognize.",
 "sections": [
   ("Ten you can use", [
     "Good to meet you at [event]",
     "Following up from [event]",
     "[Event] — the thing about [topic]",
     "From [event] on Thursday",
     "Nice to meet you — [your name] from [event]",
     "You mentioned [thing] at [event]",
     "Quick follow-up from [event]",
     "[Your name], we spoke at [event]",
     "About [specific thing] from Thursday",
     "Hello from the [event] coffee queue",
   ]),
   ("Why clever ones do worse", [
     "A subject line that hides what the email is makes the reader decide whether to spend attention on a mystery from an unfamiliar name.",
     "Recognition is the whole job here. You are not competing for attention in a crowded inbox, you are answering \"do I know this person?\"",
   ]),
   ("Put your name in it if the address is unfamiliar", [
     "A personal email address with no name attached reads as a stranger. \"[Your name], we spoke at [event]\" solves it in the subject.",
   ]),
   ("Keep it under about eight words", [
     "Phones cut the rest, and the cut usually lands mid-phrase. The event name should survive the truncation, so put it early.",
   ]),
 ],
 "faq": [
   ("Should I use their name in the subject?", "It is unnecessary and it reads slightly like automated mail. Their name goes in the first line of the body."),
   ("Does 'quick' help?", "Mildly, and only if the email really is quick. Promising short and then sending six paragraphs is worse than not promising."),
   ("What about replying to an existing thread?", "Always better if one exists. A reply carries the whole context and skips the recognition problem entirely."),
 ],
 "related": ["follow-up-email-after-a-networking-event", "how-to-follow-up-after-a-networking-event", "following-up-late"],
},
{
 "slug": "what-to-do-with-the-business-cards",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "What to do with the business cards",
 "title": "What to Do With the Business Cards",
 "desc": "The pile in your bag is not a contact list. What to do in the taxi home, what to do the next morning, and what to throw away.",
 "answer": "Before you sleep, photograph each card and write one line under it: <strong>where you met and one thing they said.</strong> A card on its own is a name and a job title, which is not enough to write a follow-up from — and that is why the pile never gets used.",
 "sections": [
   ("The card is not the contact", [
     "Everyone keeps the cards and almost nobody writes the follow-up, and the reason is the same: by Tuesday the card means nothing.",
     "The detail is the asset. The card is just where to send it.",
   ]),
   ("Do it the same night", [
     "In the taxi, on the train, standing outside. Photograph the card, add a line: \"Leeds meetup, runs ops at the bakery, looking for a supplier.\"",
     "Ten seconds each. It is the difference between eight contacts and eight pieces of card.",
   ]),
   ("Write on the card itself as you go", [
     "If you are the kind of person who will actually do it, one word on the back in the moment beats any system. It is also completely normal behavior at an event.",
     "If writing on cards in front of people feels wrong, step away and use your phone.",
   ]),
   ("Then act on them within two days", [
     "Sort into two piles: worth a message, and not. Send the messages. Put the rest in your contacts and let them go.",
     "A card you will not act on is not a contact, it is a reason to feel guilty in a month.",
   ]),
   ("If you have no cards of your own", [
     "It matters much less than it used to. Ask for theirs and follow up first — that puts you in control of whether anything happens, which is the better half of the exchange anyway.",
   ]),
 ],
 "faq": [
   ("Is a scanning app worth it?", "Only if it captures your note too. An app that files a perfectly transcribed name and title has solved the part that was never the problem."),
   ("Should I throw the cards away?", "Once the detail and the address are somewhere you will look, yes. A drawer of cards is a pile of decisions you keep not making."),
   ("What if I did not get a card?", "Look them up that night while you still remember the name and the company. Searching two days later almost never works."),
 ],
 "related": ["how-to-follow-up-after-a-networking-event", "how-to-remember-who-you-met", "networking-with-dyslexia"],
},
{
 "slug": "following-up-late",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "Following up when it has been too long",
 "title": "Following Up When It Has Been Too Long",
 "desc": "Three weeks, three months, or a year later. What to write, how much to apologize, and when it genuinely is too late.",
 "answer": "Send it anyway. <strong>Name the gap in half a sentence and move on</strong> — \"we met at [event] back in March and I have been meaning to write since.\" The long apology is what makes it awkward. The delay itself is almost never the problem.",
 "sections": [
   ("Half a sentence, then the point", [
     "\"I have been meaning to write since\" covers it completely. Three lines about how busy you have been makes your delay the subject of their email.",
     "Then go straight to the specific thing you remember. That is what proves the meeting was real.",
   ]),
   ("You still need the detail", [
     "If you can recall what they said, the gap does not matter much. If you cannot, the message reads as a contact-list sweep, and that is the thing people ignore.",
     "Check their LinkedIn before you write. Something they have posted since is a legitimate reason to make contact now rather than then.",
   ]),
   ("Use the delay as the reason", [
     "\"I saw you had launched [thing] and it reminded me we met at [event]\" is a better message than a punctual one with nothing in it.",
     "A late message with a reason beats a fast message without one.",
   ]),
   ("When it is genuinely too late", [
     "Almost never for a connection. Frequently for a specific opportunity — a role, a project, a deadline they mentioned.",
     "If that was the point, say so plainly and ask whether the door is still open. The worst outcome is a no, which is where you already are.",
   ]),
 ],
 "faq": [
   ("A year later — still worth it?", "Yes, if you have a reason now. \"We met at X, I have been following what you are doing, and I wanted to ask about Y\" is a completely normal message."),
   ("Should I pretend it has not been that long?", "No. They can see the date of the event and the gap is obvious. Naming it takes it off the table."),
   ("What if I promised to send something and never did?", "Send it now with one line: \"far later than I said — here it is.\" People remember the thing arriving much more than when it was due."),
 ],
 "related": ["how-to-follow-up-after-a-networking-event", "follow-up-email-after-a-networking-event", "how-to-remember-who-you-met"],
},
{
 "slug": "how-to-remember-who-you-met",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "How to remember who you met",
 "title": "How to Remember Who You Met",
 "desc": "Why names disappear within minutes, the ten-second note that fixes it, and what to write down that is actually useful later.",
 "answer": "Do not try to remember. <strong>Type a name and one detail into your phone the moment you walk away</strong> — nobody minds, and everybody assumes you are answering a message. Memory is not the tool for arbitrary names in a loud room under stress.",
 "sections": [
   ("Why it fails", [
     "A name is arbitrary information, attached to a face, in noise, while you are also producing speech. It is the hardest thing the room asks of you.",
     "People who seem good at it almost always have a system. Very few of them have a better memory.",
   ]),
   ("The ten-second note", [
     "Name. Where. One thing they said that is not on their LinkedIn.",
     "\"Priya — Leeds meetup — runs ops at the bakery place, needs a supplier in Yorkshire.\" That is a follow-up you can write a week later.",
   ]),
   ("Write the detail, not the title", [
     "Their job title will be on their profile. What they were worried about, pleased about or trying to solve will not, and it is the only part that makes a message feel like it was written to them.",
   ]),
   ("Do it as you walk away, not at the end", [
     "The end of the night is when you are most tired and the names have already blurred into each other.",
     "Stepping aside to use your phone mid-event is invisible. Everyone does it, for less good reasons.",
   ]),
   ("What Haveo does with this", [
     "Haveo keeps the people you met with the event they belong to, so the note, the name and the reminder to follow up are in the same place rather than in three.",
   ]),
 ],
 "faq": [
   ("Is it rude to use my phone at an event?", "Not for ten seconds after a conversation has ended. It looks exactly like checking a message, which is what everyone assumes."),
   ("What about memory tricks with names?", "Repeating the name aloud once, in the conversation, genuinely helps. The visual association tricks take more attention than a room like this leaves you."),
   ("How many people should I expect to remember?", "Without notes, two or three. With notes, all of them. That gap is the entire argument."),
 ],
 "related": ["how-to-follow-up-after-a-networking-event", "when-you-forget-someones-name", "networking-with-adhd"],
},
{
 "slug": "what-to-say-in-a-coffee-chat",
 "hub": "how-to-follow-up-after-a-networking-event",
 "h1": "What to say in a coffee chat",
 "title": "What to Say in a Coffee Chat",
 "desc": "You asked for twenty minutes and got it. How to open, what to ask, what not to ask, and how to end it without an awkward pause.",
 "answer": "You asked for it, so <strong>you run it</strong>. Open by saying what you are hoping to get out of it, ask three prepared questions, watch the clock yourself, and end on time even if it is going well. Ending early is what gets you a second one.",
 "sections": [
   ("Open by naming the purpose", [
     "\"Thanks for the time — I'm trying to work out whether to move into X, and you have done it, so mostly I want to hear how it actually went.\"",
     "Thirty seconds. It stops them guessing what you want, which is the thing that makes these conversations drift.",
   ]),
   ("Bring three questions, not ten", [
     "\"What does the work actually look like day to day?\" \"What did you not know before you made the move?\" \"What would make someone with my background a credible candidate?\"",
     "Three real questions fill twenty minutes easily, because good answers generate their own follow-ups.",
   ]),
   ("Do not ask them for a job", [
     "It converts a generous twenty minutes into an obligation, and it is the reason many people stop agreeing to these.",
     "If you want them to think of you, the line at the end is: \"if anything crosses your desk I'd appreciate a heads up.\" Once, no pressure.",
   ]),
   ("End it yourself, on time", [
     "At minute eighteen: \"I said twenty minutes and I want to respect that — this was really useful.\" Then stop.",
     "Nothing makes a second conversation more likely than visibly protecting their time in the first one.",
   ]),
   ("Send the thank-you the same day", [
     "Three lines. One specific thing you are going to do because of what they said. That last part is what makes them glad they did it.",
   ]),
 ],
 "faq": [
   ("Who pays?", "You asked, so you offer. Most people will wave it away, and the offer still registers."),
   ("Video or in person?", "Whatever is easier for them — say so explicitly when you ask. Making it easy is most of why people say yes."),
   ("What if I run out of questions?", "Ask who else they would talk to in your position. It is the most useful question in the conversation and it is a natural ending."),
 ],
 "related": ["job-search-networking", "informational-interview-questions", "how-to-follow-up-after-a-networking-event"],
},
]

# ------------------- tranche 6: neurodivergent hub + the introvert hub
PAGES += [
{
 "slug": "autistic-networking-events",
 "hub": "neurodivergent-networking",
 "h1": "Autistic people at networking events",
 "title": "Autistic People at Networking Events",
 "desc": "The unwritten rules nobody states, what to do about small talk you find pointless, and which parts are worth complying with.",
 "answer": "The rules are real, mostly unstated, and largely arbitrary. <strong>Learn the three that carry weight — open with something light, leave conversations cleanly, follow up in writing — and ignore the rest.</strong> You do not have to enjoy small talk to use it as a doorway.",
 "sections": [
   ("What small talk is actually for", [
     "It is not an exchange of information, which is why it reads as pointless. It is a low-stakes way for two people to check whether a longer conversation is wanted.",
     "Once you treat it as a door rather than a conversation, ninety seconds of weather is easy to produce and easy to stop resenting.",
   ]),
   ("The three rules worth following", [
     "<strong>Open light.</strong> The first thirty seconds are not the place for your actual subject. Get through them and the real conversation is allowed.",
     "<strong>Close cleanly.</strong> \"I'm going to get a drink — good to meet you\" ends it without anyone feeling dropped.",
     "<strong>Follow up in writing.</strong> This is where you have the advantage. A specific, well-written message a day later beats any amount of charm in the room.",
   ]),
   ("Depth is not a flaw here", [
     "Going deep on one subject with one person is a better networking outcome than circulating. Two people who had a real conversation remember each other; twenty introductions do not.",
     "If you notice the other person disengaging, ask a question. That is the repair, and it works.",
   ]),
   ("Plan the exits, and the quiet", [
     "Know where you can go: outside, a corridor, the far end of the room. Decide before you need it, because deciding while you need it is much harder.",
     "Set an end time. An evening with a known edge is a different thing from an open-ended one.",
   ]),
   ("Eye contact and the rest", [
     "Nobody is scoring it. Looking at someone's eyebrows or mouth reads as identical from across a table, and it costs you far less.",
     "Do not spend the conversation monitoring your own face. That is the thing that actually makes it hard to follow what they are saying.",
   ]),
 ],
 "faq": [
   ("Should I disclose?", "You never owe it. If you want a specific accommodation you can ask for the thing without the label — \"could we move somewhere quieter\" needs no explanation."),
   ("What if I talk too long about one thing?", "Ask a question roughly every third turn. It is mechanical rather than a personality change, which is exactly why it works under pressure."),
   ("Are these events even worth it for me?", "Sometimes not, and that is a legitimate answer. One prepared conversation with a specific person is usually higher value than any mixer."),
 ],
 "related": ["neurodivergent-networking", "sensory-overload-at-events", "masking-at-work-events"],
},
{
 "slug": "sensory-overload-at-events",
 "hub": "neurodivergent-networking",
 "h1": "Sensory overload at a networking event",
 "title": "Sensory Overload at a Networking Event",
 "desc": "Loud rooms, hard lighting and no quiet corner. What to check before you go, what to carry, and what to do when it has already happened.",
 "answer": "Find the quiet place before you need it, not during. <strong>Walk the venue in the first five minutes and locate one exit you can use without explaining yourself.</strong> Loop earplugs take the edge off the noise without taking the conversation with it.",
 "sections": [
   ("Do the reconnaissance first", [
     "In the first five minutes, find the corridor, the stairwell or the bit of street outside. Knowing it exists changes the whole evening even if you never use it.",
     "Also note where it is quietest inside. Most rooms have one, usually away from the bar and the speakers.",
   ]),
   ("What actually helps in the room", [
     "<strong>Filtered earplugs.</strong> They cut the volume, not the speech. Most people cannot tell you are wearing them.",
     "<strong>Stand at the edge.</strong> The middle of a room is the loudest point and the one with most movement in your vision.",
     "<strong>Face away from the speakers and the door.</strong> Less to track.",
   ]),
   ("Break before you need one", [
     "Five minutes outside at a decided point in the evening is worth far more than twenty minutes after it has already tipped.",
     "Put it in your plan at the start, like the end time. A break you have to justify to yourself is one you will not take.",
   ]),
   ("If it has already tipped", [
     "Leave the room now, without explaining. Then make your out-breath longer than your in-breath for two minutes.",
     "Decide whether to go back only once you are outside. Deciding while still in the noise is deciding with the thing that caused it.",
   ]),
   ("Choosing events at all", [
     "Workshops, small meetups and anything with a shared activity are far easier than a mixer in a bar. The activity carries the conversation and the room is usually quieter.",
     "Volunteering at an event gives you a role, a reason to move, and permission to be in the quiet parts of the venue.",
   ]),
 ],
 "faq": [
   ("Do earplugs look odd?", "The filtered kind are nearly invisible and increasingly common. Far less conspicuous than leaving after twenty minutes."),
   ("Should I tell the organizer?", "If you want something specific — a quieter room, a seat away from the speakers — ask. Organizers are usually glad to help and rarely asked."),
   ("What if the recovery takes days?", "That is real and it is worth planning around: do not book anything demanding the next day. If it is consistently costing days, that is worth raising with a professional."),
 ],
 "related": ["neurodivergent-networking", "what-to-do-if-you-panic-at-an-event", "networking-when-youre-already-drained"],
},
{
 "slug": "masking-at-work-events",
 "hub": "neurodivergent-networking",
 "h1": "Masking at work events",
 "title": "Masking at Work Events",
 "desc": "Why an evening of performing costs more than the evening itself, how to spend less of it, and what to do about the day after.",
 "answer": "Masking is why a two-hour event costs a whole day. <strong>You cannot switch it off on command, but you can shorten the evening and drop the parts nobody is checking</strong> — eye contact, matching energy, the face you hold between sentences.",
 "sections": [
   ("Where the cost actually comes from", [
     "Not the conversations. The continuous background monitoring — your expression, your volume, whether that was the right amount of enthusiasm.",
     "That is why you can leave an event having spoken to three people and be unable to do anything else that night.",
   ]),
   ("Drop what nobody is scoring", [
     "Eye contact is the big one. Looking near someone's eyes is indistinguishable from across a table and costs a fraction as much.",
     "The neutral face you hold between sentences is doing nothing for anyone. Nobody is reading it.",
     "Matching someone's energy is optional. Calm and interested is a perfectly normal way to be at a work event.",
   ]),
   ("Shorten the evening instead of improving the performance", [
     "Ninety minutes masked is a different object from four hours masked. Deciding the end time in advance is the single biggest lever here.",
     "Two real conversations and out beats a full evening of holding it together for people whose names you will not keep.",
   ]),
   ("Plan the day after", [
     "If the event is Thursday night, do not schedule anything demanding Friday morning. This is not indulgence, it is the actual cost of the thing you just did.",
     "Treating the recovery as part of the event is what makes it sustainable rather than something you dread and cancel.",
   ]),
   ("Preparation reduces masking directly", [
     "Most of the effort goes into improvising — producing a sentence about yourself, finding the next question, judging when to leave.",
     "Written and rehearsed, those three stop being live performance. That is the mechanism, and it is why preparation helps here more than confidence advice ever does.",
   ]),
 ],
 "faq": [
   ("Should I unmask at work events?", "That is a much larger decision than one evening and it depends on your workplace. Nothing on this page requires it — shortening and preparing both work either way."),
   ("Is it dishonest?", "No. Everyone adjusts how they present at a work event. The difference is how much it costs you, not whether you are doing something other people are not."),
   ("Why am I exhausted when it went well?", "Because going well is the expensive version. A conversation that flowed usually means more monitoring, not less."),
 ],
 "related": ["neurodivergent-networking", "networking-when-youre-already-drained", "rejection-sensitivity-after-networking"],
},
{
 "slug": "rejection-sensitivity-after-networking",
 "hub": "neurodivergent-networking",
 "h1": "When a small moment stings for days",
 "title": "When a Small Moment From an Event Stings for Days",
 "desc": "The conversation that ended flatly, the message with no reply, and why the reaction is out of proportion to the event.",
 "answer": "A conversation ending flatly or a message going unanswered feels like a verdict, and it almost never is one. <strong>Write down what actually happened on the night</strong> — the recording in your head is weighted entirely toward the two seconds that stung.",
 "sections": [
   ("The reaction is real even when the cause is not", [
     "The feeling is not proportionate to the event, and being told that does not shrink it. What helps is having something to check it against.",
     "So the job is not talking yourself out of it. The job is making sure the version you remember in a week is not built only from the worst two seconds.",
   ]),
   ("Write the three lines", [
     "Who you spoke to. One thing that went normally. One thing you would do differently.",
     "That third line gives the feeling somewhere specific to land, and it is usually much smaller than the general dread it was becoming.",
   ]),
   ("Unanswered is not rejected", [
     "Most messages go unanswered because of an inbox, not a judgment. People miss things, intend to reply, and then it is three weeks later and they feel awkward.",
     "One follow-up after about ten days, then stop. Two unanswered messages is information about their inbox, not about you.",
   ]),
   ("A flat conversation is usually not about you", [
     "People are tired, looking for someone specific, or halfway through their own difficult evening. You are seeing three minutes of a night you know nothing else about.",
     "The evidence to check is what happened at the time, not how you read their face afterwards.",
   ]),
   ("When to get actual help", [
     "If this is shaping what you will agree to attend, or lasting days every time, that is worth taking to a professional. This is a preparation tool and it does not pretend to be more.",
   ]),
 ],
 "faq": [
   ("Is this the same as overthinking?", "It is more specific — tied to a social event, starting afterwards, focused on how you came across. The research name for that pattern is post-event processing, from Clark and Wells' 1995 cognitive model of social phobia."),
   ("Does going to more events fix it?", "Not on its own. Repetition helps the specific skills; it does not do much for the aftermath. Writing the night down does more."),
   ("Should I ask the person if it was okay?", "Usually no. It puts them in an odd position and the reassurance does not last. Your own written record on the night is more durable."),
 ],
 "related": ["neurodivergent-networking", "social-anxiety-after-a-networking-event", "masking-at-work-events"],
},
{
 "slug": "how-many-people-should-i-talk-to",
 "hub": "networking-for-introverts",
 "h1": "How many people should you talk to?",
 "title": "How Many People Should You Talk To at a Networking Event?",
 "desc": "Two or three. Why counting introductions is the wrong measure, and what to aim at instead.",
 "answer": "Two or three real conversations is a good night. <strong>Counting introductions measures the wrong thing</strong> — one person who remembers a real conversation with you is worth more than twenty who half-recall your name, and the twenty is the harder evening.",
 "sections": [
   ("Why more is not better", [
     "The value of an event is the people who would recognize your name next month. That number is almost never improved by circulating faster.",
     "Twenty introductions produces twenty people who cannot say what you do. That is not a network, it is an evening.",
   ]),
   ("What a real conversation looks like", [
     "Long enough that you both said something specific about your actual work. Usually five to fifteen minutes.",
     "You should be able to write one line about them afterwards that is not on their LinkedIn. That is the test.",
   ]),
   ("Set the number before you go", [
     "\"Two real conversations and I can leave\" is a goal you can finish. Finishing it is what lets you stop, and stopping is what makes it repeatable.",
     "An open-ended evening has no success condition, so it always ends in the feeling that you should have done more.",
   ]),
   ("If you get one", [
     "One good conversation is still a good night. The events people remember as worthwhile almost always turn out to have been one conversation, not eight.",
   ]),
 ],
 "faq": [
   ("What if my job requires collecting contacts?", "Then the number is set for you, and the honest approach is different: short, purposeful, and a note on every one. Just do not confuse that with building a network."),
   ("Is it bad to stay with one person all night?", "Only if you both wanted to move and neither did. If it is a genuinely good conversation, that is the outcome you came for."),
   ("How do I know if it counted?", "You can name one specific thing they told you. If you cannot, it was an introduction."),
 ],
 "related": ["networking-for-introverts", "how-to-end-a-conversation-politely", "how-to-leave-a-networking-event-early"],
},
{
 "slug": "networking-when-youre-already-drained",
 "hub": "networking-for-introverts",
 "h1": "Networking when you are already drained",
 "title": "Networking When You Are Already Drained",
 "desc": "The event is tonight and you have nothing left. What to cut, what is still worth doing, and when to just not go.",
 "answer": "Go for forty minutes with one goal, or do not go. <strong>The version that costs you tomorrow is the open-ended one</strong> — arriving with no end time when you were already empty is how an event turns into two lost days.",
 "sections": [
   ("Decide which of the two it is, now", [
     "Forty minutes, one conversation, home — or a clear no. Both are fine. The bad option is arriving undecided and staying until the guilt lifts, which it does not.",
     "A short, deliberate appearance is a real attendance. Nobody is measuring the hours.",
   ]),
   ("If you go, cut everything except one thing", [
     "One person you want to speak to, or one conversation of any kind. Not a list, not the talks, not the after-drinks.",
     "Say your opening sentence out loud once before you leave the house. It is the only preparation worth doing when you have nothing spare.",
   ]),
   ("If you do not go, do the cheap version", [
     "Message one person you would have seen. \"Sorry to miss tonight — I wanted to ask you about X.\" That is most of the value of the event, for none of the cost.",
     "This is not a consolation prize. A specific message converts better than a room does.",
   ]),
   ("Protect the next day either way", [
     "Do not put anything demanding the morning after. Treating the recovery as part of the event is what stops the whole category becoming something you cancel.",
   ]),
   ("If every event feels like this", [
     "Then the problem is the volume, not the evening. Fewer, more deliberately chosen events beat a full calendar you resent, and they produce more, because you arrive with something left.",
   ]),
 ],
 "faq": [
   ("Is it worse to cancel late?", "For a small dinner or anything with a headcount, yes — tell them early. For a general event, nobody notices and you owe no explanation."),
   ("What if I always feel like this before?", "Dread before and fine during is extremely common, and it is different from arriving genuinely empty. The forty-minute version is a good test of which one it is."),
   ("Does coffee help?", "It reliably makes the physical symptoms of anxiety louder. If you are going in nervous rather than tired, it usually makes the first hour harder."),
 ],
 "related": ["networking-for-introverts", "masking-at-work-events", "how-to-leave-a-networking-event-early"],
},
{
 "slug": "conferences-for-introverts",
 "hub": "networking-for-introverts",
 "h1": "Getting through a multi-day conference",
 "title": "How to Get Through a Conference as an Introvert",
 "desc": "Three days is not one event three times. How to plan the days, which sessions to skip, and why the hallway is the actual conference.",
 "answer": "Plan the days like a budget, not a schedule. <strong>Pick two things per day and protect a real gap between them</strong> — the people who get the most out of a conference attend fewer sessions, not more, and spend the difference in the hallway.",
 "sections": [
   ("The hallway is the conference", [
     "Almost every talk will be online within a month. The conversations will not be.",
     "So skipping a session to keep talking to someone is not slacking, it is the correct trade. Plan to do it.",
   ]),
   ("Two things a day", [
     "One session you genuinely want, and one social thing. Everything else is optional and treating it that way is what makes day three survivable.",
     "Put a real gap between them. Not a gap you will fill — an empty one, in your room or outside.",
   ]),
   ("Day three is the one that breaks people", [
     "Energy does not reset overnight at a conference. Plan day three as the lightest day, not the one where you finally catch up on everything you missed.",
     "The last-night dinner is usually the best social value of the whole event. Protect the capacity for it.",
   ]),
   ("Go to the small things", [
     "Workshops, birds-of-a-feather sessions, anything with twelve people and a shared task. You will meet more people there than at any evening reception.",
     "A structured activity supplies the conversation, which removes the part that costs you most.",
   ]),
   ("Book one thing in advance", [
     "One coffee with one specific person, arranged before you travel. It gives the trip a guaranteed outcome and takes the pressure off every other interaction.",
   ]),
 ],
 "faq": [
   ("Should I go to the parties?", "Pick one. Going to all of them is how day three disappears, and they are largely interchangeable."),
   ("What if my employer sent me?", "Nobody is counting sessions. Come back with two useful contacts and a clear summary and you have done more than most attendees."),
   ("Is it worth staying in the venue hotel?", "Usually yes — being able to go upstairs for twenty minutes is worth more than the cheaper room twenty minutes away."),
 ],
 "related": ["networking-for-introverts", "networking-when-youre-already-drained", "sensory-overload-at-events"],
},
{
 "slug": "online-networking-for-introverts",
 "hub": "networking-for-introverts",
 "h1": "Networking online instead",
 "title": "Networking Online Instead of in a Room",
 "desc": "What actually works when you replace events with writing and messages, how long it takes, and where it beats a room outright.",
 "answer": "It works, it is slower to start and better afterwards. <strong>Writing in public and sending specific messages to specific people</strong> beats a mixer on almost every measure except speed — and unlike a room, it keeps working while you are asleep.",
 "sections": [
   ("What actually works", [
     "<strong>Writing in public.</strong> Anything that shows how you think about your own work. It brings people to you already knowing what you do, which is the hard part of a room solved in advance.",
     "<strong>Answering questions where your people are.</strong> A useful answer in a forum or a community is read by far more people than you would meet in an evening.",
     "<strong>Specific messages to specific people.</strong> One message referencing their actual work beats fifty connection requests.",
   ]),
   ("What does not", [
     "Connection requests with no note. Generic comments. Anything sent to a list.",
     "Volume is the failure mode online exactly as it is in a room, and it is easier to do at scale, which is why it is more common.",
   ]),
   ("It is slower at the start", [
     "A room gives you eight contacts in an evening and most of them are worth nothing. Online gives you almost nothing for a few months and then compounds.",
     "If you need something this quarter, a room or a set of direct messages is faster. If you are building something over a year, this wins.",
   ]),
   ("Where it is simply better", [
     "You can edit. For anyone who writes better than they improvise — which includes most dyslexic, autistic and anxious people once the writing tool fits them — that is not a small advantage.",
     "There is no closing time, no noise, and no recovery day.",
   ]),
   ("The hybrid that works best", [
     "Go to one event a quarter, and do the online part continuously. The event gives you names; the writing makes those names come back to you.",
   ]),
 ],
 "faq": [
   ("Does it have to be LinkedIn?", "No. Wherever your field actually talks — a forum, a Discord, a mailing list, a newsletter. LinkedIn is the default, not the requirement."),
   ("How often do I need to post?", "Consistently beats often. Once a fortnight for a year does more than daily for a month."),
   ("Is video required?", "No. Written work is read by more people than it is watched by in most professional fields, and it is searchable afterwards."),
 ],
 "related": ["networking-for-introverts", "linkedin-networking-message-examples", "do-i-actually-have-to-network"],
},
]

# ----------------------- tranche 7: the job-search hub, and the last few
PAGES += [
{
 "slug": "career-fair-with-social-anxiety",
 "hub": "job-search-networking",
 "h1": "Getting through a career fair with social anxiety",
 "title": "Career Fair With Social Anxiety",
 "desc": "A hall full of queues and recruiters. How to pick five tables, what to do about the queue, and why the first one should be a company you do not want.",
 "answer": "Pick five tables before you go and do your worst-fit one first. <strong>The first conversation is always the roughest, so spend it on a company you do not care about.</strong> Twenty seconds and one question per table is a complete interaction — nobody expects more.",
 "sections": [
   ("Five tables, chosen in advance", [
     "Walking the whole hall means reaching the companies you actually want while tired and out of sentences.",
     "Look at the exhibitor list the night before, pick five, and let the rest go. You are not missing anything — the rest are hiring through the same website.",
   ]),
   ("Burn the first one", [
     "Your worst-fit company first, deliberately. The first conversation is where your voice does the thing and you forget your own degree.",
     "By the third table you sound like a person. That is the only reason the order matters.",
   ]),
   ("The queue is the easiest part of the day", [
     "Everyone in it is in your position and there is a guaranteed shared subject. \"Have you done this one before?\" is an entire conversation, and those people are often more useful than the recruiter.",
     "It is also the only place at a career fair where nobody is assessing you.",
   ]),
   ("Twenty seconds is a full interaction", [
     "Who you are, what you are looking for, one specific thing about them. Then one question. Then their name and where to send the application.",
     "Recruiters at a fair are having the same ninety-second conversation two hundred times. Short is a relief, not a failure.",
   ]),
   ("Plan the exit and the break", [
     "Decide when you are leaving before you arrive, and take a break outside after the third table. Halls like these are loud, bright and airless, and that is doing more to you than the conversations are.",
   ]),
 ],
 "faq": [
   ("What if I freeze at the table?", "Hand over your résumé and say \"I'm interested in your graduate roles — what do you look for?\" It is a complete interaction and the question does the work."),
   ("Is it worth going at all if I apply online anyway?", "The name is what you get. An application that says \"I spoke to Priya at the fair\" is read differently from one that does not."),
   ("Can I go with a friend?", "Walk in together and split up at the door. Doing the tables as a pair halves how much anyone talks to either of you."),
 ],
 "related": ["career-fair-what-to-say", "job-search-networking", "networking-with-social-anxiety"],
},
{
 "slug": "informational-interview-questions",
 "hub": "job-search-networking",
 "h1": "Questions for an informational interview",
 "title": "Informational Interview Questions",
 "desc": "Fifteen questions that get a real answer, the three to avoid, and the one to always end on.",
 "answer": "Ask what the work is actually like, what they did not expect, and what would make someone like you credible. <strong>Avoid anything they cannot answer or that is on the website</strong> — and always end by asking who else you should be talking to.",
 "sections": [
   ("About the work itself", [
     "What does a normal week actually look like?",
     "What is the part of this job nobody warns you about?",
     "What did you believe about this work before you did it that turned out to be wrong?",
     "What is the hardest decision you make regularly?",
     "What would make you leave?",
   ]),
   ("About the path in", [
     "How did you end up here — what was the actual route?",
     "What would make someone with my background credible for this?",
     "What is the gap you would expect me to have?",
     "Is there a title or a step I should be aiming at first?",
     "What do the people who get hired here tend to have in common?",
   ]),
   ("About the field", [
     "What is changing in this work that people outside it have not noticed?",
     "What is overrated right now, and what is underrated?",
     "Where would you look if you were starting today?",
     "What should I be reading or following?",
     "Who is doing the most interesting work in this area?",
   ]),
   ("The three to avoid", [
     "<strong>\"Are you hiring?\"</strong> It converts a generous conversation into an obligation, and it is why people stop agreeing to these.",
     "<strong>Anything on the website.</strong> What the company does, how many people work there, when it was founded. Asking signals you did not look.",
     "<strong>\"What is your salary?\"</strong> Ask about the range for the role in the market, not about their pay.",
   ]),
   ("Always end with this one", [
     "\"Who else should I be talking to?\" It is the most valuable question in the conversation, it is a natural ending, and it often produces an introduction you could not have asked for directly.",
   ]),
 ],
 "faq": [
   ("How many should I ask?", "Three prepared, and expect to use two. Good answers generate their own follow-ups and twenty minutes fills faster than people expect."),
   ("Should I send them in advance?", "Only if they ask. Sending a list makes it feel like an interview of them, which changes how candidly people answer."),
   ("Is it okay to take notes?", "Yes, and say so — \"do you mind if I write some of this down?\" People are more forthcoming when they can see it is being taken seriously."),
 ],
 "related": ["job-search-networking", "what-to-say-in-a-coffee-chat", "how-to-ask-for-a-referral"],
},
{
 "slug": "linkedin-networking-message-examples",
 "hub": "job-search-networking",
 "h1": "LinkedIn messages to someone you have never met",
 "title": "LinkedIn Networking Message Examples",
 "desc": "Four cold messages that get replies, the structure underneath them, and the two mistakes that get everything else ignored.",
 "answer": "Short, specific, and asking for something they can give in three sentences. <strong>Reference their actual work in the first line</strong> — a message that would make sense sent to a hundred people gets treated as if it was.",
 "sections": [
   ("The structure", [
     "One line proving you know who they are, one line on who you are, and one question they can answer quickly. That is the whole message.",
     "Under eighty words. Longer messages do not get more replies, they get fewer.",
   ]),
   ("Asking about their path", [
     "\"Hi [name] — I saw you moved from consulting into product at [company], which is roughly the move I am trying to make. Was the transition as hard as people say? I am [one line about me]. Any answer appreciated, even a short one.\"",
   ]),
   ("Asking about their work", [
     "\"Hi [name] — your post about [specific thing] stuck with me, particularly the part about [detail]. I am working on something similar at [context]. Did you end up keeping that approach?\"",
   ]),
   ("Asking for twenty minutes", [
     "\"Hi [name] — I am trying to work out whether to move into [field] and you have actually done it. Would you be open to twenty minutes in the next couple of weeks? Happy to work entirely around you, and happy to send questions in advance if that is easier.\"",
   ]),
   ("After a mutual introduction", [
     "\"Hi [name] — [mutual] suggested I get in touch. I am [one line], trying to [specific thing], and they thought you would have a view on [topic]. Do you have twenty minutes in the next fortnight?\"",
     "A named mutual is worth more than everything else on this page combined. Always lead with it.",
   ]),
   ("The two mistakes", [
     "<strong>No specific reference.</strong> If the first line could be sent to anyone in their industry, it reads as a mail merge.",
     "<strong>Asking for too much.</strong> \"Can I pick your brain?\" has no shape, so it has no easy yes — where \"twenty minutes\" and \"one question\" both do.",
   ]),
 ],
 "faq": [
   ("Connection request or message?", "A note on the request if it is short. A proper message once connected, if it needs more than eighty words. Never a pitch inside the request."),
   ("What reply rate should I expect?", "Low, and it is not about you. Five thoughtful messages beat fifty generic ones, and the fifty will make you hate doing it."),
   ("Should I follow up?", "Once, after about ten days, shorter than the first. Then stop."),
 ],
 "related": ["job-search-networking", "linkedin-message-after-meeting-someone", "online-networking-for-introverts"],
},
{
 "slug": "networking-as-a-student",
 "hub": "job-search-networking",
 "h1": "Networking while you are still studying",
 "title": "Networking as a Student",
 "desc": "You have less to offer and far more permission to ask. How to use the student advantage before it expires.",
 "answer": "Being a student is the best position you will ever have for this. <strong>\"I am a student trying to work out what to aim at\" gets answered by people who ignore everyone else</strong> — because you are asking for advice rather than a job, and advice is easy to give.",
 "sections": [
   ("Use the permission while it lasts", [
     "A student asking how someone got into their field is charming. The same question from a mid-career person is a networking request with all the friction that carries.",
     "This window closes the month you graduate. Spend it.",
   ]),
   ("Alumni are the whole game", [
     "Shared university is the single most reliable reason a stranger replies. Most schools have a searchable alumni list, and LinkedIn will filter by it.",
     "\"I am at [university] now, doing [subject], and I saw you did the same\" is a complete opening line.",
   ]),
   ("Ask for the route, not the role", [
     "\"How did you get from a degree like mine to what you are doing?\" is answerable and interesting to them.",
     "\"Do you have any openings?\" is a question most people cannot answer and will not enjoy receiving.",
   ]),
   ("Do things that are visible", [
     "A project, a society you actually run, something you built and published. It is the fastest way to have something to talk about that is not your coursework.",
     "It also solves the real problem of student networking, which is not access but having anything specific to say.",
   ]),
   ("Career fairs are practice, not the goal", [
     "Go, get names, and treat the conversations as reps. The applications still go through the website, and the value is the name you can put in them.",
   ]),
 ],
 "faq": [
   ("Is it too early in first year?", "No, and it is the easiest time. Nobody expects a first-year to know what they want, so the conversations are genuinely low stakes."),
   ("What if I have no experience to talk about?", "Talk about what you are curious about instead. \"I am trying to work out whether X or Y\" is a better conversation than a thin resume."),
   ("Do professors count?", "Very much. They have decades of former students in industry and they are rarely asked. Ask who they would put you in touch with."),
 ],
 "related": ["job-search-networking", "career-fair-what-to-say", "informational-interview-questions"],
},
{
 "slug": "networking-after-a-layoff",
 "hub": "job-search-networking",
 "h1": "Networking after being laid off",
 "title": "Networking After Being Laid Off",
 "desc": "What to say about it, who to tell first, and why the message you dread sending is the one that works.",
 "answer": "Say it plainly and early. <strong>\"My role was cut in the restructure, so I am looking\"</strong> is a complete explanation, it is extremely common, and it tells people exactly how to help. Vagueness is what stops people acting, not the layoff.",
 "sections": [
   ("Name it without apology", [
     "A layoff is a company decision, and everyone reading your message knows that. Treating it as something to explain away invites a scrutiny that is not otherwise there.",
     "One clear sentence, then what you are looking for. That is the whole thing.",
   ]),
   ("Tell your existing contacts first", [
     "Former colleagues, former managers, people you worked with at other companies. They already know your work, which is the hard part solved.",
     "This is the most effective and most avoided step, because it is the one where it feels most exposing. It is also where the jobs come from.",
   ]),
   ("Be specific about what you want", [
     "\"Looking for anything\" is unanswerable. \"Looking for a senior backend role, ideally fintech, remote or Leeds\" is something a person can match against a thing they saw yesterday.",
     "People want to help and mostly cannot, because they were not given enough to act on.",
   ]),
   ("Ask for something small", [
     "\"If anything crosses your desk I would appreciate a heads up\" is easy to say yes to. \"Can you get me an interview\" is not.",
     "The small ask is what keeps you in their head for the next six months.",
   ]),
   ("Going to events while looking", [
     "Go, and be straightforward about why you are there. Nobody at a professional event finds it strange, and a lot of the room has been through it.",
     "Prepare the sentence in advance so you are not composing it in the moment, which is when it comes out sounding worse than the situation is.",
   ]),
 ],
 "faq": [
   ("Should I put 'open to work' on my profile?", "It measurably increases recruiter contact. Some people find the banner uncomfortable — the setting that shows it only to recruiters is a reasonable middle."),
   ("How long should I wait before telling people?", "Days, not weeks. The market moves and the awkwardness does not decrease with time — it increases, because then you also have to explain the gap in contact."),
   ("What if I was let go rather than laid off?", "\"It was not the right fit and we parted ways\" is a normal sentence that closes the subject. Do not volunteer more; almost nobody asks a second question."),
 ],
 "related": ["job-search-networking", "how-to-ask-for-a-referral", "how-to-introduce-yourself-at-a-networking-event"],
},
{
 "slug": "how-to-ask-for-a-referral",
 "hub": "job-search-networking",
 "h1": "How to ask someone for a referral",
 "title": "How to Ask for a Referral",
 "desc": "Who you can reasonably ask, the message that makes it easy to say yes, and how to make it almost no work for them.",
 "answer": "Ask people who have seen you work, name the exact role, and <strong>write the paragraph for them</strong>. A referral fails when it is effortful — give them the link, two lines on why you fit, and an easy way to decline.",
 "sections": [
   ("Who you can actually ask", [
     "Anyone who has seen your work directly: former colleagues, managers, clients, collaborators. They are staking their judgment, so they need to have some.",
     "Someone you met once at an event cannot refer you. They can introduce you, which is a different and much easier ask.",
   ]),
   ("Make it nearly no work", [
     "The link to the specific role. Two or three lines they can paste about why you fit it. Your resume attached.",
     "Most referrals die because the person meant to do it and the task never got small enough to finish.",
   ]),
   ("The message", [
     "\"Hi [name] — [company] is hiring a [role] and I am applying. We worked together on [project], so you have actually seen me do this. Would you be comfortable putting in a referral? I have pasted a couple of lines below you are welcome to use or ignore. Completely fine if not.\"",
   ]),
   ("Give them the exit", [
     "\"Completely fine if not\" at the end matters more than it looks. Without it, someone who is not comfortable referring you often just does not reply, and you lose the contact as well as the referral.",
   ]),
   ("Afterwards", [
     "Tell them what happened either way. People who referred someone and never heard the outcome are noticeably less willing the next time.",
   ]),
 ],
 "faq": [
   ("What if we have not spoken in years?", "Acknowledge it in half a line and ask anyway. Former colleagues are usually glad to hear from someone and a referral is a small thing to give."),
   ("Is it rude to ask someone senior?", "No, if they saw your work. Referring good people is part of a senior job and most companies pay a bonus for it."),
   ("What if they say no?", "Thank them and move on without asking why. A no protects a relationship that a pressured yes would damage."),
 ],
 "related": ["job-search-networking", "networking-after-a-layoff", "informational-interview-questions"],
},
{
 "slug": "networking-for-a-career-change",
 "hub": "job-search-networking",
 "h1": "Networking when you are changing fields",
 "title": "Networking for a Career Change",
 "desc": "Nobody in the new field knows you and your resume points the wrong way. What to ask, and how to stop leading with the gap.",
 "answer": "Stop explaining the gap and start asking about the work. <strong>\"What would make someone from my background credible here?\"</strong> turns your resume from a problem you are defending into a question they can help with — and people are far more willing to answer that.",
 "sections": [
   ("Lead with the destination, not the history", [
     "\"I am moving into X\" is a much better opening than \"I have spent eight years in Y.\" The first is a direction; the second is a thing to be explained.",
     "Your history becomes an advantage once the direction is established, and a liability if it arrives first.",
   ]),
   ("The question that does the most work", [
     "\"What would make someone with my background credible for this?\" It is specific, they know the answer, and it makes them a collaborator instead of an assessor.",
     "It also gets you the real hiring criteria, which is rarely what the job posting says.",
   ]),
   ("Find the people who already made the same move", [
     "They have made your argument before, to someone who eventually said yes. They know which parts of your history to foreground and which to drop.",
     "They are also unusually willing to help, because somebody did it for them.",
   ]),
   ("Build one visible thing", [
     "A project, a piece of writing, a small piece of real work in the new field. It converts \"wants to move into X\" into \"has done X\", which is a different conversation entirely.",
     "This does more than any number of coffees, and it makes the coffees go better.",
   ]),
   ("Expect it to take longer", [
     "A change of field runs on months of small contact, not a burst of applications. The people who make it are usually the ones who kept talking to the same handful of contacts over a year.",
   ]),
 ],
 "faq": [
   ("Do I need to retrain first?", "Often no, and it is the most common way people delay. Ask three people in the field before you spend money on a course — they will tell you whether it is the actual barrier."),
   ("How do I explain the change?", "One sentence, forward-looking. \"I want to work on X and this is the closest I can get\" needs no defense and invites no follow-up."),
   ("Is it worth going to events in the new field if I know nobody?", "Yes, and being new is a usable position: \"I am moving into this and trying to work out who does what\" is a legitimate reason to talk to anyone in the room."),
 ],
 "related": ["job-search-networking", "informational-interview-questions", "do-i-actually-have-to-network"],
},
{
 "slug": "what-to-bring-to-a-networking-event",
 "hub": "networking-with-social-anxiety",
 "h1": "What to bring to a networking event",
 "title": "What to Bring to a Networking Event",
 "desc": "A short list. What actually gets used, what never does, and the one thing most people forget.",
 "answer": "A charged phone, something to hold, and your two prepared questions. <strong>The thing most people forget is a way to take a note</strong> — without it every conversation has to survive in your memory until you get home, and none of them do.",
 "sections": [
   ("The short list", [
     "<strong>A charged phone.</strong> Notes, the event app, the taxi home, and a legitimate thing to look at if you need thirty seconds.",
     "<strong>Your two questions and your opening line.</strong> In your notes app, said out loud once before you left.",
     "<strong>Cards, if you have them.</strong> Ten is plenty. If you do not have them, it matters much less than it used to.",
     "<strong>Filtered earplugs, if noise is a problem for you.</strong> They cut the volume without cutting the speech.",
   ]),
   ("What never gets used", [
     "Printed résumés at a general networking event — different from a career fair, where they are the currency.",
     "A laptop bag. It is one more thing to manage and there is nowhere to put it down.",
     "A folder of anything. If it needs a folder, it is a meeting, not an event.",
   ]),
   ("Wear something with pockets", [
     "You will be holding a drink. Anything that needs two hands is a problem you have created for yourself.",
   ]),
   ("Eat before you go", [
     "Not something to bring, but the one that changes the first hour most. Event food arrives late, is impossible to eat standing up, and there is never enough of it.",
   ]),
 ],
 "faq": [
   ("Do I still need business cards?", "Less every year, but they solve the exchange in three seconds with no phones. If you have them, bring a few."),
   ("Should I bring a notebook?", "Only if you will actually use it. A phone is faster, quieter and does not require a surface."),
   ("What should I wear?", "Match the industry and go one step smarter if unsure. It is the least interesting decision of the evening and worth settling the night before."),
 ],
 "related": ["the-hour-before-a-networking-event", "how-to-remember-who-you-met", "what-to-do-with-the-business-cards"],
},
{
 "slug": "how-to-network-at-a-conference",
 "hub": "networking-for-introverts",
 "h1": "How to meet people at a conference",
 "title": "How to Network at a Conference",
 "desc": "Where the conversations actually happen, how to use the schedule as a tool, and the one thing to arrange before you travel.",
 "answer": "Skip a session to keep talking to someone. <strong>The hallway is where a conference actually happens</strong> — the talks are online within a month, the conversations are not. Arrange one specific coffee before you travel so the trip has a guaranteed outcome.",
 "sections": [
   ("Arrange one thing in advance", [
     "One person, one coffee, booked before you get on the plane. It takes the pressure off every other interaction because the trip already worked.",
     "The message is easy: \"I see you are speaking at [conference] — I would like to ask you about [thing]. Any chance of twenty minutes while we are both there?\"",
   ]),
   ("Use the schedule as a conversation tool", [
     "\"Are you going to the [topic] session?\" is the easiest opener at a conference and it is always available.",
     "Sitting next to someone in a session gives you a shared subject the moment it ends. That is the cheapest introduction in the building.",
   ]),
   ("Go to the small sessions", [
     "Workshops and roundtables with a dozen people produce more contacts than any evening reception, because you are doing something together rather than performing conversation.",
   ]),
   ("The queue and the coffee table", [
     "Everyone in a queue has time and no one to talk to. It is the single highest-yield place at the whole event and it costs nothing.",
   ]),
   ("Write the note before the next session", [
     "Name and one detail, into your phone, between sessions. By day three you will have met thirty people and remember four of them without this.",
   ]),
 ],
 "faq": [
   ("Should I go to the speaker's talk before approaching them?", "Yes, and reference something specific from it. It is the difference between a fan and a colleague, and it takes one sentence."),
   ("What if I do not know anyone at all?", "Arrive early on day one. The first morning is the only time nobody has formed groups yet, and it is much easier than day two."),
   ("Is the evening event worth it?", "One of them. They are largely interchangeable and going to all of them is how the last day disappears."),
 ],
 "related": ["conferences-for-introverts", "networking-for-introverts", "how-to-remember-who-you-met"],
},
]

# ------------------------------------------------- tranche 8: the last three
PAGES += [
{
 "slug": "how-to-network-on-linkedin",
 "hub": "job-search-networking",
 "h1": "How to network on LinkedIn",
 "title": "How to Network on LinkedIn",
 "desc": "What works, in order: being findable, being useful in public, and sending few specific messages. Plus what to stop doing.",
 "answer": "Three things, in this order: <strong>make your profile say what you actually do, comment usefully where your field talks, and send few specific messages.</strong> Most people do only the third, which is why it does not work for them.",
 "sections": [
   ("First, be findable and legible", [
     "Your headline should say what you do, not your job title. \"I build booking systems for clinics\" is searchable and human; \"Senior Engineer II\" is neither.",
     "The About section is the one people read before deciding whether to reply to you. Three short paragraphs in plain words beats a list of technologies.",
   ]),
   ("Second, be useful in public", [
     "A specific, helpful comment on someone's post is read by their whole audience and costs you two minutes. It is by far the highest return per unit of effort on the platform.",
     "Posting your own work is better but slower. Commenting well for a month is the cheapest way to become a name people recognize.",
   ]),
   ("Third, and only third, message people", [
     "Few and specific. One line proving you know their work, one line on you, one question they can answer quickly.",
     "The order matters: a message from someone whose comments they have seen is a different object from a message out of nowhere.",
   ]),
   ("What to stop doing", [
     "Connection requests with no note, automated anything, asking to \"pick your brain\", congratulating strangers on work anniversaries.",
     "All of them are volume tactics, and volume is what trained everyone to ignore this kind of message in the first place.",
   ]),
   ("It compounds slowly", [
     "Nothing happens for two months and then people start replying because they half recognize you. That lag is normal and it is the reason most people quit at week three.",
   ]),
 ],
 "faq": [
   ("Do I have to post?", "No. Commenting well does most of the work and takes a fraction of the effort. Posting accelerates it."),
   ("How often?", "Consistently rather than often. A few comments a week for a year beats a burst of daily activity for a month."),
   ("Is a premium account worth it?", "For most people no. The free account does everything described here."),
 ],
 "related": ["linkedin-networking-message-examples", "online-networking-for-introverts", "job-search-networking"],
},
{
 "slug": "your-first-networking-event",
 "hub": "networking-with-social-anxiety",
 "h1": "What to expect at your first networking event",
 "title": "What to Expect at Your First Networking Event",
 "desc": "What actually happens, in order, from the door to going home — so that none of it is a surprise.",
 "answer": "A room of people who mostly also do not know each other, standing in small groups, holding drinks. <strong>There is no structure and nobody is in charge of introducing you</strong> — which is the part that surprises people, and the reason arriving early helps so much.",
 "sections": [
   ("What actually happens, in order", [
     "You give your name at a desk and get a badge. Somebody points at the room.",
     "People stand in groups of two to five and talk. There may be a talk partway through, and it is usually the easiest part of the night.",
     "It ends earlier than you expect. Most weekday events are thinning out within two hours.",
   ]),
   ("Nobody is going to introduce you", [
     "This is the thing first-timers find hardest, and it is not a failure of the event. There is no host moving between groups introducing people.",
     "Which means approaching is the whole skill, and it is why arriving early — when there are fewer formed groups — is worth more than anything else you can do.",
   ]),
   ("Everyone is more nervous than they look", [
     "The groups that look established usually met twenty minutes ago. The person who looks completely at ease is often the one who has been to forty of these and still dreads them.",
     "\"Is this your first one of these?\" gets a yes far more often than the room suggests.",
   ]),
   ("What counts as a good night", [
     "Two conversations you can remember something specific from. That is it.",
     "Not a pocket of cards, not meeting the speaker, not staying until the end.",
   ]),
   ("Bring three sentences", [
     "Who you are, two questions, and a line for leaving a conversation. Said out loud once before you go.",
     "With those three, the room stops requiring improvisation, which is the part that makes a first event exhausting.",
   ]),
 ],
 "faq": [
   ("When should I arrive?", "Early, ideally in the first fifteen minutes. An empty room is much easier to enter than a full one and the conversations start themselves."),
   ("How long do I have to stay?", "Until you have done the thing you came for. Forty minutes with two conversations is a complete, successful attendance."),
   ("What if I know nobody at all?", "That is the normal condition, not the bad case. Find someone else standing alone and say so out loud — it works because it is true."),
 ],
 "related": ["networking-with-social-anxiety", "how-to-go-to-a-networking-event-alone", "what-to-bring-to-a-networking-event"],
},
{
 "slug": "common-networking-mistakes",
 "hub": "what-to-say-when-you-dont-know-anyone",
 "h1": "The mistakes that actually cost you something",
 "title": "Common Networking Mistakes",
 "desc": "Not the etiquette list. The handful of things that genuinely waste an evening, and what to do instead of each.",
 "answer": "Almost none of the usual advice matters. <strong>The three that actually cost you are: never following up, trying to meet everyone, and asking for something before you have given anything.</strong> The rest is etiquette nobody is grading.",
 "sections": [
   ("Not following up", [
     "This is the only one that costs something real. An evening of good conversations with no message afterwards produces exactly nothing.",
     "It fails for a mechanical reason, not a character one: the detail is gone by the time you sit down to write. Take the note on the night.",
   ]),
   ("Trying to meet everyone", [
     "Twenty introductions leaves twenty people who cannot say what you do. Two real conversations leaves two who can.",
     "Circulating feels productive and is the most common way to end an evening with nothing.",
   ]),
   ("Asking before giving", [
     "A request in the first conversation puts the other person in the position of saying no to a stranger, and most will avoid that by not replying at all.",
     "Ask a question they can answer instead. The person who answered a question is the one who thinks of you later.",
   ]),
   ("Talking only to the person you came with", [
     "A friend is a place to hide, and a pair reads as closed to everyone else in the room. Walk in together and split at the door.",
   ]),
   ("Staying too long", [
     "An open-ended evening has no success condition, so it ends in the feeling that you should have done more, regardless of what happened.",
     "Decide the end time before you arrive. Leaving on it, having done the thing, is what makes the next one answerable.",
   ]),
   ("What does not matter", [
     "A slightly awkward opener, forgetting a name, not having cards, leaving early. Saying something a bit odd and then thinking about it for a week.",
     "Nobody else is keeping that record. You are the only person in the building running it.",
   ]),
 ],
 "faq": [
   ("Is it a mistake to talk about myself?", "Only if you do not stop. A rough rule: a question roughly every third thing you say keeps it a conversation."),
   ("What about drinking?", "One is fine if you normally drink. The problem with more is the follow-up note you never take and the conversations you cannot reconstruct."),
   ("Is it bad to leave a conversation?", "No — it is the expected behavior at an event, and doing it cleanly is a kindness. Being unable to leave one is what actually ruins evenings."),
 ],
 "related": ["what-to-say-when-you-dont-know-anyone", "how-to-follow-up-after-a-networking-event", "how-many-people-should-i-talk-to"],
},
]

# ===================== WAVE 2: neurodivergence and anxiety at work ==========
# See PAGE-QUEUE.md "Wave 2". Two hard lines: nothing medical (no diagnosis,
# symptoms, tests or medication) and nothing that reads as legal advice.

PAGES += [
{
 "slug": "adhd-at-work",
 "hub": None,
 "h1": "ADHD at work",
 "title": "ADHD at Work — What Actually Helps",
 "desc": "The parts of a working day that cost most with ADHD, and the fixes that survive a real job: meetings, email, deadlines, and the follow-through nobody sees.",
 "answer": "Most ADHD advice at work is about focus. <strong>The parts that actually cost you are the ones with no structure</strong> — an unstructured meeting, an inbox, a task with no deadline until it is late. Add the structure from outside rather than trying to supply it yourself.",
 "sections": [
   ("Where the day actually goes wrong", [
     "Not the deep work. People with ADHD often do that part well, sometimes better than anyone.",
     "It goes wrong at the joins: remembering what was agreed, starting something with no deadline, answering the email you read three days ago, being somewhere at a time.",
   ]),
   ("Put the structure outside your head", [
     "<strong>Write during the meeting, not after.</strong> Whatever you have not written down by the time you stand up is gone, and no amount of intending to remember changes that.",
     "<strong>Give unstructured tasks a fake deadline and tell someone.</strong> The external commitment is what makes it real.",
     "<strong>Decide the first physical action.</strong> \"Write the report\" does not start. \"Open the doc and paste last month's headings\" does.",
   ]),
   ("The follow-through is what people actually see", [
     "Colleagues do not see your focus. They see whether the thing you said you would send arrived.",
     "That is why capture beats willpower here: the reply you never sent is the whole impression, and it usually failed because the detail was gone, not because you did not care.",
   ]),
   ("Say the thing out loud", [
     "\"Send me that in writing and I will act on it\" is a completely normal sentence and it fixes half the problem without disclosing anything.",
     "So is \"give me until Thursday\" instead of an optimistic yes. Time estimates are a known weak point and a deliberate buffer is cheaper than an apology.",
   ]),
   ("What Haveo does with this", [
     "Haveo is built for the events end of this — preparing what you will say, and capturing who you met before the detail disappears. The same habit that saves a networking follow-up saves a meeting action.",
   ]),
 ],
 "faq": [
   ("Should I tell my employer?", "That is a real decision with no single right answer, and it depends on your workplace and your country. There is a page on it here that walks through what people actually weigh up — it is not legal advice."),
   ("Do productivity apps help?", "The ones that reduce a decision help. The ones that add a system to maintain become another thing to abandon in three weeks, which is its own small cost."),
   ("Is it worse in an open-plan office?", "Usually, and that is worth naming as an environment problem rather than a personal failing. Noise-filtering earplugs and a booked room for anything that needs thinking are the two cheapest fixes."),
 ],
 "related": ["adhd-job-interview", "adhd-in-meetings", "networking-with-adhd"],
},
{
 "slug": "adhd-job-interview",
 "hub": "adhd-at-work",
 "h1": "Job interviews with ADHD",
 "title": "Job Interviews With ADHD",
 "desc": "Rambling, losing the question, and the weakness question. What to prepare, what to ask for, and how to answer without disclosing anything you do not want to.",
 "answer": "Prepare six stories, not answers. <strong>An interview with ADHD goes wrong when you improvise at length</strong> — you start well, lose the question halfway, and finish somewhere else. Six rehearsed stories cover almost every question and stop the rambling at the source.",
 "sections": [
   ("Six stories, not thirty answers", [
     "Something you shipped, something that went wrong, a time you disagreed with someone. A time you had to learn something fast, something you are proud of, and why this job.",
     "Almost every behavioral question is one of those six wearing a different hat. Rehearsing six is achievable; rehearsing thirty is why people stop preparing.",
   ]),
   ("Say them out loud before the day", [
     "Out loud, not in your head. A story you have only thought through comes out twice as long and half as clear under pressure.",
     "Time one. If it runs past two minutes it will run past four on the day.",
   ]),
   ("When you lose the question", [
     "Ask for it back. \"Sorry, could you repeat the question?\" is completely ordinary and interviewers do not mark it.",
     "Better still, buy time on purpose: \"Let me think about that for a second.\" Silence reads as considered, and it is far better than talking while you search.",
   ]),
   ("The weakness question", [
     "You do not have to name a diagnosis. Answer with a behavior and the thing you do about it: \"I lose detail in long meetings, so I write during them and send a summary after — it has caught things twice.\"",
     "That is true, specific, and it demonstrates the fix rather than confessing a flaw.",
   ]),
   ("Asking for adjustments", [
     "You can ask for the questions in advance, extra time, or a written task instead of a timed verbal one. Many employers say yes and it is a normal request.",
     "You can ask for the thing without the label — \"could you send the questions beforehand?\" needs no explanation attached.",
   ]),
 ],
 "faq": [
   ("Should I disclose ADHD in an interview?", "You are not obliged to, and what protection you have varies by country. Most people who do it wait until they have an offer. This is a decision, not legal advice."),
   ("What if I interrupt the interviewer?", "Say \"sorry, go on\" and let them finish. It reads as enthusiasm far more often than rudeness, and the recovery is what people remember."),
   ("Are panel interviews worse?", "Usually, because there is more to track. Ask who is who at the start and write the names down — that removes one whole thing you would otherwise be holding."),
 ],
 "related": ["adhd-at-work", "asking-for-interview-adjustments", "what-to-say-about-your-weakness"],
},
{
 "slug": "adhd-in-meetings",
 "hub": "adhd-at-work",
 "h1": "Meetings with ADHD",
 "title": "Meetings With ADHD",
 "desc": "Losing the thread, interrupting, and remembering nothing afterwards. Four fixes that work in a real meeting, including the one that matters most.",
 "answer": "Write during the meeting, not after. <strong>Whatever is not written down by the time you stand up is gone</strong>, and intending to remember it does not work. That single habit fixes more than any amount of trying to concentrate harder.",
 "sections": [
   ("Take notes as a way of listening", [
     "Not minutes. Fragments: names, decisions, anything with your name on it.",
     "Writing gives the restless part of your attention a job, which is why note-takers follow long meetings better than people trying to sit still and focus.",
   ]),
   ("Park the thought instead of saying it", [
     "Interrupting is usually offloading a thought before it disappears, not rudeness. Put it somewhere else: three words in your notes, or one finger against your leg.",
     "\"I want to come back to something\" also works, and most people hear it as engagement.",
   ]),
   ("Ask for the thing you missed", [
     "\"Can I check what we decided on the second point?\" is a good question, not an admission. Half the room usually wanted to ask it.",
     "Do it in the meeting rather than guessing afterwards, which is where the real cost lands.",
   ]),
   ("Send the summary", [
     "Five lines within the hour: what was decided, who is doing what, what is unclear. It takes three minutes.",
     "It is also the highest-leverage habit on this page — it fixes your own recall AND makes you the person whose meetings produce outcomes.",
   ]),
   ("Long meetings", [
     "Ask whether you are needed for all of it. \"Do you need me after the first item?\" is a normal question and the answer is often no.",
   ]),
 ],
 "faq": [
   ("Is it rude to take notes on a laptop?", "Say what you are doing — \"I am taking notes, not emailing\" — and it stops being ambiguous. Paper avoids the question entirely if the room is funny about screens."),
   ("What about video meetings?", "Harder, because there is less to do with your body and more to watch. Notes help more, not less, and turning off self-view removes one thing you are monitoring."),
   ("I zone out and miss my turn.", "Ask to go first when there is a round. It costs nothing and removes twenty minutes of waiting for your name."),
 ],
 "related": ["adhd-at-work", "speaking-up-in-meetings", "adhd-note-taking"],
},
{
 "slug": "adhd-remote-work",
 "hub": "adhd-at-work",
 "h1": "Working from home with ADHD",
 "title": "Remote Work With ADHD",
 "desc": "No commute, no colleagues, no edges to the day. What to build back in, and why the structure has to come from outside you.",
 "answer": "Remote work removes every external structure at once and asks you to supply it. <strong>Put the edges back deliberately</strong> — a start, an end, and at least one commitment with another person in it. Willpower is not a substitute for a calendar.",
 "sections": [
   ("What was removed", [
     "A commute that marked the start, and people who could see whether you had started. A lunch that happened because others went, and an end because the building emptied.",
     "None of those were motivation. They were structure, and losing all of them at once is why remote work is harder with ADHD rather than easier.",
   ]),
   ("Put edges back", [
     "<strong>A start ritual.</strong> A walk around the block, the same coffee, anything that is not opening a laptop in bed.",
     "<strong>A hard end.</strong> An alarm, a gym class, somebody expecting you. Without it the day leaks until midnight and tomorrow starts already tired.",
     "<strong>One scheduled human.</strong> A standing call with a colleague does more for follow-through than any app.",
   ]),
   ("Body doubling", [
     "Working on a call with someone else working, both silent, is the single most reported remote fix among people with ADHD. It sounds odd and it works.",
     "It reproduces the only useful thing about an office: somebody else is present and also working.",
   ]),
   ("Asking for it formally", [
     "Flexible hours, written briefs instead of verbal ones, and a recorded meeting you can rewatch are all reasonable, common requests.",
     "You can ask for any of them as a working preference, without a label attached.",
   ]),
   ("Days with no meetings", [
     "They sound ideal and are usually the worst ones, because nothing anchors the day. If you have one, put one small fixed commitment in the middle of it.",
   ]),
 ],
 "faq": [
   ("Is an office actually better?", "For some people yes, and that is worth knowing about yourself rather than assuming remote is a perk. A hybrid pattern chosen on purpose beats either by default."),
   ("Do timers help?", "A timer that starts something helps. A timer that measures how long you focused becomes another score to fail at."),
   ("What about working from a cafe?", "Often very well — background activity, a reason to have started, and a natural end when you leave. The cost is noise, so bring filtered earplugs."),
 ],
 "related": ["adhd-at-work", "adhd-time-blindness-at-work", "going-back-to-the-office"],
},
]

PAGES += [
{
 "slug": "adhd-note-taking",
 "hub": "adhd-at-work",
 "h1": "Taking notes with ADHD",
 "title": "Note-Taking With ADHD",
 "desc": "Why the neat system always gets abandoned, and the four-line format that survives a real week.",
 "answer": "Any system you have to maintain will be abandoned by week three. <strong>Capture in one place, in whatever state, and sort later or never.</strong> A messy note you actually wrote beats a beautiful system you stopped using on the ninth of the month.",
 "sections": [
   ("Why the good systems fail", [
     "Tags, folders and color codes are a second job, and it is the job that gets dropped first when the week gets hard.",
     "The system also becomes a procrastination target: reorganising it feels productive and produces nothing.",
   ]),
   ("One inbox, no decisions", [
     "One note, one app, always the same one. Anything that requires choosing where something goes is a decision you will avoid making at the moment of capture.",
     "The whole value is in the writing-down. Retrieval matters far less than people think, because most captured things only need to exist for a day.",
   ]),
   ("Four lines is a meeting note", [
     "Decided, owed by me, owed to me, unclear.",
     "That is enough to act on and short enough to write while still listening. Anything longer competes with the meeting.",
   ]),
   ("Say it instead of writing it", [
     "Dictation and voice memos capture far faster than typing, and speed is the whole point at the moment something is said.",
     "Especially useful for names and for anything you are catching as you walk away.",
   ]),
   ("Review once, weekly, briefly", [
     "Fifteen minutes, once a week, to pull anything owed into your actual task list. Not to tidy, not to re-file.",
     "If you skip it, the capture still worked. That is the test of a system that fits: it fails gracefully.",
   ]),
 ],
 "faq": [
   ("Which app?", "Whichever one is already on your phone and opens fastest. The app is not the variable — reducing friction at capture is."),
   ("Handwriting or typing?", "Handwriting helps recall and is slower. In meetings the speed usually matters more; for thinking, paper is often better."),
   ("What about AI meeting recorders?", "They solve capture completely and create a new problem: hours of transcript nobody reads. Still write the four lines."),
 ],
 "related": ["adhd-at-work", "adhd-in-meetings", "dyslexia-and-note-taking"],
},
{
 "slug": "adhd-time-blindness-at-work",
 "hub": "adhd-at-work",
 "h1": "Time blindness at work",
 "title": "ADHD Time Blindness at Work",
 "desc": "Being late, underestimating everything, and losing an afternoon. What to change when your sense of elapsed time is not reliable.",
 "answer": "Stop estimating and start measuring. <strong>Time your normal tasks once, write the real numbers down, and quote those instead of your instinct</strong> — which is reliably optimistic. Then set alarms for departures, not for deadlines.",
 "sections": [
   ("Your estimate is not the problem to fix", [
     "The instinct will keep being wrong, and trying harder to estimate accurately does not work. What works is replacing the estimate with a measurement.",
     "Time four or five things you do often. Write the numbers where you will see them. Use those.",
   ]),
   ("Alarm the departure, not the deadline", [
     "A calendar reminder at the meeting time is useless. The useful alarm is the one that says leave now, and it needs to account for the getting-ready that always takes longer.",
     "Two alarms: one to stop what you are doing, one to actually go.",
   ]),
   ("Make elapsed time visible", [
     "A clock you can see, or a timer counting down in view. The problem is not caring about time, it is that time passes without registering.",
     "An analogue clock works better than a digital one for many people, because the movement shows the passing rather than stating it.",
   ]),
   ("Buffer as a rule, not a feeling", [
     "Add fifty percent to anything you have not measured, and say the padded number out loud when you commit.",
     "Delivering early is a reputation. Apologizing for late is also a reputation, and it is the expensive one.",
   ]),
   ("Ask for the deadline that is real", [
     "\"Is Friday the real deadline or the comfortable one?\" is a normal question, and the answer changes how you plan.",
   ]),
 ],
 "faq": [
   ("Does this get better with practice?", "The measurement approach gets easier. The underlying sense of elapsed time is not something people report improving much, which is exactly why the fix is external."),
   ("What about being late to everything socially?", "Same fix — alarm the departure, not the event. And tell people, because a friend who knows will pick a meeting point rather than a time."),
   ("Is asking for deadlines annoying?", "Asking once, clearly, is much less annoying than missing one. Most managers prefer the question."),
 ],
 "related": ["adhd-at-work", "adhd-remote-work", "adhd-in-meetings"],
},
{
 "slug": "adhd-and-email-at-work",
 "hub": "adhd-at-work",
 "h1": "Email with ADHD",
 "title": "Email With ADHD",
 "desc": "Read it, meant to reply, three weeks gone. Why that happens and the two rules that stop it.",
 "answer": "The problem is not volume, it is the gap between reading and replying. <strong>Never open an email you cannot deal with now.</strong> Reading marks it as handled in your head while leaving it undone in the world, and that gap is where the three weeks go.",
 "sections": [
   ("Why read-and-not-reply is the whole failure", [
     "Opening it gives you the sense of having dealt with it. The task closes internally and stays open externally.",
     "By the time you notice, replying is socially expensive — now you also have to explain the delay, which makes it even easier to keep not doing.",
   ]),
   ("Two rules", [
     "<strong>Do not open it unless you can act.</strong> Scanning the inbox is fine; opening is a commitment.",
     "<strong>If it takes under two minutes, do it now.</strong> Anything else goes on your actual task list in the same movement, not \"later\".",
   ]),
   ("Reply badly rather than not at all", [
     "\"Got this — will come back to you Thursday\" takes eight seconds and buys a week. It also removes the shame that makes the real reply harder.",
     "A short imperfect reply on Tuesday beats a considered one that never gets sent.",
   ]),
   ("The late one", [
     "Name the gap in half a sentence and move on. \"Sorry for the slow reply\" is enough; three lines about how busy you have been makes your delay the subject.",
   ]),
   ("Fixing the inbox itself", [
     "Turn off notifications and check at fixed times. An inbox that interrupts converts every email into an interruption and a half-formed intention.",
   ]),
 ],
 "faq": [
   ("Should I use folders?", "One archive and search. Filing is a decision at exactly the moment you are least able to make one."),
   ("What about inbox zero?", "It is a system to maintain, so treat it as optional. The two rules above deliver most of the benefit and survive a bad week."),
   ("I have hundreds of unread.", "Archive everything older than a month. If it mattered, it will come back. Starting from zero is worth more than the few things you lose."),
 ],
 "related": ["adhd-at-work", "writing-emails-with-dyslexia", "adhd-note-taking"],
},
{
 "slug": "telling-your-employer-you-have-adhd",
 "hub": "adhd-at-work",
 "h1": "Telling your employer you have ADHD",
 "title": "Should You Tell Your Employer You Have ADHD?",
 "desc": "What people actually weigh up, when they tend to do it, and the option most people miss — asking for the thing without the label.",
 "answer": "You can usually get what you need without disclosing. <strong>Ask for the adjustment, not the accommodation</strong> — \"send me that in writing\" and \"can we do this async\" are working preferences nobody questions. Disclose when you need something a preference cannot get you.",
 "sections": [
   ("This is not legal advice", [
     "What protection you have, and what an employer must do, depends entirely on your country and sometimes your contract. Nothing here is a statement about your rights.",
     "What follows is the decision people describe making, and how they tend to make it.",
   ]),
   ("The option most people miss", [
     "Most of what helps is a working preference, not a medical accommodation: written briefs, agendas in advance, a recorded meeting, a flexible start, a door that closes.",
     "All of those can be asked for plainly, and in most teams they are granted without anyone asking why.",
   ]),
   ("When disclosing is the way", [
     "When you need something a preference cannot reach — a formal adjustment, a change to how you are assessed, or protection you have to be on record to have.",
     "Also when not saying it is costing you more than saying it would. Some people find the concealment more tiring than the reaction.",
   ]),
   ("Who to tell, and when", [
     "People commonly tell a manager they already trust rather than HR first, and commonly after an offer rather than during hiring.",
     "You can also tell one person and not the team. Disclosure is not all-or-nothing and it does not have to be permanent in scope.",
   ]),
   ("How to say it", [
     "Short, forward-looking, with the thing you want attached: \"I have ADHD. The practical effect is I lose detail in long verbal briefs, so written ones work much better for me.\"",
     "Naming the effect and the fix in the same sentence is what turns it from a disclosure into a request.",
   ]),
 ],
 "faq": [
   ("Will it be held against me?", "Some people report it going well and some do not, and the difference is usually the manager rather than the company. That is worth weighing honestly rather than optimistically."),
   ("Do I have to tell them?", "In most places, no, unless it affects safety-critical work. The specifics depend on your country — check a local source rather than this page."),
   ("What if I already struggled before telling them?", "Naming it alongside what you are doing about it reframes the past rather than excusing it, and that is usually how it lands."),
 ],
 "related": ["adhd-at-work", "adhd-accommodations-at-work", "telling-your-employer-you-have-dyslexia"],
},
{
 "slug": "adhd-accommodations-at-work",
 "hub": "adhd-at-work",
 "h1": "Asking for what you need at work with ADHD",
 "title": "ADHD Accommodations at Work",
 "desc": "The adjustments people actually ask for, how to phrase the request so it gets a yes, and what to do if it does not.",
 "answer": "Ask for one specific thing, tied to a result. <strong>\"Written briefs instead of verbal ones — I will turn work around faster\"</strong> gets a yes far more often than a general request for support, because it tells your manager exactly what to do and what they get.",
 "sections": [
   ("The ones people actually ask for", [
     "Written briefs instead of verbal handovers, agendas sent in advance, meetings recorded, a flexible start time, and a quiet space or permission to work elsewhere for focused work.",
     "Deadlines stated as real or soft. Fewer, longer blocks instead of a fragmented calendar. Noise-canceling headphones as normal rather than antisocial.",
   ]),
   ("Phrase it as a trade", [
     "One thing, specific, with the benefit attached. \"If I get the brief in writing I can start the same day\" is a business case, not a favour.",
     "A list of five reads as a problem. One request reads as someone managing themselves well.",
   ]),
   ("You do not have to say why", [
     "Most of these are ordinary working preferences. \"That works much better for me\" is a complete justification and almost nobody pushes past it.",
   ]),
   ("Put it in writing afterwards", [
     "A one-line email confirming what was agreed. It makes it real, it survives your manager changing, and it costs nothing.",
   ]),
   ("If the answer is no", [
     "Ask what would make it possible, and ask for a trial rather than a permanent change. \"Could we try it for a month?\" converts a refusal into an experiment surprisingly often.",
     "If it stays no and the thing genuinely matters, that is information about the job rather than about you.",
   ]),
 ],
 "faq": [
   ("Do I need a diagnosis to ask?", "Not for a working preference. For a formal adjustment the answer depends on your country and employer — check a local source."),
   ("Should I go to HR or my manager?", "Most people start with the manager if the relationship is good, because it stays practical. HR makes it a process, which is what you want only if you need it on record."),
   ("What if I have not been performing well?", "Bring the request and the fix together. Asking for what would help, with a plan, is a much stronger position than waiting to be managed."),
 ],
 "related": ["adhd-at-work", "telling-your-employer-you-have-adhd", "asking-for-accommodations-at-work"],
},
]

PAGES += [
{
 "slug": "dyslexia-at-work",
 "hub": None,
 "h1": "Dyslexia at work",
 "title": "Dyslexia at Work",
 "desc": "Reading under time pressure, writing in public, and being asked to read something out. The practical fixes, and how to ask for them without a long explanation.",
 "answer": "Almost every hard moment at work with dyslexia is <strong>reading or writing in front of other people, at speed</strong>. Remove the speed and the audience and most of it goes. Ask for things in advance, write in a draft nobody sees, and decline to read aloud cold.",
 "sections": [
   ("It is the live part, not the reading", [
     "Given time and no audience, most of this is manageable. The cost lands when a document arrives in a meeting, or a message has to go now, or someone hands you a page to read out.",
     "So the fixes are about changing the conditions rather than getting faster.",
   ]),
   ("Ask for things in advance", [
     "\"Can you send that before the meeting?\" is the highest-value sentence on this page, and it is a completely ordinary request that improves meetings for everyone.",
     "Nobody asks why. Plenty of people without dyslexia ask the same thing.",
   ]),
   ("Write in private, send in public", [
     "Draft in a document, not in the message box. Read it back with text-to-speech, which catches the wrong-word errors a spellchecker cannot.",
     "Then paste and send. The speed people see is the speed of pasting.",
   ]),
   ("You can decline to read aloud", [
     "\"I would rather not read it cold — can you summarize it?\" ends the request and nobody investigates.",
     "If you want to read it, ask for a minute first. \"Give me a second with this\" is normal.",
   ]),
   ("The tools that actually earn their place", [
     "Text-to-speech for checking your own writing, dictation for capturing anything fast, and a font and spacing you can change. Those three cover most of it.",
   ]),
 ],
 "faq": [
   ("Should I tell my employer?", "There is a page here on that decision. Most of the fixes above work without telling anyone, which is worth knowing before you decide."),
   ("Does it get easier in a job you have done for years?", "Usually yes, because the vocabulary becomes familiar and you know what is coming. A new role resets that, and it is worth expecting rather than being surprised by."),
   ("Is AI writing help cheating?", "No more than a spellchecker. The judgement about what to say is still yours, and that is the part the job is paying for."),
 ],
 "related": ["dyslexia-email-signature", "reading-out-loud-at-work", "networking-with-dyslexia"],
},
{
 "slug": "dyslexia-email-signature",
 "hub": "dyslexia-at-work",
 "h1": "The dyslexia line in an email signature",
 "title": "Dyslexia Email Signature — Should You Add One?",
 "desc": "What the line is for, four versions people actually use, and the honest case against having one at all.",
 "answer": "It is one line under your name saying you are dyslexic, so a typo is read as a typo rather than carelessness. <strong>It works best when it is short and matter-of-fact</strong> — a long apology invites the judgement it was meant to prevent.",
 "sections": [
   ("What it is actually doing", [
     "It changes how an error is interpreted. Without it, a wrong word reads as sloppy; with it, it reads as a known thing about how you write.",
     "It also means you do not re-read a short message six times before sending, which is the larger daily saving for most people.",
   ]),
   ("Four versions people use", [
     "<strong>Plain.</strong> \"I am dyslexic. Please excuse any typos.\"",
     "<strong>Shorter.</strong> \"Dyslexic — apologies for any typos.\"",
     "<strong>Confident.</strong> \"Sent with dyslexia. The ideas are sound, the spelling may not be.\"",
     "<strong>Neutral.</strong> \"I am dyslexic, so occasional typos get through. Happy to clarify anything.\"",
   ]),
   ("Keep it to one line", [
     "Two lines starts to read as a disclaimer, and a disclaimer invites the reader to start looking. One line is a fact stated once.",
     "Put it under your name and contact details, not above them.",
   ]),
   ("The case against", [
     "You are disclosing to everyone you email, permanently, including people you have not met. That is a real decision and it is not reversible for messages already sent.",
     "Some people find it changes how clients read them. Others find it removes a background anxiety entirely. Both are common and neither is wrong.",
     "A middle option: use it internally and not on external mail.",
   ]),
   ("If you would rather not", [
     "Draft in a document, use text-to-speech to read it back, then paste. That removes the errors rather than explaining them, and it discloses nothing.",
   ]),
 ],
 "faq": [
   ("Does it look unprofessional?", "Short and factual does not. The versions that read badly are the ones that apologize at length or sound defensive."),
   ("Should the company add it as standard?", "Some do, as an option in the signature template. That normalizes it far better than an individual adding it alone."),
   ("What about LinkedIn or a resume?", "Different decision — those are read by people deciding about you rather than corresponding with you. Most people who use the email line do not put it on a resume."),
 ],
 "related": ["dyslexia-at-work", "writing-emails-with-dyslexia", "telling-your-employer-you-have-dyslexia"],
},
{
 "slug": "reading-out-loud-at-work",
 "hub": "dyslexia-at-work",
 "h1": "Being asked to read something out loud",
 "title": "Reading Out Loud at Work With Dyslexia",
 "desc": "The round-the-table read, the slide you did not write, and the document handed to you in a meeting. What to say instead.",
 "answer": "You are allowed to decline, with no reason. <strong>\"I would rather not read it cold — can you summarize it?\"</strong> is a complete sentence and nobody follows up. If you want to read it, ask for a minute with it first, which is a normal request from anyone.",
 "sections": [
   ("Reading aloud is a separate skill", [
     "Reading to understand and reading aloud fluently are different tasks, and dyslexia affects the second far more. People who read perfectly well silently can find reading out loud genuinely hard.",
     "That is worth knowing because the usual internal explanation — that you are not understanding it — is often wrong.",
   ]),
   ("Three sentences that end it", [
     "\"I would rather not read it cold — could you summarize it?\"",
     "\"Give me a minute with this and I will come back to it.\"",
     "\"Could someone else take that one? I will pick up the next.\"",
   ]),
   ("The round-the-table read", [
     "If you can see it coming, count ahead to your paragraph and read it silently first. Most of the difficulty is the surprise.",
     "You can also volunteer to go first, which means reading the part you have already had time with.",
   ]),
   ("Presenting your own slides", [
     "Much easier, because you wrote them and you know what comes next. Notes in your own words beat notes copied from the deck.",
     "Practice out loud once. The second time through any text is dramatically easier than the first, which is the whole reason cold reading is the hard version.",
   ]),
   ("If it happens a lot", [
     "It is reasonable to say once, to the person who runs the meeting, that you would rather not be asked to read cold. Framed as a preference it is usually just accepted.",
   ]),
 ],
 "faq": [
   ("Will people think I cannot read?", "They will think you did not want to read aloud, which is a thing plenty of people without dyslexia also avoid. It is far less remarkable than it feels."),
   ("What if I stumble halfway through?", "Stop, say \"let me start that line again\", and carry on. Everyone stumbles reading aloud and the recovery is what is remembered."),
   ("Does text-to-speech help?", "For your own preparation, a lot — hearing it once makes reading it aloud much easier. It does not help in the moment."),
 ],
 "related": ["dyslexia-at-work", "presenting-at-work", "dyslexia-in-a-job-interview"],
},
{
 "slug": "writing-emails-with-dyslexia",
 "hub": "dyslexia-at-work",
 "h1": "Writing emails with dyslexia",
 "title": "Writing Emails With Dyslexia",
 "desc": "The draft-and-paste habit, why text-to-speech catches what spellcheck cannot, and how to stop re-reading a three-line message six times.",
 "answer": "Never write in the message box. <strong>Draft in a document, read it back with text-to-speech, then paste and send.</strong> Spellcheck cannot catch a correctly spelled wrong word — form, from, their, there — and hearing it aloud catches nearly all of them.",
 "sections": [
   ("Why text-to-speech is the one that matters", [
     "The errors that survive proofreading are real words in the wrong place. Your eye supplies the word you meant, every time you read it.",
     "Your ear does not. A sentence read aloud by a machine is the first time you hear what you actually wrote.",
   ]),
   ("Draft somewhere with no send button", [
     "The message box invites sending before it is finished, and it is where the accidental early send happens.",
     "A document also lets you change the font and spacing to whatever you read most easily, which most mail clients will not.",
   ]),
   ("Say it before you write it", [
     "Dictate the message as if you were talking to the person, then tidy. Getting the content out by speaking is much faster and the result usually reads warmer.",
   ]),
   ("Stop re-reading short messages", [
     "Two passes, then send. A third pass on a three-line message is anxiety, not proofreading, and it is a real daily cost.",
     "The signature line, if you use one, exists precisely so that this pass can stop.",
   ]),
   ("Long or important ones", [
     "Ask someone to read it. That is what colleagues are for and people are almost always glad to be asked.",
   ]),
 ],
 "faq": [
   ("Is it fine to use AI to rewrite my emails?", "Yes, with one caution: make sure it still sounds like you. An email that reads like a press release is its own problem."),
   ("Which reads better, a long or short email?", "Short, for everyone. That is a genuine advantage here — the habits that make dyslexic writing easier also make it easier to read."),
   ("What about instant messages, where speed matters?", "Lower the standard deliberately. Chat is speech in writing, and nobody is proofreading it."),
 ],
 "related": ["dyslexia-at-work", "dyslexia-email-signature", "adhd-and-email-at-work"],
},
{
 "slug": "dyslexia-and-note-taking",
 "hub": "dyslexia-at-work",
 "h1": "Taking notes with dyslexia",
 "title": "Note-Taking With Dyslexia",
 "desc": "Writing fast enough to keep up, spelling names you have only heard, and being able to read it back tomorrow.",
 "answer": "Do not write, capture. <strong>Dictation and voice memos remove spelling and speed from the problem entirely</strong>, and both are invisible in a meeting. Write the four things that matter afterwards, with time and a machine reading it back.",
 "sections": [
   ("The three separate problems", [
     "Keeping up in real time. Spelling a name you have only heard. Reading your own notes back a day later.",
     "Speed is the one people notice; the third is the one that actually costs you, because unreadable notes are the same as no notes.",
   ]),
   ("Capture by voice", [
     "A voice memo after a meeting, or dictation during one, gets everything at speaking speed with no spelling involved.",
     "Recording the meeting itself, where the culture allows, removes the problem completely — ask once and it is usually fine.",
   ]),
   ("Names you have only heard", [
     "Write it how it sounds and fix it later from the calendar invite or their email signature. A phonetic note you can act on beats a blank.",
     "Do not stall the meeting trying to get it right in the moment.",
   ]),
   ("Four things, written after", [
     "What was decided, what you owe, what you are owed, what is unclear. Written with time, not under pressure.",
     "Short deliberate notes are far more useful than a long transcript, and much easier to read back.",
   ]),
   ("Make them readable tomorrow", [
     "Type them rather than handwriting if you find your own handwriting hard to reread. Then have them read back to you once — errors that matter show up immediately.",
   ]),
 ],
 "faq": [
   ("Is recording a meeting rude?", "Ask, briefly, and almost nobody minds. \"Do you mind if I record so I do not miss anything?\" is usually welcomed."),
   ("Do AI meeting notes solve it?", "Largely, and they create a transcript nobody reads. Still write the four things."),
   ("What about handwriting for memory?", "It does help recall. If your handwriting is hard to reread, the trade is rarely worth it."),
 ],
 "related": ["dyslexia-at-work", "adhd-note-taking", "how-to-remember-who-you-met"],
},
{
 "slug": "dyslexia-in-a-job-interview",
 "hub": "dyslexia-at-work",
 "h1": "Job interviews with dyslexia",
 "title": "Job Interviews With Dyslexia",
 "desc": "Written tests, documents handed to you on the day, and whether to say anything. What to ask for in advance.",
 "answer": "Ask what the format is before the day, and ask for what you need then. <strong>\"Is there a written exercise, and can I see the brief in advance?\"</strong> is a normal question that removes almost every surprise a dyslexic candidate runs into.",
 "sections": [
   ("Ask about the format first", [
     "A single email to whoever arranged it: how long, who is there, and whether there is a written or timed element.",
     "Everything else on this page depends on knowing that, and almost nobody asks, so the information is just sitting there.",
   ]),
   ("What you can ask for", [
     "Extra time on a written exercise, the brief or the questions in advance, or a task done at home instead of on the clock.",
     "These are common requests and many employers have a standard process for them. Asking does not require naming a diagnosis, though naming one often makes it easier to grant.",
   ]),
   ("If a document appears on the day", [
     "\"Can I take a couple of minutes with this?\" is an entirely normal thing for any candidate to say, and it is usually granted.",
     "Read for the question being asked rather than reading it all. You are almost never expected to absorb every line.",
   ]),
   ("The interview itself is usually the easy part", [
     "It is spoken, and most people with dyslexia are fine there. Prepare it the way anyone should: six stories, said out loud once before the day.",
   ]),
   ("Whether to mention it", [
     "You are not obliged to, and what protection you have varies by country. Many people mention it only when asking for an adjustment, and only then.",
     "If you do, attach the fix: \"I am dyslexic, so I would work better with the brief in advance.\"",
   ]),
 ],
 "faq": [
   ("Will asking for extra time count against me?", "Requests go to a coordinator far more often than to the panel. Most candidates who ask report it being handled as routine admin."),
   ("What about online tests with a timer?", "That is exactly the case to ask about, and untimed or extended versions usually exist. Ask before you start it, not after."),
   ("Should it be on my resume?", "Most people do not put it there. A resume is for deciding whether to meet you; the adjustment conversation belongs later."),
 ],
 "related": ["dyslexia-at-work", "adhd-job-interview", "asking-for-interview-adjustments"],
},
{
 "slug": "telling-your-employer-you-have-dyslexia",
 "hub": "dyslexia-at-work",
 "h1": "Telling your employer you have dyslexia",
 "title": "Should You Tell Your Employer You Have Dyslexia?",
 "desc": "What people weigh up, when they tend to say it, and how to ask for what you need without disclosing at all.",
 "answer": "Most of what helps can be asked for as a working preference. <strong>\"Send it to me in advance\" and \"I would rather not read cold\" need no explanation.</strong> Disclose when you want something a preference cannot reach, or when not saying it costs more than saying it.",
 "sections": [
   ("This is not legal advice", [
     "What an employer must do, and what you are protected from, depends on your country and sometimes your contract. Nothing here is a statement about your rights.",
     "This is about the decision people describe making.",
   ]),
   ("Most of it does not require telling anyone", [
     "Documents in advance, not reading aloud cold, drafting before sending, extra time on written work — all ordinary requests, all commonly granted with no reason given.",
     "Work out what you actually need first. It is often smaller than the decision to disclose.",
   ]),
   ("When people do say it", [
     "When they want a formal adjustment, when a pattern needs explaining, or when the hiding has become the tiring part.",
     "Commonly after an offer rather than during hiring, and commonly to one manager rather than announced.",
   ]),
   ("How to say it", [
     "One sentence, with the practical effect and the fix: \"I am dyslexic. It means I read slowly under time pressure, so having documents in advance makes a real difference.\"",
     "That is a request, not a confession, and it usually gets a practical answer rather than an emotional one.",
   ]),
   ("The signature line is a version of this", [
     "Adding a line to your email signature discloses to everyone you write to, permanently. Some people find that freeing and some find it a decision they cannot take back. There is a separate page on it.",
   ]),
 ],
 "faq": [
   ("Do I have to tell them?", "In most places no, unless it affects safety-critical work. The specifics vary by country — check a local source rather than this page."),
   ("What if I was diagnosed as an adult?", "It changes nothing about how you ask. \"I am dyslexic\" needs no history attached and people rarely ask for one."),
   ("What if they react badly?", "It happens, and it is usually the individual rather than the organization. Having asked in writing means there is a record of what was requested."),
 ],
 "related": ["dyslexia-at-work", "dyslexia-accommodations-at-work", "telling-your-employer-you-have-adhd"],
},
{
 "slug": "dyslexia-accommodations-at-work",
 "hub": "dyslexia-at-work",
 "h1": "Asking for what you need at work with dyslexia",
 "title": "Dyslexia Adjustments at Work",
 "desc": "The adjustments people actually ask for, how to phrase one so it gets agreed, and what to do if it is refused.",
 "answer": "Ask for one specific thing with the benefit attached. <strong>\"Documents the day before — I will come to the meeting with the answer rather than reading in it\"</strong> gets agreed far more often than a general request, because it tells your manager what to do and what they get.",
 "sections": [
   ("What people ask for", [
     "Documents and agendas in advance, not being asked to read aloud without warning, extra time on written tasks, text-to-speech and dictation software, and a screen and font you can change.",
     "Instructions in writing rather than verbally, or verbally rather than in writing — people differ, and yours is the one that counts.",
   ]),
   ("One request, with the benefit", [
     "\"If I get the deck the day before, I will come with comments instead of reading it in the room.\" That is a business case and it is easy to say yes to.",
     "A list of six reads as a problem to manage. One reads as someone managing themselves.",
   ]),
   ("You usually do not have to say why", [
     "Most of these are preferences plenty of people have. \"That works much better for me\" is a complete answer and it is rarely questioned.",
   ]),
   ("Confirm it in writing", [
     "One line by email after the conversation. It survives a change of manager, and it means you are not renegotiating it in six months.",
   ]),
   ("If it is refused", [
     "Ask what would make it workable, and propose a trial rather than a permanent change. A month-long experiment gets agreed when a policy change does not.",
     "If it stays no on something that genuinely matters, that tells you about the job rather than about you.",
   ]),
 ],
 "faq": [
   ("Do I need a formal diagnosis?", "Not for a working preference. For a formal adjustment it depends on your country and employer — check a local source."),
   ("Is software expensive?", "Text-to-speech and dictation are built into every major operating system and cost nothing. Start there before asking for a budget."),
   ("What if my manager does not understand dyslexia?", "Do not explain dyslexia. Explain the specific thing you want and what it produces — that conversation does not require them to understand anything."),
 ],
 "related": ["dyslexia-at-work", "telling-your-employer-you-have-dyslexia", "adhd-accommodations-at-work"],
},
]

PAGES += [
{
 "slug": "social-anxiety-at-work",
 "hub": None,
 "h1": "Social anxiety at work",
 "title": "Social Anxiety at Work",
 "desc": "Meetings, work socials, the first day, the review. The moments that cost most in a working week, and what to do about each.",
 "answer": "Work is not one social situation, it is about eight of them, and they fail differently. <strong>Prepare the specific one you are dreading</strong> rather than trying to become a more confident person in general — that is the advice that never converts into anything you can do on Tuesday.",
 "sections": [
   ("The moments that actually cost", [
     "Speaking in a meeting, the work social you cannot skip again, your first day, a review, or a one-to-one where something has to be raised.",
     "Each has a different shape and a different fix, which is why general confidence advice slides off. There is a page here for each.",
   ]),
   ("Prepare the sentence, not the personality", [
     "The thing that reliably helps is having said the words out loud once before the moment. That is a small, specific action.",
     "\"Be more confident\" is an outcome, not an instruction, and treating it as advice is why people conclude the problem is them.",
   ]),
   ("Most of it is invisible", [
     "People overestimate how visible their own anxiety is. You feel your heart; they see a colleague talking.",
     "This one has been measured: in Savitsky and Gilovich's 2003 speech study (<em>Journal of Experimental Social Psychology</em>), speakers rated their nerves as far more visible than their audience did.",
   ]),
   ("Give the week edges", [
     "Decide in advance which social things you are doing and which you are not, instead of deciding in the moment every time.",
     "A week with two chosen commitments is far cheaper than a week of five undecided ones you spend energy avoiding.",
   ]),
   ("When it is more than preparation", [
     "If this is shaping what jobs you apply for or what you will agree to attend, that is worth taking to a professional. Haveo is a preparation tool and does not pretend to be treatment.",
   ]),
 ],
 "faq": [
   ("Will a new job fix it?", "It resets the specific fears and not the underlying pattern. Worth knowing before you conclude the job is the problem."),
   ("Should I tell my manager?", "You can ask for what helps without naming anything — an agenda in advance, a heads-up before being asked to speak. Start there."),
   ("Does it get better with exposure?", "The specific situations do, with repetition. The general feeling is less responsive, which is why preparing each one beats waiting to feel differently."),
 ],
 "related": ["speaking-up-in-meetings", "first-day-at-a-new-job", "networking-with-social-anxiety"],
},
{
 "slug": "speaking-up-in-meetings",
 "hub": "social-anxiety-at-work",
 "h1": "Speaking up in meetings",
 "title": "How to Speak Up in Meetings",
 "desc": "The gap that never comes, the point that gets said by someone else, and what to do in the first five minutes to make the rest possible.",
 "answer": "Say something in the first five minutes, however small. <strong>The longer you go without speaking, the higher the bar gets in your own head</strong> — by minute thirty it has to be brilliant. A question or an agreement early keeps the bar where it started.",
 "sections": [
   ("Why the bar rises", [
     "Speak at minute two and it is just talking. Speak at minute forty, having been silent, and it feels like an announcement that needs to justify the wait.",
     "Nobody else is tracking your silence. You are the only person in the room keeping that score, and it is the score that makes it harder.",
   ]),
   ("The cheap first contribution", [
     "\"Can I check I have understood — do you mean X?\" Asking a clarifying question is contributing, and it is the lowest-risk thing to say in any meeting.",
     "Agreeing out loud also counts: \"That matches what we saw last month.\" You do not have to introduce anything new.",
   ]),
   ("Write it down first", [
     "Write the sentence in your notes before saying it. It stops the mid-sentence collapse and it means the point survives if the moment passes.",
     "It also means you can send it afterwards if you never got in.",
   ]),
   ("When someone says your point", [
     "Say so, out loud. \"That is what I was going to say, and the bit I would add is...\" You keep the credit and it is a completely normal thing to say.",
     "Staying silent because it has been said is how people end up feeling invisible in meetings they contributed to.",
   ]),
   ("Ask for the agenda", [
     "The single highest-value request: knowing what is coming lets you prepare one sentence. Ask the organizer once and it usually becomes standard.",
   ]),
 ],
 "faq": [
   ("What if I get talked over?", "\"I had not quite finished\" is a complete sentence. It works far more often than people expect, and nobody thinks badly of it."),
   ("Are video meetings harder?", "Usually — the turn-taking cues are gone. Use the chat as a legitimate way to contribute, and say your name before speaking."),
   ("What if my idea is wrong?", "Most contributions in most meetings are partly wrong and it is not remembered. Being consistently silent is remembered."),
 ],
 "related": ["social-anxiety-at-work", "adhd-in-meetings", "video-call-anxiety"],
},
{
 "slug": "work-parties-and-socials",
 "hub": "social-anxiety-at-work",
 "h1": "Work socials you cannot skip again",
 "title": "Work Social Anxiety",
 "desc": "Drinks after work, the team night out, the thing you have declined twice. How to go for an hour and have it count.",
 "answer": "Go early, stay an hour, leave cleanly. <strong>Arriving at the start is much easier than walking into a room that is already loud and grouped</strong>, and an hour at the beginning counts as having been there far more than two hours at the end.",
 "sections": [
   ("Early is the whole trick", [
     "The first twenty minutes are the easy ones: few people, no formed groups, and conversations start because you are standing near someone.",
     "The version people dread — walking into a full loud room and having to break in — is the version you get by arriving late.",
   ]),
   ("An hour is a full attendance", [
     "Nobody audits the length. What registers is whether you came, and whether you spoke to anyone properly.",
     "Two real conversations and out is a better night than three hours near the wall, and it is the version you will agree to repeat.",
   ]),
   ("Have a job", [
     "Get the first round, help with the food, look after whoever is newest. A role removes the question of what to do with yourself and gives you a reason to move.",
     "Looking after a new colleague is the best one: it is genuinely useful and it is a conversation with a built-in subject.",
   ]),
   ("Leaving", [
     "\"I am going to head off — good to see you\" to whoever you are with. You do not need to find everyone, and you do not need a reason.",
     "Decide the time before you go rather than in the moment, which is how an hour becomes three and the whole thing becomes something to dread next time.",
   ]),
   ("Declining sometimes", [
     "You can skip things. The cost is only real if you skip all of them, because that does eventually get noticed. Pick the ones that matter and go to those properly.",
   ]),
 ],
 "faq": [
   ("Do I have to drink?", "No, and it is barely noticed now. Hold something — the glass answers the question before anyone asks it."),
   ("What if I have nothing to say to my colleagues?", "Ask about the thing they are working on, or the commute, or the weekend. Work socials run on ordinary small talk, not on wit."),
   ("Is it career-limiting to skip them?", "Skipping some, no. Skipping all of them tends to show up as being seen as distant, which is a slower cost but a real one."),
 ],
 "related": ["social-anxiety-at-work", "the-office-christmas-party", "team-lunches-and-work-food"],
},
{
 "slug": "the-office-christmas-party",
 "hub": "social-anxiety-at-work",
 "h1": "The office Christmas party",
 "title": "Office Christmas Party Anxiety",
 "desc": "The one work social with the most pressure attached. How long to stay, what to do about the drinking, and the morning after.",
 "answer": "Arrive on time, stay ninety minutes, leave before it turns. <strong>The part people regret is almost always the late part</strong> — and the part that counts socially is the first hour, when people are still having actual conversations.",
 "sections": [
   ("The first hour is the useful one", [
     "Early on it is a normal social event: people arrive, talk in small groups, and you can speak to someone properly.",
     "Later it becomes loud, drunk and hard to leave. Nothing that happens then improves how the night is remembered.",
   ]),
   ("Decide the exit before you arrive", [
     "A time, and ideally a reason that exists — a train, an early start, someone expecting you. Say it early in the evening so leaving is expected rather than announced.",
   ]),
   ("The drinking", [
     "This is the event where it gets hardest to manage, because rounds are bought and glasses are topped up. Holding a drink you are not finishing solves most of it.",
     "The people who regret the Christmas party are almost never the ones who left at ten.",
   ]),
   ("Who to talk to", [
     "Someone from another team you never normally speak to. It is the one useful thing these events do, it is a genuinely easy conversation, and it is the only part worth planning.",
   ]),
   ("The morning after", [
     "If you are replaying something you said, it is almost certainly smaller than it feels, and everyone else is doing the same about themselves.",
     "Turn up. Turning up normally is what ends it; staying away is what makes a small thing into a story.",
   ]),
 ],
 "faq": [
   ("Can I just not go?", "Once, yes, easily. It is the most noticed absence of the year, so if you are going to attend one thing, this is usually the efficient one to pick."),
   ("What if there are games or dancing?", "You can decline both without explanation and nobody follows up. Standing near it is enough to have participated."),
   ("Secret Santa?", "Do it — it is low effort and opting out is more conspicuous than joining in."),
 ],
 "related": ["work-parties-and-socials", "social-anxiety-at-work", "social-anxiety-after-a-networking-event"],
},
{
 "slug": "first-day-at-a-new-job",
 "hub": "social-anxiety-at-work",
 "h1": "The first day at a new job",
 "title": "First Day at a New Job — Anxiety",
 "desc": "Names you will not remember, lunch, and not knowing what you are supposed to be doing. What actually happens, so none of it is a surprise.",
 "answer": "Almost nothing is expected of you on day one. <strong>You are not being assessed, you are being set up</strong> — accounts, a laptop, a tour, some meetings you will not follow. Write down every name and do not try to be impressive.",
 "sections": [
   ("What actually happens", [
     "Paperwork, a laptop that does not work, accounts that are not ready, and being introduced to more people than anyone could retain.",
     "Some meetings you will not understand. That is normal on day one and normal in week three.",
   ]),
   ("Write every name down", [
     "Name, team, one detail, in your phone, all day. You will meet twenty people and remember three without this.",
     "Nobody minds. Everyone assumes you are taking notes, which you are.",
   ]),
   ("You are allowed to not know anything", [
     "\"I am completely new, can you explain what that team does?\" has an expiry date and it is the most useful sentence you have. Spend it.",
     "Writing down the acronyms and asking later is fine too.",
   ]),
   ("Lunch", [
     "The bit people dread most. Say yes to whatever is offered on the first day, even if you would rather not — it is the cheapest possible entry to the group.",
     "If nothing is offered, ask one person. \"Is there anywhere decent nearby?\" usually turns into them showing you.",
   ]),
   ("The first week is not the job", [
     "Feeling useless is the standard experience and it is not evidence about whether you can do it. Most people describe it lifting somewhere around week three.",
   ]),
 ],
 "faq": [
   ("What should I wear?", "Ask before the day — \"what do people usually wear?\" is a normal question to send your manager. It removes one whole decision."),
   ("What if I forget everyone's name?", "You will. Asking again in week one is completely expected and nobody counts it."),
   ("Should I stay late to look keen?", "No. Leaving at a normal time on day one sets the pattern you actually want, and nobody is noting your hours yet."),
 ],
 "related": ["social-anxiety-at-work", "when-you-forget-someones-name", "office-small-talk"],
},
{
 "slug": "video-call-anxiety",
 "hub": "social-anxiety-at-work",
 "h1": "Why video calls feel worse",
 "title": "Video Call Anxiety",
 "desc": "Seeing your own face, not knowing when to speak, and the silence that is not really silence. Four changes that help.",
 "answer": "Turn off self-view. <strong>Watching your own face for an hour is the single largest avoidable cost of a video call</strong>, and it is the one nobody thinks to change. No in-person meeting puts a mirror in front of you.",
 "sections": [
   ("Self-view is the main problem", [
     "You are monitoring your own expression continuously, on top of following the meeting. That is a second task running the entire time.",
     "Every major platform lets you hide it from your own screen while everyone else still sees you. It is the highest-value setting on this page.",
   ]),
   ("The turn-taking is genuinely broken", [
     "The small cues that tell you someone is about to finish are mostly gone, and the lag means you talk over each other.",
     "So it is not you being bad at it. Saying your name first — \"this is Sam, can I add something\" — works because it replaces a cue that is missing.",
   ]),
   ("Use the chat", [
     "It is a legitimate contribution, it is often read out by whoever is chairing, and it is a way to make a point when you cannot find the gap.",
     "Writing the point in chat also means it exists, whether or not you get to say it.",
   ]),
   ("Silence is not the same as in a room", [
     "Two seconds of silence on a call feels like ten and it is usually just the connection. Do not fill it with something you have not thought through.",
   ]),
   ("Cameras", [
     "You can ask whether camera-on is expected. Plenty of teams do not require it, and a whole day of back-to-back video is genuinely tiring for most people.",
   ]),
 ],
 "faq": [
   ("Is it rude to turn my camera off?", "It depends on the team. Ask once rather than guessing — the answer is often more relaxed than assumed."),
   ("Why am I more tired than after in-person meetings?", "More faces at close range, a mirror, and missing cues you are working to replace. It is a real effect and it is not a lack of stamina."),
   ("Should I look at the camera or the person?", "The camera reads as eye contact and the screen is where the information is. Most people switch and nobody notices either way."),
 ],
 "related": ["social-anxiety-at-work", "speaking-up-in-meetings", "video-interview-anxiety"],
},
]

PAGES += [
{
 "slug": "performance-review-anxiety",
 "hub": "social-anxiety-at-work",
 "h1": "The performance review",
 "title": "Performance Review Anxiety",
 "desc": "Being told what someone thinks of you, in a room, with a form. How to prepare so the conversation is not a surprise.",
 "answer": "Write your own version first. <strong>Most of the dread is not knowing what they will say</strong>, and the fastest way to remove it is to list what you did, what went badly, and what you want next — then send it before the meeting.",
 "sections": [
   ("The dread is the unknown, not the feedback", [
     "People are rarely upset by the feedback itself. They are braced for something worse than what arrives, for weeks beforehand.",
     "Anything that reduces the unknown reduces the cost, and most of that is available to you in advance.",
   ]),
   ("Write it before they do", [
     "Three lists: what you delivered, what did not go well and what you did about it, and what you want next.",
     "Naming your own weak spot first is the single strongest move in a review. It changes the meeting from an assessment into a conversation about a plan.",
   ]),
   ("Send it in advance", [
     "A short summary a few days before gives your manager the material to write from, and managers are usually grateful rather than annoyed.",
     "It also means nothing in the room is new to either of you, which is the whole goal.",
   ]),
   ("If something critical does land", [
     "\"Can you give me an example?\" is the right response, not a defensive one. A specific example is something you can act on; a general impression is not.",
     "You are also allowed to think about it: \"I want to sit with that and come back to you\" is a good answer.",
   ]),
   ("Ask for what you want out loud", [
     "The thing you want next — a project, a title, money — has to be said. Reviews are one of the few moments where asking is explicitly expected.",
   ]),
 ],
 "faq": [
   ("What if I disagree with the rating?", "Ask what specifically would have moved it, and get that in writing. Arguing the rating rarely changes it; the criteria for next time is the useful thing."),
   ("Should I bring notes?", "Yes, and visibly. It reads as preparation, and it means you do not lose your points when the conversation turns."),
   ("What if I have no idea what they think of me?", "That is a question to ask now rather than in the review. \"Is there anything you would want me doing differently?\" a month before removes most surprises."),
 ],
 "related": ["social-anxiety-at-work", "one-on-ones-with-your-manager", "imposter-syndrome-at-work"],
},
{
 "slug": "one-on-ones-with-your-manager",
 "hub": "social-anxiety-at-work",
 "h1": "One-to-ones with your manager",
 "title": "One-on-One Meeting Anxiety",
 "desc": "The recurring meeting with no agenda that you spend the morning dreading. What to put in it so it stops being an interrogation.",
 "answer": "Bring an agenda. <strong>A one-to-one with no agenda becomes a test you did not study for</strong> — they ask how things are going and you improvise. Three bullets sent the day before turns it into a working meeting you are running.",
 "sections": [
   ("Whoever brings the agenda runs the meeting", [
     "Without one, the shape defaults to your manager asking questions and you answering, which is the version that feels like an assessment.",
     "With one, you are reporting and asking. Same meeting, completely different experience, and it costs three bullets.",
   ]),
   ("What goes in it", [
     "What moved since last time, what is stuck, what you need a decision on. Three lines.",
     "\"What is stuck\" is the one people leave out, and it is the one that is actually the manager's job.",
   ]),
   ("Raising something difficult", [
     "Say it early in the meeting, not at minute twenty-five. Late-raised things get no time and you spend the whole meeting holding it.",
     "Lead with what you want: \"I want to talk about my workload and what we might drop.\"",
   ]),
   ("Silence is not a test", [
     "Managers often pause because they are thinking. Filling it is how people talk themselves into saying more than they meant.",
     "You can say \"that is all from me\" and let the meeting end early. Ending early is fine.",
   ]),
   ("If it keeps getting canceled", [
     "Say once that you would like it to happen. A repeatedly canceled one-to-one is a real problem and asking for it is completely reasonable.",
   ]),
 ],
 "faq": [
   ("What if I have nothing to report?", "Then report that and use it to ask something. \"Quiet fortnight — can I ask about the roadmap?\" is a perfectly good one-to-one."),
   ("Should I raise problems or look competent?", "Raise them. Unsurfaced problems become surprises, and a surprise is the thing managers genuinely mind."),
   ("Can I ask for feedback directly?", "Yes, specifically: \"is there anything you would want me doing differently?\" General requests get general answers."),
 ],
 "related": ["social-anxiety-at-work", "performance-review-anxiety", "speaking-up-in-meetings"],
},
{
 "slug": "team-lunches-and-work-food",
 "hub": "social-anxiety-at-work",
 "h1": "Team lunches and eating at work",
 "title": "Work Lunch Anxiety",
 "desc": "The group lunch, the kitchen at noon, and eating in front of people. Small, practical things that make it easier.",
 "answer": "Sit at a corner or an end, next to one person you can talk to. <strong>Most of the difficulty at a group lunch is the open middle of a long table</strong>, where you are visible to everyone and talking to nobody in particular.",
 "sections": [
   ("Where you sit decides the meal", [
     "An end or a corner means one or two neighbors and one conversation. The middle of a long table means being in everyone's view with no natural partner.",
     "Arrive slightly early so you get to choose rather than take what is left.",
   ]),
   ("One neighbor is the whole job", [
     "You are not required to entertain a table. A decent conversation with the person beside you is a completely successful lunch.",
   ]),
   ("Ordering", [
     "Decide before the waiter reaches you, and if you are unsure, order the same as someone else. It is a small decision that gets disproportionately stressful when it is your turn and everyone is listening.",
   ]),
   ("Eating in front of people", [
     "More common as a worry than people assume, and almost never noticed. Nobody at a work lunch is watching anyone else eat.",
     "Ordering something easy to manage removes the thought entirely, which is worth more than picking what you most wanted.",
   ]),
   ("The everyday kitchen version", [
     "The office kitchen at noon is its own small ordeal. Going slightly before or after the rush is a legitimate solution and not an avoidance to feel bad about.",
   ]),
 ],
 "faq": [
   ("Can I eat at my desk instead?", "Most days, yes. Doing it every single day is what gets read as distance, so pick a couple of lunches that matter and go to those."),
   ("What if I have dietary restrictions?", "Tell whoever books it, in advance and by message. It removes an on-the-spot conversation you would otherwise have in front of everyone."),
   ("What do people even talk about?", "Weekends, the commute, television, and the work everyone is already doing. It is genuinely ordinary."),
 ],
 "related": ["social-anxiety-at-work", "office-small-talk", "work-parties-and-socials"],
},
{
 "slug": "going-back-to-the-office",
 "hub": "social-anxiety-at-work",
 "h1": "Going back to the office",
 "title": "Return to Office Anxiety",
 "desc": "After remote work, the office is loud, social and full of small unwritten rules again. What to expect and what to ask for.",
 "answer": "Expect it to be tiring for a few weeks and plan around that rather than through it. <strong>The exhaustion is the social and sensory load returning all at once</strong>, not a sign you have lost the ability to do it.",
 "sections": [
   ("What actually changed", [
     "Noise, interruption, being visible all day, small talk on arrival, and no ability to step away without it being seen.",
     "None of those existed at home, and all of them return on the same morning. That is a genuine load, not a soft one.",
   ]),
   ("Plan the first weeks lightly", [
     "Do not schedule demanding evenings in the first fortnight back. The tiredness is real and predictable, and planning around it is the difference between adjusting and dreading it.",
   ]),
   ("Get your escape routes early", [
     "Find the quiet room, the stairwell, the walk around the block. Knowing where you can go changes the day even if you never go.",
     "A booked room for focused work is a normal request in most offices now.",
   ]),
   ("The arrival small talk", [
     "The first five minutes each morning are the bit people forget about. Two prepared lines — the weekend, the commute, whatever is on — carry it completely.",
   ]),
   ("Asking for a pattern", [
     "Which days, and whether they can be fixed, is a reasonable thing to ask about. Fixed days let you plan; random ones mean every week is renegotiated.",
   ]),
 ],
 "faq": [
   ("Is it normal to find it harder than before?", "Very. Most people report the same, and the comparison point has changed — you have had years of a quieter default."),
   ("Can I ask to stay remote?", "You can ask, with a reason tied to output. Whether it is granted depends on the employer, and asking does not cost you anything."),
   ("How long does the adjustment take?", "People commonly describe a few weeks. If it is still getting worse after a couple of months, that is worth taking seriously rather than pushing through."),
 ],
 "related": ["social-anxiety-at-work", "adhd-remote-work", "sensory-issues-in-an-office"],
},
{
 "slug": "imposter-syndrome-at-work",
 "hub": "social-anxiety-at-work",
 "h1": "Feeling like you do not belong at work",
 "title": "Imposter Syndrome at Work",
 "desc": "The sense that you got in by luck and will be found out. Why the usual reassurance does not land, and what actually shifts it.",
 "answer": "Reassurance does not work because the feeling reinterprets it — praise becomes politeness, success becomes luck. <strong>What shifts it is a written record of specific things you did</strong>, because a list is harder to argue with than a memory.",
 "sections": [
   ("Why being told you are good does not help", [
     "The feeling has an answer for every piece of evidence: praise was kindness, the project went well because the team was strong, the interview went well because the questions were easy.",
     "So more reassurance produces more reinterpretation. That is why it keeps not working, and it is not that people are not trying.",
   ]),
   ("Keep a written record", [
     "A running note: what you shipped, what you fixed, what someone thanked you for, with dates.",
     "Specific and dated is the format that resists reinterpretation. It is also exactly what you need at a review, so it pays twice.",
   ]),
   ("Separate the two questions", [
     "\"Do I feel competent\" and \"am I doing the job\" are different, and only the second one has evidence. Plenty of people do the second for years while answering no to the first.",
     "Deciding by the second question is the practical move, rather than waiting to feel different.",
   ]),
   ("Say it to one person", [
     "It is close to universal, and almost nobody says it out loud. Saying it to one colleague you trust usually produces \"oh, me too\" from someone you assumed was certain.",
   ]),
   ("New job, new role, new level", [
     "It spikes at every transition and that is expected rather than diagnostic. Being new at something is not the same as being unqualified for it.",
   ]),
 ],
 "faq": [
   ("Does it go away with seniority?", "Mostly it changes shape rather than leaving. People describe it getting quieter and more familiar rather than ending."),
   ("Should I tell my manager?", "You can ask for concrete feedback without framing it this way. \"What would you want me doing differently?\" gets you the evidence without the conversation."),
   ("Is it ever accurate?", "Occasionally you are genuinely new and under-skilled — and that is a learning plan, not a character verdict. The test is whether you can name the specific gap."),
 ],
 "related": ["social-anxiety-at-work", "performance-review-anxiety", "first-day-at-a-new-job"],
},
{
 "slug": "presenting-at-work",
 "hub": "social-anxiety-at-work",
 "h1": "Presenting at work",
 "title": "Presentation Anxiety at Work",
 "desc": "The internal presentation, the demo, the slot at the all-hands. What to rehearse, what to cut, and what to do in the first thirty seconds.",
 "answer": "Rehearse the first thirty seconds until they are automatic. <strong>Almost all of the difficulty is in the opening</strong> — once you are talking, the rest usually runs. A memorized first line means you never start by improvising.",
 "sections": [
   ("The opening is the hard part", [
     "The peak is the moment before and the first few sentences. After that most people find they settle, and knowing that in advance helps.",
     "So spend your preparation disproportionately on the start rather than spreading it evenly.",
   ]),
   ("Out loud, standing, twice", [
     "Reading slides silently is not rehearsal. Say it out loud, standing, at least twice — the second run is always dramatically better than the first, and you want the first one to happen in private.",
     "Time it. Everything runs longer live.",
   ]),
   ("Cut a third", [
     "Almost every internal presentation is too long. Cutting makes it better and it shortens the part you are dreading.",
     "One idea per slide, and no slide you would have to read out.",
   ]),
   ("Questions", [
     "Write the three questions you hope nobody asks and prepare those. They are the ones that will come.",
     "\"I do not know, I will find out and come back to you\" is a complete, professional answer and it is better than improvising something wrong.",
   ]),
   ("Notes are fine", [
     "Nobody minds notes. Bullet points in your own words work better than a script, which is hard to find your place in when your hands are shaking.",
   ]),
 ],
 "faq": [
   ("What if my voice shakes?", "It is far less audible than it feels. A pause and a slow breath resets it, and a pause reads as considered rather than nervous."),
   ("Should I stand or sit?", "Standing tends to make your voice carry and your breathing steadier. If the room is small and everyone is sitting, sit."),
   ("Is it worth practicing in front of someone?", "One friendly colleague once is worth several solo run-throughs, mainly because it surfaces which part is unclear."),
 ],
 "related": ["social-anxiety-at-work", "reading-out-loud-at-work", "speaking-up-in-meetings"],
},
]

PAGES += [
{
 "slug": "autistic-at-work",
 "hub": None,
 "h1": "Autistic at work",
 "title": "Being Autistic at Work",
 "desc": "The office, the unwritten rules, the social parts nobody scheduled. What costs most in a working week and what can be changed.",
 "answer": "The job is usually not the hard part. <strong>The cost is the environment and the unscheduled social layer around the work</strong> — open plan noise, the small talk, the meeting with no agenda. Those are changeable, and more of them than people expect.",
 "sections": [
   ("What costs, and what does not", [
     "The work itself is often the part that goes well, and that is worth saying because the exhaustion gets misread as not coping with the job.",
     "The cost is the noise, the lighting, the interruption, the arrival small talk, and the meetings whose shape is never stated.",
   ]),
   ("Ask for the shape of things", [
     "Agendas in advance, written briefs, being told what a meeting is for, and what decision is being made and by whom.",
     "These read as good practice rather than accommodations, so they are almost always granted, and they help everybody in the room.",
   ]),
   ("The environment is negotiable", [
     "A desk away from the walkway, a booked room for focused work, headphones as normal, or a day at home for anything that needs sustained attention.",
     "Most offices will agree to these if asked specifically and one at a time.",
   ]),
   ("The social layer", [
     "Arrival small talk, lunch, the after-work thing. Doing some of it deliberately costs less than avoiding all of it, because avoiding all of it is what gets read as distance.",
     "Pick which ones and go to those properly. There are pages here on each.",
   ]),
   ("Recovery is part of the week", [
     "If a work event costs you the next morning, plan for that rather than being surprised by it. Treating the recovery as part of the commitment is what makes it sustainable.",
   ]),
 ],
 "faq": [
   ("Should I tell my employer?", "There is a page here on that decision. Almost everything above can be asked for without disclosing anything."),
   ("Is remote work better?", "Often, for the sensory and interruption part. It removes the incidental contact too, which some people miss — worth deciding deliberately rather than by default."),
   ("What if I am doing the work well and still struggling?", "That is the common pattern rather than a contradiction. It is usually the environment, and the environment is the thing with levers on it."),
 ],
 "related": ["asking-for-accommodations-at-work", "sensory-issues-in-an-office", "autistic-networking-events"],
},
{
 "slug": "autistic-burnout-after-work-events",
 "hub": "autistic-at-work",
 "h1": "The day after a work event",
 "title": "Recovering After a Work Event",
 "desc": "Why a two-hour event costs the next day, how to plan for it, and what actually helps the recovery.",
 "answer": "Treat the recovery as part of the event, not as a failure afterwards. <strong>A two-hour work social can cost the following morning</strong>, and planning for that is the difference between it being manageable and it being something you cancel.",
 "sections": [
   ("Why two hours costs a day", [
     "The event is not just conversation. It is noise, lighting, movement, continuous social processing, and holding a version of yourself steady for the whole time.",
     "All of that runs at once and none of it stops when you leave. The bill arrives later, which is why it gets misread as unrelated.",
   ]),
   ("Plan the day after, before the event", [
     "Nothing demanding the next morning. No early meeting you would have to perform in. If you can, a later start.",
     "This is the single most effective thing on the page and it has to be done in advance, because afterwards you have no capacity to rearrange anything.",
   ]),
   ("Shorten the event instead of enduring it", [
     "Ninety minutes deliberately costs far less than four hours endured. Decide the end time before you go and say it early so leaving is expected.",
   ]),
   ("What the recovery actually needs", [
     "Quiet and low input, usually more than sleep. People commonly describe needing an evening with nothing in it rather than an early night.",
     "Reducing decisions helps too — food already in the house, nothing to arrange.",
   ]),
   ("When it is not recovering", [
     "If it is taking longer each time, or the recovery is not happening, that is worth taking to a professional. This page is about planning a week, not about diagnosis or treatment.",
   ]),
 ],
 "faq": [
   ("Is this just being tired?", "It behaves differently — it is disproportionate to the hours, and rest does not resolve it the way ordinary tiredness does. Naming it accurately makes it easier to plan around."),
   ("Should I skip work events entirely?", "Skipping all of them has its own cost over time. Fewer events, deliberately chosen, with recovery planned, is the trade most people land on."),
   ("Can I tell my employer this is why?", "You can ask for a later start after an evening event without explaining anything. That gets you most of the benefit with none of the disclosure."),
 ],
 "related": ["autistic-at-work", "sensory-issues-in-an-office", "masking-at-work-events"],
},
{
 "slug": "asking-for-accommodations-at-work",
 "hub": "autistic-at-work",
 "h1": "Asking for what you need at work",
 "title": "Asking for Accommodations at Work",
 "desc": "How to make one request that gets agreed, what people actually ask for, and what to do when the answer is no.",
 "answer": "One thing, specific, with the result attached. <strong>\"An agenda before each meeting — I will come with the answers instead of forming them live\"</strong> is easy to say yes to. A general request for support gives a manager nothing to act on.",
 "sections": [
   ("This is not legal advice", [
     "What an employer is required to do depends on your country and your contract. Nothing here is a statement about your rights.",
     "This is about how to make a request land.",
   ]),
   ("What people actually ask for", [
     "Agendas and documents in advance, written briefs, a quieter desk, permission to wear headphones, a booked room for focused work, flexible hours, notice before being put on the spot.",
     "Almost all of these are ordinary working preferences that plenty of people request without any label attached.",
   ]),
   ("One at a time, with the benefit", [
     "A list reads as a problem to solve. One request with a clear payoff reads as someone who knows how they work.",
     "Get the first one agreed, let it become normal, then ask for the next.",
   ]),
   ("Put it in writing after", [
     "A one-line confirmation email. It survives a change of manager and means you are not renegotiating in six months.",
   ]),
   ("If the answer is no", [
     "Ask what would make it possible, and offer a trial. \"Could we try it for a month and see?\" gets agreed far more often than a permanent change.",
     "If it stays no on something that genuinely matters, that is information about this job rather than about you.",
   ]),
 ],
 "faq": [
   ("Do I need a diagnosis?", "Not for a working preference. For a formal adjustment it depends on your country and employer — check a local source."),
   ("Manager or HR?", "Manager first if the relationship is decent, because it stays practical. HR makes it a process, which you want only when you need it on record."),
   ("What if I have asked before and nothing happened?", "Put it in writing this time, with one specific thing and a date. Verbal requests are the ones that evaporate."),
 ],
 "related": ["autistic-at-work", "adhd-accommodations-at-work", "dyslexia-accommodations-at-work"],
},
{
 "slug": "sensory-issues-in-an-office",
 "hub": "autistic-at-work",
 "h1": "Open-plan offices, noise and light",
 "title": "Sensory Issues in an Office",
 "desc": "Noise you cannot turn off, lighting you did not choose, and a desk in a walkway. What can actually be changed, and how to ask.",
 "answer": "Most of it is changeable and almost nobody asks. <strong>Where your desk is, what you can wear on your ears, and where you can go to work quietly</strong> are the three biggest levers, and all three are ordinary requests in most offices.",
 "sections": [
   ("Where your desk is", [
     "Away from the walkway, the kitchen, the printer and the busiest team. Backing onto a wall rather than an open room.",
     "Desk moves are usually the easiest thing to get agreed and the most underused. Ask the person who owns the floor plan, not HR.",
   ]),
   ("Noise", [
     "Noise-canceling headphones are normal office equipment now. Filtered earplugs are a quieter option if headphones read as unavailable in your team.",
     "If headphones are discouraged, that is worth asking about directly — many such rules turn out to be assumed rather than actual.",
   ]),
   ("Light", [
     "Overhead fluorescent is the common complaint and it is often adjustable — a desk lamp with the overhead off above your area, or a seat away from the brightest zone.",
     "Screen brightness and a warmer color temperature are free and help more than people expect.",
   ]),
   ("Somewhere to go", [
     "One bookable room, or a known quiet corner, for anything needing sustained attention. Knowing it exists changes the day even on days you do not use it.",
   ]),
   ("Ask for one thing at a time", [
     "Each of these on its own is a small, reasonable request. All of them at once reads as a list of problems, which is a harder conversation for no extra benefit.",
   ]),
 ],
 "faq": [
   ("Do I need to explain why?", "\"I focus much better away from the walkway\" is a complete reason and it is rarely questioned."),
   ("What about hot-desking?", "Ask whether you can book the same desk regularly. Many systems allow it and few people realize."),
   ("Is it reasonable to ask to work from home for focused work?", "Very common now, and easiest to get agreed for specific tasks rather than as a general pattern."),
 ],
 "related": ["autistic-at-work", "going-back-to-the-office", "sensory-overload-at-events"],
},
{
 "slug": "office-small-talk",
 "hub": "autistic-at-work",
 "h1": "Small talk in the office",
 "title": "Office Small Talk",
 "desc": "The five minutes on arrival, the kitchen, the elevator. What it is for, and the lines that carry it without effort.",
 "answer": "It is not an exchange of information, which is why it reads as pointless. <strong>It is a low-cost signal that things between you are fine.</strong> Two prepared lines cover almost every instance of it, and it does not need to be interesting.",
 "sections": [
   ("What it is actually doing", [
     "Confirming the relationship is normal. That is the entire function, and it is why the content does not matter and nobody remembers it.",
     "Once you stop trying to make it interesting, it gets much cheaper to produce.",
   ]),
   ("Two lines carry the week", [
     "Something about the day — the weather, the commute, how busy it is. Something about them — their weekend, their project, something they mentioned last time.",
     "That is it. You are not expected to be entertaining and nobody is assessing the material.",
   ]),
   ("The moments it happens", [
     "Arrival, the kitchen, the elevator, the two minutes before a meeting starts. Knowing the list means none of them is a surprise.",
     "The pre-meeting two minutes is the one worth preparing, because it happens with an audience.",
   ]),
   ("Ending it is allowed", [
     "\"Right, I had better get on\" ends any of these and nobody minds. Small talk is designed to be short and stopping it is not rude.",
   ]),
   ("You can skip some of it", [
     "Headphones on at your desk is a recognized signal in most offices. Using it some of the time is normal; using it all of the time is what gets read as distance.",
   ]),
 ],
 "faq": [
   ("What if I genuinely have nothing to say?", "Ask them something. A question you asked counts fully, and it moves the talking to them."),
   ("Do I have to remember what they told me?", "It helps a lot and it is exactly what a note is for. One line about a colleague is not strange to keep."),
   ("Is it okay to be bad at it?", "Almost everyone is. Being consistently pleasant and brief is read as perfectly normal — it is silence that gets interpreted."),
 ],
 "related": ["autistic-at-work", "team-lunches-and-work-food", "small-talk-questions-that-arent-boring"],
},
{
 "slug": "telling-your-employer-you-are-autistic",
 "hub": "autistic-at-work",
 "h1": "Telling your employer you are autistic",
 "title": "Should You Tell Your Employer You Are Autistic?",
 "desc": "What people weigh up, when they tend to do it, and why most of what helps can be asked for without saying anything.",
 "answer": "Work out what you need first — it is usually smaller than the decision to disclose. <strong>Agendas, a quieter desk, headphones and written briefs are all ordinary requests</strong> that need no explanation. Disclose when you need something those cannot reach.",
 "sections": [
   ("This is not legal advice", [
     "Protection and obligation vary by country and sometimes by contract. Nothing here is a statement about your rights — check a local source for that.",
     "This is about the decision as people describe making it.",
   ]),
   ("Separate the need from the label", [
     "List what would actually make the week easier. Most of it will be environment and information: where you sit, what you can wear, knowing what a meeting is for.",
     "Nearly all of that is grantable as a preference. The label is only required when the thing you need is formal.",
   ]),
   ("Reasons people do disclose", [
     "To get a formal adjustment. To explain a pattern rather than have it interpreted. Because concealing it has become the expensive part.",
     "That last one is real and underrated — for some people the masking costs more than any reaction would.",
   ]),
   ("Who, and when", [
     "Commonly one trusted manager rather than HR or the team, and commonly after an offer rather than during hiring. It does not have to be everyone and it does not have to be permanent in scope.",
   ]),
   ("How to say it", [
     "Short, with the practical effect and what helps: \"I am autistic. In practice that means unstructured meetings are hard for me to contribute in, so an agenda beforehand makes a real difference.\"",
     "That is a request. It tends to get a practical response rather than an emotional one.",
   ]),
 ],
 "faq": [
   ("Will it change how I am treated?", "Reports vary widely and it usually comes down to the individual manager rather than the company. Weigh that honestly against what you gain."),
   ("Do I have to tell them?", "In most places no. The specifics depend on your country — check a local source rather than this page."),
   ("What if I am self-identified rather than diagnosed?", "For working preferences it makes no difference. For formal adjustments it may — that varies by country and employer."),
 ],
 "related": ["autistic-at-work", "asking-for-accommodations-at-work", "telling-your-employer-you-have-adhd"],
},
{
 "slug": "job-interviews",
 "hub": None,
 "h1": "Job interviews when they make you anxious",
 "title": "Job Interview Anxiety",
 "desc": "What to prepare, what you are allowed to ask for, and what actually happens in the room. For anxious, ADHD, autistic and dyslexic candidates.",
 "answer": "Prepare six stories, not thirty answers. <strong>Almost every behavioral question is one of six stories wearing a different hat</strong>, and six is a number you can actually rehearse out loud. That is what stops the rambling and the blank.",
 "sections": [
   ("Six stories", [
     "Something you shipped, something that went wrong, a disagreement, something you learned fast, something you are proud of, and why this job.",
     "Rehearse those six out loud. Thirty prepared answers is why people give up on preparing at all.",
   ]),
   ("Ask what the format is", [
     "How long, who is in the room, and whether there is a written or timed element. One email to whoever arranged it.",
     "Almost nobody asks, the answer is freely given, and it removes most of what people find hard about interview day.",
   ]),
   ("You can ask for adjustments", [
     "Questions in advance, extra time on a written task, a take-home instead of a timed exercise, or a break between stages.",
     "These are common requests handled by a coordinator rather than the panel, and they do not have to come with a diagnosis attached.",
   ]),
   ("When you lose the question", [
     "Ask for it again. \"Could you repeat that?\" and \"let me think for a second\" are both completely ordinary and neither is marked against you.",
   ]),
   ("The day before", [
     "Say your stories out loud once. Check the route or the link. Then stop — more preparation the night before raises the stakes rather than the readiness.",
   ]),
 ],
 "faq": [
   ("Should I disclose anything?", "You are not obliged to and protections vary by country. Most people who do it wait until they have an offer, or mention it only when asking for an adjustment."),
   ("What if I go blank completely?", "Say so: \"I have gone blank — can I come back to that?\" Interviewers almost always say yes and it is remembered far less than you would think."),
   ("How much research is enough?", "What they do, one recent thing they did, and one genuine question. More than that rarely shows up in the conversation."),
 ],
 "related": ["adhd-job-interview", "social-anxiety-in-interviews", "dyslexia-in-a-job-interview"],
},
{
 "slug": "social-anxiety-in-interviews",
 "hub": "job-interviews",
 "h1": "Interviews with social anxiety",
 "title": "Job Interviews With Social Anxiety",
 "desc": "The shaking voice, the blank, and the small talk on the way to the room. What to prepare and what not to worry about.",
 "answer": "Prepare the first two minutes hardest. <strong>The peak is arriving, the greeting and the opening question</strong> — after that most people settle. Rehearsing the walk-in and your answer to \"tell me about yourself\" covers the worst of it.",
 "sections": [
   ("The peak is at the start", [
     "The corridor, the handshake, the small talk on the way, and the first question. That is where it is hardest, and it passes.",
     "Knowing the shape of it in advance is itself useful: you are not bracing for the whole hour, only the first part of it.",
   ]),
   ("Rehearse the walk-in", [
     "Your name, a normal greeting, and one line of small talk you have already decided on. Say it out loud before the day.",
     "It sounds excessive and it removes the exact moment most people describe as the worst.",
   ]),
   ("\"Tell me about yourself\"", [
     "Almost always first, and therefore the one to have automatic. Sixty to ninety seconds: what you do now, one thing you did that is relevant, why you are here.",
     "Having a rehearsed opening means you start speaking without improvising, which changes the whole rest of the conversation.",
   ]),
   ("Your voice and your hands", [
     "A shaking voice is far less audible than it feels, and interviewers are not marking it. A pause and a slow breath resets it.",
     "Something to hold — water, a notebook — solves the hands and gives you a legitimate pause any time you want one.",
   ]),
   ("What they are actually deciding", [
     "Whether you can do the job and whether working with you would be fine. Not whether you were relaxed.",
     "Plenty of visibly nervous people get offers. Nerves in an interview are the most expected thing in the room.",
   ]),
 ],
 "faq": [
   ("Should I mention that I am nervous?", "A light \"sorry, I am a bit nervous\" early often helps — it is disarming and it stops you managing it silently. A long explanation does not."),
   ("Are panel interviews worse?", "For most people yes. Ask who will be there beforehand and write the names down as you arrive."),
   ("What about the small talk walking to the room?", "Prepare one line about the building, the journey or the weather. It is thirty seconds and it is the part nobody rehearses."),
 ],
 "related": ["job-interviews", "video-interview-anxiety", "the-day-before-an-interview"],
},
{
 "slug": "video-interview-anxiety",
 "hub": "job-interviews",
 "h1": "Video interviews",
 "title": "Video Interview Anxiety",
 "desc": "Self-view, lag, and the one-way recorded interview. What to set up beforehand and what to do when nobody reacts.",
 "answer": "Turn off self-view and put your notes behind the camera. <strong>Watching your own face while being interviewed is a second task running the whole time</strong>, and it is the one thing a video interview adds that a real room does not.",
 "sections": [
   ("Self-view first", [
     "Hide it from your own screen. Every platform allows it, they still see you, and it removes continuous self-monitoring at the worst possible moment.",
   ]),
   ("Notes go behind the camera", [
     "Sticky notes around the lens, or a document just below it. Your six story titles and three questions — headings, not scripts.",
     "Reading a script is visible. Glancing at four words is not.",
   ]),
   ("Nobody reacting is not a bad sign", [
     "Video flattens the nodding and the small encouragements you would get in a room, so it feels like it is going badly when it is going normally.",
     "Do not adjust based on faces on a screen. The feedback you are used to reading is simply not being transmitted.",
   ]),
   ("Test it the day before", [
     "The link, the camera, the microphone, the light. Technical trouble in the first minute costs you the calm you prepared, and it is entirely avoidable.",
     "Have a phone number as a fallback and say so at the start if you like.",
   ]),
   ("One-way recorded interviews", [
     "Genuinely unpleasant, and widely disliked. Treat it as a rehearsal you happen to be recording: use your allowed retakes, and answer as though one person is there.",
   ]),
 ],
 "faq": [
   ("Where do I look?", "The camera when making a point, the screen otherwise. Everyone switches and nobody scores it."),
   ("What if the connection drops?", "Rejoin and carry on. It happens constantly and no interviewer holds it against a candidate."),
   ("Is it harder than in person?", "Different. The cues are worse and the logistics are easier, and you can have notes in view, which in a room you cannot."),
 ],
 "related": ["job-interviews", "video-call-anxiety", "social-anxiety-in-interviews"],
},
{
 "slug": "what-to-say-about-your-weakness",
 "hub": "job-interviews",
 "h1": "The weakness question",
 "title": "What to Say About Your Weakness in an Interview",
 "desc": "A real answer that does not damage you, why the fake ones fail, and how to answer without naming a diagnosis.",
 "answer": "Name a real behavior, then the thing you already do about it. <strong>\"I lose detail in long verbal briefs, so I write during them and send a summary\"</strong> is honest, specific, and demonstrates the fix. That structure is the entire answer.",
 "sections": [
   ("Why the fake answers fail", [
     "\"I am a perfectionist\" and \"I care too much\" are recognized immediately as non-answers, and what they actually signal is that you would rather not be straight with them.",
     "The question is not really about the weakness. It is about whether you can assess yourself accurately.",
   ]),
   ("The structure", [
     "A specific behavior, the context where it shows up, and the concrete thing you do about it. Three parts, thirty seconds.",
     "The fix is the part being marked. A weakness with an active fix reads as self-awareness; one without reads as a risk.",
   ]),
   ("Answering without naming a diagnosis", [
     "You never have to say ADHD, dyslexia or anxiety here. Describe the effect, not the cause.",
     "\"I read slowly under time pressure, so I ask for documents in advance and come in with comments\" says everything useful and discloses nothing.",
   ]),
   ("Pick something true but not central", [
     "Not the core skill of the job. A real thing at the edges, that you have genuinely worked on.",
     "If the honest answer is the central skill, that is worth knowing about the fit before you talk yourself into the role.",
   ]),
   ("Have it ready", [
     "It is the one question people improvise and then regret. Write it, say it out loud once, and it stops being the question you are dreading.",
   ]),
 ],
 "faq": [
   ("Can I say I do not have one?", "It reads as evasive and it is the answer interviewers most often flag. Everyone has one and the question is testing whether you know yours."),
   ("What if my weakness is nerves?", "Usable, with a fix: \"I used to go blank in presentations, so I rehearse the opening until it is automatic.\" That is a good answer."),
   ("Is it a trick question?", "No, and treating it as one produces the fake answers. It is one of the more genuinely informative questions asked."),
 ],
 "related": ["job-interviews", "adhd-job-interview", "interview-questions-you-can-prepare"],
},
{
 "slug": "asking-for-interview-adjustments",
 "hub": "job-interviews",
 "h1": "Asking for interview adjustments",
 "title": "Asking for Interview Adjustments",
 "desc": "What you can ask for, who to ask, when to ask, and whether you have to say why.",
 "answer": "Email whoever arranged the interview, not the panel. <strong>Ask for one specific thing, in advance, without a justification</strong> — \"could you send the questions beforehand?\" is a request coordinators handle as routine admin, and the panel often never sees it.",
 "sections": [
   ("This is not legal advice", [
     "What you are entitled to ask for, and what an employer must grant, depends on your country and sometimes on the role. Nothing here is a statement about your rights.",
     "What follows is the request people describe making, and how it is usually handled.",
   ]),
   ("What people ask for", [
     "The questions in advance, extra time on a written or timed task, a take-home instead of a live exercise, a break between stages, or the names and roles of who will be in the room.",
     "Interviewing on a specific day, or remotely instead of in person, are also ordinary asks.",
   ]),
   ("Ask the coordinator", [
     "Whoever sent the calendar invite. They arrange logistics for a living and this is logistics to them.",
     "Going to the hiring manager makes it a conversation about you. Going to the coordinator makes it a booking detail.",
   ]),
   ("You do not have to say why", [
     "\"I would work better with the questions in advance\" is a complete request. Many people add a reason and it is rarely needed.",
     "If you do want to give one, the effect is enough: \"I read slowly under time pressure.\" No diagnosis required.",
   ]),
   ("Ask early", [
     "When the interview is booked, not the day before. Early reads as organized; late reads as a problem to solve at short notice.",
   ]),
   ("If they refuse", [
     "Rare, and informative. An employer that will not send an agenda is telling you something about how it runs meetings.",
   ]),
 ],
 "faq": [
   ("Will the panel know I asked?", "Sometimes, and usually only the practical part — that you get ten extra minutes, not why. Coordinators generally do not pass on reasons."),
   ("Does it make me look like hard work?", "Asking for one thing clearly and early reads as prepared. It is a list of six, sent the night before, that creates an impression."),
   ("Can I ask after I have already been booked in?", "Yes, at any point. Sooner is easier for them and therefore easier for you."),
 ],
 "related": ["job-interviews", "dyslexia-in-a-job-interview", "adhd-job-interview"],
},
{
 "slug": "interview-questions-you-can-prepare",
 "hub": "job-interviews",
 "h1": "The questions that always come up",
 "title": "Interview Questions You Can Actually Prepare",
 "desc": "The nine that appear in almost every interview, and the two you should ask them.",
 "answer": "Nine questions cover most interviews, and they map onto the six stories. <strong>Prepare the stories, not the questions</strong> — one story answers three or four of these depending on which part you emphasise.",
 "sections": [
   ("The nine", [
     "Tell me about yourself.",
     "Why this role, and why us.",
     "Tell me about something you delivered.",
     "Tell me about something that went wrong.",
     "A time you disagreed with someone.",
     "A time you had to learn something quickly.",
     "What is your weakness.",
     "Where do you want to be.",
   ]),
   ("They are six stories, reused", [
     "\"Something that went wrong\" and \"a time you disagreed\" are often the same event told with a different emphasis. So is \"learned quickly\" and \"proud of\".",
     "Prepare the events, not scripted answers, and you can point them at whatever is asked.",
   ]),
   ("Keep them to two minutes", [
     "Situation, what you actually did, what happened, what you would change. Time one out loud — the untimed version runs to five minutes and loses the room.",
   ]),
   ("Have numbers where you can", [
     "\"Cut it from six hours to twenty minutes\" is remembered. \"Improved the process\" is not, and it is the same achievement.",
   ]),
   ("The two to ask them", [
     "\"What does the first ninety days look like?\" and \"what would make you glad you hired someone in six months?\"",
     "Both get a real answer, both tell you whether you want the job, and both are visibly not questions from a list.",
   ]),
 ],
 "faq": [
   ("What if I have no big achievements?", "Small and specific beats big and vague. A thing you fixed that annoyed everyone is a good story."),
   ("Should I write answers out in full?", "Write them, then reduce to bullet points and say them out loud. A memorized script sounds memorized and collapses if interrupted."),
   ("How many questions should I ask?", "Two good ones. A long list rarely gets through and the time is usually shorter than expected."),
 ],
 "related": ["job-interviews", "what-to-say-about-your-weakness", "the-day-before-an-interview"],
},
{
 "slug": "the-day-before-an-interview",
 "hub": "job-interviews",
 "h1": "The day before an interview",
 "title": "The Day Before an Interview",
 "desc": "What is worth doing, what makes it worse, and when to stop.",
 "answer": "Do three things and then stop. <strong>Say your stories out loud once, check the route or the link, and decide what you are wearing.</strong> Preparation past that point raises the stakes rather than your readiness.",
 "sections": [
   ("Say the stories out loud, once", [
     "Not read, said. One pass through your six. Twenty minutes.",
     "The value is in having heard your own voice say them; a second and third pass adds very little and starts to feel like cramming.",
   ]),
   ("Check the logistics", [
     "The route and how long it takes, or the link and whether it opens. The building, the floor, who to ask for.",
     "This is the anxiety that is completely avoidable, and it is the one that most often produces the bad first ten minutes.",
   ]),
   ("Decide the clothes", [
     "Tonight, not in the morning. It is a small decision that becomes disproportionate when you are already braced for something else.",
   ]),
   ("Then stop", [
     "More research the night before does not surface in the conversation, and it reliably raises how much the whole thing feels like it matters.",
     "Do something that occupies you. The people who sleep badly are usually the ones who kept preparing.",
   ]),
   ("In the morning", [
     "Eat something. Arrive early enough to not be rushing, and then wait somewhere nearby rather than sitting in reception for half an hour.",
   ]),
 ],
 "faq": [
   ("What if I cannot sleep?", "One bad night does not noticeably affect how you come across, and believing it will is its own problem. Plan an easy morning rather than trying to force sleep."),
   ("Should I re-read my resume?", "Once. You should know what is on it, because they will ask about a line of it."),
   ("What about the questions I want to ask?", "Have two written down and take them in. Nobody minds and it means you still have them if the conversation runs long."),
 ],
 "related": ["job-interviews", "social-anxiety-in-interviews", "interview-questions-you-can-prepare"],
},
]
