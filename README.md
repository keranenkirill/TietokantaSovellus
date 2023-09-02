# OT-P 
[OT-P kirjanpito & työtila](https://github.com/KeranenKirill/OT-P/blob/main/DOKUMENTAATIO/TYOAIKAKIRJANPITO.md)
  
    
# Vaatimusmäärittely
## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tarjota käyttäjälle keskusteluketju-alusta, jossa voidaan käsitellä eri puheenaiheita.

## Perusversion toiminallisuudet (26.08.2023) 
Projektin kehityksen säänöllisyys vähenee toisten kurssien takiatoistaiseksi (alkaen 4.9.2023). Tarkoituksena kuitenkin lisätä uusia toiminallisuuksia samalla ylläpitäen ohjelmointi aktiivisuutta.


(tämä kappale päivitetään projektin edetessä)

- Sovellus toimii paikallisesti
- Käyttäjä voi kirjautua palveluun tai luoda uuden käyttäjä-tilin 
   - Luodessaan käyttäjä-tiliä, käyttäjä voi asettaa:
      - etunimen, sukunimen, iän, kotikaupunginsa, käyttäjänimen, salasanan (lisäksi vahvistetaan sala sana toiseen otteeseen)
      - luontivaiheessa, mikäli käyttäjä jättää kohdat täyttämättä, tai kirjoittaa väärin, niin aiheutuu virhe-viestit (kaupunkien kohdalla input- muutetaan valinta-toiminnaksi seuraavissa päivityksissä)
      - Salasanat muutetaan hash-muotoon
- Uloskirjautuminen ja sisäänkirjautuminen luoduilla käyttäjillä
- Kun käyttäjä on kirjautunut, avautuu näkymä, jossa voidaan luoda keskusteluketju
   - keskusteluketjun luomiseen tarvitaan puheenaihe (topic), sekä ensimmäinen kommentti (kesksutelun luojan on myös aloitettava keskustelu)
- Ensimmäinen keskusteluketju renderöityy etusivulle
   - käyttäjä näkee tällöin puheenaiheen, ensimmäisen kommentin, kseskusteluketjun luoneen käyttäjänimen, sekä redirect -linkin.
- Redirect -linkki etusivulla johta keskusteluketjuun, jossa näkyy aihe, mahdollisuus lisätä kommentti, sekä keskusteluketjun kaikki kommentit. (uusin kommentti alhaalla)
- Kommenteille on mahdollista antaa joko positiivinen tykkäys tai negatiivinen tykkäys
   - käyttäjä ei voi antaa monta tykkäystä peräkkäin
- käyttäjällä on oma etusivu, jossa:
   - mahdollisuus tarkastella kaikkia omia puheenaiheita ja kommentteja, sekä näiden kautta pääsy tarkastelemaan koko keskusteluketjua
   - toiminallisuus muokata tietojaan (etunimi, sukunimi, ikä, kaupunki ja käyttäjänimi) 

- Neljä tietokanta-taulua:
   - otp_users
   - otp_topics
   - otp_comments
   - otp_user_reactions


  

## Perusversion tavoite-toiminallisuudet

- Sovellus toimii kehitysvaiheen alussa paikallisesti, mutta tarkoituksena on saada se palvelimelle (Fly.io)
- Käyttäjä voi kirjautua palveluun tai luoda tilin suojatulla salasanalla (hash)
- Luodessaan tilin, käyttäjä voi asettaa:
   - käyttäjänimen
   - salasanan (sekä salasanan vahvistaminen)
   - paikkakunnan (tämän perusteella voidaan suodattaa paikkakunnittain muiden jäsenien julkaisuja)
- kun käyttäjä on kirjautunut, palvelun etusivulla näkyvät kesksusteluaiheet, joiden keskusteluketjuihin pääsee käsiksi
- palvelun etusivulta löytyy myös mahdollisuus luoda uusi keskusteluaihe
   - luodessaan keskusteluaiheen, on samalla lisättävä aloitusteksti
- palvelun etusivulta pääsee omalle sivulle, jossa näkyy omat tykätyt kommentit/keskusteluaiheet, sekä itse luodut keskusteluaiheet tai kommentit muiden kesksuteluissa
- palvelun etusivulla myös toiminallisuus, jossa näkyy suosituimmat puheenaiheet paikkakunnan, tykkäysten, sekä kommenttien määrän mukaan
- palvelun etusivulla toiminallisuus, jolla voi hakusanalla hakea keskusteluaiheita ja keskusteluja

### Tuotannon kehitysideoita/ -taskeja
- mahdollisuus muuttaa omaa salasanaa
- käyttäjän etusivun kommenttien ja puheenaiheiden looginen esitystapa
- palvelun etusivulle mahdollisuus sorttaamaan keskusteluketjujen näkymiä
- kuvien lisäämisen mahdollistaminen keskusteluketjuihin
- visuaalisia parannuksia

