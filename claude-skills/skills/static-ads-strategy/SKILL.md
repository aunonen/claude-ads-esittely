---
name: static-ads-strategy
description: >
  Applies a proven static ad strategy framework to evaluate, brief, and
  strengthen the brand's Meta image ad creatives. Invoke this skill whenever you
  need to assess whether an ad idea or brief meets the standards of
  high-converting static ads, or to produce a strategy brief before creative
  generation. Grounded in six principles: an irresistible offer,
  skimmability, objection handling, social proof, scroll-stopping imagery and
  simplified copy, plus design as a moat.
---

# Static Ads Strategy

## What This Skill Is For

Static image ads remain one of the most efficient tools available to
brands. A well-made static can be produced in a fraction of the
time of a video ad, tests messaging and imagery at low cost, and — when made
correctly — can reduce CPA by 30–40% at scale.

**The critical qualifier: "when made correctly."**

Most static ads fail not because the product is wrong or the budget is too
low, but because they violate the basic principles that make static creative
convert. This skill applies those principles to the brand's specific context
(from `context/` and `CLAUDE.md`'s Brand Assets) so
every creative brief and finished ad is built on a strategic foundation
rather than intuition.

Invoke this skill:

- Before creative generation, to produce a **Static Ad Strategy Brief** that
  informs the offer × angle choices and copy direction
- During creative review, to **score and pressure-test** proposed cards
  against the framework before committing to generation
- As a standalone reference, to answer "why is this ad likely to work / fail?"

---

## The Principles of High-Converting Static Ads

These are the non-negotiable standards every static must meet. Run
every ad idea through all of them before briefing generation.

---

### Principle 1 — Irresistible Offer

Offer is the most important part of an ad. Scroll-stopping creative is nothing if the offer isn't converting.

Offer is the promise or exchange proposed in the ad that captures attention, sparks desire, and motivates a potential customer to take action.

**A good ad offer consists of:**

- Dream outcome: what they want most
- Likelihood of Achievement: why it’ll work for them
- Time Delay: When they’ll get it
- Effort and Sacrifice: How little they have to do

The only job of a successful ad offer is to make someone stop scrolling and think: That’s exactly what I want.. How do I get it?

**Ad offer examples**

Each offer clearly communicates a dream outcome, likelihood of achievement, timeframe, optionally a mechanism and effort&sacrifice in one simple sentence.

- “We help contractors add 50K/month in booked jobs or you don’t pay”
- “Chiropractors: Fill your calendar with 20 new patients in 30 days quaranteed”
- “Roofers: Get 6 new installs in 30 days only pay per result”
- “Solar companies: 40-60 qualified leads in 45 days guaranteed or no fee”
- “Dental clinics: 40 new patient inquiries in 30 days or your next month is free”

### Principle 2 — Skimmability

**The rule:** A prospect must understand what the ad is about within one
second of encountering it. If it takes longer, they have already scrolled past.

Unlike video — where the viewer commits at least five seconds before deciding
whether to keep watching — a static ad is judged in a glance. If either the
image or the visible text slows the prospect down, the ad fails before it begins.

**What kills skimmability:**

- Too much copy on the image itself: more layers or longer lines than the
  length table in `creative-strategy`'s _Creative Copy_ section allows for that
  creative concept
- Font that is too small, too thin, or low contrast against the background
- A composition with no clear visual hierarchy
- An image that requires explanation to understand

**What enables skimmability:**

- A single dominant visual element (the product, the finished work, an in-use scene, a
  bold headline)
- One dominant first line at high contrast, large enough to read without
  zooming (how to write it: `creative-strategy`'s _Creative Copy_ section)
- A clear visual hierarchy: hero element → headline → supporting detail → CTA

**Applied to the brand:**
A vivid product shot in context does most of the work without any copy at all.
Copy overlays should add one single layer of meaning — not describe what the
image already shows. If the image shows the product surrounded by its key
ingredients or in use, or the finished work, the overlay should speak to the
outcome or the frustration it solves (e.g. "[Outcome], [without the thing they
dread]") — not to a spec (e.g. "18 kW, SCOP 4.5" or "500mg per serving"). Keep the on-image text to the
layers and lengths in `creative-strategy`'s _Creative Copy_ section. Everything
else belongs in the primary text of the post caption.

---

### Principle 3 — Objection Handling

**The rule:** Static ads often reach prospects mid-to-bottom funnel — people
who've seen the brand before but haven't purchased. Use the creative to
dismantle the specific objection stopping them.

**Objection categories and the right response.** Use the brand's own table in
`context/offer-brief.md` → _Objections & Creative Responses_. The common
categories look like this:

| Objection           | What the prospect is thinking               | Creative response                                                                                  |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Price               | "Why pay more than the cheap alternative?"  | Reframe value (cost per use, cost of what they waste today, savings, tax credits); payment terms     |
| Trust               | "Does it actually do/contain what it says?" | Lead with verification (reviews, experience, certifications, testing, guarantees), not just claims |
| Fit / identity      | "This isn't for someone like me"            | Myth-break framing, audience-specific proof                                                          |
| Efficacy skepticism | "Will I actually notice a difference?"      | Expectation-setting, real customer language                                                        |
| Category myth       | "Isn't this [common misconception]?"        | Direct myth-reversal, grounded in a sourced fact                                                   |

**Applied to the brand:**
Before briefing any ad, nominate the specific objection it is
designed to handle. A creative that handles one objection clearly outperforms
one that vaguely gestures at several — the objection should be legible in the
headline or visual treatment without the prospect reading the caption.

---

### Principle 4 — Social Proof

**The rule:** Include at least one social proof element **as an on-image graphic** in at least 1 out of every 2 creatives of the pool (50%); inside a test, a challenger keeps the control's proof element. The other half of the pool does not need an on-image badge — the same proof point can still run in the caption/primary text copy for those cards; it simply isn't rendered as an on-image graphic.

Social proof reduces risk perception and provides external validation that
bypasses internal scepticism. A person unsure whether to trust an unfamiliar
brand is reassured seeing that thousands of others already have.

**The brand's real proof assets** are listed in `context/offer-brief.md` →
_Social Proof Assets_. Use only those. Typical formats:

| Format              | Example                                                    | Best used when                                      |
| ------------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| Review count        | "[N]+ five-star reviews"                                   | Building initial trust                              |
| Customer count      | "Trusted by [N]+ customers"                                | Establishing credibility and scale                  |
| Certification       | "[Certification name]"                                     | Answering the trust/quality objection               |
| Third-party testing | "Third-party tested"                                       | Reinforcing a certification claim                   |
| Press mentions      | "As Featured In" + logos (from `reference/design-assets/`) | Establishing broader credibility                    |
| Guarantee           | "[N]-day money-back guarantee"                             | Removing purchase risk for price-hesitant prospects |

At least one of these must appear in 1 out of every 2 statics — as image copy
on the creative itself. For the other half, the same proof point can still
appear in the primary text/caption instead — it just isn't an on-image
graphic for that creative.

When a creative does carry an on-image badge, vary its visual treatment
across the pool (pill, icon+text lockup, corner seal, inline checkmark —
never the same orange rectangle every time) and include a rendered graphic
star element whenever the proof is review/rating-based — see
the badge section of `~/.claude/skills/ad-design/design-guide.md` for the
full menu.

**Note — USP/benefit icons are a separate design element, not a social proof
treatment.** When a creative uses icon sets from `reference/design-assets/`,
they are never a single lone icon accent — they always appear as a themed
group of 3–4, each paired with a short grounded benefit label, all in one color
variant, centered as a row, no background box. This is independent of whether
the creative also carries a social proof badge (a card may have neither, either,
or both). See the USP row section of `~/.claude/skills/ad-design/design-guide.md`
for the full spec — not duplicated here.

---

### Principle 5 — Scroll-Stopping Creative

**The rule:** The creative must stop the scroll before the copy gets a chance to
work. If the visual doesn't stop the scroll, the words never get read.

This is not about polish or production cost — it's about whether the visual
does something unexpected, emotionally resonant, or immediately recognisable to
the target customer. A product on a plain white background rarely stops the
scroll.

**What makes an image stop the scroll:**

- **Colour contrast** — a vivid product or brand colour against a neutral feed
  stands out instantly
- **unexpected composition** — the product in a surprising or aspirational
  context creates a micro-pause; a native creative concept can help once the
  concept is being tested (see `creative-strategy`'s _When the creative concept
  matters_)
- **Emotional resonance** — an image that makes the prospect feel something
  (craving, energy, relief, envy, recognition) triggers a pause before
  conscious thought
- **Visual specificity** — real work, material, ingredient or in-use backgrounds are more arresting
  than a generic studio shot

**What does NOT stop the scroll:**

- A plain white-background product cutout with no context
- An image that requires reading the caption to understand

**Applied to the brand:**
Find the brand's inherent visual tension or appeal (e.g. old vs. new, mess vs.
finished, indulgence vs. health, luxury vs. price, craft vs. convenience) and
lead with it visually — vivid colour, the real finished work or in-use
context, desirable or aspirational
styling — with the proof as the secondary layer. Use the lifestyle/context
imagery in `reference/products/Images/` and the backgrounds in
`reference/design-assets/` for this.

---

### Principle 6 — Copy Simplicity

**The rule:** Reduce the message to its single irreducible core. One benefit.
One emotion. One reason to click.

The impulse when briefing ad copy is to include everything — all the USPs, all
the benefits, all the objections handled at once. This produces copy that
reads like a spec sheet and converts like one too.

Never lead with a technical spec or dose number (e.g. "18 kW" or "500mg per
capsule"). How on-image text is written, layered and sized lives in one place:
`creative-strategy`'s _Creative Copy_ section.

**The test:** Cover the logo and ask "What is this ad for, and why should I
care?" If the answer requires more than one sentence, the copy is doing too much.

**Copy structure for a static:** the layers in `creative-strategy`'s
_Creative Copy_ section (first line, second layer, format text, proof), plus
the logo. The rest — supporting copy, USPs, CTA, offer detail — goes in the
post caption (primary text), not on the image.

---

## Design as a Moat

Well-designed statics are harder to copy than generic ones. A brand that
consistently produces clean, on-brand, visually coherent statics builds a
recognisable creative identity that competitors cannot easily replicate.

For the brand this means:

- **Brand colour and both fonts are used correctly and consistently** — see
  `CLAUDE.md`'s Brand Assets section (primary colour; headline font for the
  headline; body font for everything else) — every creative, not just some
- **Logo appears in a deliberate position, with visible clear space around
  it** — not cropped, not touching the frame edge, not competing with copy,
  not cramped into a corner with no breathing room
- **Text and badges sit directly on the continuous photographic
  background** — never boxed into a separate solid-colour panel or band
  that visually splits the frame into a "photo part" and a "text part"
- **Tone matches the market's sophistication** — check the _Stage of
  Sophistication_ in `context/offer-brief.md`. In a claim-fatigued (Stage 4–5)
  market, credibility-first expectation-setting ("give it 3 weeks")
  outperforms "see results fast!" hyperbole

This consistency compounds over time. A prospect who sees the brand's third ad
already recognises the brand before reading a word.

---

## Evaluating an Ad Against the Framework

Before briefing any ad idea or card for generation, score it against these six questions,
one per principle:

| #   | Principle    | Question                                                                                                             | Pass / Fail |
| --- | ------------ | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| 1   | Offer        | Does it make one clear offer the audience would want (dream outcome, likelihood, time delay, effort)?                |             |
| 2   | Skimmability | Can a prospect understand this ad in one second?                                                                     |             |
| 3   | Objection    | Does it address one specific objection clearly?                                                                      |             |
| 4   | Social proof | Does it include at least one social proof element (on-image for ~half the pool, caption/primary text for the rest)? |             |
| 5   | Scroll-stop  | Does the image do something to stop the scroll?                                                                      |             |
| 6   | Simplicity   | Is the message stripped to its single irreducible core?                                                              |             |

An idea that fails two or more of these should be revised before proceeding
to generation. The cost of generating a weak ad is not just the
generation credit — it is the testing budget spent on an ad that was never
going to convert.
