from SudokuSolver.Sudoku import Sudoku
from SudokuSolver.SudokuSolver import SudokuSolver


s = Sudoku()
s.load(source='test')
s.print()

solver = SudokuSolver(s)
solver.bfs()
# solver.last_digit()



