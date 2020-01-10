import sqlite3

DB_NAME = 'example.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS tasks
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
        desciption TEXT
        date TEXT
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS completed
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
        desciption TEXT
        date TEXT
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS deleted
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
        desciption TEXT
        date TEXT
    )
''')

conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()