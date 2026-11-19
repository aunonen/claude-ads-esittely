# Plan: Agentuurin mainoskirjasto — kuviot, referenssit ja tyyli näytön pohjalta

**Created:** 2026-10-26
**Status:** In progress — steps 1–8 implemented 2026-10-26; step 9 (pilot) and step 10 (validation after pilot, commit) pending
**Request:** Agentuuritason mainoskirjasto, joka kerää korkean arvon palveluyritysten mainoksia Metan mainoskirjastosta ja muuttaa ne luotettavasti kuvioiksi (tarjoukset, kulmat, creative conceptit, creative copyn keinot, formaatit), referensseiksi ja tyylikirjastoksi niin, ettei huonoja mainoksia valita.

---

## Overview

### What This Plan Accomplishes

Hubiin rakennetaan yhteinen mainoskirjasto (`library/`), johon pääsee vain selvästi toimivia julkisia mainoksia ankaran pääsyehdon kautta. Kirjastosta kootaan **kuviokortit** (mikä toimii, miksi, milloin, millä näytöllä), kuhunkin 2–3 **referenssiä** ja konkreettinen **tyylikirjasto** (kieli ja visuaalisuus). Jokaisella kuviolla on **luottamustaso**, ja tason nosto vaatii käyttäjän hyväksynnän. Asiakkaiden analyysi ja strategia käyttävät kirjastoa tason 3 näyttönä ja ideoiden valikkona.

### Why This Matters

Yksittäisen asiakkaan aineisto on liian pieni luotettaviin kuvioihin (yhdistelmäanalyysi vaatii vähintään kaksi mainostajaa, ja paikallisia mainostajia on vähän). Kirjasto antaa agentuurille kertyvän, näyttöön perustuvan osaamisen siitä, minkä tyyppiset mainokset korkean arvon palveluissa toimivat ja millä tyylillä. Se nopeuttaa uusien asiakkaiden aloitusta ja tekee ideoiden hypoteeseista perusteltuja.

---

## Current State

### Relevant Existing Structure

- `~/.claude/skills/ad-inspiration-collection/SKILL.md`: asiakaskohtainen keruu (hakusanakorit, selainluku, EU-tavoittavuus, näyttöpisteet, tavoite, pysäytetyt mainokset, `Dropped`, versioparit, sivutiedostot, näyttöloki)
- `~/.claude/skills/competitor-analysis/SKILL.md`: kuvaileva analyysi, komponenttikartta (mainostajamäärät), yhdistelmäanalyysi (signaalipisteet, tuomiot), New to Us, Intelligence Report
- `~/.claude/skills/creative-strategy/SKILL.md`: sallitut arvot, Creative Copy -osio (ensimmäisen rivin keinot), kortit hypoteeseineen
- `~/.claude/skills/ads-analytics/SKILL.md`: tulosluokat, `learnings.md`:n päivitys
- `~/.claude/skills/ad-design/design-guide.md`: layoutit ja creative concept -pohjat
- Hubin `CLAUDE.md`: säännöt, mm. **No cross-client bleed** ja **One client per session**
- Hubin `.gitignore`: kuvat ja salaisuudet pois gitistä

### Gaps or Problems Being Addressed

- Kuvioita ja referenssejä ei kerry mihinkään asiakkaiden yli; jokainen asiakas aloittaa tyhjästä.
- Yksittäisen asiakkaan aineistossa harva yhdistelmä täyttää kahden mainostajan ehdon.
- Ei ole menetelmää, joka erottaa "näyttää hyvältä" ja "todennäköisesti toimii", eikä luottamustasoja.
- Tyyli (kieli, visuaalisuus) on kuvattu vain yleisinä sääntöinä, ei näyttöön perustuvina esimerkkeinä.

---

## Proposed Changes

### Summary of Changes

- Uusi hubin kansio `library/` (mainokset, näyttöloki, kuviokortit, tyylikirjasto, indeksi)
- Uusi skilli `ad-library` (keruu hub-tilassa, uusintatarkistus, synteesi, tason nostoehdotukset)
- Kuviokortin ja tyylimerkinnän pohjat
- `competitor-analysis` ja `creative-strategy` käyttämään kirjastoa; `ads-analytics` antamaan palautetta (avoin kysymys 1)
- Hubin `CLAUDE.md`, README ja `.gitignore` päivitetään; uusi sääntö kirjaston sisällöstä
- Pilotti yhdellä alalla ennen laajentamista

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `library/README.md` | Mitä kirjasto on, mitä sinne saa ja ei saa laittaa, rakenne, luottamustasot |
| `library/_collection-log.md` | Keruukerrat: päivä, alat, hakusanat koreittain, mainostajat per kori, rajoitukset |
| `library/_evidence-log.md` | Jokainen kirjaston mainos: ala, ostotilanne, pisteet, luokka, tavoite, tila (Candidate/Confirmed/Stopped/Dropped), tarkistuspäivät ja tavoittavuuden kehitys; versioparit omana osionaan |
| `library/ads/<ala>/<tiedosto>.jpg` + `.txt` | Mainoskuva (git-ignorattu) ja sivutiedosto (seurattu) |
| `library/patterns.md` | Indeksi: kaikki kuviokortit taulukkona (tunniste, tyyppi, nimi, luottamustaso, ostotilanteet, viimeksi nähty) |
| `library/patterns/<ID>-<slug>.md` | Yksi kuviokortti per kuvio |
| `library/style/style-guide.md` | Tyylikirjasto: kieli (S-LANG-*) ja visuaalisuus (S-VIS-*) |
| `library/_templates/pattern-card.md` | Kuviokortin pohja |
| `library/_templates/style-entry.md` | Tyylimerkinnän pohja |
| `~/.claude/skills/ad-library/SKILL.md` | Kirjaston skilli: collect, recheck, synthesize, report |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `~/.claude/skills/competitor-analysis/SKILL.md` | Lukee `../../library/patterns.md` ja kortit ostotilanteen mukaan suodatettuna tason 3 näyttönä; komponenttikartassa ja yhdistelmäanalyysissä sarake "Kirjasto"; ideoiden hypoteesit viittaavat kuvion tunnisteeseen |
| `~/.claude/skills/creative-strategy/SKILL.md` | Kuviovalikko luottamustason mukaan; kortin uusi kenttä `Library patterns`; Tuettu-tason tyylimerkinnät täydentävät Creative Copy -osiota |
| `~/.claude/skills/ads-analytics/SKILL.md` | (Avoimen kysymyksen 1 mukaan) ehdottaa kuvioiden luottamustason päivitystä testitulosten perusteella ilman asiakasdataa |
| `~/.claude/skills/ad-design/design-guide.md` | Viittaus Tuettu-tason visuaalisiin tyylimerkintöihin (S-VIS-*) valinnaisena ohjeena |
| `~/.claude/skills/ad-inspiration-collection/SKILL.md` | Viittaus kirjastoon: tason 3 mainokset haetaan ensin kirjastosta; kirjastokelpoiset löydöt voi ehdottaa kirjastoon |
| `CLAUDE.md` (hub) | Kansiorakenteeseen `library/`; uusi sääntö kirjaston sisällöstä; skilli listaan |
| `README.md` (hub) | Kirjaston käyttö: keruu, uusintatarkistus, synteesi, hyväksyntä |
| `.gitignore` (hub) | `library/ads/**/*.jpg`, `*.png`, `*.webp` pois gitistä, sivutiedostot mukaan |
| `_template/CLAUDE.md`, `clients/<asiakas>/CLAUDE.md` | Maininta, että analyysi käyttää agentuurin kirjastoa tason 3 näyttönä |

### Files to Delete (if any)

Ei poistettavia.

---

## Design Decisions

### Key Decisions Made

1. **Näyttö ennen makua.** Mainoksen näyttöpisteet kirjataan ennen kuvan arviointia. Kirjastoon pääsee vain pääsyehdon kautta, ei siksi, että mainos näyttää hyvältä.

2. **Pääsyehto (tiukempi kuin asiakaskeruussa):**
   - tavoite liidi tai myynti (sisältö- ja tunnettuusmainokset vain tyylimerkintöjen esimerkeiksi, merkittynä)
   - luokka A **ja** vähintään kaksi toisistaan riippumatonta signaalia: käyttöikä vähintään 60 pv sekä vähintään yksi näistä: monta versiota, selvästi suuri EU-tavoittavuus, idea palaa uudella kuvalla
   - testaava mainostaja (kymmeniä mainoksia, uusia versioita säännöllisesti); suurten brändien tunnettuusmainonta merkitään ja jätetään kuvioiden ulkopuolelle
   - tila **Candidate** pääsyhetkellä; **Confirmed** vasta, kun mainos on uusintatarkistuksessa (aikaisintaan 30 pv myöhemmin) yhä käynnissä ja tavoittavuus kasvanut
   - pysäytetyt (`Dropped`) mainokset kirjataan vastanäyttönä tekstiriveinä, versioparit erikseen

3. **Kuvio ≠ referenssi.** Kuvio on abstraktio ja sen mekanismi. Referenssi on kuvion paras esimerkki, eikä irrallisia "hienoja mainoksia" tallenneta.

4. **Kuviokortti** (`library/patterns/<ID>-<slug>.md`), tunnisteet tyypin mukaan: `OFF` tarjous, `ANG` kulma, `CON` creative concept, `CPY` creative copyn keino, `FMT` formaatti/layout. Kortin osiot:
   - nimi ja tyyppi, tunniste (esim. `CPY-004`)
   - **mekanismi**: miksi todennäköisesti toimii (toistuminen ei riitä perusteluksi)
   - milloin sopii: tietoisuustaso, ostotilanne (hintataso, päätöksen pituus, liidimalli), tarjoustyyppi
   - näyttö: mainostajat, alat, luokat, käyttöiät, tavoittavuuden kehitys, versioparit
   - vastanäyttö: pudottajat ja tilanteet
   - referenssit (2–3, eri mainostajilta, Confirmed-tilasta)
   - suomenkielinen sovellusohje: rakenne, ei sanamuotoja
   - luottamustaso ja muutoshistoria (päivä, taso, kuka hyväksyi)

5. **Luottamustasot:**

   | Taso | Vaatimus | Käyttö skilleissä |
   |---|---|---|
   | **Candidate** | Vähintään 2 mainostajaa pääsyehdon läpäisseillä mainoksilla | Vain nimettynä testinä |
   | **Supported** | Vähintään 3 mainostajaa, mieluiten 2+ alaa, vähintään 2 Confirmed-mainosta, pudottajia vähemmän kuin käyttäjiä | Hypoteesin perusteena |
   | **Proven** | Supported + voittanut agentuurin oman testin (avoin kysymys 1) | Oletusvalinta |
   | **Fading** | Ei nähty 6 kk:een tai pudottajien enemmistö | Merkitään, ei suositella |

   Tason nosto ja Fading-merkintä tapahtuvat vain käyttäjän hyväksynnällä: skilli ehdottaa perusteluineen, käyttäjä päättää.

6. **Tyylikirjasto erillään sisällöstä.** Merkinnät `S-LANG-*` (lauseenpituus, luvut, puhuttelu, sävy) ja `S-VIS-*` (kuvatyyppi, tekstin sijainti, kontrasti, kehystys) kirjataan konkreettisina ja mitattavina, vain Confirmed-mainoksista ja vähintään kahdelta mainostajalta. Samat luottamustasot.

7. **Kirjasto sisältää vain julkisia mainoksia.** Asiakkaiden mainoksia, lukuja, väitteitä tai materiaaleja ei koskaan tallenneta kirjastoon (No cross-client bleed).

8. **Markdown on totuuden lähde.** Kirjasto on tiedostoina hubissa, jotta skillit lukevat sen suoraan ja muutokset näkyvät gitissä. Google Sheet on valinnainen peilikopio selailua varten (avoin kysymys 2).

9. **Kirjastotyö tehdään hub-istunnossa.** Asiakasistunnon skillit lukevat kirjastoa polulla `../../library/`, mutta eivät kirjoita sinne.

10. **Painotus asiakkaan analyysissä:** omat tulokset (`learnings.md`) > saman markkinan näyttö (asiakkaan keruu) > kirjasto. Kirjaston kuvio ei voi yksin todistaa ideaa asiakkaan markkinassa.

### Alternatives Considered

- **Kaikki mainokset kirjastoon, valinta analyysivaiheessa:** hylätty, koska heikot mainokset päätyvät helposti referensseiksi ja kirjasto paisuu.
- **Kuviot suoraan skilleihin (esim. static-ads-strategy):** hylätty, koska kuviot muuttuvat ja tarvitsevat näyttö- ja tasohistorian; skillit pysyvät menetelminä.
- **Pelkkä Google Sheet:** hylätty totuuden lähteeksi, koska skillit lukevat tiedostoja luotettavammin ja git näyttää muutokset.
- **Automaattinen tason nosto:** hylätty, koska käyttäjän hyväksyntä on toinen suoja virheellisiä kuvioita vastaan.

### Open Questions (if any)

1. ~~Proven-taso ja asiakkaiden erottelu~~ **Ratkaistu 2026-10-26:** saa. Kirjastoon kirjataan vain kuvion tunniste, voitti/hävisi ja päivä, ei asiakastietoja (ei asiakkaan nimeä, lukuja, väitteitä eikä materiaaleja). Proven-taso on mukana. Hubin CLAUDE.md:n No cross-client bleed -sääntöön lisätään tämä nimetty poikkeus.
2. **Ratkaistu 2026-10-26:** ei Google Sheet -peiliä, markdown-tiedostot riittävät.
3. **Ratkaistu 2026-10-26:** pilotti kodin energia- ja lämmitysremonteista ja 1–2 samaa ostotilannetta jakavasta alasta; muut alat myöhemmin.
4. **Ratkaistu 2026-10-26:** uusintatarkistus käsin kuukausittain hub-istunnossa ("tarkista kirjasto"), ei ajastettua tehtävää.
5. **Ratkaistu 2026-10-26:** kuviokortit ja tyylikirjasto suomeksi; skillit pysyvät englanniksi.

Kaikki avoimet kysymykset on ratkaistu, ja suunnitelma on valmis toteutettavaksi.

---

## Step-by-Step Tasks

### Step 1: Kirjaston rakenne

Luo `library/`-kansio ja perustiedostot.

**Actions:**

- Luo `library/README.md`: tarkoitus, sisältösääntö (vain julkiset mainokset), rakenne, pääsyehto tiivistettynä, luottamustasot, miten kirjastoa käytetään asiakastyössä.
- Luo `library/_collection-log.md` ja `library/_evidence-log.md` otsikkoineen. Näyttölokin sarakkeet: Tiedosto, Mainostaja, Ala, Ostotilanne, Library ID, Löytyi (kori: sana), Alkoi, Versiot, EU-tavoittavuus (päivä → päivä), Kohdennus, Pisteet, Luokka, Tavoite, Tila, Tarkistettu, Havainto. Alle osiot Versioparit ja Pudotetut (tekstirivit).
- Luo `library/patterns.md` (tyhjä indeksitaulukko), `library/patterns/`, `library/style/style-guide.md` (otsikot S-LANG ja S-VIS), `library/ads/`.
- Lisää hubin `.gitignore`:en `library/ads/**/*.jpg`, `library/ads/**/*.jpeg`, `library/ads/**/*.png`, `library/ads/**/*.webp`.

**Files affected:**

- `library/**`
- `.gitignore`

---

### Step 2: Kortti- ja tyylipohjat

**Actions:**

- Luo `library/_templates/pattern-card.md` Design Decision 4:n osioilla, esimerkkitäytöllä hakasulkeissa.
- Luo `library/_templates/style-entry.md`: tunniste, kuvaus mitattavasti, milloin sopii, näyttö (mainostajat, Confirmed-mainokset), vastaesimerkit, referenssit, luottamustaso ja historia.

**Files affected:**

- `library/_templates/pattern-card.md`
- `library/_templates/style-entry.md`

---

### Step 3: Skilli `ad-library`

Uusi skilli hub-istuntoon, neljä tilaa.

**Actions:**

- **collect:** alat ja ostotilanteet käyttäjältä; hakusanat neljässä korissa kuten `ad-inspiration-collection` (viittaus, ei kopiota); selainluku (2a–2d); pisteytys ja tavoite; **kirjaston pääsyehto** (Design Decision 2); tallennus `library/ads/<ala>/` + sivutiedosto; näyttöloki tilaan Candidate; pudotetut tekstiriveinä; versioparit.
- **recheck:** jokainen Candidate- ja Confirmed-mainos uudelleen (mainostajan sivu tekstinä + lisätiedot): käynnissä ja tavoittavuus kasvanut → Confirmed; pysähtynyt → Stopped ja luokka alas; kirjaa tavoittavuuden kehitys.
- **synthesize:** kuviot kuvailevista riveistä kuten `competitor-analysis`:n komponenttikartta ja yhdistelmäanalyysi (mainostajamäärät, vastanäyttö, signaalipisteet); uudet kortit Candidate-tasolla; olemassa olevien korttien näytön päivitys; tyylimerkinnät; **tason nosto- ja Fading-ehdotukset perusteluineen**, joita ei tallenneta ennen käyttäjän hyväksyntää; referenssien valinta (2–3, Confirmed, eri mainostajat, korkein pistemäärä).
- **report:** muutokset, ehdotukset hyväksyttäväksi, kirjaston tila (mainoksia, kuvioita tasoittain, alat).
- Säännöt: vain julkiset mainokset; ei koskaan asiakkaan dataa; ajetaan hub-istunnossa.

**Files affected:**

- `~/.claude/skills/ad-library/SKILL.md`

---

### Step 4: `competitor-analysis` käyttämään kirjastoa

**Actions:**

- Starting Point -osioon: lue `../../library/patterns.md` ja asiakkaan ostotilanteeseen sopivat kortit (Candidate, Supported, Proven; ei Fading).
- Komponenttikarttaan ja yhdistelmäanalyysiin sarake **Kirjasto**: vastaava kuvio-ID ja taso. Kirjasto ei kasvata signaalipisteitä, vaan näkyy erikseen.
- Brand Ad Ideas: hypoteesi voi viitata kuvio-ID:hen; painotus Design Decision 10:n mukaan.
- Raporttiin rivi: mitkä kirjaston kuviot sopivat asiakkaalle mutta puuttuvat sen markkinasta (tyhjän tilan ehdokkaat).

**Files affected:**

- `~/.claude/skills/competitor-analysis/SKILL.md`

---

### Step 5: `creative-strategy` käyttämään kirjastoa

**Actions:**

- Step 1 -lähteisiin: kirjaston indeksi ja asiaankuuluvat kortit sekä tyylikirjasto.
- Korttiin uusi kenttä `Library patterns: [ID:t tai "none"]`.
- Kuviovalikko: Proven = oletusvaihtoehto, Supported = hypoteesin peruste, Candidate = vain nimettynä testinä.
- Creative Copy -osioon: Supported- ja Proven-tason `S-LANG`-merkinnät täydentävät laatukriteerejä; ristiriidassa skillin oma osio voittaa.

**Files affected:**

- `~/.claude/skills/creative-strategy/SKILL.md`

---

### Step 6: Palaute testituloksista (Proven-taso)

Käyttäjä hyväksyi 2026-10-26: kirjastoon saa kirjata vain kuvion tunnisteen, tuloksen (voitti/hävisi) ja päivän.

**Actions:**

- `ads-analytics`:iin vaihe: jos testattu mainos nojasi kirjaston kuvioon (kortin `Library patterns` -kenttä), raporttiin rivi "Kirjastopalaute: `<ID>` voitti/hävisi, `<päivä>`". Ei asiakkaan nimeä, lukuja, väitteitä eikä materiaaleja.
- Asiakasistunto ei kirjoita kirjastoon. `ad-library`:n synthesize-tila kokoaa palauterivit asiakkaiden raporteista hub-istunnossa ja ehdottaa niiden perusteella Proven-nostoa tai Fading-merkintää käyttäjän hyväksyttäväksi.
- Kuviokorttiin osio "Agentuurin testit": vain rivit muotoa `<päivä> · voitti/hävisi`.
- Hubin `CLAUDE.md`:n No cross-client bleed -sääntöön nimetty poikkeus: "the agency library may record a pattern ID with won/lost and a date from a client's test, nothing else".

**Files affected:**

- `~/.claude/skills/ads-analytics/SKILL.md`
- `~/.claude/skills/ad-library/SKILL.md`
- `library/_templates/pattern-card.md`
- `CLAUDE.md` (hub)

---

### Step 7: Design-oppaan ja keruuskillin viittaukset

**Actions:**

- `design-guide.md`: lyhyt kohta "Tyylikirjasto": Supported- ja Proven-tason `S-VIS`-merkinnät ovat valinnaisia ohjeita layoutin valintaan, authenticity rules voittavat.
- `ad-inspiration-collection`: Step 1:een, että tason 3 mainokset katsotaan ensin kirjastosta; Outputiin, että kirjaston pääsyehdon täyttävät löydöt voi ehdottaa kirjastoon hub-istunnossa.

**Files affected:**

- `~/.claude/skills/ad-design/design-guide.md`
- `~/.claude/skills/ad-inspiration-collection/SKILL.md`

---

### Step 8: Dokumentaatio ja säännöt

**Actions:**

- Hubin `CLAUDE.md`: `library/` kansiorakenteeseen; uusi sääntö "Library holds public ads only: never a client's ads, numbers, claims or assets"; `ad-library` skillilistaan.
- README: osio "Agentuurin mainoskirjasto" (miten kerätään, tarkistetaan, syntetisoidaan, hyväksytään).
- `_template/CLAUDE.md` ja `clients/<asiakas>/CLAUDE.md`: Phase 1 -riville maininta kirjastosta tason 3 näyttönä.

**Files affected:**

- `CLAUDE.md`, `README.md`, `_template/CLAUDE.md`, `clients/<asiakas>/CLAUDE.md`

---

### Step 9: Pilotti yhdellä alalla

**Actions:**

- Hub-istunnossa `ad-library collect`: "kodin energia- ja lämmitysremontit" + 1–2 samaa ostotilannetta jakavaa alaa, tavoite 10–15 testaavaa mainostajaa.
- `synthesize`: ensimmäiset kortit Candidate-tasolla, tyylimerkinnät.
- Käy tulokset läpi käyttäjän kanssa: ovatko kuviot uskottavia, onko joukossa mainoksia, joiden ei olisi pitänyt päästä läpi? Säädä pääsyehtoa tarvittaessa.
- 30 pv kuluttua `recheck` ja ensimmäiset tason nostoehdotukset.

**Files affected:**

- `library/**`

---

### Step 10: Validointi ja commit

**Actions:**

- Käy läpi Validation Checklist.
- Commitoi molemmat repot vasta käyttäjän pyynnöstä.

**Files affected:**

- kaikki yllä

---

## Connections & Dependencies

### Files That Reference This Area

- `competitor-analysis` (näyttöluokat, komponenttikartta, yhdistelmäanalyysi, ideat)
- `creative-strategy` (Creative Copy -osio, kortit, hypoteesit)
- `ads-analytics` (`learnings.md`, tulosluokat)
- `ad-inspiration-collection` (pisteytys, korit, selainluku: kirjaston skilli viittaa näihin)
- Hubin `CLAUDE.md` säännöt (cross-client bleed, one client per session)

### Updates Needed for Consistency

- Pisteytys, tavoitekategoriat ja korit pysyvät määriteltyinä vain `ad-inspiration-collection`:ssa; `ad-library` viittaa niihin.
- Kuvioiden tunnistelyhenteet (`OFF`, `ANG`, `CON`, `CPY`, `FMT`, `S-LANG`, `S-VIS`) samat kaikkialla.
- Luottamustasojen nimet samat README:ssä, skilleissä ja korttipohjassa.

### Impact on Existing Workflows

- Asiakasistunnon työnkulku ei muutu, mutta Phase 1 ja Phase 2 lukevat kirjastoa, jos se on olemassa. Ilman kirjastoa skillit toimivat kuten ennenkin.
- Kirjastotyö on oma hub-istuntonsa: keruu, uusintatarkistus ja synteesi.
- Agentuurin työhön tulee säännöllinen kirjaston tarkistus (rytmi avoin kysymys 4).

---

## Validation Checklist

- [ ] `library/`-rakenne ja pohjat olemassa, kuvat git-ignorattu ja sivutiedostot seurattu
- [ ] `ad-library`-skilli näkyy skillilistassa ja sen neljä tilaa on kuvattu
- [ ] Pääsyehto, luottamustasot ja tunnisteet ovat samat README:ssä, skillissä ja pohjissa
- [ ] `competitor-analysis` ja `creative-strategy` lukevat kirjaston polulla `../../library/` ja toimivat myös ilman sitä
- [ ] Kirjastoon ei kirjoiteta asiakasistunnosta; sääntö on hubin CLAUDE.md:ssä
- [ ] Pilotin jälkeen vähintään 10 testaavaa mainostajaa ja ensimmäiset Candidate-kortit referensseineen
- [ ] Käyttäjä on käynyt pilotin kortit läpi eikä kirjastoon ole päässyt mainoksia, jotka hän hylkäisi
- [ ] CLAUDE.md, README ja template päivitetty

---

## Success Criteria

The implementation is complete when:

1. Kirjastoon pääsee vain pääsyehdon läpäiseviä mainoksia, ja jokaisella on näyttörivi ja sivutiedosto.
2. Jokaisella kuviokortilla on mekanismi, näyttö, vastanäyttö, 2–3 referenssiä ja luottamustaso, jonka nostot on hyväksytty.
3. Asiakkaan Intelligence Report ja brief viittaavat kirjaston kuvioihin tunnisteella ja painottavat niitä oman markkinan näyttöä kevyemmin.
4. Pilotin kuvioista käyttäjä pitää valtaosaa uskottavina ilman merkittäviä vääriä positiivisia.

---

## Notes

- Kirjasto kannattaa pitää pienenä ja tiukkana: 10–15 testaavaa mainostajaa per ala riittää alkuun. Laatu ennen määrää.
- Myöhemmin: Ad Library API voi nopeuttaa uusintatarkistuksia (`ad-inspiration-collection`:n valinnainen osio).
- Kirjaston mainokset ovat kolmansien osapuolten materiaalia: vain sisäiseen analyysiin, ei koskaan käytetä sellaisenaan asiakkaan mainoksissa.
- Kuviokortteja voi myöhemmin käyttää myös myyntimateriaalina ("näin korkean arvon palveluiden mainokset toimivat"), kunhan referenssikuvia ei julkaista.
