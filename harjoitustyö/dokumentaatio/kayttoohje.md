# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/ronituohino/ohte-harjoitustyo/releases/tag/viikko6).

## Konfigurointi

**tulossa**

## Vaatimukset

Varmista, että sinulla on asennettuna Python ja sen versio on 3.8 tai uudempi.  
Varmista, että sinulla on asennettuna Poetry.

## Ohjelman käynnistäminen

Asenna ensiksi ohjelman riippuvuudet komennolla:

```
poetry install
```

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

Ohjelma avautuu päävalikkoon.

## Pelaaminen

Voit valita pelattavan Sudokun klikkaamlla ruudun alhaalla olevia näppäimiä `<-` ja `->`. Avaa Sudoku painamalla nappia `Play`.

### Sudoku

Peliin avautuu Sudoku -ikkuna ja palkki valittavia numeroita.
Voit sijoittaa numeron ruudukkoon ensiksi klikkaamalla oikealta palkista haluamasi numeron, ja sitten klikkaamalla ruudukkoa.

Tarkoituksena on täyttää Sudoku -ruudukko siten, että jokaisessaa 3x3 ruudukossa ja vaaka- ja pystyrivissä on kaikki numerot välillä 1-9 tasan yhden kerran. Jos Sudoku on ratkaistu oikein, alas ilmestyy teksti "Congratulations".

## Käyttäjän luominen

Voit luoda käyttäjän peliin jolloin ratkaistut sudokut, ja niihin käytetty aika, kirjataan ylös.

Käyttäjän pystyy luomaan päävalikosta painamalla ensin nappia "Login", ja sen jälkeen nappia "New user?". Kenttiin pystyy kirjoittamaan painamalla niitä ensin hiirellä ja sen jälkeen naputtelemalla näppäimistöllä.

Paina nappia "Register", kun kentät ovat täynnä. Jos mitään ei tapahdu, käyttäjänimesi on jo käytössä.

## Kirjautuminen

Voit kirjautua käyttäjälle menemällä "Login" näkymään ja täyttämällä käyttäjänimen ja salasanan.

Kirjaudu sisään painamalla "Login" nappia. Jos mitään ei tapahdu, käyttäjänimi tai salasana on väärin.

## Uloskirjautuminen

Voit kirjautua ulos painamalla päävalikossa olevaa nappia "Logout". Nappi näkyy ainoastaan jos olet kirjautunut jo sisään.
