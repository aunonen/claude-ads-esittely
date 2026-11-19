# Audience Hypotheses — {{BRAND_NAME}}

> **Everything worth testing, in one place: suggestions, not fixed personas.** Audiences, problems, desires and awareness levels, and the other components a card can test: offers, angles, arguments, creative concepts and creative copy. Each row is a hypothesis with its **source** and evidence. Ads test them; results move them between statuses.
>
> Who writes here: `customer-research` (rows from the research, incl. its angles), `competitor-analysis` (rows from competitors' ads and the agency library, after every Phase 1), `ads-analytics` (statuses after every results check, and proposed rows from winning `New:` cards). Write rows by hand too, as `Hypothesis`, or as `AT` for the agency owner's priorities.
>
> **Every table stands on its own.** No table links to another (no audience column in problems, desires or awareness, no awareness column in audiences): a card or a _Suggested tests_ row is where components are combined. The columns are fixed; the skills write them exactly as below (the `competitor-analysis` skill lists them; `customer-research` lists the ones it writes).
>
> **Every row has a label** (first column), in every table: audiences, problems, desires, offers, angles, arguments, creative concepts and creative copy. Awareness levels use their five fixed names, and suggested tests their `#`. Labels go on the brief cards, into creative names and in the Sheet: PascalCase, ASCII only (ä→a, ö→o, å→a), no spaces or hyphens (e.g. `VuotavaKatto`), and kept once in use. Cards may also test something not listed here, marked `New:`; a new row is added when it wins.
>
> **Ratings:** every row is also listed in the internal Sheet's **Komponentit** tab, where the agency owner rates it 1–5 (5 = use this, 1 = don't use). `creative-strategy` syncs the tab from this file before every round and chooses the highest-rated components first. The ratings live only in the Sheet, never in this file.

**Source values** (a row may have several, e.g. `Research, Competitor`; add a source when another one backs the same row, never a duplicate row):

| Source | Where the row comes from | How strong the evidence is |
|---|---|---|
| `Research` | The customer research (`customer-deep-research-report.md`) | Reliability `Confirmed` (the client's own customers, at least 6 sources) · `Supported` (public reviews or the client interview, recurring: at least 15 quotes from at least 6 sources) · `Draft` (forums, media or fewer sources), as defined in `customer-research` |
| `Competitor` | Ads in `reference/ad-inspiration/`, via `competitor-analysis` | The Combination Analysis verdict (`Pattern` / `Unclear` / `Single observation`), advertisers and evidence classes, and the search basket that found them. Found only through `validate` searches = weak (the search picked the words) |
| `Library` | The agency library (`../../library/`), a Library Gap or a style entry | The card ID and its level (`Candidate` / `Supported` / `Proven`) |
| `Own results` | The client's earlier ads (`learnings.md`) | The ads and rounds behind it |
| `Hypothesis` | Our own idea: white space, the client's wish, the user's hunch | None yet. A card built on it tests whether it holds at all |
| `AT` | The agency owner's addition | A priority, not evidence: the pool gives these rows a fair share of cards, but a card built on one says it has no empirical evidence yet. Its example sentences are drafts, not approved claims |

**Status values:** `Untested` · `In test` · `In winning combo` · `In losing combo` · `Won` · `Lost` · `Unclear`. `Won` / `Lost` only from a component test (a challenger that changed just this component); a broad concept test gives its components `In winning combo` / `In losing combo`, because a multivariable win doesn't show which component carried it (see `ads-analytics`).

---

## Audiences (used directly by the skills)

Observable situations, not personalities: what is true of them that an ad can speak to.

| Label | Who they are (situation, home, stage) | Source | Evidence | Status |
|---|---|---|---|---|
| {{e.g. Oil heater}} | {{e.g. "Detached house with an ageing oil boiler, considering a switch"}} | {{Research}} | {{research §Customer segments · Draft}} | Untested |

## Problems (used directly by the skills)

| Label | The problem, in the customers' words | Source | Evidence | Status |
|---|---|---|---|---|
| {{e.g. Boiler at end of life}} | {{"…verbatim…" (research §Language bank)}} | {{Research}} | {{… · Draft}} | Untested |

## Desires (used directly by the skills)

| Label | The desire, in the customers' words | Source | Evidence | Status |
|---|---|---|---|---|
| {{e.g. Worry-free heating}} | {{"…verbatim…"}} | {{Research}} | {{… · Draft}} | Untested |

## Awareness levels (used directly by the skills)

All five levels, always, each described as it looks in this client's category: what a buyer at that level knows and doesn't know about the problem, the solution and this client, and what an ad for them opens with. A level with no evidence yet is still written, as `Hypothesis`.

| Level | What the buyer knows at this level (in this category) | What the ad opens with | Source | Evidence | Status |
|---|---|---|---|---|---|
| Unaware | {{e.g. "Heats with oil as always; doesn't see the boiler's age or the cost as a problem yet"}} | {{e.g. a recognisable moment or a curiosity gap, not the product}} | {{Hypothesis}} | {{…}} | Untested |
| Problem aware | {{…}} | {{…}} | {{Research}} | {{…}} | Untested |
| Solution aware | {{…}} | {{…}} | {{Research}} | {{…}} | Untested |
| Product aware | {{…}} | {{…}} | {{…}} | {{…}} | Untested |
| Most aware | {{…}} | {{…}} | {{…}} | {{…}} | Untested |

## Offers (used directly by the skills)

Offer ideas worth testing. **A card may only use an offer whose _Client approval_ is `Approved`** (it is in the offer brief's _Approved Offers_, same label). `Idea` rows are inputs for `offer-development`, which turns them into proposals for the client (`Proposed (P-00X)`).

| Label | The offer (what the customer gets) | Source | Evidence | Client approval | Status |
|---|---|---|---|---|---|

_Empty until the first Phase 1 or offer development. Approved offers are listed here too, with Source `Own results` or `Hypothesis`._

## Angles (used directly by the skills)

An angle is an ad's single dominant persuasion viewpoint; each card has one primary angle. The angles are specific to this client; their _Angle type_ is one of `creative-strategy`'s fixed types (`Problem` / `Desire` / `Loss` / `RiskReversal` / `Comparison` / `Mechanism` / `Value` / `Credibility` / `Effort` / `BeliefShift` / `Timing` / `Control`). **Described, never written as ad copy:** no ready-made sentences or headlines here; the copy is written on the card. _Core message_: the one idea an ad from this angle leaves behind, as a plain statement. _Viewpoint_: what the ad approaches the topic from (the situation, comparison, fact or tension it starts with). _Why it could stop the viewer_: the need, doubt or belief it plays on. **This table is the client's only angle register:** cards take their angle labels from here, results go into _Status_, and a card's new angle (`New:`) is added when it wins. **Not angles:** an audience call-out (a _Creative copy_ device) and a restated offer (_Offers_). Two rows with the same type and core message are merged; the dropped label goes to _Label aliases_.

| Label | Angle type | Core message | Viewpoint | Why it could stop the viewer | Source | Evidence | Status |
|---|---|---|---|---|---|---|---|

## Arguments (used directly by the skills)

Reasons to believe, each with its own label. _Argument type_ is one of `creative-strategy`'s fixed types (`Social proof` / `Data` / `Guarantee` / `Demonstration` / `Authority` / `Mechanism` / `Testimonial`); _The proof_ is the specific proof in one line. Only proof the client actually has; a competitor's proof is a row only when the client can show the same.

| Label | Argument type | The proof | Source | Evidence | Status |
|---|---|---|---|---|---|

## Creative concepts (used directly by the skills)

Formats worth testing for this client, each with its own label: _Concept_ is a name from `creative-strategy`'s list (or a new one, flagged), and the row says how this client's ads use it. Two rows may share a concept when they use it differently.

| Label | Concept | How it is used (what the image shows, what the text does) | Source | Evidence | Status |
|---|---|---|---|---|---|

## Creative copy (used directly by the skills)

Copy patterns, each with its own label: _First-line device_ is the nearest of `creative-strategy`'s fixed devices, _Pattern_ says what the copy does, and _Example_ is verbatim from the ad, or our draft.

| Label | First-line device | Pattern | Example | Source | Evidence | Status |
|---|---|---|---|---|---|---|

## Suggested tests (prioritised)

Combinations worth testing first, with the reason: any components, e.g. audience × problem × awareness from the research, or a recurring combination from the Combination Analysis. `creative-strategy` uses this list when building a first round or a new direction.

| # | Combination (components) | Source | Why (evidence) | What a result would tell us | Status |
|---|---|---|---|---|---|
| 1 | {{label × label × level}} | {{Research}} | {{…}} | {{…}} | Untested |

## Retired

Rows that lost repeatedly or turned out not to exist, with the date and why: kept so they aren't proposed again without a reason. _Type_: audience / problem / desire / awareness / offer / angle / argument / concept / copy. Competitor patterns with the verdict `Avoid` go here too.

| Label | Type | Retired on | Why |
|---|---|---|---|

## Label aliases

Old labels that still appear in the Sheet, earlier briefs or creative names, and the label they now point to. `ads-analytics` and `creative-strategy` read an old label as its new one, so history stays comparable. _Why_: merged duplicate / renamed / moved to another registry (e.g. an audience call-out moved to _Creative copy_).

| Old label | Now | Type | Since | Why |
|---|---|---|---|---|
