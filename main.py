from SudokuSolver.Sudoku import Sudoku

new_puzzle = Sudoku()
new_puzzle.print()
try:
	new_puzzle.fill('rowe', 0, 0, 7)
except Exception as e:
	print(e.__doc__)
	print(e)