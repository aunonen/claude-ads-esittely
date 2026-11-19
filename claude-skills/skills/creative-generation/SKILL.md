---
name: creative-generation
description: >
  Accepts the Creative Brief from creative-strategy — after the Phase 2.5 human
  review checkpoint has approved the N cards chosen for the test — and produces
  the ads: designs each approved card as an HTML layout built on the client's
  own photos, renders it to PNG in square, vertical and horizontal sizes with
  headless Chrome/Edge, uploads to Drive and logs to Sheets. No AI-generated
  imagery. Invoke for Phase 3 of the Create New Ads workflow. Always run after
  creative-strategy has produced a complete Creative Brief and it has been
  reviewed at the Phase 2.5 checkpoint.
---

# Creative Generation — Meta Ad Creatives (HTML designs)

## Terminology — Read This First

- **Offer × angle** — a creative's two biggest components (e.g. `Vahennys60`
  × `Hinta`), the first two parts of its name.
- **Creative** — an individual ad, built from one approved brief card. Its
  `Role` says whether it is a first-round entry, a challenger to the control
  (same offer × angle, one component changed: the card's `Tests` field) or a
  new direction. Each creative becomes its own ad set in Phase 4.
- **Creative concept** — a component: the format the ad borrows (news,
  WhatsApp chat, testimonial…). Never a grouping.
- **Design** — the HTML file a creative is built from. One design per
  creative holds all three sizes.

Each creative is rendered in **3 sizes** (square, vertical, horizontal).

---

## Before You Start

1. **Confirm the Creative Brief is in context** — count the cards actually
   present in `outputs/generated-assets/creative-brief-current.md` to determine
   **N** (the cards the user chose for the test at the checkpoint). If the file
   is missing (standalone run), write the approved cards there first.

2. **List the client's photos:**
   ```bash
   ls "reference/products/Images/"
   ```
   This is the exhaustive list of photo folders. For every card, confirm the
   exact file(s) its `Photo` field names exist
   (`ls "reference/products/Images/<folder>/"`), and **look at them with
   `Read`** before designing — you need to see where the subject sits to place
   the copy. If a card's photo is missing or unsuitable, list those cards and
   ask the user before continuing; never substitute a made-up or stock image.

3. **Read the design guide in full:**
   📄 `~/.claude/skills/ad-design/design-guide.md`
   (authenticity rules, file anatomy, layout patterns, typography, logo, badge,
   USP row, review checklist).

4. **Read the brand config:** `CLAUDE.md`'s **Brand Assets** section,
   `reference/brand/brand.css` (must have no `{{…}}` left — if it does, stop and
   tell the user to finish `/onboard brand`), the logo files in
   `reference/design-assets/`, and the notes in `reference/products/README.md`.

5. **Check the renderer works** once per run:
   ```bash
   python ~/.claude/skills/ad-design/render.py --help
   ```
   (`python3` on macOS.) If no browser is found, tell the user to install
   Chrome or set `CHROME_PATH`.

---

## Step 1 — Design all N creatives

Work through the cards in brief order, in batches of about 4.

For each card:

1. **Pick the layout pattern** from the card's `Layout` and `Visual direction`
   (see the design guide's Layout patterns). Follow the card: a challenger
   keeps the control's layout, badge treatment and copy position; otherwise
   vary them across the batch.
2. **Write the design file** `outputs/generated-assets/designs/<CreativeName>.html`
   following the design guide's anatomy:
   - the card's photo(s), cropped per size with `--pos-*`
   - every line of the card's CREATIVE COPY block (headline, subline, format
     text, other on-image text) — **exact** wording, in the card's reading order
   - the social proof element only if the card has one, in this card's treatment
   - the logo only if the card's `Logo:` is Yes
   - per-size adjustments so SQ, VT and HZ each look composed, not squeezed
3. When the batch's designs are written, **render them together**:
   ```bash
   python ~/.claude/skills/ad-design/render.py outputs/generated-assets/designs/A.html outputs/generated-assets/designs/B.html ...
   ```
4. **Look at every PNG** (`Read`, all three sizes) and run the design guide's
   review checklist. Fix and re-render (`--sizes` for just the size that
   needs it) until each creative passes. Don't show the user anything that
   fails the checklist.

Print one line per finished creative:
```
✅ Creative [N] — [Offer-Angle-Variant] — SQ/VT/HZ rendered
```

## Step 2 — Upload to Drive

Read the generated-assets Drive folder ID from `reference/gws-config.json`.
For each PNG:
```bash
gws drive files create \
  --json '{"name": "[CreativeName]-SQ_[DD-MM-YYYY].png", "parents": ["DRIVE_FOLDER_ID"]}' \
  --upload "outputs/generated-assets/[CreativeName]-SQ_[DD-MM-YYYY].png" 2>/dev/null
```
Capture each returned `id` → `https://drive.google.com/file/d/FILE_ID/view`.

## Step 3 — Write the state file

`outputs/generated-assets/phase3a-state.json` — an array of N objects in brief order:

```json
[
  {
    "n": 1,
    "name": "Offer-Angle-A",
    "components": {
      "offer": "Offer label",
      "angle": "Angle label",
      "angle_type": "RiskReversal",
      "tests": "Component that differs within the combination",
      "test_scope": "Concept / Component",
      "audience": "Audience label",
      "awareness_level": "Problem aware",
      "problem_desire": "…",
      "argument": "…",
      "supporting_elements": "… / none",
      "creative_concept": "…",
      "cta": "…",
      "first_line_device": "Question",
      "from_hypotheses": "Test #2; Copy: … / none"
    },
    "design_file": "outputs/generated-assets/designs/Offer-Angle-A.html",
    "photos": ["reference/products/Images/<folder>/<file>"],
    "layout": "Photo + headline",
    "sq_local_path": "outputs/generated-assets/Offer-Angle-A-SQ_DD-MM-YYYY.png",
    "vt_local_path": "outputs/generated-assets/Offer-Angle-A-VT_DD-MM-YYYY.png",
    "hz_local_path": "outputs/generated-assets/Offer-Angle-A-HZ_DD-MM-YYYY.png",
    "sq_drive_link": "https://drive.google.com/file/d/FILE_ID/view",
    "vt_drive_link": "...",
    "hz_drive_link": "...",
    "creative_copy": "All on-image text from the card's CREATIVE COPY block, in reading order, one line per element",
    "headline": "Exact headline from brief card",
    "subline": "Exact subline or empty string",
    "social_proof": "Social proof element from brief card, or empty",
    "primary_text": "Full primary text from brief card",
    "ad_headline": "Ad headline from brief card",
    "logo_included": true
  }
]
```

## Step 4 — Log to Sheets (one batch at the end)

Check the header row first:
```bash
gws sheets spreadsheets values get \
  --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "Creative Generations!1:1"}' 2>/dev/null
```
Append N×3 rows (SQ, VT, HZ per creative). Every component gets its own
column, copied exactly from the brief card, so results can later be compared
component by component (`ads-analytics` joins Meta results to these rows by
creative name):

| Col | Field | What to put |
|---|---|---|
| A | Creative Name | Full asset name with size suffix, e.g. `Vahennys60-Hinta-A-SQ_24-10-2026` |
| B | Offer | `Label — one sentence` |
| C | Angle | `Label — one sentence` |
| D | Tests | The component this creative varies |
| E | Audience | Audience label |
| F | Awareness Level | Unaware / Problem aware / Solution aware / Product aware / Most aware |
| G | Problem / Desire | From the card |
| H | Argument | From the card |
| I | Creative Concept | From the card |
| J | CTA | From the card |
| K | Creative Copy | All on-image text, in reading order (the first line is the headline) |
| L | Design File | Design file + photo(s) used |
| M | Drive Link | `https://drive.google.com/file/d/FILE_ID/view` |
| N | Primary Text | Full primary text |
| O | Ad Headline | The headline below the image, from the card |
| P | First-Line Device | From the card |
| Q | From Hypotheses | From the card (`Test #N; Copy: …` or `none`) |
| R | Angle Type | From the card (one fixed angle type) |
| S | Test Scope | From the card: `Concept` / `Component` |
| T | Supporting Elements | From the card, or `none` |

Write "n/a" for an empty value so the columns don't shift. **Older headers:**
if the header row is this table with only trailing columns missing (an older
tab ending at `First-Line Device` or `From Hypotheses`), append the missing
header names after the last existing one — never reorder, rename or fill old
rows (`ads-analytics` reads columns by header name and treats a blank as
unknown) — then write the rows in the order of the header row. If the header
has other columns (e.g. an older layout with `Hook` or `Copy` columns), stop and
tell the user the tab needs the new header row first, rather than writing rows
that don't match it.

## Step 5 — Creative inventory

Print a table of all N×3 assets grouped by offer × angle, then creative, then size.
Then state:

> **Creative Generation complete. N creatives × 3 sizes = N×3 ads rendered from the client's own photos, uploaded to Google Drive, and logged to Google Sheets. Ready for the Phase 3.5 review checkpoint.**

---

## Targeted Revisions (invoked from the Phase 3.5 checkpoint)

Feedback at Phase 3.5 is applied by editing the design and re-rendering. It's
fast and exact, so apply what the user asks literally.

1. Look up each flagged creative in `phase3a-state.json` and open its
   `design_file`.
2. Apply the feedback as a direct edit: wording (only to wording the user gives
   or that's in context), sizes, positions, crop (`--pos-*`), a different photo
   from the client's folder, scrim strength, badge treatment, logo on/off.
3. **Size scope:** changes to shared elements (copy, photo, colours) affect all
   three sizes, so re-render all three. A change scoped with an
   `html[data-size=…]` selector only needs that size (`--sizes vt`).
4. **Brand-wide feedback** ("headlines always smaller", "use the darker
   green"): change `reference/brand/brand.css` (or tell the user it belongs
   there), then re-render every design in the batch so they stay consistent.
5. Overwrite the same PNG filenames, upload the new files to Drive, update the
   state entry and the existing Sheet rows in place (match by creative name).
6. Report back only the revised creatives so the checkpoint re-presents just
   what changed.

---

## Naming Each Creative

```
[Offer]-[Angle]-[Variant]-[Size]_[DD-MM-YYYY]
```

`[Size]` is `SQ`, `VT` or `HZ`, added by `render.py` along with the date. The
design file is just `[Offer]-[Angle]-[Variant].html`. Offer, angle and variant
come from the brief card's `Creative` field, ASCII only (ä→a, ö→o) so file
names and Drive links stay clean.

Examples:
- `Vahennys60-Hinta-A-SQ_06-07-2026`
- `IlmainenKartoitus-Luotettavuus-B-VT_06-07-2026`

This name becomes the ad name in Meta Ads Manager.
