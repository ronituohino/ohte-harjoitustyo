from utils.validation import username_validation, password_validation


class Login:
    """Luokka, joka hallitsee kirjautumisnäkymän toimintoja

    Attributes:
        game: Peliluokan referenssi
        username: Tekstikenttään annettu käyttäjänimi
        password: Tekstikenttään annettu salasana
    """

    def __init__(self, game):
        """Luokan konstruktori

        Args:
            game: Peliluokan referenssi
        """

        self.game = game
        self.username = None
        self.password = None

    def __name__(self):
        return "Login"

    # Pylint complains about similar lines here and in register.py, (also validate())
    # However, both of these functions should remain unique
    # R0801 = Similar lines in %s files

    # pylint: disable=locally-disabled, R0801
    def validate(self):
        """Validoi syötetyt tiedot

        Returns:
            Virhetaulukon jos on virheitä,
            Tyhjä taulukko jos ei ole virheitä
        """

        errors = {}
        err = username_validation(self.username)
        if len(err) > 0:
            errors["username"] = err
        err = password_validation(self.password)
        if len(err) > 0:
            errors["password"] = err
        return errors

    def login(self):
        """Aktivoi kirjautumistapahtuman: validointi, kirjautuminen

        Returns:
            Virhetaulukon jos on virheitä,
            None jos ei ole virheitä
        """

        errors = self.validate()

        if len(errors.keys()) > 0:
            print(errors)
            return errors

        result = self.game.database.login(self.username, self.password)
        if not result:
            return {"login": "Username or password invalid"}

        self.game.user = result
        self.game.open_menu()
        return None

    def open_menu(self):
        """Kutsuu peliluokan open_menu() -funktiota"""

        self.game.open_menu()

    def open_register(self):
        """Kutsuu peliluokan open_register() -funktiota"""

        self.game.open_register()
