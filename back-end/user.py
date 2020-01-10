import hashlib

from database import DB

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def create(self):
        with DB() as db:
            values = (self.username, self.password)
            db.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', values)
            return self

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()