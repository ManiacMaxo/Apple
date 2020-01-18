import sqlite3

DB_NAME = 'database.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS tasks
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        date TEXT,
        state INTEGER,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS projects
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        owner INTEGER,
        FOREIGN KEY(owner) REFERENCES users(id)
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS links
    (
        user_id INTEGER,
        project_id INTEGER,
        PRIMARY KEY(user_id, project_id),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(project_id) REFERENCES projects(id)
    )
''')

conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
