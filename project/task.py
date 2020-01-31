from database import DB


class Task:
    def __init__(self, id, title, description, deadline, state, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.state = state
        self.user_id = user_id

    # state values:
    # 0 -> to do
    # 1 -> in progress
    # 2 -> completed
    # 3 -> deleted

    # return all tasks
    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('''SELECT * FROM tasks''').fetchall()
            return [Task(*row) for row in rows]

    # create a task
    def create(self):
        with DB() as db:
            values = (self.title, self.description,
                      self.deadline, self.state, self.user_id)
            db.execute(
                '''INSERT INTO tasks (title, description, deadline, state, user_id) VALUES (?, ?, ?, ?, ?)''', values)

    # update a task
    def save(self):
        with DB() as db:
            values = (self.title, self.description, self.deadline,
                      self.state, self.user_id, self.id)
            db.execute(
                '''UPDATE tasks SET title = ?, description = ?, deadline = ?, state = ?, user_id = ? WHERE id = ?''', values)

    # find task by id
    @staticmethod
    def find_by_id(id):
        if not id:
            return None
        with DB() as db:
            row = db.execute(
                '''SELECT * FROM tasks WHERE id = ?''', (id,)).fetchone()
            if row:
                return Task(*row)

    # get all to_do tasks for a user
    def get_to_do(user_id):
        with DB() as db:
            rows = db.execute(
                '''SELECT * FROM tasks WHERE state = 0 AND user_id = ?''', (user_id,)).fetchall()
            return [Task(*row) for row in rows]

    # get all in_progress tasks for a user
    def get_in_progress(user_id):
        with DB() as db:
            rows = db.execute(
                '''SELECT * FROM tasks WHERE state = 1 AND user_id = ?''', (user_id,)).fetchall()
            return [Task(*row) for row in rows]

    # get all completed tasks for a user
    def get_completed(user_id):
        with DB() as db:
            rows = db.execute(
                '''SELECT * FROM tasks WHERE state = 2 AND user_id = ?''', (user_id,)).fetchall()
            return [Task(*row) for row in rows]

    # get all deleted tasks for a user
    def get_deleted(user_id):
        with DB() as db:
            rows = db.execute(
                '''SELECT * FROM tasks WHERE state = 3 AND user_id = ?''', (user_id,)).fetchall()
            return [Task(*row) for row in rows]

    # move a task to to_do
    def move_to_to_do(self):
        with DB() as db:
            self.state = 0
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''',
                       (self.state, self.id))

    # move a task to in_progress
    def move_to_in_progress(self):
        with DB() as db:
            self.state = 1
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''',
                       (self.state, self.id))

    # move a task to completed
    def move_to_completed(self):
        with DB() as db:
            self.state = 2
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''',
                       (self.state, self.id))

    # move a task to deleted
    def move_to_deleted(self):
        with DB() as db:
            self.state = 3
            db.execute('''UPDATE tasks SET state = ? WHERE id = ?''',
                       (self.state, self.id))
