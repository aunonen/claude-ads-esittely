# Onboard

> One-time setup that configures a **client workspace** for one client brand. The user is an agency running Meta ads for several clients; each client has its own folder under `clients/`, created by `/new-client`. Interview the user about the client, then write their answers into the right files. Safe to re-run: if a file is already filled in, show what's there and only change what the user wants to update.

**Check where you are first.** If the current directory has no `context/` folder (e.g. it's the agency hub or `_template/`), stop: tell the user to run `/new-client <name>` from the hub and then open the new client folder in a fresh session. Never onboard a client into `_template/`.

The agency's own details (who they are, how they work) live in the hub `CLAUDE.md` one level up, which is loaded automatically. Use it to pre-fill the agency's role in `context/personal-info.md` instead of asking again.

## Variables

section: $ARGUMENTS (optional — e.g. `brand`, `offer`, `meta`, `google`. If given, run only that round, then the readiness check.)

---

## How to run this

- Start by explaining in 3–4 lines what's about to happen: six short rounds, about 15–30 minutes, and what they'll have at the end.
- Ask **one round at a time**, in plain conversation. Group questions so each round is one message, not twenty. `AskUserQuestion` is fine for genuine multiple-choice items (e.g. currency); free-text answers go in normal chat.
- If the user gives a website URL, use `WebFetch` on it (homepage, product pages, about page, reviews) to **pre-fill draft answers**, then ask them to confirm or correct. Don't make them type what you can read.
- **Never invent claims, numbers, certifications, press mentions or reviews.** If something isn't confirmed by the user or clearly stated on their own site, leave it out. Everything in `context/offer-brief.md` can end up in a live ad.
- Write each file at the end of its round, then show a short summary of what was written.
- Leave a `{{…}}` placeholder in place (don't delete it) for anything the user wants to skip, so the readiness check flags it.

---

## Round 1 — Business & role

Ask for: brand name, website, what they sell and who it's for, positioning/differentiation, sales channels, real proof figures (review count, customer count), genuine press coverage, the agency's role and scope for this client (and the client contact who approves creatives), and the client's current goals for Meta ads (current vs. target ROAS, creative volume per week, share of revenue, hours spent). Ask specifically for the **target CPL** (lead gen) or **target CPA / ROAS** (store) and what counts as a qualified lead: the skills size every test and judge every ad against it.

Write:
- `context/business-info.md`
- `context/personal-info.md`
- `context/strategy.md` (including the _Ad Targets_ section)

## Round 2 — Brand identity

Ask for:
- Primary, secondary/light-background, background and text colours (hex). Offer to pull them from the website CSS if they don't know.
- **Headline font** and **body font** names. Offer to read them from the website CSS. The ads are rendered as HTML, so the real font is used: if it's on Google Fonts, build the `@import` URL; if it's a licensed font, ask them to put the font files (`.woff2`/`.ttf`/`.otf`) in `reference/brand/fonts/` and write `@font-face` rules. If neither is possible, pick the closest Google Font together with the user. Check the fonts include ä, ö, å.
- **Logo:** ask them to put their full logo lockup (transparent PNG or SVG) in `reference/design-assets/`, ideally both a dark and a light (white) version so it reads on any photo. Confirm the filenames with `ls`.

Write: the **Brand Assets** table in `CLAUDE.md` (replace every `{{…}}` in that section, and update the Setup status note if everything is filled) **and** `reference/brand/brand.css` (colours, fonts, font loading). Then render a quick font test to confirm the fonts load: a one-off design in `outputs/generated-assets/designs/_brand-test.html` with the headline and body fonts, colours and logo on a client photo (or plain background if none yet), rendered with `python ~/.claude/skills/ad-design/render.py ... --sizes sq`. Show it to the user, then delete the test files.

## Round 3 — Products & offer

Ask for:
- **Service business:** the services to advertise, what's included, the process (contact → survey → quote → job), service area, timeline, price range, financing and subsidies (e.g. household tax credit), warranties, certifications and licences, capacity and seasonality, and jobs they don't want. **Online store:** products, specs, variants, pricing, subscription terms, guarantee and shipping
- **Approved offers**: every offer the client agrees to run, each with a short label, the exact offer, its components (core, risk reversal, time, bonus, scope), terms, validity and who approved it. Also ask what the client **could** promise for future offers: guarantees, price commitments, install times, bonuses, capacity (this feeds `offer-development`). The offer is the component the ads test most, so get 2–4 if the client can stand behind them (e.g. a free survey, a fixed-price quote, a tax-credit calculation)
- **Approved USPs** (5–8), each with a matching emoji
- **Approved CTA sentences** (3–5, evergreen)
- **Real deadlines & seasonality**: only real, dated reasons to act now (subsidy end dates, booking cut-offs before a season), or none
- **Social proof assets**: exact wording only, plus which design-asset file goes with each (if any)
- **Top objections** and how they'd answer each
- **Off-limits claims**: regulated health claims, legal sensitivities, words to avoid
- Market sophistication (how claim-fatigued is the category?)

Write: `context/offer-brief.md`. Fill every section marked *(used directly by the skills)* first, then as much of the strategic sections (big idea, UMP/UMS, awareness, etc.) as the user can give. Offer to draft the rest for their review.

Then the research: run the `customer-research` skill in **initial** mode (`Skill({"skill": "customer-research"})`). It gives the user a client interview script (by phone; the client reads out real customer messages and questions where they can), researches public sources with a starting-situation map (every situation a customer could buy from) and its fixed source map (six groups with minimums, standard search terms, market context, coverage check) without waiting for the interview, and writes, with a reliability level for every section and no personal data:
- `context/customer-deep-research-report.md` (language bank with verbatim quotes and sources)
- `context/audience-hypotheses.md`: the audiences, problems and desires worth testing, all five awareness levels as they look in this category, the research's angles, and a prioritised list of suggested tests, with Source `Research`; the objections go to the offer brief's _Objections & Creative Responses_. The tables don't link to each other (no audience column). Suggestions, not fixed personas. Its other tables (offers, arguments, creative concepts, creative copy, and more angles) fill from Phase 1 onwards
- `context/necessary-beliefs.md` (background)
- `context/research-sources.md`

If the interview can't happen yet, the skill drafts from public sources and marks everything `Draft`; run its **update** mode after the interview.

Leave `context/learnings.md` as the empty template: `ads-analytics` fills it from the first results on.

Tell them what is `Confirmed`, `Supported` and `Draft`, and that the client interview is the fastest way to raise it.

Then ask them to add the client's own photos to `reference/products/Images/<folder>/` per `reference/products/README.md`: product shots for an online store; for a service business, photos of finished projects, before/after pairs, the team at work, vehicles or premises, one folder per service or project type. These photos are the raw material of every ad (nothing is AI-generated), so more and better photos mean better ads. Descriptive filenames help (e.g. `kylpyhuone-ennen.jpg`, `kylpyhuone-jalkeen.jpg`). Note anything worth knowing in that README (e.g. which photos the client doesn't want used).

## Round 4 — Meta Ads account

Ask for:
- **How the ads convert:** sales on a website (`objective: OUTCOME_SALES`, `conversion_location: website`), leads on a website form (`OUTCOME_LEADS` + `website`), or leads with a Meta instant form (`OUTCOME_LEADS` + `instant_form`). Service businesses are usually the last one.
- Ad account ID (digits only, no `act_`), Facebook Page ID, and the Pixel ID (`website` only) or the instant form's ID (`lead_form_id`, `instant_form` only: Page → Publishing tools → Instant forms). Point them to Meta Business Settings → Accounts / Data sources. If IDs aren't available yet, write `null`: phases 0–3 work without them and Phase 4 stops and lists what's missing.
- Targeting area: whole countries, or a radius around a city for a local business (`geo_targeting`).
- Currency and symbol, target countries, the **total daily budget for the test campaign** (`campaign_daily_budget_total`, the whole campaign, not per ad) and the **minimum daily budget per ad** (`min_daily_budget_per_ad`, default 5). Total ÷ minimum = how many ads one round can test; tell the user the number
- Conversion event (`website` only: Purchase for a store, Lead for a website form), CTA button (`cta_type`: `SHOP_NOW` for a store, usually `GET_QUOTE` or `SIGN_UP` for leads) and attribution (default 7-day click, 1-day view)
- Website domain, display link, and landing pages: map each photo folder (product or service) or offer label to its URL, plus a default. Verify each URL loads with `WebFetch`.

Write: `reference/meta-ads-config.json`.

Then the access token. First check whether one is already set (`[ -n "$META_ACCESS_TOKEN" ] && echo set`, never print the value). Ask how this client's ad account is accessed:

- **Shared to the agency's Business Manager** (the usual case): the agency's System User token in `~/.claude/settings.json` covers it. If no token is set yet, this is the first client: walk them through creating the agency token once. The only per-client step is assigning the agency's System User to this client's ad account and Page.
- **Client's own Business Manager with a separate token**: that token goes in this client folder's `.claude/settings.local.json` (git-ignored), which overrides the user-level one.

Creating a **System User** token: Business Settings → Users → System Users → Admin → Generate token with `ads_management` + `ads_read`; assign the system user to the ad account and Page. Ask them to paste it into the right file **themselves**, as `{"env": {"META_ACCESS_TOKEN": "..."}}`, or offer to write that file for them. **Never write the token into a client folder's `settings.json` or any other tracked file**, and don't echo it back in chat. Remind them to restart Claude Code afterwards so it loads.

Also confirm the **Meta Ads connector** is connected in Claude (it provides the `ads_*` tools). If it isn't, tell them to connect it via claude.ai → Settings → Connectors.

## Round 5 — Google Sheets & Drive

Check `gws` is installed (`which gws`). If it isn't, point them to the README's Google Workspace CLI section and continue.

Each client gets **its own** Sheets and Drive folders (never share one across clients), ideally inside the agency's Drive under a folder named after the client. There are **two spreadsheets**, because one may be shared with the client and the other must not:
- **Client log** `<Client> – mainosloki` (may be shared with the client for approvals), two tabs:
  - **Creative Generations** (A–Q): `Creative Name | Offer | Angle | Tests | Audience | Awareness Level | Problem / Desire | Argument | Creative Concept | CTA | Creative Copy | Design File | Drive Link | Primary Text | Ad Headline | First-Line Device | From Hypotheses`
  - **Tarjousehdotukset**: `ID | Ehdotus | Mitä asiakas saa | Osat | Mitä vaatii teiltä | Vastaa huoleen | Peruste | Ehdotettu testi | Tila | Päivä | Kommentti / hyväksyntä` (offer proposals for the client; written by `offer-development`, which also creates the tab if missing)
  - **Brief** (A–X): `Batch | # | Creative | Status | Role | Tests | Hypothesis | Offer | Angle | Audience | Awareness Level | Problem / Desire | Argument | Creative Concept | Creative Copy | Ad Headline | Primary Text Plan | Primary Text | CTA | Photo | Layout | First-Line Device | Alternates | From Hypotheses`
- **Internal inspiration** `<Client> – mainosinspiraatio (sisäinen)` (agency only, never shared), two tabs:
  - **Ad Inspiration** (A–Q): `Filename | Brand | Evidence | Goal | Creative Copy | Primary Text | Creative Concept | Offer | Angle | Audience | Awareness Level | Problem / Desire | Argument | Creative Execution | CTA | Drive Link | Why It Might Work`
  - **Komponentit**: `Tyyppi | Tunniste | Kuvaus | Lähde | Näyttö | Tila | Arvio (1–5) | Kommentti | Päivitetty` (every component of `context/audience-hypotheses.md`, which the user rates 1–5; synced and read by `creative-strategy`, which also creates the tab if missing)
- A Drive folder for generated assets (briefs go here too), and one for ad inspiration

If they'd like you to create these and `gws` is authenticated, create both spreadsheets, their tabs and header rows and the two folders, then capture their IDs.

Write: `reference/gws-config.json`.

## Round 6 — Readiness check

Run these checks and print a ✅/⚠️ checklist:

1. `grep -n "{{" CLAUDE.md context/*.md reference/*.json reference/brand/brand.css`: list every unfilled placeholder, grouped by file. Placeholders in the strategic sections of the offer brief are ⚠️ (nice to have). Placeholders in Brand Assets, `brand.css`, every *(used directly by the skills)* section of the offer brief, the *(used directly by the skills)* tables of `audience-hypotheses.md`, the _Ad Targets_ section of `strategy.md`, `meta-ads-config.json` or `gws-config.json` are ❌ (they block the workflow).
2. The primary logo file named in Brand Assets exists in `reference/design-assets/`
3. `reference/products/Images/` has at least one folder containing at least one photo
4. `reference/ad-inspiration/` has collected ads with an `_evidence-log.md` (the `_starter-formaatit/` examples don't count). If not, ⚠️: suggest running the `ad-inspiration-collection` skill before the first batch
5. `META_ACCESS_TOKEN` is set (`[ -n "$META_ACCESS_TOKEN" ] && echo set`, without printing the value)
6. Ad rendering works: `python ~/.claude/skills/ad-design/render.py --help` runs and a Chrome or Edge browser is installed (the brand test render in Round 2 counts as proof)
6b. Meta Ads connector available (`ads_get_ad_accounts`)
7. `gws` installed and authenticated

Finish with what to do next: fix any ❌ items, then start a fresh session (`/prime`) and say **"let's make some new ads."** Remind them that the workflow only ever creates **PAUSED** campaigns, so nothing spends until they activate it in Ads Manager.
