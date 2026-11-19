---
name: ad-library
description: >
  Maintains the agency's shared ad library in the hub's library/ folder: public
  Meta ads from high-value service businesses that pass a strict evidence gate,
  turned into pattern cards (offers, angles, creative concepts, creative copy
  devices, formats) with 2–3 references each, a style library (language and
  visuals) and confidence levels that only rise with the user's approval. Four
  modes: collect, recheck, synthesize, report. Runs in a hub session (not in a
  client folder). Invoke when the user asks to collect ads into the library,
  check/refresh the library, update the library's patterns, or see the
  library's status.
---

# Agency Ad Library

The library turns public ads into **reliable** knowledge about what works in
high-value services, without letting good-looking but unproven ads in. Its
rules, structure and confidence levels are in `library/README.md`; read it first.

**Where it runs.** In a session opened in the agency hub (the folder with
`library/`, `clients/` and `_template/`). Client sessions only read the library
(`../../library/`); they never write to it. If the current folder isn't the hub,
stop and say so.

**What never goes in.** A client's own ads, name, numbers, claims, assets or
research. The only client-derived data allowed is a pattern ID with won/lost
and a date (mode synthesize, step 4).

The library's text (cards, style entries, logs) is written in **Finnish**.

---

## Mode: collect — "kerää kirjastoon [ala]"

Uses the browser method, scoring and goal categories of
`~/.claude/skills/ad-inspiration-collection/SKILL.md` (read Steps 1–3 there;
don't redefine them), with these differences:

1. **Plan per category, not per client.** Ask which categories and buying
   situations to cover (`library/_evidence-log.md` explains the buying-situation
   tags). Build the search plan in the four baskets (map / discover / snowball /
   validate) from neutral category words, places and known advertisers; the
   validate basket uses the hypotheses in existing pattern cards instead of a
   client's context. Show the plan and wait for the user's OK.
2. **Advertisers first.** Shortlist advertisers from the map basket and score
   them: similarity to the target buying situation (service, size, lead model,
   price level) and testing maturity (number of ads, new versions, time
   active). Mark national brands running awareness budgets; their ads don't
   form patterns.
3. **Read each advertiser's page as text** (active, and for testing advertisers
   also inactive ads from the last 12 months), then open the details of each ad
   that might pass the gate (EU reach, targeting). Snowball new words.
4. **Score before looking closely at the creative.** Record points, class, goal
   and run time first; only then look at the image.
5. **Apply the library gate** (`library/README.md` → Pääsyehto): lead or sales
   goal; class A with at least two independent signals (run time ≥ 60 days plus
   multiple versions, clearly large EU reach, or the idea returning with a new
   image); a testing advertiser. Everything else stays out, except:
   - `Dropped` ads of testing advertisers → text rows (counter-evidence)
   - content/awareness ads with an exceptional style → only as style examples,
     marked `Tavoite: Content (vain tyyli)`
6. **Save** passing ads to `library/ads/<ala>/<advertiser>-<what-it-does>.<ext>`
   with a sidecar `.txt` (same fields as `ad-inspiration-collection` Step 4,
   plus `Ala:` and `Ostotilanne:`), and a row in `library/_evidence-log.md` with
   status `Candidate`. Version pairs and dropped text rows go in their sections.
7. **Log the round** in `library/_collection-log.md` (baskets, advertisers per
   basket, snowball words, limits).

At most 3 saved ads per advertiser unless a fourth carries a clearly different
idea. Target for a first category: 10–15 testing advertisers.

## Mode: recheck — "tarkista kirjasto" (monthly)

For every advertiser with `Candidate`, `Confirmed` or `Stopped` ads in the log,
read their Library page as text again and open each logged ad's details:

- still running, at least 30 days after it entered, and EU reach grown → `Confirmed`
- still running, reach not grown or not shown → stays `Candidate`, note it
- stopped after a long run → `Stopped`, class one step lower
- stopped within ~3 weeks of entering → `Dropped` (counter-evidence)

Write every reach reading with its date (`120 000 (1.9.) → 416 612 (26.10.)`)
and the check date. Also collect new dropped ads and version pairs from the
same reads. Log the round in `_collection-log.md`.

## Mode: synthesize — "päivitä kirjaston kuviot"

1. **Describe and group.** From the logged ads' rows and sidecars (and the
   images of `Candidate`/`Confirmed` ads), describe each ad's components in your
   own words as `competitor-analysis` Step 2 does, then group descriptions into
   patterns and run the combination analysis (`competitor-analysis` → Component
   Map and Combination Analysis): count **advertisers**, not ads; check
   counter-evidence (`Dropped`, version pairs); score signals.
2. **Pattern cards.** For each pattern seen with 2+ advertisers that passed the
   gate, create or update a card from `library/_templates/pattern-card.md`:
   mechanism (why it likely works, not just that it recurs), when it fits,
   evidence, counter-evidence, Finnish application notes. New cards start at
   `Candidate`. IDs by type: `OFF-001`, `ANG-001`, `CON-001`, `CPY-001`,
   `FMT-001` (next free number).
3. **References.** Pick 2–3 per card: `Confirmed` ads from different
   advertisers with the highest points. Say in one line why each is a good
   example. No reference without a pattern.
4. **Agency test feedback.** Ask the user for the "Kirjastopalaute" lines from
   the clients' Phase 0 analytics reports (`clients/*/outputs/analytics/
   analytics-report-*.md`); read only those lines, nothing else from the
   client folders. Add each to the card's _Agentuurin testit_ as
   `[päivä] · voitti/hävisi` — never the client's name, numbers or copy.
5. **Style entries.** From `Confirmed` ads only, write concrete, measurable
   language (`S-LANG-*`) and visual (`S-VIS-*`) traits seen with 2+ advertisers,
   from `library/_templates/style-entry.md`, into `library/style/style-guide.md`.
6. **Level proposals — never applied without approval.** For each card and
   style entry, propose a level change with its reason:
   - `Candidate → Supported`: 3+ advertisers (ideally 2+ categories), 2+
     `Confirmed` ads, fewer droppers than users
   - `Supported → Proven`: at least one agency test won (and none lost since)
   - `→ Fading`: not seen for 6 months, or droppers outnumber users
   Show the proposals as a list and **stop**. Apply only the ones the user
   approves, and record each in the card's _Historia_ with the date and
   "hyväksyjä: käyttäjä".
7. **Index.** Update `library/patterns.md` (cards and style entries, level,
   buying situations, advertisers, last seen).

## Mode: report — "kirjaston tila"

Ads by status and category, patterns and style entries by level, pending level
proposals, cards not seen in 4+ months, categories short of 10 testing
advertisers, and the date of the last recheck.

## Output

End each mode with a short summary of what changed (files, counts) and, for
synthesize, the list of level proposals waiting for the user.
