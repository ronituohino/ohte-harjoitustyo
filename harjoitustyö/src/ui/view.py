# Parent class for game views
class View:
    """Luokka, jonka kaikki näkymäluokat perivät, ja ylikirjoittavat tick() -metodin"""

    def tick(self, screen, screen_dimensions):
        """Kutsutaan käyttöliittymän päivittämisen / piirtämisen yhteydessä"""
        pass
