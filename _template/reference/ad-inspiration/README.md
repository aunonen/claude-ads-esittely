# Ad Inspiration

A curated swipe file of static image ads. Phase 1 of the workflow (`competitor-analysis`) reads every image here, analyses the visual + copy, logs it to the "Ad Inspiration" Google Sheet tab, and translates the patterns into ad ideas for your brand, component by component.

## What's included

`_starter-formaatit/` (not included in this showcase copy) holds a starter set of static ads from DTC brands (supplements, personal care, food, home). They're **format examples only**: Phase 1 skips them and never treats them as evidence of what works. Real inspiration comes from the client's own market, collected with the `ad-inspiration-collection` skill.

## Add your own

Ads you add here are higher-signal than the starter set:

- **Competitor ads** you've found in the Meta Ad Library that are clearly performing (long-running, many variations)
- **Cross-category ads** with a format or hook you want to borrow
- **Your own past winners.** Prefix them with your brand name (e.g. `yourbrand-summer-bundle-comparison.jpg`) so they're recognised and studied especially closely.

Use descriptive kebab-case filenames: `<brand>-<what-the-ad-does>.jpg`. The filename is used for de-duplication, so each image is only analysed once.

## Collecting ads

Ask Claude to **collect ad inspiration** (the `ad-inspiration-collection` skill): it plans searches by relevance tier, browses Meta's Ad Library, scores each ad's evidence and goal, and saves the image, a sidecar and a log row for each. The sections below describe what it saves, in case you add ads by hand.

## Primary text: a sidecar file per ad

A screenshot shows the image, not the text above it. Save the ad's text in a `.txt` file with **the same name** as the image (`brand-what-it-does-A.jpg` + `brand-what-it-does-A.txt`):

```
Primary text: [the ad's full primary text, copied from the Ad Library]
Headline: [the line below the image]
CTA: [button text]
Ad Library: [link]
Goal: [lead form / quote request / call / website conversion / purchase / content / event / awareness]
Started running: [date]
EU reach: [from the ad's details, with the date read]
Targeting: [locations; age; gender]
```

Without it the analysis marks the primary text "missing" and can't use the ad's copy.

## Evidence class

A good-looking ad isn't proof that it works: the Ad Library hides spend and results. When you collect an ad, score it from what the Ad Library shows (how long it has run, how many versions, the advertiser's testing habits) and end the filename with its class: `-A` (strong), `-B` (moderate) or `-C` (weak, format idea only), e.g. `brand-tax-credit-headline-A.png`. The scoring table is in the `ad-inspiration-collection` skill. For more detail, keep a `_evidence-log.md` in this folder with each file's points. Unscored ads still get analysed, but the strategy doesn't treat them as proof that an angle works.
