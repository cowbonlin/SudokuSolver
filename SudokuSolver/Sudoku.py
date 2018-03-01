from requests import post
from bs4 import BeautifulSoup
from SudokuSolver.Cell import Cell
from SudokuSolver.House import House

class Sudoku:
    def __init__(self):
        self.cells = [ Cell(index) for index in range(81) ]
        self.box = [ House('box', i, self) for i in range(9) ]
        self.col = [ House('col', i, self) for i in range(9) ]
        self.row = [ House('row', i, self) for i in range(9) ]
    
    
    def load(self, source='internet'):
        if source == 'internet':
            page = post("http://www.sudokuweb.org/", data={"sign2":"9x9"}).text
            soup = BeautifulSoup(page, 'html.parser')
            for index, td in enumerate(soup.find_all('td')):
                if td.span['class'][0] == 'sedy':
                    self.cells.append(int(td.span.text))
                else:
                    self.cells.append(0)
        elif source == 'test':
            testing_data = [0, 0, 0, 0, 0, 0, 7, 2, 1, 0, 6, 0, 5, 0, 0, 9, 4, 3, 4, 2, 0, 0, 1, 0, 0, 8, 5, 5, 0, 4, 7, 8, 0, 0, 6, 0, 0, 8, 6, 0, 4, 0, 0, 0, 7, 0, 7, 2, 6, 9, 0, 0, 0, 8, 2, 0, 3, 8, 7, 6, 5, 0, 0, 6, 9, 0, 0, 0, 1, 8, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0]
            for index, (cell, data) in enumerate(zip(self.cells, testing_data)):
                if data != 0:
                    cell.value = data
                    cell.is_clue = True
        [ box.update() for box in self.box ]
        [ col.update() for col in self.col ]
        [ row.update() for row in self.row ]
    
    
    def fill(self, house_type, index_grid, index_cell, digit):
        assert (house_type in ('row', 'col', 'box')), "Invalid house_type"
        assert (0 <= index_grid <= 8), "Invalid index_grid"
        assert (index_cell is None or 0 <= index_cell <= 8), "Invalid index_cell"
        
        cell = getattr(self, house_type)[index_grid][index_cell]
        self.check_fill(cell, digit)
        cell.value = digit
        self.print(cell.row[0], cell.row[1])
    
    
    def candidate_value(self, cell):
        candidates = { i for i in range(1, 10) }
        for c in self.box[cell.box[0]]:
            candidates.discard(c.value)
        for c in self.row[cell.row[0]]:
            candidates.discard(c.value)
        for c in self.col[cell.col[0]]:
            candidates.discard(c.value)
        return candidates
        
    
    def check_fill(self, cell, digit):
        for c in self.row[cell.row[0]].cells:
            if digit == c.value:
                raise ValueError('Invalid Input: row[{}][{}] with number {}'.format(c.row[0], c.row[1], c.value))
        for c in self.col[cell.col[0]].cells:
            if digit == c.value:
                raise ValueError('Invalid Input: col[{}][{}] with number {}'.format(c.col[0], c.col[1], c.value))
        for c in self.box[cell.box[0]].cells:
            if digit == c.value:
                raise ValueError('Invalid Input: box[{}][{}] with number {}'.format(c.box[0], c.box[1], c.value))
        
    
    def print(self, row=None, col=None):
        print(' ' * ((col//3)*8+2 + (col%3)*2+1 + 1) + "*" if col is not None else '')
        print("  -------------------------\n" ,end='')
        print("* " if row == 0 else "  ", end='')
        
        for index, cell in enumerate(self.cells):
            if index % 9 == 0:
                print("|" ,end=' ')
            
            print(cell.value or "_", end=' ')
            
            if index % 3 == 2:
                print("|", end=' ')
            
            if index % 9 == 8:
                print()
            
            if index % 27 == 26:
                print("  -------------------------")
            
            if row and index % 9 == 8 and index // 9 == row-1 :
                print("* ", end='')
            elif index % 9 == 8:
                print("  ", end='')
        print()
