from SudokuSolver.Sudoku import Sudoku
from SudokuSolver.SudokuSolver import SudokuSolver

s = Sudoku()
s.load(source='test')
s.print()

solver = SudokuSolver(s)

# try:
# 	n.fill('row', 0, 1, 7)
# except Exception as e:
# 	print(e)

