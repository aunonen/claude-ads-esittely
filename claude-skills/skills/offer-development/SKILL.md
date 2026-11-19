---
name: offer-development
description: >
  Develops new offers for the brand as proposals the client can approve: built
  from what the client can actually deliver (service details, capacity,
  guarantees), the four value levers (dream outcome, likelihood, time, effort)
  and offer components (core, risk reversal, time, bonus, scope), with evidence
  from competitors' offers, the agency library and the brand's own results.
  Writes context/offer-proposals.md and the client log's "Tarjousehdotukset"
  tab; approved proposals move to the offer brief's Approved Offers. Invoke as
  Phase 1.5 of create-new-ads when fewer than 3 offers are approved or Phase 0
  recommends an offer test, or whenever the user asks to develop, improve or
  propose offers.
---

# Offer Development

The offer is the component the ads test most (`static-ads-strategy`, Principle
1). This skill turns "what could we offer?" into concrete proposals the client
can say yes or no to. **The client's approval stays the gate:** nothing here
goes into a live ad until it is in the offer brief's _Approved Offers_ with a
name and a date.

Runs in a client folder. Writes in the client's language (Finnish by default).

---

## Step 1 — Read

- `context/offer-brief.md` — _Approved Offers_ (with components), _Service
  details_ (what's included, process, area, timeline, price range, financing
  and subsidies, warranties, capacity, jobs not wanted), _Objections_, _Real
  Deadlines_, _Off-Limits Claims_, _Stage of Sophistication_
- `context/offer-proposals.md` — earlier proposals and their status. Never
  re-propose a `Rejected` or `Withdrawn` proposal unless something has changed;
  say what.
- `context/learnings.md` — which offers and components won or lost
- `context/audience-hypotheses.md` — audiences and their problems/desires, and
  the _Offers_ table: offer ideas (`Idea`) from competitors, the library and
  our own hypotheses, each with its evidence. When an idea becomes a proposal,
  set its _Client approval_ to `Proposed (P-00X)`; when the client approves,
  `Approved`
- The newest `outputs/analytics/ad-inspiration-report-*.md` — competitors'
  offers (incl. offers hidden in CTAs) and their evidence
- `../../library/patterns.md` → `OFF` cards fitting the client's buying
  situation (read only)
- `~/.claude/skills/static-ads-strategy/SKILL.md` → Principle 1

## Step 2 — Map what the client can deliver

Before any idea, list the client's real levers from _Service details_: what
they can promise (speed, fixed price, guarantees, free survey, financing,
subsidy help), what it costs them, and capacity limits. **If something an
offer would need is unknown** (e.g. "can you commit to an install date?",
"would you give a price guarantee?"), write it as a question for the client
instead of assuming it.

## Step 3 — Build 6–10 proposals

Use the four value levers and the offer components:

| Lever | Raise / lower | Typical components |
|---|---|---|
| Dream outcome | ↑ the result the customer wants, stated concretely | `core` |
| Likelihood of achievement | ↑ why it will work for them | `risk reversal` (guarantee, fixed price, no obligation), proof |
| Time delay | ↓ how soon they get it | `time` (install by…, quote within…) |
| Effort and sacrifice | ↓ what they have to do | `core` (turnkey), `bonus` (we handle the subsidy paperwork) |

Plus `scope` (who it's for, until when). Each proposal changes the offer in a
way the customer would notice, not just its wording. Cover different levers,
and include at least one proposal that removes the strongest objection in the
offer brief.

Sources for ideas, in order: what the client can deliver (Step 2), the brand's
own results, competitors' offers with strong evidence, library `OFF` cards.
A competitor's offer is a starting point, never something to copy.

## Step 4 — Filter

Drop any proposal that:

- the client can't deliver at the volume the ads could bring (capacity)
- breaks `Off-Limits Claims` or consumer-protection rules on prices and
  savings (no savings or "from" prices without a documented basis, no fake
  urgency: deadlines only from _Real Deadlines_)
- is the same as an approved offer with different words

## Step 5 — Write the proposals

For each remaining proposal, a row in `context/offer-proposals.md`:

- **ID** (`P-001`, next free) and a **proposed label** (PascalCase, ASCII)
- **The offer**: one sentence the customer would read
- **Components**: `core · risk reversal · time · bonus · scope`
- **What it requires from the client**: work, cost, risk, capacity
- **Answers objection**: which one
- **Evidence**: competitor ads (file, class), library card (ID, level), own
  results — or "new: no evidence yet"
- **Suggested test**: the whole offer against the current one, or one
  component (e.g. the same offer with a fixed-price guarantee vs without),
  everything else held constant
- **Status** `Proposed`, date

## Step 6 — Show the client (Tarjousehdotukset tab)

Write the proposals to the **Tarjousehdotukset** tab of the client log
(`spreadsheet_id` in `reference/gws-config.json`). If the tab doesn't exist,
create it with this header row first:

`ID | Ehdotus | Mitä asiakas saa | Osat | Mitä vaatii teiltä | Vastaa huoleen | Peruste | Ehdotettu testi | Tila | Päivä | Kommentti / hyväksyntä`

Write the rows in plain Finnish for the client: no internal jargon (no
"Most aware", no "risk reversal": say "takuu", "kiinteä hinta"). Set the
status to `With client` in both places, and give the user the link. List the
questions from Step 2 separately, for the user to ask the client.

## Step 7 — Record decisions (when the user reports back)

When the user tells you the client's answer (or it appears in the tab's last
column):

- **Approved / Approved with changes** → add a row to _Approved Offers_ in
  `offer-brief.md` with the label, the final wording, components, terms,
  validity and "Approved by client: <name>, <date>". Update the status in the
  file and the tab.
- **Rejected** → status `Rejected` with the reason in the file and the tab.

Never mark anything approved on your own or from a comment that doesn't
clearly say so: ask the user.

## Output

> **Offer proposals: [N] written ([L] levers covered), [Q] questions for the client. Shown in Tarjousehdotukset: [link]. Approved offers now: [A].**

In `create-new-ads`, the round continues with the offers already approved;
new ones join a later round once approved.
