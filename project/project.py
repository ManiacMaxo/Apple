from database import DB

class Project:
    def __init__(self, id, title, owner):
        self.id = id
        self.title = title
        self.owner = owner

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('''SELECT * FROM projects''').fetchall()
            return [Project(*row) for row in rows]