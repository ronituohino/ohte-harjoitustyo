import sqlite3
import os


class Database:
    def __init__(self, mode):
        self.cwd = os.getcwd()

        # mode, 0 == production, 1 == development, 2 == test
        if mode == 0:
            self.con = sqlite3.connect(f"{self.cwd}/database/production.db")
        elif mode == 1:
            self.con = sqlite3.connect(f"{self.cwd}/database/development.db")
        else:
            self.con = sqlite3.connect(f"{self.cwd}/database/test.db")
        self.cur = self.con.cursor()
        self.create()

    def get_sql_script(self, name):
        with open(f"{self.cwd}/database/{name}", "r") as sql_file:
            sql_script = sql_file.read()
        return sql_script

    def create(self):
        sql_script = self.get_sql_script("schema.sql")
        self.cur.execute(sql_script)
        self.con.commit()

    def clear(self):
        sql_script = self.get_sql_script("clear.sql")
        self.cur.execute(sql_script)
        self.con.commit()

    def sample_data(self):
        sql_script = self.get_sql_script("sample.sql")
        self.cur.execute(sql_script)
        self.con.commit()

    def create_account(self):
        pass

    def login(self, username, password):
        pass
