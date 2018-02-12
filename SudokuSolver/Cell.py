class Cell:
	def __init__(self):
		self.value = None
		self.is_clue = False
		self.row = [None, None]
		self.col = [None, None]
		self.box = [None, None]
	
	def index_update(self, index):
		self.row[0] = index // 9
		self.row[1] = index % 9
		self.col[0] = index % 9
		self.col[1] = index // 9
		self.box[0] = self.row[0] // 3 * 3 + self.row[1] // 3
		self.box[1] = self.row[0] % 3 * 3 + self.row[1] % 3	
		