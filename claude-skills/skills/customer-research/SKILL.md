---
name: customer-research
description: >
  Builds and updates the client's customer and market research with a fixed,
  repeatable method, so every client gets research of the same breadth: a
  starting-situation map drawn up before any search (every situation a
  customer could buy from: customer types, what they move from, triggers), so
  the audiences don't narrow to the one route the offer points at; a
  source map covering six source groups with minimum counts (the client's own
  customers, competitors' reviews, several forums, customer stories, media and
  authorities, search questions), a standard set of search terms, fixed research
  questions, market context with dated facts, breadth targets for segments,
  problems and desires, and a coverage check before finishing. Single-source
  findings and interpretations are kept, marked as such, never dropped. Every
  quote verbatim with its source; a reliability level for every section; no
  personal data. Section-by-section reporting rules and fixed rules for turning
  findings into components (what is an audience, problem, desire or objection,
  merging, labels, quotes, evidence format, awareness levels, test priority).
  Writes customer-deep-research-report.md, audience-hypotheses.md (incl.
  research angles), the offer brief's objections, research-sources.md and
  necessary-beliefs.md (background). Three modes:
  initial, update, check. Invoke during /onboard round 3, when the user has new
  material from the client (an interview, read-out messages, new reviews), or
  whenever the user asks to research, update or check the client's customer
  understanding.
---

# Customer Research

The audiences, problems, desires, objections and customer language the ads
are built on come from here. Research that is too narrow gives the ads too
little to test; research that is guesswork talks to an imagined customer. This
skill does both halves: it searches **wide, the same way for every client**,
and it keeps the evidence visible, so every row says how sure we are.

Runs in a client folder. Writes in the client's language (Finnish by default).
Read `context/business-info.md`, `context/offer-brief.md`,
`context/strategy.md` and the existing research files first: what the client
and the onboarding already said about its customers is research material too
(source type `client interview`).

---

## Rules (all modes)

- **Breadth first, evidence visible.** Write down every segment, problem,
  desire and objection the sources support, with the number of sources behind
  it. A finding from one source is kept as a row marked `1 lähde`, never
  dropped into a note: a test tells whether it holds. Only claims no source
  supports at all stay out.
- **Source types, strongest first** (used for reliability, not for what gets
  written):
  1. `own customer` — the client's own customers' words: their reviews of the
     client, messages or questions read out in the interview, customer
     stories on the client's site
  2. `client interview` — what the client and staff say customers ask, fear
     and decide on, including what the onboarding recorded
  3. `public review` — reviews of competitors and other providers
  4. `customer story` — named-situation stories in media, manufacturers' or
     competitors' case studies, where a customer speaks
  5. `forum` — Suomi24, vauva.fi, Facebook groups, Reddit, trade forums
  6. `media` — news, guides, authorities, trade associations
  7. `search` — questions people type (Google autocomplete, "People also ask",
     related searches)
- **Quotes are verbatim**, in quotation marks, as
  `"…" — source type, source, date`, typos kept. An interpretation or summary
  is allowed when it adds something the quotes don't say, marked
  _(tulkinta)_, with the sources it rests on; never presented as a quote.
- **No personal data.** Never write names, contact details, addresses or
  anything that identifies a private person into any file. Anonymise while
  writing (e.g. "asiakas, Kempele, 2026-09").
- **Facts are dated and sourced.** Prices, subsidies, tax rules, regulations
  and deadlines come from an official or primary source where one exists, with
  the date read. They change: say when to re-check.
- **Reliability per section** (`customer-deep-research-report.md`) and per row
  (`audience-hypotheses.md`):
  - `Confirmed` — from `own customer` sources, at least **6 sources**
  - `Supported` — reviews, customer stories or the client interview,
    recurring: at least **15 quotes from at least 6 sources**
  - `Draft` — forums, media, search or fewer sources
- **Every source is logged** in `context/research-sources.md`, with its group
  (A–F below), and the coverage table kept up to date.

---

## The research method (initial and update)

### 1. Research questions (every client, every time)

The research answers these; each maps to a report section:

| # | Question | Report section |
|---|---|---|
| 1 | What is happening in the market now: prices, subsidies and tax rules, regulations, deadlines, seasonality, trends? | Market context |
| 2 | Who buys, in what observable situation (home, business, life stage, region)? | Customer segments |
| 3 | What makes them start looking now? | Purchase triggers |
| 4 | What do they use today, what do they like and hate about it? | Existing solutions |
| 5 | What do they fear, doubt or believe wrongly? Where does trust break? | Myth versus reality and the trust gap |
| 6 | How do they decide: where they look, how many quotes, how long, what tips it? | Decision journey |
| 7 | What do happy and unhappy buyers say afterwards? | Post-purchase sentiment |
| 8 | Who else do they consider, and what do they say about them? | Competitive landscape |
| 9 | What words do they use? | Language bank |

### 2. Starting-situation map (before any search)

Research that follows one route finds one audience: when every search goes
through the same current solution, offer or subsidy, every segment comes out
as the same person. So before the source map, list **every situation from
which a customer could end up buying the service**, from four directions:

- **The client's customer types and services** — every customer type and
  service named in `business-info.md`, `offer-brief.md`, `strategy.md` and the
  interview (e.g. homes, holiday homes, housing companies, businesses, new
  builds; each service line).
- **What they move from** — every current solution or alternative a buyer
  could be replacing or adding to: the competing technologies, doing it
  themselves, doing nothing, an older version of the same service. Check the
  category's common starting points with a search (`[palvelu] vai`,
  `[palvelu] tilalle`, `[palvelu] korvaamaan`), not only the ones the offer
  mentions.
- **Triggers that create a buyer** — breakdown or end of life, renovation,
  moving or building new, a cost rise, a rule or subsidy change, a life
  change (family, retirement, inheritance).
- **The current focus** — mark which situations the client's Meta focus
  (`strategy.md`) covers. Situations outside it stay on the map.

Write the map to `research-sources.md` → _Starting situations_ before
searching, and fill in its result columns as the research goes.

Rules:
- Every situation **in the focus** gets the full search-term set (step 4)
  with that situation as `[vaihtoehto]`, and at least **2 sources**; every
  situation outside the focus gets one search pass.
- An offer, subsidy or deadline that applies to one situation doesn't narrow
  the map: note it on that situation's row and research the others too.
- No single situation gives more than ~50 % of the language bank's quotes,
  unless the sources really show nothing else (say so in the coverage table).
- Every situation in the focus ends as an **audience row** (`1 lähde` where
  so), **merged** into another row (name it), or a **gap** in _Open questions
  and gaps_ with the reason and how to close it. Never silently dropped.

### 3. Source map — six groups, minimum coverage

Work through every group. The minimums make the research equally broad for
every client; go further when a group keeps bringing new themes.

| Group | What | Minimum |
|---|---|---|
| **A. The client's own** | Every review of the client (Google, Facebook, trade sites), customer stories and references on its site, what the onboarding and offer brief say about customers, the client interview when there is one | All of them |
| **B. Competitors' reviews** | Google and Facebook reviews of 3–5 competitors **in the client's area** and 1–2 national players; read the 1–2 ★ and the 5 ★ ones | 4 providers, 20 reviews |
| **C. Forums** | At least **3 different sites** (e.g. Suomi24, vauva.fi, a trade forum such as lampopumput.info or rakentaja.fi, Reddit r/Suomi, public Facebook groups found by search). No single site gives more than ~40 % of the quotes | 3 sites, 10 threads |
| **D. Customer stories** | Media "kokemuksia" stories, manufacturers' and competitors' case studies, where a real customer speaks; prefer the client's region | 3 stories |
| **E. Media and authorities** | Local and national news, consumer and energy authorities, the tax administration, trade associations, ministries: the market context, rules and myths | 5 sources |
| **F. Search questions** | Google autocomplete, "People also ask" and related searches for the core search terms below | 1 pass per core term |

**Region.** For a local business, at least a third of groups B–D comes from
the client's own region; say in the coverage table how much did.

**Sign-in walls.** When a site needs sign-in or shows only part of the
content (Google Maps, Facebook), note it in `research-sources.md` and use
another route (the site's own search, a search engine with `site:`, the
company's review page), rather than leaving the group thin.

### 4. Search terms — the standard set

Build the terms from the service (`[palvelu]`), the starting situations
(`[vaihtoehto]`: run the set once **per situation** on the map, see step 2),
the client's area (`[alue]`) and competitors (`[kilpailija]`). Run all of them
in Finnish (and in the client's other languages if it has any):

- `[palvelu] kokemuksia` · `[palvelu] kannattaako` · `[palvelu] hinta` ·
  `[palvelu] ongelmat` · `[palvelu] pettymys` / `katuu`
- `[palvelu] vai [vaihtoehto]` · `[vaihtoehto] luopuminen` / `vaihto`
- `[palvelu] [alue]` · `[kilpailija] kokemuksia` · `[kilpailija] arvostelut`
- `[palvelu] tuki` / `kotitalousvähennys` / `rahoitus` (where relevant)
- `[palvelu] site:suomi24.fi` · `site:vauva.fi` · `site:` the trade forum

Add terms the sources themselves use (the customers' own words for the
service and the problem): the second pass often finds more than the first.

### 5. Stop rule

Stop only when **every group has reached its minimum**, **every starting
situation in the focus has its 2 sources or a recorded gap**, and the last
three new sources brought no new theme. If a minimum can't be reached (a niche with no
forum, no competitor reviews), say why in the coverage table.

### 6. Breadth targets for the output

So every client gets a comparable starting point. Fewer is fine only when the
sources really don't support more, and the report says so.

| Output | Target |
|---|---|
| Segments / audiences | 3–5, and every starting situation in the focus as a row, a merge or a gap |
| Problems | 8–15 |
| Desires | 5–8 |
| Objections (in the offer brief and the report) | 5–10 |
| Language bank | 30+ quotes over at least 8 themes |
| Awareness levels | all 5, described for this category |
| Suggested tests | 4–6 |
| Top ad angle opportunities | 5–8 |

### 7. Coverage check (before writing the summary)

Fill the coverage table in `research-sources.md`: sources and quotes per
group, how many from the client's region, the largest single site's share of
quotes, the starting situations (sources and quotes each, the largest
situation's share of the language bank, the result of each), and every
minimum not reached with the reason. Show it to the user with the summary.
---

## Writing the report

`context/customer-deep-research-report.md`, section by section, in this
order. Every section starts with `**Reliability:**` (and the number of
sources behind it). Write it so the strategist can use it without opening the
sources: findings first, then the quotes that show them. Keep each section to
what the ads can use; no general category background.

| Section | What goes in | Form and length |
|---|---|---|
| **Market context** | Prices (typical range, the client's own price), subsidies and tax rules, regulations, real deadlines, seasonality, market size and trend | Bullet per fact: the fact, its date, the source with a link. `Checked:` date and `re-check by` date at the top. 5–10 bullets |
| **Customer segments** | Covers the starting-situation map: one block per segment (3–5): **who** (observable situation: home, stage, region), **trigger** (why now), **wants**, **stops them**, **sources** (count, `1 lähde` where so) | 4–6 lines per block, 1–2 quotes each. A segment the client named in the interview or onboarding but the public sources don't show is kept and marked so. End with one line per situation on the map that isn't a block of its own: merged into which segment, or a gap |
| **Existing solutions audit** | Per current solution or alternative: what customers like, what they complain about, why they'd switch | One block per solution, 2–4 quotes, complaints grouped by theme with the number of sources |
| **Myth versus reality and the trust gap** | Every recurring fear, doubt or wrong belief (these are the objections): the belief in the customers' words, the reality with a source, and what would answer it | One block per objection (5–10): **Belief** (quote) · **Reality** (fact + source) · **Answer** (what the client can show). Then where trust breaks in the category (sellers, promises, after-sales) |
| **Purchase triggers and decision journey** | Triggers ranked by how many sources name them; the path from first thought to purchase (where they look, how many quotes, how long, who decides); what tips the decision | Numbered triggers with source counts, then the path as one short paragraph or arrow chain, then the deciding criteria with quotes |
| **Post-purchase sentiment** | What happy buyers praise and unhappy ones regret, the client's own customers first, separately from competitors' | Two lists (happy / unhappy), each theme with a quote and source count; the client's own reviews marked as such |
| **Language bank** | The customers' own words, grouped by theme (8+ themes, 30+ quotes): problems, fears, desires, triggers, the words they use for the service, how they describe the result | Theme in bold, then 3–5 quotes from **different** sources; never only one site per theme where others exist |
| **Competitive landscape snapshot** | The providers customers compare: local first, then national | Table: competitor · positioning · price point · strength (what customers praise) · weakness (what they complain about), with sources |
| **Top ad angle opportunities** | 5–8 directions the research suggests for ads | Per angle: label · angle type · core message · viewpoint · why it could stop the viewer · evidence (sections, source count). Described, never as ad copy. The same rows go to the _Angles_ table (below) |
| **Open questions and gaps** | What the research couldn't establish, every source-map minimum not reached and why, contradictions between sources | Bullets; each ends with how to close it (interview question, source to read) |

The summary in chat follows the Output line at the end of this skill, plus the
coverage table.

---

## From findings to components

How the report becomes rows in `context/audience-hypotheses.md` and the
offer brief's objections. Every row comes from the report: write the report
first, then derive the rows from it.

**What is which.** Ask of each finding:

| Component | Is it… | Test | Example |
|---|---|---|---|
| **Audience** | an observable situation someone is in | Could you tell from outside (the house, the life stage, the region) without asking how they feel? | "Omakotitalo, alkuperäinen katto 30 vuotta vanha", "Taloyhtiö, putkiremontti edessä" |
| **Problem** | a pain in the current situation | Does it exist **before** they consider buying, whether or not they ever buy? | "Katto vuotaa keväisin", "Pihan kunnossapito vie viikonloput" |
| **Desire** | an outcome they want | Is it what life looks like **after** the purchase, in their words? | "Ei tarvitse ajatella kattoa vuosiin", "Kerralla valmista" |
| **Objection** | a doubt or fear about **buying** (the solution, the price, the seller) | Does it stop or delay the purchase rather than describe the current pain? | "Remontti venyy", "Urakoitsija katoaa kesken" |
| **Awareness level** | how much the buyer knows | Not a finding to label; derived (below) | |
| **Angle** | a direction an ad could take | A viewpoint the ad starts from, backed by one or more of the above | |

A fear about the current situation ("katto pettää") is a **problem**; the
same person's fear about the solution ("uusi katto ei kestä lumikuormaa") is
an **objection**. One finding can give both, as two rows.

**Merge or split.**
- Same thing in different words (and the same answer would address it) → one
  row, all sources on it.
- Different situations, causes or answers → separate rows, even when the words
  are close (e.g. "the bill is high" vs "the bill is unpredictable").
- A row so broad that one ad couldn't address it ("worries about heating") is
  split; one so narrow that only one source could ever say it is merged into
  its nearest row as a quote.

**Labels.** Short (1–3 words), client-specific, in the client's language,
naming the thing itself, not a category: `VuotavaKatto`, not `Ongelmat`.
PascalCase, ASCII only (ä→a, ö→o, å→a), no spaces or hyphens, as in `creative-strategy`'s Allowed values: the
same label goes on the cards, into creative names and the Sheet. Never reuse a label for a different thing; never
rename a label already used on a card.

**The quote on the row.** Pick the **shortest, most concrete** verbatim quote
that says the thing in the customer's words, preferring, in order: the
client's own customers, the client's region, a recent date, a forum or review
over media. Where no quote exists, write the finding in plain words marked
_(tulkinta)_.

**Evidence, always in this form:**
`report §[section] · [N] sources ([types, e.g. 3 forum, 2 public review]) · [region note if any] · [Confirmed / Supported / Draft]`,
and `1 lähde` instead of the count where so. E.g.
`report §Myth versus reality · 5 sources (4 forum, 1 media; 2 from the client's region) · Draft`.

**Awareness levels.** Derive all five from the research questions:
- `Unaware` — who has the problem but doesn't look for anything (from
  triggers: who hasn't hit one yet)
- `Problem aware` — feels the pain, doesn't know the solution (problems,
  existing solutions)
- `Solution aware` — knows the solution type, compares options (decision
  journey, myths)
- `Product aware` — knows the client (the client's own reviews, the interview)
- `Most aware` — ready to buy, needs a reason now (real deadlines, triggers)

_What the ad opens with_ follows from what the level doesn't know yet. A
level the sources don't describe gets Source `Hypothesis`.

**Objections → the offer brief.** Every objection from _Myth versus reality_
goes to `context/offer-brief.md` → _Objections & Creative Responses_: the
objection's name, _What the prospect is thinking_ as the verbatim quote, and
_Creative response_ only from what the client can actually show (offer brief,
business info, the interview); where the client hasn't confirmed one, write
`(vahvistettava asiakkaalta: …)` with the suggestion. Add rows and fill empty
ones; never rewrite or delete a row the user or client wrote, add the new
quote under it instead.

**Angles → the _Angles_ table.** Each _Top ad angle opportunity_ becomes a row
with Source `Research`: label, angle type (one of `creative-strategy`'s fixed
types), core message (a plain statement, not a headline), viewpoint, why it
could stop the viewer, and evidence in the form above. A "who it's for"
framing is an audience or a call-out, not an angle. Described, never as ad copy. If
`competitor-analysis` already wrote the same angle, add `Research` to its
_Source_ and the evidence to its _Evidence_ instead of a new row.

**Suggested tests, prioritised:**
1. Combinations whose parts have the strongest evidence (more sources, own
   customers, the client's region) come first.
2. Among equals, the one whose result would teach the most: it decides
   between two directions, or tests the main audience or the main objection.
3. Each test combines components from **different** tables (audience ×
   problem or desire × awareness level, optionally an angle), says in _Why_
   which rows it rests on, and in _What a result would tell us_ what we'd do
   differently either way.
4. 4–6 tests; at least one built on a `1 lähde` or `Hypothesis` row the
   research found promising, marked so.

---

## Mode: initial — first research for a client

### 1. Client interview (by phone, run by the user)

Give the user this interview script in Finnish, adapted to the client's
business, and ask them to run it with the client (owner, salesperson or the
person who answers customers) and send back their notes. Ask the client to
**read out** real messages, questions and reviews where they can: read-out
customer words count as `own customer`, the client's own summaries as
`client interview`. No names.

1. Keitä asiakkaanne yleensä ovat? Missä tilanteessa he ottavat yhteyttä, ja
   mitä heillä oli ennen teitä (mistä ratkaisusta he tulevat)?
2. Mitä asiakkaat kysyvät ensimmäisenä? Voitko lukea pari viimeisintä
   tarjouspyyntöä tai viestiä sanasta sanaan (ilman nimiä)?
3. Mitä he pelkäävät tai epäilevät ennen kuin päättävät?
4. Miksi kaupat jäävät syntymättä? Mitä asiakas sanoo, kun hän kieltäytyy?
5. Mikä saa asiakkaan lopulta päättämään? Kuinka kauan päätös kestää?
6. Mitä tyytyväiset asiakkaat sanovat jälkikäteen? Entä tyytymättömät?
7. Keihin kilpailijoihin teitä verrataan, ja mitä niistä sanotaan?
8. Mitä asiakkaat ymmärtävät väärin palvelusta tai alasta?
9. Millaisia asiakkaita ette halua (liian pieni työ, väärä alue, …)?

Don't wait for the interview: do the public research (steps 1–7 of the
method) now, and run **update** when the notes arrive.

### 2. Research

Run the method above: research questions, the starting-situation map,
all six source groups to their minimums, the standard search terms, the stop rule, the breadth targets and
the coverage check.

### 3. Write

- `context/customer-deep-research-report.md` — per _Writing the report_.
- `context/audience-hypotheses.md` — per _From findings to components_:
  audiences, problems and desires, all five awareness levels as they look in
  this category, the research's angles, and a prioritised _Suggested tests_
  list.
  Source `Research` (a level the research says nothing about: `Hypothesis`),
  status `Untested`. Each table stands on its own: no audience column in
  problems, desires or awareness levels, no awareness column in audiences.
  Columns, exactly:
  - Audiences: `Label` · `Who they are (situation, home, stage)` · `Source` · `Evidence` · `Status`
  - Problems: `Label` · `The problem, in the customers' words` · `Source` · `Evidence` · `Status`
  - Desires: `Label` · `The desire, in the customers' words` · `Source` · `Evidence` · `Status`
  - Awareness levels: `Level` · `What the buyer knows at this level (in this category)` · `What the ad opens with` · `Source` · `Evidence` · `Status`, five rows (`Unaware`, `Problem aware`, `Solution aware`, `Product aware`, `Most aware`)
  - Angles: `Label` · `Angle type` · `Core message` · `Viewpoint` · `Why it could stop the viewer` · `Source` · `Evidence` · `Status` (angle types and the not-an-angle rules: `creative-strategy`'s _Angles_)
  - Suggested tests: `#` · `Combination (components)` · `Source` · `Why (evidence)` · `What a result would tell us` · `Status`

  The file's other tables (offers, arguments, concepts, copy) belong to
  `competitor-analysis` and `ads-analytics`; rows from other sources in the
  tables above are left as they are, except for adding `Research` to their
  _Source_ when the research backs them.
- `context/offer-brief.md` → _Objections & Creative Responses_: the
  objections, per _From findings to components_.
- `context/necessary-beliefs.md` — background for strategy: the belief
  sequence a buyer goes through.
- `context/research-sources.md` — the starting-situation map with results,
  sources (with group), interviews, counts per section, the coverage table.

Show the user a short summary: the coverage table, what's `Confirmed`,
`Supported` and `Draft`, and the biggest gaps.

## Mode: update — new material

Use when the user has new material (interview notes, read-out messages, new
reviews) or the research is older than ~6 months. Add the sources to
`research-sources.md`, add quotes to the language bank, re-check the market
context facts, rewrite the report sections the new material changes (per
_Writing the report_), update reliability levels and the `audience-hypotheses.md`
rows' evidence (source counts, `1 lähde` → more), and add new rows for new
findings, objections and angles (per _From findings to components_). A new
starting situation (e.g. one the client named in the interview) goes on the
map and gets its search pass. When the research backs a row that came from another source (e.g. a
`Competitor` problem), add `Research` to its _Source_ instead of a new row.
Never change a row's test **status** here (that is `ads-analytics`'s job).
Report what changed and which levels rose.

## Mode: check — how solid is the research?

Read the research files and `research-sources.md` and report: the coverage
table against the minimums, starting situations in the focus with no row
and no recorded gap (or missing map), sections and rows by reliability, rows the ads
rely on that are only `Draft` or `1 lähde`, market facts older than ~6
months, and the 3–5 questions the next client interview should answer.
Change nothing.

## Output

> **Customer research ([mode]): [N] sources in [G]/6 groups ([O] own customer, [R] from the client's region), [Q] quotes. Starting situations [M] ([A] as audiences, gaps: [list or none]). Segments [S], problems [P], desires [D]. Confirmed: [list] · Supported: [list] · Draft: [list]. Minimums not reached: [list or none]. Biggest gap: [one line].**
