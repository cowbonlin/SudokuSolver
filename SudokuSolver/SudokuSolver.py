class SudokuSolver:
	def __init__(self, sudoku):
		self.sudoku = sudoku
	
	def lastDigit(self):
		# for box in self.sudoku.rowes (generator?)
		for i in range(9):
			pass