# Kulmamalli: yksi pääkulma per mainos, kulmatyypit, konsepti- ja komponenttitestit

**Tila:** toteutettu 2026-10-31 (skillit, templatet, own business). Lämpösaagan kansiot ja Sheetit migroidaan erikseen (ks. _Jäljellä_).

## Miksi

- "Kulma" sekoittui muihin komponentteihin: yleisön rajaus (`RajattuKohderyhma`) ja tarjouksen toisto (`MaksutonArvio`) olivat Angles-taulukossa kulmina.
- Kortti valitsi komponentit peräkkäin, mutta mikään ei tarkistanut, että yleisö, tietoisuustaso, motiivi, kulma, tarjous ja argumentti sopivat yhteen.
- Primary text noudatti aina rakennetta Problem → Agitate → Solution, myös riskin poistoon tai haluun perustuvissa mainoksissa.
- Ensimmäisen kierroksen voitto olisi merkinnyt jokaisen komponentin `Won`-tilaan, vaikka monimuuttujatesti ei kerro, mikä komponentti voiton teki.
- `AT`-rivit (omistajan prioriteetit) eivät erottuneet empiirisestä näytöstä.

## Mitä muuttui

| Alue | Muutos |
|---|---|
| Kulman määritelmä | Kulma on mainoksen **yksi hallitseva suostuttelun näkökulma**. Kortilla on yksi pääkulma; muut asiat ovat tukielementtejä. |
| Kulmatyyppi | Kiinteä luokittelu, sama kaikille asiakkaille: `Problem` · `Desire` · `Loss` · `RiskReversal` · `Comparison` · `Mechanism` · `Value` · `Credibility` · `Effort` · `BeliefShift` · `Timing` · `Control`. Itse kulmat ovat asiakaskohtaisia. |
| Angles-taulukko | Uudet sarakkeet `Angle type` ja `Core message` heti `Label`-sarakkeen jälkeen. |
| Duplikaatit | Yleisön call-out on creative copy -keino, tarjous kuuluu Offers-taulukkoon. Samantyyppiset kulmat, joilla on sama ydinviesti, yhdistetään. Vanha nimi jää _Label aliases_ -taulukkoon. |
| Kortin rakentaminen | Ensin valitaan kuusi komponenttia yhdessä: yleisö, tietoisuustaso, ostajan motiivi, pääkulma, hyväksytty tarjous ja tukeva argumentti. Sitten kirjoitetaan **coherence-lause** ja **viestihierarkia** (stop line → ydinviesti → tarjous → tuki → CTA). Vasta tämän jälkeen konsepti ja copy. |
| Primary text | Rakenne valitaan kulmatyypin mukaan (12 rakennetta). Problem → Agitate → Solution koskee vain `Problem`-kulmia. |
| Testit | `Test scope`: **Concept** (laaja, tulos koskee yhdistelmää) tai **Component** (yksi komponentti vaihtuu kontrolliin nähden). |
| Analytiikka | `Won`/`Lost` merkitään komponentille vain komponenttitestistä. Konseptitestissä komponentit saavat tilan `In winning combo` / `In losing combo`. Voittanut yhdistelmä ja näytön vahvuus (`Weak` / `Moderate` / `Strong`) kirjataan learnings.md:n _Combination results_ -taulukkoon. |
| AT | `AT` on omistajan prioriteetti, ei näyttöä. Poolissa noin joka neljäs kortti rakennetaan AT-rivin varaan. Kortin hypoteesi kertoo, ettei empiiristä näyttöä vielä ole. AT-rivin esimerkkilause on luonnos, ei hyväksytty väite. |
| Väitteet | Valintatarkistus varoittaa väitteestä, jota mikään `context/`-tiedosto ei tue. Kulma ei saa tuoda mukaan hyväksymätöntä tarjousta. |
| Valintasääntö | Konseptitestissä saman kulmatyypin kulmat lasketaan samaksi kulmaksi. |

## Muokatut tiedostot

**Skillit (`~/.claude/skills/`)**
- `creative-strategy/SKILL.md`: kulman määritelmä, kulmatyyppitaulukko, "mikä ei ole kulma", Allowed values (Angle type, Core message, Supporting elements, Test scope, buyer motivation), konsepti- ja komponenttitestit, AT-sääntö, valintasääntö, korttiketju ja coherence, korttipohja, kulmatyypin mukaiset primary text -rakenteet, Test Plan ja yleiskatsaustaulukko, Ad Inspiration A:R
- `ads-analytics/SKILL.md`: sarakkeet luetaan otsakkeen nimellä, vanhojen rivien test scope päätellään, näytön vahvuus, Combination results, statussäännöt (komponentti vs. konsepti), aliakset, raportin sarakkeet ja tulkinta
- `creative-generation/SKILL.md`: Creative Generations R–T, state-tiedoston kentät, vanhojen otsakkeiden täydennys
- `create-new-ads/SKILL.md`: Brief Y–AC, vanhojen otsakkeiden täydennys, Phase 2.5 -taulukko (kulma + tyyppi), ketju korttitekstissä, valintatarkistus (kulmatyyppi, tukematon väite)
- `competitor-analysis/SKILL.md`: kulma + tyyppi analyysissa, Ad Inspiration R (Angle Type), vanhojen otsakkeiden täydennys, ideoiden kulma, Angles-sarakkeet, Label aliases, AT-lähde ja uudet tilat, vanhan Angles-taulukon migraatio
- `customer-research/SKILL.md`: Angles-sarakkeet ja tutkimuksen kulmamahdollisuudet (tyyppi + ydinviesti)

**Hub (`Claude ads/`)**
- `_template/context/audience-hypotheses.md`: AT-lähde, tilat, Angles-sarakkeet ja ohje, Label aliases -taulukko
- `_template/context/learnings.md`: Combination results; What works koskee vain komponenttitestejä
- `README.md`: Sheet-skeemat (A–T, A–AC, A–R), hypoteesitiedoston kuvaus
- `plans/2026-10-31-kulmamalli.md`: tämä tiedosto

**Own business**
- `context/audience-hypotheses.md`: AT-määritelmä, tilat, AT-yleisöjen nimet nimilappumuotoon, Angles-taulukko uusilla sarakkeilla (17 riviä), duplikaattien yhdistäminen, Call out yhdistetty, testi #7 päivitetty, Retired + Label aliases
- `context/learnings.md`: Combination results
- `outputs/generated-assets/creative-brief-current.md`: kulmatyyppi, ydinviesti ja test scope jokaiselle kortille; #7 ja #16 nimetty uudelleen; #1 ja #15 validoitu; uusi kortti #20; suositus #1, #15, #20
- Sheetit: Brief A1:AC21 kirjoitettu uudelleen; Creative Generations R–T- ja Ad Inspiration R -otsakkeet lisätty; Driven brief-kopio päivitetty

## Migraatiokartta

**Nimilaput**

| Vanha | Uusi | Tyyppi | Miksi |
|---|---|---|---|
| `RajattuKohderyhma` (kulma) | creative copy `Call-out: rajaus otsikossa`; kortin kulma on sen oma | angle → copy | Yleisön call-out on copy-keino |
| `RiippuvuusSuosituksista` | `PuskaradioEiSkaalaudu` | angle | Sama tyyppi ja ydinviesti |
| `Call out` (copy) | `Call-out: rajaus otsikossa` | copy | Duplikaatti |
| `Lisää töitä tarvitseva` ym. AT-yleisöt | `LisaaToitaTarvitseva`, `KasvuhaluinenYrittaja`, `MainontaaHarkitseva`, `KilpailijoilleHaviavat` | audience | Nimilappumuoto |
| `MaksutonArvio` | sama nimi, uusi määritelmä (RiskReversal: "tiedät ennen kuin sitoudut") | angle | Oli pelkkä tarjouksen toisto |

**Creative names (brief, ei vielä Sheetissä tai Metassa)**

| Vanha | Uusi |
|---|---|
| `EiTulostaEiLaskua-RajattuKohderyhma-A` | `EiTulostaEiLaskua-RiskiOnMinun-A` |
| `MaksutonKartoitus-RajattuKohderyhma-A` | `MaksutonKartoitus-MaksutonArvio-B` |

**Sarakkeet:** kaikki uudet sarakkeet on lisätty olemassa olevien perään. Mitään ei siirretty eikä nimetty uudelleen, joten vanhat rivit ja kirjainviittaukset pysyvät ennallaan. Tyhjä uusi solu vanhalla rivillä tarkoittaa "ei kirjattu silloin". `ads-analytics` päättelee vanhan rivin test scopen `Tests`-sarakkeesta ja kulmatyypin Angles-taulukosta.

## Validointi: kolme esimerkkimainosta

Kortit ovat briefissä (#1, #15, #20) ja muodostavat yhdessä valintasäännön täyttävän suosituksen.

### 1. Riskin poisto: #1 `EnsimmainenKuukausiIlmaiseksi-RiskiOnMinun-A`

| Komponentti | Valinta |
|---|---|
| Yleisö × tietoisuus | PettynytToimistoon × Solution aware |
| Ostajan motiivi | Problem: RahatHukkaan |
| Pääkulma (tyyppi) | RiskiOnMinun (`RiskReversal`), ydinviesti: "Rahallisen riskin kantaa tekijä, ei yrittäjä." |
| Tarjous | EnsimmainenKuukausiIlmaiseksi (Approved) |
| Argumentti | Guarantee: 0 € palkkio ensimmäiseltä kuulta, lopetus milloin vain |
| Tuki | UusiJaRehellinen vain "miksi voin" -kohdassa; USP ilmoitus jokaisesta liidistä |
| Copy-keino | Direct offer (hinnoittelukortti) |

**Viestihierarkia:** "1. kuukausi: 0 € palkkiota" (stop line ja tarjous samassa) → riski on tekijän (lista ja "Täällä se on toisin päin") → tuki (ilmoitus, budjettirivi) → CTA.

**Mitä validointi muutti:** primary text oli kirjoitettu Problem-rakenteeseen (Opener → Problem → Agitate → Solution). Se kirjoitettiin RiskReversal-rakenteeseen: riski, jonka he yleensä kantavat → kuka kantaa sen täällä → miksi voin → entä jos ei toimi → CTA.

**Mitä testi voi osoittaa:** konseptitestinä se osoittaa, toimiiko tämä yhdistelmä toimistoon pettyneelle. Se ei kerro, oliko syy tarjous, kulma vai hinnoittelukortti. Jos kortti voittaa, seuraava komponenttitesti pitää tarjouksen ja vaihtaa yhden osan, esimerkiksi copy-keinon "Kuka maksaa, jos mainonta ei toimi?" (Question).

### 2. Ongelma: #15 `MaksutonKartoitus-PuskaradioEiSkaalaudu-A`

| Komponentti | Valinta |
|---|---|
| Yleisö × tietoisuus | PuskaradionVarassa × Problem aware |
| Ostajan motiivi | Problem: HidasPuskaradio |
| Pääkulma (tyyppi) | PuskaradioEiSkaalaudu (`Problem`), ydinviesti: "Suosittelut ovat hyviä, mutta niiden tahtia et päätä itse." |
| Tarjous | MaksutonKartoitus (Approved) |
| Argumentti | Mechanism: sama ihminen tekee mainokset ja vastaa puhelimeen, ei myyjiä |
| Tuki | USP:t omat työkuvat ja yksi tekijä |
| Copy-keino | Customer's words |

**Viestihierarkia:** "Vie aikaa, että sana alkaa kiiriä." → "tahtia et päätä itse" → "Selvitetään 20 minuutissa … Maksutta." → 📸 👤 ja "Puhelu ei velvoita mihinkään" → CTA.

**Mitä validointi muutti:** coherence-lause ei toiminut. Vastaväite oli "ei tarvetta", mutta argumentti (yksi tekijä, ei myyjiä) vastaa eri pelkoon. Vastaväitteeksi vaihdettiin "kartoitus on vain myyntipuhelu", johon argumentti vastaa. "Ei tarvetta" -vastaväitteeseen vastaa jo kulma itse. Primary text oli jo Problem-rakenteessa.

**Mitä testi voi osoittaa:** saako ongelmalähtöinen viesti ja matalan kynnyksen tarjous liikkeelle ison joukon, jolla ei ole aiempaa mainontaa. Tulos koskee yhdistelmää. Jos se voittaa, seuraava komponenttitesti on tarjous: sama kulma EnsimmainenKuukausiIlmaiseksi-tarjouksella, jolloin nähdään, kantoiko voiton kartoitus vai kulma.

### 3. Halu: #20 `EiTulostaEiLaskua-TasainenKalenteri-A` (uusi)

| Komponentti | Valinta |
|---|---|
| Yleisö × tietoisuus | LisaaToitaTarvitseva (AT) × Problem aware |
| Ostajan motiivi | Desire: TasainenTarjouspyyntovirta (AT) |
| Pääkulma (tyyppi) | New: TasainenKalenteri (`Desire`), ydinviesti: "Tasainen tarjouspyyntövirta on tavoite, jonka voi sopia etukäteen." |
| Tarjous | EiTulostaEiLaskua (Approved): sovittu liiditavoite, palkkiota ei laskuteta, jos se ei täyty |
| Argumentti | Guarantee: sama ehto |
| Tuki | Problem: HidasPuskaradio vain "mikä on välissä" -kohdassa; USP ilmoitus jokaisesta liidistä |
| Copy-keino | Question |

**Viestihierarkia:** "Miltä näyttäisi kalenteri, johon tulee tarjouspyyntöjä tasaisesti?" → tasaisen virran voi sopia tavoitteeksi → "Sovitaan kuukauden liiditavoite. Jos se ei täyty, et maksa palkkiota." → puskaradion sattumanvaraisuus ja 🔔 → CTA.

**Miksi juuri tämä tarjous:** coherence-lause yhdistää halun tarjouksen ytimeen, koska tavoite on juuri se tasainen virta. Ensimmäisen kuukauden tarjous ei olisi yhtä suora seuraava askel.

**Väitteet:** kaikki väitteet ovat offer briefistä tai hyväksytyistä USP:istä: omat työkuvat, tarjouspyyntö suoraan Facebookissa (pikalomake on konversiomekanismi), ilmoitus jokaisesta liidistä ja takuu. Kuvaan ei tule kalenterigrafiikkaa keksittyine merkintöineen.

**AT:** hypoteesi sanoo suoraan, ettei omistajan riveillä ole vielä empiiristä näyttöä.

**Mitä testi voi osoittaa:** toimiiko halulähtöinen viesti Problem aware -yleisöllä tämän tarjouksen kanssa. Voitto ei todista, että halu olisi parempi kuin kipu. Sen selvittäisi komponenttitesti: sama tarjous, yleisö ja tietoisuustaso, mutta `Problem`-kulma (esim. EpatasainenAsiakasvirta).

**Valintasääntö (#1, #15, #20):** kolme eri tarjousta ja kolme eri kulmatyyppiä (`RiskReversal`, `Problem`, `Desire`). #15 ja #20 jakavat tietoisuustason, mutta eroavat kolmessa muussa. Muut parit eroavat kaikessa neljässä. Entinen suositus #1, #7, #15 ei enää täytä sääntöä, koska #7:n kulma on migraation jälkeen RiskiOnMinun.

## Jäljellä

- **Olemassa olevat asiakaskansiot:** Angles-taulukoista puuttuvat `Angle type` ja `Core message`, ja Label aliases -taulukko puuttuu. Ne lisätään asiakkaan omassa sessiossa. `competitor-analysis` tekee tämän automaattisesti ennen kuin se kirjoittaa uusia rivejä. Sheeteissä skillit lisäävät puuttuvat otsakkeet seuraavalla kirjoituskerralla. Lämpösaagan Creative Generations -välilehdeltä puuttuu jo `From Hypotheses`, ja sen 18 historiariviä jäävät ennalleen.
- **Ad Inspiration (own business):** vanhojen rivien `Angle Type` on tyhjä. Se voidaan täyttää seuraavan Phase 1:n yhteydessä.
- **Briefin kortit #2–#14 ja #16–#19:** niillä on kulmatyyppi, ydinviesti ja test scope, mutta ei coherence-lausetta eikä viestihierarkiaa. Nämä täydennetään, kun kortti valitaan testiin. Primary text -rakenne tarkistetaan samalla kulmatyypin mukaan.
