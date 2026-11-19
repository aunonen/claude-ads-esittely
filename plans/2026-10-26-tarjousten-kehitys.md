# Plan: Tarjousten kehitys osaksi mainosprosessia

**Created:** 2026-10-26
**Status:** In progress — implemented 2026-10-26
**Request:** Tarjouksia pitää pystyä kehittämään aktiivisesti mainoksia tehdessä, ei vain käyttämään offer briefiin valmiiksi hyväksyttyjä. Asiakkaan hyväksyntä pysyy portinvartijana.

---

## Overview

### What This Plan Accomplishes

Mainosprosessiin lisätään tarjousten kehitysvaihe, joka rakentaa tarjousehdotuksia järjestelmällisesti siitä, mitä asiakas oikeasti pystyy tekemään, kilpailijoiden ja kirjaston tarjouskuvioista sekä omista tuloksista. Ehdotukset menevät asiakkaalle hyväksyttäviksi perusteluineen, ja hyväksytyt siirtyvät offer briefin _Approved Offers_ -taulukkoon ja testiin.

### Why This Matters

Tarjous on järjestelmän tärkein testattava komponentti (static-ads-strategy, Periaate 1; creative-strategyn "big five"). Nyt uusia tarjouksia syntyy vain sivutuotteena Phase 1:n ideoista ("needs client approval"), eikä niitä koskaan suositella testiin. Tarjousten kehittäminen jää siis tekemättä, vaikka se on suurin vipu tulokseen.

---

## Current State

### Relevant Existing Structure

- `context/offer-brief.md`: _Approved Offers_ (label, tarjous, ehdot, voimassa, hyväksyjä), _Service details_ (prosessi, alue, aikataulu, hinta, tuet, takuut, kapasiteetti, ei-toivotut työt), _Real Deadlines_, _Off-Limits_
- `static-ads-strategy`: Principle 1 — Irresistible Offer (unelmatulos, onnistumisen todennäköisyys, aika, vaiva; esimerkit)
- `competitor-analysis`: ideoiden _Offer status_ (Approved / Needs client approval), raportin _Open Questions for the Client_
- `creative-strategy`: hyväksymätön tarjous saa olla poolissa mutta ei suosituksessa; Phase 2.5 varoittaa
- `ad-library`: `OFF`-kuviokortit
- `learnings.md`: tarjousten tulokset komponenteittain

### Gaps or Problems Being Addressed

- Ei vaihetta, joka suunnittelee tarjouksia; uudet tarjoukset syntyvät satunnaisesti.
- Tarjousehdotuksille ei ole muotoa, jonka asiakas voi hyväksyä (mitä luvataan, mitä se vaatii asiakkaalta, riskit).
- Hyväksymättömät tarjoukset eivät koskaan pääse testiin, joten hyvätkin ideat jäävät kokeilematta.
- Tarjouksen osia (esim. takuu, aikalupaus, bonus) ei testata erikseen.

---

## Proposed Changes

### Summary of Changes

- Uusi skilli `offer-development` (tarjousten kehitys)
- Uusi tiedosto asiakkaalle: `context/offer-proposals.md` (ehdotukset ja niiden tila)
- `create-new-ads`: tarjousten kehitys valinnaisena vaiheena 1.5 (ennen strategiaa), kun tarjouksia on vähän tai Phase 0 suosittelee tarjoustestiä
- Offer briefin _Approved Offers_ -taulukkoon tarjouksen osat (mistä tarjous rakentuu)
- `creative-strategy` ja `ads-analytics` tunnistavat tarjouksen osat testattavina

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `~/.claude/skills/offer-development/SKILL.md` | Tarjousehdotusten rakentaminen, arviointi ja asiakkaalle esittäminen |
| `_template/context/offer-proposals.md` | Tarjousehdotusten lista ja tila (ehdotettu / asiakkaalla / hyväksytty / hylätty) |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `_template/context/offer-brief.md` | _Approved Offers_ -taulukkoon sarake "Osat" (perustarjous, riskin poisto, aika, bonus, rajaus) |
| `~/.claude/skills/create-new-ads/SKILL.md` | Phase 1.5 Offer Development (valinnainen), ehdot milloin ajetaan |
| `~/.claude/skills/creative-strategy/SKILL.md` | Allowed values: tarjouksen osa testattavana komponenttina; tarjoustestin rakenne |
| `~/.claude/skills/competitor-analysis/SKILL.md` | Tarjousideat ohjataan `offer-proposals.md`:hen raportin avointen kysymysten sijaan |
| `~/.claude/skills/ads-analytics/SKILL.md` | Tarjousten ja niiden osien tulokset `learnings.md`:hen; ehdotus seuraavasta tarjouskokeilusta |
| `~/.claude/commands/onboard.md` | Kierros 3: myös mitä asiakas voi luvata (kapasiteetti, takuuhalukkuus), jotta tarjouksia voidaan kehittää |
| `README.md`, `_template/CLAUDE.md`, hubin `CLAUDE.md` | Uusi skilli ja tiedosto |

---

## Design Decisions

### Key Decisions Made

1. **Lähtökohta on asiakkaan kyky, ei mainoksen tarve.** Jokainen ehdotus perustuu offer briefin _Service details_ -tietoihin: mitä asiakas pystyy tekemään, missä ajassa, millä kapasiteetilla ja millä riskillä. Tarjousta, jota asiakas ei pysty lunastamaan, ei ehdoteta.
2. **Rakenne Periaatteesta 1.** Ehdotukset rakennetaan neljästä vivusta (unelmatulos ↑, onnistumisen todennäköisyys ↑, aika ↓, vaiva ↓) ja tarjouksen osista: perustarjous, riskin poisto (takuu, kiinteä hinta), aikalupaus, bonus, rajaus (kenelle, mihin asti).
3. **Lähteet:** asiakkaan kyky, kilpailijoiden tarjoukset (Intelligence Report), kirjaston `OFF`-kortit, `learnings.md`:n tulokset ja vastaväitteet (tarjous voi poistaa vastaväitteen).
4. **Ehdotusmuoto asiakkaalle:** suomeksi, jokaisesta: mitä luvataan, mitä se vaatii asiakkaalta (työ, kustannus, riski), mihin vastaväitteeseen vastaa, näyttö (kilpailija, kirjasto, oma tulos) ja ehdotettu testi. Asiakas voi hyväksyä, muokata tai hylätä.
5. **Hyväksyntä pysyy portinvartijana.** Hyväksytty ehdotus siirtyy _Approved Offers_ -taulukkoon nimellä ja päivällä. Hylätty jää `offer-proposals.md`:hen perusteluineen, ettei sitä ehdoteta uudelleen.
6. **Tarjoustesti on oma testityyppinsä.** Tarjousta voi testata kokonaisena (uusi tarjous vs nykyinen) tai osana (sama tarjous, eri riskin poisto / aikalupaus). Muut komponentit pidetään vakiona.

### Alternatives Considered

- **Tarjousten kehitys osana creative-strategya:** hylätty, koska strategia on jo laaja ja tarjousten kehitys vaatii asiakkaan hyväksynnän ennen strategiaa.
- **Hyväksymättömät tarjoukset suoraan testiin:** hylätty; asiakas ei voi lunastaa tarjousta, jota se ei ole luvannut.

### Open Questions (if any)

1. **Ratkaistu 2026-10-26:** ajetaan, kun hyväksyttyjä tarjouksia on alle 3, kun Phase 0 suosittelee tarjoustestiä, tai pyynnöstä.
2. **Ratkaistu 2026-10-26:** ehdotukset asiakkaan mainoslokin välilehdelle "Tarjousehdotukset"; `offer-proposals.md` pysyy lähteenä.

---

## Step-by-Step Tasks

### Step 1: Template-tiedostot

**Actions:**

- Luo `_template/context/offer-proposals.md`: taulukko (ID, ehdotus, osat, mitä vaatii asiakkaalta, vastaa vastaväitteeseen, näyttö, ehdotettu testi, tila, päivä, asiakkaan kommentti).
- Lisää `_template/context/offer-brief.md`:n _Approved Offers_ -taulukkoon sarake "Osat".

**Files affected:** `_template/context/offer-proposals.md`, `_template/context/offer-brief.md`

### Step 2: Skilli `offer-development`

**Actions:**

- Kirjoita skilli: lähteiden luku, asiakkaan kyvyn kartoitus (puuttuvat tiedot kysytään), 6–10 ehdotusta neljän vivun ja osien avulla, karsinta (lunastettavuus, kielletyt väitteet, kuluttajansuojan hinta- ja säästöväitteet), arvio jokaiselle, asiakkaalle esitettävä muoto, hyväksyttyjen siirto offer briefiin.

**Files affected:** `~/.claude/skills/offer-development/SKILL.md`

### Step 3: Kytkennät mainosprosessiin

**Actions:**

- `create-new-ads`: Phase 1.5 (ehdot, odottaa asiakkaan hyväksyntää; jos hyväksyntää ei vielä ole, kierros jatkuu hyväksytyillä tarjouksilla).
- `competitor-analysis`: tarjousideat → `offer-proposals.md`.
- `creative-strategy`: tarjouksen osa testattavana komponenttina (`Tests: Offer component`), tarjoustestin pidä-vakiona-sääntö.
- `ads-analytics`: tarjousten ja osien tulokset, ehdotus seuraavasta tarjouskokeilusta.

**Files affected:** neljä skilliä

### Step 4: Onboard ja dokumentaatio

**Actions:**

- `/onboard` kierros 3: kysy myös asiakkaan halukkuus takuisiin, aikalupauksiin ja bonuksiin sekä kapasiteetti.
- README, CLAUDE.md:t.
- Kerro käyttäjälle, että Lämpösaaga tarvitsee `offer-proposals.md`:n ja _Osat_-sarakkeen.

**Files affected:** `~/.claude/commands/onboard.md`, `README.md`, `CLAUDE.md`, `_template/CLAUDE.md`

---

## Connections & Dependencies

### Files That Reference This Area

- `offer-brief.md` (kaikki mainosvaiheet), `static-ads-strategy` Principle 1, `ad-library` `OFF`-kortit

### Updates Needed for Consistency

- _Approved Offers_ -sarakkeet samat templatessa, skilleissä ja asiakkaissa.

### Impact on Existing Workflows

- Uusi valinnainen vaihe; ilman sitä prosessi toimii kuten nyt.
- Asiakkaan kanssa syntyy uusi hyväksyntäkierros tarjouksille.

---

## Validation Checklist

- [ ] Skilli tuottaa ehdotukset, jotka perustuvat asiakkaan kykyyn ja joilla on perustelut
- [ ] Hyväksytty ehdotus siirtyy offer briefiin nimellä ja päivällä
- [ ] Hylättyä ehdotusta ei ehdoteta uudelleen
- [ ] Tarjoustesti pitää muut komponentit vakiona

---

## Success Criteria

1. Jokaisella kierroksella, jolla tarjouksia on vähän, asiakkaalle syntyy perustellut tarjousehdotukset.
2. Tarjoukset ja niiden osat ovat testattavia komponentteja, ja tulokset kirjautuvat `learnings.md`:hen.

---

## Notes

- Lämpösaagalla neljä tarjousta odottaa vahvistusta; tarjousten kehitys kannattaa kokeilla ensin siellä.
