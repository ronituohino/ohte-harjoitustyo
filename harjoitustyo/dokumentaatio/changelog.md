## Viikko 3

Sudoku -peliprojektin pohja ja perustoiminnallisuus

- Lisätty index.py, joka toimii sovelluksen aloitustiedostona ja sovelluksen pohjana
- Lisätty Sudoku -luokka, joka vastaa itse pelin ajamisesta
- Lisätty Canvas -luokka, joka vastaa käyttöliittymän tapahtumien käsittelystä
- Lisätty Button -luokka, joka toimii yleisenä nappina
- Lisätty invoke -kutsut, joilla pystyy ajamaan itse projektin, sekä testit
- Testattu Sudoku -luokan toiminnallisuus
  - Sudokun lataaminen tiedostosta
  - Sudokuruudun arvon muuttaminen
  - Sudokun ratkaisun tarkistaminen

## Viikko 4

Projektin refaktorointia, ja Sudoku -valikon toiminnallisuus

- Lisätty valikko, josta voi valita Sudokun ratkaistavaksi
- Lisätty exit -nappi, jolla pääsee takaisin valikkoon
- Pylint otettu käyttöön
- Lisätty sovellusarkkitehtuuria kuvaava luokkakaavio [arkkitehtuuri.md](arkkitehtuuri.md)
- Refaktoroitu pelisilmukka omaan Game -luokkaan
- Refaktoroitu käyttöliittymä omiin tiedostoihin ui/views -kansioon

## Viikko 5

Käyttöliittymäluokkia, kirjautuminen, rekisteröityminen ja tietokanta

- Lisätty kirjautumisnäkymä, josta pystyy kirjautumaan olemassa olevalle käyttäjälle
- Lisätty rekisteröitymisnäkymä, josta pystyy tekemään uuden käyttäjän tietokantaan
- Lisätty logout -nappi, josta kirjaudutaan ulos käyttäjätililtä
- Refaktoroitu käyttöliittymäluokkia, ja luotu uusia (text.py, textbox.py, form.py) helpottamaan työskentelyä
- Korotettu testauskattavuutta
- Lisätty kirjautumistapahtumaa kuvaava sekvenssikaavio [arkkitehtuuri.md](arkkitehtuuri.md)

## Viikko 6

Suoritettujen sudokujen esitys päävalikkoon sekä kattavan dokumentaation tuottaminen

- Lisätty suoritettujen Sudokujen tallennus tietokantaan ja esitys päävalikkoon
- Lisätty testikattavuutta
- Parannettu koodin rakennetta ja laatua
- Lisätty docstringit lähestulkoon kaikkiin luokkiin ja funktioihin
- Parannettu [arkkitehtuurikuvausta](arkkitehtuuri.md)
- Lisätty [käyttöohje](kayttoohje.md)
