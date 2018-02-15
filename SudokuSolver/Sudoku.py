from requests import post
from bs4 import BeautifulSoup
from SudokuSolver.Cell import Cell
from SudokuSolver.House import House

class Sudoku:
    def __init__(self):
        self.cells = list()
        self.boxes = [ House('box', i, self) for i in range(9) ]
        self.coles = [ House('col', i, self) for i in range(9) ]
        self.rowes = [ House('row', i, self) for i in range(9) ]
        for index in range(81):
            cell = Cell()
            cell.index_update(index)
            self.cells.append(cell)
    
    
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
        [ box.update() for box in self.boxes ]
        [ col.update() for col in self.coles ]
        [ row.update() for row in self.rowes ]
    
    
    def fill(self, house_type, index_grid, index_cell, digit):
        assert (house_type in ('row', 'col', 'box')), "Invalid house_type"
        assert (0 <= index_grid <= 8), "Invalid index_grid"
        assert (index_cell is None or 0 <= index_cell <= 8), "Invalid index_cell"
        
        try:
            cell = self.find_cell(house_type, index_grid, index_cell)
            self.check_request(cell, digit)
            cell.value = digit
            self.print(cell.row[0], cell.row[1])
        except ValueError as e:
            raise ValueError('invalid digit: {} in [{},{}], {}'.format(digit, cell.row[0], cell.row[1], e))
      
        
    def find_cell(self, house_type, index_grid, index_cell):
        for cell in self.cells:
            if getattr(cell, house_type) == [index_grid, index_cell]:
                return cell
        raise IndexError
    
    
    def check_request(self, cell, digit):
        for c in self.get('row', cell.row[0]):
            if digit == c.value:
                raise ValueError('row')
        for c in self.get('col', cell.col[0]):
            if digit == c.value:
                raise ValueError('col')
        for c in self.get('box', cell.box[0]):
            if digit == c.value:
                raise ValueError('box')
    
    
    def row(self, index_row, index_cell=None):
        assert (0 <= index_row <= 8 or 0 <= index_cell <= 8), "Invalid input"
        if index_cell is None:
            return self.cells[index_row * 9 : index_row * 9 + 9]
        return self.cells[index_row * 9 + index_cell]
    
    
    def col(self, index_col, index_cell=None):
        assert (0 <= index_col <= 8 or 0 <= index_cell <= 8), "Invalid input"
        result_list = list()
        for cell in self.cells:
            if cell.col[0] == index_col:
                result_list.append(cell)
        if index_cell is None:
            return result_list
        return result_list[index_cell]
    
    
    def box(self, index_box, index_cell=None):
        assert (0 <= index_box <= 8 or 0 <= index_cell <= 8), "Invalid input"
        result_list = list()
        for cell in self.cells:
            if cell.box[0] == index_box:
                result_list.append(cell)
        if index_cell is None:
            return result_list
        return result_list[index_cell]
        
    
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
