from utils.sudoku import sudokus_in_folder


class Menu:
    """Luokka, joka hallitsee päävalikon toiminnallisuuksia

    Attributes:
        game: Peliluokan referenssi
        sudokus: Sudoku -kansiossa olevat sudokut
        selected_sudoku: Valikossa valitun sudokun indeksi

        completed_data: Sudokujen suoritusdata: [("nimi", "suoritusaika")]
        completed_sudokus: Lista suoritetuista sudokuista: ["nimi1", "nimi2"]
    """

    def __init__(self, game, sudoku_folder_path):
        """Luokan konstruktori, hakee sudokutiedostot kansiosta ja suoritusdatan tietokannasta

        Args:
            game: Peliluokan referenssi
            sudoku_folder_path: Sudokukansion polku
        """

        self.game = game

        self.sudokus = sudokus_in_folder(sudoku_folder_path)
        self.selected_sudoku = 0
        self.sudoku_amount = len(self.sudokus)

        if self.game is not None and self.game.user is not None:
            self.completed_data = self.get_completed_data()
            self.completed_sudokus = [t[0] for t in self.completed_data]
        else:
            self.completed_data = []
            self.completed_sudokus = []

    def get_completed_data(self):
        return self.game.database.get_completed_data(self.game.user["id"])

    def __name__(self):
        return "Menu"

    def move_left(self):
        """Siirtää valittua sudokua vasemmalle"""

        if self.selected_sudoku > 0:
            self.selected_sudoku -= 1

    def move_right(self):
        """Siirtää valittua sudokua oikealle"""

        if self.selected_sudoku < self.sudoku_amount - 1:
            self.selected_sudoku += 1

    def open_sudoku(self):
        """Avaa valitun sudokun"""

        self.game.open_sudoku(self.sudokus[self.selected_sudoku])

    def open_login(self):
        """Avaa kirjautumisnäkymän"""

        self.game.open_login()

    def logout(self):
        """Kirjaa käyttäjän ulos ja tyhjentää suoritusdatan"""

        self.completed_data = []
        self.completed_sudokus = []
        self.game.logout()
