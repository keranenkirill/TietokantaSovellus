# OT-P 
[OT-P kirjanpito & työtila](https://github.com/KeranenKirill/OT-P/blob/main/DOKUMENTAATIO/TYOAIKAKIRJANPITO.md)
  
    
# Vaatimusmäärittely
## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tarjota käyttäjälle keskusteluketju-alusta, jossa voidaan käsitellä eri puheenaiheita.

## Perusversion toiminallisuudet nykyhetkellä (24.07.2023)

- Sovellus toimii paikallisesti
- Käyttäjä voi kirjautua palveluun tai luoda uuden käyttäjä-tilin 
   - Luodessaan käyttäjä-tiliä, käyttäjä voi asettaa:
      - etunimen, sukunimen, iän, kotikaupunginsa, käyttäjänimen, salasanan (lisäksi vahvistetaan sala sana toiseen otteeseen)
      - luontivaiheessa, mikäli käyttäjä jättää kohdat täyttämättä, tai kirjoittaa väärin, niin aiheutuu virhe-viestit (kaupunkien kohdalla input- muutetaan valinta-toiminnaksi seuraavissa päivityksissä)
- Salasanat muutetaan hash-muotoon
- Uloskirjautuminen ja sisäänkirjautuminen luoduilla käyttäjillä
- Kaksi tietokanta-taulua:
   - otp_users
   - otp_users_info
  

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




