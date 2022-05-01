CREATE TABLE IF NOT EXISTS accounts (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);

CREATE TABLE IF NOT EXISTS completions (
  id INTEGER PRIMARY KEY,
  account_id INTEGER REFERENCES accounts,
  sudoku TEXT
);