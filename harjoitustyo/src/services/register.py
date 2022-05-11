from utils.validation import (
    username_validation,
    password_validation,
    password_again_validation,
)


class Register:
    """Luokka, joka hallitsee rekisteröitymisnäkymän toimintoja

    Attributes:
        game: Peliluokan referenssi
        username: Tekstikenttään annettu käyttäjänimi
        password: Tekstikenttään annettu salasana
        password_again_ Tekstikenttään annettu salasana uudestaan
    """

    def __init__(self, game):
        """Luokan konstruktori

        Args:
            game: Peliluokan referenssi
        """

        self.game = game
        self.username = None
        self.password = None
        self.password_again = None

    def __name__(self):
        return "Register"

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
        err = password_again_validation(self.password, self.password_again)
        if len(err) > 0:
            errors["password_again"] = err
        return errors

    def register(self):
        """Aktivoi rekisteröitymistapahtuman: validointi, rekisteröityminen

        Returns:
            Virhetaulukon jos on virheitä,
            None jos ei ole virheitä
        """

        errors = self.validate()

        if len(errors.keys()) > 0:
            return errors

        result = self.game.database.create_account(
            self.username, self.password)
        if not result:
            return {"register": "Username already taken"}

        self.game.user = result
        self.game.open_menu()
        return None

    def open_menu(self):
        """Kutsuu peliluokan open_menu() -funktiota"""

        self.game.open_menu()

    def open_login(self):
        """Kutsuu peliluokan open_login() -funktiota"""

        self.game.open_login()
