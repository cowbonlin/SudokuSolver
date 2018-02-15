from SudokuSolver.Cell import Cell

class House:
	def __init__(self, type, index, sudoku):
		self.type = type
		self.index = index
		self.sudoku = sudoku
		self.cells = list()
	
	
	def __getitem__(self, key):
		assert (0 <= key <= 8), 'invalid key value: {}'.format(key)
		return self.cells[key]
	
	
	def update(self):
		for cell in self.sudoku.cells:
			if getattr(cell, self.type)[0] == self.index:
				self.cells.append(cell)
				
				
	def remain_number(self):
		result = 0
		for cell in self.cells:
			if cell.value is None:
				result += 1
		return result