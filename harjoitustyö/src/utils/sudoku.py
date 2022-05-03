import os
from os.path import isfile, join


def parse_sudoku_file(sudoku_folder_path, sudoku_name):
    """Lukee .sudoku -tiedoston ja palauttaa sen tekstijonona

    Args:
        sudoku_folder_path: Polku .sudoku -tiedostojen kansioon
        sudoku_name: Sudokun nimi kansiossa

    Returns:
        .sudoku -tiedoston tekstijonona
    """

    # Read the .sudoku file
    string = ""
    with open(
        f"{sudoku_folder_path}/{sudoku_name}.sudoku", "r", encoding="utf8"
    ) as file:
        i = 0
        for line in file:
            if i < 12:
                string += line

    # Turn the file into string of numbers
    string = string.replace("|", "")
    string = string.replace(",", "")
    string = string.replace("-", "")
    string = string.replace("\n", "")

    return string


def sudokus_in_folder(sudoku_folder_path):
    """Lukee kansion .sudoku -tiedostot

    Args:
        sudoku_folder_path: Polku kansioon

    Returns:
        Kansion .sudoku -tiedostojen nimet taulukkona
    """

    return [
        f.replace(".sudoku", "")
        for f in os.listdir(sudoku_folder_path)
        if isfile(join(sudoku_folder_path, f))
    ]
