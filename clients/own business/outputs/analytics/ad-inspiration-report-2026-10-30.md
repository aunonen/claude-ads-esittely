# Ad Inspiration Intelligence Report — oma agency — 30.10.2026

> **Päivitys 30.10.2026 (käyttäjä):** kuukausihintaa ei näytetä mainoksissa eikä laskeutumissivulla, koska hinta sovitaan asiakaskohtaisesti. Ideoissa #1 ja #12 hinnoittelukortti näyttää vain "Ensimmäinen kuukausi: 0 €". Idea #5 (laskelma 500 €) ei ole käytettävissä sellaisenaan. Pää-CTA: "Selvitä, voisinko tuoda yrityksellesi lisää tarjouspyyntöjä".

> Vaihe 1 (`competitor-analysis`). Aineisto: 11 tallennettua kuvamainosta (Sheet "Ad Inspiration", sisäinen) + 20 tekstiriviä evidence-lokista (videot ja lopetetut mainokset). Kaikki analyysit ovat kilpailijoiden mainoksia; omia mainoksia ei vielä ole.
>
> **Aineisto on ohut:** liidi- tai tarjoustavoitteisia A/B-kuvamainoksia on 6 (suositus ≥ 10). Siksi yhdistelmäanalyysissä käytetään A- ja B-mainostajia yhdessä (pelkillä A-mainoksilla yksikään yhdistelmä ei yltäisi kahteen mainostajaan), ja tekstirivit (videot) lasketaan mukaan copyn, tarjouksen ja kulman osalta, ei luovan konseptin.

---

## 1. Starting Point

- **Kierroksen tyyppi:** First round (ei Phase 0 -raporttia, ei aiempia mainoksia)
- **Kontrolli:** ei ole
- **Testatut tarjous × kulma -parit:** ei yhtään. `context/learnings.md` on tyhjä pohja.
- **Testislotit:** 15 €/pv ÷ 5 €/mainos = **3 mainosta** kierroksella (meta-ads-config.json)
- **Hyväksytyt tarjoukset:** `EnsimmainenKuukausiIlmaiseksi` (kärki), `EiTulostaEiLaskua`, `IlmainenKuukausiJaTakuu`
- **Kuvat:** `reference/products/Images/` on tyhjä → ensimmäisen kierroksen mainokset ovat tekstipohjaisia tai natiiviformaatteja (käyttäjä voi ottaa kuvia briefin mukaan)
- **Agencyn kirjasto:** 6 Candidate-korttia (kodin palvelut). Sopivat tason 3 näytöksi: `OFF-001` maksuton asiantuntija-arvio, `CPY-001` kysymys ja vastaus, `CPY-002` maksuton apu otsikossa, `FMT-001` CTA-laatikko kuvassa. Ei Supported/Proven-kortteja.

## 2. Inspiration Inventory

| Tiedosto | Mainostaja | Luokka | Tavoite | Tarjous | Kulma | Luova konsepti | Ensimmäinen rivi | Primary text |
|---|---|---|---|---|---|---|---|---|
| kamu-digital-maksuton-google-ads-auditointi-A.jpg | Kamu Digital | A | Quote request | Maksuton Google Ads -auditointi | Ilmainen asiantuntijakatsaus ennen ostoa | Maskottihahmo + nuoli, uteliaisuus | "Varaa Google Ads -audit, kun haluat tietää seuraavat asiat." | ✅ |
| kamu-digital-maksuton-markkinoinnin-kartoitus-B.jpg | Kamu Digital | B (stopped) | Quote request | Maksuton 30 min kartoitus | Tarjous edellä | Maskotti + kädet (kiireinen markkinoija) | "Varaa ilmainen markkinoinnin kartoitus!" | ✅ |
| kamu-digital-montako-hattua-B.jpg | Kamu Digital | B (stopped) | Quote request | Ulkoistus, varaus | Lukijan kuorma / roolit | Visuaalinen metafora (hattupino) | "Onko markkinoinnin hattuja kertynyt jo liian monta?" | ✅ |
| oikio-micro-2-viikkoa-ilmaiseksi-A.jpg | Oikio Digital | A | Website conversion | 49 €/kk, 2 vk ilmaiseksi | Uutuus + riskitön kokeilu | Hinnoittelukortti | "Nyt se on julkaistu!" | ✅ |
| oikio-maksa-mainonnasta-ei-toimistolaskusta-B.jpg | Oikio Digital | B | Website conversion | 199 €/kk, ei tuntiveloituksia | Maksa mainonnasta, älä toimistolaskusta | Abstrakti 3D-vaaka | "Google ja Meta mainonta yhdellä hinnalla!" | ✅ |
| liidikeskus-yksi-kauppa-maksaa-liidit-B.jpg | Liidikeskus.fi | B (stopped) | Lead form | Tarjouspyynnöt 40 €/kpl, ei kk-maksua | Laskelma: kauppa maksaa liidit | Pelkkä tekstikysymys mustalla | "Jos voisit ostaa yrityksellesi tarjouspyyntöjä hintaan 40€/kpl" | ✅ |
| miami-agency-todennakoisin-valinta-B.jpg | MIAMI Agency | B | Awareness | – | Haastaa liidimäärän mittarina | Perustajan sitaattikortti | "Markkinoinnin tehtävä ei ole tuottaa mahdollisimman paljon liidejä." | ✅ |
| meio-rahat-hukkaan-perustajan-tarina-C.jpg | Meio | C | Content | Maksuton opas | Mainonta ei ole vika, sivusto on | Perustajakuva + tekstikerros | "Mainos lupaa. Sivusto ei lunasta." | ✅ |
| eki-eke-3kk-200e-kokeilu-C.jpg | Eki & Eke | C | Quote request | 3 kk alkaen 200 €/kk | Edullinen aloitus, ihmiseltä ihmiselle | Brändätty valokuva | "Markkinoinnin paras kaveri — Ei yhtään enempää." | ✅ |
| popup-media-get-proper-jobs-C.jpg | Popup Media (AU) | C | Lead form | Karsitut liidit, alk. $450/vk | Laatu määrän sijaan | Kohdeasiakas + otsikkopaneeli | "QUALIFIED LEADS ONLY" | ✅ |
| popup-media-yksi-tekija-per-alue-C.jpg | Popup Media (AU) | C | Call booking | Maksuton 15 min konsultaatio | "Not a you problem" | TV-uutisraportti (**mediabrändi, ei saa jäljitellä**) | "TRADIES ARE LOSING JOBS BEFORE THEY EVEN QUOTE." | ✅ |

**Koko aineisto:** Own 0 · A 2 · B 5 · C 4 · Unscored 0 (kuvat). Tekstirivit: B 11 (joista 5 lopetettuja Adspark-ideoita), C 9, Dropped 1 (Oikio, todennäköisesti uudelleenjulkaisu).

## 3. Component Map

Mainostajat lasketaan kerran per kuvio. Liidi/myyntitavoite paitsi erikseen merkityt. Löytökori: map = kategoria/kilpailijanimi, discover = neutraali aihe, validate = omat sanat.

| Komponentti | Kuvio | Own + A | B | C + Unscored | Tried and dropped | Esimerkit (kori) |
|---|---|---|---|---|---|---|
| Tarjous | **Tulostakuu / maksa vain tuloksesta** | 0 | 4 (Adspark, Pyymäki, Xcellent, Roof Coating Leads) | 3 (VELON, Liidilab, Advanced Agent*) | 0 | tekstirivit (map, discover; *validate) |
| Tarjous | **Maksuton arvio / kartoitus / konsultaatio** | 1 (Kamu) | 1 (Xcellent) | 3 (Popup, Tropical Familia, Triplat) | 0 | kamu-…-A, kamu-…-kartoitus-B (map) |
| Tarjous | **Hinta näkyvissä** | 1 (Oikio) | 2 (Liidikeskus, Digital Marketing Genius) | 1 (Popup) | 0 | oikio-…-A, liidikeskus-…-B (map) |
| Tarjous | **Ei sitoumuksia / ei kk-maksua** | 0 | 2 (Liidikeskus, DMG) | 2 (Liidilab, VELON) | 0 | liidikeskus-…-B (map) |
| Tarjous | **Ilmainen / alennettu aloitusjakso** | 1 (Oikio Micro) | 0 | 1 (Eki & Eke) | 0 | oikio-micro-…-A (map) |
| Kulma | **Kyllästynyt toimistoihin / toimistolasku** | 0 | 3 (Oikio, Adspark, DMG) | 3 (Paving Leads, Blacktop, Harvest) | 0 | oikio-…-B (map), tekstirivit |
| Kulma | **Liidien laatu: karsitut, oikeat asiakkaat** | 0 | 3 (Liidikeskus, Adspark, Xcellent) | 2 (Popup, Tropical Familia) | 0 | liidikeskus-…-B, popup-…-C |
| Kulma | **Puskaradio ei riitä** | 0 | 1 (CloudBridge) | 2 (Tropical Familia, Popup) | 0 | tekstirivit (discover, map) |
| Kulma | **Jaetut liidit vs. omat** | 0 | 1 (Liidikeskus: "juuri teidän yritykseltänne") | 1 (Tree Service MA) | 0 | tekstirivit (discover) |
| Kulma | **Kuorma / liian monta roolia** | 0 | 1 (Kamu) | 0 | 0 | kamu-…-hattua-B (map) |
| Copy, 1. rivi | **Call-out: ala / koko / hinta rajattu otsikossa** | 0 | 4 (Adspark, Xcellent, Roof Coating, Pyymäki) | 2 (Popup, Tropical Familia) | 0 | tekstirivit, popup-…-C |
| Copy, 1. rivi | **Suora tarjous ("Varaa maksuton…")** | 1 (Kamu) | 0 | 0 | 0 | kamu-…-A |
| Copy, 1. rivi | **Kysymys** | 0 | 2 (Kamu hattua, Liidikeskus) | 0 | 0 | kamu-…-hattua-B, liidikeskus-…-B |
| Copy, 1. rivi | **Vastakkainasettelu "Maksa X, älä Y"** | 0 | 1 (Oikio) | 0 | 0 | oikio-…-B |
| Copy, 1. rivi | **Case-luvut avauksena** | 0 | 2 (Adspark, Pyymäki) | 2 (VELON, Popup) | 0 | tekstirivit |
| Luova konsepti | **Hinnoittelukortti** | 1 (Oikio) | 0 | 0 | 0 | oikio-micro-…-A |
| Luova konsepti | **Pelkkä teksti tummalla (kysymys)** | 0 | 1 (Liidikeskus) | 0 | 0 | liidikeskus-…-B |
| Luova konsepti | **Maskotti / visuaalinen metafora** | 1 (Kamu) | 0 | 0 | 0 | kamu-… (kaikki 3) |
| Luova konsepti | **Perustaja kasvoina / henkilöbrändi** | 0 | 3 (Adspark, Xcellent, Pyymäki; videoita) + MIAMI (awareness) | 2 (Meio content, Liidilab) | 0 | miami-…-B (format) |
| Tietoisuus | **Solution aware** (tarjous/riskin poisto edellä) | 2 (Kamu, Oikio) | 4 | 4 | 0 | – |
| Tietoisuus | **Problem aware** (kuorma, rahat hukkaan, häviät tarjoukset) | 0 | 1 (Kamu hattua) | 2 (Meio, Popup) | 0 | – |
| CTA | **Varaa (maksuton) aika / puhelu** | 1 (Kamu) | 2 (Xcellent, Kamu kartoitus) | 2 | 0 | – |
| CTA | **Lomake + karsintakysymykset** | 0 | 2 (Liidikeskus, Roof Coating) | 2 (Tropical, Popup) | 0 | – |

**Mitä vahvoissa mainoksissa toistuu?**
- **Riskin poisto on alan valtavirtaa:** tulostakuu (4 B-mainostajaa), ei sitoumuksia, maksuton arvio. Pelkkä "takuu" ei enää erota, mutta se on odotettu.
- **Rajaus otsikossa** ("Yrittäjä: Myykö firmasi…", "HVAC Companies Doing $1M+", "yli 1000€ hintaista") on vahvin copy-kuvio: 4 B-mainostajaa. Se karsii ja tekee lukijasta tunnistetun.
- **Staattisissa A-mainoksissa** voittaa yksinkertaisuus: yksi tarjous, yksi rivi, selvä CTA (Kamu: "Varaa…", Oikio: hinta + "Kokeile 2 viikkoa ilmaiseksi").
- **Omia mainoksia ei ole**, joten ei laajennettavaa voittajaa.
- **Sopivimmat kulmat agencylle** (palveluyritykset, ≥ 200 k€): toimistopettymys, liidien laatu ja riskin poisto. Ne osuvat tutkimuksen toistuvimpiin pelkoihin (RahatHukkaan, SopimusLukko, VaaraKohderyhma).

## 3b. Combination Analysis

Pisteet: Own +3, A +2, B +1, C 0, Dropped −2. Vain liidi/myyntitavoite.

| Yhdistelmä | Mainostajat (luokat) | Pudottajat | Pisteet | Verdict | Kirjasto | Esimerkit |
|---|---|---|---|---|---|---|
| hinta näkyvissä × riskin poisto (ilmainen jakso / ei sitoumuksia) | 3 (Oikio A, Liidikeskus B, DMG B) | 0 | +4 | **Pattern** | – | oikio-micro-…-A, liidikeskus-…-B |
| call-out-rajaus otsikossa × tulostakuu | 4 (Adspark B, Xcellent B, Roof Coating B, Pyymäki B) | 0 | +4 | **Pattern** | – | tekstirivit |
| maksuton arvio/kartoitus × Solution aware × varaa-CTA | 2 + 2 C (Kamu A, Xcellent B; Popup C, Tropical C) | 0 | +3 | **Pattern** | `OFF-001` Candidate, `CPY-002` Candidate | kamu-…-A, kamu-…-kartoitus-B |
| toimistopettymys avauksena × riskin poisto | 3 + 3 C (Oikio B, Adspark B, DMG B; Paving, Blacktop, Harvest C) | 0 | +3 | **Pattern** | – | oikio-…-B, tekstirivit |
| liidien laatu (karsinta) × lomake karsintakysymyksin | 2 + 2 C (Liidikeskus B, Roof Coating B; Popup, Tropical C) | 0 | +2 | **Pattern** | – | liidikeskus-…-B, popup-…-get-proper-jobs-C |
| kysymys ensimmäisenä × Solution/Problem aware | 2 (Kamu hattua B, Liidikeskus B) | 0 | +2 | **Pattern** (heikko) | `CPY-001` Candidate | kamu-…-hattua-B, liidikeskus-…-B |
| case-luvut avauksena × tulostakuu | 2 (Adspark B, Pyymäki B) + VELON C | 0 | +2 | **Pattern** – **ei käytettävissä** (agencylla ei lukuja) | – | tekstirivit |
| ilmainen kokeilujakso × hinta näkyvissä | 1 (Oikio A) + Eki C | 0 | +2 | **Single observation** | – | oikio-micro-…-A |
| puskaradio ei riitä × Problem aware | 1 (CloudBridge B) + Tropical C, Popup C | 0 | +1 | **Single observation** | – | tekstirivit |
| jaetut liidit vs. omat × urakoitsija | 1 (Liidikeskus B, osittain) + Tree Service C | 0 | +1 | **Single observation** | – | tekstirivit |
| ei myyjiä / ei painostusta × maksuton puhelu | 1 (Xcellent B: "No pitch deck. No pressure. No salesperson.") | 0 | +1 | **Single observation** | – | tekstirivi |
| uutisraportti oikealla mediabrändillä | 1 (Popup C) | – | 0 | **Avoid** (eettinen ja Meta-politiikka, ei näyttö) | – | popup-…-yksi-tekija-per-alue-C |

**Versioparit:**
- **Oikio, ilmainen kokeilu:** "1 viikko ilmaiseksi" (40 pv) → "2 viikkoa ilmaiseksi" (aktiivinen, suurin tavoittavuus). Viittaa siihen, että **pidempi ilmainen jakso** korvasi lyhyemmän. Tukee `EnsimmainenKuukausiIlmaiseksi`-tarjousta.
- **Adspark, case-luvut:** isommilla luvuilla päivitetty versio ajettiin yhtä pitkään (~4 kk). Lukuja päivitetään, ideaa ei vaihdeta.
- **Oikio, "löytääkö hän sinut":** lopetettu 2 päivässä, sama teksti jatkui uusilla ID:illä → uudelleenjulkaisu, ei testitulos.

## 4. White Space

| Mitä kukaan ei tee | Agencyn fakta, joka mahdollistaa sen | Hypoteesi |
|---|---|---|
| **Ilmainen ensimmäinen kokonainen kuukausi** palveluna (Oikio antaa 2 vk työkalusta, Eki & Eke alennuksen) | Hyväksytty tarjous `EnsimmainenKuukausiIlmaiseksi` | Pidempi ja koko palvelun kattava riskitön jakso erottuu, kun takuu on jo yleinen |
| **Rehellinen "olen uusi"** | Ei asiakkaita eikä tuloksia (business-info) | Kaikki muut avaavat isoilla luvuilla; avoin uutuus + riskin kantaminen voi olla uskottavampi kuin lukujen puute |
| **Mainokset yrityksen omista työkuvista, ei tekoälyä** | USP offer-briefissä | Kukaan ei mainitse; Popup käyttää itse AI-näköisiä kuvia |
| **Yksi ihminen tekee kaiken, ei myyjiä** | USP; Xcellent sivuaa ("No salesperson") | Vastaa tutkimuksen TyrkyttavatMyyjat-pelkoon |
| **Palveluyrittäjä 200 k€+ suomeksi ilman videota** | Kohdeasiakas strategy.md:ssä | Tropical Familia käyttää samaa rajausta, mutta vain videona ja vasta 27.10. alkaen |

## 4a. Library Gaps

Ei yhtään: kirjastossa ei ole Supported- tai Proven-kortteja. `OFF-001` (Candidate) sopii toisena ostotilanteena (B2B-markkinoinnin kartoitus); ehdotus kirjastoon lisättäväksi hub-sessiossa.

## 4b. New to Us

| Löydös | Mainokset | Ei ole `context/`-tiedostoissa |
|---|---|---|
| Rajaus otsikossa (ala, liikevaihto, palvelun hinta) | Adspark, Xcellent, Roof Coating, Pyymäki, Popup | Uusi copy-kuvio |
| Hinta per liidi kysymyksenä ("kuinka monta ostaisit?") | Liidikeskus B | Uusi kulma (laskelma lukijan päässä) |
| Liidien karsinta palveluna ("We filter the tyre-kickers") | Popup, Tropical, Liidikeskus | Uusi kulma |
| "Not a you problem, that's a marketing problem" (syyn siirto) | Popup C, Meio C | Uusi kulma |
| Nopein vastaaja voittaa työn | Popup C | Uusi ongelma |
| Yksinoikeus alueelle / toimialalle ("One tradie per suburb") | Popup C | Uusi tarjousidea (ei hyväksytty) |
| "Teemme puolestasi, emme myy kurssia" | Popup C | Uusi argumentti |
| Liidit, jotka eivät vastaa puhelimeen | Adspark | Uusi ongelma |
| Maksuton kartoitus / arvio | Kamu A, Xcellent B | Uusi tarjousidea (ei hyväksytty) |

## 5. Brand Ad Ideas (First round, 12 ideaa)

Kaikki tekstipohjaisia, koska kuvia ei ole: layoutit `Plain text`, `Headline on top`, natiiviformaatit (`sticky note with text`, `iphone notes`, `checklist`, `calculator`). Kuvia tarvitseva idea on merkitty.

**1. Ilmainen kuukausi hinnoittelukorttina**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `RiskiOnMinun` — lähtee siitä, kuka kantaa riskin, kun mainonta ei toimi
- Audience: `PettynytToimistoon` · Solution aware · Problem: `RahatHukkaan` · Objection: rahat menevät hukkaan
- Argument: `Guarantee — ensimmäinen kuukausi 0 € palkkiota, lopetus milloin vain`
- Creative copy: "Ensimmäinen kuukausi: 0 €" · "Sen jälkeen 500 €/kk. Ei aloitusmaksua. Lopeta milloin vain." · pienellä: "Mainosbudjetti maksetaan suoraan Metalle."
- Creative concept: hinnoittelukortti (lähin: `spreadsheet` / uusi: **Hinnoittelukortti**, flag)
- CTA: Lisätietoja → pikalomake
- Lähde: oikio-micro-…-A (A), liidikeskus-…-B
- **Hypothesis:** Uskomme, että ilmainen kuukausi hinnoittelukorttina tuo liidejä alle 40 €, koska `hinta näkyvissä × riskin poisto` on Pattern (3 mainostajaa, +4, ei pudottajia) ja Oikion versiopari osoittaa pidemmän ilmaisjakson korvanneen lyhyemmän.
- Status: New · Offer status: Approved · Feasibility: custom `.card` (Plain text), ei kuvaa tarvita

**2. Rajaus otsikossa + tulostakuu**
- Offer: `EiTulostaEiLaskua` · Angle: `New: RajattuKohderyhma` — puhuttelee suoraan yli 200 000 €:n palveluyritystä ja lupaa, ettei palkkiota makseta ilman tulosta
- Audience: `PuskaradionVarassa` / yleinen palveluyrittäjä · Solution aware · Desire: `MaksanVainTuloksesta` · Objection: rahat hukkaan
- Argument: `Guarantee — jos sovittu liiditavoite ei täyty, kuukauden palkkiota ei laskuteta`
- Creative copy: "Palveluyrittäjä, liikevaihto yli 200 000 €?" · "Sovitaan liiditavoite. Jos se ei täyty, et maksa palkkiota."
- Creative concept: `Plain text` (Liidikeskus-tyyli: tumma pohja, iso teksti)
- CTA: Lisätietoja
- Lähde: Adspark, Xcellent, Roof Coating, Pyymäki (B, tekstirivit)
- **Hypothesis:** Uskomme, että rajaus otsikossa karsii huonot liidit ja nostaa liidin laatua, koska `call-out-rajaus × tulostakuu` on Pattern (4 B-mainostajaa, +4). Riski: takuu on jo yleinen, joten tulos kertoo, riittääkö rajaus erottumaan.
- Status: New · Offer status: Approved · Feasibility: Plain text, ei kuvaa

**3. Toimistopettymys: "Maksoitko vuoden sopimuksesta?"**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `EiVuodenSopimusta` — lähtee aiemmasta huonosta sopimuksesta
- Audience: `PettynytToimistoon` · Solution aware · Problem: `SopimusLukko` · Objection: joudun pitkään sopimukseen
- Argument: `Guarantee — ei aloitusmaksua, ei sitoutumista, ensimmäinen kuukausi 0 €`
- Creative copy: "Maksoitko markkinoinnista vuoden, eikä puhelin soinut?" · "Täällä ensimmäinen kuukausi on ilmainen. Ja voit lopettaa milloin vain."
- Creative concept: `iphone notes` tai `sticky note with text`
- Lähde: oikio-…-B (B), Adspark B, DMG B
- **Hypothesis:** Uskomme, että toimistopettymyksestä lähtevä avaus tavoittaa ratkaisutietoisen, aiemmin pettyneen yrittäjän, koska `toimistopettymys × riskin poisto` on Pattern (3 B, +3) ja tutkimuksen RahatHukkaan/SopimusLukko ovat toistuvimmat pelot.
- Status: New · Offer status: Approved · Feasibility: natiiviformaatti `.note`, ei kuvaa

**4. "Olen uusi. Siksi kannan riskin."**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `UusiJaRehellinen`
- Audience: `PettynytToimistoon` · Product aware/Solution aware · Problem: `TyrkyttavatMyyjat` · Objection: uusi tekijä, ei näyttöä
- Argument: `Guarantee — ensimmäinen kuukausi 0 €`
- Creative copy: "Olen uusi. En voi näyttää satoja asiakkaita." · "Siksi ensimmäinen kuukausi on ilmainen."
- Creative concept: `handwritten text on paper` / `sticky note with text` (tai perustajan kuva + sitaatti, jos kuva otetaan)
- Lähde: white space; MIAMI B (perustajan sitaattikortti, format)
- **Hypothesis:** Uskomme, että avoin "olen uusi" -viesti erottuu kilpailijoiden lukupohjaisista avauksista ja tuo liidejä alle 40 €, koska kukaan aineistossa ei tee sitä (white space) ja agency ei voi käyttää case-lukuja. Single observation -tason ajatus; testaa itse rivin.
- Status: New · Offer status: Approved · Feasibility: `.note` / `.paper`; kuvaversio tarvitsee kuvan agencyn tekijästä (ei ole)

**5. Laskelma: yksi työ maksaa kuukauden**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `New: YksiTyoMaksaaKuukauden` — lähtee siitä, paljonko yksi uusi asiakas on yritykselle arvoinen
- Audience: palveluyrittäjä, palvelun arvo > 1 000 € · Solution aware · Desire: `LisaaAsiakkaita` · Objection: 500 €/kk on paljon
- Argument: `Data — yksi yli 1 000 €:n työ kattaa kuukauden palkkion (500 €)`
- Creative copy: "Paljonko yksi uusi asiakas on yrityksellesi arvoinen?" · "Jos yli 500 €, tämä maksaa itsensä yhdellä työllä."
- Creative concept: `calculator`
- Lähde: liidikeskus-…-B (B)
- **Hypothesis:** Uskomme, että lukijan oman laskelman herättävä kysymys tekee hinnasta pienen, koska `kysymys ensimmäisenä × Solution aware` on Pattern (2 B, +2) ja Liidikeskuksen laskelma-kysymys ajettiin 5 kk. Ei luvata liidihintaa (off-limits).
- Status: New · Offer status: Approved · Feasibility: natiivi `calculator`, custom

**6. Karsitut yhteydenotot**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `New: KarsitutLiidit` — liidien laatu, ei määrä
- Audience: `TarjouspalvelunKayttaja` / `ItseTekeva` · Solution aware · Problem: `VaaraKohderyhma` · Objection: somesta tulee huonoja liidejä
- Argument: `Mechanism — lomake kysyy toimialan ja koon ennen kuin yhteystieto tulee sinulle`
- Creative copy: "Ei hintojen kyselijöitä." · "Lomake karsii ennen kuin puhelin soi."
- Creative concept: `checklist` (✓ toimiala ✓ alue ✓ budjetti)
- Lähde: liidikeskus-…-B, popup-…-get-proper-jobs-C
- **Hypothesis:** Uskomme, että karsinta-lupaus vastaa huonolaatuisten liidien pelkoon, koska `liidien laatu × lomakekarsinta` on Pattern (2 B, +2). **Vahvistettava:** teetkö asiakkaan kampanjoihin karsivat lomakkeet (palvelukuvaus)?
- Status: New · Offer status: Approved (lupaus lomakkeesta: needs confirmation) · Feasibility: `.checklist`

**7. Jaetut liidit vs. omat**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `OmatLiiditEiProvisioita`
- Audience: `TarjouspalvelunKayttaja` · Problem aware · Problem: `KalliitProvisiot` · Objection: tottumus tarjouspalveluun
- Argument: `Mechanism — yhteydenotot tulevat vain sinulle, ei provisiota per työ`
- Creative copy: "Maksoitko tarjouspyynnöstä, jonka sai myös neljä muuta?"
- Creative concept: `choose A/b` (tarjouspalvelu vs. omat mainokset)
- Lähde: Tree Service MA (C), Liidikeskus B
- **Hypothesis:** Single observation (+1); testaa, onko urakoitsijoista oma segmentti.
- Status: New · Offer status: Approved · Feasibility: `.comparison`

**8. Puskaradio ja hiljainen kuukausi**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `PuskaradioEiSkaalaudu`
- Audience: `PuskaradionVarassa` · Problem aware · Problem: `HidasPuskaradio`
- Argument: `Guarantee — ensimmäinen kuukausi 0 €`
- Creative copy: "Suositukset ovat paras asiakaslähde." · "Mutta mitä teet kuukautena, jona kukaan ei suosittele?"
- Creative concept: `calendar reminder` (tyhjä viikko kalenterissa)
- Lähde: CloudBridge B, Tropical Familia C
- **Hypothesis:** Single observation (+1); testaa isointa joukkoa (ei aiempaa mainontaa).
- Status: New · Offer status: Approved · Feasibility: `.calendar`

**9. Ei myyjiä**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `YksiTekijaEiMyyjia`
- Audience: `PettynytToimistoon` · Solution aware · Problem: `TyrkyttavatMyyjat`
- Argument: `Mechanism — sama ihminen tekee mainokset ja vastaa puhelimeen`
- Creative copy: "Ei myyjiä. Ei välikäsiä." · "Sama ihminen tekee mainoksesi ja vastaa puhelimeen."
- Creative concept: `Plain text`
- Lähde: Xcellent B ("No pitch deck. No pressure. No salesperson.")
- **Hypothesis:** Single observation (+1) + tutkimuksen TyrkyttavatMyyjat (3 lähdettä).
- Status: New · Offer status: Approved · Feasibility: Plain text

**10. Maksuton mainonnan kartoitus** ⚠️
- Offer: `New: MaksutonKartoitus` — 20 min puhelu, jossa käydään läpi yrityksen nykyinen asiakashankinta
- Angle: `New: MaksutonArvio` · Solution aware · Desire: `NakeeMitaTehdaan`
- Creative copy: "Varaa maksuton 20 minuutin mainonnan kartoitus."
- Lähde: kamu-…-A (A, 21 kk), kamu-…-kartoitus-B, Xcellent B; kirjasto `OFF-001`
- **Hypothesis:** Uskomme, että matalan kynnyksen ensiaskel tuo enemmän liidejä kuin palvelun suora myynti, koska `maksuton arvio × Solution aware × varaa-CTA` on Pattern (+3) ja Kamun mainos pyöri 21 kk.
- Status: New · **Offer status: Needs client approval** (et ole vielä hyväksynyt maksutonta kartoitusta) · Feasibility: Plain text

**11. Kuormametafora yrittäjälle**
- Offer: `EnsimmainenKuukausiIlmaiseksi` · Angle: `New: LiikaaRooleja`
- Audience: `ItseTekeva` · Problem aware · Problem: `AikaEiRiita`
- Creative copy: "Yrittäjä, montako roolia sinulla jo on?" · "Anna mainonta pois. Ensimmäinen kuukausi on ilmainen."
- Creative concept: `checklist` (rastitettu rooliluettelo: myyjä, asentaja, laskuttaja, markkinoija…)
- Lähde: kamu-…-hattua-B (B, 11 kk; kohde oli in-house-markkinoija)
- **Hypothesis:** Single observation (+1); kopioi rakenne, ei kohdetta.
- Status: New · Offer status: Approved · Feasibility: `.checklist`

**12. Laskelma ilman ilmaista kuukautta (tarjoustesti)**
- Offer: `IlmainenKuukausiJaTakuu` · Angle: `RiskiOnMinun`
- Creative copy: "Ensimmäinen kuukausi 0 €. Sen jälkeen maksat vain, kun tavoite täyttyy."
- Creative concept: hinnoittelukortti (kuten #1)
- **Hypothesis:** Tarjoustesti #1:n rinnalle: kertooko takuun lisääminen enemmän kuin pelkkä ilmainen kuukausi? (Offer brief: "monimutkainen mainokseen", siksi vain yksi lause.)
- Status: Variation of #1 · Offer status: Approved · Feasibility: `.card`

## 6. Priority Ideas (3 slottia)

1. **#1 Ilmainen kuukausi hinnoittelukorttina** (`EnsimmainenKuukausiIlmaiseksi × RiskiOnMinun`): vahvin yhdistelmä (+4, A-mainostaja), kärkitarjous ja white space (kokonainen ilmainen kuukausi).
2. **#2 Rajaus otsikossa + tulostakuu** (`EiTulostaEiLaskua × RajattuKohderyhma`): vahvin copy-kuvio (4 B-mainostajaa); testaa eri tarjousta ja karsii liidejä.
3. **#4 "Olen uusi. Siksi kannan riskin."** (`EnsimmainenKuukausiIlmaiseksi × UusiJaRehellinen`): ainoa idea, jota kukaan ei tee; kertoo, toimiiko rehellisyys näytön puutteessa.

Vaihtoehto #3:lle: **#3 Toimistopettymys** (+3 Pattern), jos haluat kolmanneksikin todistetumman kulman.

## 7. Open Questions for the Client (eli sinulle)

- **Maksuton 20 min kartoitus** (idea #10): haluatko tarjota sen? Vahvin yksittäinen pitkäikäinen mainos (Kamu, 21 kk) perustuu siihen. → `offer-development`
- **Yksinoikeus toimialalle / alueelle** ("otan yhden asiakkaan per ala per kaupunki"): pitääkö paikkansa? Aito niukkuus ilman keksittyä lukua.
- **Karsivat lomakkeet asiakkaille** (idea #6): kuuluuko palveluun? Jos kyllä, lisätään USP:ksi.
- **Kuva itsestäsi** (idea #4 kuvaversio, perustajan sitaattikortti): ei pakollinen, tekstiversio toimii ilman.

## 8. Missing material (agencylle)

- Primary text puuttuu: ei yhtään (kaikilla sidecar).
- Taso 1: 7 kuvaa / tavoite 10–15 · Taso 2: 2 kuvaa + 11 tekstiriviä / 8–12 · Taso 3: 0 kuvaa / 3–5 → **alle tavoitteen**, koska agency-mainonta on pääosin videota.
- Refresh: seuraava keräys noin 1–2 kk päästä tai heti, kun Tropical Familian, VELONin ja Adsparkin uudet mainokset ovat pyörineet 30+ päivää (niiden kesto kertoo, toimiiko sama kohderyhmä).

## 9. Added to the test hypotheses

Ks. `context/audience-hypotheses.md` (30.10.2026):

- **Problems (uusia, Competitor):** `LiiditEivatVastaa`, `HaviaaTarjoukset`
- **Offers (Idea):** `MaksutonKartoitus`, `YksinoikeusToimialalle`
- **Angles (uusia, Competitor):** `RajattuKohderyhma`, `KarsitutLiidit`, `YksiTyoMaksaaKuukauden`, `LiikaaRooleja`, `MaksutonArvio`
- **Arguments:** neljä riviä, jotka agency voi näyttää (Guarantee ×2, Mechanism ×2)
- **Creative concepts:** `Hinnoittelukortti` (uusi, flag), `Plain text` (tumma, yksi kysymys), `checklist`, `calculator`, `iphone notes`
- **Creative copy:** call-out-rajaus, suora tarjous, kysymys + laskelma, vastakkainasettelu, case-luvut (merkitty: ei käytettävissä ilman lukuja)
- **Suggested tests:** #6–#8 (yhdistelmät yllä)
- **Lähde lisätty olemassa oleviin:** `PettynytToimistoon`, `TarjouspalvelunKayttaja`, `PuskaradionVarassa`, `ItseTekeva`, `RahatHukkaan`, `SopimusLukko`, `VaaraKohderyhma`, `TarjouksiinEiVastata`, `TyrkyttavatMyyjat`, `MaksanVainTuloksesta`, `VapausLopettaa`, `LisaaAsiakkaita`, `RiskiOnMinun`, `EiVuodenSopimusta`, `OmatLiiditEiProvisioita`, `NaetMihinRahatMenevat`, `PuskaradioEiSkaalaudu`, `YksiTekijaEiMyyjia`, tarjoukset `EnsimmainenKuukausiIlmaiseksi`, `EiTulostaEiLaskua`; awareness-rivit Problem/Solution aware
- **Retirement-ehdotukset:** ei. Avoid: uutisformaatti mediabrändillä (ei riviä; kirjattu evidence-lokiin)
