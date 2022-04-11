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
