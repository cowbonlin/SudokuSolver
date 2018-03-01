from SudokuSolver.Sudoku import Sudoku
from SudokuSolver.SudokuSolver import SudokuSolver
from time import clock


s = Sudoku()
load_start_time = clock()
print('loading...')
s.load(source='test')
load_end_time = clock()
s.print()

solve_start_time = clock()
solver = SudokuSolver(s)
solver.bfs()
solve_end_time = clock()

print('load  time:', round(load_end_time-load_start_time, 4))
print('solve time:', round(solve_end_time-solve_start_time, 4))
