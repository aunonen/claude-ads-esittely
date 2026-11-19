# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

This is a **client workspace** inside an agency's Meta Ads setup: one folder per client brand, under `clients/` in the agency hub. The agency's own context lives in the hub `CLAUDE.md` one level up (loaded automatically). Everything in *this* folder is about **this client only**: never use claims, assets or numbers from another client's folder.

It's a **Meta Ads Creative Workspace** for Claude Code. It's a structured environment where Claude acts as an agent assistant that researches ad inspiration, writes a creative strategy, designs static image ads from the client's own photos (HTML layouts rendered to PNG, no AI-generated imagery), and builds them into a **paused** Meta Ads Manager campaign for human review.

The user spins up fresh Claude Code sessions repeatedly, using `/prime` at the start of each to load essential context without bloat. A brand-new user runs `/onboard` once to configure the workspace for their brand.

**This file (CLAUDE.md) is the foundation.** It is automatically loaded at the start of every session. Keep it current — it is the single source of truth for how Claude should understand and operate within this workspace.

> **Setup status:** If the Brand Assets table below still contains `{{…}}` placeholders, the workspace hasn't been configured yet. Tell the user to run `/onboard` before running the ads workflow.

---

## The Claude-User Relationship

Claude operates as an **agent assistant** with access to the workspace folders, context files, commands, and outputs. The relationship is:

- **User**: Defines goals, provides context about their role/function, and directs work through commands
- **Claude**: Reads context, understands the user's objectives, executes commands, produces outputs, and maintains workspace consistency

Claude should always orient itself through `/prime` at session start, then act with full awareness of who the user is, what they're trying to achieve, and how this workspace supports that.

---

## Workspace Structure

```
.
├── CLAUDE.md                    # This file — client context + Brand Assets, always loaded
├── .claude/
│   └── settings.local.json      # Only if this client has its own Meta token (git-ignored)
├── context/                     # Brand, customer, offer and strategy context. Read by /prime and the skills.
├── plans/                       # Implementation plans created by /create-plan
├── outputs/generated-assets/    # Creative briefs, state files, ad designs (designs/*.html) and rendered PNGs
├── reference/
│   ├── ad-inspiration/          # Curated swipe file of static ads (Phase 1 input)
│   ├── brand/brand.css          # Brand colours + fonts as CSS variables; every ad design uses it
│   ├── brand/fonts/             # Licensed font files, if the brand's fonts aren't on Google Fonts
│   ├── design-assets/           # Logo, icons, backgrounds, press/trust logos
│   ├── products/Images/         # The client's own photos, one folder per product/service
│   ├── gws-config.json          # Google Sheet + Drive IDs
│   └── meta-ads-config.json     # Meta ad account, pixel, page, budget, targeting, landing pages
└── scripts/                     # Automation scripts (if applicable)
```

Shared across all clients (not in this folder):

- `~/.claude/skills/`: the ads pipeline (see "Ads Workflow" below) and `ad-design/` (design guide, base.css, render.py)
- `~/.claude/commands/`: `/onboard`, `/prime`, `/create-plan`, `/implement`, `/new-client`
- `~/.claude/settings.json`: the agency's `META_ACCESS_TOKEN`
- `../../CLAUDE.md` and `../../README.md`: the agency hub guide

Changing a skill changes it for every client, so make client-specific rules in this folder's `context/` files instead.

**Key directories and files:**

| Path | Purpose |
| --- | --- |
| `context/` | Who the user is, the business, strategy (with Ad Targets), offer brief (approved offers, USPs, CTAs, proof, objections, real deadlines, off-limits claims, service details), audience hypotheses (everything worth testing: audiences, problems, desires, awareness levels, offers, angles, arguments, creative concepts and creative copy, each with its source, evidence and status), offer proposals waiting for the client (`offer-proposals.md`), research sources (`research-sources.md`), necessary beliefs, customer research, and `learnings.md`: what earlier rounds showed, updated by `ads-analytics`. |
| `reference/ad-inspiration/` | Competitor and cross-category ads analysed in Phase 1: image + `.txt` sidecar (primary text, goal, Library link) per ad, and `_evidence-log.md` with each ad's evidence class. Collected with the `ad-inspiration-collection` skill; `_starter-formaatit/` holds format examples only. |
| `reference/brand/brand.css` | The brand's colours and fonts for the ad designs. Change it and every ad restyles. |
| `reference/design-assets/` | Every non-photo visual asset the ad designs may use (logo, icons, press logos). See its README. |
| `reference/products/Images/` | The client's own photos (products, or projects for a service business), one folder per product/service. The raw material of every ad. See its README. |
| `reference/meta-ads-config.json` | Everything account-specific that campaign setup needs. |
| `reference/gws-config.json` | The two Google Sheets and the Drive folders used for logging: the client log (Creative Generations, Brief and Tarjousehdotukset tabs, may be shared with the client) and the internal inspiration sheet (Ad Inspiration tab, and the Komponentit tab where you rate every component 1–5; never shared). |
| `outputs/` | Deliverables and generated creatives. |
| `plans/` | Detailed implementation plans. |

---

## Brand Assets

Canonical source for the brand's visual identity. Skills reference this section rather than repeating these values. Filled in by `/onboard`.

| Property | Value |
| --- | --- |
| Brand name | **{{BRAND_NAME}}** |
| Website | {{yourbrand.com}} (ei vielä verkkosivuja) |
| Primary color | `#2F5BFF` (sähkönsininen). Accent for headlines, badges, CTA bars, design elements. |
| Secondary / light background | `#EEF1FF` |
| Background | `#FFFFFF` |
| Text | `#111111` |
| Font — Headline | **Space Grotesk** (700), reserved exclusively for the main headline text on a creative. Never used for subline, badge, additional copy, or logo. Loaded in `reference/brand/brand.css`. |
| Font — Body / Badge | **Inter**, used for every other on-image text element: subline, social-proof badge text, USPs, additional copy. Loaded in `reference/brand/brand.css`. |
| Primary logo file | `reference/design-assets/{{logo.svg}}`: tekstilogo (nimi brändifontilla, tumma + vaalea versio), tehdään kun nimi on päätetty |

> **The values here and in `brand.css` must match.** `brand.css` is what the ads actually use; this table is the human-readable record.

> **Two-font system:** headline font for the headline only, body font for everything else rendered in the image. Never mix these roles, and never introduce a third font (the only exception: an optional handwriting font, `--font-hand`, for the sticky-note and handwritten formats; see the ad-design guide).

**Logo: full lockup, ~3-in-4 frequency.**

When a creative includes the logo (per the Creative Brief's per-card decision, typically **~3 in 4 creatives in a batch**, not every one), it is the primary logo file above (or its light version on dark photos), centred at the top of the image with clear open space around it by default; native formats (review card, note) may place it top-left. Never a bare icon mark as the main logo.

Secondary marks (e.g. a checkmark or seal version of the logo) are **not** the main logo. Reserve them for illustrating a specific claim or USP callout, never as the primary brand logo upload.

Accent/USP icon sets in `reference/design-assets/` that come in several color variants: pick the variant matching the colour of the product or service featured in a given creative, not a fixed brand-wide accent.

---

## Ads Workflow

Say "let's make some new ads" (or similar) to trigger the `create-new-ads` skill, which runs a results check and four phases in one continuous context:

| Phase | Skill | What happens |
| --- | --- | --- |
| 0 | `ads-analytics` | Reads earlier ads' results, names the control and the next round type (first round if there are no earlier ads) |
| 1 | `competitor-analysis` | Analyses new images in `reference/ad-inspiration/`, logs them to the internal inspiration Sheet, maps the set component by component (weighted by evidence; the agency library in `../../library/` adds tier-3 patterns), and writes ideas that fit the round type, each with a hypothesis; report saved to `outputs/analytics/` |
| 2 | `creative-strategy` | Writes a Test Plan sized to the budget (test slots = total ÷ min per ad, round type from the testing logic), a ~20-card pool with every component on each card, and a recommended selection (uses `static-ads-strategy` as its rubric) |
| 2.5 | *Human checkpoint* | User picks the cards for the test; Claude checks the pick against the Test Plan and warns, never blocks |
| 3 | `creative-generation` | Designs approved creatives as HTML layouts on the client's own photos, renders SQ/VT/HZ PNGs (`~/.claude/skills/ad-design/`), uploads to Drive, logs to the "Creative Generations" tab |
| 3.5 | *Human checkpoint* | User reviews the actual ads and asks for revisions (quick edits to the designs) |
| 4 | `meta-ads-campaign-setup` | Builds an ABO testing campaign in Meta Ads Manager, one ad set per ad with an equal share of the total budget. **Everything PAUSED. Nothing ever goes live.** |

Supporting skills: `customer-research` (customer research with sources and reliability levels; also in `/onboard`), `offer-development` (offer proposals for the client to approve; Phase 1.5 when needed), `ad-inspiration-collection` (collects and scores ads from Meta's Ad Library before Phase 1; say "collect ad inspiration"), `static-ads-strategy` (the six-principle framework), `ad-design/` (design guide, shared `base.css`, `render.py`), `skill-creator`, `mcp-integration`.

**Required connections:** Chrome or Edge (for rendering), Meta Ads connector, the `gws` Google Workspace CLI, and a `META_ACCESS_TOKEN` (the agency's, in `~/.claude/settings.json`, or this client's own in `.claude/settings.local.json`). See the hub README.

---

## Commands

### /onboard

**Purpose:** One-time setup. Interviews the user, then fills in Brand Assets (above), `context/` files, `reference/meta-ads-config.json`, `reference/gws-config.json`, and the Meta token. Finishes with a readiness check. Safe to re-run to update any section.

### /prime

**Purpose:** Initialize a new session with full context awareness.

Run this at the start of every session. Claude will:

1. Read CLAUDE.md and context files
2. Summarize understanding of the user, workspace, and goals
3. Confirm readiness to assist (or point to `/onboard` if the workspace isn't configured)

### /create-plan [request]

**Purpose:** Create a detailed implementation plan before making changes.

Use when adding new functionality, commands, scripts, or making structural changes. Produces a thorough plan document in `plans/` that captures context, rationale, and step-by-step tasks.

Example: `/create-plan add a competitor analysis command`

### /implement [plan-path]

**Purpose:** Execute a plan created by /create-plan.

Reads the plan, executes each step in order, validates the work, and updates the plan status.

Example: `/implement plans/2026-01-28-competitor-analysis-command.md`

---

## Critical Instruction: Maintain This File

**Whenever Claude makes changes to the workspace, Claude MUST consider whether CLAUDE.md needs updating.**

After any change — adding commands, scripts, workflows, or modifying structure — ask:

1. Does this change add new functionality users need to know about?
2. Does it modify the workspace structure documented above?
3. Should a new command be listed?
4. Does context/ need new files to capture this?

If yes to any, update the relevant sections. This file must always reflect the current state of the workspace so future sessions have accurate context.

**Examples of changes requiring CLAUDE.md updates:**

- Adding a new slash command → add to Commands section
- Creating a new output type → document in Workspace Structure or create a section
- Adding a script → document its purpose and usage
- Changing workflow patterns → update relevant documentation

---

## Session Workflow

1. **First time only**: Run `/onboard`
2. **Start**: Run `/prime` to load context
3. **Work**: Use commands or direct Claude with tasks (e.g. "let's make some new ads")
4. **Plan changes**: Use `/create-plan` before significant additions
5. **Execute**: Use `/implement` to execute plans
6. **Maintain**: Claude updates CLAUDE.md and context/ as the workspace evolves

---

## Notes

- Keep context minimal but sufficient — avoid bloat
- Never commit secrets: tokens belong in `~/.claude/settings.json` (agency) or this folder's `.claude/settings.local.json` (git-ignored), never in a tracked file
- Plans live in `plans/` with dated filenames for history
- Outputs are organized by type/purpose in `outputs/`
- Reference materials go in `reference/` for reuse
