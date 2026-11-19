# Offer Brief — {{BRAND_NAME}}

*Main audiences for this brief: suomalaiset palveluyrittäjät (liikevaihto ≥ 200 000 €, palvelun arvo mieluiten > 1 000 €), jotka haluavat lisää asiakkaita. Tarkentuu audience-hypotheses.md:ssä asiakastutkimuksen jälkeen.*

> 💡 This is the most important file for ad quality. Every offer, claim, USP, proof point and CTA used in an ad must come from here or from `business-info.md`. **The skills never invent claims.** If it isn't written down here, it won't appear in an ad. The sections marked **(used directly by the skills)** must be filled in before the first run.

> **30.10.2026:** tarjoukset hyväksytty; kärkenä EnsimmainenKuukausiIlmaiseksi. Vastaväitteet, USP:t ja CTA:t ovat luonnoksia, jotka käyttäjä arvioi.

---

## Approved Offers (used directly by the skills)

The offer is the most important component the ads test. Each row is one offer the client has agreed to, with a short **label** (PascalCase, ASCII only: ä→a, ö→o) that goes into the creative names and the Sheet, so keep a label once it is in use. An offer not in this table, or one whose last column doesn't yet name who approved it and when, is marked "needs client approval" and never goes into a live ad until it is approved here.

| Label | Exact offer (what the customer gets) | Components | Terms & conditions | Valid until | Approved by client |
|---|---|---|---|---|---|
| EnsimmainenKuukausiIlmaiseksi | "Ensimmäinen kuukausi ilman palkkiota: maksat vain mainosbudjetin." Jatkon hinta sovitaan asiakaskohtaisesti (ei näytetä mainoksissa eikä sivulla). | core: asiakashankinta Meta-mainoksilla · risk reversal: 0 € palkkio 1. kk, ei aloitusmaksua, lopetus milloin vain · scope: palveluyritykset | Mainosbudjetti maksetaan suoraan Metalle myös 1. kuukautena. Rajallinen määrä asiakkaita. | ongoing | Käyttäjä (agency), 30.10.2026. **Kärkitarjous mainonnassa.** |
| EiTulostaEiLaskua | "Sovitaan yhdessä liiditavoite. Jos se ei täyty, et maksa sen kuukauden palkkiota." | core: asiakashankinta Meta-mainoksilla · risk reversal: palkkio vain, jos tavoite täyttyy · scope: palveluyritykset | Tavoite (liidiä/kk) sovitaan asiakaskohtaisesti ennen aloitusta. Mainosbudjetti maksetaan Metalle aina. Ei aloitusmaksua, lopetus milloin vain. | ongoing | Käyttäjä (agency), 30.10.2026 |
| IlmainenKuukausiJaTakuu | Molemmat yhdessä: "Ensimmäinen kuukausi ilman palkkiota. Sen jälkeen maksat vain kuukausista, joissa sovittu liiditavoite täyttyy." | core · risk reversal: 0 € 1. kk + tulostakuu · scope | Kuten yllä. Monimutkainen mainokseen: käytä vain, jos sen voi sanoa yhdellä lauseella. | ongoing | Käyttäjä (agency), 30.10.2026 |
| MaksutonKartoitus | "Varaa maksuton 20 minuutin kartoitus: käydään läpi yrityksesi nykyinen asiakashankinta ja kerron, voisinko tuoda lisää tarjouspyyntöjä." | core: kartoituspuhelu · risk reversal: maksuton, ei sitoumuksia · time: 20 min · scope: palveluyritykset | Puhelu tai videopuhelu; ei velvoita mihinkään. Kartoitus on myös laskeutumissivun ja lomakkeen jatkoaskel. Voidaan yhdistää tarjoukseen EnsimmainenKuukausiIlmaiseksi. | ongoing | Käyttäjä (agency), 30.10.2026 |

**Components** name the parts of the offer, so a test can change one part and keep the rest: `core` (what is delivered), `risk reversal` (guarantee, fixed price, no obligation), `time` (how fast / until when), `bonus` (something extra), `scope` (who it's for, limits). New offers are developed with the `offer-development` skill and wait in `offer-proposals.md` until the client approves them.

## Approved USPs (used directly by the skills)

- 🤝 Jos sovittu liiditavoite ei täyty, kuukauden palkkiota ei laskuteta
- 🔓 Ei aloitusmaksua eikä sitoutumista: voit lopettaa milloin vain
- 👤 Yksi ihminen tekee kaiken: tarjous, mainokset ja kampanjat. Ei välikäsiä.
- 📸 Mainokset tehdään yrityksesi omista työkuvista, ei tekoälykuvia
- ♾️ Mainosten määrää ei rajata
- 🔔 Saat ilmoituksen jokaisesta liidistä
- 🎯 Tarjous hiotaan ennen mainoksia, koska tarjous ratkaisee eniten

## Approved CTA Sentences (used directly by the skills)

- Selvitä, voisinko tuoda yrityksellesi lisää tarjouspyyntöjä (pääasiallinen CTA, käyttäjä 30.10.2026)
- Soita heti (laskeutumissivulla soittolinkki)
- Jätä yhteystietosi, niin soitan sinulle
- Kysy, sopiiko tämä sinun yrityksellesi
- Katso, paljonko liidejä yrityksesi voisi saada
- Varaa lyhyt puhelu, ei sitoumuksia

## Social Proof Assets (used directly by the skills)

Ei yhtään vielä. Ei asiakasmääriä, tuloksia, arvosteluja eikä lehtijuttuja. **Mainoksissa ei käytetä mitään näyttömerkkejä.** Luottamus rakennetaan riskin poistolla (takuu, ei sitoutumista).

| Format | Exact wording | Best used when | Matching design asset (if any) |
|---|---|---|---|
| Guarantee | "Jos sovittu liiditavoite ei täyty, et maksa palkkiota" | Riskin poisto | — |

Curated, attributed customer quotes: None.

## Objections & Creative Responses (used directly by the skills)

| Objection | What the prospect is thinking | Creative response |
|---|---|---|
| Kokeiltu jo | "Kokeilin Facebook-mainontaa / toimistoa, ei tullut mitään" · tutkimus: "Koen, että 700 euroa kuukaudessa on mennyt hukkaan." — customer story, Yrittäjät-lehti, 17.1.2024 | Tulostakuu: jos tavoite ei täyty, ei palkkiota. Tarjous hiotaan ennen mainoksia, eikä samaa yleismainosta toisteta. |
| Huonot liidit | "Somesta tulee vain hintojen kyselijöitä" · tutkimus: "Ne eivät aina vastaa sitä mitä on kirjoiteltu urakkatarjouspyynnöissä" — forum, Suomi24, 9.2.2018 | Tavoite sovitaan laadukkaina liideinä, ja lomakkeen kysymykset karsivat. Tarjous rakennetaan isompaan työhön. |
| Ei näyttöä | "Uusi tekijä, ei referenssejä" | Rehellisesti: "Olen uusi, siksi kannan riskin." Ensimmäinen kuukausi ilman palkkiota, takuu. |
| Mainosbudjetin riski | "Mainosbudjetti menee silti hukkaan" | Budjetti sovitaan pieneksi alkuun, ja saat ilmoituksen jokaisesta liidistä. Voit lopettaa milloin vain. |
| Sitoutuminen | "Joudun pitkään sopimukseen" · tutkimus: "Myyjät ei sanallakaan kerro että heidän tuotteet ovat vuoden kestävillä sopimuksilla." — forum, Suomi24, 25.8.2023 | Ei aloitusmaksua, ei sitoutumista. |
| Aika ja vaiva | "Ei ole aikaa alkaa kuvata ja kirjoittaa" | Mainokset tehdään valmiista työkuvistasi. Sinä vain hyväksyt ne ja soitat liideille. |
| Kapasiteetti | "En ehdi edes hoitaa nykyisiä töitä" | (Ei kohdeasiakas juuri nyt. Ei vastausta mainoksissa.) |
| Hinta | "Paljonko tämä maksaa?" / "Toimisto on kallis" · tutkimus: "Miten Fonectalla on kanttia pyytää 850 euroa 1 euron arvoisesta tuotteesta?" — forum, Suomi24, 11.10.2022 | Ensimmäinen kuukausi ilman palkkiota: näet tulokset ennen kuin maksat. Hinta sovitaan puhelimessa ennen aloitusta. (Ei hintaa mainokseen.)  Vanha luonnos: Yksi työ (> 1 000 €) maksaa sen takaisin. Ensimmäinen kuukausi ilman palkkiota. |
| Läpinäkymättömyys | "Ei osattu kertoa, mihin markkinointi on kohdennettu" — customer story, Yrittäjät-lehti, 17.1.2024 | Ilmoitus jokaisesta liidistä, kuukausiraportti. (vahvistettava: onko mainostili asiakkaan oma ja näkeekö hän sen?) |
| Tyrkyttävät myyjät | "Taas yrittivät tyrkyttää jotain 850€ pakettia, oli ilo sanoa, EI." — forum, Suomi24, 10.10.2022 | Ei puhelinmyyntiä: asiakas jättää itse yhteystiedot, ehdot kirjallisesti. (vahvistettava) |

## Real Deadlines & Seasonality (used directly by the skills)

- None — no dated urgency claims. ("Otan vain rajallisen määrän asiakkaita" on totta, mutta ilman lukua sitä ei käytetä kiireväitteenä.)

## Off-Limits Claims & Compliance Notes (used directly by the skills)

- Ei väitteitä kokemuksesta, asiakasmääristä, tuloksista tai "satoja liidejä" -tyyppisistä luvuista, koska niitä ei ole
- **Ei kuukausihintaa (500 €/kk tai muuta) mainoksissa eikä laskeutumissivulla:** hinta sovitaan asiakaskohtaisesti (käyttäjä 30.10.2026). "Ensimmäinen kuukausi 0 € palkkiota" saa näkyä.
- Ei taattuja liidimääriä tai liidihintoja: tavoite sovitaan asiakaskohtaisesti
- Ei muiden asiakkaiden (esim. muiden kansioiden asiakkaat) nimiä, mainoksia, lukuja tai kuvia ilman asiakkaan kirjallista lupaa
- "Ilmainen" vain ehdoilla: aina selvästi, että mainosbudjetti maksetaan Metalle erikseen
- Ei henkilökohtaisia ominaisuuksia kohdistavaa kieltä (Meta-politiikka), esim. "Oletko yrittäjä, jolla ei ole asiakkaita?"

## Stage of Sophistication

- Vaihe 4–5 (Schwartz). Palveluyrittäjät näkevät paljon "lisää liidejä / asiakkaita somesta" -mainoksia toimistoilta ja kouluttajilta. Suorat lupaukset eivät enää toimi. Erottuminen tulee riskin poistosta (takuu, ei sitoutumista), rehellisyydestä ("olen uusi") ja mekanismista (tarjous ensin, omat työkuvat).

---

## Service details (service business)

- **What's included:** asiakashankinta Meta-mainoksilla: tarjouksen hiominen, strategia, rajaton määrä mainoksia yrityksen omista kuvista, kampanjoiden rakentaminen ja optimointi, ilmoitus jokaisesta liidistä, kuukausiraportti. Asiakas hoitaa liidien yhteydenotot itse.
- **Process:** Meta-pikalomake (karsintakysymykset) → soitto → kartoitus → liiditavoitteen sopiminen → käyttöoikeudet → aloitus
- **Service area:** koko Suomi, etänä
- **Timeline:** kampanja käyntiin noin viikossa sopimuksesta, kun asiakkaan Meta-tilien käyttöoikeudet (kumppanuus Business Managerissa) saadaan kuntoon. Oikeuksien jako voi viivästyttää aloitusta, joten aikalupausta ei käytetä mainoksissa.
- **Price range:** sisäinen lähtöhinta 500 €/kk + asiakkaan Meta-mainosbudjetti, ei aloitusmaksua. **Hinta sovitaan asiakaskohtaisesti, eikä sitä mainita mainoksissa eikä laskeutumissivulla** (käyttäjä 30.10.2026).
- **Warranties:** tulostakuu (ks. EiTulostaEiLaskua)
- **Capacity:** rajallinen, ei tarkkaa lukua
- **Jobs we don't want:** liikevaihto < 200 000 €, palvelun arvo pieni (< 1 000 €), verkkokaupat (ei tämän kampanjan kohde)

## Product details (online store)

- n/a

---

## Level of Consciousness: Low/High

- Korkea: yrittäjä tietää haluavansa lisää asiakkaita ja tuntee Meta-mainonnan. Pain point (epävarma asiakasvirta, aiemmat huonot kokemukset mainostoimistoista) on tiedossa.

## Level of Awareness:

- Enimmäkseen ongelma- ja ratkaisutietoisia: tuntevat ratkaisun (mainonta, toimistot), mutta eivät luota siihen. Tarkentuu audience-hypotheses.md:ssä.

## Big Idea

- {{luonnostellaan tutkimuksen jälkeen; ehdokas: "Mainostoimisto, joka kantaa riskin: jos liidejä ei tule, et maksa"}}

## Metaphor

- {{…}}

## Potential UMP (unique mechanism of the problem)

- {{ehdokas: mainokset epäonnistuvat yleensä tarjouksen takia, ei mainoksen ulkonäön takia}}

## Potential UMS (unique mechanism of the solution)

- {{ehdokas: tarjous hiotaan ensin, mainokset yrityksen omista työkuvista, testataan useita tarjouksia}}

## Guru / Face of the business:

- {{oma nimi / kasvot? (odottaa päätöstä kuvista)}}

## Discovery Story

- {{miksi aloitit}}

## Potential Headline/Subheadline Ideas

- Ei tuloksia? Ei laskua.

## List all objections you can think of

- Ks. Objections-taulukko yllä

## Belief Chains (what does the prospect have to believe in order to buy)

- See necessary-beliefs.md

## Examples/Swipes

- {{kilpailijat: suomalaiset Meta-mainostoimistot ja freelancerit (kerätään ad-inspiration-collectionilla)}}

## Other notes

- Liidiprosessi (30.10.2026): laskeutumissivu tehdään (tekstit: outputs/landing-page/landing-page-teksti-ja-rakenne.md), lomake + soita heti -linkki. Ensimmäisen kierroksen konversiopaikka (pikalomake + linkki sivulle vai suoraan sivu) on vielä päättämättä.
