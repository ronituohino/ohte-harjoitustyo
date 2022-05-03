import sqlite3
import os
from werkzeug.security import check_password_hash, generate_password_hash


class Database:
    """Luokka, jonka avulla kommunikoidaan tietokannan kanssa

    Attributes:
        cwd: Tämänhetkinen hakemisto, os.getcwd()
        con: sqlite yhteysluokka
        cur: sqlite yhteysluokan .cursor(), jolla suoritetaan kyselyitä
    """

    def __init__(self, mode):
        """Luokan konstruktori, joka luo uuden tietokannan/muodostaa yhteyden tietokantaan

        Args:
            mode: 0=tuotantotietokanta (säilyttää tiedot),
              1=kehitystietokanta (pyyhkii tiedot sovelluksen käynnistyessä),
              2=testitietokanta (käytetään testeissä)
        """

        self.cwd = os.getcwd()

        # mode, 0 == production, 1 == development, 2 == test
        if mode == 0:
            self.con = sqlite3.connect(f"{self.cwd}/database/production.db")
        elif mode == 1:
            self.con = sqlite3.connect(f"{self.cwd}/database/development.db")
        else:
            self.con = sqlite3.connect(f"{self.cwd}/database/test.db")
        self.cur = self.con.cursor()

    def get_sql_script(self, name):
        """Lukee .sql tiedoston ja palauttaa sen tekstijonona

        Args:
            name: sql -tiedoston nimi /database -kansiossa

        Returns:
            sql -tiedoston tekstijonona
        """

        with open(f"{self.cwd}/database/{name}", "r", encoding="utf8") as sql_file:
            sql_script = sql_file.read()
        return sql_script

    def get_commands_from_script(self, script):
        """Erottelee sql -tekstijonosta komennot ; -merkin avulla

        Args:
            script: sql -tiedosto yhtenä tekstijonona

        Returns:
            Komennot tekstijonoina taulukossa
        """

        commands = script.split(";")
        return commands

    def create(self):
        """Luo tietokannan schema.sql -tiedoston mukaisesti"""

        sql_script = self.get_sql_script("schema.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def clear(self):
        """Tyhjentää tietokannan clear.sql -tiedoston mukaisesti"""

        sql_script = self.get_sql_script("clear.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def sample_data(self):
        """Täyttää tietokannan sample.sql -tiedoston mukaisesti"""

        sql_script = self.get_sql_script("sample.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def create_account(self, username, password):
        """Luo uuden käyttäjän tietokantaan

        Args:
            username: Uuden käyttäjän käyttäjänimi
            password: Uuden käyttäjän salasana tekstijonona

        Returns:
            False, jos jokin meni pieleen
            Käyttäjän tiedot, jos käyttäjän luonti onnistui
        """

        hash_value = generate_password_hash(password)
        try:
            sql = """INSERT INTO accounts (username, password) VALUES (:username, :password);"""
            self.cur.execute(
                sql, {"username": username, "password": hash_value})
            self.con.commit()
        except sqlite3.Error:
            return False
        return self.login(username, password)

    def login(self, username, password):
        """Kirjautuu käyttäjätilille

        Args:
            username: Käyttäjänimi
            password: Salasana

        Returns:
            False, jos jokin meni pieleen
            Käyttäjän tiedot, jos kirjautuminen onnistui
        """

        sql = """SELECT id, password FROM accounts WHERE username=:username;"""
        result = self.cur.execute(sql, {"username": username})
        account = result.fetchone()
        if not account:
            return False

        if check_password_hash(account[1], password):
            return {
                "id": account[0],
                "username": username,
            }

        return False

    def get_completed_data(self, account_id):
        """Hakee suoritettujen sudokuiden tiedot käyttäjällä

        Args:
            account_id: Käyttäjän ID tietokantataulukossa

        Returns:
            Suoritettujen sudokuiden tiedot muodossa [("nimi", "suoritusaika")]
        """

        sql = """SELECT sudoku, time FROM completions WHERE account_id=:account_id;"""
        result = self.cur.execute(sql, {"account_id": account_id})
        return result.fetchall()

    def add_completed(self, account_id, sudoku, time):
        """Lisää sudokusuorituksen tietokantaan

        Args:
            account_id: Käyttäjän ID tietokantataulukossa
            sudoku: Suoritetun sudokun nimi
            time: Sudokun suorittamiseen käytetty aika
        """

        try:
            sql = """INSERT INTO completions (account_id, sudoku, time)
                     VALUES (:account_id, :sudoku, :time);"""
            self.cur.execute(
                sql, {"account_id": account_id, "sudoku": sudoku, "time": time}
            )
            self.con.commit()
        except sqlite3.Error:
            return False
        return True
