class Node:
	def __init__(self, sudoku, cell=None, value=None, is_root=False):
		self.sudoku = sudoku
		self.cell = cell
		self.value = value
		self.is_root = is_root
		self.children = []
		
	def start(self):
		print("Start: {} {}".format('root' if self.is_root else self.cell.row, self.value))
		for child in self.children:
			self.test_each_child(child)
		self.sudoku.cells[self.cell.index].value = 0
		print("{} fail, row back".format(self.cell.row))
		
	def test_each_child(self, child):
		# 1. enter value
		self.sudoku.cells[child.cell.index].value = child.value
		print("{} fill child {} with value {}".format('root' if self.is_root else self.cell.row, child.cell.row, child.value))
		self.sudoku.print(child.cell.row[0], child.cell.row[1])
		
		# 2. get child's children
		result = child.get_children()
		print("{}'s children:".format(child.cell.row))
		if not child.children:
			print("\tno child")
		for c in child.children:
			print('\t', c.cell.row, c.value)
		
		# 3. check valid
		if len(child.children) == 0:
			self.sudoku.cells[child.cell.index].value = 0
			return False
		else:
			child.start()
			
	def get_children(self):
		next_index = 0 if self.is_root else self.cell.index + 1
		while self.sudoku.cells[next_index].is_clue:
			next_index += 1
			if next_index == 81:
				print("Puzzle Solved!!")
				return 'solved'
		target_cell = self.sudoku.cells[next_index]
		
		for candidate in self.sudoku.candidate_value(target_cell):
			new_node = Node(self.sudoku, target_cell, candidate)
			self.children.append(new_node)


class SudokuSolver:
	def __init__(self, sudoku):
		self.sudoku = sudoku
	
	def bfs(self):
		root_node = Node(self.sudoku, is_root=True)
		root_node.get_children()
		root_node.start()
		
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
			
			
			
