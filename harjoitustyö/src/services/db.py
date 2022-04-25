import sqlite3
import os
from werkzeug.security import check_password_hash, generate_password_hash


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

    def create_account(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO accounts (username, password) VALUES (:username, :password)"
            self.cur.execute(sql, {"username": username, "password": hash_value})
            self.con.commit()
        except:
            return False
        return self.login(username, password)

    def login(self, username, password):
        sql = "SELECT id, password FROM accounts WHERE username=:username"
        result = self.cur.execute(sql, {"username": username})
        account = result.fetchone()
        if not account:
            return False
        else:
            if check_password_hash(account[1], password):
                return {
                    "id": account[0],
                    "username": username,
                }
            else:
                return False
