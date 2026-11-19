---
name: competitor-analysis
description: >
  Analyses curated ad inspiration in reference/ad-inspiration/ — competitor ads
  the user has hand-picked plus the brand's own past winners — to extract winning
  ad components (offers, angles, creative copy, creative concepts, copy frameworks and
  visual execution) for the brand's Meta ad campaigns. Invoke this skill for Phase 1 of the Create New
  Ads workflow, or any time you need creative intelligence to inform strategy.
  Brand context is read on-demand from context/.
---

# Ad Inspiration Analysis — Creative Intelligence

Act as an **elite creative strategist and creative intelligence analyst**. Every
image in `reference/ad-inspiration/` has been hand-picked by the user — either a
competitor/cross-category ad they found genuinely inspiring, or one of the
brand's own past successful ads. This is high-signal, curated input. Study each one
closely, extract the patterns that make it work, and translate those learnings
into concrete ad ideas for **the brand**, written component by component (named in `CLAUDE.md`'s Brand
Assets section, referred to below as "the brand").

---

## Step 1 — List Local Files & Check for Duplicates

Read `reference/gws-config.json` for the `ad_inspiration_folder_id` and the
`inspiration_spreadsheet_id`. The inspiration analysis lives in its own
**internal** spreadsheet (agency only, never shared with the client); the
client-facing `spreadsheet_id` holds only the client's own ads and briefs. If
`inspiration_spreadsheet_id` is missing, stop and tell the user to run
`/onboard google` rather than writing competitor analysis into the client's log.

**1. List local files:**

```bash
ls "reference/ad-inspiration/" 2>/dev/null
```

Each ad is an **image** plus an optional **sidecar text file with the same
name** (`brand-what-it-does-A.jpg` + `brand-what-it-does-A.txt`) holding what
the screenshot doesn't show:

```
Primary text: [the ad's full primary text]
Headline: [the line below the image]
CTA: [button text]
Ad Library: [link]
Started running: [date]
```

Only images count as ads: skip `.txt` sidecars, files and folders whose name
starts with `_` (notes such as `_evidence-log.md`, the `_starter-formaatit/`
format examples) and anything else that isn't an image.

**If the folder is thin, collect first.** If it has no images, or fewer than ~10
`A`/`B`/`Own` ads with a lead or sales goal, or the newest collection in the
evidence log is older than ~2 months, tell the user and suggest running
`ad-inspiration-collection` before this analysis. Go on only if they choose to.

**2. Fetch existing filenames from column A of the "Ad Inspiration" tab to build a
deduplication list:**

```bash
gws sheets spreadsheets values get --params '{"spreadsheetId": "INSPIRATION_SHEET_ID", "range": "Ad Inspiration!A:A"}' 2>/dev/null
```

Only files not already in column A need analysis — these are the new additions
since the last run. If every local file is already logged, state that the folder
has no new inspiration and skip to re-reading the existing "Ad Inspiration" tab
rows (Step 3) to refresh the synthesis with full context.

---

## Step 2 — Visually Analyse Every New Image

For each local file whose name is NOT already in column A, read the image and
its sidecar directly with the Read tool — no download needed:

```
Read("reference/ad-inspiration/filename.jpg")
Read("reference/ad-inspiration/filename.txt")   # if it exists
```

This is the most important part of this phase — spend real effort here.
**Describe what the ad actually does, in your own words. Never pick a value
from a list and never force the ad into the brand's own categories**: a
competitor's ad is evidence to understand, not a card to fill in. Only the
awareness level uses fixed values. Write each field as a short, specific
description (a sentence or two), in the client's working language.

| Component              | What to extract |
| ---------------------- | --------------- |
| **Brand**              | Whose ad is this? Record the actual advertiser's name. If it's one of the brand's own past ads (its product, logo or branding, or a filename prefixed with the brand name), record the brand name as-is. Those are proven winners worth studying especially closely |
| **Goal**               | What the ad asks the viewer to do, and so what it is optimised for: use the goal in the evidence log or sidecar when there is one (categories in `ad-inspiration-collection`), otherwise read it from the CTA, the sidecar and the creative. An ad whose goal isn't a lead or a sale can't show that its offer or angle sells, however long it has run |
| **Creative copy**      | **All text on the creative**, verbatim, in the order a viewer reads it (headline first, then sublines, bullets, badges, small print). The first line read is what stops the scroll |
| **Primary text**       | The ad's full primary text from the sidecar, verbatim. If there is no sidecar, write "missing" (never reconstruct it from notes or the CTA) |
| **Creative concept**   | Describe the creative concept: what the ad pretends to be or borrows its form from, and how that form carries the message (e.g. "A brochure-style benefit list next to a product photo, built like a spec sheet"; "Looks like an article teaser: headline on an orange band over a real house"). Describe, don't label |
| **Offer**              | What exactly is offered, including an offer hidden in the CTA or primary text (e.g. "Pyydä tarjous ja selvitä paljonko voisit säästää" = a quote with a savings estimate). "None" only if there truly is none |
| **Angle**              | The ad's single dominant persuasion viewpoint, inferred, in one sentence, plus its **angle type** from `creative-strategy`'s fixed list (`Problem` / `Desire` / `Loss` / `RiskReversal` / `Comparison` / `Mechanism` / `Value` / `Credibility` / `Effort` / `BeliefShift` / `Timing` / `Control`). An audience call-out is the ad's first-line device, not its angle (e.g. "Makes the case for the category itself — why choose this heating type at all — rather than starting from the customer's problem") |
| **Audience**           | Who the ad talks to, as specifically as the ad allows |
| **Awareness level**    | The stage the ad assumes: Unaware / Problem aware / Solution aware / Product aware / Most aware |
| **Problem / desire**   | The **customer's** problem or desire the ad speaks to, not the ad's topic ("Afraid the electricity bill will explode", not "Why choose this pump") |
| **Argument**           | Why the ad claims the solution works, and how it proves it (a list of claimed benefits is a claim, not a demonstration; say what the proof actually is, or that there is none) |
| **Creative execution** | Fonts, colours, layout, images and composition: hero element, foreground/background relationship, use of space |
| **CTA**                | The step asked for: the button and/or the closing line |
| **Why it might work**  | One or two sentences tying the ad's evidence class and goal to what it does well. Not ideas for the brand: those belong in the Intelligence Report |

**This is non-negotiable** — copy alone is insufficient. The creative intelligence
is in how the image is composed, what it foregrounds, and what visual language it
uses. You cannot translate a winning ad to the brand without having seen and
understood the actual visual.

For each new file, also handle logging immediately after analysing it:

- Upload to the Ad Inspiration Drive folder:
  ```bash
  gws drive files create \
    --json '{"name": "FILENAME", "parents": ["AD_INSPIRATION_FOLDER_ID"]}' \
    --upload "reference/ad-inspiration/FILENAME" 2>/dev/null
  ```
- Capture the returned file `id`, construct the Drive link:
  `https://drive.google.com/file/d/FILE_ID/view`
- Append one row to the "Ad Inspiration" tab of the **inspiration** spreadsheet
  (columns A–R), values in exactly this order:
  ```bash
  gws sheets spreadsheets values append \
    --params '{"spreadsheetId": "INSPIRATION_SHEET_ID", "range": "Ad Inspiration!A:R", "valueInputOption": "USER_ENTERED"}' \
    --json '{"values": [["FILENAME", "BRAND", "EVIDENCE", "GOAL", "CREATIVE COPY", "PRIMARY TEXT", "CREATIVE CONCEPT", "OFFER", "ANGLE", "AUDIENCE", "AWARENESS LEVEL", "PROBLEM / DESIRE", "ARGUMENT", "CREATIVE EXECUTION", "CTA", "DRIVE LINK", "WHY IT MIGHT WORK", "ANGLE TYPE"]]}' 2>/dev/null
  ```
  Escape double quotes inside values (`\"`) so the JSON stays valid. Never leave a
  cell out — write "n/a" for an empty component so the columns don't shift. If the
  header row is the table below with only trailing columns missing (an older
  tab ending at `Why It Might Work`), append the missing header names after
  the last one and leave older rows as they are. If it differs otherwise, stop
  and tell the user instead of writing rows under the wrong headers.

| Col | Field              | What to put                                                     |
| --- | ------------------ | --------------------------------------------------------------- |
| A   | Filename           | Local image filename (used for deduplication)                   |
| B   | Brand              | Advertiser's brand name (the brand's own name for its past ads) |
| C   | Evidence           | `A` / `B` / `C` / `Own` / `Dropped` / `Unscored` — see below    |
| D   | Goal               | What the ad is optimised for                                    |
| E   | Creative Copy      | All on-image text, verbatim, in reading order                   |
| F   | Primary Text       | Verbatim from the sidecar, or "missing"                         |
| G   | Creative Concept   | Description of the creative concept                             |
| H   | Offer              | What exactly is offered (incl. in the CTA), or "none"           |
| I   | Angle              | Inferred, one sentence                                          |
| J   | Audience           | Who the ad talks to                                             |
| K   | Awareness Level    | Unaware / Problem aware / Solution aware / Product aware / Most aware |
| L   | Problem / Desire   | The customer's problem or desire                                |
| M   | Argument           | Why it claims to work, and the actual proof                     |
| N   | Creative Execution | Fonts, colours, layout, images, composition                     |
| O   | CTA                | The step asked for                                              |
| P   | Drive Link         | `https://drive.google.com/file/d/FILE_ID/view`                  |
| Q   | Why It Might Work  | Evidence class + goal + what it does well                       |
| R   | Angle Type         | One fixed angle type (added 2026-10-31; older rows are blank)   |

### Evidence — how sure are we that the ad works?

Meta's Ad Library hides spend and results, so a good-looking ad is not proof
of a winning ad. Each inspiration ad gets an evidence class when it is
collected. The scoring and the goal categories are defined in one place: the
`ad-inspiration-collection` skill (Step 3). In short: **A** = strong, **B** =
moderate, **C** = weak (format idea only), **Own** = the brand's own past ad
with known results (the strongest evidence of all), **Dropped** = a testing
advertiser stopped it within ~3 weeks: counter-evidence for its idea.

The evidence log also holds **text-only rows** for dropped ads with no image,
and a **Version pairs** section (what differed between a surviving and a
dropped version of the same idea). Read both: they are part of the evidence
even though they have no image to analyse.

Where the class comes from, in this order — never guess it from the image:

1. `reference/ad-inspiration/_evidence-log.md`, if it exists (a row per file
   with its points, class and goal; a `stopped` ad has already been lowered)
2. a filename suffix `-A`, `-B` or `-C` (e.g. `brand-angle-A.png`)
3. the brand's own ad with results the user gave → `Own`
4. otherwise `Unscored`

---

## Step 3 — Synthesis & Brand Translation

After analysing every new image, re-read the existing rows in the "Ad Inspiration"
tab of the inspiration spreadsheet (`Ad Inspiration!A:R`) so your synthesis covers the whole curated set, not just
what's new this run — then do the deeper creative work.

### Starting Point — what this round needs

The ideas must fit the round, so read before synthesising:

- **The agency ad library** (`../../library/patterns.md`, if it exists): read
  the index, then open only the cards (and `../../library/style/style-guide.md`
  entries) whose buying situation fits the client and whose level is
  Candidate, Supported or Proven (skip Fading). This is **tier-3 evidence**:
  weaker than the client's own results and its own market. Never write to the
  library from a client session.
- **`context/learnings.md`**: the control, what works and what doesn't per
  component, broken hypotheses and the
  two work queues (angle labels: the _Angles_ table in
  `context/audience-hypotheses.md`, the only angle register). Ideas build on it: don't propose what it says has failed
  without a reason, and fill the "New directions" queue.

- **The Phase 0 report** (newest `outputs/analytics/analytics-report-*.md`, if
  any): the **round type** (First round / Broad retest / Narrow test / Keep
  control), the **control** and, for a narrow test, **the component to test**.
  No report = First round.
- **What has been tested already:** the Creative Generations tab (Offer,
  Angle, Tests, Creative Concept, Creative Copy columns) and the report's class for each
  ad. Build a list of offer × angle pairs and component values already tested,
  each marked won / promising / lost / inconclusive / not yet live.

### Component Map

**Mind how the ads were found.** The evidence log's _Found via_ column says
which search basket led to each advertiser (`ad-inspiration-collection`). A
pattern carried only by ads found through `validate` searches (our own offer
and research words) is not evidence for those words: the search picked them.
Say which basket each pattern comes from, and trust patterns found through
`map`, `discover` and `snowball` advertisers more.

**Weight by evidence.** Patterns are drawn from `Own` and `A` ads first, then
`B`. `C` and `Unscored` ads only contribute format ideas, never a claim that
an angle or offer "works". `Dropped` ads (and dropped text-only rows) count
**against** a pattern. Say in the report how many ads of each class the
patterns rest on.

The rows hold descriptions, not categories, so the map is built by reading
them: for each component (goal, creative copy, creative concept, offer, angle,
awareness level, problem/desire, argument, CTA), group the descriptions that
are really the same idea under one short pattern name of your own, and count
how many **advertisers** (not ads) use each pattern among strong-evidence ads
(`Own` + `A`), moderate (`B`) and weak (`C` + `Unscored`). Five ads from one
advertiser are one advertiser's style, not an industry pattern. Count only ads whose goal is a lead
or a sale towards what "works"; content ads (articles, events) go in their own
row as format ideas.

| Component | Pattern (your own name, with what unites the ads) | Advertisers: Own + A | B | C + Unscored | Tried and dropped | Example files |
|---|---|---|---|---|---|---|
| Creative concept | "Article teaser over a real house photo" | 2 | 1 | 0 | 1 | `x-A.png`, `y-A.png` |

**Tried and dropped** counts the testing advertisers who ran this pattern and
dropped it. A pattern with more advertisers dropping it than keeping it is not
a pattern worth copying, whatever its A-ads say; one dropped by a single
advertiser is a caution, not a verdict. **Version pairs** are the closest thing
to a competitor's test result: list them, and what they suggest about the
component that differed (often the creative copy's first line or the offer).

A pattern that recurs among strong-evidence lead or sales ads is worth
testing; one seen only in weak ads or content ads is a format idea at most.
For creative copy, note what the first line read does (asks, calls out, states
a number, quotes a customer…) and how long the on-image text is. Then answer in
a few lines:

- Which patterns dominate among the strong ads, and which combinations of them
  (e.g. a call-out question + article-teaser concept + Problem aware)?
- If the set includes the brand's own past ads, what do they tell you about what
  already works — and how can those be extended rather than repeated?
- Which angles suit the brand's category best (see `context/business-info.md`)?

### Combination Analysis

What works is usually a **combination**: a question as the first line may work
in a Problem aware article teaser and fail in a Most aware offer ad. The
Component Map counts components one at a time; this step looks at which
combinations carry the winning signals.

**1. A recipe per ad.** For every ad whose goal is a lead or a sale (content
ads only if they share a format idea), condense its row into a short recipe of
pattern names from the Component Map, in this order:

`first line (what it does) × creative concept × awareness level × problem/desire × offer × argument × CTA`

e.g. `question first line × article teaser × Problem aware × fear of the
electricity bill × no offer × expert explanation × read the article`. Use the
same pattern names as the map, so recipes can be compared. Include `Dropped`
ads and the text-only dropped rows, and note the evidence class and advertiser
of each recipe.

**2. Recurring pairs (and triples).** Look for pairs of components that occur
together in the recipes of **at least two different advertisers** among `Own`
and `A` ads. Count advertisers, not ads. Triples only when they also reach two
advertisers: with a few dozen ads they're rare, so pairs carry most of the
weight. A combination seen with one advertiser only is a **single
observation**, never a pattern.

**3. Counter-evidence.** Check every recurring combination against the
`Dropped` ads and the version pairs. If testing advertisers have dropped it
too, it is **unclear**, not proven. If a version pair shows that changing one
of its components made the ad survive or die, note which.

**4. Signal score.** Give each combination a weighted score over the
advertisers using it (lead/sales goal only):

| Evidence of the advertiser's ad | Points |
|---|---|
| `Own` | +3 |
| `A` | +2 |
| `B` | +1 |
| `C`, `Unscored` | 0 |
| `Dropped` | −2 |

Count each advertiser once per combination, at its strongest class (or −2 if
its only use of the combination was dropped).

**5. The client's own results win.** If `context/learnings.md` already holds a
result for the same combination, it overrides the competitors' signal: say so
next to the score.

Present the result as a ranked table:

| Combination | Advertisers (classes) | Dropped by | Score | Verdict | Library | Example files |
|---|---|---|---|---|---|---|
| question first line × Problem aware | 3 (A, A, B) | 0 | +5 | Pattern | `CPY-002` Supported | `x-A.png`, `y-A.png` |
| price first line × Most aware | 2 (A, B) | 2 | −1 | Unclear | — | `z-A.png` |

The **Library** column names a matching library card and its level. It never
adds to the score: the client's market decides the verdict, the library only
shows whether the same thing holds more widely.

Verdicts: **Pattern** (2+ advertisers, positive score, no more droppers than
users), **Unclear** (droppers as many as users, or mixed), **Single
observation** (one advertiser), **Avoid** (negative score). Ideas in Step 3
can build on a Pattern; they may use an Unclear or Single-observation
combination only as a stated test, never as proof.

### White Space

List what **nobody in the set does**, or does only weakly, that the brand
could own: an offer no competitor leads with, an angle missing from the
category, a proof point only the brand has, a format no one in the category
uses. White space is a hypothesis, not proof: say so, and pair each item with
the brand fact from `context/` that makes it possible.

### Brand Translation

If these files are already in context from earlier in this session, reuse them
rather than re-reading — only read what's missing.

**Before writing any creative copy or ad ideas, read these to
ground copy in real customer language:**

- `context/audience-hypotheses.md` — everything worth testing: audiences, problems, desires, awareness levels, offers, angles, arguments, creative concepts and creative copy, each with its source (`Research` / `Competitor` / `Library` / `Own results` / `Hypothesis`), evidence and status. Weigh ideas that rest on `Draft` research rows, `Unclear` or `Single observation` competitor rows, or `Hypothesis` rows as tests of the row itself
- `context/necessary-beliefs.md` — background: the belief sequence a buyer goes through
- `context/offer-brief.md` — USPs, offer structure, positioning, objections
- `context/customer-deep-research-report.md` — language patterns and what resonates

**Off-limits angles — discard any idea that leads with these, even if the
inspiration ad itself ran it successfully:**

- Ecommerce: Any baseline service-quality claim any ecommerce brand could make

These create zero desire and zero curiosity — they belong on product pages, not
in paid image ads. **Also check `context/offer-brief.md`'s _Off-Limits Claims &
Compliance Notes_** for this brand's own off-limits list, plus its _Stage of
Sophistication_ notes, and apply both.

**For each remaining strong pattern, answer: "How would we do this for our brand?"**
Think through:

- Does this angle create emotional desire or genuine curiosity?
- Ecommerce: What product/flavor would best fit this idea?
- What would the creative copy say, in the brand's voice — above all the first line read?
- What visual treatment would bring it to life using the brand's product imagery (`reference/products/Images/`)?

**What to produce depends on the round type** (from the Starting Point):

| Round type | Ideas to produce |
|---|---|
| **First round / Broad retest** | At least **10 broad ideas**, each its own offer × angle. Cover different offers, angles, emotional registers and awareness levels; creative concepts traditional (see `creative-strategy`'s _When the creative concept matters_), while other concepts seen in strong ads go to the _Creative concepts_ table for a later concept test. In a broad retest, leave out offer × angle pairs that already lost |
| **Narrow test / Keep control** | **6–10 alternatives for the component under test** (e.g. creative copy, creative concepts or arguments seen in strong-evidence ads), each keeping the control's offer × angle, plus **3–5 new-direction ideas** (broad, as in a first round) |

There is no "concept" name: each idea is defined by its components, the same
ones `creative-strategy` puts on its cards, using its Allowed values:

- **Offer** (label from the _Approved Offers_ table) and **Angle** (the idea's
  one primary angle: a short label plus one sentence on the direction it
  takes, and its angle type, reusing the _Angles_ table's labels; these become
  the batch's offer × angle combinations in Phase 2). A call-out or a
  restated offer is not an angle (see `creative-strategy`'s _Angles_)
- Audience (a label from `context/audience-hypotheses.md`, or a new audience marked `New:` when
  the ads show one the file doesn't have) and awareness level
- Problem / desire (a label from the same file, or `New:`) and the objection
  it addresses
- Argument (reason to believe)
- Draft creative copy for the brand: the on-image text, first line first
- Creative concept (described, plus the closest pattern from `creative-strategy`'s list if one fits)
- Recommended CTA
- Source inspiration (which image / brand / pattern inspired it, with its evidence class)

And four fields that make it testable:

- **Hypothesis** — one sentence: "We believe [this idea] will [beat the
  control / get leads below target] because [evidence: which combination and
  its score from the Combination Analysis, which ads and classes, a library
  card ID and level, or which white-space fact]." Name the combination the idea rests on, e.g. "because
  `question first line × Problem aware` is a Pattern (3 advertisers, score +5,
  dropped by none)". A result can then be read as confirming or breaking a
  specific assumption.
- **Status** — `New` / `Variation of [tested ad]` / `Previously lost: [ad]`. A
  previously lost pair is only proposed with a stated reason why this time is
  different.
- **Offer status** — `Approved` (the offer is in the _Approved Offers_ table of
  `context/offer-brief.md` and its last column names who approved it and when;
  use its label) or
  `Needs client approval` (anything the client hasn't promised: a free
  inspection, a discount, a guarantee). Never present an unapproved offer as
  ready to use.
- **Feasibility** — the creative concept's design pattern (from the ad-design
  guide, or "needs custom build") and whether a fitting photo exists in
  `reference/products/Images/` (name the folder, or "no fitting photo").

### Write the test hypotheses

Everything this analysis found worth testing goes into
`context/audience-hypotheses.md`, so the next phases and rounds draw from one
list. Read the file first and write per its tables; a table or the _Source_
column missing from an older file is added with the structure of the hub's
`_template/context/audience-hypotheses.md` (two folders up), existing rows
kept as they are.

**The tables and their columns** (fixed: write them exactly like this, in
this order, and never add a column that links one table to another; a card or
a _Suggested tests_ row is where components are combined):

| Table | Columns |
|---|---|
| Audiences | `Label` · `Who they are (situation, home, stage)` · `Source` · `Evidence` · `Status` |
| Problems | `Label` · `The problem, in the customers' words` · `Source` · `Evidence` · `Status` |
| Desires | `Label` · `The desire, in the customers' words` · `Source` · `Evidence` · `Status` |
| Awareness levels | `Level` · `What the buyer knows at this level (in this category)` · `What the ad opens with` · `Source` · `Evidence` · `Status`. Always five rows, one per level: `Unaware`, `Problem aware`, `Solution aware`, `Product aware`, `Most aware` |
| Offers | `Label` · `The offer (what the customer gets)` · `Source` · `Evidence` · `Client approval` (`Approved` / `Proposed (P-00X)` / `Idea`) · `Status` |
| Angles | `Label` · `Angle type` (one of `creative-strategy`'s fixed types) · `Core message` (the one idea an ad from this angle leaves behind, as a plain statement) · `Viewpoint` (what the ad approaches the topic from: the situation, comparison, fact or tension it starts with) · `Why it could stop the viewer` (the need, doubt or belief it plays on) · `Source` · `Evidence` · `Status`. Described, never as ad copy: no ready sentences or headlines. An audience call-out goes to _Creative copy_, a restated offer to _Offers_; an angle with the same type and core message as an existing row is merged into it |
| Arguments | `Label` · `Argument type` (one of `creative-strategy`'s fixed types) · `The proof` (the specific proof, one line) · `Source` · `Evidence` · `Status`. Only proof the client actually has |
| Creative concepts | `Label` · `Concept` (a name from `creative-strategy`'s list, or a new one, flagged) · `How it is used (what the image shows, what the text does)` · `Source` · `Evidence` · `Status`. Two rows may share a concept when they use it differently |
| Creative copy | `Label` · `First-line device` (the nearest of `creative-strategy`'s fixed devices) · `Pattern` (what the copy does, described) · `Example` (verbatim from the ad, or our draft) · `Source` · `Evidence` · `Status` |
| Suggested tests | `#` · `Combination (components)` · `Source` · `Why (evidence)` · `What a result would tell us` · `Status` |
| Retired | `Label` · `Type` (audience / problem / desire / awareness / offer / angle / argument / concept / copy) · `Retired on` · `Why` |
| Label aliases | `Old label` · `Now` (the label it points to) · `Type` · `Since` · `Why` (merged duplicate / renamed / moved to another registry) |

`Source`: `Research` / `Competitor` / `Library` / `Own results` / `Hypothesis`
/ `AT` (the agency owner's priority: a hypothesis to take seriously, not
evidence; never removed, never rewritten by a skill) (several allowed,
comma-separated). `Status`: `Untested` / `In test` / `In winning combo` /
`In losing combo` / `Won` / `Lost` / `Unclear` (`Won` / `Lost` only from a
component test, see `ads-analytics`). An older Angles table without
`Angle type` and `Core message` gets the two columns added after `Label` and
filled for every row before new rows are written; show the user the types
chosen. In the same way, an older Arguments, Creative concepts or Creative
copy table without `Label` gets the new columns: split `Type — proof` into
`Argument type` and `The proof`, the old concept name into `Concept`, the old
copy pattern into `First-line device` and `Pattern`, and give every row a
label (PascalCase, as in `creative-strategy`'s _Allowed values_). Show the
user the labels chosen.

What to write:

- **What goes in:** components and combinations with the verdict `Pattern`,
  `Unclear` or `Single observation` (the verdict goes in _Evidence_), White
  Space items (Source `Hypothesis`, with the brand fact), Library Gaps
  (Source `Library`, card ID and level), and New to Us items (Source
  `Competitor`). Per component: audiences, problems and desires the ads speak
  to, offers (_Client approval_ `Idea`, unless already approved), angles,
  arguments the client can also show, creative concepts and creative copy
  patterns. Awareness: what the ads show about how buyers at each level are
  addressed goes into that level's row (its _Evidence_, and _What the ad opens
  with_ when the row has none). Recurring combinations go to _Suggested tests_.
- **Evidence:** advertisers and their classes, droppers, the score, the
  basket(s) that found them, example files and the report date, e.g.
  `Pattern: 3 advertisers (A, A, B), dropped by 0, +5 · map · x-A.png · report 2026-10-27`.
- **The same idea already in the file** (from any source): never a duplicate
  row. Add `Competitor` to its _Source_ and the evidence to its _Evidence_.
  If competitors' evidence goes against it, write that in _Evidence_ too.
- **`Avoid` verdicts:** not as new rows. A matching existing row gets the
  counter-evidence in _Evidence_; propose moving it to _Retired_.
- **Never** change a row's _Status_ (that's `ads-analytics`), delete a row, or
  edit a `Research` row's quote. Labels: PascalCase, ASCII only (ä→a, ö→o, å→a), no spaces or hyphens (as
  in `creative-strategy`'s Allowed values), client-specific, reusing existing
  labels.

List what was added and changed in the report (section 9).

---

## Output Format

%this is the output what the next part sees, how and what we iclude in here

Produce an **Ad Inspiration Intelligence Report**. Phase 2 (`creative-strategy`)
builds the brief from it, so every section is something the brief uses:

1. **Starting Point** — round type, control, the component under test (narrow
   test), and the list of already-tested offer × angle pairs and component
   values with their results
2. **Inspiration Inventory** — table of every image analysed this run (filename,
   brand, evidence, goal, offer, angle, creative concept, the creative copy's first
   line, whether a primary text sidecar was present), plus the
   evidence count for the whole set (Own / A / B / C / Unscored)
3. **Component Map** — the table and the short answers from Step 3
3b. **Combination Analysis** — the ranked combination table with scores and
   verdicts, and the version pairs that bear on them
4. **White Space** — what nobody does, with the brand fact that enables it
4a. **Library Gaps** — library patterns (Supported or Proven) that fit the
   client's buying situation but nobody in its market uses: white-space
   candidates with wider evidence behind them
4b. **New to Us** — angles, offers, phrases and framings found in the ads that
   don't appear anywhere in the client's `context/`, with the ads that show
   them: candidates for the "New directions" queue in `learnings.md`
5. **Brand Ad Ideas** — per the round type, component by component, each with
   hypothesis, status, offer status and feasibility. Flag any idea built on a
   pattern that testing advertisers have dropped, and say why it might still
   work for the brand (or leave it out)
6. **Priority Ideas** — 3–5 ideas (their offer × angle pairs, or the
   alternatives for the component under test) for this batch, each with a
   one-sentence rationale tied to its evidence
7. **Open Questions for the Client** — every offer marked `Needs client
   approval` (these are inputs for `offer-development`, which turns them into
   proposals the client can approve), and any missing photo a priority idea
   needs
8. **Missing material (for the agency)** — inspiration ads without a primary
   text sidecar, tiers short of their targets in `ad-inspiration-collection`,
   and whether a refresh is due
9. **Added to the test hypotheses** — the rows added to
   `context/audience-hypotheses.md` per table (with their source), the
   existing rows that got a new source or counter-evidence, and any proposed
   retirements

**Save the report** to `outputs/analytics/ad-inspiration-report-YYYY-MM-DD.md`
(next to the Phase 0 analytics report) and show it in chat. Phase 2 reads the
file if the report is no longer in context, e.g. when the work continues in a
new session.

After logging is complete, state:

> **Ad Inspiration Intelligence Report complete ([round type]). [N] new ads analysed and logged to Google Sheets ([X] already logged, skipped). [I] ideas, [Q] open questions for the client, [H] rows added to `context/audience-hypotheses.md`. Saved to `outputs/analytics/ad-inspiration-report-YYYY-MM-DD.md`. Ready to proceed to Phase 2: Creative Strategy.**
