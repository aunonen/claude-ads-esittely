# Keruuloki

Jokainen kirjaston keruu- ja tarkistuskerta. Uusin ylimpänä.

| Päivä | Tila (collect / recheck) | Alat | Hakusanat koreittain (map / discover / snowball / validate) | Mainostajia per kori | Uusia mainoksia | Rajoitukset |
|---|---|---|---|---|---|---|
| 2026-10-26 | collect | Kotipalvelut ja remontit: katot, ikkunat, kylpyhuoneet, lämmitys/energia, kotisiivous; lisäksi salaojien ja julkisivujen kartoitus | map: kattoremontti, lämpöpumppu, ikkunaremontti, kylpyhuoneremontti, salaojaremontti, julkisivuremontti, siivouspalvelu, aurinkopaneelit; discover: omakotitalo, talveen, kodin kunnossapito; snowball: huoltosuunnitelma, testisiivous; validate: ei hakuja | Mainostajasivuista map 16, discover 1, snowball 0 uutta tarkistettua; yhteensä 17, joista 10:llä testausnäyttöä | 10 (A 10, B/C 0; Quote request 10; Candidate 10), seitsemältä mainostajalta | Suurten sivujen teksti ja inaktiivihistoria jäivät osin otoksiksi; 192 inaktiivista korttia luettu / 136 alkoi 12 kk sisällä; ei vahvistettuja Dropped-rivejä tai versiopareja. Lopussa net::ERR_CONNECTION_CLOSED. Kahdessa dynaamisessa mainoksessa päätekstiä ei näytetä. |

## Synteesi 26.10.2026

Käyttäjän keruun jälkeinen jatkopyyntö: hajota mainokset komponentteihin ja etsi kuviot niiden sekä yhdistelmien perusteella. [Analyysiraportti](analysis-2026-10-26.md) sisältää kaikkien 10 kuvan tekstit ja visuaalisen analyysin, komponenttikartan sekä reseptin jokaiselle mainokselle. Laskentayksikkö on mainostaja, ei mainosmäärä.

Luotu kuusi Candidate-korttia: OFF-001 (4 mainostajaa), ANG-001 (2), CON-001 (5), CPY-001 (4), CPY-002 (2), FMT-001 (3). Vahvin kuvattu yhdistelmä: tila tai tekijä näyttämönä × maksuton asiantuntija-arvio, 4 A-mainostajaa / +8; kyse on testihypoteesista. Kymen kaksi ja LämpöYkkösen kolme kuvaa eivät moninkertaista mainostajapisteitä.

Käyttäjä ilmoitti, ettei Kirjastopalaute-rivejä ole. Agentuurin testit 0; Confirmed-mainokset 0; referenssit 0; tyylimerkinnät 0. Supported-/Proven-tasolle nostamista ei ehdoteta. Aiemman keruun inaktiiviotoksen rajat säilyvät; puuttuvaa vastanäyttöä ei tulkita voitoksi. Kuvioindeksi päivitetty; ei tasomuutoksia tai git-committia.

## Lumipallosanat

Kerätyistä mainoksista löytyneet sanat ja ilmaisut, ja onko niillä haettu.

| Päivä | Sana tai ilmaisu | Mistä mainoksesta | Haettu? |
|---|---|---|---|
| 2026-10-26 | huoltosuunnitelma | Kymen Kattokeskus, 1607713493817196 ja 912424291580816 | Kyllä; löytyi saman mainostajan pitkäikäisiä mainoksia, ei uutta tarkemmin tarkistettua mainostajaa |
| 2026-10-26 | testisiivous | Ametro.fi, 1313808140362787 | Kyllä; jatkojonoon Kotova ja Nordicshine Oy, ei tallennuksia niiltä |
| 2026-10-26 | ehjä ikkuna ei ole sama kuin toimiva ikkuna | Pihla, 2016151809271288 (kuvateksti) | Ei |
| 2026-10-26 | asiantuntija maksutta käyttöösi | Tiivi, 1211962417654236 (kuvateksti) | Ei |

## 26.10.2026 — rajaus, havainnot ja kattavuus

Käyttäjä laajensi alkuperäisen energia- ja lämmitysremonttirajauksen kotipalveluihin ja remontteihin. Maa Suomi, staattiset mainokset, tarjouspyyntö / kartoitus / ajanvaraus / palvelun osto. Mukana myös jatkuva kotisiivous; yhden siivouskäynnin hintaa ei rinnasteta suuren remontin hintaan. Ostotilanteiden hintatasot jätettiin tuntemattomiksi, ellei mainos niitä kertonut. Päätöspituudet ovat tulkintoja.

### Hakukorit

- **map:** 8 neutraalia kategoriasanahakua (62 % kategoriasanahauista); mainostajasivuille siirryttiin Metan hakuehdotusten kautta. Sivujen nimet eivät ole uusia kulmahypoteeseja.
- **discover:** 3 hakua (23 %): omakotitalo, talveen, kodin kunnossapito. Omakotitalo toi LämpöYkkösen; talveen toi Max’s Energyn jatkoehdokkaaksi. Kodin kunnossapito ei tuonut tuloksia. Max’s Energyn mainostajaprofiilia ei saatu valittua eikä siitä tallennettu mainoksia.
- **snowball:** 2 hakua (15 %): mainoksista löytyneet huoltosuunnitelma ja testisiivous. Testisiivoushaussa uudet jatkoehdokkaat Kotova ja Nordicshine Oy; ensimmäisen näkyvän otoksen Kotova-mainokset olivat videoita ja Nordicshine hyvin tuore. Kodinhoitaja Päiväksi oli näkynyt jo map-haussa.
- **validate:** 0 hakua. Tyhjässä kuvioindeksissä ei ollut testattavia hypoteeseja. Prosentit koskevat 13 kategoriasanahakua; mainostajaprofiilien valintoja ei lasketa uusiksi kategoriasanahauiksi.

### Mainostajasivujen tarkistus

Tulosten määrä on Metan ilmoittama likimääräinen luku, ei itsenäisten ideoiden tai kuvien määrä. Saman konsernin/nimen mahdolliset eri sivut erotettiin hakuehdotuksista. Tekstinä luettiin näkyvät mainoskortit; lisätuloksia ladattiin suurilta sivuilta, mutta kaikkien sivujen koko sisältöä ei saatu luettua.

| Mainostaja | Löytyi | Aktiivisia tuloksia noin | Testausnäyttö | Tallennettu | Ratkaisu / rajoitus |
|---|---|---:|---|---:|---|
| Järki-Saneeraus Oy | map: kattoremontti | 1 | Riittämätön tässä otoksessa | 0 | Mainos 1762347901468597: 61 pv, neljä versiota, EU reach 98 436; yksi aktiivinen mainos ei vahvistanut vaadittua laajaa testausta. |
| Kylpyri | map: kylpyhuoneremontti | 22 | Kyllä | 1 | Kartoitusmainos, 3 versiota; uudet julkaisut heinä–lokakuussa. |
| Ametro.fi | map: siivouspalvelu | 21 | Kyllä | 1 | Pitkäikäinen testisiivousmainos, 10 versiota; jatkuvan palvelun ostotilanne merkitty erikseen. |
| Ikkunasepät Oy | map: ikkunaremontti | 5 | Riittämätön tässä otoksessa | 0 | Pitkiä ajoja ja versioita, mutta laajan testaajan ehto ei vahvistunut. Ei väitettä heikosta tuloksesta. |
| Tapijola-ikkunat | map: ikkunaremontti | 6 | Riittämätön tässä otoksessa | 0 | Pitkä käyttöikä yksin ei riitä; aktiivisia vanhoja mainoksia ei rajattu pois niiden aloitusvuoden perusteella. |
| Remontti Rex Oy | map: kylpyhuoneremontti | 4 | Riittämätön tässä otoksessa | 0 | Uudehko, samana päivänä alkanut pieni joukko; ei vahvistettua testaushistoriaa. |
| Kymen Kattokeskus | map: kattoremontti | 31 | Kyllä | 2 | Pinnoitus vs remontti sekä arvaus vs huoltosuunnitelma; molemmissa 4 versiota. |
| Restak Fi | map: kattoremontti | 6 | Riittämätön tässä otoksessa | 0 | Pitkät ajot, mutta testaajan laajuusehto jäi vahvistamatta. |
| TCL-tekniikka | map: lämpöpumppu | 9 | Riittämätön tässä otoksessa | 0 | Useita tuotteita ja versioita; kymmenien mainosten testausta ei vahvistettu. |
| Uudenmaan Aurinkovoima Oy | map: aurinkopaneelit | 8 | Riittämätön tässä otoksessa | 0 | Pitkiä tarjous- ja arvontamainoksia, mutta testaajan laajuusehto ei vahvistunut. |
| 1KOMMA5 Suomi | map: aurinkopaneelit | 18 | Kyllä, lisäksi noin 160 inaktiivista tulosta | 1 | Kesä–lokakuun lisäetuversiot + kymmenien mainosten historia. Aktiivimäärästä ei kokeneen mainostajan lisäpistettä. |
| Tiivi | map: ikkunaremontti | 51 | Kyllä | 1 | Valtakunnallinen brändi; valittiin konkreettinen maksuton kartoitus. Päätekstiä ei näytetty. |
| Pihla | map: ikkunaremontti | 48 | Kyllä | 1 | Valtakunnallinen brändi; valittiin arviokäynnin varaus. Rahoitusartikkeli, taloyhtiöartikkeli ja arvonnat jäivät pois. Päätekstiä ei näytetty. |
| Vesivek | map: kattoremontti / salaojaremontti | 36 | Kyllä | 0 | Tarkistetut staattiset liidi- ja tarjousmainokset pääosin alle 60 pv. Tunnettuus, oppaat ja rekrytointi rajattiin pois. Koko historiaa ei luettu. |
| Itä-Helsingin Lasi Oy | map: julkisivuremontti | 33 | Kyllä | 0 | Saunalasitus 2245077822668965: 459 pv, 2 versiota, reach 11 340. Uudemmassa 1230952615095799 sama kohdekuva ilman tekstipeittoa; paluusignaalia ei laskettu. 4 p / B, ei tallennusta. |
| LämpöYkkönen Oy | discover: omakotitalo | 64 | Kyllä | 3 | Tarjouspyyntö, hintalaskuri ja huolto ovat eri ostotilanteita. Mainostajakohtainen 3 mainoksen katto täynnä. Valtakunnallisen toimijan sisältömainoksia ei tallennettu. |
| Koti Puhtaaksi Oy | map: siivouspalvelu | 38 | Kyllä | 0 | Luetut staattiset mainokset liian tuoreita tai sisältöä/arvontoja. Inaktiivihaku katkesi yhteysvirheeseen. |

Yhteensä **17 mainostajaprofiilia**, joista **10 täytti tarkastelussa testaajan tunnusmerkit**. Tallenteita 7 mainostajalta. Kartoitustavoite 10–15 testaavaa mainostajaa saavutettiin alarajalta; mainostajien määrä ei ole tallennettujen tai toimiviksi todistettujen mainosten määrä.

### Inaktiiviset mainokset ja vastanäyttö

Raja: aloittanut 26.10.2025 tai myöhemmin. Käyttöikä on lopetus- ja aloituspäivän erotus. Vanhempia kortteja näkyi samalla sivulla, mutta niitä ei käytetä tämän 12 kuukauden otoksen vastanäyttönä. Alle 21 päivän ajo ei yksin riitä Dropped-luokitukseen.

| Mainostaja | Luettuja inaktiivisia kortteja | Aloitti 12 kk sisällä | Näistä ≤21 pv | Kattavuus |
|---|---:|---:|---:|---|
| Kylpyri | 21 | 21 | 9 | Otos, kirjastossa noin 43 inaktiivista tulosta; ryhmittely voi yhdistää useita mainoksia. |
| Ametro.fi | 28 | 19 | 0 | Otos, noin 52 tulosta. |
| Kymen Kattokeskus | 21 | 11 | 2 | Otos, noin 87 tulosta; lyhyet havaitut jaksot rekrytointia. |
| Tiivi | 27 | 23 | 1 | Otos; lyhyt havainto arvontamainos, ei vahvistettu hävinneeksi ideaksi. |
| Pihla | 29 | 18 | 1 | Otos, noin 470 tulosta; lyhyt havainto arvontamainos. |
| 1KOMMA5 Suomi | 27 | 27 | 6 | Otos, noin 160 tulosta; joukossa webinaarien määräaikoihin päättyneitä ajoja, rekry ja sisältömainos. |
| LämpöYkkönen Oy | 39 | 17 | 1 | Otos, noin 720 tulosta; lyhyt 40 kk rahoituskampanja jäi ilman riittävää määräaika- ja jatkoversiotarkistusta. |
| **Yhteensä** | **192** | **136** | **20** | **Ei kattava selvitys.** |

**Dropped 0 vahvistettua, versiopareja 0 vahvistettua.** Tämä ei tarkoita, ettei mainostajilla olisi hävinneitä testejä. Esimerkiksi Kylpyrin heinäkuun lyhyitä ideoita palasi myöhemmin, ja heinäkuun etua jatkettiin kesäetuna: niitä ei kirjattu suoraan hävinneiksi. Kymen pinnoitusmainoksen 42 päivän rinnakkaisajo 2123107584929179 havaittiin, mutta kuvaeroa ei varmistettu eikä sitä luokiteltu lyhyeksi pudotukseksi.

### Tallennusten jakauma ja rajoitukset

- 10 alkuperäistä JPEG-kuvaa + 10 samannimistä tekstisivutiedostoa + 10 näyttölokin riviä.
- Alat: kylpyhuone/sauna 1, kotisiivous 1, kattopalvelut 2, ikkunat/ovet 2, energia- ja lämpöpumppupalvelut 4.
- Kaikki A-luokkaa ja liidi-/tarjouspyyntö-/ajanvarauspolkuja; 0 sisältö- tai tunnettuusmainosta, 0 videoita. Kuvia arvioitiin vasta alustavan pisteytyksen jälkeen.
- Pääteksti puuttuu Metan näkyvästä näkymästä 2 tallenteessa (Tiivi, Pihla). Kuvan tekstiä ei keksitty päätekstiksi.
- Kaikista 10 tallennetusta mainoksesta luettiin EU-tavoittavuus ja kohdennus yksityiskohdista 26.10.2026. Tavoittavuus on arvio; ei kulutietoa, liidimäärää, ROASia tai kannattavuusnäyttöä.
- Isojen sivujen automaattinen lisälataus ja vaihtuvat tulosryhmät rajoittivat tekstilukujen kattavuutta. Koti Puhtaaksi -inaktiivihaku päättyi lopuksi virheeseen `net::ERR_CONNECTION_CLOSED`. Vesivekin, Itä-Helsingin Lasin ja Koti Puhtaaksi -yrityksen inaktiiveista ei tehty kattavaa arviota. Niiltä ei tallennettu mainoksia.
- Uusintatarkistamaton aineisto: kaikki tallenteet Candidate. Keruuvaiheessa ei muodostettu kuvioita; saman päivän myöhempi synteesi loi kuusi Candidate-korttia (yllä). Ei Confirmed-referenssejä, tyylimerkintöjä tai tasomuutoksia. Ensimmäinen mahdollinen 30 päivän uusintatarkistuspäivä 25.11.2026.
- Keittiö-, maalaus-, lattia- ja piharemontit eivät kuuluneet tämän kierroksen erillisiin hakuihin. Salaojista ja julkisivuista tehtiin kartoitus, mutta niistä ei lisätty pääsyehdon läpäisseitä mainoksia.
- Mainostajien väitteet ovat analysoitavaa julkista mainossisältöä; niitä ei saa siirtää asiakkaan väitteiksi. Ei asiakaskansioiden lukemista tai käyttöä, ei yhteydenottoja mainostajiin, ei lomakkeita täytetty, ei julkaisuja eikä git-committia.
