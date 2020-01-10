import hashlib

from database import DB

class Task:
    def __init__(self, id, title, description, date):
        self.id = id
        self.title = title
        self.description = description
        self.date = date

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks''').fetchall()
            return [Task(*row) for row in rows]

    @staticmethod
    def find(id):
        with DB() as db:
            row = db.execute('''SELECT * FROM tasks WHERE id = ?''',(id,)).fetchone()
            return Task(*row)

    def create(self):
        with DB() as db:
            values = (self.title, self.description, self.date)
            db.execute('''INSERT INTO tasks (title, description, date) VALUES (?, ?, ?)''', values)
            return self

    def save(self):
        with DB() as db:
            values = (self.title, self.description, self.date, self.id)
            db.execute('''UPDATE tasks SET title = ?, description = ?, date = ? WHERE id = ?''', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('''DELETE FROM tasks WHERE id = ?''', (self.id,))

    def complete(self):
        with DB() as db:
            values = (self.title, self.description, self.date)
            db.execute('''DELETE FROM tasks WHERE id = ?''', (self.id,))
            db.execute('''INSERT INTO completed (title, description, date) VALUES (?, ?, ?)''', values)

    def delete_from_tasks(self):
        with DB() as db:
            values = (self.title, self.description, self.date)
            db.execute('''DELETE FROM tasks WHERE id = ?''', (self.id,))
            db.execute('''INSERT INTO deleted (title, description, date) VALUES (?, ?, ?)''', values)

    def delete_from_completed(self):
        with DB() as db:
            values = (self.title, self.description, self.date)
            db.execute('''DELETE FROM completed WHERE id = ?''', (self.id,))
            db.execute('''INSERT INTO deleted (title, description, date) VALUES (?, ?, ?)''', values)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()