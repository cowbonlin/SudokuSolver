class Cell:
	def __init__(self, index):
		self.value = None
		self.is_clue = False
		self.row = [index//9, index%9]
		self.col = [index%9, index//9]
		self.box = [self.row[0]//3*3 + self.row[1]//3, \
					self.row[0] %3*3 + self.row[1] %3 ]
	
	def __repr__(self):
		return "<Cell [{},{}]={}>".format(self.row[0], self.row[1], self.value)