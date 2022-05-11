# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellukella käyttäjä pystyy pelamaan tunnettua Sudoku -peliä tietokoneellaan. Sovellus pitää kirjaa kirjautuneen käyttäjän ratkaistuista sudokuista ja niiden suoritusajoista.

## Käyttäjät

Sovelluksella on kaksi käyttäjäroolia eli _vieraileva_ ja _normaali_ käyttäjä. Vieraileva käyttäjä pystyy pelaamaan Sudokua, mutta hänen Sudokujen suoritustietoja ei tallennetta.

## Sudokut

Sovelluksella on `sudokus/` kansiossa määritellyt lokaalit sudokut, ja niitä voi luoda lisää millä tahansa tekstieditorilla.

## Käyttöliittymäluonnos

Sovellus koostuu alustavasti neljästä näkymästä:

- Päävalikko
- Sudoku pelinäkymä
- Kirjautumislomake
- Rekisteröitymislomake

Sovelluksen kehityksen alussa tehty suunnitelma käyttöliittymästä
![Luonnos](./kuvat/luonnos.jpg)

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- [x] Käyttäjä pystyy valitsemaan minkä Sudokun hän haluaa ratkaista
- [x] Käyttäjä pystyy pelaamaan Sudokua
  - Graafinen käyttöliittymä
  - Ohjelma osaa tarkistaa Sudokun
- [x] Käyttäjä pystyy luomaan käyttäjätunnuksen
  - Tunnuksen luominen onnistuu syöttämällä käyttäjätunnuksen, salasanan ja salasanan uudestaan
  - Käyttäjätunnuksen täytyy olla uniikki, ja sisältää ainakin kaksi merkkiä
- [x] Käyttäjä pystyy kirjautumaan järjestelmään
  - Kirjautuminen onnistuu syöttämällä olemassa olevan käyttäjätunnus/salasana -yhdistelmän kirjautumislomakkeelle

### Kirjautumisen jälkeen

- [x] Käyttäjän tilastoja kerätään Sudokuja pelatessa
  - Suoritetut Sudokut
  - Sudokujen suorittamiseen käytetty aika
- [x] Käyttäjä pystyy katsomaan omia tilastojaan
- [x] Käyttäjä pystyy kirjautumaan ulos

## Jatkokehitysideoita

Perusversiota voidaan mahdollisesti laajentaa seuraavilla ominaisuuksilla:

- Erillinen tilastonäkymä
  - Suoritettujen Sudokujen määrä
  - Suoritettujen Sudokujen vaikeustaso
- Sovelluksen asetuksien graafinen muuttaminen
- Graafinen työkalu Sudokujen luomiseen
- Verkkotietokanta, josta Sudokuja pystyy lataamaan
- Graafinen tulostaulu kaikista kirjautuneista käyttäjistä
- Pääkäyttäjä, joka pystyy hallitsemaan verkossa olevia Sudokuja ja käyttäjiä
- Pääkäyttäjän graafiset työkalut
