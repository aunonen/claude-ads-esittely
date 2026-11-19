# Plan: Asiakastutkimuksen skilli — lähteet, menetelmä ja luotettavuus

**Created:** 2026-10-26
**Status:** In progress — implemented 2026-10-26
**Request:** Asiakastutkimukselle (tutkimusraportti, kielipankki, yleisöhypoteesit, uskomukset) oma ohjeistus, koska nykyinen on ohut ja tuottaa verkkohaun luonnoksia, joiden päälle yleisöhypoteesit, ongelmat ja creative copy rakentuvat.

---

## Overview

### What This Plan Accomplishes

Uusi skilli `customer-research` määrittelee, mistä tutkimus tehdään (lähteet tärkeysjärjestyksessä), miten paljon aineistoa tarvitaan, miten sitaatit merkitään, miten segmentit ja ongelmat tunnistetaan, ja antaa jokaiselle osiolle luotettavuustason. Se päivittää tutkimusta, kun asiakkaalta saadaan uutta aineistoa. Tulos kirjoitetaan nykyisiin tiedostoihin, joten muu järjestelmä toimii sellaisenaan.

### Why This Matters

Yleisöhypoteesit, ongelmat, kielipankki ja vastaväitteet ohjaavat kortteja ja creative copya. Jos ne ovat verkkohaun luonnoksia keskustelupalstoilta, mainokset puhuvat kuvitellulle asiakkaalle. Luotettavuustason ansiosta strategia tietää, mihin se voi nojata ja mitä pitää testata.

---

## Current State

### Relevant Existing Structure

- `/onboard` kierros 3: asiakkaan omat lähteet ensin, sitten verkkohaku; luonnokset tutkimusraportista, yleisöhypoteeseista (audience-hypotheses.md) ja uskomuksista
- `_template/context/customer-deep-research-report.md`: osiot (segmentit, ratkaisut, myytit, ostopolku, ostamisen jälkeen, kielipankki, kilpailijat, kulmamahdollisuudet)
- `_template/context/audience-hypotheses.md`: testattavat yleisöt, ongelmat, halut ja tietoisuustasot näyttöineen
- `_template/context/necessary-beliefs.md`: tausta
- Lämpösaaga: tutkimus "Draft by Claude" julkisilta keskustelupalstoilta

### Gaps or Problems Being Addressed

- Ei menetelmää: lähteiden määrä ja laatu, sitaatin ja tulkinnan erottelu, segmentin tunnistaminen, päivitys.
- Ei luotettavuustasoja: luonnos ja tarkistettu tieto näyttävät samalta.
- Asiakkaan omaa aineistoa (puhelut, tarjouspyynnöt, arvostelut) ei kerätä järjestelmällisesti, vaikka se on paras lähde.

---

## Proposed Changes

### Summary of Changes

- Uusi skilli `customer-research` (tilat: initial, update, check)
- Tutkimusraportin pohjaan luotettavuustasot ja lähdeluettelo
- Kielipankin sitaatteihin lähde, päivä ja tyyppi
- `/onboard` kierros 3 kutsuu skilliä
- `creative-strategy` ja `competitor-analysis` huomioivat luotettavuustason

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `~/.claude/skills/customer-research/SKILL.md` | Tutkimuksen menetelmä, lähteet, sitaatit, segmentit, luotettavuus, päivitys |
| `_template/context/research-sources.md` | Lähdeluettelo: mitä on luettu, milloin, kuinka paljon, mistä (asiakkaan oma / julkinen) |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `_template/context/customer-deep-research-report.md` | Jokaiseen osioon luotettavuustaso; kielipankin sitaattimuoto |
| `_template/context/audience-hypotheses.md` | Rivien näytön luotettavuus tutkimuksen tasoista |
| `~/.claude/commands/onboard.md` | Kierros 3 käyttää `customer-research`-skilliä |
| `~/.claude/skills/creative-strategy/SKILL.md` | Kielipankin painoarvo luotettavuustason mukaan |
| `~/.claude/skills/competitor-analysis/SKILL.md` | Yleisöhypoteesien ja ongelmien luotettavuus näkyy Starting Pointissa |
| `README.md`, `CLAUDE.md`, `_template/CLAUDE.md` | Uusi skilli |

---

## Design Decisions

### Key Decisions Made

1. **Lähteet tärkeysjärjestyksessä:**
   1. asiakkaan omat asiakkaat: tarjouspyyntöjen ja lomakkeiden vapaat tekstit, puheluissa kysytyt asiat (myyjän muistiinpanot tai haastattelu), sähköpostit, asiakkaan arvostelut
   2. asiakkaan haastattelu (myyjä, asentaja): mitä asiakkaat kysyvät, mitä he pelkäävät, miksi kaupat jäävät syntymättä
   3. julkiset arvostelut asiakkaasta ja kilpailijoista (Google, alan palvelut)
   4. keskustelupalstat ja yhteisöt (Suomi24, Facebook-ryhmät, Reddit), media
2. **Luotettavuustasot jokaiselle osiolle ja yleisöhypoteesille:**
   - **Vahvistettu:** asiakkaan omista asiakkaista, vähintään ~10 erillistä lähdettä
   - **Tuettu:** julkisista arvosteluista tai haastattelusta, toistuu useissa lähteissä
   - **Luonnos:** keskustelupalstoilta tai yksittäisistä lähteistä
3. **Sitaatit:** sanatarkka lainaus erotetaan tulkinnasta. Jokaisella sitaatilla on lähdetyyppi (oma asiakas / arvostelu / palsta), lähde ja päivä. Mukaillut tekstit merkitään tulkinnoiksi.
4. **Segmentit ja ongelmat toistuvuuden perusteella:** segmentti tai ongelma kirjataan vasta, kun se toistuu useammassa erillisessä lähteessä; yksittäinen tarina on huomio, ei segmentti.
5. **Vähimmäisaineisto:** esim. 30 sitaattia vähintään 10 lähteestä ennen kuin yleisöhypoteesi kirjataan Tuettu-tasolle; luvut tarkennetaan pilotissa.
6. **Päivitys:** update-tila lisää uutta aineistoa (esim. asiakkaan tarjouspyynnöt), nostaa luotettavuustasoja ja merkitsee muuttuneet kohdat.
7. **Käyttö:** strategia nojaa Vahvistettu- ja Tuettu-tason tietoon; Luonnos-tason ongelmat ja yleisöhypoteesit ovat testattavia oletuksia.

### Alternatives Considered

- **Pelkkä ohjeen tarkennus `/onboard`:iin:** hylätty, koska tutkimusta päivitetään myös myöhemmin ja menetelmä tarvitsee oman paikan.
- **Ulkoinen deep research -palvelu:** voi olla yksi lähde, mutta ei korvaa asiakkaan omaa aineistoa eikä luotettavuustasoja.

### Open Questions (if any)

1. **Ratkaistu 2026-10-26:** asiakkaan oma aineisto kerätään haastattelurungolla (puhelu), ei kirjallista aineistopyyntöä.
2. **Ratkaistu 2026-10-26 (oletus):** aineisto anonymisoidaan aina; nimiä ja yhteystietoja ei kirjata `context/`-tiedostoihin.
3. **Ratkaistu 2026-10-26:** kevyemmät rajat: Tuettu vähintään 15 sitaattia vähintään 6 lähteestä; Vahvistettu asiakkaan omilta asiakkailta vähintään 6 lähdettä.

---

## Step-by-Step Tasks

### Step 1: Pohjat

**Actions:**

- Päivitä `_template/context/customer-deep-research-report.md`: luotettavuustaso per osio, sitaattimuoto (`"sitaatti" — lähdetyyppi, lähde, päivä`).
- `_template/context/audience-hypotheses.md` saa luotettavuuden tutkimuksen tasoista (pohjassa jo sarake).
- Luo `_template/context/research-sources.md`.

### Step 2: Skilli `customer-research`

**Actions:**

- Tilat: initial (ensimmäinen tutkimus), update (uusi aineisto), check (luotettavuuskatsaus ja puutteet).
- Lähteet tärkeysjärjestyksessä, aineiston pyytäminen asiakkaalta, anonymisointi, sitaattien merkintä, segmenttien ja ongelmien tunnistus toistuvuudella, luotettavuustasot, tulos nykyisiin tiedostoihin (tutkimusraportti, yleisöhypoteesit ja Ad components, uskomukset taustaksi).

### Step 3: Kytkennät

**Actions:**

- `/onboard` kierros 3 kutsuu skilliä.
- `creative-strategy`: kielipankin ja yleisöhypoteesien painoarvo luotettavuustason mukaan.
- `competitor-analysis`: luotettavuustasot Starting Pointiin.

### Step 4: Dokumentaatio ja Lämpösaaga

**Actions:**

- README, CLAUDE.md:t.
- Ehdota Lämpösaagalle update-ajoa, kun asiakkaan omaa aineistoa saadaan.

---

## Connections & Dependencies

### Files That Reference This Area

- `audience-hypotheses.md` (Audience ja Problem / desire -arvot), kielipankki (creative copy), `offer-brief.md` (vastaväitteet)

### Updates Needed for Consistency

- Luotettavuustasojen nimet samat pohjissa ja skilleissä.

### Impact on Existing Workflows

- `/onboard` kierros 3 muuttuu; olemassa olevat asiakkaat voivat ajaa update-tilan.

---

## Validation Checklist

- [ ] Jokaisella osiolla ja yleisöhypoteesilla on luotettavuustaso ja lähteet
- [ ] Sitaatit erottuvat tulkinnoista
- [ ] Henkilötietoja ei tallenneta
- [ ] Strategia käsittelee Luonnos-tason tietoa oletuksena

---

## Success Criteria

1. Uusi asiakas saa tutkimuksen, jonka luotettavuus näkyy jokaisessa osiossa.
2. Kun asiakkaan omaa aineistoa tulee, tutkimus päivittyy ja luotettavuus nousee.

---

## Notes

- Lämpösaagan nykyinen tutkimus on Luonnos-tasoa; asiakkaan tarjouspyynnöt ja puhelukysymykset olisivat nopein tapa nostaa sitä.
