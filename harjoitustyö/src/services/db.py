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
        with open(f"{self.cwd}/database/{name}", "r", encoding="utf8") as sql_file:
            sql_script = sql_file.read()
        return sql_script

    def get_commands_from_script(self, script):
        commands = script.split(";")
        return commands

    def create(self):
        sql_script = self.get_sql_script("schema.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def clear(self):
        sql_script = self.get_sql_script("clear.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def sample_data(self):
        sql_script = self.get_sql_script("sample.sql")
        for command in self.get_commands_from_script(sql_script):
            self.cur.execute(command)
        self.con.commit()

    def create_account(self, username, password):
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
        sql = """SELECT sudoku, time FROM completions WHERE account_id=:account_id;"""
        result = self.cur.execute(sql, {"account_id": account_id})
        return result.fetchall()

    def add_completed(self, account_id, sudoku, time):
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
