---
name: ads-analytics
description: >
  Reads the brand's live Meta ad results and classifies every ad as winner,
  promising, loser or inconclusive, using fixed metrics and minimum-data rules,
  so decisions are made on evidence rather than impressions. Produces an
  Analytics Report that names the current control (benchmark) and which branch
  of creative-strategy's testing logic applies next. Invoke before every new ad
  round (creative-strategy requires it), or whenever the user asks how the ads
  are doing, which ad is winning, or what to test next.
---

# Ads Analytics — Decision Metrics

The job of this skill is to decide, per ad: **is it a winner, is it promising,
is it losing, or is it too early to tell?** It never changes anything in Meta:
it only reads results.

> ⚠️ **Skeleton.** The structure is final; the numeric thresholds marked
> **PROVISIONAL** are starting defaults for small lead-gen budgets, to be tuned
> with real data. Client-specific targets (target CPL, lead-quality criteria)
> never go in this file: they belong in the client's `context/strategy.md`.

---

## Step 1 — Read Targets

Read from the client folder:

- `reference/meta-ads-config.json`: `ad_account_id`, `objective`, budget fields
- `context/strategy.md` → _Ad Targets_: **target CPL** (cost per lead) or, for
  a store, target CPA / ROAS, and what counts as a qualified lead

If there is no target CPL/CPA, stop and ask the user for one, and suggest
adding it to `context/strategy.md`. Every rule below is relative to it.

If `ad_account_id` is missing (`null` or `{{…}}`), stop: there are no results
to read yet.

## Step 2 — Fetch Results

Pull ad-level results through the Meta Ads connector's insights tool, or the
Graph API with `$META_ACCESS_TOKEN` (never print the token):

```bash
curl -s -G "https://graph.facebook.com/v21.0/act_${AD_ACCOUNT_ID}/insights" \
  -H "Authorization: Bearer $META_ACCESS_TOKEN" \
  --data-urlencode "level=ad" \
  --data-urlencode "date_preset=maximum" \
  --data-urlencode "fields=ad_id,ad_name,adset_name,campaign_name,spend,impressions,reach,frequency,inline_link_clicks,inline_link_click_ctr,cost_per_inline_link_click,cpm,actions,cost_per_action_type"
```

Leads are the `actions` entries with `action_type` `lead` (instant forms may
report `onsite_conversion.lead_grouped`; use whichever the account returns, and
never count both). Restrict to the campaigns this workflow created
(`campaign_name_prefix` from config).

**Attach the components.** Read the Creative Generations tab of the Sheet
(`reference/gws-config.json` → `spreadsheet_id`), SQ rows only. Match each Meta
ad to its row by name: the ad name `[Offer]-[Angle]-[Variant]_[DD/MM/YYYY]` is
the row's Creative Name without the `-SQ` size suffix and with the date
written `DD-MM-YYYY`. That gives every ad its offer, angle, angle type, what
it tests, test scope, audience, awareness level, problem/desire, argument,
supporting elements, creative concept, CTA, creative copy and first-line
device. Read columns **by header name**, not by letter: older tabs may lack
the newer columns (`From Hypotheses`, `Angle Type`, `Test Scope`,
`Supporting Elements`). For a row without them: test scope is `Concept` when
its `Tests` is `Offer × angle`, `-` or empty, otherwise `Component`; angle
type comes from the angle's row in the _Angles_ table (via _Label aliases_
for an old label), or "unknown". List any ad with no matching row as "components unknown" rather than
guessing them from the name.

Ask the user for **lead quality** (how many leads from each ad were real,
reachable prospects), since Meta can't see it. If unknown, mark it "not
assessed" and say so in the report.

## Step 3 — Metrics

| Level | Metric | Role |
|---|---|---|
| Primary | **CPL** (spend ÷ leads), or CPA/ROAS for a store | The decision metric |
| Primary | **Lead quality** (share of qualified leads) | Overrides a cheap CPL: cheap junk leads are not a win |
| Leading | **Link CTR** | Do the creative copy and creative stop the scroll and earn the click? |
| Leading | **CPC** (link) | Cost of attention |
| Leading | **CPM** | Context only: auction cost, not creative quality |
| Context | **Frequency** | Above ~3 the result may be fatigue, not the ad |

Leading metrics explain *why* an ad wins or loses; they never declare a winner
on their own.

## Step 4 — Minimum Data Before Judging (PROVISIONAL)

An ad is judged only when **both** hold:

- spend **≥ 2 × target CPL**, and
- **≥ 1,000 impressions** and **≥ 3 days** live

Below that it is **Inconclusive**, whatever the numbers look like.

## Step 5 — Classify Every Ad (PROVISIONAL)

| Class | Rule |
|---|---|
| 🏆 **Winner** | CPL ≤ target **and** ≥ 3 leads **and** lead quality acceptable (or not yet assessed, flagged) |
| 🌱 **Promising** | Judged, but: CPL within 1.0–1.5 × target, **or** fewer than 3 leads with link CTR clearly above the account median |
| ❌ **Loser** | Spend ≥ 3 × target CPL with 0 leads, **or** CPL > 1.5 × target with ≥ 3 leads, **or** leads judged mostly unqualified |
| ⏳ **Inconclusive** | Minimum data (Step 4) not reached |

**Evidence strength (PROVISIONAL)** — for every Winner and Loser, how much
its result can carry:

| Strength | Rule |
|---|---|
| `Weak` | Judged at the minimum data only (Step 4), or fewer than 5 leads |
| `Moderate` | Spend ≥ 4 × target CPL and ≥ 5 leads, and the CPL differs from the next ad in its test by ≥ 20 % |
| `Strong` | ≥ 10 leads, CPL differs from the next ad by ≥ 20 % on comparable spend, and lead quality assessed |

**Control (benchmark):** the best Winner by CPL is the control the next
round's challengers try to beat. Keep the existing control unless a challenger
beats it clearly (CPL at least ~20% lower on comparable data). If there is no
Winner yet, there is no control: say so.

## Step 6 — Map to the Testing Logic

Pick the branch from `creative-strategy`'s _Ads testing logic_ that the results
point to, and say why:

- Nothing works → test a substantially different problem, promise or offer
- Something works but the reason is unclear → narrow follow-up test changing one component
- A working idea exists → fix its biggest remaining weakness
- A challenger clearly beat the control → it becomes the new control
- No improvement → keep the current control
- Unclear results → don't build the next round on an assumed winner

Also name at least one **new direction** to explore in parallel, as
`creative-strategy` requires.

## Step 7 — Update `context/learnings.md`

After the report, update the client's learnings file (if it's missing, create it
with the structure of the agency hub's `_template/context/learnings.md`, two
folders up):

- **Current control** — the control named in Step 5
- **Combination results** — one row per judged ad from a **concept test**
  (Winner or Loser): the round, the ad, the whole combination (audience ×
  awareness × buyer motivation × angle (type) × offer × argument × creative
  concept × first-line device), the class with CPL and leads, the evidence
  strength, and one line on what it establishes and what it doesn't (e.g.
  "this combination works; not yet which component carries it").
- **What works / What doesn't work** — component values only, from
  **component tests** (a challenger vs. the control, one component changed),
  citing the ads and the round. A value with the same result in two or more
  rounds becomes `Pattern`; one round is `Hint`. A concept-test result never
  goes here: it goes to _Combination results_. When the same component value
  is in winning combinations in two or more rounds whose other big components
  differed, add it to the work queue as the next component test, still not
  to _What works_. Never write an Inconclusive ad in any table.
- **Hypotheses** — for each judged ad, whether its card's hypothesis held
- **Test hypotheses** — in `context/audience-hypotheses.md`, set the status of
  each row a judged ad tested, with the round and the evidence strength, and
  add `Own results` to its _Source_:
  - **Component test:** the row of the component under test (the `Tests`
    column) gets `Won` / `Lost` / `Unclear`. The control's other components
    keep their status.
  - **Concept test:** the component rows get `In winning combo` /
    `In losing combo` (never `Won` / `Lost`: a multivariable win doesn't show
    which component carried it). A _Suggested tests_ row is itself a
    combination, so it gets `Won` / `Lost` / `Unclear`.
  - A row already `Won` or `Lost` from a component test keeps that status; a
    combo result is added to its _Evidence_ only.
  - `AT` in _Source_ is the owner's priority, not evidence: a result adds
    `Own results` beside it and the status says what the data showed. Match a card to its rows by the Sheet columns: labels exactly,
  ignoring case, spaces, hyphens and accents in older rows and cards
  (`KattilaLoppu` = `Kattila-loppu`, `OljystaLuopuja` = `Öljystä luopuja`); arguments and creative concepts by
  their label (the part before ` — `; an older card without one: an argument by its text, a concept by its
  name, and say so in the report); suggested tests and copy patterns by the `From Hypotheses` column. An old label listed in the
  _Label aliases_ table is matched to the label it now points to. The _Angles_ table is the only
  angle register: an angle's result goes there. When a Winner's card used a
  component marked `New:` (incl. a new angle),
  propose adding it as a new row with Source `Own results` (show the proposal; the user decides); propose
  moving a row to _Retired_ after it has `Lost` in component tests in two rounds
- **Work queues** — the next component to test on the control, and the new
  directions
- **Client feedback** — lead-quality answers from Step 2, dated

Change only rows this round's results support; leave the rest as they are.
Show the user what changed.

## Output — Analytics Report

Save to `outputs/analytics/analytics-report-YYYY-MM-DD.md` and show it in chat:

1. **Period and data** — date range, total spend, leads, blended CPL vs. target
2. **Per-ad table** — ad name, offer, angle (type), test scope, tests, spend,
   impressions, link CTR, CPC, leads, CPL, lead quality, class, evidence strength
3. **Control** — the current benchmark ad, or "none yet"
4. **What the results suggest** — compare by component, from the Sheet columns:
   - concept tests (first-round entries and new directions): which
     **combinations** win, with their evidence strength; group by angle type
     to see whether one persuasion viewpoint does better. Say plainly that a
     winning combination doesn't show which component carried it, and name
     the component test that would
   - challengers vs. the control: they share its offer × angle, so the
     difference comes from the component in their `Tests` column (creative
     copy — compare by first-line device —, creative concept, audience…)
   - across all rounds: shared components among winners vs. losers
   State plainly when the data is too thin to say.
5. **Next round** — the testing-logic branch, what to keep, what to change,
   and one new direction. Recommend an **offer test** (which triggers
   `offer-development` in Phase 1.5) when offers look like the weak point:
   leading metrics fine but CPL high, or every offer tested has lost
6. **Kirjastopalaute** — for each judged ad (Winner or Loser only, never
   Promising or Inconclusive) whose brief card lists `Library patterns`, one
   line per pattern: `Kirjastopalaute: <ID> voitti|hävisi, <YYYY-MM-DD>`.
   Nothing else on these lines: no client name, numbers, claims or copy. The
   agency adds them to the library in a hub session (`ad-library`,
   synthesize); never write to the library from here. Omit the section if no
   judged ad used a library pattern.

End with:

> **Analytics Report complete. [N] ads: [W] winners, [P] promising, [L] losers, [I] inconclusive. Control: [ad name / none]. Ready for the next round.**
