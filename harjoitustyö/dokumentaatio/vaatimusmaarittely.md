# Vaarimusmäärittely

## Sovelluksen tarkoitus

Sovellukella käyttäjä pystyy pelamaan tunnettua Sudoku -peliä tietokoneellaan. Sovellus pitää kirjaa käyttäjän ratkaistuista sudokuista ja käyttäjän tilastoista.

## Käyttäjät

Alkuvaiheessa sovelluksella on kaksi käyttäjäroolia eli _vieraileva_ ja _normaali_ käyttäjä. Vieraileva käyttäjä pystyy pelaamaan Sudokua, mutta hänen tilastojaan ei tallennetta. Myöhemmin sovellukseen saatetaan lisätä suurempien oikeuksien omaava _pääkäyttäjä_.

## Sudokut

Alkuvaiheessa sovelluksella on ainoastaan ennalta määritellyt lokaalit sudokut, ja niitä voi luoda lisäämällä sudoku -määrittelytiedostoja tiettyyn kansioon. Myöhemmin sovellukseen saatetaan lisätä graafisia työkaluja sudokujen luomiseen. Myöhemmin sovellukseen saatetaan myös lisätä verkossa oleva tietokanta, josta muiden luomia sudokuja pystyy ratkaisemaan.

## Käyttöliittymäluonnos

Sovellus koostuu alustavasti neljästä näkymästä. Myöhemmin saatetaan lisätä asetusnäkymä, erillinen tilastonäkymä, tulostaulu, Sudoku -työkalu, sekä pääkäyttäjän työkalut.  
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

- [ ] Käyttäjän tilastoja kerätään Sudokuja pelatessa
  - Suoritetut Sudokut
  - Sudokujen suorittamiseen käytetty aika
- [ ] Käyttäjä pystyy katsomaan omia tilastojaan
- [x] Käyttäjä pystyy kirjautumaan ulos

## Jatkokehitysideoita

Jos aikaa on vielä kätettävissä, perusversiota voidaan laajentaa seuraavilla ominaisuuksilla:

- Erillinen tilastonäkymä
  - Suoritettujen Sudokujen määrä
  - Suoritettujen Sudokujen vaikeustaso
- Sovelluksen asetuksien graafinen muuttaminen
- Graafinen työkalu Sudokujen luomiseen
- Verkkotietokanta, josta Sudokuja pystyy lataamaan
- Graafinen tulostaulu kaikista kirjautuneista käyttäjistä
- Pääkäyttäjä, joka pystyy hallitsemaan verkossa olevia Sudokuja ja käyttäjiä
- Pääkäyttäjän graafiset työkalut
