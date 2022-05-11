import time
from utils.sudoku import parse_sudoku_file


class Sudoku:
    """Luokka, joka hallitsee Sudoku -pelin toimintaa

    Attributes:
        game: Peliluokan referenssi
        sudoku_name: Tämän sudokun nimi
        time_start: time.time() ajankohta pelin alkaessa
        completion_time: None pelin suorituksen aikana,
            kun Sudoku on valmis, sisältää time.time() ajankohdan
        grid: Sudokun numerot: [(0-9) * 9 * 9]
        selection_value: Asetettavan numeron arvo
        solved: False jos Sudoku ei ole ratkaistu, True jos on
    """

    def __init__(self, game, sudoku_folder_path, sudoku_name) -> None:
        """Luokan konstruktori, lataa Sudokun tiedostosta ja alustaa muuttujat

        Args:
            game: Peliluokan konstruktori
            sudoku_folder_path: Polku Sudoku -kansioon
            sudoku_name: Sudokun nimi kansiossa
        """

        self.game = game
        self.sudoku_name = sudoku_name
        self.time_start = time.time()
        self.completion_time = None

        string = parse_sudoku_file(sudoku_folder_path, sudoku_name)

        # Init board data
        self.grid = [int(c) for c in string]
        self.immutable = [int(c) != 0 for c in string]
        self.selection_value = 1
        self.solved = False

    def __name__(self):
        return "Sudoku"

    # Set value in sudoku board to selection_value
    def set_value(self, coords: tuple) -> None:
        """Asettaa sudokulaudan arvon koordinaateissa coords selection_value:n arvoksi,
        ja tarkistaa jos Sudoku on sitten ratkaistu

        Args:
            coords: Ruudun koordinaatit: (x, y)
        """

        if not self.immutable[coords[1] * 9 + coords[0]]:
            self.grid[coords[1] * 9 + coords[0]] = self.selection_value

            if self.check_sudoku():
                self.completion_time = time.time() - self.time_start

                # If logged in -> update database
                if self.game and self.game.user is not None:
                    account_id = self.game.user["id"]
                    self.game.database.add_completed(
                        account_id, self.sudoku_name, self.completion_time
                    )

                self.solved = True

    def set_selection_value(self, value: int) -> None:
        """Asettaa selection_valuen arvon

        Args:
            value: Uusi arvo
        """

        self.selection_value = value

    def check_sudoku(self) -> bool:
        """Tarkistaa jos Sudoku on ratkaistu

        Returns:
            True jos on
            False jos ei ole
        """

        horizontal_rows = [self.grid[i * 9 : i * 9 + 9] for i in range(9)]
        vertical_rows = [self.grid[i : 9 * 9 + i : 9] for i in range(9)]

        for row in horizontal_rows:
            if not self.check_row(row):
                return False

        for row in vertical_rows:
            if not self.check_row(row):
                return False

        return True

    # Checks if a row has all of the numbers from 1-9
    def check_row(self, row: list) -> bool:
        """Tarkistaa jos lista arvoja sisältää kaikki arvot välillä (1-9) tasan kerran

        Returns:
            True, jos tämä pätee
            False jos ei
        """

        has_num = [False] * 9
        for num in row:
            has_num[num - 1] = True

        # This returns False, if one of has_num is False
        return min(has_num)

    def exit_to_menu(self):
        """Poistuu päävalikkoon, kutsuu peliluokan open_menu() -funktiota"""

        self.game.open_menu()
