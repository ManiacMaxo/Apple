from database import DB

class Link:
	def __init__(self, user_id, task_id):
		self.user_id = user_id
		self.task_id = task_id

	def task_ids_of_user(user_id):
		with DB() as db:
			rows = db.execute('''SELECT * FROM links WHERE user_id = ?''', (user_id, )).fetchall()
			return [Link(*row).task_id for row in rows]

	def link_exists(user_id, task_id):
		with DB() as db:
			row = db.execute('''SELECT * FROM links WHERE user_id = ? AND task_id = ?''', (user_id, task_id)).fetchone()
			if(row):
				return True
			return False
