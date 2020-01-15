from database import DB

class Task:
    def __init__(self, id, title, description, date, state, user):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.state = 0
        self.user = user

    # 0 -> to do
    # 1 -> completed
    # 2 -> deleted

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
            values = (self.title, self.description, self.date, self.state, self.user)
            db.execute('''INSERT INTO tasks (title, description, date, state, user) VALUES (?, ?, ?, ?, ?)''', values)
            return self

    def save(self):
        with DB() as db:
            values = (self.title, self.description, self.date, self.state, self.user, self.id)
            db.execute('''UPDATE tasks SET title = ?, description = ?, date = ?, state = ?, user = ? WHERE id = ?''', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('''DELETE FROM tasks WHERE id = ?''', (self.id,))

    def complete(self):
        with DB() as db:
            self.state = 1
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state,))
            
    def delete_from_tasks(self):
        with DB() as db:
            self.state = 2
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state,))