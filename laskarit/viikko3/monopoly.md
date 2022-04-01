## Tehtävä 1: Monopoli

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

```mermaid
 classDiagram
			Monopoli "1" -- "1" Pelilauta
			Monopoli "1" -- "2" Noppa
			Pelilauta "1" -- "40" Peliruutu
			Peliruutu "1" -- "1" Peliruutu : Seuraava ruutu
			Pelaaja "1" -- "1" Pelinappula
			Monopoli "1" -- "2-8" Pelaaja
			Pelinappula "1" -- "1" Peliruutu

			class Monopoli { }
      class Pelilauta { }
      class Noppa { }
      class Pelaaja { }
			class Pelinappula { }
			class Peliruutu { }
```

## Tehtävä 2: Laajennettu Monopoli

Laajennetaan edellisen tehtävän luokkakaaviota tuomalla esiin seuraavat asiat:
Ruutuja on useampaa eri tyyppiä:

- Aloitusruutu
- Vankila
- Sattuma ja yhteismaa
- Asemat ja laitokset
- Normaalit kadut (joihin liittyy nimi)

Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.
Jokaiseen ruutuun liittyy jokin toiminto.
Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.
Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.
Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. Kadun voi omistaa joku pelaajista. Pelaajilla on rahaa.

```mermaid
 classDiagram
			Monopoli "1" -- "1" Pelilauta
			Monopoli "1" -- "2" Noppa
			Pelilauta "1" -- "40" Peliruutu
			Peliruutu "1" -- "1" Peliruutu : Seuraava ruutu
			Pelaaja "1" -- "1" Pelinappula
			Monopoli "1" -- "2-8" Pelaaja
			Pelinappula "1" -- "1" Peliruutu

			Pelaaja "1" -- "1" Tili
			Pelilauta --> Aloitusruutu
			Pelilauta --> Vankilaruutu
			Peliruutu "1" -- "*" Toiminto

			Ostettavaruutu --|> Peliruutu
			Katuruutu --|> Ostettavaruutu
			Asemaruutu --|> Ostettavaruutu
			Aloitusruutu --|> Peliruutu
			Vankilaruutu --|> Peliruutu
			Sattumaruutu --|> Peliruutu
			Yhteismaaruutu --|> Peliruutu

			Sattumaruutu "1" -- "*" Kortti
			Yhteismaaruutu "1" -- "*" Kortti
			Kortti "1" -- "1" Toiminto

			Katuruutu "1" -- "1" Rakennus
			Talo "1" -- "1" Rakennus
			Hotelli "1" -- "1" Rakennus
			Pelaaja "1" -- "*" Ostettavaruutu

			class Monopoli { }
      class Pelilauta { }
      class Noppa { }
      class Pelaaja { }
			class Pelinappula { }
			class Peliruutu { }

			class Tili { }
			class Ostettavaruutu { }
			class Katuruutu {
				rakennus_taso : int
			}
			class Asemaruutu { }
			class Aloitusruutu { }
			class Vankilaruutu { }
			class Sattumaruutu { }
			class Yhteismaaruutu { }

			class Kortti { }
			class Toiminto { }

			class Rakennus { }
			class Talo { }
			class Hotelli { }
```

> Written with [StackEdit](https://stackedit.io/).
