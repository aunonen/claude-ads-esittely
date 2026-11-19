# CLAUDE.md — Agency hub

This file provides guidance to Claude Code (claude.ai/code) for the agency's Meta Ads workspaces. It's loaded in every session opened here **and** in every client folder below it (Claude Code reads `CLAUDE.md` files from parent folders too), so keep it about the agency, never about one client.

---

## The agency

> Fill in once. `/onboard` uses this to pre-fill each client's `context/personal-info.md`.

| | |
| --- | --- |
| Agency name | No name yet: early-stage one-person agency, no website |
| Who works here | One person does everything: offer, strategy, creative, campaigns, reporting, client contact |
| Clients | Businesses running Meta ads: service businesses and online stores |
| Services for clients | Building the offer, strategy, static ad concepts from the client's own material (usually photos of their projects), producing the ads, campaign planning, publishing, reporting |
| Working language | **Finnish, everything.** Talk to the user in Finnish, and write all ad copy (headlines, on-image text, primary text, CTAs) in Finnish unless a client's `context/` says otherwise |
| How approvals work | The client approves the ads and the campaign plan. The agency then publishes the ads: the workflow builds everything PAUSED and the user activates it in Ads Manager after the client's approval |

**Service-business clients:** many clients sell services, not products. For them, `reference/products/Images/` holds the client's project photos (one folder per service or project type) instead of packshots, and the "product" in a creative is the finished work or the service result. Every ad is built on the client's real photos; nothing is AI-generated.

---

## How the folders work

```
Claude ads/                      ← agency hub (this folder)
├── CLAUDE.md                    ← this file: agency context, loaded everywhere below
├── README.md                    ← setup + day-to-day guide
├── _template/                   ← clean client workspace. Never onboard or edit a client here.
├── library/                     ← agency ad library: public ads, pattern cards, style library (see library/README.md)
├── plans/                       ← plans for changes to the workspace itself
└── clients/
    └── <client-slug>/           ← one folder per client: own CLAUDE.md (Brand Assets), context/,
                                    reference/, outputs/, Sheet + Drive IDs, Meta account IDs
```

Shared by every client, outside this folder (`~/.claude/` = `C:\Users\merik\.claude\`):

| Path | What |
| --- | --- |
| `~/.claude/skills/` | The ads pipeline: `create-new-ads`, `ads-analytics`, `ad-inspiration-collection`, `ad-library`, `offer-development`, `customer-research`, `competitor-analysis`, `creative-strategy`, `creative-generation`, `meta-ads-campaign-setup`, `static-ads-strategy`, `ad-design/` (design guide, shared `base.css`, `render.py`), plus `skill-creator`, `mcp-integration` |
| `~/.claude/commands/` | `/new-client`, `/onboard`, `/prime`, `/create-plan`, `/implement` |
| `~/.claude/settings.json` | The agency's Meta System User token (`META_ACCESS_TOKEN`), shared by every client whose ad account is in the agency's Business Manager |

## Rules

- **One client per session.** Ads work always runs in a session opened in `clients/<slug>/`. The skills read `context/` and `reference/` relative to the session's folder, so they don't work from the hub.
- **No cross-client bleed.** Never read or reuse another client's claims, numbers, assets, copy or customer research. Each client's ads use only what's in its own folder. One named exception: the agency library may record a pattern ID with won/lost and a date from a client's test (the "Kirjastopalaute" lines), nothing else.
- **The agency library holds public ads only.** `library/` contains public Meta ads that pass its evidence gate, and the patterns and style entries drawn from them: never a client's ads, name, numbers, claims or assets. It is maintained in a hub session with the `ad-library` skill; client sessions read it (`../../library/`) but never write to it. Pattern levels rise only with the user's approval.
- **Skills are shared.** A change to `~/.claude/skills/` affects every client. Client-specific rules go in that client's `context/` files.
- **Template changes** (new context files, new config fields) go in `_template/`. Existing client folders don't update automatically, so tell the user which clients would need the same change.
- **Real photos, no AI imagery.** Ads are HTML designs on the client's own photos, rendered to PNG (`~/.claude/skills/ad-design/`). Never generate or AI-edit images, so ads look authentic and carry no AI label.
- **Nothing goes live.** The workflow only ever creates PAUSED campaigns.
- **Git tracks the system.** Two repos, each with a private GitHub remote (`aunonen/claude-ads`, `aunonen/claude-skills`): this hub folder, and `~/.claude/` (whitelisted to `skills/` and `commands/` only; `settings.json` with the token is excluded). Client photos, inspiration images and generated output are git-ignored. When the user edits skills or the workspace themselves and asks for a consistency check, start from `git status` / `git diff` in **both** repos, then check that related skills, `CLAUDE.md`, README, `_template/` and existing client folders still agree. Commit and push only when the user asks.

## Commands

| Command | Where | What |
| --- | --- | --- |
| `/new-client <name>` | hub | Copies `_template/` to `clients/<slug>/` |
| `/onboard` | client folder | One-time brand, offer, Meta and Google setup for that client |
| `/prime` | anywhere | In a client folder: loads that client's context. In the hub: lists clients and their setup status |
| `/create-plan`, `/implement` | anywhere | Plan and make changes to the workspace itself |

---

## Critical Instruction: Maintain This File

When the agency setup changes (new shared command or skill, a change to the folder structure, a new rule for all clients), update this file and the README. When a client-level structure changes, update `_template/CLAUDE.md` too.
