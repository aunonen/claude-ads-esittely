---
name: create-new-ads
description: >
  End-to-end workflow for creating a new batch of Meta image ad creatives for
  the brand configured in this workspace and setting them up in Meta Ads Manager for review. Triggers whenever
  the user asks to create new ads, generate new ad creatives, run the ads
  workflow, start a new creative batch, or any variation of "let's make some
  new ads." Orchestrates four phases in sequence: ad inspiration analysis →
  creative strategy → creative generation → campaign setup (DRAFT only, never
  live). Always use this skill when the user wants to produce new paid social
  image ads for this brand on Meta/Facebook/Instagram, even if phrased casually
  like "time to make some new ads."
---

# Create New Ads — Meta Advertising Workflow

## Your Role

You are an **elite Meta advertising strategist** specialising in direct-response
image creatives for service businesses and online stores. You combine data-driven creative strategy with
deep brand knowledge — grounded in whichever brand's `context/` files are
loaded — to produce ads that convert, based on customer psychology, competitive
analysis, and this brand's unique market positioning.

---

## ⚠️ NON-NEGOTIABLE RULE: DO NOT LAUNCH ANY ADS ⚠️

**This workflow ends with campaign structures set up in DRAFT/PAUSED status
inside Meta Ads Manager. Under no circumstances are any campaigns, ad sets, or
ads to be activated, made live, or allowed to accrue any spend.**

Every asset produced exists for **human review and manual approval**. A real
person must sign off before anything goes live. This applies to every phase
without exception. If any tool, connector, or setting offers to "publish",
"activate", "go live", or "start delivery" — do not use it.

Reiterate this to the user at the end of the workflow.

---

## Workflow Overview

A results check and four phases run in strict sequence. Each phase depends on the outputs of the
phase before it, and each phase's output (Sheets rows, the Creative Brief file,
generated assets) stays directly in your context as you move forward, so later
phases build on what earlier phases actually produced rather than re-deriving it.
Do not skip ahead or run phases out of order, and do not use the Agent tool to
delegate any phase — running everything in one continuous context is what keeps
quality consistent end-to-end.

```
Phase 0 → Results Check (ads-analytics: decides the round type)
Phase 1 → Ad Inspiration Analysis
Phase 1.5 → Offer Development (only when needed: offer-development)
Phase 2 → Creative Strategy (Test Plan + ~20-card pool + recommended selection)
  ↳ Checkpoint → Creative Brief Review (human picks the cards for the test)
Phase 3 → Creative Generation (only the approved cards)
  ↳ Checkpoint → Generated Asset Review (human reviews the actual images, requests
                 revisions before anything reaches Meta)
Phase 4 → Campaign Setup (DRAFT only)
```

At the start of the workflow, briefly tell the user what is about to happen and
what to expect as each phase completes.

**Pre-flight check:** before Phase 1, confirm the workspace is configured. If
`CLAUDE.md`'s Brand Assets table, `context/offer-brief.md`'s sections marked
*(used directly by the skills)* (including _Approved Offers_), the
*(used directly by the skills)* tables in `context/audience-hypotheses.md`, `reference/gws-config.json` or
`reference/meta-ads-config.json` still contain `{{…}}` placeholders, or
`reference/products/Images/` has no product folders, stop and tell the user
to run `/onboard` first (list exactly what's missing). Also check the budget
fields (`campaign_daily_budget_total`, `min_daily_budget_per_ad`) and
`context/strategy.md`'s _Ad Targets_: Phase 2 sizes the test from them. Meta
IDs (`ad_account_id`, `page_id`…) are only needed in Phase 4: if they're
`null` or placeholders, say so and carry on, and Phase 4 will stop.

---

## Phase 0: Results Check

**Sub-skill:** `ads-analytics` — `Skill({"skill": "ads-analytics"})`

Decides what kind of round this is, so the brief tests the right thing:

- **Previous ads exist and `ad_account_id` is set** → run `ads-analytics`. Its
  report (`outputs/analytics/analytics-report-YYYY-MM-DD.md`) names the
  control and the testing-logic branch for this round.
- **Previous ads ran but results can't be read here** (no ad account ID yet,
  or ads not made with this workflow) → ask the user for the results in plain
  words (which ad, spend, leads) and write a short report from them in the
  same file, marked "reported by user".
- **No previous ads** → First round. Say so and move on; no report needed.

**Wait for Phase 0 to finish before Phase 1.**

---

## Phase 1: Ad Inspiration Analysis

**Sub-skill:** `competitor-analysis` — `Skill({"skill": "competitor-analysis"})`

Checks `reference/ad-inspiration/` for user-curated reference ads (competitor
ads plus the brand's own past winners), reads each new image directly for deep
visual + copy analysis, uploads to Drive, logs new ones to the "Ad Inspiration"
tab (deduplicated by filename), reads brand context from `context/`, and
reads the Phase 0 round type and what has already been tested, maps the set
component by component (weighted by evidence class), finds white space, and
writes ideas that fit the round: broad offer × angle ideas in a first round,
alternatives for the component under test in a narrow test. Each idea carries
a hypothesis, a status (new / variation / previously lost), an offer status
(approved / needs client approval) and feasibility. Off-limits angles are
filtered out. The report is saved to
`outputs/analytics/ad-inspiration-report-YYYY-MM-DD.md`, with open questions
for the client at the end.

If the inspiration folder is thin or stale (see `competitor-analysis` Step 1),
Phase 1 suggests running `ad-inspiration-collection` first; it runs only if the
user agrees.

**Wait for Phase 1 to complete fully — all Ad Inspiration data must be logged to
Google Sheets before Phase 2 begins.**

---

## Phase 1.5: Offer Development (when needed)

**Sub-skill:** `offer-development` — `Skill({"skill": "offer-development"})`

Run it when **fewer than 3 offers are approved** in `context/offer-brief.md`,
when the **Phase 0 report recommends an offer test**, or when the user asks.
Otherwise skip it and say so in one line.

It writes offer proposals to `context/offer-proposals.md` and the client log's
**Tarjousehdotukset** tab for the client to approve. This round does **not**
wait for the client: it continues with the offers already approved, and
approved proposals join a later round. (Proposals can still sit in the pool
marked "needs client approval", as before.)

---

## Phase 2: Creative Strategy

**Sub-skill:** `creative-strategy` — `Skill({"skill": "creative-strategy"})`

Syncs the internal **Komponentit** tab with `context/audience-hypotheses.md`
and reads the user's 1–5 ratings (the strongest components are chosen first),
reads the "Ad Inspiration" tab, all `context/` brand files, applies the
static-ads-strategy framework and the Phase 0 report, and produces a Creative
Brief: a **Test Plan** (test slots from the budget, round type, selection
rule), a pool of **~20 cards** each defined component by component, and a
**recommended selection** that fits the test.

Once complete, save the full brief (Test Plan, all cards, overview table,
recommended selection) to `outputs/generated-assets/creative-brief-current.md`
(overwrite if it exists), **and put it in Drive** so it can be reviewed and
shared outside this session:

1. **Brief tab** in the client's log spreadsheet (`spreadsheet_id` in
   `reference/gws-config.json`), one row per card, appended (earlier batches
   stay). If the tab doesn't exist, create it with this header row first:

   | Col | Field | What to put |
   |---|---|---|
   | A | Batch | Brief date, `YYYY-MM-DD` |
   | B | # | Card number in the pool |
   | C | Creative | `Offer-Angle-Variant` |
   | D | Status | `Recommended` / `Candidate` (Phase 2.5 changes it to `Selected` / `Dropped`) |
   | E | Role | First-round entry / Challenger / New direction |
   | F | Tests | The component it varies |
   | G | Hypothesis | From the card |
   | H | Offer | `Label — sentence` (with "needs client approval" if so) |
   | I | Angle | `Label — sentence` |
   | J | Audience | Audience label |
   | K | Awareness Level | From the card |
   | L | Problem / Desire | From the card |
   | M | Argument | From the card |
   | N | Creative Concept | From the card |
   | O | Creative Copy | Every on-image line, in reading order |
   | P | Ad Headline | From the card |
   | Q | Primary Text Plan | One line per step |
   | R | Primary Text | Full text |
   | S | CTA | From the card |
   | T | Photo | Photo path(s) |
   | U | Layout | From the card |
   | V | First-Line Device | From the card |
   | W | Alternates | The card's two alternate first lines, with their devices |
   | X | From Hypotheses | From the card |
   | Y | Angle Type | From the card |
   | Z | Test Scope | `Concept` / `Component` |
   | AA | Supporting Elements | From the card, or `none` |
   | AB | Coherence | The card's coherence line |
   | AC | Message Hierarchy | From the card |

   If the tab exists with an older header (only trailing columns missing),
   append the missing header names after the last one, never reorder or
   rename, and write each row in the order of the header row. Earlier rows
   stay as they are (blank = not recorded then).

2. **The brief file** uploaded to the generated-assets Drive folder
   (`drive_folder_id`) as `creative-brief-YYYY-MM-DD.md`, with the Test Plan
   the tab doesn't hold.

Give the user both links.

**Wait for Phase 2 to complete fully — the brief must be written before the
Phase 2.5 checkpoint begins.**

---

## Phase 2.5: Creative Brief Review (Human Checkpoint)

**A checkpoint, not a fifth phase — no sub-skill invoked here.** Its job is to
get explicit human sign-off on which cards from the pool go into the test.
The user always makes the final choice. Do not invoke Phase 3 until this ends
in a clean approval.

1. **Present the Test Plan block first** (round type, test slots, budget per
   ad, control, what is being tested, days to a verdict), **then the pool as a
   compact table**, one row per card:

   ```
   | # | Creative | Role | Offer | Angle (type) | Tests | Headline | Creative concept | Awareness | Photo folder |
   |---|---|---|---|---|---|---|---|---|---|
   | 1 | Vahennys60-Hinta-A | First-round entry | Vahennys60 | Hinta (Value) | Offer × angle | [Headline] | News | Problem aware | [photo-folder-name] |
   | ... | ... | ... | ... | ... |
   ```

   **After the table, the text of every card**, so the user can judge the
   words before choosing, one short block per card:

   ```
   #1 Vahennys60-Hinta-A
   Ketju:    [the card's coherence line]
   Kuvassa:  [every line of the CREATIVE COPY block, in reading order] ([first-line device])
   Vaihtoehdot: [the two alternate first lines]
   Primary text -suunnitelma: [the card's Primary text plan, one line per step]
   Mainosotsikko: [Ad headline]
   ```

   The full primary texts are in the brief file and on the Brief tab in Drive
   (see Phase 2): say where.

   Then the **recommended selection** and its alternative, with their reasons,
   and plain-language instructions, e.g.:
   > The budget fits **3 new ads**. Reply with the numbers to test —
   > `recommended`, a list like `1,7,14`, or edits inline, e.g. `1,7,14 but
   > change the headline on #7 to "..."`. Anything not listed is dropped.

   Then stop your turn. This is a plain conversational pause — do **not** use
   `AskUserQuestion` (caps at 4 options, can't handle a 20-item select), and do
   **not** delegate this to a fresh sub-agent (same continuous-context rule as
   the Workflow Overview).

2. **Parse the reply:**
   - **Recommended** (`"recommended"`, `"looks good"`, `"proceed"`) → keep the
     recommended selection, go to the selection check.
   - **Keep by number** (`"1,7,14"`) → discard every card not listed.
   - **`all`** → treat as a request to test every card: run the selection
     check, which will flag the budget, and ask the user to confirm.
   - **Inline edits** (reword a headline, swap a USP, change a card's product,
     shorten primary text) → apply directly in this context. Do **not**
     re-invoke `creative-strategy` for these.
   - **Structural requests** ("these don't work, give me new ideas for slot X")
     → re-invoke `Skill({"skill": "creative-strategy"})` with the feedback,
     instructing it to revise only the flagged cards. Re-present the updated
     table and repeat until a clean approval.
   - **Ambiguous reply** → ask one plain clarifying question.

3. **Selection check — warn, never block.** Check the chosen set against the
   Test Plan and list every issue in plain language, with its consequence:
   - **More ads than slots:** "You picked 5, the budget fits 3: each ad gets
     3 €/day instead of 5 €, and a verdict takes ~30 days instead of ~18."
   - **Fewer ads than slots:** the unused budget, and that the total can be
     lowered or a card added.
   - **Selection rule broken:** e.g. "#3 and #5 share the offer and the angle,
     so in a first round their results won't show which big component worked",
     or "#1 and #7 both argue from a `RiskReversal` angle, so the round
     explores one persuasion viewpoint twice"
     or "#9 changes the creative copy *and* the creative concept vs. the control, so a
     win can't be traced to either."
   - **No new direction** in a narrow test with 3+ slots.
   - **Missing pieces:** a card with no suitable photo.
   - **Unapproved offer:** a card whose offer is marked "(needs client
     approval)": the client must agree to the offer before the ad can run.
   - **Unsupported claim:** a line on the card that no `context/` file backs
     (e.g. an `AT` row's example sentence about the service that the business
     info doesn't confirm).

   If there are no issues, say "The selection fits the test plan." Otherwise
   ask once whether to go ahead as chosen or adjust. The user's answer is
   final: never swap cards on your own.

4. Once a final approved set exists (size **N**), **rewrite
   `outputs/generated-assets/creative-brief-current.md`** to contain the Test
   Plan (updated to the final N: budget per ad, days to a verdict) and only
   those N cards (with edits applied), in original relative order. Recompute
   the Test Overview Table so it lists only the approved cards. Add a footer:
   `> Approved: N of [M] pool cards, approved by user on [date]. Selection check: [OK / issues the user accepted].`
   Then update the Brief tab: set **Status** to `Selected` for the chosen
   cards and `Dropped` for the rest of this batch, write any edits into their
   rows, and upload the rewritten file over the Drive copy.

5. Print a short confirmation — "Proceeding with N of [M] creatives: [names]" —
   then move to Phase 3.

---

## Phase 3: Creative Generation

**Sub-skill:** `creative-generation` — `Skill({"skill": "creative-generation"})`

Immediately after the Phase 2.5 checkpoint ends in approval. All within the same
context: designs each approved card as an HTML layout on the client's own
photos, renders square/vertical/horizontal PNGs to `outputs/generated-assets/`,
uploads them to Drive and logs all N×3 assets to Sheets in one batch. No
AI-generated imagery.

**Wait for Phase 3 to complete fully — all N×3 assets generated, uploaded, and
logged before the Phase 3.5 checkpoint begins.**

---

## Phase 3.5: Generated Asset Review (Human Checkpoint)

**A checkpoint, not a fifth phase — no sub-skill invoked for the initial review.**
Phase 2.5 gates the *brief*; this gates the *actual rendered ads* before any
reach Meta Ads Manager. Do not invoke Phase 4 until this ends in a clean approval.

1. **Present each creative for visual review, in brief order.**
   For every one of the N creatives, print its number, name, offer, angle, what
   it tests, and headline, then `Read` its square PNG from `outputs/generated-assets/` inline
   — the primary QA surface for copy, crop, legibility and logo issues. Note
   the Drive links for that creative's VT/HZ sizes, available on request.
   Revisions are quick edits to the HTML design, so invite specific visual
   feedback (bigger headline, different crop, other photo, darker overlay).

2. **Ask the user to reply** with one of:
   - `all` / `looks good` / `proceed` — approve everything as-is.
   - A list of creative numbers/names to revise, with feedback,
     e.g. `#4 headline smaller, #7 use a different photo, all: darker overlay`.
   - A request to see VT/HZ for specific creatives first.

   Then stop your turn — same reasoning as Phase 2.5 (no `AskUserQuestion`, no
   sub-agent delegation).

3. **Parse the reply:**
   - **Approve-all** → proceed to Phase 4.
   - **Flagged creatives with feedback** → re-invoke `creative-generation`'s
     **Targeted Revisions** flow with the flagged names/numbers and each
     one's feedback (state clearly this is a targeted revision, not a full
     Phase 3 run). Re-present only the revised creatives and repeat step 2.
   - **Request to see VT/HZ** → open/note the Drive link(s), repeat step 2.
   - **Ambiguous reply** → ask one plain clarifying question.

4. Once every creative is approved, print "All N creatives approved after
   review." — then move to Phase 4.

---

## Phase 4: Campaign Setup

**Sub-skill:** `meta-ads-campaign-setup` — `Skill({"skill": "meta-ads-campaign-setup"})`

Immediately after the Phase 3.5 checkpoint ends in approval. Builds an ABO
Testing Campaign in Meta Ads Manager (everything PAUSED), one ad set per ad with an equal share of the total budget
from the Creative Brief, applies targeting and the objective (sales or leads,
website or instant form) per the brand's config, uses each card's approved
primary text and ad headline as they are (one of each per ad), and produces a
Campaign Structure Summary.

**Wait for Phase 4 to complete fully before delivering the Workflow Completion
Summary below.**

---

## Completion

Once all four phases are complete, deliver a **Workflow Completion Summary**:

```
✅ WORKFLOW COMPLETE — READY FOR HUMAN REVIEW
=============================================

Phase 1 ✅  Ad Inspiration Intelligence Report — [N] ads analysed
Phase 2 ✅  Creative Strategy — Test Plan ([round type], [S] slots) + pool of [M] cards
Checkpoint ✅  Creative Brief Review — [N] of [M] cards chosen for the test
Phase 3 ✅  Creative Generation — [N]×3 assets produced ([N] approved creatives × 3 sizes)
Checkpoint ✅  Generated Asset Review — [N] creatives approved after review
Phase 4 ✅  Campaign Setup — ABO Testing campaign built in Meta Ads Manager

⚠️  ALL CAMPAIGNS ARE PAUSED — NO SPEND WILL OCCUR UNTIL MANUALLY ACTIVATED

Next steps for the team:
1. Review the [N]×3 generated assets ([N] approved creatives × 3 sizes each)
2. Review the campaign structures in Meta Ads Manager
3. Activate any approved campaigns and ad sets manually
4. Archive or delete any creatives that don't pass review
```

Remind the user that **no ads will run, no budget will be spent, and nothing is
live** until a human manually activates the campaigns inside Meta Ads Manager.
