from SudokuSolver.Sudoku import Sudoku
from SudokuSolver.SudokuSolver import SudokuSolver

s = Sudoku()
s.load(source='test')
print(s.rowes[1][8])
print(s.rowes[1][6])
print(s.boxes[8][6])
print(s.coles[3].cells)

s.print()

solver = SudokuSolver(s)
# solver.lastDigit()

# try:
# 	n.fill('row', 0, 1, 7)
# except Exception as e:
# 	print(e)

