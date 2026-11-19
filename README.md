# Meta Ads Creative Workspace for Claude Code

> **Esittelyversio.** Tämä on julkinen kopio yhden hengen Meta-mainostoimiston Claude Code -työtilasta. Asiakkaiden kansiot, Google Drive -tunnisteet, yhteystiedot ja kolmansien osapuolten mainoskuvat on poistettu. Esimerkkiasiakkaana on toimiston oma työtila (`clients/own business/`), ja `sites/meta-mainonta/` sisältää toimiston laskeutumissivun. Varsinaiset taidot (skills) ovat erillisessä repossa (`~/.claude/skills/`).

**Agency edition:** one workspace per client, with the pipeline shared across all of them. See *Agency setup* below.

An end-to-end system that turns Claude Code into your static-ad creative team. It studies winning ads, writes a creative strategy grounded in your customer research, generates on-brand image ads from the client's own photos in every Meta placement size, and builds them into a **paused** campaign in Meta Ads Manager, ready for you to review.

```
 Ad inspiration ──► Creative strategy ──► ✋ You approve the brief
                                                  │
 Paused Meta campaign ◄── ✋ You approve the images ◄── Image generation (SQ / VT / HZ)
```

> ⚠️ **Nothing ever goes live automatically.** Every campaign, ad set and ad is created **PAUSED**. A human has to activate it in Ads Manager before a single cent is spent.

---

## What's inside

| Phase | Skill | What it does |
|---|---|---|
| 0 | `ads-analytics` | Reads the earlier ads' results, classifies each as winner / promising / loser / inconclusive, names the control and the next round type |
| 1 | `competitor-analysis` | Reads every new ad in `reference/ad-inspiration/` (image + primary-text sidecar), describes it component by component in the internal inspiration Sheet, maps the patterns by evidence and advertiser count, and writes ideas that fit the round, each with a hypothesis |
| 2 | `creative-strategy` | Writes a Test Plan sized to the budget (how many ads one round can test, what they test) and a ~20-card pool (every component, headline, primary text, photo, visual direction, logo/badge decisions) with a recommended selection, scored against a 6-principle static-ad framework |
| ✋ | Brief review | You pick the cards for the test (`recommended`, or `1,7,14, change #7's headline to "…"`); Claude warns if the pick doesn't fit the budget or the test, but you decide |
| 3 | `creative-generation` | Designs each approved card as an HTML layout on the client's own photos and renders it to PNG in square (1:1), vertical (9:16) and horizontal (16:9) with Chrome/Edge, then uploads to Drive and logs to Sheets. No AI-generated imagery, so nothing for Meta's AI label to pick up |
| ✋ | Ad review | You look at every ad and ask for changes (bigger headline, other photo, different crop), applied in seconds |
| 4 | `meta-ads-campaign-setup` | Builds an ABO testing campaign (one ad set per ad, equal share of the total budget), uploads all three sizes per ad with placement-specific mapping, and uses each card's approved primary text and headline (one per ad, so results stay traceable). Sales or leads, website or instant form, from the config. **All PAUSED.** |

Also included:
- **`/new-client`**: creates a new client workspace from the template
- **`/onboard`**: an interactive setup that configures everything for one client brand
- **`/prime`**: loads your context at the start of each session
- **`/create-plan`** + **`/implement`**: plan and make changes to the workspace itself
- **`ad-inspiration-collection`**: say "collect ad inspiration" in a client folder and Claude searches Meta's Ad Library by relevance tier, scores each ad's evidence and goal, and saves image + sidecar + evidence-log row
- A **starter set** of format examples in `reference/ad-inspiration/_starter-formaatit/` (other categories; never used as evidence). *Not included in this showcase copy: the images are other brands' ads.*

---

## Prerequisites

| You need | Why | Notes |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) | Runs the whole system | A paid Claude plan |
| **Chrome or Edge** + **Python 3** | Renders the HTML ad designs to PNG (`~/.claude/skills/ad-design/render.py`) | Already on most computers; no extra packages |
| **Meta Ads connector** | Creates campaigns, ad sets and ads | Connect in claude.ai → Settings → Connectors |
| **Meta System User access token** | Uploads images to your ad account | Permissions `ads_management` + `ads_read`. `/onboard` walks you through it |
| **Google Workspace CLI (`gws`)** | Logs inspiration + creatives to Google Sheets, uploads images to Drive | See [googleworkspace/cli](https://github.com/googleworkspace/cli), then authenticate with your Google account |
| A Meta ad account, Pixel and Facebook Page | Where the campaign gets built | You'll need their IDs |

---

## Agency setup

```
Claude ads/                      ← agency hub: open a session here to add clients or change the setup
├── CLAUDE.md                    ← agency context (loaded in every client session too)
├── README.md                    ← this file
├── _template/                   ← clean client workspace, copied by /new-client
└── clients/
    ├── acme-oy/                 ← open a session HERE to make Acme's ads
    └── ...

~/.claude/skills/                ← the pipeline, shared by every client
~/.claude/commands/              ← /new-client, /onboard, /prime, /create-plan, /implement
~/.claude/settings.json          ← the agency's META_ACCESS_TOKEN
```

**Why one folder per client:** each client's brand assets, claims, proof figures and customer research stay isolated, so one client's claims can never end up in another client's ad. The skills live once at user level (`~/.claude/`), so an improvement reaches every client at once.

**Meta token:** if clients share their ad accounts to your agency's Business Manager, one System User token covers them all. Put it in `~/.claude/settings.json` as `{"env": {"META_ACCESS_TOKEN": "..."}}`, and assign the System User to each client's ad account and Page. A client that gives access through its own Business Manager gets its own token in `clients/<slug>/.claude/settings.local.json`, which overrides the agency token.

**Google:** each client gets its own Sheet and Drive folders, which you can share with the client for approvals.

---

## Quick start

1. **Once:** fill in the agency section of the hub `CLAUDE.md` (or ask Claude to do it with you).
2. **New client:** open a session in the hub and run **`/new-client Acme Oy`**. This creates `clients/acme-oy/`.
3. **Open a new session in the client folder** and run **`/onboard`**. Claude interviews you (brand, colours, fonts, products, USPs, proof, Meta IDs, Google Sheet) and fills in every config file. Give it the client's website URL and it will pre-fill much of this for you.
4. **Add the client's assets** in their folder:
   - `reference/design-assets/`: the full logo lockup (icon + wordmark, transparent PNG) plus any icons, backgrounds or press logos. See the folder's README.
   - `reference/products/Images/`: one folder per product with packshots and lifestyle images. See the folder's README.
   - `reference/ad-inspiration/`: run **"collect ad inspiration"** (the `ad-inspiration-collection` skill) and add the client's own past ads with their results.
5. **To make ads:** start a fresh session in the client folder, run `/prime`, and say **"let's make some new ads."**

---

## Where everything lives (inside each client folder)

```
CLAUDE.md                        ← Brand Assets (colours, fonts, logo) + workspace guide
context/
  business-info.md               ← who the client is, services/products, area, proof figures
  personal-info.md               ← your agency's role for this client
  strategy.md                    ← the client's goals, priorities and Ad Targets (target CPL)
  offer-brief.md                 ← ⭐ approved offers, USPs, CTAs, social proof, objections, real deadlines, off-limits claims, service details
  audience-hypotheses.md         ← everything worth testing (audiences, problems, desires, awareness, offers, angles with angle type and core message, arguments, concepts, copy), each with source, evidence and status, plus label aliases
  necessary-beliefs.md           ← background: the belief sequence a buyer goes through
  customer-deep-research-report.md ← research with market context and a reliability level per section (customer-research skill)
  research-sources.md            ← every research source and client interview
  offer-proposals.md             ← offer proposals and the client's decisions (offer-development skill)
  learnings.md                   ← what earlier rounds showed; updated by ads-analytics after every results check
reference/
  meta-ads-config.json           ← ad account, pixel, page, budget, countries, landing pages
  gws-config.json                ← Google Sheet + Drive folder IDs
  ad-inspiration/                ← swipe file
  design-assets/                 ← logo, icons, backgrounds
  products/Images/               ← product photography, one folder per product
outputs/analytics/               ← results reports and Intelligence Reports
outputs/generated-assets/        ← the brief, state file and generated images (git-ignored)
.claude/settings.local.json      ← only if this client has its own META_ACCESS_TOKEN (git-ignored)
```

**The golden rule:** the skills only ever use claims that are written in `context/`. If a USP, certification, review count or press mention isn't in `offer-brief.md` or `business-info.md`, it won't appear in an ad. The more accurate and specific those files are, the better the ads.

---

## Google Sheet layout

`/onboard` can create these for you. Each client has **two spreadsheets**: a log that may be shared with the client, and an internal one for competitor analysis that never is.

**Client log** `<Client> – mainosloki`:

**Creative Generations** (columns A–T, one component per column; defined in `creative-generation`; the skills read columns by header name and append missing trailing headers to older tabs)

| Creative Name | Offer | Angle | Tests | Audience | Awareness Level | Problem / Desire | Argument | Creative Concept | CTA | Creative Copy | Design File | Drive Link | Primary Text | Ad Headline | First-Line Device | From Hypotheses | Angle Type | Test Scope | Supporting Elements |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Tarjousehdotukset** (offer proposals for the client, written by `offer-development`, which creates the tab if missing)

| ID | Ehdotus | Mitä asiakas saa | Osat | Mitä vaatii teiltä | Vastaa huoleen | Peruste | Ehdotettu testi | Tila | Päivä | Kommentti / hyväksyntä |
|---|---|---|---|---|---|---|---|---|---|---|

**Brief** (columns A–AC, one row per brief card, all batches; defined in `create-new-ads`)

| Batch | # | Creative | Status | Role | Tests | Hypothesis | Offer | Angle | Audience | Awareness Level | Problem / Desire | Argument | Creative Concept | Creative Copy | Ad Headline | Primary Text Plan | Primary Text | CTA | Photo | Layout | First-Line Device | Alternates | From Hypotheses | Angle Type | Test Scope | Supporting Elements | Coherence | Message Hierarchy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Internal inspiration** `<Client> – mainosinspiraatio (sisäinen)`:

**Ad Inspiration** (columns A–R, described in the analyst's own words; defined in `competitor-analysis`)

| Filename | Brand | Evidence | Goal | Creative Copy | Primary Text | Creative Concept | Offer | Angle | Audience | Awareness Level | Problem / Desire | Argument | Creative Execution | CTA | Drive Link | Why It Might Work | Angle Type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Komponentit** (every component of `context/audience-hypotheses.md`, one row each, for your 1–5 ratings; `creative-strategy` creates and syncs it before every round and chooses the highest-rated components first; it never touches _Arvio_ or _Kommentti_)

| Tyyppi | Tunniste | Kuvaus | Lähde | Näyttö | Tila | Arvio (1–5) | Kommentti | Päivitetty |
|---|---|---|---|---|---|---|---|---|

Arvio: **5** käytä tätä · **4** vahva · **3** / tyhjä neutraali (näyttö ratkaisee) · **2** heikko, vain tarvittaessa · **1** älä käytä.

Then put both spreadsheet IDs and the two Drive folder IDs (generated assets, ad inspiration) into the client folder's `reference/gws-config.json`. Each inspiration ad's primary text goes in a `.txt` sidecar next to its image (see `reference/ad-inspiration/README.md`).

### `gws` setup on this machine (done once, 2026-10-24)

- Installed with `npm install -g @googleworkspace/cli`.
- Authenticated with the agency's Google account through its own Google Cloud project (`Claude ads`, Sheets + Drive APIs, Desktop-app OAuth client, account added as a test user). The OAuth client file must be named exactly `C:\Users\merik\.config\gws\client_secret.json`: Google downloads it as `client_secret_<id>.json`, which `gws` doesn't find.
- Log in with `gws auth login -s drive,sheets`, opening the printed link in your own browser (the redirect goes to localhost). `gws auth status` shows whether you're logged in.
- Each client gets a Drive folder `Claude ads – <Client>` containing `Generoidut mainokset/`, `Mainosinspiraatio/` and the spreadsheet `<Client> – mainosloki`.

---

## Optional: shell aliases

Add to `~/.zshrc` (or `~/.bashrc`), then run `source ~/.zshrc`:

```bash
alias cs='claude "/prime"'                                   # Claude Safe: asks before acting
alias cr='claude --dangerously-skip-permissions "/prime"'    # Claude Run: no permission prompts
```

- **`cs`** gives you oversight. It's good for unfamiliar tasks or for learning what Claude is doing.
- **`cr`** gives you speed for familiar workflows. Use it with care: Claude won't ask before running commands.

---

## Customising

- **Change the rules for every client:** the skills are plain Markdown in `~/.claude/skills/`. Edit them directly, or run `/create-plan <change>` then `/implement` from the hub so the docs stay in sync.
- **Change the rules for one client:** write it into that client's `context/` files (e.g. off-limits claims in `offer-brief.md`), not into a skill.
- **Change what new clients start with:** edit `_template/`. Existing client folders don't update automatically.
- **How many ads one round tests:** the client's `campaign_daily_budget_total` ÷ `min_daily_budget_per_ad` in `reference/meta-ads-config.json`. Target CPL in `context/strategy.md` → _Ad Targets_.
- **Pool size, logo frequency, badge frequency:** set in `creative-strategy` and `static-ads-strategy`.
- **Budget, countries, CTA:** the client folder's `reference/meta-ads-config.json`.
- **Ad look and layouts:** per client in `reference/brand/brand.css`; for all clients in `~/.claude/skills/ad-design/` (`design-guide.md`, `base.css`).

### Version control (git)

Two git repos record every change so it can be reviewed or undone. Both have a **private** GitHub remote (account `aunonen`), so the system can be used on another computer:

| Repo | GitHub | Tracks | Left out |
| --- | --- | --- | --- |
| `Claude ads/` (this folder) | `aunonen/claude-ads` | `CLAUDE.md`, README, `_template/`, each client's `context/`, `plans/`, configs, brand files | Client photos (`reference/products/Images/`), inspiration images, generated output, secrets |
| `~/.claude/` | `aunonen/claude-skills` | Only `skills/` and `commands/` | Everything else, including `settings.json` with the Meta token |

After you edit the system yourself, ask Claude to "check the changes for consistency": it reads `git diff` in both repos and checks that the skills, docs and `_template/` still match. Commit once you're happy, so the next diff only shows new changes, and push when you want the other computer to get them.

**Another computer:** install git and `gh`, run `gh auth login`, then clone `aunonen/claude-ads` to `Documents/Claude ads` and `aunonen/claude-skills` into `~/.claude` (if `~/.claude` already exists there, clone elsewhere and copy `skills/`, `commands/`, `.gitignore` and `.git/` in). Then add what git leaves out: `~/.claude/settings.json` with the Meta token, each client's photos (`reference/products/Images/`) and inspiration images. Before working, `git pull` in both; after, commit and `git push`.

---

## Customer research and offers

- **`customer-research`** ("tutki asiakkaat", "päivitä tutkimus", "kuinka luotettava tutkimus on"): researches every client the same way and equally wide: first a starting-situation map (every situation a customer could buy from: customer types, what they move from, triggers), so the audiences don't narrow to the one route the offer points at; then a source map of six groups with minimums (the client's own reviews and interview, competitors' reviews, at least three forums, customer stories, media and authorities, search questions), a standard set of search terms, fixed research questions, market context with dated facts, breadth targets (3–5 segments, 8–15 problems, 5–8 desires, 30+ quotes) and a coverage check. Single-source findings and interpretations are kept but marked. Every section gets a reliability level (`Confirmed` / `Supported` / `Draft`), quotes are verbatim with their source, and no personal data is stored. Writes the research report, `audience-hypotheses.md` and `research-sources.md`.
- **`offer-development`** ("kehitetään tarjouksia"): builds offer proposals from what the client can actually deliver, the four value levers and offer components, with evidence from competitors, the library and own results. Proposals go to `offer-proposals.md` and the client log's **Tarjousehdotukset** tab; approved ones move to the offer brief. Runs as Phase 1.5 when fewer than 3 offers are approved or Phase 0 recommends an offer test.

## Agency ad library

`library/` in the hub is the agency's shared knowledge of what works in high-value service ads: public Meta ads that pass a strict evidence gate (lead or sales goal, class A with two independent signals, a testing advertiser, still running at a recheck), turned into **pattern cards** (offers, angles, creative concepts, creative copy devices, formats) with 2–3 references each, and a **style library** (language and visuals). Each pattern has a confidence level (Candidate → Supported → Proven, or Fading), and levels change only when you approve them. Details: `library/README.md`.

Run it in a **hub session** with the `ad-library` skill:

- **"Kerää kirjastoon [ala]"**: collects ads for a category (same browser method and scoring as `ad-inspiration-collection`)
- **"Tarkista kirjasto"** (monthly): rechecks every logged ad; still running with growing reach → Confirmed
- **"Päivitä kirjaston kuviot"**: writes/updates pattern cards and style entries and proposes level changes for you to approve
- **"Kirjaston tila"**: status report

Client sessions use the library automatically: `competitor-analysis` reads fitting patterns as tier-3 evidence (weaker than the client's own results and market), `creative-strategy` uses them as a menu by level, and `ads-analytics` writes "Kirjastopalaute" lines (pattern ID, won/lost, date) that you add to the library in a hub session. Nothing about a client beyond those lines ever goes into the library.

## Notes

- The ads in `reference/ad-inspiration/` belong to their respective brands. They're included only as reference for creative analysis, so don't reuse them in your own ads.
- Ads are only as good as the client's photos. Ask clients for plenty of real, large photos of their work, and check spelling and crops at the review checkpoint.
- You're responsible for making sure your ads comply with Meta's advertising policies and the regulations in your category.
