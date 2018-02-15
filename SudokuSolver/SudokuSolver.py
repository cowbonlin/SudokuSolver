class SudokuSolver:
	def __init__(self, sudoku):
		self.sudoku = sudoku
	
	def last_digit(self):
		for box in self.sudoku.box:
			if box.remain_number() == 1:
				numbers = { i for i in range(1,10) }
				for cell in box.cells:
					if cell.value is None:
						target_cell = cell
					else:
						numbers.discard(cell.value)
				self.sudoku.fill('box', target_cell.box[0], target_cell.box[1], numbers.pop())
			
			
			
