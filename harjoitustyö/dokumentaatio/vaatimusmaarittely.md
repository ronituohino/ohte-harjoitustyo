# Vaarimusmäärittely

## Sovelluksen tarkoitus

Sovellukella käyttäjä pystyy pelamaan tunnettua Sudoku -peliä tietokoneellaan. Sovellus pitää kirjaa käyttäjän ratkaistuista sudokuista ja käyttäjän tilastoista.

## Käyttäjät

Alkuvaiheessa sovelluksella on kaksi käyttäjäroolia eli *vieraileva* ja *normaali* käyttäjä. Vieraileva käyttäjä pystyy pelaamaan Sudokua, mutta hänen tilastojaan ei tallennetta. Myöhemmin sovellukseen saatetaan lisätä suurempien oikeuksien omaava *pääkäyttäjä*.

## Sudokut

Alkuvaiheessa sovelluksella on ainoastaan ennalta määritellyt lokaalit sudokut, ja niitä voi luoda lisäämällä sudoku -määrittelytiedostoja tiettyyn kansioon. Myöhemmin sovellukseen saatetaan lisätä graafisia työkaluja sudokujen luomiseen. Myöhemmin sovellukseen saatetaan myös lisätä verkossa oleva tietokanta, josta muiden luomia sudokuja pystyy ratkaisemaan.

## Käyttöliittymäluonnos

...

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- [ ] Käyttäjä pystyy valitsemaan minkä Sudokun hän haluaa ratkaista
- [ ] Käyttäjä pystyy pelaamaan Sudokua
  - Graafinen käyttöliittymä
  - Ohjelma osaa tarkistaa Sudokun
- [ ] Käyttäjä pystyy luomaan käyttäjätunnuksen
  - Tunnuksen luominen onnistuu syöttämällä käyttäjätunnuksen, salasanan ja salasanan uudestaan
  - Käyttäjätunnuksen täytyy olla uniikki, ja sisältää ainakin kaksi merkkiä
- [ ] Käyttäjä pystyy kirjautumaan järjestelmään
  - Kirjautuminen onnistuu syöttämällä olemassa olevan käyttäjätunnus/salasana -yhdistelmän kirjautumislomakkeelle
  
### Kirjautumisen jälkeen

- [ ] Käyttäjän tilastoja kerätään Sudokuja pelatessa
  - Suoritetut Sudokut
  - Sudokujen suorittamiseen käytetty aika
  - Suoritettujen Sudokujen määrä
  - Suoritettujen Sudokujen vaikeustaso
- [ ] Käyttäjä pystyy katsomaan omia tilastojaan
- [ ] Käyttäjä pystyy kirjautumaan ulos

## Jatkokehitysideoita

Jos aikaa on vielä kätettävissä, perusversiota voidaan laajentaa seuraavilla ominaisuuksilla:

- Graafinen työkalu Sudokujen luomiseen
- Verkkotietokanta, josta Sudokuja pystyy lataamaan
- Graafinen tulostaulu kaikista kirjautuneista käyttäjistä
- Pääkäyttäjä, joka pystyy hallitsemaan verkossa olevia Sudokuja ja käyttäjiä
- Pääkäyttäjän graafiset työkalut
