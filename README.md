# Sudoku

Sovelluksella pystyy pelamaan hyvin tunnettua Sudoku -peliä paikallisesti. Sovellukseen pystyy luomaan käyttäjän jolloin se pitää kirjaa suoritetuista Sudokuista. Sovellus on luotu Pythonilla Poetry-ympäristössä, ja se käyttää pygame -kirjastoa käyttöliittymän toteutuksessa.

Sovellus on toteutettu Python -versiolla `3.8` ja muilla Python -versioilla saattaa esiintyä ongelmia.

Tämä sovellus on kurssin [Ohjelmistotekniikka 2022](https://ohjelmistotekniikka-hy.github.io/) harjoitustyö.

## Julkaisut

- [Loppupalautus](https://github.com/ronituohino/ohte-harjoitustyo/releases/tag/loppupalautus)
- [Viikko 6](https://github.com/ronituohino/ohte-harjoitustyo/releases/tag/viikko6)
- [Viikko 5](https://github.com/ronituohino/ohte-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Vaatimusmäärittely](./harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./harjoitustyo/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./harjoitustyo/dokumentaatio/changelog.md)
- [Käyttöohje](./harjoitustyo/dokumentaatio/kayttoohje.md)
- [Testidokumentti](./harjoitustyo/dokumentaatio/testaus.md)

## Asennus

Varmista, että sinulla on asennettuna Python ja sen versio on 3.8 tai uudempi.  
Varmista, että sinulla on asennettuna Poetry.

- Kloonaa tämä repo koneellesi
- Avaa terminaali ja siirry kansioon `harjoitystyö/`
- Asenna Poetry riippuvuudet komennolla `poetry install`
- Käynnistä ohjelma komennolla `poetry run invoke start`

## Komennot

### Ohjelman käynnistäminen

Ohjelman voi käynnistää tuotantomoodissa komennolla: `poetry run invoke start`  
Ohjelman voi käynnistää kehitysmoodissa komennolla: `poetry run invoke dev`

Kehitysmoodissa käytetään kehitystietokantaa, joka alustetaan testausarvoilla aina kun sovellus käynnistetään uudestaan. Tuotantotietokanta säilyttää kaikki tiedot.

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
Tämä generoi kansion `htmlcov` harjoitustyo -kansioon.  
Kattavuutta voi tarkastella avaamalla `htmlcov` -kansiosta tiedoston `index.html` selaimella.
