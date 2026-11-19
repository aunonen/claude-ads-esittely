---
name: meta-ads-campaign-setup
description: "Sets up the brand's Meta Ads campaign (ABO) in Meta Ads Manager using the Meta connector, using the account details in reference/meta-ads-config.json. All campaigns and ads are created in PAUSED/DRAFT status — nothing is activated or made live. Invoke this skill for Phase 4 of the Create New Ads workflow, or any time you need to build a new campaign structure for review. Always run this after creative generation so all assets are ready before setup begins."
---

# Meta Ads Campaign Setup

## ⚠️ CRITICAL: DO NOT ACTIVATE ANY ADS ⚠️

**Every campaign, ad set, and ad created by this skill must be set to PAUSED or
DRAFT status. Under no circumstances should any campaign, ad set, or ad be
activated, made live, or allowed to spend budget. This is an absolute rule with
zero exceptions.**

The purpose of this skill is to build a complete campaign structure for
**human review and approval**. A real person must manually review and activate
everything before any spend occurs. State this clearly in your summary output.

---

## Account Details — Read From Config

All account-specific values live in **`reference/meta-ads-config.json`**. Read it
first and use its values throughout. Do not look them up some other way and do not
prompt the user for them:

| Config key | Used for |
|---|---|
| `ad_account_id` | Every Meta call; the Graph API image-upload URL (`act_<ad_account_id>`) |
| `page_id` | `object_story_spec` on every ad; `promoted_object` for instant forms |
| `objective` | Campaign objective: `OUTCOME_SALES` (store, website purchases) or `OUTCOME_LEADS` (lead gen) |
| `conversion_location` | `website` (pixel conversion on the site) or `instant_form` (Meta lead form, no website needed) |
| `pixel_id` | Ad set conversion tracking — `website` only |
| `conversion_event` | Ad set optimisation event — `website` only (default `Purchase`; `Lead` for a website lead form) |
| `lead_form_id` | The instant form attached to every ad — `instant_form` only |
| `attribution` | Ad set attribution window (default 7-day click, 1-day view) |
| `currency`, `currency_symbol` | Budget display; budgets are sent to the API in the currency's minor unit |
| `campaign_daily_budget_total` | The only budget authority: the whole test's daily budget, control included |
| `min_daily_budget_per_ad` | Used by `creative-strategy` to size the test; here only to warn if an ad set falls below it |
| `countries`, `geo_targeting` | Geo targeting: whole countries, or a radius around a place (`{"type": "radius", "location": "Oulu, Finland", "radius_km": 50}`) |
| `website_domain`, `display_link`, `landing_pages` | Ad destination URLs |
| `campaign_name_prefix` | Campaign naming |
| `cta_type` | Call to action (default `SHOP_NOW`) |

**Required keys depend on the setup.** Always: `ad_account_id`, `page_id`,
`objective`, `conversion_location`. Plus, for `website`: `pixel_id`,
`conversion_event`, `website_domain`; for `instant_form`: `lead_form_id`. **If
the file is missing, or any required key is `null`, empty or still a `{{…}}`
placeholder, stop** and list exactly which keys are missing. Tell the user to
run `/onboard meta` (or fill in the file) before Phase 4. Never guess or invent
an ID.

---

## Step 0 — Read Creative Data from Google Sheets

**All campaign structure, ad copy, and asset information comes from the
Creative Generations tab. Read it first, before touching any Meta tools.**

Read `reference/gws-config.json` for the spreadsheet ID, then fetch all rows:

```bash
gws sheets spreadsheets values get \
  --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "Creative Generations!1:500"}' 2>/dev/null
```

The first row is the header. Parse the column layout from it. The data you
need per row:

| Column | Field |
|---|---|
| Creative Name | The full asset name (e.g., `Vahennys60-Hinta-A-SQ_06-07-2026`) |
| Offer, Angle | The offer and angle, both written `Label — sentence`; the labels (e.g. `Vahennys60`, `Hinta`) are also the first two parts of the creative name |
| Tests, Creative Concept, Creative Copy… | The other components (full layout in `creative-generation` Step 4); used for copy variations, not structure |
| Drive Link | The Google Drive URL for this asset |
| Creative Copy | All on-image text from the brief card (reference only; it is in the image already) |
| Primary Text | The full primary text body for this creative |

**Filter to SQ (square) rows only for campaign structure purposes** — one SQ
row per creative gives you the creative name, offer, angle and copy. VT
and HZ rows are additional size variants uploaded alongside the square for the
same ad, not separate ads. So if you have 20 creatives × 3 sizes = 60 rows, use
the 20 SQ rows to drive the ad structure, then upload all three local files
(SQ + VT + HZ) per creative in Step 4a.

**One ad set per creative.** Each approved creative gets its own ad set
with an equal budget, so Meta can't pour the whole budget into one ad in the
first days and every ad gets a fair test. The Offer and Angle columns (also
the first two segments of the creative name) still say which offer × angle
each ad tests.

Also read the **Test Plan** at the top of
`outputs/generated-assets/creative-brief-current.md`: it says whether a
control keeps running in an earlier campaign, which affects the budget
(Step 3).

---

## Step 1 — Confirm Ad Account

Use `ads_get_ad_accounts` to verify the account is accessible, then confirm
you're working against the `ad_account_id` from `reference/meta-ads-config.json`
for all subsequent calls. If it isn't in the accessible list, stop and tell the
user. Don't fall back to another account.

---

## Campaign Structure Overview

One **ABO Testing Campaign** with one ad set per creative, each with the
same daily budget. Equal ABO budgets make the test fair: every ad gets the
same chance to spend, so `ads-analytics` can compare them. The control (if
any) keeps running where it is; it is not duplicated, because a copy would
restart its learning.

```
[campaign_name_prefix] - ABO Testing Campaign (PAUSED)
├── Ad Set: [OfferA-AngleA-A] | ABO | [DD/MM/YYYY] (PAUSED)
│   └── Ad: OfferA-AngleA-A (PAUSED)
├── Ad Set: [OfferB-AngleB-A] | ABO | [DD/MM/YYYY] (PAUSED)
│   └── Ad: OfferB-AngleB-A (PAUSED)
└── ...
```

---

## Step 2 — Create the Campaign

| Parameter | Value |
|---|---|
| Name | `[campaign_name_prefix] - ABO Testing - [Month Year] - Image Ads` |
| Buying type | Auction |
| Objective | `objective` from config (`OUTCOME_SALES` / `OUTCOME_LEADS`) |
| Campaign spending limit | None |
| Budget type | Ad set budget (ABO) |
| Bid strategy | Highest volume or value (default) |
| Status | **PAUSED** |

Use `ads_create_campaign` with these parameters.

---

## Step 3 — Create Ad Sets (one per creative)

For each approved creative from Step 0, create one ad set using `ads_create_ad_set`.

### Ad Set Naming

```
[Offer]-[Angle]-[Variant] | ABO | [DD/MM/YYYY]
```
Example: `Vahennys60-Hinta-A | ABO | 06/07/2026`

### Budget per Ad Set

```
budget per ad set = (campaign_daily_budget_total − control's daily budget, if a control keeps running)
                    ÷ number of new creatives
```

Example: 15 €/day total, no control, 3 creatives → 5 €/day each. With a
control that keeps its 5 €/day, 2 new creatives → 5 €/day each. If the result
is below `min_daily_budget_per_ad`, still build it, but say so in the summary
(the user accepted this at the Phase 2.5 selection check).

### Ad Set Parameters

| Parameter | Value |
|---|---|
| Campaign | The campaign ID from Step 2 |
| Daily budget | The budget per ad set from above, sent to the API in the currency's minor unit (e.g. 5 €/day = `500` cents) |
| Conversion location, goal, tracking | Per `conversion_location`, see the table below |
| Attribution | `attribution` from config |
| Schedule | Always on / no end date |
| Age targeting | Meta default (leave blank) |
| Interest / custom targeting | None — broad only |
| Audience suggestions | Off |
| Placements | Advantage+ Placements, **Audience Network excluded** (see below) |
| Status | **PAUSED** |

**Per conversion location:**

| | `website` | `instant_form` |
|---|---|---|
| Conversion location | Website | Instant forms (`destination_type: ON_AD`) |
| Performance goal | Sales: maximise value of conversions. Leads: maximise number of conversions | Maximise number of leads (`optimization_goal: LEAD_GENERATION`, `billing_event: IMPRESSIONS`) |
| Tracking | `promoted_object: {pixel_id, custom_event_type: <conversion_event>}` | `promoted_object: {page_id}` |

### Geographic Targeting — Applied to Every Ad Set

**Default: the `countries` list from config, broad, no exclusions.** No regional
exclusions unless a specific brief or the user calls for them.

**Radius targeting** (`geo_targeting.type: "radius"`): look up the place's key
with the targeting search (`GET /search?type=adgeolocation&location_types=["city"]&q=<location>`),
then replace `countries` in `geo_locations` with
`"cities": [{"key": "<key>", "radius": <radius_km>, "distance_unit": "kilometer"}]`.
Re-fetch the saved ad set's `targeting` and confirm the place and radius
before moving on.

```json
{
  "age_min": 18,
  "age_max": 65,
  "geo_locations": { "countries": [<countries from config>], "location_types": ["frequently_in", "home"] },
  "targeting_automation": { "advantage_audience": 1 },
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed", "marketplace", "right_hand_column", "story", "search", "instream_video"],
  "instagram_positions": ["stream", "story", "explore", "reels"]
}
```

> **Audience Network exclusion REQUIRES an explicit `publisher_platforms`
> list** — it is not excluded by default. List `publisher_platforms` explicitly
> as `["facebook", "instagram"]` (without `"audience_network"` and without
> `audience_network_positions`). Leaving `publisher_platforms` unset defaults
> to Advantage+ Placements, which DOES include Audience Network.
>
> **Do NOT include `"video_feeds"` in `facebook_positions`** — deprecated for
> the current API version; both `ads_create_ad_set` and `ads_update_entity`
> reject it (error_subcode `2490562`). Omit it; the remaining positions still
> give full Facebook coverage.

**If a future brief needs regional exclusions:** only some Meta geo-types are
`region`-type; others (e.g. county-level areas) require the undocumented
`medium_geo_areas` field inside `excluded_geo_locations`, not the public
`geo_locations` reference table. Pass **`key`-only objects** on write (e.g.
`{"key": "4082"}`) — the live `ads_create_ad_set` call rejects objects that also
include `name`/`country_code`, even though Meta's `/targetingsentencelines`
dry-run validator accepts them. Verify any exclusion by re-fetching the saved
ad set's `targeting` field (or running it through `/targetingsentencelines`)
before trusting it.

### Placements — Audience Network Must Be Off

Use Advantage+ Placements but manually deselect **Audience Network**. Verify
it is deselected on every ad set before saving.

---

## Step 4 — Upload Images to Meta and Create Ads

> **Note on `ads_create_creative`:** This tool is in gradual rollout and may not
> be available on your ad account (only Meta can unlock it). The proven
> solution used throughout this skill works on every account: `ads_create_ad`
> with **Placement Asset Customization (PAC)**: combine `object_story_spec`
> (page_id only) with `asset_feed_spec` + `asset_customization_rules` (Step
> 4c). This maps all three uploaded image hashes (SQ/VT/HZ) to the correct
> placements automatically — fully scripted, no manual thumbnail selection.

For each creative (one per ad set):

### 4a — Upload all three size variants to Meta via curl

All three size variants are already saved locally in `outputs/generated-assets/`.
Upload directly to Meta's ad image library via the Graph API. Authentication
uses `$META_ACCESS_TOKEN`, a System User token that never expires. Agency setup:
the agency's token lives once in `~/.claude/settings.json` (user level, outside
every client folder). A client whose ad account is NOT shared to the agency's
Business Manager gets its own token in that client folder's
`.claude/settings.local.json`, which overrides the user-level one.

**If `$META_ACCESS_TOKEN` is not set**, instruct the user to:
1. Go to Meta Business Suite → Settings → Users → System Users
2. Select (or create) an Admin System User → Generate New Token
3. Grant permissions: `ads_management`, `ads_read`
4. Assign the System User to the ad account (and Page) with full control
5. Copy the token into `~/.claude/settings.json` (agency token, shared by all clients) or, for a client with its own Business Manager, into that client folder's `.claude/settings.local.json`: `{"env": {"META_ACCESS_TOKEN": "token_here"}}`. **Never into a client folder's `.claude/settings.json`**, which may be committed to git
6. Restart Claude Code so the env var loads

**Upload command** (run for each file, sequentially — not in parallel):

```bash
AD_ACCOUNT_ID=$(python3 -c "import json; print(json.load(open('reference/meta-ads-config.json'))['ad_account_id'])")
HASH=$(curl -s -X POST \
  "https://graph.facebook.com/v21.0/act_${AD_ACCOUNT_ID}/adimages" \
  -H "Authorization: Bearer $META_ACCESS_TOKEN" \
  -F "filename=@outputs/generated-assets/[CreativeName]-SQ_[DD-MM-YYYY].png" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(list(d['images'].values())[0]['hash'])")
echo "SQ hash: $HASH"
```

Run the same command for VT and HZ variants. **Capture all three hashes for
every creative** — all three are used programmatically in Step 4c via
`asset_customization_rules`, which maps each hash to its correct placement group.

| Size | File suffix | Dimensions |
|---|---|---|
| Square | `-SQ_` | 1080×1080 |
| Vertical | `-VT_` | 1080×1920 |
| Horizontal | `-HZ_` | 1920×1080 |

### 4b — Select the landing page

For `instant_form`, the conversion happens in the form, so the landing page is
only the form's "visit website" / thank-you link: use `landing_pages.default`
unless a page matches the offer better.

Use the `landing_pages` map in `reference/meta-ads-config.json` to pick the most
relevant destination for this creative's product/service or offer. Match on
photo folder name or offer label, and fall back to `default`. If no mapping fits well,
browse `website_domain` (via `WebFetch`) for the best matching product or
collection page.

Always use a real, working URL on `website_domain`. Never make one up.

### 4c — Create the ad with Placement Asset Customization (PAC)

```json
{
  "object_story_spec": {"page_id": "{page_id from config}"},
  "asset_feed_spec": {
    "images": [
      {"hash": "{SQ_HASH}", "adlabels": [{"name": "img_sq"}]},
      {"hash": "{VT_HASH}", "adlabels": [{"name": "img_vt"}]},
      {"hash": "{HZ_HASH}", "adlabels": [{"name": "img_hz"}]}
    ],
    "bodies": [{"text": "{Primary Text from the Sheet}"}],
    "titles": [{"text": "{Ad Headline from the Sheet}"}],
    "link_urls": [{"website_url": "{landing_page}", "display_url": "{display_link from config}"}],
    "ad_formats": ["SINGLE_IMAGE"],
    "call_to_action_types": ["{cta_type from config}"],
    "asset_customization_rules": [
      {
        "customization_spec": {
          "publisher_platforms": ["facebook", "instagram"],
          "facebook_positions": ["feed", "marketplace", "right_hand_column"],
          "instagram_positions": ["stream"]
        },
        "image_label": {"name": "img_sq"}
      },
      {
        "customization_spec": {
          "publisher_platforms": ["facebook", "instagram", "messenger"],
          "facebook_positions": ["story"],
          "instagram_positions": ["story", "reels"],
          "messenger_positions": ["story"]
        },
        "image_label": {"name": "img_vt"}
      },
      {
        "customization_spec": {
          "publisher_platforms": ["facebook"],
          "facebook_positions": ["instream_video"]
        },
        "image_label": {"name": "img_hz"}
      }
    ]
  }
}
```

**Instant forms** (`conversion_location: instant_form`): the ad's call to
action must carry the form. Add the form to the creative's call-to-action
value: `"call_to_action": {"type": "{cta_type}", "value": {"lead_gen_form_id": "{lead_form_id}"}}`
(alongside `call_to_action_types` in `asset_feed_spec`). If the connector or
API rejects the form on a PAC ad, create the ad without it, still PAUSED, and
tell the user to attach `lead_form_id` in Ads Manager (Ad → Destination →
Instant form) before activating. Verify on the first run which way works for
this account and note it in the summary.

Use `ads_create_ad` with:

| Parameter | Value |
|---|---|
| Ad set | This creative's own ad set ID |
| Name | `[Offer]-[Angle]-[Variant]_[DD/MM/YYYY]` (see naming convention below) |
| Status | **PAUSED** |
| Display link | `display_link` from config |
| Personalised destinations | Off |

---

## Copy — One Primary Text and One Headline per Ad

Each ad gets **exactly one** primary text and **one** headline, both taken
word for word from the creative's Creative Generations row:

- **Primary text** → the `Primary Text` column
- **Headline** (the line below the image) → the `Ad Headline` column

Don't write extra variations. With several texts Meta mixes them per viewer,
so a result can no longer be traced to the components the card says it
tests, and copy written here would skip the user's Phase 2.5 approval. If a
row has no `Ad Headline` (older brief), stop and ask the user for one rather
than writing it yourself.

---

## Ad Naming Convention

```
[Offer]-[Angle]-[Variant]_[DD/MM/YYYY]
```

Offer, angle and variant come directly from the Sheets creative name, dropping
the size suffix. Keep this exact form: `ads-analytics` matches each Meta ad to
its Creative Generations row (and so to its components) by this name.
Examples:
- `Vahennys60-Hinta-A_06/07/2026`
- `IlmainenKartoitus-Luotettavuus-B_06/07/2026`

---

## Creative Enhancements — ⚠️ ALL MUST BE OFF ⚠️

**Check every enhancement on every ad and confirm all are disabled. Meta
silently re-enables these — check twice before saving each ad.**

- Site links: **OFF**
- Website highlights: **OFF**
- Promotions: **OFF**
- Products: **OFF**
- Music: **OFF** (if present)
- Image enhancements: **OFF**
- Automatic placements enhancements: **OFF**
- Advantage+ creative: **OFF**

After setting them to off, check again before saving.

**Why this matters for this agency:** the ads are designed from the client's
real photos and must not get Meta's "AI info" label or be altered by Meta's
generative AI (image expansion, background generation, text variations).
When creating the ad through the API, opt out explicitly as well:

```json
"degrees_of_freedom_spec": {
  "creative_features_spec": {
    "standard_enhancements": {"enroll_status": "OPT_OUT"}
  }
}
```

If the connector or API rejects this field, create the ad without it and
tell the user to confirm in Ads Manager (Ad → Advantage+ creative /
Creative enhancements) that every enhancement is off before activating.
Never mark an ad as AI-generated: these ads contain no AI-generated imagery.

---

## Final Verification Checklist

Before completing setup, confirm every item:

- [ ] Campaign status: PAUSED
- [ ] All ad sets: PAUSED
- [ ] All ads: PAUSED
- [ ] Geographic targeting matches the brief (default: `countries` from config, no exclusions)
- [ ] Audience Network excluded from placements on every ad set
- [ ] All creative enhancements: OFF on every ad
- [ ] CTA: `cta_type` from config on every ad
- [ ] Exactly 1 primary text and 1 headline on every ad, word for word from the Sheet
- [ ] Objective and conversion location match the config; for instant forms, `lead_form_id` attached (or the user told to attach it)
- [ ] Ad names follow naming convention with date suffix
- [ ] Personalised destinations: OFF
- [ ] Display link: `display_link` from config on every ad
- [ ] Landing page: a real, working URL on `website_domain` on every ad

---

## Output Summary

After completing setup, produce a **Campaign Structure Summary**:

```
CAMPAIGN SETUP COMPLETE — AWAITING HUMAN REVIEW
================================================
⚠️  Everything is PAUSED. No spend will occur until manually activated.

ABO TESTING CAMPAIGN
  Campaign ID:   [ID]
  Campaign Name: [Name]
  Status:        PAUSED

BUDGET: [total]/day total − [control]/day control = [X]/day × [N] ad sets

AD SETS ([N] total — one per creative):
  [Offer]-[Angle]-[Variant] | ABO | [date]
    ID: [ID] | Budget: [currency_symbol][X]/day | Ads: 1 | Status: PAUSED
    Ads:
      [AdName] — ID: [ID] — PAUSED
      ...
  ...

TOTAL ADS CREATED: [N]

ALL CAMPAIGNS, AD SETS, AND ADS ARE PAUSED.
Nothing is live. Manual review and activation required before any spend occurs.
```
