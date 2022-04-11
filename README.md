# Sudoku

Sovelluksella pystyy pelamaan hyvin tunnettua Sudoku -peliä paikallisesti. Sovellus on luotu Pythonilla Poetry-ympäristössä, ja se käyttää pygame -kirjastoa käyttöliittymän toteutuksessa.

Sovellus on toteutettu Python -versiolla `3.8` ja muilla Python -versioilla saattaa esiintyä ongelmia.

Tämä sovellus on kurssin [Ohjelmistotekniikka 2022](https://ohjelmistotekniikka-hy.github.io/) harjoitustyö.

## Dokumentaatio

- [Vaatimusmäärittely](./harjoitustyö/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./harjoitustyö/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./harjoitustyö/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./harjoitustyö/dokumentaatio/changelog.md)

## Asennus

Varmista, että sinulla on asennettuna Python ja sen versio on `3.8` tai uudempi.  
Varmista, että sinulla on asennettuna Poetry.  

- Kloonaa tämä repo koneellesi
- Avaa terminaali ja siirry kansioon `harjoitystyö/`
- Asenna Poetry riippuvuudet komennolla `poetry install`
- Käynnistä ohjelma komennolla `poetry run invoke start`

## Komennot

### Ohjelman käynnistäminen

Ohjelman voi käynnistää komennolla: `poetry run invoke start`

### Linttaus & formatointi

Ohjelman voi ajaa Pylintin läpi komennolla: `poetry run invoke lint`  
Tämä antaa arvion koodin laadusta.

Ohjelman koodin voi formatoida autopep8 avulla komennolla: `poetry run invoke format`  
Tämä ajaa koodin autopep8 formatointiohjelman läpi, kommennosta ei ole tulostetta.

### Testaus

Testit voi ajaa komennolla: `poetry run invoke test`

### Testikattavuus

Testikattavuuden voi generoida komennolla: `poetry run invoke coverage`  
Tämä generoi `.coverage` -tiedoston harjoitystyö -kansioon.

Testikattavuudesta voi myös generoida HTML -tiedoston komennolla: `poetry run invoke coverage-report`  
Tämä generoi kansion `htmlcov` harjoitustyö -kansioon.  
Kattavuutta voi tarkastella avaamalla `htmlcov` -kansiosta tiedoston `index.html` selaimella.
