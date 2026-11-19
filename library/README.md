# Agentuurin mainoskirjasto

Agentuurin yhteinen kirjasto korkean arvon palveluyritysten **julkisista** Meta-mainoksista. Siitä kootaan näyttöön perustuvia **kuvioita** (tarjoukset, kulmat, creative conceptit, creative copyn keinot, formaatit), niiden **referenssejä** ja **tyylikirjasto** (kieli ja visuaalisuus).

Kirjastoa ylläpidetään hub-istunnossa `ad-library`-skillillä. Asiakasistunnot lukevat sitä polulla `../../library/`, mutta eivät koskaan kirjoita siihen.

---

## Mitä kirjastoon saa ja ei saa laittaa

- ✅ Julkisia mainoksia Metan mainoskirjastosta, jotka läpäisevät pääsyehdon
- ✅ Kuvion tunniste, tulos (voitti/hävisi) ja päivä agentuurin testeistä (kohta "Agentuurin testit")
- ❌ **Ei koskaan** asiakkaan omia mainoksia, nimiä, lukuja, väitteitä, materiaaleja tai tutkimusta
- ❌ Ei mainoksia, jotka "näyttävät hyviltä" mutta eivät läpäise pääsyehtoa

Kirjaston mainokset ovat kolmansien osapuolten materiaalia: vain sisäiseen analyysiin, ei koskaan sellaisenaan asiakkaan mainoksiin.

## Rakenne

| Polku | Sisältö |
|---|---|
| `_collection-log.md` | Keruukerrat: päivä, alat, hakusanat koreittain, mainostajat per kori, rajoitukset |
| `_evidence-log.md` | Jokainen kirjaston mainos näyttöineen ja tiloineen, versioparit ja pudotetut mainokset |
| `analysis-YYYY-MM-DD.md` | Mainoskohtainen komponenttihajotus, komponenttikartta ja mainostajittain pisteytetyt yhdistelmät; kuviokorttien analyysilähde |
| `ads/<ala>/` | Mainoskuva (ei gitissä) ja samanniminen sivutiedosto `.txt` (gitissä) |
| `patterns.md` | Kuvioindeksi: kaikki kortit luottamustasoineen |
| `patterns/<ID>-<nimi>.md` | Yksi kuviokortti per kuvio |
| `style/style-guide.md` | Tyylikirjasto: `S-LANG-*` (kieli) ja `S-VIS-*` (visuaalisuus) |
| `_templates/` | Kuviokortin ja tyylimerkinnän pohjat |

## Pääsyehto

Näyttö kirjataan **ennen** kuvan arviointia. Kirjastoon pääsee mainos, joka täyttää kaikki:

1. **Tavoite liidi tai myynti.** Sisältö- ja tunnettuusmainokset vain tyylimerkintöjen esimerkeiksi, merkittynä.
2. **Luokka A ja vähintään kaksi toisistaan riippumatonta signaalia:** käyttöikä vähintään 60 päivää sekä vähintään yksi näistä: monta versiota, selvästi suuri EU-tavoittavuus, idea palaa uudella kuvalla. (Pisteytys: `ad-inspiration-collection`-skilli.)
3. **Testaava mainostaja:** kymmeniä mainoksia ja uusia versioita säännöllisesti. Suurten brändien tunnettuusmainonta merkitään eikä se muodosta kuvioita.

Mainoksen tila:

| Tila | Merkitys |
|---|---|
| `Candidate` | Läpäisi pääsyehdon, ei vielä uusintatarkistettu |
| `Confirmed` | Uusintatarkistuksessa (aikaisintaan 30 pv myöhemmin) yhä käynnissä ja tavoittavuus kasvanut |
| `Stopped` | Pysähtyi pitkän käytön jälkeen; luokka alas |
| `Dropped` | Testaavan mainostajan alle ~3 viikossa pudottama: vastanäyttö (tekstirivi) |

## Kuviot ja referenssit

- **Kuvio** on abstraktio ja sen mekanismi, esim. "kysymys, joka toistaa asiakkaan epäilyn, + vastaus samassa kuvassa".
- **Referenssi** on kuvion paras esimerkki: 2–3 per kuvio, `Confirmed`-tilasta, eri mainostajilta. Irrallisia "hienoja mainoksia" ei tallenneta.

Tunnisteet: `OFF` tarjous · `ANG` kulma · `CON` creative concept · `CPY` creative copyn keino · `FMT` formaatti/layout · `S-LANG` kieli · `S-VIS` visuaalisuus.

## Luottamustasot

| Taso | Vaatimus | Käyttö asiakastyössä |
|---|---|---|
| **Candidate** | Vähintään 2 mainostajaa pääsyehdon läpäisseillä mainoksilla | Vain nimettynä testinä |
| **Supported** | Vähintään 3 mainostajaa, mieluiten 2+ alaa, vähintään 2 `Confirmed`-mainosta, pudottajia vähemmän kuin käyttäjiä | Hypoteesin perusteena |
| **Proven** | Supported + voittanut agentuurin oman testin | Oletusvalinta |
| **Fading** | Ei nähty 6 kuukauteen tai pudottajien enemmistö | Merkitään, ei suositella |

**Tason nosto ja Fading-merkintä vain käyttäjän hyväksynnällä.** Skilli ehdottaa perusteluineen, ja käyttäjä päättää.

## Käyttö asiakastyössä

Painotus: asiakkaan omat tulokset (`learnings.md`) > saman markkinan näyttö (asiakkaan keruu) > kirjasto.

- `competitor-analysis` lukee kirjaston asiakkaan ostotilanteeseen sopivat kuviot tason 3 näyttönä ja näyttää ne erikseen omasta markkinasta.
- `creative-strategy` käyttää kuvioita valikkona luottamustason mukaan; kortin `Library patterns` -kenttä nimeää tunnisteet.
- `ads-analytics` kirjaa asiakkaan raporttiin "Kirjastopalaute: `<ID>` voitti/hävisi, `<päivä>`", jonka `ad-library` kokoaa hub-istunnossa.

## Ylläpito (hub-istunnossa)

- "Kerää kirjastoon [ala]" → `ad-library` collect
- "Tarkista kirjasto" (kuukausittain) → recheck
- "Päivitä kirjaston kuviot" → synthesize (ehdotukset hyväksyttäväksi)
- "Kirjaston tila" → report
