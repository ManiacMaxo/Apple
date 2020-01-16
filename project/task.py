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
    # 1 -> in progress
    # 2 -> completed
    # 3 -> deleted

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

    def get_to_do():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks WHERE state = 0''').fetchall()
            return [Task(*row) for row in rows]

    def get_in_progress():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks WHERE state = 1''').fetchall()
            return [Task(*row) for row in rows]

    def get_completed():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks WHERE state = 2''').fetchall()
            return [Task(*row) for row in rows]

    def get_deleted():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks WHERE state = 3''').fetchall()
            return [Task(*row) for row in rows]

    def move_to_to_do(self):
        with DB() as db:
            self.state = 0
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state, self.id))
            return self

    def move_to_in_progress(self):
        with DB() as db:
            self.state = 1
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state, self.id))
            return self

    def move_to_completed(self):
        with DB() as db:
            self.state = 2
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state, self.id))
            return self
            
    def move_to_deleted(self):
        with DB() as db:
            self.state = 3
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''', (self.state, self.id))
            return self