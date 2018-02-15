from SudokuSolver.Sudoku import Sudoku
from SudokuSolver.SudokuSolver import SudokuSolver

s = Sudoku()
s.load(source='test')
s.print()
# s.fill('box', 0, 0, 8)
# s.fill('box', 0, 1, 3)
# print(s.row[0][1])

solver = SudokuSolver(s)
solver.last_digit()

# try:
# 	n.fill('row', 0, 1, 7)
# except Exception as e:
# 	print(e)

