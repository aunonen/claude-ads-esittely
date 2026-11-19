# FMT-001 — Toimintakehotus erottuvana laatikkona kuvassa

**Tyyppi:** FMT formaatti
**Taso:** Candidate
**Luotu:** 2026-10-26 · **Viimeksi nähty:** 2026-10-26

---

## Mikä se on

Kuvan toimintakehotus erotetaan omaksi täytetyksi suorakulmioksi tai pyöristetyksi laatikoksi. Laatikon tekstissä on toiminta ja sen kohde; alustan oma CTA on erillinen osa mainosta.

## Mekanismi: miksi se todennäköisesti toimii

Tekstin, kuvan ja brändimerkkien joukosta voi olla helpompi löytää seuraava askel, kun sillä on oma kontrastialue. Aineistossa ei ole testiä, joka erottaisi laatikon vaikutuksen tarjouksesta tai sanamuodosta.

## Milloin sopii

- **Tietoisuustaso:** Solution aware sekä arviointipalvelua etsivä Problem aware
- **Ostotilanne:** Kartoituksen varaus tai palvelun kokeilu · hintataso tuntematon · yksi selkeä seuraava askel
- **Tarjoustyyppi:** Nimetty varaus, tilaus tai kokeilu. Formaatin käyttö ei muuta palvelua maksuttomaksi.
- **Ei sovi, kun:** Laatikko sisältää vain hyötyväitteen tai hintamerkin, kilpailevia toimintolaatikoita on monta tai teksti ei pysy luettavana pienessä koossa.

## Näyttö

**3 eri mainostajanimeä, 4 lähdemainosta.** Yhdistelmien signaalilaskennassa yksi A-mainostaja = +2; tämän komponentin esiintymisen summa +6. Summa ei ole liiditulos eikä korota luottamustasoa. Löytökorit: map; ei validate-hakuun perustuva kuvio.

| Mainostaja | Ala | Mainos (Library ID) | Luokka | Tila | Käyttöikä | EU-tavoittavuus |
|---|---|---|---|---|---|---|
| Kylpyri | Kylpyhuone- ja saunaremontit | [1036353882690112](https://www.facebook.com/ads/library/?id=1036353882690112) / [kuva](../ads/kylpyhuoneremontit/kylpyri-ilmainen-kartoitus-A.jpg) | A | Candidate | 88 pv | 6 257 (26.10.2026) |
| Ametro.fi | Kotisiivous | [1313808140362787](https://www.facebook.com/ads/library/?id=1313808140362787) / [kuva](../ads/kotisiivous/ametro-testisiivous-A.jpg) | A | Candidate | 413 pv | 40 251 (26.10.2026) |
| Kymen Kattokeskus | Kattojen huolto ja pinnoitus | [912424291580816](https://www.facebook.com/ads/library/?id=912424291580816) / [kuva](../ads/kattopalvelut/kymen-kattokeskus-pinnoitus-vai-remontti-A.jpg) | A | Candidate | 215 pv | 22 073 (26.10.2026) |
| Kymen Kattokeskus | Kattojen huolto ja kunnostus | [1607713493817196](https://www.facebook.com/ads/library/?id=1607713493817196) / [kuva](../ads/kattopalvelut/kymen-kattokeskus-arvaus-vai-huoltosuunnitelma-A.jpg) | A | Candidate | 215 pv | 41 226 (26.10.2026) |

**Yhdistelmät:** Näyttämökuva × erottuva toimintolaatikko: Kylpyri, Ametro, Kymen, 3 A-mainostajaa ja +6.

**Tulkinnan raja:** Kolme mainostajaa, neljä kuvaa. Kymen kaksi kuvaa lasketaan yhdeksi mainostajaksi. Tiivin ja Pihlan tavalliset tekstikehotukset ovat formaatin puuttumisen esimerkkejä, eivät sen hävinneitä testejä.

Versioparit, joissa tämä kuvio oli eroava tekijä: ei varmennettuja. Useita versioita tai eri kuvatunnisteita ei tulkita kontrolloiduksi testitulokseksi.

## Vastanäyttö

| Mainostaja | Ala | Pudotettu mainos (Library ID) | Käyttöikä | Kausi | Huomio |
|---|---|---|---|---|---|
| — | — | — | — | — | Ei vahvistettua kuvioon kohdistuvaa Dropped-riviä; inaktiivihistorian tarkistus jäi otokseksi. |

Pudottaneiden määrää ei tunneta kattavasti. Puuttuva vastanäyttö ei todista kuviota toimivaksi. Kuvioiden puuttumista toisesta A-mainoksesta ei lasketa epäonnistuneeksi testiksi.

## Referenssit

**Ei vielä Confirmed-referenssejä.** Kaikki yllä olevat lähdemainokset ovat Candidate-tilassa. Näyttötaulun kuvalinkit ovat tarkastettavia havaintoja, eivät skillin tarkoittamia 2–3 Confirmed-referenssiä. Referenssit valitaan vasta uusintatarkistuksen jälkeen eri mainostajilta.

## Sovellusohje (suomeksi)

Erota yksi CTA taustasta asiakkaan brändiin sopivalla kontrastipinnalla. Nimeä toiminta ja palvelu; pidä lukujärjestys otsikko → selitys → CTA. LämpöYkkösen huollon kolme luottamuslaatikkoa tai 1KOMMA5:n arvoympyrä eivät ole tämän kuvion CTA-laatikoita.

Käyttö vain nimettynä testinä: kuvio × asiakkaan oma tarjous × asiakkaan oma aineisto. Asiakkaan omat analytiikkatulokset ja oman markkinan näyttö menevät tämän kirjastohypoteesin edelle.

## Agentuurin testit

Ei testipalautetta. Käyttäjä ilmoitti 26.10.2026, ettei Kirjastopalaute-rivejä ole. Asiakaskansioita ei luettu.

## Historia

| Päivä | Muutos | Hyväksyjä |
|---|---|---|
| 2026-10-26 | Luotu tasolle Candidate julkisesta komponenttianalyysistä; ei tasomuutosta | — |

Koko analyysi: [komponentit ja yhdistelmät](../analysis-2026-10-26.md). Supported-tasoa ei ehdoteta: Confirmed-mainoksia 0. Proven-tasoa ei ehdoteta: agentuurin testivoittoja 0.

